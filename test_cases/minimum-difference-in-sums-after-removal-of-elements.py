# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == -80
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -180
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -18
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == -36
    assert candidate(nums = [1, 2, 3, 100, 100, 100]) == -197
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == -8
    assert candidate(nums = [100000, 1, 100000, 1, 100000, 1]) == -99999
    assert candidate(nums = [3, 1, 2]) == -1
    assert candidate(nums = [7, 9, 5, 8, 1, 3]) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 50
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6]) == -147
    assert candidate(nums = [5, 3, 8, 1, 4, 7, 2, 6, 9]) == -14
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == -18000
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == -20
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == -80
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 160
    assert candidate(nums = [2, 1, 3, 2, 1, 3, 2, 1, 3]) == -4
    assert candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1]) == 3
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == -54
    assert candidate(nums = [1, 2, 3, 100, 200, 300, 4, 5, 6]) == -594
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8]) == -12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == -12
    assert candidate(nums = [1, 100000, 1, 2, 100000, 2, 3, 100000, 3, 4, 100000, 4]) == -200002
    assert candidate(nums = [3, 5, 2, 8, 1, 9]) == -12
    assert candidate(nums = [6, 1, 5, 2, 4, 3]) == -4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == -100
    assert candidate(nums = [99999, 99999, 99999, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9, 0, 11, 13]) == -24
    assert candidate(nums = [3, 2, 1, 6, 5, 4, 9, 8, 7]) == -18
    assert candidate(nums = [1, 1, 1, 1, 100000, 100000, 100000, 100000, 100000]) == -299997
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 1, 2, 3]) == 9
    assert candidate(nums = [100000, 1, 2, 3, 100000, 4, 5, 6, 100000]) == -200000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -50
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14]) == -34
    assert candidate(nums = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 0
    assert candidate(nums = [8, 6, 7, 5, 3, 0, 9, 1, 4, 2, 7, 6]) == -12
    assert candidate(nums = [100000, 100000, 100000, 1, 1, 1, 100000, 100000, 100000]) == -299997
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == -1800
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == -3
    assert candidate(nums = [9, 7, 5, 3, 1, 11, 13, 15, 17, 19, 21, 23]) == -64
    assert candidate(nums = [100000, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == -99999
    assert candidate(nums = [200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100]) == -200
    assert candidate(nums = [99999, 1, 99998, 2, 99997, 3, 99996, 4, 99995]) == -199989
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1, 10, 100]) == -110889
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == -32
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12]) == -26
    assert candidate(nums = [1, 2, 100000, 3, 100000, 4, 5, 100000, 6]) == -200000
    assert candidate(nums = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == -199998
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == -1800
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1, 10, 100, 1000, 10000, 100000]) == -218889
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 2, 4, 6]) == -18
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == -16
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == -36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]) == -162
    assert candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5]) == -199994
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == -3200
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == -180
    assert candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100]) == -200
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88]) == 16
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 5, 3, 8]) == -13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -50
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == -30
    assert candidate(nums = [30000, 20000, 10000, 50000, 40000, 60000, 90000, 80000, 70000]) == -180000
    assert candidate(nums = [1, 1, 1, 100000, 100000, 100000, 1, 1, 1]) == -299997
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 100000, 100000, 100000]) == -299997
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 100000, 100000, 100000]) == -299997
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95]) == -284
    assert candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == -300
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == -320
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]) == -360
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 1, 2, 3]) == -900000
    assert candidate(nums = [99999, 99998, 99997, 1, 2, 3, 4, 5, 6]) == -9
    assert candidate(nums = [1, 2, 3, 100000, 100000, 100000]) == -199997
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992]) == 9
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == -16
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == -2
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == -10
    assert candidate(nums = [12345, 67890, 54321, 98765, 43210, 87654, 32109, 76543, 21098]) == -128406
    assert candidate(nums = [9, 3, 6, 3, 9, 3, 6, 3, 9, 3, 6, 3, 9, 3, 6, 3, 9, 3, 6, 3, 9, 3, 6, 3]) == -21
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 1, 2, 3, 4, 5, 6]) == 199976
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1]) == -10
    assert candidate(nums = [50, 50, 50, 1, 1, 1, 100, 100, 100]) == -297
    assert candidate(nums = [50, 25, 100, 75, 150, 125, 200, 175, 225]) == -450
    assert candidate(nums = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == -199998
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == -20
    assert candidate(nums = [50000, 40000, 30000, 20000, 10000, 90000, 80000, 70000, 60000]) == -180000
    assert candidate(nums = [5, 4, 3, 2, 1, 9, 8, 7, 6]) == -18
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == -72
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 8, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 7, 2, 8, 1, 5, 9, 7, 6, 3, 128, 256, 128]) == -563
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20]) == 90
    assert candidate(nums = [99999, 1, 99998, 2, 99997, 3, 99996, 4, 99995]) == -199989
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -18
    assert candidate(nums = [7, 3, 5, 1, 9, 4, 6, 8, 2, 10, 12, 11]) == -28
    assert candidate(nums = [1, 3, 5, 2, 4, 6]) == -7
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8]) == -15
    assert candidate(nums = [3, 1, 2, 5, 4, 6, 9, 7, 8]) == -18
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6]) == -12
    assert candidate(nums = [100000, 100000, 1, 1, 100000, 100000, 1, 1, 100000]) == -199998
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2]) == 10
    assert candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996, 6, 99995]) == -299984
    assert candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6]) == -1497
    assert candidate(nums = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == -36
    assert candidate(nums = [6, 2, 8, 4, 10, 12, 1, 3, 5, 7, 9, 11]) == -22
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 1, 2, 3]) == -900
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 1, 2, 3, 4, 5, 6]) == -100011
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
