# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 1,categoryHandler = [1]) == 1
