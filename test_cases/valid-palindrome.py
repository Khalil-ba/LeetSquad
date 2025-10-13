# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "race a car") == False
    assert candidate(s = " ") == True
