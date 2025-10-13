# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(books = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]) == 36
    assert candidate(books = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(books = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(books = [100000]) == 100000
    assert candidate(books = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 999865
    assert candidate(books = [5, 4, 3, 2, 1]) == 7
    assert candidate(books = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(books = [7, 0, 3, 4, 5]) == 12
    assert candidate(books = [1]) == 1
    assert candidate(books = [8, 2, 3, 7, 3, 4, 0, 1, 4, 3]) == 13
    assert candidate(books = [0]) == 0
    assert candidate(books = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22
    assert candidate(books = [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]) == 9
    assert candidate(books = [100000, 99999, 99998, 99997, 99996]) == 499970
    assert candidate(books = [0, 0, 0, 0, 0]) == 0
    assert candidate(books = [8, 5, 2, 7, 9]) == 19
    assert candidate(books = [1, 2, 3, 4, 5]) == 15
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 325
    assert candidate(books = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(books = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 400
    assert candidate(books = [1, 2, 3, 0, 1, 2, 3, 4, 5, 6]) == 21
    assert candidate(books = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 3
    assert candidate(books = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 77
    assert candidate(books = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 780
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
    assert candidate(books = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 41
    assert candidate(books = [5, 6, 6, 6, 7, 8, 8, 9, 10, 10, 11, 12, 13, 13, 14, 15, 16, 17, 17, 18]) == 171
    assert candidate(books = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(books = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 47
    assert candidate(books = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 1430
    assert candidate(books = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(books = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]) == 225
    assert candidate(books = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 117
    assert candidate(books = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(books = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]) == 1260
    assert candidate(books = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(books = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(books = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 220
    assert candidate(books = [5, 6, 7, 8, 9, 10, 4, 3, 2, 1]) == 45
    assert candidate(books = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55]) == 190
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(books = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(books = [3, 2, 1, 4, 6, 5, 7, 8, 10, 9]) == 43
    assert candidate(books = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 21
    assert candidate(books = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(books = [1, 3, 5, 2, 4, 6, 8, 7, 9, 10]) == 44
    assert candidate(books = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 15
    assert candidate(books = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 18
    assert candidate(books = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55
    assert candidate(books = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 15
    assert candidate(books = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(books = [10, 10, 10, 10, 1, 1, 1, 1, 1, 1]) == 34
    assert candidate(books = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 15
    assert candidate(books = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981]) == 1999430
    assert candidate(books = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7]) == 28
    assert candidate(books = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 23
    assert candidate(books = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 23
    assert candidate(books = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 200
    assert candidate(books = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(books = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22
    assert candidate(books = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == 10
    assert candidate(books = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0]) == 100
    assert candidate(books = [3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(books = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(books = [5, 10, 15, 20, 25, 20, 15, 10, 5, 1]) == 87
    assert candidate(books = [0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000]) == 100000
    assert candidate(books = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(books = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(books = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(books = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(books = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 55
    assert candidate(books = [5, 3, 6, 7, 9, 4, 2, 8, 10, 1]) == 27
    assert candidate(books = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(books = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 10
    assert candidate(books = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(books = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 3
    assert candidate(books = [5, 3, 1, 2, 4, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15]) == 109
    assert candidate(books = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(books = [100, 50, 0, 50, 100, 50, 0, 50, 100, 50, 0]) == 150
    assert candidate(books = [10, 10, 10, 10, 10, 5, 5, 5, 5, 5]) == 40
    assert candidate(books = [5, 6, 6, 6, 7, 8, 8, 9, 10, 10]) == 55
    assert candidate(books = [100, 100, 100, 100, 100, 99, 98, 97, 96, 95]) == 905
    assert candidate(books = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]) == 185
    assert candidate(books = [0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000]) == 100000
    assert candidate(books = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 11
    assert candidate(books = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 50
    assert candidate(books = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(books = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 110
    assert candidate(books = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 865
    assert candidate(books = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]) == 3
    assert candidate(books = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 1540
    assert candidate(books = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 28
    assert candidate(books = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(books = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 15
    assert candidate(books = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
    assert candidate(books = [1, 3, 5, 7, 9, 7, 5, 3, 1, 0, 1, 3, 5, 7, 9, 7, 5, 3, 1, 0]) == 26
    assert candidate(books = [100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50]) == 847
    assert candidate(books = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 220
    assert candidate(books = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 77
    assert candidate(books = [10, 1, 2, 3, 10, 5, 6, 7, 10, 9, 8, 7, 10, 11, 12, 13, 14, 15, 16, 17]) == 136
    assert candidate(books = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 15
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 325
    assert candidate(books = [100, 50, 25, 10, 5, 1, 0, 0, 0, 0]) == 100
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 465
    assert candidate(books = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 165
    assert candidate(books = [55, 45, 36, 28, 21, 15, 10, 6, 3, 1]) == 106
    assert candidate(books = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 23
    assert candidate(books = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(books = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 55
    assert candidate(books = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 105
    assert candidate(books = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(books = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 45
    assert candidate(books = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(books = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 15
    assert candidate(books = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 100
    assert candidate(books = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 21
    assert candidate(books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(books = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 23
    assert candidate(books = [100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0]) == 100000
    assert candidate(books = [3, 4, 6, 2, 3, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(books = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(books = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 23
    assert candidate(books = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(books = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(books = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == 442
    assert candidate(books = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 172
    assert candidate(books = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 6
    assert candidate(books = [1, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 136
    assert candidate(books = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 1430
    assert candidate(books = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(books = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == 10
    assert candidate(books = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]) == 15
    assert candidate(books = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 1540
    assert candidate(books = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 100
