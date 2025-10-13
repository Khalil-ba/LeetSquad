# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 5,maxChanges = 5) == 8
    assert candidate(nums = [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],k = 3,maxChanges = 2) == 3
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 2,maxChanges = 1) == 2
    assert candidate(nums = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],k = 2,maxChanges = 1) == 2
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1,maxChanges = 0) == 0
    assert candidate(nums = [0, 0, 0, 0],k = 2,maxChanges = 3) == 4
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 4,maxChanges = 0) == 8
    assert candidate(nums = [1, 1, 0, 0, 0, 1, 1, 0, 0, 1],k = 3,maxChanges = 1) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,maxChanges = 3) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],k = 5,maxChanges = 5) == 6
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 5,maxChanges = 0) == 12
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],k = 5,maxChanges = 5) == 6
    assert candidate(nums = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],k = 2,maxChanges = 1) == 2
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 5,maxChanges = 2) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,maxChanges = 0) == 6
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],k = 12,maxChanges = 7) == 26
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 2,maxChanges = 1) == 2
    assert candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],k = 15,maxChanges = 20) == 28
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 10,maxChanges = 5) == 22
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],k = 7,maxChanges = 3) == 13
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],k = 6,maxChanges = 3) == 8
    assert candidate(nums = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],k = 4,maxChanges = 2) == 9
    assert candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],k = 4,maxChanges = 2) == 4
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 10,maxChanges = 5) == 22
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],k = 5,maxChanges = 3) == 6
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7,maxChanges = 10) == 10
    assert candidate(nums = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],k = 4,maxChanges = 0) == 12
    assert candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],k = 5,maxChanges = 5) == 8
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 20,maxChanges = 15) == 42
    assert candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],k = 15,maxChanges = 5) == 85
    assert candidate(nums = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0],k = 4,maxChanges = 0) == 9
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],k = 4,maxChanges = 10) == 4
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 10,maxChanges = 5) == 22
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],k = 2,maxChanges = 0) == 1
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],k = 6,maxChanges = 2) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15,maxChanges = 5) == 35
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 7,maxChanges = 2) == 16
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 4,maxChanges = 5) == 4
    assert candidate(nums = [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],k = 10,maxChanges = 5) == 22
    assert candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],k = 3,maxChanges = 2) == 4
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 4,maxChanges = 2) == 6
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 5,maxChanges = 3) == 8
    assert candidate(nums = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],k = 5,maxChanges = 5) == 8
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],k = 6,maxChanges = 3) == 8
    assert candidate(nums = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,maxChanges = 25) == 8
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],k = 2,maxChanges = 5) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 2,maxChanges = 2) == 2
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 3,maxChanges = 0) == 19
    assert candidate(nums = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],k = 3,maxChanges = 2) == 3
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],k = 3,maxChanges = 1) == 5
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 4,maxChanges = 1) == 6
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 1,maxChanges = 0) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],k = 2,maxChanges = 0) == 1
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3,maxChanges = 0) == 2
    assert candidate(nums = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],k = 2,maxChanges = 2) == 2
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],k = 3,maxChanges = 0) == 2
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],k = 3,maxChanges = 3) == 4
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],k = 4,maxChanges = 2) == 4
    assert candidate(nums = [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],k = 4,maxChanges = 2) == 7
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],k = 5,maxChanges = 1) == 6
    assert candidate(nums = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],k = 4,maxChanges = 3) == 6
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 2,maxChanges = 0) == 60
    assert candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],k = 4,maxChanges = 0) == 12
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3,maxChanges = 0) == 2
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 4,maxChanges = 2) == 6
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 3,maxChanges = 1) == 4
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],k = 2,maxChanges = 1) == 1
    assert candidate(nums = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],k = 4,maxChanges = 1) == 6
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 1,maxChanges = 1) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25,maxChanges = 10) == 76
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 6,maxChanges = 4) == 10
    assert candidate(nums = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],k = 4,maxChanges = 2) == 8
    assert candidate(nums = [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],k = 4,maxChanges = 2) == 5
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1,maxChanges = 10) == 0
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 3,maxChanges = 1) == 4
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 6,maxChanges = 4) == 10
    assert candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],k = 6,maxChanges = 0) == 27
    assert candidate(nums = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],k = 5,maxChanges = 3) == 7
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 10,maxChanges = 0) == 50
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,maxChanges = 10) == 6
    assert candidate(nums = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 2,maxChanges = 1) == 1
    assert candidate(nums = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],k = 3,maxChanges = 1) == 7
    assert candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],k = 8,maxChanges = 4) == 12
    assert candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 4,maxChanges = 0) == 4
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 1,maxChanges = 5) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,maxChanges = 10) == 6
    assert candidate(nums = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],k = 5,maxChanges = 10) == 8
    assert candidate(nums = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],k = 25,maxChanges = 30) == 47
    assert candidate(nums = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],k = 3,maxChanges = 2) == 4
    assert candidate(nums = [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],k = 5,maxChanges = 1) == 15
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 10,maxChanges = 3) == 30
    assert candidate(nums = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],k = 7,maxChanges = 5) == 11
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],k = 5,maxChanges = 0) == 12
    assert candidate(nums = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],k = 8,maxChanges = 3) == 22
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 3,maxChanges = 2) == 4
