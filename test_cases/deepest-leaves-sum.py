# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 92
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 15
    assert candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])) == 19
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, 6])) == 9
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, None, None, 2, None, None, 3, None, None, 4])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15])) == 29
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
    assert candidate(root = tree_node([2, 4, 6, 8, 10, 12, 14, None, None, None, None, None, None, 16, 18, None, None, None, None, None, None, 20, 22, 24, None, None, None, None, 26, 28, 30])) == 34
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, None, None, 31])) == 31
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, None, 10, 11, None, 12, 13, None, 14, 15, None, 16, 17, None, 18, 19, None, 20, 21])) == 78
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, None, None, None, None, None, None, None, 21])) == 111
    assert candidate(root = tree_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])) == 184
    assert candidate(root = tree_node([5, 4, 5, 4, 7, None, None, None, None, 7, 7])) == 14
    assert candidate(root = tree_node([5, 10, None, 15, 20, None, 25, 30, 35, None, None, 40, 45, None, None, None, None, None, None, 50, 55])) == 85
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, 16, None, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, 20, None, None, None, None, 21, None, None, None, None, 22, None, None, None, None, 23, None, None, None, None, 24, None, None, None, None, 25])) == 33
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, None, None, None, 31, 32, None, None, None, None, 35, 36, 37, 38])) == 209
    assert candidate(root = tree_node([1, 2, None, 4, None, None, None, 8, None, None, None, None, None, None, None, 16])) == 4
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10])) == 19
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, 3])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, None, None, None, 31, 32])) == 63
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, 8, None, None, None, None, None, None, None, 9, 10, None, None, None, None, 11])) == 15
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, 16, None, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, 20, None, None, None, None, 21, None, None, None, None, 22, None, None, None, None, 23, None, None, None, None, 24])) == 33
    assert candidate(root = tree_node([4, 2, 7, 1, 3, 6, 9, None, None, None, None, 5, 8, None, None, 13, 14])) == 27
    assert candidate(root = tree_node([5, 3, 8, 1, 4, None, 10, None, None, None, 9, 7, 11])) == 27
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 11, None, 12, None, 13, None, 14, None, 15])) == 15
    assert candidate(root = tree_node([31, 15, 47, 7, 23, 39, 55, 3, 11, 19, 27, 35, 43, 51, 59, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 63])) == 63
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 72
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14, None, None, 15, None, None, 16, None, None, 17, None, None, 18, None, None, 19, None, None, 20, None, None, 21, None, None, 22, None, None, 23, None, None, 24, None, None, 25])) == 15
    assert candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, None, 40, None, None, None, 45, None, None, 50, 55])) == 105
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 16
    assert candidate(root = tree_node([5, 3, 8, 1, 4, 7, 10, None, None, None, 6, None, 9, None, None, 11, 12])) == 23
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 234
    assert candidate(root = tree_node([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])) == 500
    assert candidate(root = tree_node([9, 18, 27, 36, 45, 54, 63, 72, 81, 90, None, 99, None, None, None, None, None, None, None, None, None, None, 108, 117, 126, 135, 144, 153, 162, 171, 180])) == 351
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 10
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, None, None, None, None, 12, None, None, None, 13])) == 21
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13, None, None, 14, 15, None, None, 16, 17])) == 33
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 345
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37])) == 37
    assert candidate(root = tree_node([1, 2, 3, None, 5, 6, None, 7, None, None, 8, None, None, 9, None, None, 10])) == 10
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 6])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 90
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 20
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, 29, 30])) == 59
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 140
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, 16, None, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, 20, None, None, None, None, 21, None, None, None, None, 22, None, None, None, None, 23])) == 33
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 25, 30, 40, 50, 60, 70, 80, 90])) == 300
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 205
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 779
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == 9
    assert candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, None, None, None, 5, None, None, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9])) == 4
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, None, None, None, None, 2, None, None, 16])) == 2
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 1, 2, None, None, 3, 4])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, None, None, None, 31, 32, None, None, 33, 34])) == 130
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, 9, 10, 11, 12, None, None, None, None, None, 13, 14, 15])) == 29
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, 7, 8, 9, None, None, None, None, None, None, 10, 11, 12, 13])) == 25
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 7
    assert candidate(root = tree_node([20, 15, 25, 10, 18, 23, 30, 5, 12, 16, 19, 22, 24, 29, 32, 3, 7, 11, 13, 14, 17, 21, 26, 28, 31, 33])) == 204
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, 16, None, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, 20, None, None, None, None, 21, None, None, None, None, 22, None, None, None, None, 23, None, None, None, None, 24, None, None, None, None, 25, None, None, None, None, 26])) == 33
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, None, None, None, None, None, None, None, None, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, None, None, None, None, 31, 32, 33, 34, 35])) == 165
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15
    assert candidate(root = tree_node([1, 2, 3, 4, None, 6, None, 7, None, None, None, 8, None, 9, None, None, None, None, 10, None])) == 9
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21])) == 60
    assert candidate(root = tree_node([9, 4, 5, None, None, 6, 7, None, None, None, None, None, 8])) == 13
    assert candidate(root = tree_node([9, 3, 15, 2, 7, 12, 20, 1, None, 5, 8, 11, None, None, 13, None, None, 6, 4, 9, None, 10])) == 29
    assert candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 8, None, 14, 19, None, 21, 24, 32])) == 118
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, None, None, None, None, None, None, None, None, None, None, None, 0])) == 6
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 20
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 17
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, 16, 20])) == 51
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, None, None, None, 14])) == 21
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 6, None, 7, 8, 9, None, None, None, None, None, None, 10, 11])) == 24
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, None, None, 36])) == 341
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 12
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 8, None, None, 14, None, 17, 19])) == 50
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 12
    assert candidate(root = tree_node([7, 14, 21, 28, 35, None, 42, 49, 56, 63, None, 70, 77, None, None, None, None, None, None, None, None, 84, 91, 98])) == 98
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11])) == 21
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 306
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, 16, None, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, 20, None, None, None, None, 21])) == 17
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11
    assert candidate(root = tree_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 31
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 205
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 115
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8, None, None, None, None, None, 9, None, None, None, None, 10, None, None, None, None, 11, None, None, None, None, 12])) == 15
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])) == 305
    assert candidate(root = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, None, None, None, None, None, None, None, None, None, None, None, None, None, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150])) == 295
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, 16, None, None, None, None, 17, None, None, None, None, 18, None, None, None, None, 19, None, None, None, None, 20])) == 33
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, None, None, None, None, None, None, 6, None, None, None, None, None, None, None, None, 7])) == 5
    assert candidate(root = tree_node([1, 3, None, None, 2])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, None, 7, 8, None, 9, 10, None, 11, 12, None, 13, 14, None, 15, 16, None, 17, 18, None, 19, 20, None, 21, 22, None, 23, 24, None, 25, 26, None, 27, 28, None, 29, 30])) == 212
    assert candidate(root = tree_node([3, 6, 9, 12, 15, None, 18, None, None, None, None, 21, 24, None, None, None, None, None, None, None, 27, None, None, None, None, 30])) == 45
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 15
