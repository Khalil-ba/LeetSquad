# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums1 = [0, 100, 0],nums2 = [100, 0, 0]) == 12
    assert candidate(nums1 = [1, 0, 1, 0],nums2 = [0, 1, 0, 1]) == 22
    assert candidate(nums1 = [5, 10, 15],nums2 = [15, 10, 5]) == 0
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == 8
    assert candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10]) == 0
    assert candidate(nums1 = [0, 100],nums2 = [100, 0]) == 4
    assert candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 4
    assert candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8]) == 1
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == 52
    assert candidate(nums1 = [100, 0, 100],nums2 = [0, 100, 0]) == 10
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 6
    assert candidate(nums1 = [50, 50],nums2 = [50, 50]) == 2
    assert candidate(nums1 = [50, 50, 50],nums2 = [50, 50, 50]) == 4
    assert candidate(nums1 = [100, 0, 100, 0],nums2 = [0, 100, 0, 100]) == 22
    assert candidate(nums1 = [1, 2, 5],nums2 = [2, 6, 3]) == 3
    assert candidate(nums1 = [100, 0, 50],nums2 = [0, 100, 50]) == 4
    assert candidate(nums1 = [8, 6, 4, 2],nums2 = [1, 3, 5, 7]) == 3
    assert candidate(nums1 = [100, 0, 100, 0, 100],nums2 = [0, 100, 0, 100, 0]) == 44
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == 0
    assert candidate(nums1 = [99, 99, 99],nums2 = [1, 1, 1]) == 0
    assert candidate(nums1 = [100, 0, 0],nums2 = [0, 100, 0]) == 12
    assert candidate(nums1 = [0, 1],nums2 = [1, 0]) == 4
    assert candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 22
    assert candidate(nums1 = [10, 20, 30],nums2 = [15, 25, 35]) == 0
    assert candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 267
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [3, 3, 2, 2, 1, 1]) == 34
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 255254
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000],nums2 = [1000000, 100000, 10000, 1000, 100, 10, 1]) == 0
    assert candidate(nums1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],nums2 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1108
    assert candidate(nums1 = [1, 2, 3, 2, 1],nums2 = [1, 3, 2, 3, 1]) == 7
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 350
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 350
    assert candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == 20
    assert candidate(nums1 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],nums2 = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 12932
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5
    assert candidate(nums1 = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 100, 0, 0, 0, 0, 0, 0, 0, 0]) == 2538
    assert candidate(nums1 = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42],nums2 = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 622
    assert candidate(nums1 = [100, 100, 100, 100, 100],nums2 = [50, 50, 50, 50, 50]) == 9
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [60, 50, 40, 30, 20, 10]) == 28
    assert candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 622
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 622
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 622
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],nums2 = [55, 34, 21, 13, 8, 5, 3, 2, 1, 1]) == 72
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [100, 50, 25, 12, 6, 3, 1],nums2 = [1, 3, 6, 12, 25, 50, 100]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 2
    assert candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [45, 35, 25, 15, 5]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [150, 150, 150, 150, 150]) == 4
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 57
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 622
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12]) == 3
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 350
    assert candidate(nums1 = [50, 60, 70, 80, 90],nums2 = [40, 50, 60, 70, 80]) == 7
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 610
    assert candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 34
    assert candidate(nums1 = [100, 0, 100, 0, 100],nums2 = [0, 100, 0, 100, 0]) == 44
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 55
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 8166
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 350
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 350
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 62
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 6
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 350
    assert candidate(nums1 = [10, 10, 10, 10],nums2 = [5, 5, 5, 5]) == 6
    assert candidate(nums1 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],nums2 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1108
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == 0
    assert candidate(nums1 = [0, 0, 0, 1, 1, 1, 2, 2, 2],nums2 = [1, 2, 3, 0, 1, 2, 0, 1, 2]) == 221
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [15, 25, 35, 45, 55]) == 2
    assert candidate(nums1 = [100, 100, 100, 100, 100],nums2 = [0, 0, 0, 0, 0]) == 15
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 350
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 2
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 350
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 610
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 40
    assert candidate(nums1 = [50, 25, 75, 50, 25, 75, 50, 25, 75, 50],nums2 = [75, 50, 25, 75, 50, 25, 75, 50, 25, 75]) == 278
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 267
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 6
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 1, 0, 1, 0]) == 42
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 4072
    assert candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 57
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 350
    assert candidate(nums1 = [0, 1, 1, 0, 1, 0, 1, 0],nums2 = [1, 0, 0, 1, 0, 1, 0, 1]) == 302
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1]) == 15
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 388
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 610
