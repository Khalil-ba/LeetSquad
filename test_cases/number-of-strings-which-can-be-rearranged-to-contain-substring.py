# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 4) == 12
    assert candidate(n = 1) == 0
    assert candidate(n = 10) == 83943898
    assert candidate(n = 5) == 1460
    assert candidate(n = 3) == 0
    assert candidate(n = 125) == 558399309
    assert candidate(n = 100) == 86731066
    assert candidate(n = 50) == 232825199
    assert candidate(n = 30) == 52805056
    assert candidate(n = 2) == 0
    assert candidate(n = 80) == 974106352
    assert candidate(n = 8) == 295164156
    assert candidate(n = 250) == 889526859
    assert candidate(n = 75) == 842828500
    assert candidate(n = 20) == 291395991
    assert candidate(n = 15) == 430509685
    assert candidate(n = 9) == 947613240
    assert candidate(n = 6) == 106620
    assert candidate(n = 7) == 6058192
    assert candidate(n = 90) == 122933939
    assert candidate(n = 25) == 935610434
