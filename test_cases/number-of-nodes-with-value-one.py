# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 100000,queries = [50000, 25000, 75000, 37500, 62500, 12500, 87500, 68750, 93750, 43750]) == 13
    assert candidate(n = 7,queries = [3, 3, 3]) == 3
    assert candidate(n = 2,queries = [1, 2, 1]) == 1
    assert candidate(n = 100000,queries = [50000, 25000, 75000, 12500, 87500]) == 8
    assert candidate(n = 9,queries = [9, 4, 2, 1, 5, 6, 7, 8, 3]) == 5
    assert candidate(n = 20,queries = [1, 2, 4, 8, 16]) == 13
    assert candidate(n = 15,queries = [1, 2, 4, 8, 16]) == 10
    assert candidate(n = 1000,queries = [500, 250, 750, 125, 375, 625, 875, 63, 313, 438]) == 31
    assert candidate(n = 10,queries = [5, 10, 1]) == 9
    assert candidate(n = 7,queries = [4, 2, 3, 6, 5, 7]) == 2
    assert candidate(n = 10,queries = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(n = 10,queries = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(n = 100,queries = [50, 25, 75, 1, 99]) == 96
    assert candidate(n = 100000,queries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50849
    assert candidate(n = 15,queries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 5
    assert candidate(n = 5,queries = [1, 2, 5]) == 3
    assert candidate(n = 7,queries = [1, 1, 1, 1, 1, 1, 1]) == 7
    assert candidate(n = 20,queries = [10, 15, 20, 5, 1]) == 16
    assert candidate(n = 100,queries = [50, 25, 75, 100, 1]) == 96
    assert candidate(n = 50000,queries = [25000, 12500, 37500, 6250, 18750, 43750, 75000, 3125, 15625, 23438]) == 19
    assert candidate(n = 10,queries = [1, 1, 1, 1, 1]) == 10
    assert candidate(n = 15,queries = [7, 10, 14, 15]) == 2
    assert candidate(n = 50000,queries = [25000, 12500, 37500, 50000, 1, 2, 3, 4, 5]) == 32769
    assert candidate(n = 100000,queries = [50000, 50000, 50000]) == 2
    assert candidate(n = 2,queries = [1, 2]) == 1
    assert candidate(n = 50000,queries = [25000, 12500, 37500, 18750, 43750]) == 5
    assert candidate(n = 20,queries = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
    assert candidate(n = 100000,queries = [1, 50000, 99999]) == 99997
    assert candidate(n = 100000,queries = [50000]) == 2
    assert candidate(n = 15,queries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(n = 10,queries = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]) == 7
    assert candidate(n = 7,queries = [1, 3, 5, 7]) == 4
    assert candidate(n = 20,queries = [10, 5, 15, 2, 3, 7, 11, 13, 17, 19]) == 13
    assert candidate(n = 10,queries = [1, 5, 10, 5]) == 9
    assert candidate(n = 10,queries = [1, 2, 3, 4, 5]) == 6
    assert candidate(n = 20,queries = [10, 5, 1, 15, 20]) == 16
    assert candidate(n = 1000,queries = [500, 250, 125, 625, 312, 156, 78, 39, 20, 10]) == 91
    assert candidate(n = 10,queries = [5, 5, 5, 5, 5]) == 2
    assert candidate(n = 7,queries = [1, 3, 7, 5]) == 4
    assert candidate(n = 15,queries = [1, 3, 7, 15]) == 10
    assert candidate(n = 15,queries = [1, 4, 8, 12, 15]) == 11
    assert candidate(n = 1,queries = [1]) == 1
    assert candidate(n = 15,queries = [1, 1, 1, 1, 1]) == 15
    assert candidate(n = 100,queries = [50, 25, 75, 80, 90]) == 5
    assert candidate(n = 100,queries = [50, 25, 75, 1, 100]) == 96
    assert candidate(n = 20,queries = [10, 15, 20, 5, 1, 3]) == 11
    assert candidate(n = 10,queries = [1]) == 10
    assert candidate(n = 1000,queries = [500, 250, 750, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 613
    assert candidate(n = 100000,queries = [50000, 50000, 50000, 50000, 50000]) == 2
    assert candidate(n = 10,queries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(n = 15,queries = [1, 3, 5, 7, 9, 11, 13, 15]) == 8
    assert candidate(n = 100,queries = [50, 25, 12, 6, 3, 1]) == 74
    assert candidate(n = 10,queries = [1, 2, 4, 8, 10]) == 7
    assert candidate(n = 7,queries = [3, 7, 3]) == 1
    assert candidate(n = 7,queries = [3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(n = 10,queries = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(n = 7,queries = [1, 3, 5]) == 3
    assert candidate(n = 1,queries = []) == 0
    assert candidate(n = 20,queries = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(n = 100000,queries = [50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1]) == 77130
    assert candidate(n = 7,queries = [3, 3, 3, 3]) == 0
    assert candidate(n = 100000,queries = [50000, 25000, 75000, 100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50847
    assert candidate(n = 15,queries = [1, 3, 7, 15, 14, 13, 12, 11, 10, 9, 8, 6, 5, 4, 2]) == 5
    assert candidate(n = 10,queries = [1, 1, 1, 1]) == 0
    assert candidate(n = 100000,queries = [1, 50000, 100000]) == 99999
    assert candidate(n = 7,queries = [4, 5, 6, 7]) == 4
    assert candidate(n = 8,queries = [2, 4, 6, 8, 1, 3, 5, 7]) == 5
    assert candidate(n = 100000,queries = [1, 100000]) == 99999
    assert candidate(n = 7,queries = [1, 3, 7, 3, 7]) == 7
    assert candidate(n = 10,queries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(n = 3,queries = [2, 3, 3]) == 1
    assert candidate(n = 7,queries = [1, 3, 7]) == 5
    assert candidate(n = 100,queries = [50, 25, 75, 12, 37, 63, 88, 4, 69, 92]) == 41
    assert candidate(n = 1000,queries = [500, 250, 125, 62, 31, 15, 7, 3, 1]) == 662
    assert candidate(n = 10,queries = [1, 1, 1]) == 10
    assert candidate(n = 100000,queries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50000, 100000]) == 50848
    assert candidate(n = 10,queries = [1, 4, 4, 8]) == 9
    assert candidate(n = 10,queries = [1, 3, 7, 9]) == 7
