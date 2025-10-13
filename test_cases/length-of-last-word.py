# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "Hello World") == 5
    assert candidate(s = "   fly me   to   the moon  ") == 4
    assert candidate(s = "luffy is still joyboy") == 6
