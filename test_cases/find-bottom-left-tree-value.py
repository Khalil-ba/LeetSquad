# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([2, 1, 3])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, None, None, 7])) == 7
    assert candidate(root = tree_node([0, None, 1])) == 1
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 15
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 1
    assert candidate(root = tree_node([2, 2, 2, 3, None, 3, None, 4, None, 4, None, 5, None, 5, None, 6])) == 6
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
    assert candidate(root = tree_node([1, -2, -3, -4, None, -5, -6, None, None, None, -7])) == -7
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, None, 6, None, 7])) == 7
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18])) == 3
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 7, None, None, None, None, None, None, 8])) == 4
    assert candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 7, 5, None, None, 8, 6, None, None, None, 11, None, 13, None, None, None, 14])) == 14
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 10
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 6, 7, None, 8, 9, None, None, 10])) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, 9, None, None, None, 10, None, 11])) == 10
    assert candidate(root = tree_node([0, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15])) == -8
    assert candidate(root = tree_node([1, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 9
    assert candidate(root = tree_node([8, 5, 1, 6, 9, None, None, 7, None, 10, 11])) == 7
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 55, 85, 5, 15, 30, 40, 52, 60, 70, 90])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, 11, 12, 13, None, None, None, None, 14])) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9])) == 8
    assert candidate(root = tree_node([100, 50, 150, 25, 75, None, 175, 10, 35, 65, 85, None, None, None, None, None, 200, 15, 40, 60, 80, 90, 110, 130, 180, 250])) == 90
    assert candidate(root = tree_node([8, 15, 1, None, -98, 75, None, 94, 93, None, -82, None, -70, None, -52])) == -70
    assert candidate(root = tree_node([2, 2, 2, 3, None, 3, None, 4, None, 4, None, 5, None, 5, None, 6, None, 6, None, 7, None, 7])) == 7
    assert candidate(root = tree_node([1, None, 3, 2, 4, None, None, 5, None, 6])) == 6
    assert candidate(root = tree_node([1, None, 3, None, None, 2])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, 9])) == 8
    assert candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7])) == -4
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, None, None, 5])) == 4
    assert candidate(root = tree_node([0, -1, -2, -3, None, -4, -5, -6, None, None, None, -7, -8])) == -6
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 7
    assert candidate(root = tree_node([5, 3, 8, 1, 4, None, 9, None, 2, None, None, None, 6, None, 10, 7, None, 11, 12])) == 11
    assert candidate(root = tree_node([20, 15, 25, 10, 17, 22, 30, 5, 12, None, 18, 21, 24, 28, 35, 3, None, 11, 14, 16, None, 19, None, None, 23, 27, 31, None, None, None, None, 33, None, 36, 37])) == 33
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, 15])) == 8
    assert candidate(root = tree_node([25, 20, 30, 15, 22, 28, 35, 10, None, 18, 24, None, None, 26, 29, None, None, 5, None, None, None, None, None, None, 12])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, 9, 10, 11, 12])) == 12
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, 8, None, 16, 18, 19, 21])) == 19
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, None, None, 8])) == 8
    assert candidate(root = tree_node([5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 3
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15
    assert candidate(root = tree_node([2147483647])) == 2147483647
    assert candidate(root = tree_node([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, None, None, 11, 12, None, 13, None, None, 14])) == 13
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, None, None, None, None, None, None, 8, 10])) == 8
    assert candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == -8
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, None, None, None, None, 5.5, 9, 10.5, None, None, 14, 16, 22, None, None, 17, None, None, None, None, None, None, None, None, None, None, 19])) == 19
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, None, 17, 23, None, 27, None, 18])) == 18
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, None, 11, None, 12])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, 0, None, None, 0])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, 9, 10, None, None, 11])) == 11
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 20
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 4
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([2, 3, 4, 5, None, 6, 7, 8, None, None, None, None, None, None, 9])) == 9
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, None, None, None, 10])) == 1
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, None, 18, 28, None, 38, 45])) == 5
    assert candidate(root = tree_node([30, 15, 45, 7, 22, 35, 50, 3, 11, 18, 27, 32, 42, 48, 55, 1, 5, 9, 13, 17, 20, 24, 26, 29, 31, 34, 38, 41, 44, 46, 49, 52, 54, 57, 60, 2, 4, 6, 8, 10, 12, 14, 16, 19, 21, 23, 25, 28, 30, 33, 36, 39, 43, 45, 47, 50, 53, 56, 58, 61, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 62])) == 62
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, 5, None, 7, 10])) == 1
    assert candidate(root = tree_node([-2147483648, None, 2147483647, -2147483647])) == -2147483647
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, None, None, 20, 35, 55, 70, None, None, None, None, None, 105, 130, 135, 145, None, None, 155, 175, 185, None, None, None, None, None, None, None, 7])) == 155
    assert candidate(root = tree_node([1, 2, 3, None, 5, 6, None, 7, 8, 9, 10, None, 11, 12])) == 11
    assert candidate(root = tree_node([1, 2, 2, 3, None, None, 3, 4, 4, None, None, 5, 5])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, None, None, None, 10])) == 8
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, None, None, 5, 5])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, None, None, 9, 10])) == 9
    assert candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85])) == 10
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 9, 11, 13, 17, 20])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11
    assert candidate(root = tree_node([10, 5, 15, None, None, 6, 20, None, None, None, 30, 25, 35])) == 25
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None])) == 8
    assert candidate(root = tree_node([1, None, 2, None, None, 3, None, None, None, 4, None, None, None, None, 5])) == 2
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25])) == 1
    assert candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3, 5, 5, None, None, 6, 6, None, None, 7, 7])) == 7
