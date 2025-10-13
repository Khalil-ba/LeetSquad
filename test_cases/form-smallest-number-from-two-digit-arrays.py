# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 4, 5]) == 3
    assert candidate(nums1 = [1, 2],nums2 = [3, 4]) == 13
    assert candidate(nums1 = [1, 9],nums2 = [2, 8]) == 12
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9]) == 16
    assert candidate(nums1 = [9, 8, 7],nums2 = [6, 5, 4]) == 47
    assert candidate(nums1 = [1],nums2 = [2]) == 12
    assert candidate(nums1 = [2],nums2 = [3]) == 23
    assert candidate(nums1 = [7, 8, 9],nums2 = [9, 8, 7]) == 7
    assert candidate(nums1 = [9, 8],nums2 = [7, 6]) == 68
    assert candidate(nums1 = [3, 5, 2, 6],nums2 = [3, 1, 7]) == 3
    assert candidate(nums1 = [5],nums2 = [5]) == 5
    assert candidate(nums1 = [7, 3],nums2 = [3, 7]) == 3
    assert candidate(nums1 = [1],nums2 = [9]) == 19
    assert candidate(nums1 = [9],nums2 = [1]) == 19
    assert candidate(nums1 = [2, 4, 6],nums2 = [1, 3, 5]) == 12
    assert candidate(nums1 = [4, 1, 3],nums2 = [5, 7]) == 15
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 14
    assert candidate(nums1 = [1, 4, 7],nums2 = [2, 5, 8, 9]) == 12
    assert candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [2, 4, 6, 8]) == 12
    assert candidate(nums1 = [2, 4, 6, 8],nums2 = [3, 5, 7, 9, 1]) == 12
    assert candidate(nums1 = [8, 9],nums2 = [8, 9, 1, 2]) == 8
    assert candidate(nums1 = [2, 3, 5],nums2 = [2, 3, 4]) == 2
    assert candidate(nums1 = [7, 9, 1],nums2 = [2, 4, 6]) == 12
    assert candidate(nums1 = [7, 8, 9],nums2 = [2, 4, 6]) == 27
    assert candidate(nums1 = [1, 4, 7],nums2 = [2, 5, 8]) == 12
    assert candidate(nums1 = [3, 1, 4],nums2 = [1, 5, 9]) == 1
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [2, 4, 6, 8]) == 2
    assert candidate(nums1 = [5, 7, 9],nums2 = [5, 3, 8, 2]) == 5
    assert candidate(nums1 = [2, 3, 6, 9],nums2 = [1, 4, 7]) == 12
    assert candidate(nums1 = [8, 2, 4, 6],nums2 = [7, 3, 9, 1]) == 12
    assert candidate(nums1 = [3, 4, 5],nums2 = [3, 4, 5]) == 3
    assert candidate(nums1 = [1],nums2 = [1]) == 1
    assert candidate(nums1 = [5, 9],nums2 = [5, 3]) == 5
    assert candidate(nums1 = [8, 2, 4],nums2 = [5, 6, 7, 9]) == 25
    assert candidate(nums1 = [2, 4, 6, 8],nums2 = [1, 3, 5, 7]) == 12
    assert candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [4, 3, 2, 1]) == 15
    assert candidate(nums1 = [7, 3, 8],nums2 = [9, 4, 1]) == 13
    assert candidate(nums1 = [1, 4, 7],nums2 = [2, 5, 8]) == 12
    assert candidate(nums1 = [9, 7, 5],nums2 = [3, 1]) == 15
    assert candidate(nums1 = [9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8]) == 19
    assert candidate(nums1 = [5, 6, 1],nums2 = [6, 7, 2]) == 6
    assert candidate(nums1 = [4, 5, 6],nums2 = [6, 7, 8]) == 6
    assert candidate(nums1 = [1, 5, 9],nums2 = [2, 6, 8]) == 12
    assert candidate(nums1 = [3, 6, 9],nums2 = [3, 5, 8]) == 3
    assert candidate(nums1 = [2, 5, 9],nums2 = [5, 8, 3]) == 5
    assert candidate(nums1 = [9, 8, 7, 6],nums2 = [5, 4, 3, 2, 1]) == 16
    assert candidate(nums1 = [8, 6, 4, 2, 0],nums2 = [7, 5, 3, 1, 9]) == 1
    assert candidate(nums1 = [5, 3, 7],nums2 = [8, 5, 3]) == 3
    assert candidate(nums1 = [6, 3, 1],nums2 = [7, 5, 9, 2, 4]) == 12
    assert candidate(nums1 = [4, 5],nums2 = [4, 5, 6]) == 4
    assert candidate(nums1 = [1, 2],nums2 = [3, 4, 5, 6, 7, 8, 9]) == 13
    assert candidate(nums1 = [3, 7, 1, 5],nums2 = [1, 9, 6, 8]) == 1
    assert candidate(nums1 = [1],nums2 = [9, 8, 7, 6, 5, 4, 3, 2]) == 12
    assert candidate(nums1 = [7, 8, 9],nums2 = [1, 2, 3]) == 17
    assert candidate(nums1 = [3, 5, 7],nums2 = [5, 7, 9]) == 5
    assert candidate(nums1 = [3, 6, 9],nums2 = [3, 6, 9]) == 3
    assert candidate(nums1 = [7, 2, 9],nums2 = [3, 2, 8]) == 2
    assert candidate(nums1 = [8, 6, 2],nums2 = [4, 2, 9]) == 2
    assert candidate(nums1 = [2, 4, 6, 8],nums2 = [1, 3, 5, 7, 9]) == 12
    assert candidate(nums1 = [3],nums2 = [9, 8, 7, 6, 5, 4, 2, 1]) == 13
    assert candidate(nums1 = [9, 7, 5],nums2 = [8, 6, 4]) == 45
    assert candidate(nums1 = [1, 6],nums2 = [5, 6]) == 6
    assert candidate(nums1 = [1, 5, 9],nums2 = [1, 5, 9]) == 1
    assert candidate(nums1 = [9, 8, 7],nums2 = [6, 5, 4]) == 47
    assert candidate(nums1 = [5, 3, 8, 1],nums2 = [4, 7, 6, 2, 9]) == 12
    assert candidate(nums1 = [2, 3, 5, 7],nums2 = [1, 4, 6, 8, 9]) == 12
    assert candidate(nums1 = [5],nums2 = [5, 4, 3, 2, 1]) == 5
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2],nums2 = [1]) == 12
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8]) == 12
    assert candidate(nums1 = [1, 3, 7, 9],nums2 = [2, 4, 6, 8]) == 12
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 0]) == 1
    assert candidate(nums1 = [3, 7, 9],nums2 = [3, 4, 5]) == 3
    assert candidate(nums1 = [5, 3, 8],nums2 = [8, 2, 7]) == 8
    assert candidate(nums1 = [3, 6, 8],nums2 = [2, 5, 7]) == 23
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9]) == 9
    assert candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8]) == 12
    assert candidate(nums1 = [8, 9],nums2 = [1, 2, 3, 4, 5]) == 18
    assert candidate(nums1 = [5, 9],nums2 = [5, 7]) == 5
    assert candidate(nums1 = [9, 7, 5, 3],nums2 = [8, 6, 4, 2, 1]) == 13
    assert candidate(nums1 = [1, 2],nums2 = [2, 3]) == 2
    assert candidate(nums1 = [1, 3, 5, 7],nums2 = [9, 8, 6, 4, 2, 0]) == 1
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [3, 4, 5, 6, 7]) == 3
    assert candidate(nums1 = [4],nums2 = [4]) == 4
    assert candidate(nums1 = [2, 4, 6, 8],nums2 = [4]) == 4
    assert candidate(nums1 = [7, 8, 9],nums2 = [1, 2, 3, 4, 5, 6]) == 17
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 6, 7, 8, 9]) == 5
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8]) == 12
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 4, 5]) == 3
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 4, 5, 6, 7]) == 3
    assert candidate(nums1 = [1],nums2 = [9, 8, 7, 6, 5, 4, 3, 2]) == 12
    assert candidate(nums1 = [5, 6, 7],nums2 = [1, 2, 3, 4]) == 15
    assert candidate(nums1 = [4, 8],nums2 = [5, 7, 9]) == 45
    assert candidate(nums1 = [7, 5, 3, 1],nums2 = [8, 6, 4, 2]) == 12
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums1 = [2, 8, 6],nums2 = [7, 4, 1]) == 12
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 5, 6, 7]) == 4
    assert candidate(nums1 = [3, 6, 9],nums2 = [3, 5, 7]) == 3
