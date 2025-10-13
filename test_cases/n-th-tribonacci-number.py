# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 3) == 2
    assert candidate(n = 4) == 4
    assert candidate(n = 37) == 2082876103
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 1
    assert candidate(n = 25) == 1389537
    assert candidate(n = 30) == 29249425
    assert candidate(n = 15) == 3136
    assert candidate(n = 22) == 223317
    assert candidate(n = 12) == 504
    assert candidate(n = 35) == 615693474
    assert candidate(n = 26) == 2555757
    assert candidate(n = 27) == 4700770
    assert candidate(n = 18) == 19513
    assert candidate(n = 20) == 66012
    assert candidate(n = 10) == 149
    assert candidate(n = 5) == 7
