# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),p = 2,q = 3) == 1
    assert candidate(root = tree_node([5]),p = 5,q = 5) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 15) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5]),p = 4,q = 3) == 3
    assert candidate(root = tree_node([1]),p = 1,q = 1) == 0
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, 9, 10]),p = 2,q = 10) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),p = 4,q = 5) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 14,q = 10) == 6
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),p = 13,q = 14) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 14) == 5
    assert candidate(root = tree_node([2, 1]),p = 1,q = 2) == 1
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 2,q = 1) == 1
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 5) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 1,q = 15) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, None, 4]),p = 2,q = 4) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7]),p = 2,q = 6) == 4
    assert candidate(root = tree_node([5, 1, 4, None, 2, None, 3]),p = 3,q = 2) == 4
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9]),p = 2,q = 6) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 11) == 4
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),p = 1,q = 15) == 6
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 0) == 3
    assert candidate(root = tree_node([2, 3, None, 1]),p = 2,q = 1) == 2
    assert candidate(root = tree_node([0, 1, 1, -1, -1, -1, -1]),p = 1,q = -1) == 3
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),p = 3,q = 7) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 2,q = 6) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7]),p = 4,q = 7) == 3
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 7) == 2
    assert candidate(root = tree_node([1, 2]),p = 1,q = 2) == 1
    assert candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8]),p = 3,q = 7) == 3
    assert candidate(root = tree_node([2, 1, 3]),p = 1,q = 3) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9]),p = 8,q = 9) == 2
