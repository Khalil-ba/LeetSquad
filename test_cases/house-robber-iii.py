# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 23
    assert candidate(root = tree_node([3, 2, None, 1, 3, None, 1])) == 7
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 9
    assert candidate(root = tree_node([3, 0, 0])) == 3
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 38
    assert candidate(root = tree_node([3, 4, 5, 1, 3, None, 1])) == 9
    assert candidate(root = tree_node([2, 1, 3, None, 4, None, 7])) == 13
    assert candidate(root = tree_node([2, 1, 3, None, 4])) == 7
    assert candidate(root = tree_node([1, None, 3, 2, 4, None, 5, 6])) == 14
    assert candidate(root = tree_node([3, 2, 3, None, 3, None, 1])) == 7
    assert candidate(root = tree_node([0])) == 0
    assert candidate(root = tree_node([3, None, 4, None, 5])) == 8
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, 3, 18, None, 6, 2, 0, 1, 5, None, None, None, None, 4])) == 59
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 30
    assert candidate(root = tree_node([10, 5, 15, 2, 7, None, 20, 1, None, 6, 8, None, None, None, 9])) == 55
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, 12, 14, 17, 19])) == 97
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 13, 17, 23, 27, 33, 37, 1, 3, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38])) == 418
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7])) == 17
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 5, 5, None, None, 6, 6, 7, 7, 8, 8, 9, 9])) == 63
    assert candidate(root = tree_node([2, 1, 3, None, 4, None, 5, None, 6])) == 13
    assert candidate(root = tree_node([5, 2, 13, None, 5, None, 14, 20, None, None, 9, 10, 3])) == 44
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 980
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, None, 11, 13, None, None, 18, 22])) == 104
    assert candidate(root = tree_node([3, 2, 3, 3, 3, None, 2, None, 1])) == 11
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])) == 80
    assert candidate(root = tree_node([3000, 1000, 2000, 500, 700, None, 3000, None, 600, None, 800, None, 900])) == 7400
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, 9, None, None, 11, 13, None, None, 15, 17])) == 82
    assert candidate(root = tree_node([3, 2, 3, 2, None, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1])) == 16
    assert candidate(root = tree_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])) == 320
    assert candidate(root = tree_node([3, 1, 4, 3, None, 1, 5])) == 12
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9])) == 18
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 13, None, None, None, None, 19])) == 61
    assert candidate(root = tree_node([10, 5, 15, 2, 7, None, 20, 1, None, 6, 8, None, None, None, None, 18])) == 58
    assert candidate(root = tree_node([5, 1, 5, None, 7, 6, None, 4, None, 3, None, 2, 8, None, None, None, 9])) == 35
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, 18, 13, 17, 16, 19, 14, 21, 10, 11, None, 15])) == 137
    assert candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])) == 34
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, None, 20, 17, 21])) == 92
    assert candidate(root = tree_node([6, 3, 7, 2, 5, None, 8, 1, 4, None, None, None, None, None, 9])) == 32
    assert candidate(root = tree_node([8, 4, 13, 2, 6, 10, 14, 1, None, 5, 7, None, None, 9, 12])) == 53
    assert candidate(root = tree_node([3, 2, 3, None, 3, None, 1, 5, 6, 7, 8, 9, 10, 11, 12])) == 63
    assert candidate(root = tree_node([15, 10, 20, 8, None, None, 25, None, None, None, 30])) == 60
    assert candidate(root = tree_node([50, 20, 50, 10, 30, 40, 60, 5, 15, None, None, None, None, None, 70])) == 210
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 368
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 162
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 97
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 6, 8, 9, 12, 14, 17, 19])) == 106
    assert candidate(root = tree_node([10, 5, None, 1, 7, None, 12, 0, 2, 6, 8, None, None, 11, 13, None, None, 3, 4, None, None, None, None, 9, 10])) == 76
    assert candidate(root = tree_node([5, 4, 7, 3, None, 2, 9, None, None, None, 10])) == 27
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 259
    assert candidate(root = tree_node([3, 2, 3, None, 3, None, 1, None, None, 5, 6])) == 17
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, 15, 20, 35, 65, 70, 85, 105, 135, 145, 155, 175, 185, 190])) == 1890
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 6, 8, 12, 14, 17, 9, 11, 2, 4, 16, 19, 20])) == 144
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 8, 12, None, None, 11, None, 10])) == 59
    assert candidate(root = tree_node([3, 2, 3, None, 3, None, 1, 5, 6, 7, 8, 9, 10])) == 45
    assert candidate(root = tree_node([9, 4, 17, 3, 6, 11, 20, 1, 5, 8, 13, None, 22, None, 2, None, None, 0, 2, None, 9, None, None, 7, 12, None, None, None, 2])) == 89
    assert candidate(root = tree_node([2, 1, 3, None, 4, None, 5, 6, None, 7, None, 8, None, 9, None, 10])) == 32
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, None, 10, 11, None, None, None, None, None, 12])) == 49
    assert candidate(root = tree_node([50, 20, 60, 10, 30, 55, 70, 5, 15, 25, 35, 51, 59, 65, 75, 1, 4, 9, 16, 24, 26, 34, 36, 50, 58, 61, 64, 66, 73, 76, 78])) == 891
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 16
    assert candidate(root = tree_node([5, 4, 5, None, 1, 4, None, None, 2, 3])) == 14
    assert candidate(root = tree_node([10, 5, 15, 2, 7, 13, 18, 1, None, 6, 8, 9, 14, None, None, None, 19, None, 20])) == 100
    assert candidate(root = tree_node([5, 3, 7, 2, 5, None, 8, 1, None, 4, None, 6, None, 3, 5])) == 28
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, None, 6, None, 11, 13, None, None, 18, 22, 19, 23, 24, 25, 26, 27, 28, 29, 30])) == 283
    assert candidate(root = tree_node([50, 20, 60, 10, 30, 55, 70, 5, 15, 25, 35, 52, 58, 65, 75, 2, 7, 12, 17, 23, 27, 32, 37, 51, 56, 59, 64, 67, 72, 76, 78])) == 895
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 10, 10, 10, 10, 10, 10, 10, 10])) == 200
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, None, 6, None, None, None, 7])) == 13
    assert candidate(root = tree_node([2, 1, 3, None, 4, None, 5, None, 6, None, 7])) == 17
    assert candidate(root = tree_node([9, 4, 7, 3, 6, 5, 11, 2, 5, None, None, 8, None, 10, 12, None, None, None, None, None, 14])) == 63
    assert candidate(root = tree_node([3, 4, 5, 1, 3, None, 1, 5, 6, None, 2, 8, None, None, None, 9, None, None, 10])) == 41
    assert candidate(root = tree_node([8, 4, 13, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 12, 15])) == 80
    assert candidate(root = tree_node([7, 3, 8, 1, 4, 3, 9, 0, 2, 5, 6, None, None, None, None, None, 11])) == 43
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8])) == 45
    assert candidate(root = tree_node([10, 5, 15, 2, 7, 13, 18, 1, None, 6, 8, 9, 14, 19, 20])) == 97
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 14, 19, None, None, 13, None, None, None, None, None, None, 12])) == 75
    assert candidate(root = tree_node([5, 2, 8, 1, 3, None, 9, 0, None, None, 4, None, None, 6, None, 10])) == 34
    assert candidate(root = tree_node([10, 5, 15, 2, 7, 13, 18, 1, None, 6, 8, None, 14, None, None, 19])) == 77
    assert candidate(root = tree_node([50, 20, 30, 10, 40, None, None, 5, None, None, 55])) == 115
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, 2, None, None, None, 20])) == 45
    assert candidate(root = tree_node([5, 2, 6, 1, 3, None, 8, None, None, 4, 7, None, None, None, 9])) == 30
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 32
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, 11, 12])) == 56
    assert candidate(root = tree_node([7, 3, 8, 1, 4, 5, 9, 0, 2, 6, None, None, None, None, None, None, 10])) == 39
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 49
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 25
    assert candidate(root = tree_node([20, 10, 10, 5, 15, None, None, 3, 7, 12, 18])) == 60
    assert candidate(root = tree_node([8, 4, 13, 2, 6, 10, 17, 1, None, 5, 7, None, 12, None, None, None, 14])) == 65
    assert candidate(root = tree_node([7, 3, 8, 1, 4, 6, 9, 0, 2, 5, None, None, None, None, None, None, None, 10, 11, None, 12, None, 13, 14, 15, None, None, None, None, 16, 17])) == 101
    assert candidate(root = tree_node([3, 2, 3, None, 3, None, 1, 2, None, 4])) == 11
    assert candidate(root = tree_node([50, 20, 50, None, 30, None, 60, 10, 40, None, 70])) == 190
    assert candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6])) == 15
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 35
