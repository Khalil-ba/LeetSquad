# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(basket1 = [1000000000, 1000000000],basket2 = [1000000000, 1000000000]) == 0
    assert candidate(basket1 = [2, 3, 4, 1],basket2 = [3, 2, 5, 1]) == -1
    assert candidate(basket1 = [1, 1, 2, 2],basket2 = [2, 2, 1, 1]) == 0
    assert candidate(basket1 = [5, 7, 10, 15],basket2 = [15, 10, 7, 5]) == 0
    assert candidate(basket1 = [1, 2, 3],basket2 = [3, 2, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5],basket2 = [5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [1, 3, 5, 7, 9],basket2 = [2, 4, 6, 8, 10]) == -1
    assert candidate(basket1 = [4, 2, 2, 2],basket2 = [1, 4, 1, 2]) == 1
    assert candidate(basket1 = [10, 10, 10, 10],basket2 = [10, 10, 10, 10]) == 0
    assert candidate(basket1 = [100, 200, 300, 400],basket2 = [400, 500, 600, 700]) == -1
    assert candidate(basket1 = [5, 7, 9, 11],basket2 = [11, 9, 7, 5]) == 0
    assert candidate(basket1 = [1, 3, 5, 7],basket2 = [2, 4, 6, 8]) == -1
    assert candidate(basket1 = [1, 2, 3, 4],basket2 = [4, 3, 2, 1]) == 0
    assert candidate(basket1 = [1, 1, 2, 3],basket2 = [1, 1, 3, 2]) == 0
    assert candidate(basket1 = [10, 10, 10, 10],basket2 = [1, 1, 1, 1]) == 2
    assert candidate(basket1 = [5, 5, 5, 5],basket2 = [5, 5, 5, 5]) == 0
    assert candidate(basket1 = [10, 20, 30, 40],basket2 = [40, 30, 20, 10]) == 0
    assert candidate(basket1 = [1, 1, 1, 1],basket2 = [1, 1, 1, 1]) == 0
    assert candidate(basket1 = [1, 3, 5, 7, 9, 11, 13, 15],basket2 = [15, 13, 11, 9, 7, 5, 3, 1]) == 0
    assert candidate(basket1 = [100, 200, 300, 400, 500],basket2 = [500, 400, 300, 200, 100]) == 0
    assert candidate(basket1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5],basket2 = [5, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1]) == 0
    assert candidate(basket1 = [3, 5, 7, 9, 11],basket2 = [9, 11, 5, 7, 3]) == 0
    assert candidate(basket1 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4],basket2 = [1, 1, 2, 2, 2, 2, 3, 3, 4, 4]) == -1
    assert candidate(basket1 = [1, 2, 2, 3, 3, 4, 5, 5, 5, 6],basket2 = [6, 5, 5, 4, 3, 3, 2, 2, 1, 1]) == -1
    assert candidate(basket1 = [1000000000, 999999999, 1, 2],basket2 = [1000000000, 999999999, 3, 4]) == -1
    assert candidate(basket1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],basket2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
    assert candidate(basket1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],basket2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(basket1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],basket2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],basket2 = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == 0
    assert candidate(basket1 = [1, 3, 5, 7, 9, 11],basket2 = [2, 4, 6, 8, 10, 12]) == -1
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],basket2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],basket2 = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]) == 0
    assert candidate(basket1 = [1, 1, 2, 3, 4, 5, 6, 7, 8],basket2 = [8, 7, 6, 5, 4, 3, 2, 1, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],basket2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],basket2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == -1
    assert candidate(basket1 = [3, 5, 6, 7, 8, 9],basket2 = [9, 8, 7, 6, 5, 3]) == 0
    assert candidate(basket1 = [1000000000, 1000000000, 1, 1],basket2 = [1, 1, 1000000000, 1000000000]) == 0
    assert candidate(basket1 = [3, 3, 3, 3, 3, 3],basket2 = [1, 1, 1, 1, 1, 1]) == 3
    assert candidate(basket1 = [1, 2, 3, 4, 5],basket2 = [6, 7, 8, 9, 10]) == -1
    assert candidate(basket1 = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],basket2 = [6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]) == 0
    assert candidate(basket1 = [1, 3, 5, 7, 9],basket2 = [9, 7, 5, 3, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],basket2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(basket1 = [1, 2, 2, 3, 4, 5],basket2 = [5, 4, 3, 2, 2, 6]) == -1
    assert candidate(basket1 = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5],basket2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(basket1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],basket2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 5
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],basket2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 0
    assert candidate(basket1 = [1, 1, 1, 2, 2, 3],basket2 = [1, 1, 1, 2, 2, 3]) == 0
    assert candidate(basket1 = [5, 5, 5, 5, 5],basket2 = [5, 5, 5, 5, 5]) == 0
    assert candidate(basket1 = [2, 2, 2, 2, 3, 3, 3, 3],basket2 = [1, 1, 1, 1, 4, 4, 4, 4]) == 6
    assert candidate(basket1 = [9, 7, 5, 3, 1],basket2 = [1, 3, 5, 7, 9]) == 0
    assert candidate(basket1 = [1, 2, 2, 3, 4, 5],basket2 = [5, 4, 3, 2, 2, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],basket2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(basket1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],basket2 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == -1
    assert candidate(basket1 = [1, 1, 2, 3, 4, 5],basket2 = [2, 3, 4, 5, 5, 5]) == 1
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],basket2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(basket1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],basket2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(basket1 = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],basket2 = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(basket1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],basket2 = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 0
    assert candidate(basket1 = [5, 7, 9, 11, 13, 15],basket2 = [15, 13, 11, 9, 7, 5]) == 0
    assert candidate(basket1 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4],basket2 = [4, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1]) == 0
    assert candidate(basket1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],basket2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 0
    assert candidate(basket1 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],basket2 = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(basket1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],basket2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],basket2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],basket2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 0
    assert candidate(basket1 = [1, 3, 5, 7, 9, 11, 13, 15],basket2 = [2, 4, 6, 8, 10, 12, 14, 16]) == -1
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6],basket2 = [6, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],basket2 = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],basket2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(basket1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],basket2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0
    assert candidate(basket1 = [5, 10, 15, 20, 25, 30, 35, 40],basket2 = [40, 35, 30, 25, 20, 15, 10, 5]) == 0
    assert candidate(basket1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],basket2 = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],basket2 = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],basket2 = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]) == -1
    assert candidate(basket1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],basket2 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],basket2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5]) == 0
    assert candidate(basket1 = [3, 6, 8, 8, 10],basket2 = [10, 8, 6, 3, 8]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],basket2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],basket2 = [5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 0
    assert candidate(basket1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],basket2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],basket2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(basket1 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],basket2 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(basket1 = [1, 3, 5, 7, 9, 11, 13],basket2 = [13, 11, 9, 7, 5, 3, 1]) == 0
    assert candidate(basket1 = [1000000000, 1000000000, 1000000000, 1000000000],basket2 = [1, 1, 1, 1]) == 2
    assert candidate(basket1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],basket2 = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],basket2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 11]) == -1
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],basket2 = [1, 1, 1, 1, 1, 10, 10, 10, 10, 10]) == -1
    assert candidate(basket1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],basket2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8],basket2 = [8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [10, 20, 30, 40, 50, 60],basket2 = [60, 50, 40, 30, 20, 10]) == 0
    assert candidate(basket1 = [1, 2, 2, 3, 4, 5, 5, 6],basket2 = [6, 5, 5, 4, 3, 2, 2, 1]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],basket2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(basket1 = [1, 3, 5, 7, 9, 11, 13, 15],basket2 = [15, 13, 11, 9, 7, 5, 3, 1]) == 0
    assert candidate(basket1 = [5, 10, 15, 20, 25],basket2 = [25, 20, 15, 10, 5]) == 0
    assert candidate(basket1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],basket2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == -1
    assert candidate(basket1 = [10, 20, 30, 40, 50],basket2 = [50, 40, 30, 20, 10]) == 0
    assert candidate(basket1 = [1000000000, 1000000000, 1000000000],basket2 = [1, 1, 1]) == -1
    assert candidate(basket1 = [2, 2, 3, 3, 4, 4],basket2 = [4, 4, 3, 3, 2, 2]) == 0
    assert candidate(basket1 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],basket2 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == -1
    assert candidate(basket1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],basket2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],basket2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(basket1 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],basket2 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 0
    assert candidate(basket1 = [7, 7, 7, 8, 9],basket2 = [9, 8, 7, 7, 7]) == 0
    assert candidate(basket1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],basket2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 0
    assert candidate(basket1 = [1, 1, 1, 2, 2, 3],basket2 = [1, 1, 1, 2, 3, 3]) == -1
    assert candidate(basket1 = [1, 3, 5, 7, 9],basket2 = [2, 4, 6, 8, 10]) == -1
    assert candidate(basket1 = [1, 1, 2, 3, 4, 5, 6, 7],basket2 = [7, 6, 5, 4, 3, 2, 1, 1]) == 0
    assert candidate(basket1 = [10, 20, 30, 40, 50],basket2 = [5, 15, 25, 35, 45]) == -1
    assert candidate(basket1 = [1, 2, 2, 3, 4],basket2 = [1, 2, 2, 3, 4]) == 0
