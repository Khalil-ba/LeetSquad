# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [0, 0, 1, 1, 0, 0]) == 8
    assert candidate(nums = [0, 1, 0, 1, 0, 1]) == 21
    assert candidate(nums = [1, 0, 1, 0, 1]) == 15
    assert candidate(nums = [1, 1, 1, 1]) == 4
    assert candidate(nums = [1, 0, 0, 1, 0, 1, 1, 0]) == 16
    assert candidate(nums = [0, 1, 0, 1, 0]) == 15
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [0, 1]) == 3
    assert candidate(nums = [0, 0, 0, 0, 0]) == 5
    assert candidate(nums = [0, 1, 1, 1]) == 5
    assert candidate(nums = [1, 0]) == 3
    assert candidate(nums = [1, 0, 0, 1, 0, 1]) == 13
    assert candidate(nums = [1, 1, 0, 1, 0, 1]) == 16
    assert candidate(nums = [1, 1, 1, 1, 1]) == 5
    assert candidate(nums = [0]) == 1
    assert candidate(nums = [1, 0, 1, 0, 1, 0]) == 21
    assert candidate(nums = [0, 0, 0, 0]) == 4
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1]) == 36
    assert candidate(nums = [1, 1, 0, 0, 1, 1]) == 8
    assert candidate(nums = [0, 1, 1, 0, 1, 0]) == 13
    assert candidate(nums = [0, 0, 1, 0, 1, 0]) == 16
    assert candidate(nums = [1, 0, 1, 0]) == 10
    assert candidate(nums = [0, 1, 1, 0, 0, 1]) == 9
    assert candidate(nums = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0]) == 15
    assert candidate(nums = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1]) == 33
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 66
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 120
    assert candidate(nums = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == 27
    assert candidate(nums = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]) == 18
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0]) == 17
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 16
    assert candidate(nums = [1, 1, 0, 1, 0, 1, 0, 1, 1, 0]) == 32
    assert candidate(nums = [0, 1, 0, 1, 1, 0, 1, 0, 1]) == 25
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 91
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 16
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 253
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]) == 29
    assert candidate(nums = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 19
    assert candidate(nums = [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]) == 34
    assert candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]) == 14
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 22
    assert candidate(nums = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 84
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(nums = [1, 1, 0, 0, 1, 0, 1, 1, 0]) == 17
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1]) == 28
    assert candidate(nums = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == 18
    assert candidate(nums = [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0]) == 18
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 105
    assert candidate(nums = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 106
    assert candidate(nums = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1]) == 48
    assert candidate(nums = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == 15
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]) == 31
    assert candidate(nums = [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 121
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 190
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 29
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == 15
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 528
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) == 11
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1]) == 31
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 41
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 136
    assert candidate(nums = [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]) == 44
    assert candidate(nums = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0]) == 26
    assert candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1]) == 12
    assert candidate(nums = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 51
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 22
    assert candidate(nums = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]) == 34
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]) == 19
    assert candidate(nums = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]) == 46
    assert candidate(nums = [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1]) == 48
    assert candidate(nums = [0, 1, 0, 1, 1, 0, 1, 0, 1, 1]) == 26
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1]) == 13
    assert candidate(nums = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]) == 34
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0]) == 11
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 136
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]) == 49
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 210
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 55
    assert candidate(nums = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 11
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 78
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 171
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0]) == 13
    assert candidate(nums = [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1]) == 35
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1]) == 33
    assert candidate(nums = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 46
    assert candidate(nums = [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]) == 38
    assert candidate(nums = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]) == 24
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 14
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]) == 19
    assert candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == 18
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 351
    assert candidate(nums = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]) == 52
    assert candidate(nums = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 19
    assert candidate(nums = [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0]) == 38
    assert candidate(nums = [0, 0, 1, 1, 1, 0, 1, 0, 0, 1]) == 18
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 325
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 23
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 17
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 595
    assert candidate(nums = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == 22
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == 19
    assert candidate(nums = [1, 1, 0, 0, 1, 1, 0, 0, 1]) == 13
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]) == 15
    assert candidate(nums = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]) == 19
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 55
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 210
    assert candidate(nums = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]) == 44
    assert candidate(nums = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]) == 22
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0]) == 45
    assert candidate(nums = [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]) == 49
