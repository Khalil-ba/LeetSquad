# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),nums = [2, 4, 6, 8, 10]) == 5
    assert candidate(head = list_node([4, 3, 0, 1, 2]),nums = [0, 1, 2]) == 1
    assert candidate(head = list_node([5, 6, 7, 8, 9]),nums = [6, 7]) == 1
    assert candidate(head = list_node([4, 3, 2, 1]),nums = [1, 2]) == 1
    assert candidate(head = list_node([5, 6, 7, 8, 9]),nums = [5, 9]) == 2
    assert candidate(head = list_node([10, 20, 30, 40]),nums = [10, 40]) == 2
    assert candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 1
    assert candidate(head = list_node([0]),nums = [0]) == 1
    assert candidate(head = list_node([1, 2, 3, 4, 5]),nums = [2, 3, 5]) == 2
    assert candidate(head = list_node([0, 1, 2, 3, 4]),nums = [0, 3, 1, 4]) == 2
    assert candidate(head = list_node([0, 2, 1, 3]),nums = [0, 1]) == 2
    assert candidate(head = list_node([7, 10, 1, 12, 3, 9, 6, 11, 4, 8, 2, 5]),nums = [10, 3, 5, 7, 4, 1]) == 4
    assert candidate(head = list_node([5, 6, 7, 8]),nums = [6, 7]) == 1
    assert candidate(head = list_node([0, 1, 2, 3]),nums = [0, 1, 3]) == 2
    assert candidate(head = list_node([1, 0, 2, 3, 4, 5]),nums = [0, 1, 3, 5]) == 3
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]),nums = [1, 2, 3, 4, 5]) == 1
    assert candidate(head = list_node([4, 7, 1, 13, 8, 9, 2]),nums = [1, 13, 9, 8, 2]) == 1
    assert candidate(head = list_node([7, 10, 1, 12, 3, 9, 5, 8, 4, 6, 2, 11]),nums = [1, 3, 5, 7, 9, 11]) == 4
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),nums = [6, 7, 8, 9, 10]) == 1
    assert candidate(head = list_node([3, 5, 7, 9, 11, 13, 15, 17, 19, 21]),nums = [5, 9, 13, 17, 21]) == 5
    assert candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 0, 11, 12, 13, 14, 15]),nums = [2, 4, 6, 8, 10, 1, 11, 13, 15]) == 8
    assert candidate(head = list_node([1, 2, 0, 3, 4, 5, 6, 7, 8, 9]),nums = [1, 2, 4, 7, 8]) == 3
    assert candidate(head = list_node([5, 4, 3, 2, 1]),nums = [3, 2, 1]) == 1
    assert candidate(head = list_node([1, 4, 3, 2, 5, 6, 7, 8, 9, 0]),nums = [2, 3, 1, 4]) == 1
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),nums = [0, 2, 4, 6, 8, 10]) == 6
    assert candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12]),nums = [6, 7, 9, 10, 12]) == 3
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),nums = [1, 2, 5, 6, 9, 10]) == 3
    assert candidate(head = list_node([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),nums = [10, 12, 14, 16, 18]) == 5
    assert candidate(head = list_node([0, 1, 3, 2, 5, 6, 7, 4, 8, 9]),nums = [3, 2, 4, 8, 9]) == 2
    assert candidate(head = list_node([1, 4, 3, 2, 5]),nums = [1, 3, 5]) == 3
    assert candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]),nums = [80, 82, 84, 86, 88, 90, 92, 94, 96, 98]) == 10
    assert candidate(head = list_node([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]),nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 1
    assert candidate(head = list_node([5, 1, 2, 3, 4, 6, 7, 8, 9]),nums = [1, 2, 6, 7, 9]) == 3
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15]),nums = [1, 5, 9, 15]) == 4
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]),nums = [10, 30, 50, 70, 90, 110, 130, 150]) == 8
    assert candidate(head = list_node([1, 4, 2, 5, 3, 6, 7, 8, 9]),nums = [1, 3, 5, 7]) == 3
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]),nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41]) == 11
    assert candidate(head = list_node([0, 2, 4, 6, 8, 10, 12, 14, 16]),nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 0
    assert candidate(head = list_node([23, 45, 67, 89, 101, 123, 145, 167, 189, 211]),nums = [23, 45, 67, 89, 101, 123, 145, 167, 189, 211]) == 1
    assert candidate(head = list_node([0, 2, 1, 4, 3, 5]),nums = [3, 4, 5]) == 1
    assert candidate(head = list_node([3, 2, 1, 0, 5, 4, 7, 8, 6, 9]),nums = [3, 2, 1, 0, 5, 4, 7, 8, 6, 9]) == 1
    assert candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 1
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 25
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),nums = [1, 4, 7, 10, 13, 16, 19]) == 7
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),nums = [1, 2, 5, 6, 9]) == 3
    assert candidate(head = list_node([5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 11, 10, 15, 14, 13, 12]),nums = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 11, 10, 15, 14, 13, 12]) == 1
    assert candidate(head = list_node([100, 200, 300, 400, 500, 600, 700]),nums = [100, 300, 500, 700]) == 4
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),nums = [1, 3, 5, 7, 9]) == 5
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60]),nums = [10, 30, 50]) == 3
    assert candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]),nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]) == 1
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20]) == 7
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]) == 5
    assert candidate(head = list_node([0, 2, 1, 4, 3, 5, 6, 7]),nums = [0, 2, 4, 6]) == 3
    assert candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),nums = [2, 6, 10, 14, 18]) == 5
    assert candidate(head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),nums = [2, 3, 11, 13, 17, 23, 29]) == 3
    assert candidate(head = list_node([5, 3, 9, 6, 1, 12, 7, 2, 4, 8, 11, 10]),nums = [3, 6, 7, 8, 10]) == 5
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]),nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49]) == 13
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),nums = [10, 8, 6, 4, 2]) == 5
    assert candidate(head = list_node([1, 5, 6, 3, 2, 7, 4, 0, 9]),nums = [1, 3, 0, 9]) == 3
    assert candidate(head = list_node([1, 4, 6, 8, 9, 10, 11, 12, 13, 15, 17, 19]),nums = [4, 6, 8, 9, 11, 12, 15, 17]) == 3
    assert candidate(head = list_node([3, 0, 2, 8, 1, 5, 7, 4, 6]),nums = [2, 8, 0, 6, 4]) == 2
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 1
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),nums = [30, 40, 60, 80, 100]) == 4
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),nums = [1, 2, 4, 6, 8, 10]) == 5
    assert candidate(head = list_node([29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]),nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11]) == 10
    assert candidate(head = list_node([100, 90, 80, 70, 60, 50, 40, 30, 20, 10]),nums = [100, 90, 80, 60, 50, 30, 10]) == 4
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90]),nums = [10, 20, 40, 60, 80]) == 4
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]),nums = [1, 5, 9, 13, 17, 21, 25, 29]) == 8
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 8
    assert candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30]),nums = [30, 32, 34, 36, 38, 40, 42, 44, 46, 48]) == 10
    assert candidate(head = list_node([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]),nums = [0, 4, 8, 12, 16]) == 5
    assert candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),nums = [0, 2, 4, 6, 8, 10, 12, 14]) == 8
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]),nums = [1, 7, 13, 19, 25, 29]) == 6
    assert candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 16
    assert candidate(head = list_node([1, 5, 4, 3, 2, 6, 7, 8, 9, 10]),nums = [1, 3, 5, 7, 9]) == 4
    assert candidate(head = list_node([5, 4, 3, 2, 1, 0, 11, 12, 13, 14]),nums = [5, 4, 3, 11, 12]) == 2
    assert candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]),nums = [100, 300, 500, 700, 900]) == 5
    assert candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),nums = [15, 13, 11, 9, 7, 5, 3, 1]) == 8
    assert candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]),nums = [5, 4, 3, -1, -2, -4, -5]) == 3
    assert candidate(head = list_node([9, 7, 5, 3, 1, 2, 4, 6, 8, 0]),nums = [9, 7, 5, 3, 1, 8, 0]) == 2
    assert candidate(head = list_node([2, 6, 5, 4, 3, 0, 7, 1, 8, 9]),nums = [2, 4, 7, 8, 9]) == 4
    assert candidate(head = list_node([5, 6, 2, 3, 4, 1, 7, 8]),nums = [2, 3, 4, 7, 8]) == 2
    assert candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),nums = [3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
    assert candidate(head = list_node([5, 4, 3, 2, 1, 0]),nums = [0, 1, 2, 3, 4, 5]) == 1
    assert candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45]),nums = [5, 20, 35, 50]) == 3
    assert candidate(head = list_node([3, 5, 7, 9, 11, 13, 15, 17, 19]),nums = [3, 7, 11, 15, 19]) == 5
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),nums = [10, 20, 30, 50, 60, 80, 100]) == 4
    assert candidate(head = list_node([1, 4, 2, 3, 5, 7, 6, 8, 9]),nums = [1, 2, 3, 6, 8, 9]) == 3
    assert candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),nums = [0, 2, 4, 6, 8, 10, 12, 14]) == 8
    assert candidate(head = list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91]),nums = [11, 31, 51, 71, 91]) == 5
    assert candidate(head = list_node([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]),nums = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 1
    assert candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == 10
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]),nums = [1, 3, 5, 7, 9]) == 5
    assert candidate(head = list_node([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]),nums = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]) == 11
    assert candidate(head = list_node([4, 2, 8, 6, 9, 7, 3, 0, 5, 1]),nums = [3, 0, 5, 1, 6, 7, 9]) == 1
    assert candidate(head = list_node([0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13]),nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13]) == 1
    assert candidate(head = list_node([9, 7, 5, 3, 1, 2, 4, 6, 8]),nums = [9, 7, 5, 3, 1, 4, 6, 8]) == 2
    assert candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),nums = [0, 2, 4, 6, 8]) == 5
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]) == 24
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),nums = [1, 5, 9, 13, 17]) == 5
    assert candidate(head = list_node([5, 1, 3, 7, 9, 11, 13, 15, 17, 19]),nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
    assert candidate(head = list_node([1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]),nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 1
    assert candidate(head = list_node([4, 5, 6, 7, 8, 9, 0, 1, 2, 3]),nums = [7, 8, 9, 0, 1]) == 1
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90]),nums = [10, 30, 50, 70, 90]) == 5
    assert candidate(head = list_node([7, 3, 6, 4, 5, 1, 2, 0, 8, 9]),nums = [3, 6, 5, 1, 2, 8, 9]) == 3
