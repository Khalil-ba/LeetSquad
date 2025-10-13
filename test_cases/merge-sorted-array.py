# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums1 = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0],m = 5,nums2 = [2, 4, 6, 8, 10],n = 5) == None
    assert candidate(nums1 = [1],m = 1,nums2 = [],n = 0) == None
    assert candidate(nums1 = [0],m = 0,nums2 = [1],n = 1) == None
    assert candidate(nums1 = [4, 5, 6, 0, 0, 0],m = 3,nums2 = [1, 2, 3],n = 3) == None
    assert candidate(nums1 = [1, 2, 3, 0, 0, 0],m = 3,nums2 = [2, 5, 6],n = 3) == None
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 8,nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],n = 11) == None
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 0, 0, 0, 0, 0, 0, 0],m = 7,nums2 = [2, 4, 6, 8, 10, 12, 14],n = 7) == None
    assert candidate(nums1 = [-1, 0, 0, 0, 0],m = 1,nums2 = [-10, -3, -2, -1],n = 4) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],n = 10) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],m = 0,nums2 = [1, 1, 1, 1, 1, 1],n = 6) == None
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 0, 0, 0, 0, 0, 0],m = 6,nums2 = [5, 15, 25, 35, 45, 55],n = 6) == None
    assert candidate(nums1 = [5, 10, 15, 20, 0, 0, 0, 0],m = 4,nums2 = [1, 2, 8, 16],n = 4) == None
    assert candidate(nums1 = [100, 200, 300, 400, 0, 0, 0, 0, 0, 0, 0, 0],m = 4,nums2 = [50, 150, 250, 350, 450, 550],n = 6) == None
    assert candidate(nums1 = [-10, -5, 0, 0, 0],m = 2,nums2 = [-20, -15, 5],n = 3) == None
    assert candidate(nums1 = [5, 10, 15, 20, 0, 0, 0, 0, 0],m = 4,nums2 = [1, 6, 11, 16, 21],n = 5) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0],m = 0,nums2 = [-1, -2, -3, -4, -5, -6, -7, -8],n = 8) == None
    assert candidate(nums1 = [1, 2, 4, 7, 8, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [3, 5, 6, 9, 10, 11],n = 6) == None
    assert candidate(nums1 = [1, 1, 1, 1, 0, 0, 0],m = 4,nums2 = [1, 1, 1],n = 3) == None
    assert candidate(nums1 = [3, 6, 9, 12, 0, 0, 0, 0, 0],m = 4,nums2 = [1, 2, 3, 4, 5],n = 5) == None
    assert candidate(nums1 = [-10, -5, 0, 0, 0, 0, 0],m = 2,nums2 = [-7, -6, -3, -2, -1],n = 5) == None
    assert candidate(nums1 = [100, 200, 300, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [50, 150, 250, 350, 450, 550],n = 6) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [-5, -4, -3, -2, -1, 0],n = 6) == None
    assert candidate(nums1 = [-10, -8, -6, 0, 0, 0, 0, 0],m = 3,nums2 = [-9, -7, -5, -3, -1],n = 5) == None
    assert candidate(nums1 = [1000000000, 1000000000, 1000000000, 0, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [-1000000000, -500000000, -250000000],n = 3) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],m = 19,nums2 = [20],n = 1) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0],n = 10) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [0, 1, 2, 3, 4, 5],n = 6) == None
    assert candidate(nums1 = [-10, -5, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [-20, -15, -10, -5, 5],n = 5) == None
    assert candidate(nums1 = [2, 3, 7, 8, 10, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [1, 4, 5, 6, 9, 11, 12],n = 7) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 10) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 0,nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 10) == None
    assert candidate(nums1 = [10, 20, 30, 0, 0, 0, 0, 0],m = 3,nums2 = [5, 15, 25, 35, 45],n = 5) == None
    assert candidate(nums1 = [5, 10, 15, 20, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45],n = 10) == None
    assert candidate(nums1 = [1, 1, 1, 1, 0, 0, 0, 0],m = 4,nums2 = [1, 1, 1, 1],n = 4) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 0,nums2 = [-10, -5, -3, -1, 0, 1, 2, 3, 5, 10],n = 10) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],m = 0,nums2 = [-5, -3, -1, 0, 1, 3],n = 6) == None
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 0, 0, 0, 0, 0, 0],m = 6,nums2 = [1, 10, 20, 30, 40, 50],n = 6) == None
    assert candidate(nums1 = [-10, -9, -8, -7, -6, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [-100, -99, -98, -97, -96, -95, -94, -93, -92],n = 9) == None
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 10) == None
    assert candidate(nums1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],n = 10) == None
    assert candidate(nums1 = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 17) == None
    assert candidate(nums1 = [10, 20, 30, 0, 0, 0, 0, 0],m = 3,nums2 = [5, 15, 25, 35, 45],n = 5) == None
    assert candidate(nums1 = [100, 200, 300, 400, 500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],n = 10) == None
    assert candidate(nums1 = [999999999, 999999999, 999999999, 0, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006],n = 7) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],n = 10) == None
    assert candidate(nums1 = [5, 8, 10, 12, 0, 0, 0, 0, 0, 0],m = 4,nums2 = [6, 7, 9, 11, 13, 14],n = 6) == None
    assert candidate(nums1 = [-10, -8, -6, -4, -2, 0, 0, 0, 0, 0],m = 5,nums2 = [-9, -7, -5, -3, -1],n = 5) == None
    assert candidate(nums1 = [10, 20, 30, 0, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [1, 2, 3, 4, 5, 6, 7],n = 7) == None
    assert candidate(nums1 = [10, 20, 30, 40, 50, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [5, 15, 25, 35, 45, 55],n = 6) == None
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 0, 0, 0, 0],m = 6,nums2 = [1, 1, 2, 2],n = 4) == None
    assert candidate(nums1 = [-1, 0, 1, 2, 3, 0, 0, 0, 0],m = 5,nums2 = [-4, -3, -2, 4],n = 4) == None
    assert candidate(nums1 = [-1, 0, 1, 0, 0, 0, 0, 0],m = 3,nums2 = [-2, -1, 0, 2, 3],n = 5) == None
    assert candidate(nums1 = [1, 10, 20, 0, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [2, 3, 4, 5, 6, 7, 8, 9],n = 7) == None
    assert candidate(nums1 = [3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0],m = 7,nums2 = [3, 3, 3, 3, 3, 3],n = 6) == None
    assert candidate(nums1 = [1, 1, 1, 1, 1, 0, 0, 0, 0],m = 5,nums2 = [1, 1, 1, 1],n = 4) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 0,nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],n = 20) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0],m = 9,nums2 = [0, 0, 0, 0, 0, 0],n = 6) == None
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],n = 10) == None
    assert candidate(nums1 = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [4, 5, 6, 7, 8, 9, 10, 11, 12],n = 9) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 1, 3, 5, 7, 9],m = 5,nums2 = [2, 4, 6, 8, 10],n = 5) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0],m = 0,nums2 = [-10, -8, -6, -4, -2, 0, 2],n = 7) == None
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],m = 6,nums2 = [2, 2, 2, 2, 2, 2],n = 6) == None
    assert candidate(nums1 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],n = 10) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 0,nums2 = [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13],n = 10) == None
    assert candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 0, 0, 0, 0],m = 8,nums2 = [2, 50, 100, 150],n = 4) == None
    assert candidate(nums1 = [1, 10, 20, 0, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [2, 3, 5, 7, 8, 11, 15],n = 7) == None
    assert candidate(nums1 = [5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16],n = 11) == None
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 6,nums2 = [5, 15, 25, 35, 45, 55, 65],n = 7) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 10) == None
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 0,nums2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],n = 10) == None
    assert candidate(nums1 = [-10, -5, -3, 0, 0, 0, 0, 0],m = 3,nums2 = [-8, -7, -6, -4],n = 4) == None
    assert candidate(nums1 = [1, 4, 7, 10, 13, 0, 0, 0, 0, 0],m = 5,nums2 = [2, 5, 8, 11, 14],n = 5) == None
    assert candidate(nums1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [-2, -2, -2, -2, -2, -2, -2],n = 7) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [0, 6, 7, 8, 9, 10, 11],n = 7) == None
    assert candidate(nums1 = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 5,nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 10) == None
    assert candidate(nums1 = [1000000000, 1000000000, 0, 0, 0, 0, 0, 0, 0, 0],m = 2,nums2 = [-1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000],n = 6) == None
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0],m = 10,nums2 = [-1, -2, -3, -4, -5, -6],n = 6) == None
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 20,nums2 = [],n = 0) == None
    assert candidate(nums1 = [1, 2, 2, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 7,nums2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],n = 11) == None
    assert candidate(nums1 = [100, 200, 300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],m = 3,nums2 = [50, 150, 250, 350, 450, 550],n = 6) == None
