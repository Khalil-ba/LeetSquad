# Import the utils module for prompts
from utils import *

def check(candidate):
    assert is_same_tree(candidate(root = tree_node([3, 1, 4, None, 2]),low = 1,high = 2), tree_node([1, None, 2]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]),low = 2,high = 8), tree_node([5, 3, 6, 2, 4, None, 8, None, None, None, None, 7]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),low = 3,high = 6), tree_node([5, 3, 6, None, 4]))
    assert is_same_tree(candidate(root = tree_node([3, 1, 4, None, 2]),low = 2,high = 4), tree_node([3, 2, 4]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),low = 2,high = 5), tree_node([5, 3, None, 2, 4]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),low = 3,high = 4), tree_node([3, None, 4]))
    assert is_same_tree(candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),low = 5,high = 13), tree_node([8, 6, 10, None, 7, None, 13]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2]),low = 1,high = 1), tree_node([1]))
    assert candidate(root = tree_node([1, 2, None, 2, None, 3]),low = 2,high = 4) == None
    assert is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),low = 7,high = 15), tree_node([10, 7, 15]))
    assert is_same_tree(candidate(root = tree_node([1]),low = 1,high = 2), tree_node([1]))
    assert is_same_tree(candidate(root = tree_node([1, 0, 2, None, None, 0.5, 1.5]),low = 0.5,high = 1.5), tree_node([1, None, 0.5]))
    assert is_same_tree(candidate(root = tree_node([2, 1, 3]),low = 1,high = 2), tree_node([2, 1]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2]),low = 2,high = 2), tree_node([2]))
    assert is_same_tree(candidate(root = tree_node([3, 0, 4, None, 2, None, None, 1]),low = 1,high = 3), tree_node([3, 2, None, 1]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),low = 3,high = 5), tree_node([5, 3, None, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 0, 2]),low = 1,high = 2), tree_node([1, None, 2]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2]),low = 1,high = 3), tree_node([1, None, 2]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),low = 4,high = 5), tree_node([4, None, 5]))
    assert is_same_tree(candidate(root = tree_node([1, 3, 5, None, None, 2, 4]),low = 2,high = 4), tree_node([2]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),low = 2,high = 4), tree_node([3, 2, 4]))
    assert is_same_tree(candidate(root = tree_node([3, 1, 4, None, 2]),low = 3,high = 4), tree_node([3, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3]),low = 3,high = 3), tree_node([3]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2]),low = 2,high = 4), tree_node([2]))
    assert is_same_tree(candidate(root = tree_node([1, 0, 2, None, None, 1.5, 2.5]),low = 1,high = 2), tree_node([1, None, 2, 1.5]))
    assert is_same_tree(candidate(root = tree_node([1, 0, 2, None, None, 1.5, 3]),low = 1,high = 2), tree_node([1, None, 2, 1.5]))
    assert is_same_tree(candidate(root = tree_node([2, None, 3]),low = 2,high = 2), tree_node([2]))
    assert candidate(root = tree_node([1, 2, 3, 4, 5]),low = 4,high = 5) == None
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),low = 3,high = 4), tree_node([3, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),low = 3,high = 4), tree_node([3, None, 4]))
    assert candidate(root = tree_node([1]),low = 0,high = 0) == None
