# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5])) == 4
    assert candidate(root = tree_node([3, 9, 20, 15, 7])) == 15
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 0
    assert candidate(root = tree_node([-9, -3, 2, None, 4, 4, 0, -6, None, -5])) == -11
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 7
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1])) == 1
    assert candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, None, 4])) == 15
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 40
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == 21
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, None, None, 7])) == 6
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 24
    assert candidate(root = tree_node([1])) == 0
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, None, 4])) == 0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9])) == 7
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190])) == 340
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 6, 8, 13, 17, 22])) == 26
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6])) == 6
    assert candidate(root = tree_node([5, 2, -3, None, -4, None, 1, None, None, -5, None, -6, None, -7, None, -8])) == -8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == 288
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, 5, None, 35, None, 45, 65, 85, 95, 105, 135, 145, 155, 165, 185, 195])) == 780
    assert candidate(root = tree_node([33, 18, 50, 8, None, 32, 60, 2, 11, None, 46, None, None, 29, None, None, 59, None, None])) == 29
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, 8, 9])) == 18
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, None, 17])) == 12
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10])) == 15
    assert candidate(root = tree_node([5, 15, 1, None, 6, None, 7, 8, 9, None, None, None, None, 10, 11])) == 18
    assert candidate(root = tree_node([5, 15, 7, None, 9, None, 11, None, None, 13, 14])) == 13
    assert candidate(root = tree_node([2, 1, 3, 4, None, 5, 6, None, 7, 8, None, 9, 10, 11, None, 12, 13, 14, None, 15])) == 52
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, None, None, 4, 8, 11, 13, 18, 25])) == 36
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, 8])) == 10
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, 18, 16, 19, 14, 17])) == 39
    assert candidate(root = tree_node([10, 9, 20, 8, None, 15, 25, 7, None, None, 18, 23, 30, 17, None, None, None, 24])) == 41
    assert candidate(root = tree_node([10, 5, 20, None, None, 15, 25, None, None, None, 30])) == 20
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, None, None, None, None, 7, 8, 9])) == 10
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, None, None, None, None, None, 10])) == 8
    assert candidate(root = tree_node([3, 9, 20, 4, 5, 6, 7, None, None, None, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14, None, None, 15])) == 19
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, None, None, None, 2])) == 11
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 20
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30])) == 0
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180, 5, None, None, 20, None, 40, 70, None, None, 90, 100, 120, 130, 150, None, None, 170, 190, 200])) == 670
    assert candidate(root = tree_node([1, 2, 3, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 36
    assert candidate(root = tree_node([5, 3, 8, 2, 4, None, 9, 1, None, 6, 7, None, 10])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 80
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 44
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 43, 56, 70, 81, 93])) == 174
    assert candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, None, 28, 40, 55, 65, 85, 100, None, None, None, 26, 32])) == 177
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == 7
    assert candidate(root = tree_node([1, 2, 2, 3, None, 3, None, 4, 4, None, None, 5, 5])) == 8
    assert candidate(root = tree_node([10, 5, 15, None, 7, 12, 20, None, None, 6, 8, 13, 18])) == 19
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, 6, 7, None, 8, None, 9, 10, None, 11, 12])) == 12
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 494
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, 6, None, None, 10])) == 6
    assert candidate(root = tree_node([10, None, 20, 30, 40, 50, 60, None, None, 70, 80])) == 70
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 25, 26])) == 49
    assert candidate(root = tree_node([20, 15, 25, 10, 18, None, 30, 5, 12, None, 17, 22, 35, None, None, None, None, None, 16])) == 27
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 0
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 16, 17, 18, 19, None, None, None, None, 20])) == 45
    assert candidate(root = tree_node([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 44
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 9, 0, 2, 6, None, None, 15, None, None, None, None, 16])) == 22
    assert candidate(root = tree_node([20, 10, 30, None, 15, 25, 35, None, 17, 23, None, None, None, 27, 32, 37])) == 64
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, 7, 8, None, 9])) == 5
    assert candidate(root = tree_node([20, 15, 25, 10, 18, None, 30, 5, 12, 16, 19, 27, 35, 3, None, 14, 21, 26, 28, 32, 34, 36, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 111
    assert candidate(root = tree_node([5, None, 10, None, 15, None, 20, None, 25, None, 30, None, 35])) == 0
    assert candidate(root = tree_node([100, 50, 200, 25, 75, None, 300, None, 35, None, 85, 150, None, None, 400])) == 150
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 65, 85, 115, 135, 165, 185])) == 355
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 8
    assert candidate(root = tree_node([8, 4, 12, None, 6, 10, 14, 5, None, 7, None, 9, None, 11, None, 13, None, 15])) == 39
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8])) == 7
    assert candidate(root = tree_node([3, 1, 4, None, 2])) == 0
    assert candidate(root = tree_node([12, 6, 18, 3, 9, 15, 21, 1, 5, None, None, 11, None, None, 19, 22])) == 33
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])) == 200
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 0
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, 8])) == 1
    assert candidate(root = tree_node([8, 6, 10, 5, 7, 9, 11, 4, None, None, None, None, None, 3])) == 16
    assert candidate(root = tree_node([10, None, 20, None, 30, None, 40, None, 50, None, 60, None, 70, None, 80, None, 90, None, 100])) == 0
    assert candidate(root = tree_node([7, 3, 15, None, 8, 10, None, 5, 9, 11, 13, None, None, None, 12])) == 16
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7, None, None, None, None, None, 8])) == 6
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 0
    assert candidate(root = tree_node([10, 5, 15, None, None, None, 25])) == 5
    assert candidate(root = tree_node([0, -1, 2, -2, None, -3, None, -4])) == -7
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, None, 8, 12, 22, 28, None, 32, None, None, 4, 7, None, 9, 11, 13, 14, 16, 17, 18, 19, 21, 23, 24, 26, 27, 29, 31, 33, 34])) == 162
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180])) == 340
    assert candidate(root = tree_node([5, 15, 20, 30, 5, None, 25, 45, None, None, 35, 40, 50])) == 85
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, None, 8, 12, None, None, None, None, None, None, 9, None, 11])) == 46
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, 28, None, 32, None, None, 35, 36])) == 114
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, None, 11, 12, None, 13, None, None, 14])) == 35
    assert candidate(root = tree_node([10, 8, 15, 3, 5, None, 20, 1, 4, 6, None, None, None, 17])) == 23
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30])) == 30
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, 9, None, None, 10, 11])) == 18
    assert candidate(root = tree_node([23, 18, 15, 20, 25, 16, 10, None, 22, None, None, 19, None, None, 8])) == 19
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 25
