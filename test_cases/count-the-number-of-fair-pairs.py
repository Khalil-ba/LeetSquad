# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000],lower = 0,upper = 0) == 2
    assert candidate(nums = [0, 1, 7, 4, 4, 5],lower = 3,upper = 6) == 6
    assert candidate(nums = [5, 5, 5, 5, 5],lower = 10,upper = 10) == 10
    assert candidate(nums = [-1, 0, 1, 2, 3],lower = 0,upper = 4) == 8
    assert candidate(nums = [-1, 0, 1, 2, 3],lower = -2,upper = 2) == 6
    assert candidate(nums = [10, 20, 30, 40, 50],lower = 50,upper = 70) == 6
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000],lower = -1500000000,upper = 1500000000) == 6
    assert candidate(nums = [-1, 0, 1, 2, 3],lower = 0,upper = 2) == 5
    assert candidate(nums = [1, 7, 9, 2, 5],lower = 11,upper = 11) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 5,upper = 15) == 37
    assert candidate(nums = [5, 5, 5, 5, 5],lower = 10,upper = 10) == 10
    assert candidate(nums = [-1, 0, 1, 2, 3],lower = 0,upper = 2) == 5
    assert candidate(nums = [-10, -20, -30, -40, -50],lower = -80,upper = -50) == 7
    assert candidate(nums = [1, 2, 3, 4, 5],lower = 5,upper = 8) == 7
    assert candidate(nums = [-1, 0, 1, 2, 3],lower = 0,upper = 4) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 1,upper = 38) == 189
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 0,upper = 0) == 190
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 50,upper = 150) == 37
    assert candidate(nums = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10],lower = -150,upper = -50) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = 10,upper = 20) == 64
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 10,upper = 30) == 37
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000, -250000000],lower = -1000000000,upper = 1000000000) == 11
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],lower = 15,upper = 35) == 57
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 0],lower = -1000000000,upper = 1000000000) == 8
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000, -250000000, 750000000, -750000000, 125000000, -125000000],lower = -1500000000,upper = 1500000000) == 43
    assert candidate(nums = [5, -5, 15, -15, 25, -25, 35, -35, 45, -45],lower = -50,upper = 50) == 37
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],lower = 15,upper = 20) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 5,upper = 10) == 18
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 10,upper = 28) == 35
    assert candidate(nums = [-1000000000, 1000000000, 0, -500000000, 500000000],lower = -1500000000,upper = 1500000000) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],lower = 3,upper = 7) == 34
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],lower = -10,upper = 10) == 55
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 2,upper = 2) == 45
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 10,upper = 20) == 21
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],lower = 10,upper = 20) == 18
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 1,upper = 38) == 45
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],lower = -50,upper = 50) == 24
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -150,upper = -50) == 37
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],lower = 10,upper = 50) == 97
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],lower = 100,upper = 300) == 149
    assert candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],lower = -50,upper = 50) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 5,upper = 15) == 37
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 30,upper = 170) == 43
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],lower = 500,upper = 1500) == 37
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],lower = 20,upper = 80) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = 10,upper = 20) == 64
    assert candidate(nums = [5, 2, 8, 3, 1, 9, 6, 4, 7, 10],lower = 5,upper = 15) == 37
    assert candidate(nums = [1, 2, 3, 4, 5],lower = 3,upper = 9) == 10
    assert candidate(nums = [10, 20, 30, 40, 50],lower = 50,upper = 80) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 2,upper = 2) == 105
    assert candidate(nums = [-5, -4, -3, -2, -1],lower = -8,upper = -2) == 9
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],lower = 5,upper = 10) == 37
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000, -250000000],lower = -1500000000,upper = 1500000000) == 15
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 1,upper = 2) == 190
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],lower = 1000,upper = 2000) == 29
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],lower = 20,upper = 20) == 105
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 15,upper = 18) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 100,upper = 200) == 29
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 10,upper = 20) == 21
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 0],lower = -1500000000,upper = 1500000000) == 10
    assert candidate(nums = [5, -5, 15, -15, 25, -25, 35, -35, 45, -45],lower = -30,upper = 30) == 27
    assert candidate(nums = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10],lower = 6,upper = 12) == 40
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -200,upper = -100) == 29
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],lower = 5000,upper = 15000) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 18,upper = 20) == 26
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 0,upper = 0) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 10,upper = 30) == 149
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000],lower = -1500000000,upper = 1500000000) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 15,upper = 20) == 9
    assert candidate(nums = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40],lower = 10,upper = 60) == 37
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 2,upper = 2) == 190
    assert candidate(nums = [5, -5, 15, -15, 25, -25, 35, -35],lower = -20,upper = 20) == 16
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -20,upper = -10) == 29
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 20,upper = 30) == 84
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 30,upper = 40) == 30
    assert candidate(nums = [1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10],lower = 6,upper = 12) == 49
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = 5,upper = 15) == 47
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 190,upper = 200) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 18,upper = 30) == 25
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],lower = 1000,upper = 1900) == 29
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],lower = 5,upper = 10) == 23
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -150,upper = -50) == 37
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],lower = 3,upper = 19) == 188
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],lower = 5,upper = 15) == 37
    assert candidate(nums = [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19],lower = -20,upper = -10) == 21
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],lower = 100,upper = 200) == 35
    assert candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9],lower = -18,upper = 18) == 45
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 50,upper = 150) == 37
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 0,upper = 0) == 45
