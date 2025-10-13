# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "the sky is blue") == "blue is sky the"
    assert candidate(s = "  hello world  ") == "world hello"
    assert candidate(s = "a good   example") == "example good a"
