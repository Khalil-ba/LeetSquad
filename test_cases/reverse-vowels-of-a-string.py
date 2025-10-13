# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "hello") == "holle"
    assert candidate(s = "leetcode") == "leotcede"
