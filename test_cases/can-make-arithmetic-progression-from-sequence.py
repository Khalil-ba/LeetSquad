# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr = [2, 4, 6, 8, 10]) == True
    assert candidate(arr = [-1, 1, 0]) == True
    assert candidate(arr = [5, 3, 1, 4, 2]) == True
    assert candidate(arr = [10, 20, 30, 40, 50]) == True
    assert candidate(arr = [10, 5, 15]) == True
    assert candidate(arr = [5, 3, 1, 2, 4]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11]) == True
    assert candidate(arr = [5, 3, 1, 4]) == False
    assert candidate(arr = [1, 2, 3, 5]) == False
    assert candidate(arr = [100, -100, 0]) == True
    assert candidate(arr = [-5, -3, -1, 1, 3, 5]) == True
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(arr = [5, 3, 1]) == True
    assert candidate(arr = [1, 2, 3, 4, 5]) == True
    assert candidate(arr = [0, 0, 0, 0]) == True
    assert candidate(arr = [10, 5, 0, -5, -10]) == True
    assert candidate(arr = [1, 1, 1, 1]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(arr = [1, 2, 4]) == False
    assert candidate(arr = [-1, 1, 3]) == True
    assert candidate(arr = [100, 50, 0, -50, -100]) == True
    assert candidate(arr = [3, 5, 1]) == True
    assert candidate(arr = [0, 0, 0]) == True
    assert candidate(arr = [-1, 0, 1, 2]) == True
    assert candidate(arr = [1, 2, 2, 3, 3, 4]) == False
    assert candidate(arr = [10, 10, 10, 10]) == True
    assert candidate(arr = [1000000, -1000000, 0]) == True
    assert candidate(arr = [10, 0, 20, 10]) == False
    assert candidate(arr = [-5, 0, 5, 10, 15, 20, 25]) == True
    assert candidate(arr = [5, 8, 11, 14, 17, 20]) == True
    assert candidate(arr = [100, 200, 300, 400, 500]) == True
    assert candidate(arr = [-3, -6, -9, -12, -15]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == True
    assert candidate(arr = [5, 5, 5, 5, 5]) == True
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16]) == True
    assert candidate(arr = [1, 2, 2, 3, 4]) == False
    assert candidate(arr = [1, 6, 3, 11, 9, 5]) == False
    assert candidate(arr = [-1000000, -999998, -999996, -999994]) == True
    assert candidate(arr = [1000000, -1000000, 500000, -500000, 0]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == False
    assert candidate(arr = [1000000, 999998, 999996, 999994]) == True
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == True
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(arr = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == False
    assert candidate(arr = [1000000, 2000000, 3000000, 4000000, 5000000]) == True
    assert candidate(arr = [1000000, 999998, 1000002, 999996, 1000004, 999994, 1000006, 999992, 1000008, 999990]) == True
    assert candidate(arr = [1, 2, 3, 4, 6, 8, 10]) == False
    assert candidate(arr = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == True
    assert candidate(arr = [-2, -4, -6, -8, -10, -12, -14, -16]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]) == False
    assert candidate(arr = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(arr = [38, 34, 30, 26, 22, 18, 14, 10, 6, 2]) == True
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == True
    assert candidate(arr = [-5, 0, 5, 10, 15]) == True
    assert candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == False
    assert candidate(arr = [1000000, 1000000, 1000000, 1000000, 1000000]) == True
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56]) == True
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(arr = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == True
    assert candidate(arr = [1000, 1001, 1002, 1003, 1004, 1005]) == True
    assert candidate(arr = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(arr = [1, 2, 2, 3, 4, 5]) == False
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == True
    assert candidate(arr = [100, 50, 0, -50, -100]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60]) == True
    assert candidate(arr = [-1000000, -1000001, -1000002, -1000003, -1000004]) == True
    assert candidate(arr = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0, -1, -3, -7, -15, -31, -62, -125, -250, -500, -1000]) == False
    assert candidate(arr = [1000000, 500000, 0, -500000, -1000000]) == True
    assert candidate(arr = [100, 50, 25, 0, -25, -50, -100]) == False
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == True
    assert candidate(arr = [-1000000, -999999, -999998, -999997, -999996]) == True
    assert candidate(arr = [9, 3, 15, 6, 12, 0, 18, 21, 24, 27]) == True
    assert candidate(arr = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == True
    assert candidate(arr = [1, 3, 6, 10, 15]) == False
    assert candidate(arr = [-3, -1, 1, 3, 5, 7, 9, 11, 13]) == True
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == True
    assert candidate(arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == True
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700]) == True
    assert candidate(arr = [1, 6, 11, 16, 21, 26]) == True
    assert candidate(arr = [7, 3, 11, 5, 9, 1]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == False
    assert candidate(arr = [7, 14, 21, 28, 35]) == True
    assert candidate(arr = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]) == True
    assert candidate(arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]) == False
    assert candidate(arr = [7, 7, 7, 7, 7]) == True
    assert candidate(arr = [-1000, 1000, 0, 500, -500, 250, -250, 750, -750]) == True
    assert candidate(arr = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == True
    assert candidate(arr = [7, 7, 7, 7, 7, 7]) == True
    assert candidate(arr = [23, 19, 15, 11, 7, 3, -1, -5]) == True
    assert candidate(arr = [10, 20, 30, 40, 50]) == True
    assert candidate(arr = [10, 5, 0, -5, -10, -15, -20, -25, -30]) == True
    assert candidate(arr = [-10, -20, -30, -40, -50]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(arr = [10, 20, 40, 50, 60]) == False
    assert candidate(arr = [42, 42]) == True
    assert candidate(arr = [-1000000, 1000000, 0, 500000, -500000]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
    assert candidate(arr = [100, 200, 300, 400, 500, 600]) == True
    assert candidate(arr = [7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 101]) == False
    assert candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == True
    assert candidate(arr = [-5, -10, -15, -20, -25, -30]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(arr = [-1000000, -1000001, -1000002, -1000003]) == True
    assert candidate(arr = [3, -1, 1, 5, -3, 7]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == False
    assert candidate(arr = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]) == True
    assert candidate(arr = [0, 1, 3, 6, 10, 15, 21]) == False
    assert candidate(arr = [100, 99, 97, 94, 90, 85, 79, 72, 64, 55, 45]) == False
    assert candidate(arr = [5, 1, 7, 3, 9]) == True
    assert candidate(arr = [-5, -10, -15, -20, -25]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == True
    assert candidate(arr = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == True
    assert candidate(arr = [1000000, 999999, 999998, 999997]) == True
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
    assert candidate(arr = [1000000, -1000000, 500000, 0, 1500000, -500000]) == True
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24]) == True
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == True
    assert candidate(arr = [1, 2, 3, 6, 5, 4]) == True
    assert candidate(arr = [100, 200, 150, 50, 250, 0]) == True
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]) == True
    assert candidate(arr = [-3, -2, -1, 0, 1, 2, 3]) == True
    assert candidate(arr = [1, 2, 2, 3, 4, 5, 6]) == False
    assert candidate(arr = [50, 60, 70, 80, 90, 100, 110, 120]) == True
    assert candidate(arr = [2, 4, 8, 16, 32]) == False
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64]) == False
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15]) == True
    assert candidate(arr = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == True
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]) == True
    assert candidate(arr = [5, 9, 13, 17, 21, 25]) == True
    assert candidate(arr = [12, 18, 24, 30, 36, 42, 48]) == True
    assert candidate(arr = [1, 1, 2, 3, 5, 8, 13, 21]) == False
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == True
    assert candidate(arr = [100, 200, 150, 250, 300, 350, 400]) == True
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]) == True
    assert candidate(arr = [10, 70, 30, 50, 90]) == True
    assert candidate(arr = [1, 100, 50, 75, 25]) == False
    assert candidate(arr = [500000, 499998, 499996, 499994, 499992]) == True
    assert candidate(arr = [1, 4, 7, 10, 13, 16, 19, 22, 25]) == True
    assert candidate(arr = [10, 5, 0, -5, -10]) == True
    assert candidate(arr = [1, 1, 1, 1, 1, 1]) == True
    assert candidate(arr = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40]) == True
    assert candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == True
    assert candidate(arr = [-1000, -500, 0, 500, 1000]) == True
    assert candidate(arr = [5, 3, 1, -1, -3, -5, -7, -9, -11, -13]) == True
    assert candidate(arr = [1000000, -1000000, 0, 500000, -500000]) == True
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == True
    assert candidate(arr = [10, 0, -10, -20, -30]) == True
    assert candidate(arr = [-5, 0, 5, 10, 15, 20]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30]) == True
    assert candidate(arr = [5, 10, 15, 20, 25]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == False
    assert candidate(arr = [3, 1, 5, 7, 9]) == True
