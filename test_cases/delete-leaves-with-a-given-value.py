# Import the utils module for prompts
from utils import *

def check(candidate):
    assert is_same_tree(candidate(root = tree_node([1, 2, None, 2, None, 2]),target = 2), tree_node([1]))
    assert candidate(root = tree_node([1000, 1000, 1000, 1000, 1000, 1000, 1000]),target = 1000) == None
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, 10]),target = 5), tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, 10]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 2, None, 2, 4]),target = 2), tree_node([1, None, 3, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 2, 2, 4, 2, None, 2, None, 2, None, 2]),target = 2), tree_node([1, 2, 3, 4, None, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 3, 3, 3, 2]),target = 3), tree_node([1, 3, None, None, 2]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, None, 4]),target = 4), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),target = 15), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]),target = 3), tree_node([1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3]),target = 4), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),target = 2), tree_node([1]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),target = 2), tree_node([1, None, 3, 4, 5]))
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3]),target = 2), tree_node([1, None, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),target = 7), tree_node([1, 2, 3, 4, 5, 6]))
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),target = 2), tree_node([1, None, 3]))
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),target = 10), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, 11, 12, 13, 14, 15]))
    assert is_same_tree(candidate(root = tree_node([1, None, 3, None, 4, 5, None, 6, 7]),target = 2), tree_node([1, None, 3, None, 4, 5, None, 6, 7]))
    assert candidate(root = tree_node([1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),target = 5), tree_node([1, 2, 3, None, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 4]),target = 2), tree_node([1, None, 3, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, None, 3, 3, 3]),target = 3), tree_node([1]))
    assert is_same_tree(candidate(root = tree_node([1, None, 3, 2, 2, None, 4, 2, None, 2]),target = 2), tree_node([1, None, 3, 2, None, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),target = 3), tree_node([1, 2, 3, 4, 5, 6, 7]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 2]),target = 2), tree_node([1, None, 3]))
    assert candidate(root = tree_node([1, None, 1, 1, 1, 1, 1, 1]),target = 1) == None
