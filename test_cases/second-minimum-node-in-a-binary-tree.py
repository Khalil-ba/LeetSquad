# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3])) == -1
    assert candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])) == -1
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == -1
    assert candidate(root = tree_node([2, 2, 5, None, None, 5, 7])) == 5
    assert candidate(root = tree_node([5, 5, 6, 5, 6])) == 6
    assert candidate(root = tree_node([3, 3, 4, 3, 3, None, None, 3, None, None, None])) == 4
    assert candidate(root = tree_node([1, 1, 3, 1, 1, 3, 4])) == 3
    assert candidate(root = tree_node([2, 2, 2])) == -1
    assert candidate(root = tree_node([7, 7, 8, 7, 7, 7, 9])) == 8
    assert candidate(root = tree_node([10, 10, 15, 10, None, 11, 15])) == 11
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5])) == 5
    assert candidate(root = tree_node([3, 3, 5, 3, 3, 6, 7])) == 5
    assert candidate(root = tree_node([1, 1, 3, 1, 1, 3, 4, 3, 1])) == 3
    assert candidate(root = tree_node([5, 5, 5, 5, 5])) == -1
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 3])) == 2
    assert candidate(root = tree_node([8, 8, 9, 8, 8, 10, 11, 8, None, None, 8, 9, None, 9, None, 11])) == 9
    assert candidate(root = tree_node([1, 1, 3, 1, 1, 4, 6, 1, 1, 1, 1, 5, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 3
    assert candidate(root = tree_node([8, 8, 9, 8, 8, 8, 10, 8, 8, None, None, 8, None, None, None, None, None, 8, None, None, None])) == 9
    assert candidate(root = tree_node([15, 15, 16, 15, 15, 15, 17, 15, 15, 15, 15, 15, 15, 15, 18, 15, 15, 15, 15, 15, 15, 15, 15, 15, 19])) == 16
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 3, 4, 2, 2, None, None, 2, 5, 2, 6, 2, 2, None, None, None, None, 2, 2, None, None, None, None, None, 2])) == 3
    assert candidate(root = tree_node([15, 15, 20, 15, 15, 25, 30, 15, 15, 15, 15, 35, 40, 15, 45])) == 20
    assert candidate(root = tree_node([8, 8, 9, 8, 8, 9, 10, 8, 8, 8, 8, 9, 9, 10, 11, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10])) == 9
    assert candidate(root = tree_node([1, 1, 4, 1, 1, 2, 5, 1, 1, None, None, 1, None, None, None, None, None, 1, None, None, None])) == 2
    assert candidate(root = tree_node([6, 6, 7, 6, 6, 8, 9, 6, 6, None, None, 6, 10, 6, 11, 6, 6, None, None, None, None, 6, 6, None, None, None, None, None, 6])) == 7
    assert candidate(root = tree_node([5, 5, 7, 5, 5, 8, 9, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 7
    assert candidate(root = tree_node([1, 1, 3, 1, 1, 5, 7, 1, 1, 9, 11, 1, 1, 1, 1])) == 3
    assert candidate(root = tree_node([4, 4, 6, 4, 4, 7, 9, 4, 4, 4, 4, 4, 4, 4, 4])) == 6
    assert candidate(root = tree_node([2, 2, 3, 2, 2, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 3
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 3, 4, 1, 1, 5, 6])) == 2
    assert candidate(root = tree_node([10, 10, 15, 10, 10, 12, 20, 10, 10, None, None, 12, 13, None, None, 14, None, None])) == 12
    assert candidate(root = tree_node([11, 11, 12, 11, 11, 13, 14, 11, None, 11, 11, None, None, 12, None])) == 12
    assert candidate(root = tree_node([7, 7, 8, 7, 7, 9, 10, 7, 7, 7, 7, 7, 7, 7, 7])) == 8
    assert candidate(root = tree_node([9, 9, 12, 9, 9, 15, 18, 9, 9, 9, 9, 21, 24, 9, 27])) == 12
    assert candidate(root = tree_node([5, 5, 6, 5, 5, None, 5, 5, 5, None, 5, 5, 5, None, 5])) == 6
    assert candidate(root = tree_node([2, 2, 3, 2, 2, 3, 4, 2, 2, 2, 2, 3, 3, 4, 5])) == 3
    assert candidate(root = tree_node([3, 3, 4, 3, 3, 5, 6, 3, 3, None, None, 3, None, None, None, None, None, 3, None, None, None])) == 4
    assert candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 4])) == 2
    assert candidate(root = tree_node([9, 9, 10, 9, 9, 11, 12, 9, None, 9, 9, None, None, 10, None])) == 10
    assert candidate(root = tree_node([12, 12, 13, 12, 12, 14, 15, 12, None, 12, 12, None, None, 13, None])) == 13
    assert candidate(root = tree_node([6, 6, 7, 6, 6, 8, 9, 6, None, None, 6, 7, None, 7, None, 9])) == 7
    assert candidate(root = tree_node([5, 5, 10, 5, 5, 10, 15, 5, 5, 10, 15, 20, None, None, None, None, None, None])) == 10
    assert candidate(root = tree_node([5, 5, 6, 5, 5, 6, 7])) == 6
    assert candidate(root = tree_node([10, 10, 10, 10, 10, 10, 11, 10, 10, None, None, 10, 12, 10, 13])) == 11
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4])) == 4
    assert candidate(root = tree_node([6, 6, 8, 6, 6, 9, 11, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])) == 8
    assert candidate(root = tree_node([6, 6, 9, 6, 6, 8, 9, 6, 6, 7, 8, 9, 10, 6, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, None])) == 7
    assert candidate(root = tree_node([8, 8, 9, 8, 8, 10, 11, 8, None, 8, 8, None, None, 9, None])) == 9
    assert candidate(root = tree_node([6, 6, 7, 6, 6, 7, 8, 6, 6, 6, 6, 7, 7, 8, 9])) == 7
    assert candidate(root = tree_node([9, 9, 10, 9, 9, 11, 12, 9, None, None, 9, 10, None, 10, None, 12, 9, None, 10])) == 10
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 3, 4, 1, 1, 1, 1, 5, 6, 1, 7])) == 2
    assert candidate(root = tree_node([4, 4, 8, 4, 4, 7, 10, 4, 4, 5, 7, 8, 10, 4, None, None, 4, None, None, 5, None, None, 7, None, None, 8, None, None, None])) == 5
    assert candidate(root = tree_node([7, 7, 8, 7, 7, 8, 9, 7, None, None, 7, 8, None, 8, None])) == 8
    assert candidate(root = tree_node([7, 7, 8, 7, 7, 9, 10, 7, 7, 7, 7, 7, 7, 11, 12])) == 8
    assert candidate(root = tree_node([3, 3, 6, 3, 3, 7, 8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == 6
    assert candidate(root = tree_node([6, 6, 8, 6, 6, 10, 12, 6, 6, 6, 6, 14, 16, 6, 18])) == 8
    assert candidate(root = tree_node([1, 1, 3, 1, 1, 4, 5, 1, 1, 1, 1, 2, 6])) == 2
    assert candidate(root = tree_node([10, 10, 11, 10, 10, 10, 12, 10, 10, 10, 10, 10, 10, 10, 13])) == 11
    assert candidate(root = tree_node([4, 4, 5, 4, 4, 5, 6])) == 5
    assert candidate(root = tree_node([2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 5])) == 3
    assert candidate(root = tree_node([3, 3, 6, 3, 3, 9, 12, 3, 3, 3, 3, 15, 18, 3, 21])) == 6
    assert candidate(root = tree_node([1, 1, 3, 1, 1, 2, 4, 1, 1, None, None, 1, None, None, None, None, None, 1, None, None, None])) == 2
    assert candidate(root = tree_node([6, 6, 7, 6, 6, 8, 9, 6, 6, 6, 6, 7, 7, 8, 10])) == 7
    assert candidate(root = tree_node([4, 4, 5, 4, 4, 4, 6, 4, 4, None, None, 4, None, None, None, None, None, 4, None, None, None])) == 5
    assert candidate(root = tree_node([9, 9, 10, 9, 9, 11, 12, 9, 9, 9, 9, 9, 9, 9, 9])) == 10
    assert candidate(root = tree_node([4, 4, 5, 4, 4, 6, 7, 4, 4, 4, 4, 5, 5, 6, 8])) == 5
    assert candidate(root = tree_node([6, 6, 7, 6, 6, 6, 8, 6, 6, None, None, 6, None, None, None, None, None, 6, None, None, None])) == 7
    assert candidate(root = tree_node([7, 7, 8, 7, 7, 9, 10, 7, 7, None, None, 7, 11, 7, 12, 7, None, None, None, None, 7])) == 8
    assert candidate(root = tree_node([7, 7, 8, 7, 7, 8, 9, 7, None, 7, 7, None, None, 8, None])) == 8
    assert candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == -1
    assert candidate(root = tree_node([2, 2, 3, 2, 2, 4, 5, 2, 2, 2, 2, 6, 7, 2, 8])) == 3
    assert candidate(root = tree_node([4, 4, 7, 4, 4, 10, 14, 4, 4, 4, 4, 16, 20, 4, 24])) == 7
    assert candidate(root = tree_node([9, 9, 10, 9, 9, 11, 12, 9, 9, None, None, 9, 13, 9, 14, 9, 9, None, None, None, None, 9, 9, None, None, None, None, None, 9])) == 10
    assert candidate(root = tree_node([9, 9, 11, 9, 9, 12, 13, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) == 11
    assert candidate(root = tree_node([7, 7, 8, 7, 7, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7])) == 8
    assert candidate(root = tree_node([9, 9, 10, 9, 9, 11, 12, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) == 10
    assert candidate(root = tree_node([8, 8, 10, 8, 8, 11, 12, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == 10
    assert candidate(root = tree_node([2, 2, 3, 2, 2, 4, 5, 2, 2, 2, 2, 2, 2, 2, 6])) == 3
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == -1
    assert candidate(root = tree_node([5, 5, 6, 5, 5, 7, 8, 5, 5, 9, 10, 5, 5, 11, 12])) == 6
    assert candidate(root = tree_node([10, 10, 11, 10, 10, 12, 13, 10, 10, 10, 10, 10, 10, 10, 10])) == 11
    assert candidate(root = tree_node([12, 12, 14, 12, 12, 15, 16, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12])) == 14
    assert candidate(root = tree_node([12, 12, 13, 12, 12, 14, 15, 12, None, None, 12, 13, None, 13, None, 15, 12, None, 13])) == 13
    assert candidate(root = tree_node([6, 6, 7, 6, 6, 7, 8, 6, 6, 6, 6, 7, 7, 9, 10])) == 7
    assert candidate(root = tree_node([10, 10, 15, 10, 10, 20, 20, 10, 10, 10, 10, 25, 30, 10, 10])) == 15
    assert candidate(root = tree_node([11, 11, 12, 11, 11, 13, 14, 11, None, None, 11, 12, None, 12, None, 14, 11, None, 12])) == 12
    assert candidate(root = tree_node([7, 7, 8, 7, 7, 7, 9, 7, 7, None, None, 7, 7, 7, 10])) == 8
    assert candidate(root = tree_node([9, 9, 10, 9, 9, 9, 11, 9, 9, None, None, 9, None, None, None, None, None, 9, None, None, None])) == 10
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 2, 3])) == 2
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8])) == 8
    assert candidate(root = tree_node([9, 9, 10, 9, 9, 10, 11, 9, 9, 10, 10, 10, 11, 11, 12])) == 10
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 3, 3, 1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
    assert candidate(root = tree_node([8, 8, 9, 8, 8, 10, 11, 8, 8, 8, 8, 8, 8, 8, 8])) == 9
    assert candidate(root = tree_node([2, 2, 6, 2, 2, 6, 10, 2, 2, 6, 10, 14, 18, 2, 2, 6, 10, 14, 18, 22, None, None, None, None, None, None, None, None, None, None])) == 6
    assert candidate(root = tree_node([8, 8, 9, 8, 8, 10, 11, 8, 8, 8, 8, 12, 13, 8, 14])) == 9
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 1, 3])) == 2
    assert candidate(root = tree_node([1, 1, 3, 1, 1, 3, 4, 1, None, 1, None, None, None, None, None])) == 3
    assert candidate(root = tree_node([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 6, 7])) == 5
    assert candidate(root = tree_node([7, 7, 8, 7, 7, 8, 9, 7, 7, 8, 8, 8, 9, None, 9])) == 8
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 1, 3, 1, 1, None, None, 1, None, None, None, None, None, 1, None, None, None])) == 2
    assert candidate(root = tree_node([5, 5, 6, 5, 5, 5, 7, 5, None, 5, 5, None, None, 5, None])) == 6
    assert candidate(root = tree_node([2, 2, 3, 2, 2, 4, 4, 2, 2, 2, 2, 5, 5, 5, 5])) == 3
    assert candidate(root = tree_node([8, 8, 12, 8, 8, 12, 14, 8, 8, 12, 14, 16, 18, 8, None, None, 8, None, None, None, None, None, None])) == 12
    assert candidate(root = tree_node([7, 7, 11, 7, 7, 11, 13, 7, 7, 11, 13, 17, 19, 7, None, None, 7, None, None, None, None, None, None])) == 11
    assert candidate(root = tree_node([10, 10, 11, 10, 10, 12, 13, 10, None, None, 10, 11, None, 11, None, 13])) == 11
    assert candidate(root = tree_node([10, 10, 11, 10, 10, 12, 13, 10, 10, 10, 10, 11, 11, 12, 14])) == 11
    assert candidate(root = tree_node([5, 5, 6, 5, 5, 7, 8, 5, None, None, 9, 10, 11])) == 6
    assert candidate(root = tree_node([3, 3, 4, 3, 3, 5, 6, 3, 3, None, None, None, None, None, None, 5])) == 4
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6])) == 6
    assert candidate(root = tree_node([12, 12, 13, 12, 12, 14, 15, 12, 12, 12, 12, 16, 17, 12, 18])) == 13
    assert candidate(root = tree_node([10, 10, 20, 10, 10, 10, 30, 10, 10, 10, 10, 10, 10, 40, 50])) == 20
    assert candidate(root = tree_node([4, 4, 5, 4, 4, 5, 6, 4, 4, None, None, None, None, 5])) == 5
    assert candidate(root = tree_node([5, 5, 6, 5, 5, 6, 7, 5, None, None, 5, 6, None, 6, None])) == 6
    assert candidate(root = tree_node([6, 6, 7, 6, 6, 8, 9, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 10])) == 7
