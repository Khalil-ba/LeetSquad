# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [0, 0, 0, 0, 0],k = 2) == 0
    assert candidate(nums = [0, 0, 0, 0],k = 2) == 0
    assert candidate(nums = [4, 6, 2],k = 3) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 40
    assert candidate(nums = [1, 3, 5],k = 1) == -1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6],k = 4) == 18
    assert candidate(nums = [1, 1, 1, 1, 1, 1],k = 3) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == -1
    assert candidate(nums = [2, 2, 2, 2, 2],k = 2) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 34
    assert candidate(nums = [4, 1, 5, 3, 1],k = 3) == 12
    assert candidate(nums = [2, 4, 6, 8, 10],k = 5) == 30
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == 0
    assert candidate(nums = [8, 6, 4, 2, 0],k = 3) == 18
    assert candidate(nums = [10, 20, 30, 40, 50],k = 3) == 120
    assert candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],k = 4) == 370
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 208
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 5) == 499990
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 10) == 954
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 4) == 8
    assert candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],k = 5) == 424
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 300
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 10) == 144
    assert candidate(nums = [8, 6, 4, 2, 0, -2, -4, -6, -8],k = 4) == 20
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165],k = 8) == 1012
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],k = 5) == 212
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 7) == 60
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 9) == 108
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 8) == 184
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 50
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 300
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 10) == 200
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 7) == 4900
    assert candidate(nums = [1, 3, 5, 7, 9],k = 4) == 24
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 2
    assert candidate(nums = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 3) == -1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 15) == 600
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 5) == 499990
    assert candidate(nums = [5, 8, 13, 21, 34, 55, 89, 144, 233, 377],k = 3) == 754
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 8) == 104
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980],k = 10) == 999944
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 15) == 1048544
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18],k = 5) == 70
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 8) == 520
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 44
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == -1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 4) == 88
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 15) == 1950
    assert candidate(nums = [7, 2, 9, 4, 3, 8, 6],k = 4) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 344
    assert candidate(nums = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43],k = 6) == 204
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 10) == 510
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == -1
    assert candidate(nums = [1, 3, 5, 7, 9],k = 3) == -1
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 7) == 84
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 15) == 100
    assert candidate(nums = [500, 400, 300, 200, 100, 90, 80, 70, 60, 50],k = 8) == 1740
    assert candidate(nums = [1, 3, 5],k = 3) == -1
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 6) == 599984
    assert candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],k = 3) == 540
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 110
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 3) == -1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 8) == 184
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 7) == -1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 5) == 3500
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 84
    assert candidate(nums = [11, 13, 15, 17, 19, 21, 23, 25],k = 3) == -1
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 10) == 944
    assert candidate(nums = [99, 101, 103, 105, 107, 109, 111, 113, 115, 117],k = 2) == 232
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 400
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 110
    assert candidate(nums = [8, 6, 4, 2, 0, 1, 3, 5, 7, 9],k = 8) == 44
    assert candidate(nums = [7, 11, 13, 1, 5, 3, 8, 2],k = 4) == 36
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 50
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 18
    assert candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],k = 4) == 340000
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 10) == -1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == -1
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 3) == 27000
    assert candidate(nums = [1],k = 1) == -1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 34
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3) == 2700
    assert candidate(nums = [31, 29, 23, 19, 17, 13, 11, 7, 5, 2],k = 7) == 134
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],k = 10) == 400
    assert candidate(nums = [10, 15, 3, 7, 8, 5, 2, 11],k = 4) == 44
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == -1
    assert candidate(nums = [10, 15, 20, 25, 30, 35],k = 6) == -1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 34
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 7) == 1016
    assert candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 6) == 164
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 40
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == 270
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 2
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 10) == 144
    assert candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98],k = 5) == 380
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 15) == 1950
    assert candidate(nums = [5, 8, 7, 3, 4, 2, 6, 1],k = 4) == 26
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5) == 80
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],k = 5) == 499984
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 10) == -1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 8) == 16
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5) == 80
    assert candidate(nums = [2],k = 1) == 2
    assert candidate(nums = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19],k = 3) == -1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],k = 6) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 154
    assert candidate(nums = [2, 4, 6],k = 1) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 104
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == -1
    assert candidate(nums = [10, 15, 20, 25, 30, 35],k = 4) == 110
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 5) == 40
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 6) == 44
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 100
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 15) == 390
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 7) == 699978
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],k = 6) == 584
