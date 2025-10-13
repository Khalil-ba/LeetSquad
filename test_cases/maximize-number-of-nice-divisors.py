# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(primeFactors = 1) == 1
    assert candidate(primeFactors = 3) == 3
    assert candidate(primeFactors = 2) == 2
