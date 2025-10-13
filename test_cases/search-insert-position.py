# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [-10, 0, 5, 10],target = 0) == 1
    assert candidate(nums = [1, 2, 4, 6, 7, 9],target = 3) == 2
    assert candidate(nums = [1, 3, 5],target = 4) == 2
    assert candidate(nums = [1, 3, 5, 6],target = 2) == 1
    assert candidate(nums = [-10, -5, -3, 2, 3, 4, 5],target = -4) == 2
    assert candidate(nums = [-10, 0, 10, 20, 30, 40, 50],target = -5) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 0) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11],target = 10) == 5
    assert candidate(nums = [1],target = 1) == 0
    assert candidate(nums = [-10, 0, 10, 20, 30, 40, 50],target = 25) == 4
    assert candidate(nums = [1, 3],target = 2) == 1
    assert candidate(nums = [-10, 0, 5, 10],target = 15) == 4
    assert candidate(nums = [1, 3, 5, 6],target = 7) == 4
    assert candidate(nums = [1, 3, 5, 6],target = 5) == 2
    assert candidate(nums = [1, 3],target = 4) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == 4
    assert candidate(nums = [1, 3, 4, 5, 6, 8, 9, 11, 13, 15],target = 7) == 5
    assert candidate(nums = [1, 2, 4, 6, 8, 10],target = 5) == 3
    assert candidate(nums = [1],target = 0) == 0
    assert candidate(nums = [1],target = 2) == 1
    assert candidate(nums = [-10, -5, -3, 2, 3, 4, 5],target = 3) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == 10
    assert candidate(nums = [1, 3, 5, 6],target = 0) == 0
    assert candidate(nums = [-10, 0, 5, 10],target = -5) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],target = 256) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 5) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],target = 14) == 7
    assert candidate(nums = [10000],target = 9999) == 0
    assert candidate(nums = [-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100],target = -550) == 5
    assert candidate(nums = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 15) == 7
    assert candidate(nums = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10],target = -85) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 12) == 11
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 20) == 10
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 29) == 29
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 155) == 15
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 15) == 7
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 27) == 5
    assert candidate(nums = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41],target = 39) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5.5) == 5
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],target = 27) == 8
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],target = 500000) == 6
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024],target = 200) == 14
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 33) == 6
    assert candidate(nums = [-10000, 10000],target = 10000) == 1
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24],target = 11) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 19) == 18
    assert candidate(nums = [-10000, 10000],target = 0) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 0) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 20) == 10
    assert candidate(nums = [-10, -5, -3, -1, 0, 2, 4, 6, 8, 10],target = -6) == 1
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],target = 26) == 9
    assert candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],target = 145) == 10
    assert candidate(nums = [-10, -5, -3, 0, 4, 8, 12],target = 3) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],target = 12) == 6
    assert candidate(nums = [10000],target = 10001) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],target = 512) == 9
    assert candidate(nums = [-10, -5, 0, 3, 9, 12, 15],target = 1) == 3
    assert candidate(nums = [-500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500],target = -350) == 2
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256],target = 64) == 6
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],target = 50) == 7
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],target = 67) == 13
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 10) == 5
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],target = 59) == 20
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 1) == 0
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 100) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 500) == 4
    assert candidate(nums = [-500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500],target = -250) == 3
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5.5) == 6
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20, 25, 30],target = 12) == 5
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],target = 5500) == 5
    assert candidate(nums = [-1000, -500, -250, -100, -50, -25, -10, -5, -2, -1, 0, 1, 2, 5, 10, 25, 50, 100, 250, 500, 1000],target = -750) == 1
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20],target = -3) == 2
    assert candidate(nums = [1, 3, 5, 7, 9],target = 6) == 3
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 100) == 0
    assert candidate(nums = [1, 10, 100, 1000, 10000],target = 500) == 3
    assert candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],target = -35) == 2
    assert candidate(nums = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59],target = 3) == 1
    assert candidate(nums = [-10, -5, 0, 5, 10],target = -7) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 8) == 7
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],target = 1500) == 1
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19],target = 18) == 6
    assert candidate(nums = [-10000, 10000],target = -10000) == 0
    assert candidate(nums = [-999, -998, -997, -996, -995, -994, -993, -992, -991, -990],target = -993) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],target = 20) == 10
    assert candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024],target = 1024) == 32
    assert candidate(nums = [-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1],target = -10) == 7
    assert candidate(nums = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000],target = -7500) == 3
    assert candidate(nums = [2, 4, 6, 8, 10],target = 5) == 2
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == 11
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],target = 29) == 9
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],target = 93) == 18
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 550) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 20) == 10
    assert candidate(nums = [1, 10, 100, 1000, 10000],target = 5000) == 4
    assert candidate(nums = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],target = 5000) == 15
    assert candidate(nums = [-10, -5, -3, -1, 0, 2, 4, 6, 8, 10],target = -4) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 14) == 7
    assert candidate(nums = [-5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000],target = -2500) == 3
    assert candidate(nums = [-10, -5, 0, 2, 5, 9, 11, 20],target = 3) == 4
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],target = 26) == 9
    assert candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],target = 55000) == 5
    assert candidate(nums = [-500, -250, -100, -50, -25, -10, -5, -2, -1, 0, 1, 2, 5, 10, 25, 50, 100, 250, 500],target = -75) == 3
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 31) == 15
    assert candidate(nums = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = -45) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],target = 44) == 22
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25],target = 15) == 5
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],target = 1024) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],target = 1150) == 11
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],target = 15) == 5
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],target = 100) == 6
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],target = 10000000) == 7
    assert candidate(nums = [100, 200, 300, 400, 500],target = 250) == 2
    assert candidate(nums = [-100, -50, 0, 50, 100],target = -75) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == 14
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 19) == 9
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 257) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],target = 5) == 0
    assert candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024],target = -1) == 0
