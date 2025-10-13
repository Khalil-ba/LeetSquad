# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 5,rollMax = [2, 2, 2, 2, 2, 2]) == 7200
    assert candidate(n = 1,rollMax = [1, 1, 1, 1, 1, 1]) == 6
    assert candidate(n = 1,rollMax = [15, 15, 15, 15, 15, 15]) == 6
    assert candidate(n = 10,rollMax = [2, 3, 4, 5, 6, 7]) == 58240426
    assert candidate(n = 2,rollMax = [1, 1, 2, 2, 2, 3]) == 34
    assert candidate(n = 2,rollMax = [1, 1, 1, 1, 1, 1]) == 30
    assert candidate(n = 5,rollMax = [1, 2, 3, 4, 5, 6]) == 6919
    assert candidate(n = 5,rollMax = [1, 1, 1, 1, 1, 1]) == 3750
    assert candidate(n = 4,rollMax = [1, 2, 3, 4, 5, 6]) == 1188
    assert candidate(n = 3,rollMax = [1, 1, 1, 2, 2, 3]) == 181
    assert candidate(n = 50,rollMax = [5, 5, 5, 5, 5, 5]) == 808684040
    assert candidate(n = 300,rollMax = [1, 1, 1, 15, 1, 15]) == 728503686
    assert candidate(n = 150,rollMax = [1, 2, 2, 3, 3, 4]) == 917820088
    assert candidate(n = 300,rollMax = [3, 3, 3, 3, 3, 3]) == 197968606
    assert candidate(n = 25,rollMax = [15, 14, 13, 12, 11, 10]) == 470351288
    assert candidate(n = 350,rollMax = [2, 3, 4, 5, 6, 7]) == 326686679
    assert candidate(n = 100,rollMax = [5, 5, 5, 5, 5, 5]) == 505697887
    assert candidate(n = 15,rollMax = [1, 1, 2, 2, 3, 3]) == 758892805
    assert candidate(n = 4,rollMax = [3, 2, 1, 2, 3, 4]) == 1176
    assert candidate(n = 150,rollMax = [5, 5, 5, 5, 5, 5]) == 488934088
    assert candidate(n = 10,rollMax = [1, 1, 1, 2, 3, 4]) == 27915907
    assert candidate(n = 50,rollMax = [2, 3, 4, 5, 6, 7]) == 197242731
    assert candidate(n = 10,rollMax = [2, 3, 1, 1, 4, 5]) == 36308544
    assert candidate(n = 50,rollMax = [3, 4, 5, 6, 7, 8]) == 753899520
    assert candidate(n = 400,rollMax = [1, 2, 1, 2, 1, 2]) == 987298539
    assert candidate(n = 200,rollMax = [2, 3, 4, 5, 6, 7]) == 221148447
    assert candidate(n = 50,rollMax = [1, 2, 1, 2, 1, 2]) == 825497499
    assert candidate(n = 50,rollMax = [1, 2, 3, 4, 5, 15]) == 992520282
    assert candidate(n = 200,rollMax = [2, 2, 2, 2, 2, 2]) == 818530237
    assert candidate(n = 10,rollMax = [1, 1, 1, 1, 1, 1]) == 11718750
    assert candidate(n = 100,rollMax = [10, 10, 10, 10, 10, 10]) == 568370197
    assert candidate(n = 30,rollMax = [1, 2, 1, 2, 1, 2]) == 679107530
    assert candidate(n = 100,rollMax = [1, 1, 2, 2, 3, 3]) == 12398650
    assert candidate(n = 100,rollMax = [1, 1, 1, 1, 1, 1]) == 776377743
    assert candidate(n = 400,rollMax = [15, 14, 13, 12, 11, 10]) == 379975553
    assert candidate(n = 20,rollMax = [5, 5, 5, 5, 5, 5]) == 703140572
    assert candidate(n = 100,rollMax = [1, 1, 2, 2, 3, 3]) == 12398650
    assert candidate(n = 20,rollMax = [2, 3, 4, 5, 6, 7]) == 412603689
    assert candidate(n = 400,rollMax = [4, 4, 4, 4, 4, 4]) == 418009264
    assert candidate(n = 150,rollMax = [7, 6, 5, 4, 3, 2]) == 3950632
    assert candidate(n = 40,rollMax = [3, 1, 2, 4, 1, 3]) == 255974937
