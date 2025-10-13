# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, 6])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, 8])) == 3
    assert candidate(root = tree_node([1, 2])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5])) == 2
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18])) == 17
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, None, 7, 8, None, 9, None, 10, 11, None, 12, 13])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, 6, None, None, 7, 8])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, 7, None, None, None, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, 6, None, None, None, None, 7, 8, None, None, 9, 10, 11, None, None, 12, 13])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19])) == 18
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, None, None, 8])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, None, 5, 6, None, None, None, None, 7, 8])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5])) == 3
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, 10, 11, 12, 13])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9, 10, 11])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, None, 7, 8, 9, 10, None, None, 11, 12])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13, None, None, 14, 15, None, None, 16, 17, None, None, 18, 19, None, None, 20, 21])) == 10
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, None, None, None, None, 7, 8, 9, 10])) == 6
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, 7, 8, None, None, 9, 10])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, 6, None, None, None, None, 7, 8, None, None, 9, 10, None, 11, 12])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, 7, None, 8, None, 9, None, None, 10, 11, None, None, 12, None, 13])) == 10
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, None, None, None, None, None, None, None, None, 4, 5, 6])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, 7, None, 8, 9, 10, None, None, None, None, 11, 12])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40])) == 38
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, None, None, 4, 5, 6, 7, 8, 9, 10, 11])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17])) == 15
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8, 9, 10])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, None, None, 6, 7])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18, None, None, 19, 20])) == 10
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 12
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, None, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, 7, None, None, None, None, 8, 9, 10, 11])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, 7, None, 8, None, 9, None, None, 10, None, 11, None, 12, None, 13])) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9, 10, None, None, None, None, 11, None, 12, None, 13, None, 14, None, 15])) == 6
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, None, None, 8, 9])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, 10, None, None, None, None, None, None, 11, 12, 13, 14, 15])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, 7, 8, None, 9, 10])) == 5
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, None, None, 10])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 13
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, 6, 7, None, None, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, 8])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, None, None, 7, 8, None, 9, 10, None, None, 11, 12])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, None, 5, 6, 7, None, None, 8, None, 9, None])) == 7
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, 6, None, 7, 8, None, 9, 10, None, 11, 12, None, 13, 14, None, 15, 16])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, 6, 7, None, None, None, 8, 9])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, 7, None, 8, None, 9, None, None, 10, 11, 12, None, None, 13, 14])) == 9
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 9
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, 7, None, None, 8, 9])) == 6
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, None, None, None, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, 9, 10, None, None, None, 11, 12, 13])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, None, None, 7, None, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, 9, None, None, 10, None, 11, None, None, 12, None, 13, None, None, 14, None, 15, None, None, 16, None, 17, None, 18, None, 19, None, 20])) == 7
    assert candidate(root = tree_node([1, 2, None, None, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13])) == 6
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 19
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 5
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 11
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, None, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, None, 7, 8, 9, None, None, 10, 11])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9, None, None, 10, None, None, 11])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, 9, 10, 11, 12, None, 13, 14, 15])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, 6, None, 7, None, None, 8, 9])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None, 10, 11])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 9
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, 6, None, None, None, None, 7, 8, None, None, 9, 10])) == 3
    assert candidate(root = tree_node([1, 2, None, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, 9, 10, None, None, None, None, 11, 12])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, 7, None, 8, 9, None, None, 10, None, 11, 12])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, 8, None, None, None, 9, 10, 11, None, None, None, 12])) == 5
