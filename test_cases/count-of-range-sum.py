# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3],lower = -5,upper = 5) == 24
    assert candidate(nums = [100, 200, 300, 400, 500],lower = 150,upper = 1000) == 11
    assert candidate(nums = [-1, -2, -3, -4, -5],lower = -10,upper = -5) == 7
    assert candidate(nums = [1, 2, 3, 4, 5],lower = 1,upper = 5) == 7
    assert candidate(nums = [100, 100, 100, 100, 100],lower = 200,upper = 400) == 9
    assert candidate(nums = [0, 0, 0, 0, 0],lower = 0,upper = 0) == 15
    assert candidate(nums = [-2, 5, -1],lower = -2,upper = 2) == 3
    assert candidate(nums = [5, 5, 5, 5, 5],lower = 10,upper = 20) == 9
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],lower = -2000000000,upper = 2000000000) == 10
    assert candidate(nums = [2147483647, -2147483648, -1, 0],lower = -1,upper = 1) == 4
    assert candidate(nums = [1, 2, 3],lower = 3,upper = 6) == 4
    assert candidate(nums = [0],lower = 0,upper = 0) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5],lower = -10,upper = -1) == 12
    assert candidate(nums = [-1, -2, -3, -4, -5],lower = -10,upper = -3) == 10
    assert candidate(nums = [2147483647, -2147483648, 2147483647, -2147483648],lower = -4294967295,upper = 4294967295) == 10
    assert candidate(nums = [3, -2, 1, 5, 4],lower = -3,upper = 7) == 11
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1],lower = -1,upper = 1) == 55
    assert candidate(nums = [1, 2, 3, 4, 5],lower = 1,upper = 10) == 12
    assert candidate(nums = [1, -1, 1, -1, 1, -1],lower = 0,upper = 1) == 15
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 0,upper = 0) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1],lower = -15,upper = -5) == 37
    assert candidate(nums = [100, -50, 200, -150, 300, -200, 400, -250, 500, -300],lower = 100,upper = 600) == 39
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = -1,upper = 1) == 55
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],lower = 15,upper = 25) == 21
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],lower = 100,upper = 200) == 24
    assert candidate(nums = [1, -1, 1, -1, 1, -1],lower = 0,upper = 1) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 15,upper = 30) == 19
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],lower = 500000000,upper = 2000000000) == 19
    assert candidate(nums = [5, 4, 3, 2, 1],lower = 2,upper = 7) == 8
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],lower = 1500,upper = 3500) == 23
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20],lower = -20,upper = 20) == 210
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],lower = -100,upper = -50) == 60
    assert candidate(nums = [-10, -20, -30, -40, -50],lower = -150,upper = -50) == 10
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -200,upper = -100) == 14
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = -2,upper = 2) == 55
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = -1,upper = 1) == 55
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = 0,upper = 2) == 40
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000],lower = -500,upper = 500) == 40
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 100,upper = 500) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 15,upper = 30) == 19
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -500,upper = -100) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = 50,upper = 100) == 40
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = -2,upper = 2) == 55
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],lower = 5000000000,upper = 6000000000) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],lower = 1500,upper = 3000) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 10,upper = 20) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 5,upper = 20) == 24
    assert candidate(nums = [-1000000000, -1000000000, -1000000000, -1000000000, -1000000000],lower = -6000000000,upper = -5000000000) == 1
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000],lower = -500,upper = 500) == 145
    assert candidate(nums = [100, 200, 300, 400, 500],lower = 150,upper = 1200) == 12
    assert candidate(nums = [100000000, 200000000, 300000000, 400000000, 500000000],lower = 500000000,upper = 1500000000) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 5,upper = 10) == 21
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = -5,upper = 5) == 465
    assert candidate(nums = [10, 20, 30, 40, 50],lower = 100,upper = 150) == 4
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],lower = -50,upper = 50) == 55
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],lower = -5,upper = 5) == 55
    assert candidate(nums = [5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1],lower = 0,upper = 10) == 72
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],lower = -200,upper = 0) == 206
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -30,upper = -15) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1],lower = 5,upper = 15) == 37
    assert candidate(nums = [5, -1, 5, -1, 5, -1, 5, -1, 5, -1],lower = 1,upper = 9) == 32
    assert candidate(nums = [1000000000, 1000000000, -2000000000, 0, 1000000000, -1000000000],lower = -5000000000,upper = 5000000000) == 21
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],lower = -10,upper = 10) == 55
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 25,upper = 45) == 13
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 150,upper = 450) == 30
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -30,upper = -15) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],lower = 55,upper = 100) == 73
    assert candidate(nums = [1, -100, 100, -10000, 10000, -1000000, 1000000, 1, -1, 10, -10],lower = -1000000,upper = 1000000) == 64
    assert candidate(nums = [1, 2, 3, -6, 2, 3, -6, 2, 3],lower = 1,upper = 5) == 23
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5],lower = -10,upper = 10) == 55
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = -1,upper = 1) == 55
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -450,upper = -150) == 30
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -5,upper = 5) == 90
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 0,upper = 0) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 200) == 206
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 0,upper = 5) == 40
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000],lower = -2000000000,upper = 2000000000) == 21
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = -1,upper = 1) == 210
    assert candidate(nums = [30, -10, 20, -20, 10, -10, 20, -20, 10, -10, 20, -20, 10, -10, 20, -20, 10, -10, 20, -20],lower = 0,upper = 20) == 135
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 15,upper = 30) == 31
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 5,upper = 15) == 19
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 3,upper = 7) == 30
    assert candidate(nums = [1000000000, 500000000, -1500000000, 2000000000, -2000000000, 1000000000],lower = -3000000000,upper = 3000000000) == 21
    assert candidate(nums = [100000000, 200000000, 300000000, -100000000, -200000000, -300000000],lower = 100000000,upper = 500000000) == 10
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -20,upper = -10) == 14
    assert candidate(nums = [100, 200, 300, 400, 500],lower = 500,upper = 1500) == 10
    assert candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10, -10, 10],lower = -20,upper = 20) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],lower = 0,upper = 10) == 27
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],lower = 5000000000,upper = 10000000000) == 21
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -20,upper = -5) == 24
    assert candidate(nums = [2147483647, -2147483647, 2147483647, -2147483647, 2147483647],lower = -4294967295,upper = 4294967295) == 15
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000],lower = -5000000000,upper = 15000000000) == 24
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = 0,upper = 0) == 25
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],lower = -10,upper = 0) == 27
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -15,upper = -5) == 19
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],lower = -10,upper = 10) == 54
    assert candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000],lower = 0,upper = 1) == 16
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],lower = 10000000000,upper = 15000000000) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 50,upper = 100) == 60
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1],lower = -1,upper = 1) == 55
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 0,upper = 0) == 55
