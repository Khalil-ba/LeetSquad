# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 8) == 475
    assert candidate(n = 3) == 123
    assert candidate(n = 4) == 597
    assert candidate(n = 6) == 1218
    assert candidate(n = 2) == 987
    assert candidate(n = 1) == 9
    assert candidate(n = 7) == 877
    assert candidate(n = 5) == 677
