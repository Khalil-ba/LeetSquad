# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(m = 2,n = 2,horizontalCut = [7],verticalCut = [4]) == 15
    assert candidate(m = 4,n = 3,horizontalCut = [1, 2, 3],verticalCut = [1, 2]) == 17
    assert candidate(m = 3,n = 3,horizontalCut = [1, 2],verticalCut = [1, 2]) == 11
    assert candidate(m = 5,n = 4,horizontalCut = [1, 2, 3, 4],verticalCut = [1, 2, 3]) == 36
    assert candidate(m = 6,n = 3,horizontalCut = [1, 2, 3, 4, 5],verticalCut = [1, 2]) == 32
    assert candidate(m = 4,n = 3,horizontalCut = [2, 4, 6],verticalCut = [1, 3, 5]) == 39
    assert candidate(m = 3,n = 2,horizontalCut = [1, 3],verticalCut = [5]) == 13
    assert candidate(m = 15,n = 10,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 660
    assert candidate(m = 8,n = 12,horizontalCut = [1, 2, 3, 4, 5, 6, 7],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 346
    assert candidate(m = 8,n = 12,horizontalCut = [1, 2, 3, 4, 5, 6, 7],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 346
    assert candidate(m = 15,n = 15,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1225
    assert candidate(m = 10,n = 10,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 696
    assert candidate(m = 8,n = 7,horizontalCut = [1, 3, 5, 7, 9, 11, 13],verticalCut = [2, 4, 6, 8, 10, 12]) == 294
    assert candidate(m = 7,n = 8,horizontalCut = [10, 20, 30, 40, 50, 60],verticalCut = [5, 10, 15, 20, 25, 30, 35]) == 1080
    assert candidate(m = 9,n = 11,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 367
    assert candidate(m = 12,n = 8,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],verticalCut = [1, 2, 3, 4, 5, 6, 7]) == 346
    assert candidate(m = 10,n = 10,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 375
    assert candidate(m = 9,n = 9,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40]) == 1380
    assert candidate(m = 8,n = 6,horizontalCut = [1, 2, 3, 4, 5, 6, 7],verticalCut = [1, 2, 3, 4, 5]) == 128
    assert candidate(m = 12,n = 11,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 561
    assert candidate(m = 100,n = 100,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]) == 338250
    assert candidate(m = 99,n = 100,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]) == 333201
    assert candidate(m = 8,n = 8,horizontalCut = [1, 2, 3, 4, 5, 6, 7],verticalCut = [1, 2, 3, 4, 5, 6, 7]) == 196
    assert candidate(m = 10,n = 10,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 3750
    assert candidate(m = 10,n = 10,horizontalCut = [1, 9, 2, 8, 3, 7, 4, 6, 5],verticalCut = [1, 9, 2, 8, 3, 7, 4, 6, 5]) == 375
    assert candidate(m = 10,n = 10,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 375
    assert candidate(m = 15,n = 10,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 660
