# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5
    assert candidate(root = tree_node([1, None, 3, None, 4])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7])) == 2
    assert candidate(root = tree_node([3, 2, None, 1])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == 4
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 1
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([1, None, 2, 3, 4])) == 3
    assert candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5])) == 4
    assert candidate(root = tree_node([2, 1, 3])) == 3
    assert candidate(root = tree_node([3, 2, 1, 4, 5, 6, 7])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 6, 7])) == 2
    assert candidate(root = tree_node([1, 3, 2, 4])) == 2
    assert candidate(root = tree_node([1, 2, 3])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9
    assert candidate(root = tree_node([1, 3, 2, None, None, 5, 4])) == 2
    assert candidate(root = tree_node([1, 2, None, 3, None, 4])) == 4
    assert candidate(root = tree_node([1, None, 3, None, 4, None, 5])) == 3
    assert candidate(root = tree_node([2, 3, 2, None, 1])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 2
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 2
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, None, 9])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
    assert candidate(root = tree_node([5, 4, 6, 3, 7, None, 8, 2, None, None, 9, None, None, 1])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == 2
    assert candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == 1
    assert candidate(root = tree_node([10, 9, 11, 8, 10, 12, 13, 7, 9, 11, 13, 14, 15, 6, 8, 10, 12, 14, 16, 17])) == 6
    assert candidate(root = tree_node([3, 2, 4, None, None, 1, 5, None, None, None, None, None, 6, 7])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9])) == 2
    assert candidate(root = tree_node([1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 2, None, None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None, 4, None, None, None, None, None, None, None, None, 5])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15
    assert candidate(root = tree_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, 16, 17, None, 18, None, 19, None, None, 20, None, 21, None, None, 22, None, None, 23])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
    assert candidate(root = tree_node([10, 9, 11, 8, 10, 12, 13, 7, None, None, None, None, None, None, 14])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, None, None, None, None, None, 11])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7, 8, 9, 10, 11, 12, 13])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 2
    assert candidate(root = tree_node([30, 20, 31, 10, 29, 32, 40, 5, None, 28, None, None, 33, None, 41, None, None])) == 4
    assert candidate(root = tree_node([1, 3, 2, 4, None, 5, 6, None, None, 7, 8, None, None, 9, 10, None, None, None, None, None, 11, 12, None, None, 13, 14, None, None, None, None, None, 15, 16])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, 10, None, None, 11, 12, None, None, None, 13, 14])) == 2
    assert candidate(root = tree_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28, 31, 30])) == 2
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 12, 18, 22, 28, 32, 38, 0, 2, 6, 8, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39])) == 3
    assert candidate(root = tree_node([3, 2, 4, 1, None, None, 5, 0, None, None, 6, None, None, None, 7])) == 8
    assert candidate(root = tree_node([10, 9, 11, 8, 10, 12, 13, 7, 9, 11, 12, 13, 14, 15, 16, 6, 17, 18, 19, 20, 14, 21, 22, 23, 24])) == 8
    assert candidate(root = tree_node([3, 2, 4, 1, None, 5, 6, None, None, None, 7])) == 5
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, None, 3, 5, None, None, 4, 6, None, None, 2, 4, 6, None, None, 3, 5, 7, None, None, 4, 6, None, None, None])) == 5
    assert candidate(root = tree_node([1, 3, 2, 5, 3, 4, 8, 7, 6, 4, 5, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 2
    assert candidate(root = tree_node([3, 2, None, 1, None, None, 4, None, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14, None, None, 15])) == 3
    assert candidate(root = tree_node([3, 1, 5, 0, 2, 4, 6, -1, None, None, None, 3, None, None, 7, None, -2, None, None, -3, None, 8, None, 9])) == 5
    assert candidate(root = tree_node([5, 4, 6, 3, 7, None, 8, 2, 9, None, None, None, None, None, None, None, None, 10, 11])) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 13, 17, None, None, None, None, None, None, None, 14, 16, 19, 12])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, 9])) == 2
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, None, None, 7, None, None, 8, None, None, 9])) == 4
    assert candidate(root = tree_node([10, 9, 11, 8, 10, 12, 13, 7, 9, 11, 13, 14, 15, 6, 8, 10, 12, 14, 16, 17, 5, 7, 9, 11, 13, 15, 17, 18, 19, 20])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, 9, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 2
    assert candidate(root = tree_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 2
    assert candidate(root = tree_node([1, 3, 2, None, 5, 4, None, 6, 7, None, None, 8, 9, None, None, 10, 11])) == 2
    assert candidate(root = tree_node([5, 2, 6, 1, 3, None, None, None, None, 4])) == 4
    assert candidate(root = tree_node([3, 2, 4, 1, None, 5, 6, None, None, None, None, 7, 8])) == 5
    assert candidate(root = tree_node([3, 2, 1, 4, 5, 0, -1, -2, None, None, -3, -4, None, -5, None, -6, None, None, None, None, None, None, -7])) == 2
    assert candidate(root = tree_node([1, 3, 2, 4, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10])) == 2
    assert candidate(root = tree_node([2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == 15
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == 2
    assert candidate(root = tree_node([5, 4, 6, 3, 4, 5, 7, 2, None, None, None, 6, 8])) == 6
    assert candidate(root = tree_node([10, 9, 11, 8, 10, 12, 13, 7, 9, 11, 12, 13, 14, 15])) == 7
    assert candidate(root = tree_node([5, 4, 6, 3, 4, 5, 7, 2, 3, 4, 5, 6, 8, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 2
    assert candidate(root = tree_node([1, 2, 3, 2, 3, 4, 5, None, None, 1, 2, 3, 4, 5, 6])) == 3
    assert candidate(root = tree_node([5, 4, 6, 3, 7, 2, 8, 1, None, None, None, None, 9, 0, 16])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 3, 4, 8, 7, 6, 4, 5, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])) == 2
    assert candidate(root = tree_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 2
    assert candidate(root = tree_node([2, 1, 3, 4, 6, 5, 7, 8, 10, 9, 11, None, None, None, None, None, None, 12, 13])) == 3
    assert candidate(root = tree_node([10, 9, 11, None, 10, None, 12, None, None, 11, None, 13, None, None, None, 14, None, None, None, None, 15, None, None, None, None, 16])) == 4
    assert candidate(root = tree_node([1, None, 3, 2, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12])) == 2
    assert candidate(root = tree_node([10, 9, 11, 8, 10, 10, 12, 7, 9, 11, 11, 11, 13, 6, 8, 10, 10, 10, 10, None, None, None, None, 12, None, None, None, None, None, None, None, None, 14])) == 6
    assert candidate(root = tree_node([1, None, 3, None, None, 2, 4, 5, 6, None, None, None, None, None, 7])) == 1
    assert candidate(root = tree_node([5, 3, 7, 1, 4, 6, 9, 0, 2, None, None, 5, 8, None, None, None, None, None, 10])) == 3
    assert candidate(root = tree_node([5, 4, 6, 3, None, 7, 8, 2, None, 9, 10, None, None, 1, None, None, 11])) == 7
    assert candidate(root = tree_node([3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1])) == 2
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 4
    assert candidate(root = tree_node([10, 9, 11, 8, 10, None, 12, 7, None, 9, None, 11, None, 6, None, 8, None, 10, None, None, None, None, None, 5])) == 7
    assert candidate(root = tree_node([5, 3, 7, 1, 4, 6, 8, 0, 2, None, None, None, None, None, None])) == 3
    assert candidate(root = tree_node([1, 2, 4, 3, 5, None, 7, 6, 8, None, None, 9, 10, None, None, 11])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 2
    assert candidate(root = tree_node([1, 3, 2, 5, 3, 4, 8, 7, None, 6, 4, 5, 9, 8, 10])) == 2
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 14, 16, 13, 17, 12, 18, 11, 19, 10, 20])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13, None, None, 14, 15])) == 2
    assert candidate(root = tree_node([3, 1, 4, None, 2, None, 5, None, 3, None, 6, None, 7, None, 8, None, 9, None, 10])) == 4
    assert candidate(root = tree_node([30, 25, 40, 20, 28, 35, 45, 15, 22, 26, 32, 34, 42, 48, 50, 10, 18, 21, 23, 27, 29, 31, 33, 36, 37, 41, 43, 47, 49, None, None, 51, 52])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 13
    assert candidate(root = tree_node([5, None, 4, None, 3, None, 2, None, 1, None, None, None, None, None, None, None, None])) == 5
    assert candidate(root = tree_node([3, 2, 1, 4, None, None, 5, None, None, None, None, 6, None, None, None, None, 7])) == 2
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9
    assert candidate(root = tree_node([5, 4, 6, 3, 5, 7, 9, 2, None, 5, 8, 10, 11])) == 6
    assert candidate(root = tree_node([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 2
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 2, 4, None, 7, None, 8])) == 2
    assert candidate(root = tree_node([5, 4, 6, 3, None, 7, 8, 2, None, None, 9, 10, 11, 1, None, None, None, None, 12])) == 7
    assert candidate(root = tree_node([5, 2, 6, 1, 3, None, None, None, 4, None, None, None, 7])) == 3
    assert candidate(root = tree_node([3, 2, 1, 4, 5, 0, -1, -2, None, None, -3, -4, None, -5, None, -6, None, None, None, None, None, None, -7, None, None, None, None, None, None, -8, None, None, None, None, None, -9, None, None, None, None, None, -10, None, None, None, None, None, None, -11])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 2
    assert candidate(root = tree_node([3, 2, 1, 4, 5, 0, None, None, 6, 7, None, 8, 9, None, None, None, None, None, 10])) == 2
