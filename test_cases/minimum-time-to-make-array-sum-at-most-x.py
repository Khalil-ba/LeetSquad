# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums1 = [1, 2, 3],nums2 = [1, 2, 3],x = 4) == 3
    assert candidate(nums1 = [5, 3, 8],nums2 = [2, 1, 4],x = 15) == 1
    assert candidate(nums1 = [5, 5, 5],nums2 = [1, 1, 1],x = 15) == 0
    assert candidate(nums1 = [10, 10, 10],nums2 = [0, 0, 0],x = 30) == 0
    assert candidate(nums1 = [1, 1, 1],nums2 = [0, 0, 0],x = 0) == 3
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1],x = 25) == 0
    assert candidate(nums1 = [100, 200, 300],nums2 = [10, 20, 30],x = 1000) == 0
    assert candidate(nums1 = [3, 3, 3],nums2 = [1, 2, 3],x = 10) == 0
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 3, 3],x = 4) == -1
    assert candidate(nums1 = [10, 20, 30],nums2 = [0, 0, 0],x = 15) == 2
    assert candidate(nums1 = [100, 200],nums2 = [50, 100],x = 1000) == 0
    assert candidate(nums1 = [10, 20, 30],nums2 = [0, 0, 0],x = 10) == 2
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],x = 10) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2],x = 10) == 0
    assert candidate(nums1 = [2, 4, 6],nums2 = [1, 1, 1],x = 12) == 0
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [1, 2, 3, 4],x = 100) == 0
    assert candidate(nums1 = [5, 3, 1],nums2 = [2, 1, 3],x = 10) == 0
    assert candidate(nums1 = [7, 5, 3],nums2 = [2, 4, 6],x = 20) == 0
    assert candidate(nums1 = [1, 2],nums2 = [3, 4],x = 5) == 0
    assert candidate(nums1 = [3, 2, 1],nums2 = [1, 1, 1],x = 5) == 1
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5],x = 25) == 0
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],x = 4) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5],x = 150) == 0
    assert candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1],x = 1) == -1
    assert candidate(nums1 = [3, 3, 3],nums2 = [1, 1, 1],x = 5) == 3
    assert candidate(nums1 = [999, 998, 997, 996, 995],nums2 = [1, 2, 3, 4, 5],x = 4500) == 1
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [5, 5, 5, 5, 5],x = 5) == 0
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [0, 0, 0, 0],x = 1000) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 5) == -1
    assert candidate(nums1 = [10, 20, 30],nums2 = [1, 2, 3],x = 50) == 1
    assert candidate(nums1 = [10, 20, 30],nums2 = [0, 0, 0],x = 15) == 2
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 5000) == 1
    assert candidate(nums1 = [10, 20, 30],nums2 = [1, 2, 3],x = 60) == 0
    assert candidate(nums1 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 50) == 10
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],x = 4) == 0
    assert candidate(nums1 = [1, 10, 100, 1000],nums2 = [1000, 100, 10, 1],x = 2000) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1],x = 20) == -1
    assert candidate(nums1 = [50, 100, 150, 200],nums2 = [1, 2, 3, 4],x = 300) == 2
    assert candidate(nums1 = [1000, 1000, 1000],nums2 = [1, 1, 1],x = 2500) == 1
    assert candidate(nums1 = [10, 10, 10, 10, 10],nums2 = [5, 5, 5, 5, 5],x = 25) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 550) == 0
    assert candidate(nums1 = [10, 10, 10, 10],nums2 = [1, 2, 3, 4],x = 30) == 2
    assert candidate(nums1 = [5, 10, 15, 20],nums2 = [1, 1, 1, 1],x = 15) == 3
    assert candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [1, 1, 1, 1, 1],x = 50) == 3
    assert candidate(nums1 = [999, 998, 997, 996, 995],nums2 = [1, 2, 3, 4, 5],x = 5000) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 20, 30, 40, 50],x = 100) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 100) == 0
    assert candidate(nums1 = [100, 200, 300],nums2 = [10, 20, 30],x = 1500) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],x = 5) == 0
    assert candidate(nums1 = [500, 500, 500],nums2 = [1, 1, 1],x = 1000) == 2
    assert candidate(nums1 = [1000, 1000, 1000, 1000, 1000],nums2 = [1000, 1000, 1000, 1000, 1000],x = 5000) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 1, 1, 1, 1],x = 5) == -1
    assert candidate(nums1 = [3, 6, 9],nums2 = [2, 4, 6],x = 20) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [9, 8, 7, 6, 5],x = 10) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 100) == -1
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],x = 0) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 55) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 50) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],x = 200) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [5, 4, 3, 2, 1],x = 5) == 0
    assert candidate(nums1 = [1000, 500, 250, 125, 62, 31],nums2 = [62, 31, 15, 7, 3, 1],x = 2000) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [1, 2, 3, 4, 5],x = 100) == 0
    assert candidate(nums1 = [100, 200, 300],nums2 = [10, 20, 30],x = 1000) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 10) == 0
    assert candidate(nums1 = [5, 10, 15, 20],nums2 = [2, 4, 6, 8],x = 50) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [0, 0, 0, 0, 0],x = 15) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 5000) == 0
    assert candidate(nums1 = [100, 100, 100],nums2 = [50, 50, 50],x = 300) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],x = 550) == 0
    assert candidate(nums1 = [100, 200, 300],nums2 = [0, 0, 0],x = 150) == 2
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [0, 0, 0, 0, 0],x = 50) == 3
    assert candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [5, 4, 3, 2, 1],x = 50) == 3
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [1, 2, 3, 4],x = 500) == 2
    assert candidate(nums1 = [9, 9, 9, 9],nums2 = [1, 2, 3, 4],x = 50) == 0
    assert candidate(nums1 = [1000, 1000, 1000],nums2 = [1000, 1000, 1000],x = 3000) == 0
    assert candidate(nums1 = [100, 150, 200, 250, 300],nums2 = [5, 10, 15, 20, 25],x = 2000) == 0
    assert candidate(nums1 = [999, 999, 999],nums2 = [1000, 1000, 1000],x = 2997) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 55) == 0
    assert candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [0, 1, 2, 3, 4],x = 30) == 3
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5],x = 50) == 3
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5],x = 15) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 600) == 0
    assert candidate(nums1 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 5500) == 0
    assert candidate(nums1 = [50, 50, 50, 50],nums2 = [0, 0, 0, 0],x = 150) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1],x = 20) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 4, 3, 2, 1],x = 100) == 2
    assert candidate(nums1 = [10, 20, 30],nums2 = [5, 0, 0],x = 30) == 2
    assert candidate(nums1 = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],x = 10000) == 0
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [1, 2, 3, 4],x = 100) == 0
    assert candidate(nums1 = [10, 10, 10, 10, 10],nums2 = [0, 0, 0, 0, 0],x = 10) == 4
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 2, 3, 4, 5],x = 1500) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 4, 3, 2, 1],x = 150) == 0
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9],x = 50) == 0
    assert candidate(nums1 = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 5000) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [0, 0, 0, 0, 0],x = 150) == 0
    assert candidate(nums1 = [500, 500, 500, 500, 500],nums2 = [0, 1, 2, 3, 4],x = 2000) == 2
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1],x = 50) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [0, 0, 0, 0, 1000],x = 1500) == 0
    assert candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [1, 2, 3, 4, 5],x = 150) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 5, 5, 5, 5],x = 200) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 100) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 55) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [100, 100, 100, 100, 100],x = 500) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [1, 1, 1, 1, 1],x = 50) == 2
    assert candidate(nums1 = [100, 200, 300],nums2 = [5, 10, 15],x = 600) == 0
    assert candidate(nums1 = [999, 999, 999],nums2 = [1, 1, 1],x = 2995) == 1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 500) == 1
    assert candidate(nums1 = [100, 200, 300],nums2 = [5, 10, 15],x = 500) == 1
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9],x = 45) == 0
    assert candidate(nums1 = [7, 14, 21, 28],nums2 = [1, 1, 1, 1],x = 50) == 1
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 1, 1, 1, 1],x = 1500) == 0
