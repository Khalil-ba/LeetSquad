# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [-5, 1, 1, 4, 2]) == True
    assert candidate(nums = [-1, 2, -1, 2, -1]) == False
    assert candidate(nums = [-1, -2, -3, -4, -5, 6]) == False
    assert candidate(nums = [-2, -3, -4, -5, -6]) == False
    assert candidate(nums = [1, 2, -1, -2, 3]) == False
    assert candidate(nums = [5, 1, 1, 2, 2]) == False
    assert candidate(nums = [1]) == False
    assert candidate(nums = [5, -1, 1, 4, 2]) == True
    assert candidate(nums = [-1, -1, -1, -1, -1]) == True
    assert candidate(nums = [-1, 2]) == False
    assert candidate(nums = [-1, 2, -1, -2, -1]) == False
    assert candidate(nums = [-1, -2, -3, -4, -5]) == False
    assert candidate(nums = [-5, -4, -3, -2, -1]) == True
    assert candidate(nums = [-1, 1, -1, 1, -1]) == False
    assert candidate(nums = [2, -1, 1, 2, 2]) == True
    assert candidate(nums = [1, 2, 3, 4, 5]) == True
    assert candidate(nums = [3, 1, 2, 4, 3]) == True
    assert candidate(nums = [1, -1, 5, 1, 4]) == True
    assert candidate(nums = [-2, 1, -1, -2, -2]) == False
    assert candidate(nums = [-2, -2, -2, -2, -2]) == True
    assert candidate(nums = [3, 1, 2]) == True
    assert candidate(nums = [5, 2, 3, 4, -1]) == False
    assert candidate(nums = [2, 2, 2, 2, 2]) == True
    assert candidate(nums = [1, 2, -3, -4, 5, 6, -7, -8, 9, 10, -11, -12, 13, 14, -15, -16, 17, 18, -19, -20]) == False
    assert candidate(nums = [-10, 9, 8, -7, 6, -5, 4, -3, 2, -1]) == False
    assert candidate(nums = [-2, -3, -1, 3, 2, 1, 5]) == True
    assert candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -11]) == False
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [3, 2, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True
    assert candidate(nums = [3, 1, 2, -2, -5, 6, -1]) == False
    assert candidate(nums = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5]) == False
    assert candidate(nums = [5, 1, 4, 2, 0, 6, 3]) == True
    assert candidate(nums = [5, -1, 5, -1, 5, -1, 5, -1, 5, -1]) == False
    assert candidate(nums = [1, 2, 3, 4, -1, -2, -3, -4]) == False
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == False
    assert candidate(nums = [2, 3, 1, -4, -4, 2]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [4, 2, 3, 1, 1, -1, -1]) == False
    assert candidate(nums = [-3, -1, -2, -3, -1, -2, -3, -1, -2, -3]) == True
    assert candidate(nums = [2, 3, -1, 4, -1, -2]) == False
    assert candidate(nums = [-3, 3, 2, 1, -2, -1, 4, -4]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, -6, -5, -4, -3, -2, -1]) == False
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == True
    assert candidate(nums = [1, 2, -1, -2, 1, 2, -1, -2, 1, 2, -1, -2]) == False
    assert candidate(nums = [0, 1, 1, 4, -1, 2, -1, -3, -2, 4, -5, 5, 6, 7, -7, 8, 9, 10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15, 16, -16, 17, -17, 18, -18, 19, -19, 20, -20, 21, -21, 22, -22, 23, -23, 24, -24, 25, -25, 26, -26, 27, -27, 28, -28, 29, -29, 30, -30, 31, -31, 32, -32, 33, -33, 34, -34, 35, -35, 36, -36, 37, -37, 38, -38, 39, -39, 40, -40, 41, -41, 42, -42, 43, -43, 44, -44, 45, -45, 46, -46, 47, -47, 48, -48, 49, -49, 50, -50]) == False
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(nums = [5, 4, 3, 2, 1, -5, -4, -3, -2, -1]) == False
    assert candidate(nums = [5, -1, 3, 2, -3, 4, -4, 2, 1, -1]) == False
    assert candidate(nums = [-2, 1, -1, -2, -2, 2, -1, 2, 1, -1]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, -10]) == True
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == False
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == False
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, -10, -20, -30, -40, -50, -60, -70, -80, -90]) == False
    assert candidate(nums = [2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == False
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == False
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == False
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == True
    assert candidate(nums = [5, -2, 5, -2, 5, -2, 5, -2]) == True
    assert candidate(nums = [3, 1, 2, -3, 4, 2, 1, -4, 2, 3]) == False
    assert candidate(nums = [3, 1, 2, -1, -2, 4]) == False
    assert candidate(nums = [1, 2, -1, 2, -1, 2, -1, 2, -1, 2]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == False
    assert candidate(nums = [-1, 2, 2, -1, -2, 1]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == False
    assert candidate(nums = [3, 1, 2, -2, -1]) == False
    assert candidate(nums = [2, 1, -1, -2, 2, 3, -3, -2, 1]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == False
    assert candidate(nums = [2, 3, -2, 2, -3, 2, -2, 3, -3, 1]) == False
    assert candidate(nums = [5, 3, 2, 1, 4, -2, -1, -3, -1]) == False
    assert candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 1]) == True
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == False
    assert candidate(nums = [5, 5, 2, 1, -2, -1, -3, -5, 4, 4, 3, 2, -2, -3, -4, -5, 1, 1, 2, 3]) == False
    assert candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == True
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == False
    assert candidate(nums = [3, 1, 2, 4, -1]) == False
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50]) == False
    assert candidate(nums = [-2, -3, -4, -5, 6, 7]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [-2, -3, -4, -5, -6, -1]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == False
    assert candidate(nums = [5, 1, 3, 2, 2, -1, 4]) == False
    assert candidate(nums = [10, 10, -10, -10, 10, -10, 10, -10]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1]) == False
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == True
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == False
    assert candidate(nums = [3, 1, 2, -2, 4, 2]) == True
    assert candidate(nums = [3, 1, 2, 4, 0, 2, -1, -3, -1]) == False
    assert candidate(nums = [-1, 2, 1, -2, 2, -1, 2, -1]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [5, 4, 3, 2, 1, -1]) == False
    assert candidate(nums = [2, 2, -2, -2, 2, 2, -2, -2]) == False
    assert candidate(nums = [1, 2, -1, -2, 3, 2, -3, 3]) == False
    assert candidate(nums = [2, -1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == False
    assert candidate(nums = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == True
    assert candidate(nums = [4, -1, 2, -1, -1, 2, -1, 4]) == False
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == False
    assert candidate(nums = [1, -1, 1, -1, 1, -1]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [1, 2, 3, -4, -3, -2, -1, 4, 3, 2]) == False
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(nums = [10, -10, 10, -10, 10, -10]) == True
    assert candidate(nums = [-2, -3, -4, -5, -6, -7, -8, -9, -10, -1]) == False
    assert candidate(nums = [-2, -3, -4, 0, -1, -6]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]) == False
