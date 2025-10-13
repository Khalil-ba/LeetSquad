# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([0, None, 0, None, 0])) == 1
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, None, 0, 0])) == 1
    assert candidate(root = tree_node([0, 0, None, 0, None, 0, None, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0])) == 2
    assert candidate(root = tree_node([0])) == 1
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, 0, None, 0, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, None, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, None, None, None, 0])) == 2
    assert candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, None, 0, 0, None, 0, 0, 0, None, None, 0, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, 0, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, None, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, 0, None, 0, None, None, 0, None, 0, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None])) == 8
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, None, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 9
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0])) == 7
    assert candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 7
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, None, 0, None, 0, 0, 0, 0, 0, None, None, 0, None, 0, None, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None, None])) == 4
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, None, 0, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, None, 0, 0, 0, None, None, None, 0, 0, 0, None, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, None, 0, 0, None, None, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, None, None, None, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, 0, None, None, 0, 0, None, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, None, None, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, None, None, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0])) == 6
    assert candidate(root = tree_node([0, 0, None, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, None, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, 0, None, 0, None, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 15
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, None, 0, None, 0, None, None, 0, None])) == 3
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, 0, None, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 7
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None])) == 5
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, 0, 0, None, 0])) == 10
    assert candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0])) == 11
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, None, 0, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, None, 0, 0, 0, 0, None, None, None, None, None, None, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0])) == 7
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, 0, None, 0, 0, None, 0, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, None, None, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, None, None, 0, 0, None, None])) == 5
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, None, 0, 0, None, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, None, 0, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, None, 0, None, None, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, 0, 0, None, None, 0, 0, None, 0, None, 0, None, 0, None, 0, None, None, 0, None, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, None, None, None, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, None, 0, None, None, 0, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, None, None, 0, 0, 0, None])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 7
