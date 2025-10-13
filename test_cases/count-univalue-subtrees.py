# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 4
    assert candidate(root = tree_node([2, 2, 2, 5, 2])) == 3
    assert candidate(root = tree_node([1, 2, 3])) == 2
    assert candidate(root = tree_node([0])) == 1
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1])) == 4
    assert candidate(root = tree_node([5, 5, 5, 5, 5, None, 5])) == 6
    assert candidate(root = tree_node([2, None, 2, None, 2, None, 2])) == 4
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1])) == 7
    assert candidate(root = tree_node([1, 2, 2, None, 3, 3])) == 2
    assert candidate(root = tree_node([1, 2, 2, None, 3, None, 3])) == 2
    assert candidate(root = tree_node([])) == 0
    assert candidate(root = tree_node([5, 1, 5, 5, 5, None, 5])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 1
    assert candidate(root = tree_node([1, 2, 3, 1, 1, 3, 1, None, None, None, None, None, None, 1, 1])) == 6
    assert candidate(root = tree_node([1, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 27
    assert candidate(root = tree_node([15, 15, 15, 15, 16, 16, 15, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16, 15, 15, 16, 16])) == 42
    assert candidate(root = tree_node([5, 1, 5, 5, 5, None, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 28
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == 15
    assert candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, None, 4, None, 4, None, 4, None, 4])) == 11
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, 1, None, 1, None, None, 1, 1, 1, None, 1, None, 1, 1, 1])) == 16
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, None, 5, 5, 5, 5, 5, 5])) == 13
    assert candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, None, None, 2, None, 2, None, None, 2])) == 9
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1
    assert candidate(root = tree_node([5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1])) == 15
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 1
    assert candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == 31
    assert candidate(root = tree_node([6, 6, 6, 6, 6, None, None, 6, 6, 6, None, None, 6, 6, 6])) == 11
    assert candidate(root = tree_node([1, 1, 2, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 7
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 10
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, None, None, 4, 4, 4, 4, 4, 4])) == 7
    assert candidate(root = tree_node([9, 9, 9, 9, 9, None, None, None, None, None, None, 9, 9, 9, 9])) == 5
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4])) == 4
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 31
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, 1, None, 1, None, None, 1, 1, 1, None, 1, None, 1])) == 14
    assert candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) == 30
    assert candidate(root = tree_node([1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 10
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, 1, 1, 1, None, None, 1, 1, 1, 1])) == 14
    assert candidate(root = tree_node([7, 8, 7, 8, None, 7, None, 8, 8, None, 8, 8, 7])) == 4
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 69
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, 4, 5, 5])) == 4
    assert candidate(root = tree_node([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])) == 16
    assert candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) == 37
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 15
    assert candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1])) == 8
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 54
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 21
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, 1, None, 1, 1, 1, None, 1, 1, 1])) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 60
    assert candidate(root = tree_node([1, 2, 2, 2, 2, None, None, 1, 1, 2, 2, None, None, 2, 2])) == 7
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, None, None, None, None, 1, 1, 1, 1, 1, 1])) == 16
    assert candidate(root = tree_node([1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 10
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9])) == 16
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, None, 1, 1, 1, 1, None, None, 1, 1])) == 11
    assert candidate(root = tree_node([6, 6, 6, 6, 6, None, None, 6, None, 6, None, None, 6, 6, 6])) == 10
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 29
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 13
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 25
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 44
    assert candidate(root = tree_node([1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1])) == 8
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, None, 2, 2, 2, 2, None, None, 2, 2])) == 12
    assert candidate(root = tree_node([2, 2, 2, None, 2, 2, 2, None, 2, None, None, 2, None, 2, None])) == 9
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])) == 15
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 41
    assert candidate(root = tree_node([10, 5, 10, 5, 5, None, 10, None, 5, 5, None, None, 5, None, None, None, 5])) == 7
    assert candidate(root = tree_node([1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000])) == 5
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 10
    assert candidate(root = tree_node([5, 5, 5, 5, 5, None, 5, 5, 5, None, 5, None, None, 5, 5])) == 11
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 33
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 14
    assert candidate(root = tree_node([3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 4, None, 3])) == 9
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, None, None, 3, 3, None, None, None, None, None, 3])) == 10
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 15
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 32
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, None, None, None, 5, 5, 5, 5, 5, 5])) == 21
    assert candidate(root = tree_node([1, 2, 2, 5, 5, None, None, 5, 5, 5, 5, None, None, 5, 5])) == 9
    assert candidate(root = tree_node([14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14])) == 62
    assert candidate(root = tree_node([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, None, None, 11, 11, 11, 11, 11, None, 11])) == 18
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, 1, None, 1, 1, 1, None, None, 1, 1, 2, 2, 2, 2])) == 11
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, 5, None, 5, 5, 5, None, None, 5, 5])) == 16
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == 20
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, None, 5, 5, None, None, 5, 5])) == 11
    assert candidate(root = tree_node([100, 100, 100, 100, 100, 100, 100, None, 100, 100, None, None, None, 100])) == 10
    assert candidate(root = tree_node([1000, -1000, 1000, -1000, -1000, None, 1000])) == 5
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 55
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 113
    assert candidate(root = tree_node([5, 5, 5, 5, 5, None, None, 5, 5, None, None, 5, 5])) == 9
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 30
    assert candidate(root = tree_node([11, 12, 13, 11, None, 12, 13, None, 11, None, 12, None, 13, None, 11])) == 7
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 107
    assert candidate(root = tree_node([5, 1, 5, 5, 5, None, 5, 5, None, None, 5, None, 5, 5, None, None, 5, None, 5, 5])) == 11
    assert candidate(root = tree_node([1, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1])) == 15
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, 1, None, 1, None, None, 1, 1, 1, None, 1])) == 13
