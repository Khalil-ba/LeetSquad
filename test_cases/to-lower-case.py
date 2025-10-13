# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "Hello") == "hello"
    assert candidate(s = "here") == "here"
    assert candidate(s = "LOVELY") == "lovely"
