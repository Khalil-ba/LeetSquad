# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([3, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 3, 0, 0, 4])) == 8
    assert candidate(root = tree_node([1, 0, 0, None, 3, 0, 0])) == 8
    assert candidate(root = tree_node([1, 0, 0, None, 3, 0, 0, None, 4])) == 17
    assert candidate(root = tree_node([1, 0, 2])) == 2
    assert candidate(root = tree_node([1, 0, 0, None, 3])) == 4
    assert candidate(root = tree_node([0, 0, 0, 3, 3])) == 8
    assert candidate(root = tree_node([0, 3, 0])) == 3
    assert candidate(root = tree_node([1, 0, 0, None, 3, 0, 2])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 9])) == 25
    assert candidate(root = tree_node([2, 0, 1, 3, 0, 0, 0, None, None, None, 1])) == 7
    assert candidate(root = tree_node([0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 29
    assert candidate(root = tree_node([0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])) == 29
    assert candidate(root = tree_node([1, 0, 0, 2, 0, 0, 1, None, 2, 0, 0, 0, 0, 1, 0])) == 22
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3])) == 18
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 7])) == 16
    assert candidate(root = tree_node([4, 1, 1, 1, 1, 1, 1])) == 0
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9])) == 39
    assert candidate(root = tree_node([3, 0, 0, 1, 0, 0, 0, None, None, 2, 0, 0, 0, 0, 0])) == 22
    assert candidate(root = tree_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 31
    assert candidate(root = tree_node([0, 3, 0, 0, 0, 2, 0, None, None, 0, 0, 0, 1])) == 12
    assert candidate(root = tree_node([2, 3, 3, None, None, None, 4, 0, 0, None, None, 5, 0, 0, None])) == 17
    assert candidate(root = tree_node([0, 1, 1, 2, 0, 0, 0, None, None, 0, 0, 1, 0, 0, 0])) == 21
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9])) == 84
    assert candidate(root = tree_node([1, 0, 0, 0, 0, 2, 2, None, None, 0, 0, 0, 0, 1, 0])) == 17
    assert candidate(root = tree_node([0, 1, 0, 0, 3, 0, 0, None, None, None, 0, 0, 0, 0, 5])) == 17
    assert candidate(root = tree_node([5, 3, None, 3, None, 2, 1])) == 9
    assert candidate(root = tree_node([5, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 28
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 0, 0, 0, 0])) == 23
    assert candidate(root = tree_node([2, 3, 0, 3, 0, None, 2, None, 0])) == 6
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 17
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 8])) == 23
    assert candidate(root = tree_node([0, 0, 0, 3, 0, 0, 2, None, 0, 0, 0, 1])) == 13
    assert candidate(root = tree_node([5, 0, 0, 0, 4, 0, 0, None, None, 3, 0, 0, 0, 2, 0])) == 23
    assert candidate(root = tree_node([5, 2, 2, 1, 0, 0, 3, None, None, 0, 0, 0, 0])) == 14
    assert candidate(root = tree_node([0, 0, 3, 0, 0, 0, 0, None, 4])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10])) == 42
    assert candidate(root = tree_node([1, 2, 2, None, 4, 1, 2, None, None, None, 1, None, None, 1, 2])) == 14
    assert candidate(root = tree_node([3, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 31
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 0
    assert candidate(root = tree_node([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1])) == 28
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 0])) == 27
    assert candidate(root = tree_node([1, 0, 0, 0, 1, 0, 0, None, 3, 0, 0, 0, 0, 0, 2])) == 22
    assert candidate(root = tree_node([0, 2, 0, 0, 0, 3, 0, None, None, 0, 0, 0, 0, 0, 1])) == 17
    assert candidate(root = tree_node([0, 2, 0, 0, 0, 0, 7])) == 14
    assert candidate(root = tree_node([0, 0, 0, 4, 0, 0, 0, None, 0, 2, 0, 0, 0, 0, 2])) == 19
