# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(word = "234Adas") == True
    assert candidate(word = "b3") == False
    assert candidate(word = "a3$e") == False
