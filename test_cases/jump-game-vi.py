# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
    assert candidate(nums = [1, -1, -2, 4, -7, 3],k = 2) == 7
    assert candidate(nums = [10, -5, -2, 4, 0, 3],k = 3) == 17
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 4) == -6
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 50
    assert candidate(nums = [-10000, -10000, -10000, -10000, -10000],k = 2) == -30000
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 2) == -9
    assert candidate(nums = [5, -1, 5],k = 2) == 10
    assert candidate(nums = [1],k = 1) == 1
    assert candidate(nums = [5, 4, 3, 2, 1],k = 1) == 15
    assert candidate(nums = [100, -100, 100, -100, 100],k = 2) == 300
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 5) == 50000
    assert candidate(nums = [5, 6, -4, 2, 1],k = 3) == 14
    assert candidate(nums = [1, -5, -20, 4, -1, 3, -6, -3],k = 2) == 0
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 15
    assert candidate(nums = [-5, -1, -5],k = 1) == -11
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 2) == 4000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 9
    assert candidate(nums = [1000, -500, 2000, -100, 4000, -200, 3000, -300, 5000, -400],k = 5) == 14600
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == -16
    assert candidate(nums = [1, -10, 5, 6, -4, -5, 10, 1, 2],k = 4) == 25
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 55
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == -19
    assert candidate(nums = [5, -1, -2, -3, -4, -5, 6, -1, 2, -3, -4, -5, 10],k = 5) == 22
    assert candidate(nums = [1000, -2000, 3000, -4000, 5000, -6000, 7000, -8000, 9000],k = 6) == 25000
    assert candidate(nums = [10, 20, 30, 40, 50, -60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 4) == 1140
    assert candidate(nums = [3, 2, -6, 5, 0, -3, 2, 1],k = 3) == 13
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 5500
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 550
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55
    assert candidate(nums = [10000, -5000, 5000, 6000, -2000, 3000, 7000, -8000, 4000, 10000],k = 5) == 45000
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 4) == 29
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 5) == 9
    assert candidate(nums = [1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1000],k = 10) == 2000
    assert candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 5) == 40000
    assert candidate(nums = [1, -10, 5, 6, -2, 3, 7, -8, 4, 10],k = 3) == 36
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 550
    assert candidate(nums = [10000, -9999, 10000, -9999, 10000, -9999, 10000, -9999, 10000, -9999],k = 2) == 40001
    assert candidate(nums = [5, -1, 3, -2, 7, 1, -4, 8, -3, 2],k = 4) == 26
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == 0
    assert candidate(nums = [3, -2, -2, 2, -1, 2, 1, -5, 4],k = 3) == 12
    assert candidate(nums = [100, -100, 100, -100, 100, -100, 100],k = 2) == 400
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 5) == 4000
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],k = 3) == 1000
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 4) == 7
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 10) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 210
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 15) == 1
    assert candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10],k = 2) == 55
    assert candidate(nums = [3, -1, 2, -5, 6, 2, -1, 4],k = 4) == 17
    assert candidate(nums = [1, -5, 4, 2, -2, -1, 3, 1, -1, 2, -3, 4, -5, 6],k = 3) == 23
    assert candidate(nums = [5, -10, 4, -2, 3, 100, -100, 200, -200, 300],k = 4) == 612
    assert candidate(nums = [10, 5, 2, 7, 8, 9, 3, 5, 2, 1, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5],k = 3) == 102
    assert candidate(nums = [10, -5, -20, 4, -1, 3, -6, -3, 5, 2],k = 4) == 24
    assert candidate(nums = [1, -10, 100, -1000, 10000],k = 3) == 10101
    assert candidate(nums = [-1, -5, -2, -4, -10, -20],k = 2) == -27
    assert candidate(nums = [5, -10, 15, -20, 25, -30, 35, -40, 45, -50, 55, -60, 65, -70, 75, -80],k = 5) == 240
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 15
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 3) == -220
    assert candidate(nums = [3, -1, -1, -1, 10, 5],k = 2) == 17
    assert candidate(nums = [10, -1, 10, -1, 10, -1, 10, -1, 10, -1],k = 5) == 49
    assert candidate(nums = [3, -1, 2, 1, -4, 2, 3, -5, 4],k = 4) == 15
    assert candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6],k = 4) == 187
    assert candidate(nums = [1, -5, 10, 20, -30, 5, 15],k = 4) == 51
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 55
    assert candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125, 62, -62, 31, -31],k = 5) == 1937
    assert candidate(nums = [5, 3, 2, 1, 7, 6, 4, 8, 9],k = 3) == 45
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = 10) == -110
    assert candidate(nums = [1, -10, 2, -20, 3, -30, 4, -40, 5, -50],k = 4) == -35
    assert candidate(nums = [100, -50, 200, -300, 400, -500, 600, -700, 800],k = 3) == 2100
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 4
    assert candidate(nums = [100, -50, -100, 200, -300, 400, 500],k = 3) == 1200
    assert candidate(nums = [10000, -5000, 2000, -1000, 5000, 2000, -2000, 3000, 4000, -1000],k = 3) == 25000
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20],k = 5) == 109
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 20
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 210
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 5) == 50
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 20) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 55
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10],k = 2) == 40
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 4) == 10
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150],k = 3) == -460
    assert candidate(nums = [100, 200, 300, 400, 500],k = 5) == 1500
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 5) == 1000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 55
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
