import json
import logging
import textwrap

from ..aws import BedrockClient
from .utils.complexity import Complexity

logger = logging.getLogger(__name__)


class LLMJudge:
    """
    This class uses an LLM (via Bedrock) to analyze generated code.
    """

    COMPLEXITY_PROMPT = textwrap.dedent(
        """
        You are "ComplexityJudge", an expert in code analyst. Your job is to evaluate
        the TIME and SPACE complexity of a given Python code snippet.

        Rules:
        - Identify the main algorithmic idea and key data structures.
        - Analyze the worst-case time and space complexity by default. Only use average
            complexity for certain data structures that make sense to do so. For
            example, you can use O(1) as the time complexity for hash tables.
        - Write complexity in Big-O notation. Use the letter n as default input size.
            Valid values are: `O(1)`, `O(log n)`, `O(√n)`, `O(n)`, `O(n log n)`, `O(n^2)`,
            `O(n^3)`, `O(2^n)`, `O(n!)`.
        - If there are more than one input size (e.g. m and n), drop the non-dominant
            one and write complexity in terms of n only.
        - Include a one-sentence justification for your conclusion.

        Your output MUST be a valid JSON object of the following format. Do not include
        additional sentences.
        {
            "time": {
                "complexity": "<e.g. O(n)>",
                "justification": "<e.g. the code traverses input array exactly twice>"
            },
            "space": {
                "complexity": "<e.g. O(n)>",
                "justification": "<e.g. the code uses an auxiliary array of length n>"
            }
        }

        Input Python Code:
        """
    )

    READABILITY_PROMPT = textwrap.dedent(
        """
        You are a code readability judge. Evaluate only the readability of the following
        Python snippet. Do NOT deduct points for brute force.

        Each of the following category is worth 3 points. Score each category and give a
        concise one-line justification for your score in each category.

        1. Naming
        How well do names (variables, helpers) convey purpose relative to the problem
        domain? Are loop indices and intermediate states meaningfully named? Are magic
        numbers avoided or named?

        2. Structure
        Is the structure easy to follow? Is the solution decomposed into understandable
        blocks if needed? Are there early returns/guards if helpful?

        3. Idiomatic
        Appropriate, readable use of Python features (e.g., tuple unpacking,
        list/dict/set comps when they improve clarity, slicing, any/all). Avoids obscure
        tricks and overly dense one-liners.

        4. Comment
        Brief, high-value comments around non-obvious steps or edge-case handling.
        Avoids noisy or redundant comments. The participant does not need a comment to
        describe the overall function behavior.

        Your output MUST be a valid JSON object of the following format. Do not include
        additional sentences.
        {
            "naming": {
                "score": <int>,
                "justification": <str>
            },
            "structure": {
                "score": <int>,
                "justification": <str>
            },
            "idiomatic": {
                "score": <int>,
                "justification": <str>
            },
            "comment": {
                "score": <int>,
                "justification": <str>
            }
        }

        Input code:
        """
    )

    def __init__(self, model_id=None, verbose=False):
        """
        Initializes LLM Judge.

        Args:
            model_id: Bedrock model ID. Use None for default.
            verbose: if True, allow one retry for bad LLM output.
        """
        self.llm_client = BedrockClient(model_id=model_id)
        self.verbose = verbose

    def analyze_complexity(self, code: str) -> dict:
        """
        Returns the time & space complexity in a tuple. See Complexity enum class for
        valid complexity values.

        Output dict format:
        {
            "time": {
                "complexity": "<e.g. O(n)>",
                "complexity_enum": <e.g. Complexity.LINEAR>,
                "justification": "<e.g. the code traverses input array exactly twice>"
            },
            "space": {
                "complexity": "<e.g. O(n)>",
                "complexity_enum": <e.g. Complexity.LINEAR>,
                "justification": "<e.g. the code uses an auxiliary array of length n>"
            }
        }
        """

        # validates LLM output and transforms it to dict
        def transform_llm_output(response):
            try:
                data = json.loads(response)
                if not isinstance(data, dict) or set(data.keys()) != {"time", "space"}:
                    return None
                for section in ("time", "space"):
                    obj = data.get(section)
                    if not isinstance(obj, dict) or set(obj.keys()) != {
                        "complexity",
                        "justification",
                    }:
                        return None
                    comp = obj.get("complexity")
                    obj["complexity_enum"] = Complexity.from_string(comp)
                return data
            except json.JSONDecodeError:
                return None

        # prompt the LLM and parse response into a dict
        response = self.llm_client.generate(self.COMPLEXITY_PROMPT, code)
        validated = transform_llm_output(response)

        # allow one retry if the LLM output is invalid
        if validated is None and self.verbose:
            logger.info("Received invalid response:")
            logger.info(response)
            logger.info("Retrying LLM generation...")
            response = self.llm_client.generate(self.COMPLEXITY_PROMPT, code)
            validated = transform_llm_output(response)
            if validated is None:
                raise Exception("LLM failed to generate valid time & space complexities")

        return validated

    def analyze_readability(self, code: str) -> dict:
        """
        Returns the readability scores.

        Output dict format:
        {
            "naming": {"score": <int>, "justification": <str>},
            "structure": {"score": <int>, "justification": <str>},
            "idiomatic": {"score": <int>, "justification": <str>},
            "comment": {"score": <int>, "justification": <str>},
            "overall": <int>
        }
        """

        # validates LLM output and transforms it to dict
        def transform_llm_output(response):
            try:
                data = json.loads(response)
                if not isinstance(data, dict):
                    return None
                if set(data.keys()) != {
                    "naming",
                    "structure",
                    "idiomatic",
                    "comment",
                }:
                    return None
                overall_score = 0
                for section in (
                    "naming",
                    "structure",
                    "idiomatic",
                    "comment",
                ):
                    obj = data.get(section)
                    if not isinstance(obj, dict) or set(obj.keys()) != {
                        "score",
                        "justification",
                    }:
                        return None
                    score = obj.get("score")
                    if score < 0 or score > 3:
                        return None
                    overall_score += score
                data["overall"] = overall_score
                return data
            except json.JSONDecodeError:
                return None

        # prompt the LLM and parse response into a dict
        response = self.llm_client.generate(self.READABILITY_PROMPT, code)
        validated = transform_llm_output(response)

        # allow one retry if the LLM output is invalid
        if validated is None and self.verbose:
            logger.info("Received invalid response:")
            logger.info(response)
            logger.info("Retrying LLM generation...")
            response = self.llm_client.generate(self.READABILITY_PROMPT, code)
            validated = transform_llm_output(response)
            if validated is None:
                raise Exception("LLM failed to generate valid readability scores")

        return validated
