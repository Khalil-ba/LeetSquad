# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 4
    assert candidate(root = tree_node([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 4
    assert candidate(root = tree_node([3, 1, 4, None, 2])) == 3
    assert candidate(root = tree_node([1, 2, 3])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == 4
    assert candidate(root = tree_node([1, 2, None, 4, 5])) == 2
    assert candidate(root = tree_node([1, 2])) == 1
    assert candidate(root = tree_node([4, -7, -3, None, None, -9, -3, 9, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])) == 8
    assert candidate(root = tree_node([4, 2, None, 3, None, 1])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5])) == 3
    assert candidate(root = tree_node([3, 1, 2])) == 2
    assert candidate(root = tree_node([1])) == 0
    assert candidate(root = tree_node([1, None, 2, None, 3])) == 2
    assert candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 9
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8])) == 7
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, None, None, None, None, 6])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, 11, 12, 13, 14, 15, None, None, None, None, 16])) == 8
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, None, 8, 9, None, None, None, None, 10])) == 6
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, 8, 9])) == 6
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 8
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, None, None, None, None, 5, None, None, None, None, 6])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8])) == 6
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, None, 4, None, 6, 7, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, 6, 7, None, None, 8, None, None, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 10, 11, None, None, 12, 13])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, None, 7, 8, None, None, 9, None, None, 10, 11])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, None, 10, 11])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, None, None, 9, None, None, None, None, 10, None, None, None, None, 11])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None, 10, 11])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, None, None, None, 7, None, None, 8, None, None, None, None, None, None, 9, None, None, 10])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, None, None, 6, 7, None, 8, None, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, None, 6])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, None, None, 11, 12])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, None, 7, None, 8])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, None, None, None, None, None, None, 4, None, None, None, None, 5])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, None, 6, None, None, 7, None, None, 8, None, 9])) == 5
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, None, 4, None, None, None, None, 5, None, None, None, None, None, 6])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13])) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, 10, None, 11, None, 12])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, 12, 13])) == 7
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 6
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9])) == 5
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, 10, None, None, 11, None, None, 12])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, None, 9, 10, 11])) == 7
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, 7, 8, 9, None, None, 10])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 7
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 9
    assert candidate(root = tree_node([1, 2, None, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 11
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, None, 12, 13])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, 10, 11, 12])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 11
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, 10, 11, 12, 13, 14, 15])) == 7
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7])) == 6
