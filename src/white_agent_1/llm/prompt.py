"""
Provider-agnostic prompt engineering
"""
from typing import Dict, Any, List
from abc import ABC, abstractmethod


class PromptTemplate:
    """Universal template for LeetCode problems"""
    
    SYSTEM_PROMPT = """You are an expert software engineer specializing in algorithm optimization and clean code.
Your task is to solve LeetCode problems with optimal solutions.

Always provide:
1. Clean, well-commented code
2. Clear explanation of your approach
3. Time complexity analysis
4. Space complexity analysis

Format your response as:
```python
# Your solution code here
```

Explanation: [Your explanation]
Time Complexity: O(...)
Space Complexity: O(...)
"""

    @staticmethod
    def format_problem(problem: Dict[str, Any]) -> str:
        """
        Format a LeetCode problem into a prompt
        """
        tags_str = ", ".join(problem.get('tags', []))
        
        prompt = f"""
## Problem: {problem['task_id']} - {problem.get('difficulty', 'Unknown')}
**Topics:** {tags_str}

### Problem Description:
{problem['problem_description']}

### Starter Code:
```python
{problem.get('starter_code', '# No starter code provided')}
```

Please provide an optimal solution with explanation and complexity analysis.
"""
        return prompt.strip()


class PromptEngineer:
    """
    Provider-agnostic prompt engineering
    NO PROVIDER-SPECIFIC CODE HERE
    """
    
    def __init__(self, include_hints: bool = False):
        self.include_hints = include_hints
    
    def create_prompt(self, problem: Dict[str, Any]) -> Dict[str, str]:
        """
        Create GENERIC prompt structure
        
        Returns:
            Dict with 'system' and 'user' messages (universal format)
        """
        system_message = self._build_system_message(problem)
        user_message = self._build_user_message(problem)
        
        return {
            'system': system_message,
            'user': user_message
        }
    
    def _build_system_message(self, problem: Dict[str, Any]) -> str:
        """Build system prompt with context"""
        base_system = PromptTemplate.SYSTEM_PROMPT
        
        # Add difficulty-specific guidance
        difficulty = problem.get('difficulty', 'Medium')
        if difficulty == 'Easy':
            guidance = "\nFocus on clarity and correctness. Simple, readable solutions are preferred."
        elif difficulty == 'Hard':
            guidance = "\nThis is a challenging problem. Consider advanced data structures and algorithms."
        else:
            guidance = "\nBalance between efficiency and readability."
        
        return base_system + guidance
    
    def _build_user_message(self, problem: Dict[str, Any]) -> str:
        """Build user prompt with problem details"""
        base_prompt = PromptTemplate.format_problem(problem)
        
        if self.include_hints and 'tags' in problem:
            hints = self._generate_hints(problem['tags'])
            if hints:
                base_prompt += f"\n\n### Hints:\n{hints}"
        
        return base_prompt
    
    def _generate_hints(self, tags: List[str]) -> str:
        """Generate algorithmic hints based on problem tags"""
        hint_map = {
            'Array': '- Consider two-pointer or sliding window techniques',
            'Hash Table': '- A hash map can provide O(1) lookup time',
            'Dynamic Programming': '- Look for overlapping subproblems',
            'Binary Search': '- Can you eliminate half the search space?',
            'Tree': '- Consider recursion or iterative traversal',
            'Graph': '- Think about graph traversal algorithms',
        }
        
        hints = [hint_map.get(tag) for tag in tags if tag in hint_map]
        return '\n'.join(hints) if hints else ''