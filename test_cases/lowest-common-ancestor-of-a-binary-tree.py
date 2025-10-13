# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 1) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 2,q = 7) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 6,q = 8) == None
    assert candidate(root = tree_node([37, -34, -48, None, -100, -101, 48, None, None, None, None, -54, None, -71, -22, None, None, None, 8]),p = -100,q = -101) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 4) == None
    assert candidate(root = tree_node([3, 1, 4, None, 2]),p = 2,q = 1) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 6,q = 4) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 0,q = 5) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 3,q = 0) == None
    assert candidate(root = tree_node([30, 15, 18, 3, 17, 19, 20, 1, 16, None, None, None, 14, 15, None, None, 9, 11]),p = 3,q = 17) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 6,q = 2) == None
    assert candidate(root = tree_node([3, 1, 4, None, 2]),p = 2,q = 3) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 0,q = 8) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 3,q = 5) == None
    assert candidate(root = tree_node([2, 1]),p = 2,q = 1) == None
    assert candidate(root = tree_node([1, 2]),p = 1,q = 2) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 7,q = 4) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 2,q = 4) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 2,q = 8) == None
    assert candidate(root = tree_node([37, -34, -48, None, -100, -100, 48, None, None, None, None, -54, None, -71, -22, None, None, None, 8]),p = -100,q = 48) == None
