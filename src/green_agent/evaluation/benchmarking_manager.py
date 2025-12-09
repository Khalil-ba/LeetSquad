import csv
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional

from .accuracy_check import str_to_func, test_accuracy
from .llm_judge import LLMJudge

logger = logging.getLogger(__name__)


class BenchmarkingManager:
    """
    Manages benchmarking workflow including dataset loading, agent registration,
    progress tracking, problem distribution, and result evaluation.

    Designed with in-memory storage that can be easily replaced with
    persistent storage later.
    """

    def __init__(
        self,
        csv_path: str = "dataset/LeetCodeQuestions.csv",
        llm_judge_model: Optional[str] = None,
        llm_provider: Optional[str] = None,
        skip_tests: bool = False,
        skip_llm_judge: bool = False,
        limit_problems: Optional[int] = None,
    ):
        """
        Initialize the benchmarking manager.

        Args:
            csv_path: Path to the LeetCode questions CSV file
            model: Model ID to use for LLM judge
            skip_tests: Skip running test cases
            skip_llm_judge: Skip LLM judgement
            limit_problems: Only load the specified number of problems
        """
        self.csv_path = csv_path
        self.skip_tests = skip_tests
        self.skip_llm_judge = skip_llm_judge

        # Initialize LLM judge if needed
        self.judge = (
            LLMJudge(provider=llm_provider, model_id=llm_judge_model, verbose=False)
            if not skip_llm_judge
            else None
        )
        # adjust based on LLM quota - higher number allows more parallel calls
        self.eval_executor = ThreadPoolExecutor(max_workers=3)

        # In-memory storage (designed for easy migration to DB)
        self._agents: Dict[str, str] = {}  # agent_id -> agent_name
        self._progress: Dict[str, int] = {}  # agent_id -> current_index
        self._pending: Dict[str, str] = {}  # agent_id -> pending_task_id
        self._results: Dict[str, Dict[str, Dict]] = {}  # agent_id -> {task_id -> scores}
        self._detailed_results: Dict[str, Dict[str, Dict]] = {}  # detailed LLM results
        self._dataset: List[Dict] = []  # loaded problems

        # Load dataset
        self._load_dataset(limit_problems)

        # Log args
        logger.info(
            "Initialized BenchmarkingManager with following args: "
            f"csv_path={csv_path}, "
            f"llm_judge_model={llm_judge_model}, "
            f"skip_tests={skip_tests}, "
            f"skip_llm_judge={skip_llm_judge}, "
            f"limit_problems={limit_problems}"
        )

    def _load_dataset(self, limit_problems: Optional[int]) -> None:
        """
        Load the dataset from CSV file.

        Args:
            limit_problems: Only load the specified number of problems
        """
        try:
            with open(self.csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if not row.get("task_id"):
                        logger.warning("Encountered invalid row, skipping...")
                        continue
                    self._dataset.append(
                        {
                            "task_id": row["task_id"],
                            "problem_description": row.get("problem_description", ""),
                            "starter_code": row.get("starter_code", ""),
                            "entry_point": row.get("entry_point", ""),
                            "query": row.get("query", ""),
                            "difficulty": row.get("difficulty", "Medium"),
                            "optimal_time_complexity": row.get("optimal_time_complexity", ""),
                            "optimal_space_complexity": row.get("optimal_space_complexity", ""),
                        }
                    )
                    if limit_problems and len(self._dataset) >= limit_problems:
                        break
            logger.info(f"Loaded {len(self._dataset)} problems from {self.csv_path}")
        except FileNotFoundError:
            logger.error(f"Dataset CSV file not found: {self.csv_path}")
            raise
    
    def _get_problem_by_task_id(self, task_id: str) -> Optional[Dict]:
        """Get problem data by task_id."""
        for problem in self._dataset:
            if problem["task_id"] == task_id:
                return problem
        return None
    
    def _calculate_complexity_score(
        self, achieved: Optional[int], optimal_str: str, complexity_type: str = "time"
    ) -> Dict:
        """
        Calculate complexity score comparing achieved vs optimal.
        
        Scoring:
        - Optimal or better: 100 points + bonus for beating optimal
        - Within 1 level: 80 points
        - Within 2 levels: 60 points
        - Within 3 levels: 40 points
        - Worse: 20 points
        - No data: 0 points
        
        Returns dict with score, achieved, optimal, and comparison status.
        """
        from .utils.complexity import Complexity
        
        result = {
            "score": 0,
            "achieved": None,
            "optimal": optimal_str or "Unknown",
            "status": "unknown",  # optimal, better, close, suboptimal, poor
        }
        
        if achieved is None:
            return result
        
        result["achieved"] = str(Complexity(achieved)) if achieved in [c.value for c in Complexity] else f"Level {achieved}"
        
        # Try to parse optimal complexity
        optimal_num = None
        if optimal_str:
            try:
                optimal_num = int(Complexity.from_string(optimal_str))
            except (KeyError, ValueError):
                # Try common variations
                variations = {
                    "O(n)": "O(n)", "O(1)": "O(1)", "O(log n)": "O(log n)",
                    "O(n log n)": "O(n log n)", "O(n^2)": "O(n^2)",
                    "O(n²)": "O(n^2)", "O(logn)": "O(log n)",
                }
                normalized = variations.get(optimal_str.replace(" ", ""))
                if normalized:
                    try:
                        optimal_num = int(Complexity.from_string(normalized))
                    except (KeyError, ValueError):
                        pass
        
        if optimal_num is None:
            # Can't compare, give partial credit for having a solution
            result["score"] = 50
            result["status"] = "unknown"
            return result
        
        # Compare: higher enum value = better complexity
        diff = achieved - optimal_num
        
        if diff >= 0:
            # Achieved is same or better than optimal
            result["score"] = 100 + (diff * 10)  # Bonus for beating optimal
            result["status"] = "optimal" if diff == 0 else "better"
        elif diff == -1:
            result["score"] = 80
            result["status"] = "close"
        elif diff == -2:
            result["score"] = 60
            result["status"] = "suboptimal"
        elif diff == -3:
            result["score"] = 40
            result["status"] = "suboptimal"
        else:
            result["score"] = 20
            result["status"] = "poor"
        
        return result

    def register_agent(self, agent_id: str, agent_name: str) -> None:
        """
        Register an agent and initialize their progress tracking.

        Args:
            agent_id: Unique agent identifier
            agent_name: Agent name
        """
        self._agents[agent_id] = agent_name
        self._progress[agent_id] = 0
        self._results[agent_id] = {}
        self._detailed_results[agent_id] = {}
        logger.info(f"Registered agent: {agent_name} (ID: {agent_id})")

    def is_registered(self, agent_id: str) -> bool:
        """
        Check if an agent is registered.

        Args:
            agent_id: Agent identifier

        Returns:
            True if agent is registered, False otherwise
        """
        return agent_id in self._agents

    def validate_agent(self, agent_id: str, agent_name: str) -> bool:
        """
        Validate agent credentials (ID and name for now).

        Args:
            agent_id: Agent identifier
            agent_name: Agent name

        Returns:
            True if credentials are valid, False otherwise
        """
        return self.is_registered(agent_id) and self._agents[agent_id] == agent_name

    def get_next_problem(self, agent_id: str) -> Dict:
        """
        Get the next problem for an agent.

        Args:
            agent_id: Agent identifier

        Returns:
            Dict with problem details

        Raises:
            ValueError: If client-side error (e.g. has a pending problem,
            reached end of dataset, not registered, etc.)
        """
        if not self.is_registered(agent_id):
            raise ValueError("Agent not registered")

        # Check if agent has a pending problem
        if agent_id in self._pending:
            raise ValueError("Problem already distributed. Please submit answer first.")

        # Get current progress
        current_idx = self._progress[agent_id]

        # Check if agent has completed all problems
        if current_idx >= len(self._dataset):
            return {
                "message": "You have completed all problems. No more problems available."
            }

        # Get the next problem
        problem = self._dataset[current_idx]

        # Mark as pending
        self._pending[agent_id] = problem["task_id"]

        logger.info(f"Distributed problem {problem['task_id']} to agent {agent_id}")

        return {
            "problem_description": problem["problem_description"],
            "starter_code": problem["starter_code"],
            "entry_point": problem["entry_point"],
        }

    def submit_answer(self, agent_id: str, agent_name: str, solution: str) -> None:
        """
        Receive a solution and advance agent progress.
        Start an asynchronous eval progress.

        Args:
            agent_id: Agent identifier
            agent_name: Agent name
            solution: Code solution to evaluate

        Raises:
            ValueError: If agent not registered, credentials invalid,
                       or no pending problem
        """
        if not self.is_registered(agent_id):
            raise ValueError("Agent not registered")

        if not self.validate_agent(agent_id, agent_name):
            raise ValueError("Agent name does not match ID")

        if agent_id not in self._pending:
            raise ValueError("No pending problem to submit answer for")

        # Get the pending task
        task_id = self._pending[agent_id]

        # Start eval process asynchronously (not blocking networking call)
        self.eval_executor.submit(self._evaluate_answer, agent_id, task_id, solution)

        # Clear pending and advance progress
        del self._pending[agent_id]
        self._progress[agent_id] += 1

        logger.info(f"Received solution for task {task_id} from agent {agent_id}")

    def _evaluate_answer(self, agent_id: str, task_id: str, solution: str) -> None:
        """
        Evaluate a solution and stores the results.

        Args:
            agent_id: Agent identifier
            task_id: Task identifier
            solution: Code solution to evaluate
        """
        # Get problem data for optimal complexity comparison
        problem = self._get_problem_by_task_id(task_id)
        optimal_time = problem.get("optimal_time_complexity", "") if problem else ""
        optimal_space = problem.get("optimal_space_complexity", "") if problem else ""
        difficulty = problem.get("difficulty", "Medium") if problem else "Medium"
        
        # Difficulty multiplier for scoring
        difficulty_multiplier = {"Easy": 1.0, "Medium": 1.5, "Hard": 2.0}.get(difficulty, 1.0)
        
        # Evaluate the solution
        tests_percent = None
        time_complexity_num = None
        space_complexity_num = None
        readability_overall = None
        if task_id not in self._detailed_results[agent_id]:
            self._detailed_results[agent_id][task_id] = {}

        # Run test cases
        if not self.skip_tests:
            try:
                soln_func = str_to_func(solution)
                passed, total, accuracy = test_accuracy(task_id, soln_func)
                tests_percent = (
                    round(float(accuracy), 1) if accuracy is not None else None
                )
                self._detailed_results[agent_id][task_id]["accuracy"] = {
                    "passed": passed,
                    "total": total,
                }
            except Exception as e:
                logger.error(
                    f"[async] Error testing accuracy for {agent_id}:{task_id}: {e}"
                )

        # Run LLM judge analysis
        if not self.skip_llm_judge and self.judge is not None:
            try:
                complexity = self.judge.analyze_complexity(solution)
                readability = self.judge.analyze_readability(solution)

                time_complexity_num = int(complexity["time"]["complexity_enum"])
                space_complexity_num = int(complexity["space"]["complexity_enum"])
                readability_overall = int(readability.get("overall", 0))

                self._detailed_results[agent_id][task_id]["complexity"] = complexity
                self._detailed_results[agent_id][task_id]["readability"] = readability
            except Exception as e:
                logger.error(
                    f"[async] Error in LLM analysis for {agent_id}:{task_id}: {e}"
                )

        # Calculate complexity scores against optimal
        time_score_data = self._calculate_complexity_score(time_complexity_num, optimal_time, "time")
        space_score_data = self._calculate_complexity_score(space_complexity_num, optimal_space, "space")
        
        # Calculate total problem score
        # Correctness: 40% weight (max 100 points)
        correctness_score = tests_percent if tests_percent is not None else 0
        
        # Time complexity: 30% weight (max 100+ points with bonus)
        time_score = time_score_data["score"]
        
        # Space complexity: 15% weight (max 100+ points with bonus)
        space_score = space_score_data["score"]
        
        # Readability: 15% weight (max 12 points -> normalized to 100)
        readability_score = (readability_overall / 12 * 100) if readability_overall else 0
        
        # Weighted total (before difficulty multiplier)
        weighted_score = (
            correctness_score * 0.40 +
            time_score * 0.30 +
            space_score * 0.15 +
            readability_score * 0.15
        )
        
        # Apply difficulty multiplier for final score
        final_score = round(weighted_score * difficulty_multiplier, 1)

        # Store results
        results = {
            "tests_percent": tests_percent,
            "time_complexity": time_complexity_num,
            "space_complexity": space_complexity_num,
            "readability_overall": readability_overall,
            # New scoring fields
            "difficulty": difficulty,
            "time_score": time_score_data,
            "space_score": space_score_data,
            "correctness_score": correctness_score,
            "readability_score": round(readability_score, 1),
            "weighted_score": round(weighted_score, 1),
            "final_score": final_score,
        }
        self._results[agent_id][task_id] = results
        logger.info(
            f"[async] Evaluated solution for task {task_id} from agent {agent_id} ({self._agents[agent_id]}). "
            f"Final Score: {final_score} | Correctness: {correctness_score}% | "
            f"Time: {time_score_data['status']} ({time_score}) | Space: {space_score_data['status']} ({space_score})"
        )

    # Aggregate results for all agents and overall summary
    def report_results(self) -> Dict:
        """Return aggregated benchmarking results with leaderboard across all registered agents.

        Structure:
        {
          "leaderboard": [
              {
                  "rank": <int>,
                  "agent_id": <str>,
                  "name": <str>,
                  "total_score": <float>,
                  "problems_solved": <int>,
                  "problems_attempted": <int>,
                  "optimal_solutions": <int>,
                  "better_than_optimal": <int>,
              },
              ...
          ],
          "agents": {
             "<agent_id>": {
                 "name": "<agent_name>",
                 "problems_attempted": <int>,
                 "total_score": <float>,
                 "scores_breakdown": {
                     "correctness": { "total": <float>, "avg": <float> },
                     "time_complexity": { "optimal": <int>, "better": <int>, "close": <int>, "suboptimal": <int>, "poor": <int> },
                     "space_complexity": { "optimal": <int>, "better": <int>, "close": <int>, "suboptimal": <int>, "poor": <int> },
                     "readability": { "total": <float>, "avg": <float> }
                 },
                 "by_difficulty": {
                     "Easy": { "attempted": <int>, "score": <float> },
                     "Medium": { "attempted": <int>, "score": <float> },
                     "Hard": { "attempted": <int>, "score": <float> }
                 },
                 "tests": {
                     "total_passed": <int>,
                     "total": <int>,
                     "percent": <float|null>
                 }
             },
             ...
          }
        }
        """
        agents_summary: Dict[str, Dict] = {}
        leaderboard_data: List[Dict] = []

        for agent_id, task_results in self._results.items():
            agent_name = self._agents.get(agent_id, agent_id)

            total_score = 0.0
            total_passed = 0
            total_tests = 0
            correctness_total = 0.0
            readability_total = 0.0
            
            # Complexity status counters
            time_status_counts = {"optimal": 0, "better": 0, "close": 0, "suboptimal": 0, "poor": 0, "unknown": 0}
            space_status_counts = {"optimal": 0, "better": 0, "close": 0, "suboptimal": 0, "poor": 0, "unknown": 0}
            
            # By difficulty tracking (score = final_score with multiplier, raw_score = before multiplier)
            by_difficulty = {
                "Easy": {"attempted": 0, "score": 0.0, "raw_score": 0.0},
                "Medium": {"attempted": 0, "score": 0.0, "raw_score": 0.0},
                "Hard": {"attempted": 0, "score": 0.0, "raw_score": 0.0},
            }

            # Pull accuracy details from detailed results if available
            detailed = self._detailed_results.get(agent_id, {})
            
            # Track raw weighted scores (before difficulty multiplier)
            raw_weighted_score_total = 0.0

            for task_id, scores in task_results.items():
                # Accumulate final scores
                final_score = scores.get("final_score", 0)
                total_score += final_score
                
                # Accumulate raw weighted scores (before difficulty multiplier)
                raw_weighted_score_total += scores.get("weighted_score", 0)
                
                # Correctness
                correctness = scores.get("correctness_score", 0)
                correctness_total += correctness
                
                # Readability
                readability = scores.get("readability_score", 0)
                readability_total += readability
                
                # Time complexity status
                time_score_data = scores.get("time_score", {})
                time_status = time_score_data.get("status", "unknown")
                if time_status in time_status_counts:
                    time_status_counts[time_status] += 1
                
                # Space complexity status
                space_score_data = scores.get("space_score", {})
                space_status = space_score_data.get("status", "unknown")
                if space_status in space_status_counts:
                    space_status_counts[space_status] += 1
                
                # By difficulty
                difficulty = scores.get("difficulty", "Medium")
                if difficulty in by_difficulty:
                    by_difficulty[difficulty]["attempted"] += 1
                    by_difficulty[difficulty]["score"] += final_score
                    by_difficulty[difficulty]["raw_score"] += scores.get("weighted_score", 0)

                # Sum passed/total when recorded in detailed results
                acc = detailed.get(task_id, {}).get("accuracy", {})
                p = acc.get("passed")
                t = acc.get("total")
                if isinstance(p, int) and isinstance(t, int):
                    total_passed += p
                    total_tests += t

            # Build per-agent summary
            problems_attempted = len(task_results)
            optimal_count = time_status_counts["optimal"] + time_status_counts["better"]
            better_count = time_status_counts["better"]
            
            # raw_avg_score: average of weighted_score (before difficulty multiplier)
            raw_avg_score = round(raw_weighted_score_total / problems_attempted, 1) if problems_attempted > 0 else 0
            
            # weighted_avg_score: average of final_score (with difficulty multiplier already applied)
            weighted_avg_score = round(total_score / problems_attempted, 1) if problems_attempted > 0 else 0
            
            agents_summary[agent_id] = {
                "name": agent_name,
                "problems_attempted": problems_attempted,
                "total_score": round(total_score, 1),
                "raw_avg_score": raw_avg_score,
                "weighted_avg_score": weighted_avg_score,
                "scores_breakdown": {
                    "correctness": {
                        "total": round(correctness_total, 1),
                        "avg": round(correctness_total / problems_attempted, 1) if problems_attempted > 0 else 0,
                    },
                    "time_complexity": time_status_counts,
                    "space_complexity": space_status_counts,
                    "readability": {
                        "total": round(readability_total, 1),
                        "avg": round(readability_total / problems_attempted, 1) if problems_attempted > 0 else 0,
                    },
                },
                "by_difficulty": {
                    diff: {
                        "attempted": data["attempted"],
                        "score": round(data["score"], 1),
                        "raw_avg_score": round(data["raw_score"] / data["attempted"], 1) if data["attempted"] > 0 else 0,
                        "weighted_avg_score": round(data["score"] / data["attempted"], 1) if data["attempted"] > 0 else 0,
                    }
                    for diff, data in by_difficulty.items()
                },
                "tests": {
                    "total_passed": total_passed,
                    "total": total_tests,
                    "percent": round(100.0 * total_passed / total_tests, 1) if total_tests > 0 else None,
                },
            }
            
            # Add to leaderboard data
            leaderboard_data.append({
                "agent_id": agent_id,
                "name": agent_name,
                "total_score": round(total_score, 1),
                "raw_avg_score": raw_avg_score,
                "weighted_avg_score": weighted_avg_score,
                "problems_attempted": problems_attempted,
                "problems_with_100_percent": sum(1 for s in task_results.values() if s.get("tests_percent") == 100),
                "optimal_solutions": optimal_count,
                "better_than_optimal": better_count,
                "test_pass_rate": round(100.0 * total_passed / total_tests, 1) if total_tests > 0 else 0,
            })

        # Sort leaderboard by total_score descending
        leaderboard_data.sort(key=lambda x: (-x["total_score"], -x["optimal_solutions"], x["name"]))
        
        # Add ranks
        leaderboard = []
        for rank, entry in enumerate(leaderboard_data, 1):
            leaderboard.append({"rank": rank, **entry})

        return {
            "leaderboard": leaderboard,
            "agents": agents_summary,
        }
