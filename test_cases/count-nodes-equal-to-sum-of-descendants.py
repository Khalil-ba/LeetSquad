# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 0
    assert candidate(root = tree_node([10, 3, 4, 2, 1])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5])) == 0
    assert candidate(root = tree_node([1, 0, 0, 0, 0, 0, 0])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 0
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == 0
    assert candidate(root = tree_node([5, 10, 10, None, None, 2, 3])) == 0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1])) == 0
    assert candidate(root = tree_node([2, 3, None, 2, None])) == 0
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4])) == 0
    assert candidate(root = tree_node([0])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == 0
    assert candidate(root = tree_node([20, 10, 10, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, 9, 10, None, None, None, 11])) == 0
    assert candidate(root = tree_node([30, 15, 15, 7, 8, 7, 8, 3, 4, 3, 4, 3, 4, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 0
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 13, 12, 12, 13, 13, 12])) == 4
    assert candidate(root = tree_node([1, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9, 10, 11, None, None, 12, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 14])) == 0
    assert candidate(root = tree_node([8, 4, 4, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 20
    assert candidate(root = tree_node([5, 3, 2, 2, 1, 0, 0])) == 3
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 0
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == 0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 31
    assert candidate(root = tree_node([7, 3, 3, 2, 2, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 11
    assert candidate(root = tree_node([30, 15, 15, 7, 8, 7, 8, 3, 4, 3, 5, 3, 4, 3, 5])) == 4
    assert candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, None, 2, 4, 6, 9, 11])) == 0
    assert candidate(root = tree_node([5, 2, 13, 1, 6, 10, 14, None, None, 4, 7, 9, 15])) == 0
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 10, 10, 10, 10, 5, 5, 5, 5])) == 0
    assert candidate(root = tree_node([20, 10, 10, 5, 5, 5, 5, 2, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
    assert candidate(root = tree_node([21, 10, 11, 5, 5, 5, 6, 2, 3, 3, 2])) == 3
    assert candidate(root = tree_node([10, 5, 5, None, None, 5, 5, None, None, 5, 5, None, None, 5, 5])) == 0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19])) == 0
    assert candidate(root = tree_node([25, 12, 13, 6, 6, 6, 7, 3, 3, 3, 3, 3, 3, 4, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 0
    assert candidate(root = tree_node([10, 5, 5, 2, 3, 0, 5, 1, 1])) == 3
    assert candidate(root = tree_node([10, 5, 5, 3, 2, 1, 1])) == 1
    assert candidate(root = tree_node([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 28
    assert candidate(root = tree_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 14
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 12, 13, 12, 13, 12, 13, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7])) == 4
    assert candidate(root = tree_node([20, 15, 5, 10, 5, 3, 2])) == 2
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, 3, 4, None, None, 4])) == 0
    assert candidate(root = tree_node([15, 10, 5, 3, 7, 1, 4])) == 2
    assert candidate(root = tree_node([15, 7, 8, 3, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1])) == 0
    assert candidate(root = tree_node([100, 50, 50, 25, 25, None, None, 12, 13, 14, 13, None, None, None, None, 7, 7, 7, 8, 8, 8, 8])) == 1
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 30
    assert candidate(root = tree_node([10, 5, 5, 3, 2, 1, 4, 1, 1, None, 1, None, None, None, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 50
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, None, 10, 11])) == 0
    assert candidate(root = tree_node([7, 3, 4, 1, 2, None, None, None, None, 1, 1, 1, 1])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 0
    assert candidate(root = tree_node([10, 5, 5, 3, 2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
    assert candidate(root = tree_node([10, 5, 5, 3, 2, 1, 4, 1, 1, None, 1, None, None, None, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 55
    assert candidate(root = tree_node([1000, 500, 500, 250, 250, 250, 250, 125, 125, 125, 125, 125, 125, 125, 125])) == 4
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([2, 1, 1, None, None, 1, 1, None, None, 1, 1, None, None, 1, 1])) == 0
    assert candidate(root = tree_node([10, 5, 5, 3, 2, 1, 4, 1, 1, None, 1, None, None, None, 1])) == 0
    assert candidate(root = tree_node([10, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 0
    assert candidate(root = tree_node([1, 2, None, 4, None, 8, None, 16, None, 32])) == 0
    assert candidate(root = tree_node([10, 5, 5, 3, 2, 1, 4])) == 2
    assert candidate(root = tree_node([15, 5, 10, 2, 3, 7, 3, 1, 1, 1, 1, 3, 2, None, None, None, None, None, None, None, 1])) == 3
    assert candidate(root = tree_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 14
    assert candidate(root = tree_node([20, 10, 10, 5, 5, 5, 5, 2, 3, 2, 3, 1, 1, 1, 1])) == 2
    assert candidate(root = tree_node([20, 10, 10, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1])) == 0
    assert candidate(root = tree_node([20, 10, 10, 5, 5, 5, 5, 2, 3, 2, 3, 2, 3, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 4
    assert candidate(root = tree_node([50, 20, 30, 10, 10, 10, 20, 5, 5, 5, 5, 5, 10, 10, 10])) == 3
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == 1
    assert candidate(root = tree_node([42, 21, 21, 10, 11, 10, 11, 5, 5, 6, 5, 5, 6, 5, 5])) == 2
    assert candidate(root = tree_node([7, 3, 4, 1, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 0
    assert candidate(root = tree_node([7, 3, 4, 2, 1, None, 4, 1, 1, None, None, 2, None])) == 1
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, 0, 0, 0, 0])) == 4
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 10, 10, 10, 10, 10, 10, 10, 10])) == 0
    assert candidate(root = tree_node([15, 10, 5, 5, 5, 0, 0, 3, 2, 2, 0])) == 4
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 0
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0])) == 8
    assert candidate(root = tree_node([5, 3, 1, 2, 1, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 4
    assert candidate(root = tree_node([20, 10, 10, 5, 5, 5, 5, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3])) == 1
    assert candidate(root = tree_node([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([15, 7, 8, 3, 4, 3, 5, 1, 2, 1, 3, 1, 2, 1, 2])) == 3
    assert candidate(root = tree_node([15, 10, 5, 3, 7, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([15, 5, 10, 3, 2, 6, 4, 1, 1, 1, 1, 3, 3, None, None, None, None, None, None])) == 2
    assert candidate(root = tree_node([20, 10, 10, 5, 5, 5, 5, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 1
    assert candidate(root = tree_node([35, 10, 25, 5, 5, 15, 10, 2, 3, 3, 5, 5, 5, 5, 5])) == 2
    assert candidate(root = tree_node([5, 3, 2, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
    assert candidate(root = tree_node([10, 5, 5, 2, 3, 0, 0, 1, 1, 1, 1])) == 3
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([10, 3, 4, 2, 1, None, 3, 2, None, None, 1, 1, None])) == 3
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == 0
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 12, 13, 12, 13, 12, 13, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 1
    assert candidate(root = tree_node([1, 2, 3, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])) == 0
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7])) == 0
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 12, 13, 12, 13, 12, 13])) == 4
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 10, 10, 10, 10, 10, 10, 10, 10])) == 0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 15
    assert candidate(root = tree_node([30, 10, 20, 5, 5, 10, 10, 2, 3, 2, 3, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1
    assert candidate(root = tree_node([9, 4, 5, 2, 2, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 0
