# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 3
    assert candidate(root = tree_node([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == 3
    assert candidate(root = tree_node([2, None, 3, None, 4, None, 5, None, 6])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == 3
    assert candidate(root = tree_node([1, 2])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, None, 9, 10])) == 2
    assert candidate(root = tree_node([0])) == 1
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 2
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([])) == 0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
    assert candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, None, 5, None, None, 6])) == 2
    assert candidate(root = tree_node([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7])) == 3
    assert candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, None, 6, None, 7, None, 8])) == 2
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, None, None, None, None, None, None, None, None, None, None])) == 3
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, None, 18])) == 2
    assert candidate(root = tree_node([1, None, None, 2, None, None, 3, None, None, 4, None, None, 5])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, None, None, None, None, 8])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, None, 5, None, None, None, None, None, 6, None, None, None, None, None, 7, None, None, None, None, None, 8, None, None, None, None, None, 9, None, None, None, None, None, 10, None, None, None, None, None, 11])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, None, None, None, None, 6])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, 6, 7, None, 8])) == 3
    assert candidate(root = tree_node([3, 9, 20, 15, 7, 25, 28, 30, None, None, None, 29, 31])) == 3
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5, None, None, None, None, 6, None, None, None, None, 7])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 10, 11, 12, 13, None, None, 16, 17, 18, 19])) == 3
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4])) == 2
    assert candidate(root = tree_node([3, 9, 20, None, 1, 15, 7, None, None, 14, 6, None, 8])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, None, None, None, 7, 8, None, None, 9, None])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, None, 6, None, None, 7])) == 2
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30])) == 30
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 6
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, 8, 9, None, 10])) == 4
    assert candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, None, 14, None, None, None, None, 15, None, None, None, None, 16, None, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, 20])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7])) == 4
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, None, None, 4, None, 5])) == 3
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, 16])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, None, 10, 11])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 5
    assert candidate(root = tree_node([1, None, None, 2, None, None, None, 3])) == 1
    assert candidate(root = tree_node([1, None, 2, None, None, None, None, 3, None, None, None, None, None, 4, None, None, None, None, None, 5])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, None, None, None, 6, None, None, None, None, None, 7, None, None, None, None, None, 8, None, None, None, None, None, 9])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 16])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, 12, None, 14])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6])) == 2
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, 9, None, None, 10])) == 3
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 4
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, 4, None, 5, None, 6, None, 7])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 8
    assert candidate(root = tree_node([10, 5, 15, None, 7, None, 18, None, 8, None, 20, 16, 22])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == 7
    assert candidate(root = tree_node([1, 2, None, 4, None, None, 5, None, 6, None, 7, None, 8])) == 7
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, None, None, None, None, 5, 5])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == 13
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13])) == 2
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == 2
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 7, None, None, None, None, None, 8])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 7, None, 9])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, None, None, None, 7, None, None, None, None, None, 8, None, None, None, None, None, 9, None, None, None, None, None, 10, None, None, None, None, None, 11, None, None, None, None, None, 12, None, None, None, None, None, 13])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 6
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, None, None, 16, 18, 17])) == 2
    assert candidate(root = tree_node([3, 9, None, 8, None, None, 10, None, None, None, None, 11, None, None, None, None, 12])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 12
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == 16
    assert candidate(root = tree_node([1, None, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7])) == 1
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, None, 5, None, None, None, None, None, 6])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, 10, None, None, 11])) == 4
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, 6, 7, None, None, 8, 9, None, None, 10, 11, None, 12, None, 13])) == 6
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 13
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, None, None, None, None, None, 14])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, None, None, 5, 5])) == 2
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 14, 6, None, None, None, 8])) == 2
    assert candidate(root = tree_node([42])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, 8, None, None, None, 9])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, 9, None, 10, None, 11, None, 12])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13])) == 2
    assert candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == 3
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, None, 12])) == 12
