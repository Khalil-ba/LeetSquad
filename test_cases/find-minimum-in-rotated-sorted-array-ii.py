# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 0
    assert candidate(nums = [1, 3, 5]) == 1
    assert candidate(nums = [2, 2, 2, 0, 1]) == 0
    assert candidate(nums = [5, 1, 2, 3, 4]) == 1
    assert candidate(nums = [3, 4, 5, 1, 2]) == 1
    assert candidate(nums = [15, 17, 11, 13]) == 11
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 0
    assert candidate(nums = [0, 1, 4, 4, 5, 6, 7]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 1, 3]) == 1
    assert candidate(nums = [4, 4, 5, 6, 7, 0, 1, 2, 3]) == 0
    assert candidate(nums = [11, 13, 15, 17]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 2, 2, 2]) == 0
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4]) == 1
    assert candidate(nums = [4, 4, 4, 4, 0, 1, 2, 3, 4]) == 0
    assert candidate(nums = [1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [10, 1, 10, 10, 10]) == 1
    assert candidate(nums = [4, 5, 6, 7, 0, 1, 4]) == 0
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 0, 1]) == 0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(nums = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [104, 105, 106, 107, 108, 109, 0, 100, 101, 102, 103]) == 0
    assert candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 0
    assert candidate(nums = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 1
    assert candidate(nums = [3, 4, 5, 1, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(nums = [6, 7, 1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [6, 7, 0, 1, 2, 4, 5]) == 0
    assert candidate(nums = [108, 109, 0, 100, 101, 102, 103, 104, 105, 106, 107]) == 0
    assert candidate(nums = [106, 107, 108, 109, 0, 100, 101, 102, 103, 104, 105]) == 0
    assert candidate(nums = [2, 5, 6, 0, 0, 1, 2]) == 0
    assert candidate(nums = [4, 5, 6, 7, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 1]) == 0
    assert candidate(nums = [11, 13, 15, 17, 19, 2, 5, 7]) == 2
    assert candidate(nums = [8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 0]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 0, 1, 2, 2, 3]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 1, 1]) == 1
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(nums = [11, 13, 15, 17, 19, 1, 3, 5, 7]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 1
    assert candidate(nums = [2, 3, 4, 5, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0
    assert candidate(nums = [5, 6, 7, 0, 1, 2, 3]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 0, 1]) == 0
    assert candidate(nums = [103, 104, 105, 106, 107, 108, 109, 0, 100, 101, 102]) == 0
    assert candidate(nums = [1, 0, 1, 1, 1, 1]) == 0
    assert candidate(nums = [6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 1]) == 1
    assert candidate(nums = [3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3]) == 1
    assert candidate(nums = [9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert candidate(nums = [7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6]) == 0
    assert candidate(nums = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [4, 4, 4, 4, 4, 0, 1, 2, 3]) == 0
    assert candidate(nums = [1, 2, 2, 2, 0, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [109, 0, 100, 101, 102, 103, 104, 105, 106, 107, 108]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 1, 2, 3, 4]) == 1
    assert candidate(nums = [4, 5, 6, 7, 0, 1, 2]) == 0
    assert candidate(nums = [100, 101, 102, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(nums = [15, 17, 19, 0, 1, 3, 5, 7, 9, 11, 13]) == 0
    assert candidate(nums = [2, 2, 2, 2, 1, 2, 2, 2]) == 1
    assert candidate(nums = [2, 0, 1, 1, 1, 2, 2]) == 0
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 1, 2]) == 1
    assert candidate(nums = [107, 108, 109, 0, 100, 101, 102, 103, 104, 105, 106]) == 0
    assert candidate(nums = [2, 2, 2, 0, 1, 2]) == 0
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 0
    assert candidate(nums = [105, 106, 107, 108, 109, 0, 100, 101, 102, 103, 104]) == 0
    assert candidate(nums = [2, 2, 2, 0, 1, 1, 2]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0]) == 0
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1]) == 0
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4]) == 0
    assert candidate(nums = [4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3]) == 0
    assert candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 0, 100]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 1, 3, 3, 3]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 0, 5]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert candidate(nums = [4, 4, 4, 4, 0, 1, 4]) == 0
    assert candidate(nums = [1, 2, 0, 1, 1, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 0, 0, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1]) == 0
    assert candidate(nums = [6, 7, 1, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [11, 13, 15, 17, 19, 0, 1, 3, 5, 7, 9]) == 0
    assert candidate(nums = [102, 103, 104, 105, 106, 107, 108, 109, 0, 100, 101]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 5, 10]) == 5
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 0]) == 0
    assert candidate(nums = [2, 2, 0, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 6, 6, 6, 0, 1, 2]) == 0
    assert candidate(nums = [0, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [2, 2, 2, 0, 1, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [1, 1, 0, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]) == 0
    assert candidate(nums = [11, 13, 15, 17, 19, 21, 2, 3, 5, 7, 9]) == 2
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15]) == 0
    assert candidate(nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [4, 5, 1, 2, 3]) == 1
    assert candidate(nums = [0, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 1, 3, 3]) == 1
    assert candidate(nums = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 0
