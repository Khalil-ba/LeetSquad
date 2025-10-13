# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums1 = [1, 0, 0, 0],nums2 = [0, 0, 0, 1]) == 4
    assert candidate(nums1 = [2, 0, 2, 0],nums2 = [1, 4]) == -1
    assert candidate(nums1 = [3, 2, 0, 1, 0],nums2 = [6, 5, 0]) == 12
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == 6
    assert candidate(nums1 = [1, 0, 3],nums2 = [2, 0, 2]) == 5
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [2, 2, 2, 2]) == -1
    assert candidate(nums1 = [0, 0, 0],nums2 = [1, 1, 1]) == 3
    assert candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 3
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == 4
    assert candidate(nums1 = [1, 0],nums2 = [0, 1]) == 2
    assert candidate(nums1 = [10, 20, 30, 0, 0],nums2 = [0, 0, 0, 40, 50]) == 93
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1]) == 6
    assert candidate(nums1 = [1000000, 0, 0],nums2 = [500000, 500000, 0]) == 1000002
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 65
    assert candidate(nums1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 15
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [1000000]) == 1000000
    assert candidate(nums1 = [1000000, 0, 0, 0, 0],nums2 = [500000, 500000, 0, 0, 0]) == 1000004
    assert candidate(nums1 = [1000000, 1000000, 0],nums2 = [500000, 500000, 500000, 500000, 500000, 500000, 0]) == 3000001
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5, 6]) == 21
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1, 1]) == 7
    assert candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000, 0, 0, 0, 0, 0],nums2 = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 0, 0, 0]) == 15000005
    assert candidate(nums1 = [1000000],nums2 = [1000000]) == 1000000
    assert candidate(nums1 = [1000000],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000000]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 0, 0],nums2 = [5, 4, 3, 2, 1, 0, 0]) == 17
    assert candidate(nums1 = [1, 2, 3, 0, 0],nums2 = [4, 5, 0, 0, 0]) == 12
    assert candidate(nums1 = [1000000, 0, 0, 0],nums2 = [500000, 500000, 0, 0]) == 1000003
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(nums1 = [999999, 0, 0, 0],nums2 = [500000, 500000, 0]) == 1000002
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2]) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 0, 1]) == 17
    assert candidate(nums1 = [1, 1, 1, 1, 1, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1, 0, 0, 0]) == 9
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [1000000, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1000009
    assert candidate(nums1 = [999999, 0],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(nums1 = [999999, 0, 0, 0, 0, 0],nums2 = [1000000, 1, 1, 1, 1, 1]) == 1000005
    assert candidate(nums1 = [1, 0, 1, 0, 1, 0],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums1 = [3, 0, 5, 0, 7],nums2 = [2, 0, 6, 0, 0]) == 17
    assert candidate(nums1 = [1000000, 0, 0, 500000],nums2 = [750000, 250000, 0, 0]) == 1500002
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100, 0]) == -1
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 15
    assert candidate(nums1 = [999999, 0, 0, 0],nums2 = [1, 1, 1, 1]) == -1
    assert candidate(nums1 = [1000000, 0, 0, 0],nums2 = [500000, 500000, 0, 0]) == 1000003
    assert candidate(nums1 = [1, 2, 3, 4, 0, 0, 0],nums2 = [7, 8, 9, 0, 0]) == 26
    assert candidate(nums1 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums1 = [500000, 500000, 0, 0],nums2 = [250000, 250000, 250000, 250000, 0, 0]) == 1000002
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 15
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 46
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1, 1]) == 7
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 0]) == 16
    assert candidate(nums1 = [1, 0, 1, 0, 1],nums2 = [0, 1, 0, 1, 0, 1]) == 6
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 0]) == -1
    assert candidate(nums1 = [1000000, 1000000, 1000000, 1000000],nums2 = [2000000, 0, 0, 0]) == 4000000
    assert candidate(nums1 = [100, 200, 300, 0, 0, 0, 0, 0, 0, 0],nums2 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 750
    assert candidate(nums1 = [10, 20, 30, 0, 0],nums2 = [5, 15, 25, 0, 0]) == 62
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 46
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 55
    assert candidate(nums1 = [0, 1000000, 0, 1000000],nums2 = [500000, 0, 0, 500000]) == 2000002
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [0, 0, 0, 0, 0, 0]) == 6
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums1 = [10, 20, 30, 0, 0],nums2 = [15, 15, 0, 0, 0]) == 62
    assert candidate(nums1 = [0, 1, 0, 2, 0, 3],nums2 = [4, 0, 5, 0, 6]) == 17
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 55
    assert candidate(nums1 = [1, 2, 3, 0, 0, 0],nums2 = [6, 5, 0, 0, 0]) == 14
    assert candidate(nums1 = [5, 10, 15, 20],nums2 = [20, 15, 10, 5, 0, 0]) == -1
    assert candidate(nums1 = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0],nums2 = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == 20
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 165
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 20
    assert candidate(nums1 = [1000000, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [500000, 500000, 0, 0, 0, 0, 0, 0, 0, 0]) == 1000009
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 0]) == 167
    assert candidate(nums1 = [1000000, 0, 0, 0],nums2 = [500000, 500000, 0]) == 1000003
    assert candidate(nums1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10
    assert candidate(nums1 = [1, 2, 3, 0, 0, 0],nums2 = [6, 0, 0, 0, 0, 0]) == 11
    assert candidate(nums1 = [1, 0, 3, 0, 5, 0, 7, 0, 9, 0],nums2 = [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]) == 35
    assert candidate(nums1 = [1, 0, 1, 0, 1, 0],nums2 = [0, 1, 0, 1, 0, 1]) == 6
    assert candidate(nums1 = [1, 2, 3, 0, 0, 0],nums2 = [4, 5, 0, 0, 0, 0]) == 13
    assert candidate(nums1 = [10, 20, 30, 40, 50, 0],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 151
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
    assert candidate(nums1 = [1, 2, 3, 4, 5, 0, 0],nums2 = [5, 4, 3, 2, 1, 0, 0]) == 17
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10
    assert candidate(nums1 = [999999, 999999, 999999],nums2 = [999999, 999999, 0]) == 2999997
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 12
    assert candidate(nums1 = [1, 0, 0, 0, 0, 0],nums2 = [2, 0, 0, 0, 0, 0]) == 7
    assert candidate(nums1 = [100, 200, 300, 400, 500, 0, 0, 0, 0, 0],nums2 = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [0, 0, 0, 0, 0]) == 15
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 0, 0]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 0, 0, 0],nums2 = [10, 0, 0, 0, 0, 0, 0, 0]) == 18
    assert candidate(nums1 = [999999],nums2 = [1, 0, 0, 0, 0, 0, 0]) == 999999
    assert candidate(nums1 = [10, 20, 30],nums2 = [5, 5, 5, 5, 5, 5, 5]) == -1
    assert candidate(nums1 = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0],nums2 = [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]) == 20
    assert candidate(nums1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 15
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [5, 15, 25, 35, 0, 0]) == 100
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 0, 0, 0]) == -1
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1]) == 6
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
