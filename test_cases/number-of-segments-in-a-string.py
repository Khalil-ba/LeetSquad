# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "Hello, my name is John") == 5
    assert candidate(s = "Hello") == 1
