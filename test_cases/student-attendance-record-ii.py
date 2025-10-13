# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 19
    assert candidate(n = 100) == 985598218
    assert candidate(n = 2) == 8
    assert candidate(n = 1) == 3
    assert candidate(n = 10) == 3536
    assert candidate(n = 5) == 94
    assert candidate(n = 50) == 100469819
    assert candidate(n = 300) == 921822362
    assert candidate(n = 4) == 43
    assert candidate(n = 20) == 2947811
    assert candidate(n = 200) == 110821862
