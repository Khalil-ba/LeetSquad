# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arrivalTime = 5,delayedTime = 19) == 0
    assert candidate(arrivalTime = 8,delayedTime = 16) == 0
    assert candidate(arrivalTime = 13,delayedTime = 11) == 0
    assert candidate(arrivalTime = 15,delayedTime = 5) == 20
    assert candidate(arrivalTime = 1,delayedTime = 1) == 2
    assert candidate(arrivalTime = 12,delayedTime = 12) == 0
    assert candidate(arrivalTime = 1,delayedTime = 23) == 0
    assert candidate(arrivalTime = 0,delayedTime = 24) == 0
    assert candidate(arrivalTime = 23,delayedTime = 2) == 1
    assert candidate(arrivalTime = 5,delayedTime = 20) == 1
    assert candidate(arrivalTime = 19,delayedTime = 5) == 0
    assert candidate(arrivalTime = 18,delayedTime = 6) == 0
    assert candidate(arrivalTime = 2,delayedTime = 22) == 0
    assert candidate(arrivalTime = 20,delayedTime = 4) == 0
    assert candidate(arrivalTime = 3,delayedTime = 21) == 0
    assert candidate(arrivalTime = 20,delayedTime = 5) == 1
    assert candidate(arrivalTime = 6,delayedTime = 18) == 0
    assert candidate(arrivalTime = 9,delayedTime = 15) == 0
    assert candidate(arrivalTime = 17,delayedTime = 8) == 1
    assert candidate(arrivalTime = 7,delayedTime = 17) == 0
    assert candidate(arrivalTime = 20,delayedTime = 8) == 4
    assert candidate(arrivalTime = 7,delayedTime = 18) == 1
    assert candidate(arrivalTime = 18,delayedTime = 7) == 1
    assert candidate(arrivalTime = 15,delayedTime = 9) == 0
    assert candidate(arrivalTime = 10,delayedTime = 14) == 0
    assert candidate(arrivalTime = 19,delayedTime = 6) == 1
    assert candidate(arrivalTime = 20,delayedTime = 6) == 2
    assert candidate(arrivalTime = 16,delayedTime = 8) == 0
    assert candidate(arrivalTime = 11,delayedTime = 14) == 1
    assert candidate(arrivalTime = 17,delayedTime = 7) == 0
    assert candidate(arrivalTime = 14,delayedTime = 10) == 0
