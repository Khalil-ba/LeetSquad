# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1
    assert candidate(root = tree_node([1, 1, 1, None, 1, None, None, 1, 1, None, 1])) == 4
    assert candidate(root = tree_node([1])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 1
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, 8, None, None, 9, None, None, 10])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, None, None, None, None, None, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, None, 7, 8, 9, None, 10, None, None, 11, None, None, 12])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, 9, 10])) == 2
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, None, 5, 6, None, 7, None, 8])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 1
    assert candidate(root = tree_node([1, None, 3, 2, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 8
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, None, 5, None, 6, 7, 8, None, None, None, None, 9, 10, 11, 12, 13, 14, 15])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, None, None, None, None, 18, 19, 20, None, None, 21, 22, None, None, 23, 24])) == 4
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 2
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, 7, 8, None, None, 9, None, 10])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, None, 7, None, 8, None, None, None, 9])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, 16])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, 8, None, None, 9, None, 10, None, 11])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, 14, 15, 16, 17, 18, 19, 20])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, 11, None, None, 12, 13, None, None, 14, 15])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, None, 9, None, 10])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, None, None, 7, None, None, 8, None, 9])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 2
    assert candidate(root = tree_node([1, 2, None, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 2
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, 8, 9, None, 10])) == 3
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, None, None, 5])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, None, None, None, 6, 7, 8, 9, 10, 11])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, 7, None, 8, None, None, None, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, None, 17])) == 3
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, None, 5, None, None, 6, None, None, 7])) == 3
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, None, 5, None, 6])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, 7, None, 8, 9, 10, None, None, None, None, 11, 12, 13, 14])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, 8, 9, None, None, None, 10])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, None, 7, None, 8])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 2
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, 6, 7, 8, 9, 10, 11, 12])) == 3
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, 8, None, None, 9, 10, None, None, 11])) == 5
    assert candidate(root = tree_node([1, None, 2, None, 3, 4, None, None, 5, None, None, 6, 7])) == 3
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, 4])) == 1
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, None, None, 10, None, 11, None, 12])) == 2
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, 5, None, 6, None, None, None, 7, None, 8])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, None, 7, None, None, 8, None, None, 9])) == 3
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1
    assert candidate(root = tree_node([1, None, 2, 3, 4, None, 5, 6, None, None, None, None, 7, 8, None, None, 9, 10])) == 6
    assert candidate(root = tree_node([1, 2, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 4
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, None, None, None, 8, 9, None, None, 10, 11])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 1
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 1
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13, None, None, 14, 15])) == 14
    assert candidate(root = tree_node([1, 2, None, None, 3, 4, None, None, 5, None, None, 6, 7, None, None, 8, None, None, 9, 10, None, None, 11, 12])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8, 9, None, None, None, 10, None, None, 11, None, None, 12])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 2
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 1
    assert candidate(root = tree_node([1, 2, None, 3, None, None, 4, None, 5, None, None, 6, None, None, 7, None, None, 8, None, 9])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, 7, None, None, None, None, None, 8, 9, None, None, 10])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == 1
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11])) == 10
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 1
    assert candidate(root = tree_node([1, 2, None, 3, 4, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, None, None, 11])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, None, 10, 11, None, 12, 13, None, 14, 15])) == 3
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, 6, None, None, 7, 8, None, 9, 10, None, None, None, 11, 12, 13, None, 14, None, 15, None, 16, None, 17])) == 5
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, None, 5, 6, None, 7])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, 9, None, None, None, None, 10, 11, 12, None, None, 13, None, None, 14])) == 2
    assert candidate(root = tree_node([1, None, 2, 3, 4, None, None, None, 5, None, 6, None, None, 7, None, 8, None, 9, None, 10])) == 2
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, 6, None, 7])) == 4
