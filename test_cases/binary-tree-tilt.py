# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3])) == 1
    assert candidate(root = tree_node([21, 7, 14, 1, 1, 2, 2, 3, 3])) == 9
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 40
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, None, None, 7, None, 8, 9])) == 55
    assert candidate(root = tree_node([4, 2, 9, 3, 5, None, 7])) == 15
    assert candidate(root = tree_node([1, 2])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3])) == 8
    assert candidate(root = tree_node([1, None, 2])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3])) == 8
    assert candidate(root = tree_node([0])) == 0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == 20
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 41
    assert candidate(root = tree_node([1])) == 0
    assert candidate(root = tree_node([])) == 0
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, 6, None, 7, None, None, 8])) == 131
    assert candidate(root = tree_node([1000, -1000, 500, None, None, -250, 250])) == 2000
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 330
    assert candidate(root = tree_node([5, 3, 9, 1, 4, 8, 10, 0, 2, None, None, None, None, 6, 11])) == 61
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 19
    assert candidate(root = tree_node([1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000])) == 14000
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 35
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 441
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == 647
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, None, None, 6, 7, 8, 9])) == 11
    assert candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 167
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 5, 5, None, None, 6, 6, 7, 7, None, None, 8, 8, 9, 9, None, None, 10, 10])) == 216
    assert candidate(root = tree_node([100, -50, 50, 25, -25, 25, -25, 12, -12, 12, -12, 12, -12, 12, -12])) == 296
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])) == 114
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, 6, 9])) == 43
    assert candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, 8, None, 10, None, 12, None, 14])) == 97
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1120
    assert candidate(root = tree_node([50, 25, 75, 10, 40, 60, 90, 5, 15, 30, 45, 55, 65, 80, 100])) == 585
    assert candidate(root = tree_node([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7])) == 56
    assert candidate(root = tree_node([1, None, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6])) == 0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, 16, None, 17])) == 109
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 440
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1, None, None, -1, None, None, None, None, None])) == 20
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16])) == 57
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 35
    assert candidate(root = tree_node([100, -50, -50, 30, 20, 10, -10, 2, 8, -2, -8, 1, -1, 0, 0])) == 114
    assert candidate(root = tree_node([0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3])) == 0
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, -1, 3, 8, 18, 23, 27, 32, 38])) == 240
    assert candidate(root = tree_node([100, 90, 90, 80, None, None, 80, 70, None, None, 70, 60, None, None, 60, 50, None, None, 50, 40, None, None, 40, 30, None, None, 30, 20, None, None, 20, 10, None, None, 10])) == 2400
    assert candidate(root = tree_node([-10, 15, -3, 7, -8, None, None, 6, 4])) == 54
    assert candidate(root = tree_node([1000, -1000, 500, 250, -250, 0, 0, 125, -125, 62, -62, 31, -31, 15, -15, 7, -7, 3, -3, 1, -1])) == 2488
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 87
    assert candidate(root = tree_node([20, 15, 25, 10, 17, 22, 30, None, None, 13, 19, None, None, 21, 24, 27, 33])) == 227
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5])) == 40
    assert candidate(root = tree_node([1000, -500, -500, 250, 250, -250, -250, 125, 125, 125, 125, -125, -125, -125, -125])) == 2000
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8, 9, 10])) == 94
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 163
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 167
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 35
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1])) == 533
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 215
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 928
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 0
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, None, None, None, None, None, None, 8])) == 6
    assert candidate(root = tree_node([-10, -20, -30, -40, None, -50, -60, -70, None, -80, -90])) == 530
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8])) == 107
    assert candidate(root = tree_node([20, -10, 10, None, 5, 5, None, 3, None, 2])) == 39
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, 26, 27, 28, 29, 30, -1])) == 35
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1])) == 155
    assert candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 35
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 159
    assert candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1, None, None, -1])) == 11
    assert candidate(root = tree_node([9, 4, 20, None, None, 15, 17, 12, None, 6, 18, None, 13, 7, None, None, None, None, None, None])) == 162
    assert candidate(root = tree_node([1, 2, 2, 3, None, 3, None, 4, None, 4, None, 5, None, 5, None, 6, None, 6, None, 7, None, 7, None, 8, None, 8, None, 9, None, 9, None, 10, None, 10])) == 552
    assert candidate(root = tree_node([1000, -1000, 1000, -1000, 1000, -1000, 1000])) == 6000
    assert candidate(root = tree_node([100, -100, 200, -200, 300, -300, 400])) == 1500
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 25, 15, None, None, None, None, 30, None])) == 115
    assert candidate(root = tree_node([1, -2, -3, -4, -5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) == 45
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 301
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, None, None, None, None, None, 6])) == 37
    assert candidate(root = tree_node([5, 14, 3, 7, 13, None, None, 5, 9, None, None, 4, 10, None, None, 2, 8, 11, 12])) == 216
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 132
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, 4, 9, 11, 13, 17, 21, 24, 27])) == 134
    assert candidate(root = tree_node([-1, -2, -3, -4, None, -5, -6, -7, None, -8, None, -9, None, -10])) == 75
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == 22
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, None, None, None, None, 7])) == 32
    assert candidate(root = tree_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100])) == 590
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 20
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 20
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1, None, None, None, None, 8])) == 44
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19])) == 2280
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, None, 7, 8, None, 9, 10, 11, None, 12, None, 13, 14, None, 15, 16, 17, None, 18, None, 19])) == 437
