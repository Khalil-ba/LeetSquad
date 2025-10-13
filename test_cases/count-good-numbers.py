# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 1) == 5
    assert candidate(n = 4) == 400
    assert candidate(n = 50) == 564908303
