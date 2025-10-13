# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(board = "RRYYGG",hand = "") == -1
