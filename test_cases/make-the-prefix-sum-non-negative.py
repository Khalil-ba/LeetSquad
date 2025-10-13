# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [-1, 2, -3, 4, -5]) == 2
    assert candidate(nums = [1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, -15]) == 0
    assert candidate(nums = [-1, -2, -3, 4, 5, 6]) == 3
    assert candidate(nums = [-5, -4, -3, -2, -1]) == 5
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [2, 3, -5, 4]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [-10, 20, -30, 40, -50, 60]) == 2
    assert candidate(nums = [5, 5, 5, -15, 5]) == 0
    assert candidate(nums = [0, -1, 2, -3, 4, -5, 6]) == 2
    assert candidate(nums = [-10, 100, -50, 25, -25, 75]) == 1
    assert candidate(nums = [100, -50, -25, -25, 50]) == 0
    assert candidate(nums = [10, 20, -30, 40, 50]) == 0
    assert candidate(nums = [3, -5, -2, 6]) == 1
    assert candidate(nums = [10, -10, 20, -20, 30]) == 0
    assert candidate(nums = [-5, 100, -50, 25, -25, 75]) == 1
    assert candidate(nums = [-1, -2, -3, -4, 20]) == 4
    assert candidate(nums = [1000000000, -500000000, -500000000, 500000000]) == 0
    assert candidate(nums = [100, 200, 300, -150, -250, -350, 400, 500, -600]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 0
    assert candidate(nums = [10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 1
    assert candidate(nums = [10, -3, -7, 5, -2, 1, -4, 8]) == 0
    assert candidate(nums = [100, -50, 20, -10, 5, -1, 0, -1, -2, -3]) == 0
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 3
    assert candidate(nums = [-9, 1, -2, 3, -4, 5, -6, 7, -8, 9]) == 3
    assert candidate(nums = [5, -3, -8, 10, 2, -7, 1]) == 1
    assert candidate(nums = [10, -10, 20, -20, 30, -30]) == 0
    assert candidate(nums = [-1000, 500, -250, 125, -62, 31, -15, 7, -3, 1]) == 1
    assert candidate(nums = [10, 20, 30, -15, -25, -35, 50, 60, -40, -50]) == 1
    assert candidate(nums = [1000000000, -500000000, -500000000, 1]) == 0
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 55]) == 0
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15]) == 3
    assert candidate(nums = [-100, 10, -200, 20, -300, 30, -400, 40, -500, 50, -600, 60, -700, 70, -800, 80, -900, 90]) == 9
    assert candidate(nums = [10, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 5
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 10
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 3
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, 1, 1, -5, 1, 1, 1, 1, 1, -5]) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [-1, -2, -3, 100, -100, 100]) == 3
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 9
    assert candidate(nums = [100, -50, 20, -10, 5, -1, 0, -2, 3]) == 0
    assert candidate(nums = [5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 100]) == 8
    assert candidate(nums = [1000000000, -999999999, -1, 1000000000, -1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -10]) == 0
    assert candidate(nums = [1000, -500, 250, -125, 62, -31, 15, -7, 3, -1, 0]) == 0
    assert candidate(nums = [100, 200, 300, -500, 400, -300, 200, -100, 0, -100, 100, -200, 300]) == 0
    assert candidate(nums = [5, -2, -4, 3, -1, 0, 2, -1, 1, -3, 2]) == 1
    assert candidate(nums = [100, -50, 25, -12, 6, -3, 1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [1, -1000000000, 1000000000, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000, -250000000]) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 100]) == 9
    assert candidate(nums = [100, -50, 200, -300, 400, -500, 600]) == 1
    assert candidate(nums = [-100, 50, -30, 20, -10, 5, -1, 0, 1, 2]) == 1
    assert candidate(nums = [10, 20, 30, -10, -20, -30, 40, 50, 60, -100, 70, 80, 90, -200, 100]) == 0
    assert candidate(nums = [1000000000, -500000000, 500000000, -500000000, 500000000, -500000000, 500000000, -500000000]) == 0
    assert candidate(nums = [5, -10, 15, -20, 25, -30]) == 2
    assert candidate(nums = [0, 0, 0, 0, 0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [0, 0, 0, 0, -1, 0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 1
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110, -120, 130, -140, 150]) == 2
    assert candidate(nums = [5, -3, 2, -8, 4, -1, 7, -2]) == 1
    assert candidate(nums = [5, -3, -2, 1, -4, 2, -1, 3, -5, 6, -7, 8, -9, 10]) == 2
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11]) == 2
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7]) == 3
    assert candidate(nums = [1, -1000000000, 1000000000, -1000000000, 1000000000]) == 1
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000]) == 0
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 2
    assert candidate(nums = [5, -10, 15, -20, 25, -30, 35, -40]) == 2
    assert candidate(nums = [10, -1, -2, -3, 5, -4, 6]) == 0
    assert candidate(nums = [1, 2, -3, 4, 5, -6, 7, 8, -9, 10, 11, -12, 13, 14, -15]) == 0
    assert candidate(nums = [10, -3, -6, 4, -1, 2, 5, -7, 8, -2]) == 0
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 2
    assert candidate(nums = [1000000000, -500000000, 500000000, -250000000, 250000000, -125000000, 125000000]) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 55]) == 10
    assert candidate(nums = [100, 90, 80, -50, -40, -30, -20, -10, -1, 1, 10, 20]) == 0
    assert candidate(nums = [1000000000, -500000000, -250000000, -125000000, 62500000, -31250000, 15625000, -7812500, 3906250, -1953125]) == 0
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 3
    assert candidate(nums = [10, -20, 5, 15, -10, -5]) == 1
    assert candidate(nums = [100, 200, 300, -150, -250, -350, 400, 500]) == 1
    assert candidate(nums = [100, -101, 102, -103, 104, -105, 106, -107, 108, -109]) == 1
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100, -110, 120]) == 3
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4]) == 3
    assert candidate(nums = [2147483647, -1073741824, 536870912, -268435456, 134217728, -67108864, 33554432, -16777216, 8388608, -4194304]) == 0
    assert candidate(nums = [1, -10, 100, -1000, 10000, -100000, 1000000, -10000000, 100000000, -1000000000, 1000000000, -100000000, 10000000, -1000000, 100000, -10000, 1000, -100, 10, -1]) == 5
    assert candidate(nums = [100, -50, -50, 10, -10, 5, -5, 2, -2, 1, -1]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 5
    assert candidate(nums = [100, -50, -25, 20, -10, 5, -1, 0, 1, -2]) == 0
    assert candidate(nums = [10, 20, 30, 40, -100, 10, 20, 30, 40, -100, 50, 60, 70, 80, -200]) == 0
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 0
    assert candidate(nums = [5, -1, 4, -2, 3, -3, 2, -4, 1, -5]) == 0
    assert candidate(nums = [100, -10, 200, -20, 300, -30, 400, -40, 500, -50, 600, -60, 700, -70, 800, -80, 900, -90]) == 0
    assert candidate(nums = [-1, -10, 100, -50, 20, -10, 5]) == 2
    assert candidate(nums = [10, -1, -2, -3, -4, -5, 15]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [5, -10, 3, -1, 2, -8, 7]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]) == 2
    assert candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10]) == 0
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 0
    assert candidate(nums = [5, 5, -10, 5, 5, -10, 5, 5, -10]) == 0
