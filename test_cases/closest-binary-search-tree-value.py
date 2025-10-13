# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),target = 13.0) == 13
    assert candidate(root = tree_node([3, 1, 4, None, 2]),target = 0.285714) == 1
    assert candidate(root = tree_node([2, 1, 3]),target = 2.235714) == 2
    assert candidate(root = tree_node([8, 5, 14, 3, 7, 12, 20, 1, 4, 6, 9, 11, 13, 17, 21]),target = 7.871429) == 8
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),target = 9.1) == 10
    assert candidate(root = tree_node([1, None, 3]),target = 2.5) == 3
    assert candidate(root = tree_node([3, 1, 4, None, 2]),target = 3.456789) == 3
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),target = 6.5) == 7
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),target = 3.5) == 3
    assert candidate(root = tree_node([10, 5, 15, 2, 7, None, 18]),target = 6.123456) == 7
    assert candidate(root = tree_node([2, 1, 3]),target = 1.0) == 1
    assert candidate(root = tree_node([1, 0, 2]),target = 1.642857) == 2
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),target = 6.123456) == 7
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),target = 7.234) == 7
    assert candidate(root = tree_node([1, 0, 2]),target = 1.0) == 1
    assert candidate(root = tree_node([4, 2, 5, 1, 3, None, None, None, None, None, 6]),target = 3.642857) == 4
    assert candidate(root = tree_node([1]),target = 1.0) == 1
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25]),target = 14.75) == 15
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),target = 4.56) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),target = 6.1234) == 7
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25]),target = 14.789) == 15
    assert candidate(root = tree_node([2, 1, 3, 0]),target = 0.185714) == 0
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20]),target = 8.0) == 7
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20]),target = 8.23) == 9
    assert candidate(root = tree_node([5, 4, 6, None, None, 3, None]),target = 4.890123) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),target = 8.542857) == 10
    assert candidate(root = tree_node([1]),target = 4.428571) == 1
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),target = 3.285714) == 3
    assert candidate(root = tree_node([3, 1, 4, None, 2]),target = 2.0) == 2
    assert candidate(root = tree_node([1, 0, 15, None, -1, None, 22]),target = 1.5) == 1
    assert candidate(root = tree_node([3, 1, 4, None, 2]),target = 3.0) == 3
    assert candidate(root = tree_node([3, 1, 4, None, 2]),target = 0.25) == 1
    assert candidate(root = tree_node([8, 4, 10, 2, 6, None, None, 1, 3, 5, 7]),target = 5.0) == 5
    assert candidate(root = tree_node([4, 2, 5, 1, 3]),target = 3.714286) == 4
    assert candidate(root = tree_node([7, 3, 9, None, 5, None, 11, None, None, 4, 6]),target = 6.914286) == 7
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),target = 5.4321) == 5
    assert candidate(root = tree_node([4, 2, 5, 1, 3, None, None, 0]),target = 3.892041) == 4
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),target = 3.0) == 3
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),target = 2.0) == 2
    assert candidate(root = tree_node([2, 1, 3]),target = 2.571429) == 3
    assert candidate(root = tree_node([10, 5, 15, 2, 7, None, 17]),target = 9.142857) == 10
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1]),target = 3.6) == 4
    assert candidate(root = tree_node([5, 2, 8, 1, 3, None, None, None, 4]),target = 4.5) == 5
    assert candidate(root = tree_node([25, 18, 30, 15, 22, 27, 35, 13, 17, 21, 23, 26, 29, 32, 37]),target = 24.567) == 25
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),target = 2.9) == 3
