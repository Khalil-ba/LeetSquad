# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(bottom = 3,top = 7,special = [3, 4, 5, 6, 7]) == 0
    assert candidate(bottom = 1,top = 1,special = [1]) == 0
    assert candidate(bottom = 1,top = 10,special = [3, 5, 7, 9]) == 2
    assert candidate(bottom = 6,top = 8,special = [7, 6, 8]) == 0
    assert candidate(bottom = 5,top = 15,special = [10]) == 5
    assert candidate(bottom = 3,top = 15,special = [3, 5, 7, 9, 11, 15]) == 3
    assert candidate(bottom = 1,top = 10,special = [2, 5, 8]) == 2
    assert candidate(bottom = 10,top = 20,special = [12, 14, 16, 18]) == 2
    assert candidate(bottom = 6,top = 8,special = [7, 6, 8]) == 0
    assert candidate(bottom = 2,top = 9,special = [4, 6]) == 3
    assert candidate(bottom = 10,top = 20,special = [12, 15, 18]) == 2
    assert candidate(bottom = 1,top = 10,special = [5]) == 5
    assert candidate(bottom = 10,top = 10,special = [10]) == 0
    assert candidate(bottom = 1,top = 1000000000,special = [500000000]) == 500000000
    assert candidate(bottom = 3,top = 7,special = [3, 4, 5, 6, 7]) == 0
    assert candidate(bottom = 1,top = 10,special = [3, 5, 7]) == 3
    assert candidate(bottom = 2,top = 9,special = [4, 6]) == 3
    assert candidate(bottom = 1,top = 100,special = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9
    assert candidate(bottom = 1,top = 1000000,special = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000]) == 100000
    assert candidate(bottom = 2,top = 100,special = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 10
    assert candidate(bottom = 50,top = 200,special = [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 10
    assert candidate(bottom = 1,top = 1000,special = [1, 500, 1000]) == 499
    assert candidate(bottom = 10,top = 20,special = [11, 13, 15, 17]) == 3
    assert candidate(bottom = 50,top = 200,special = [100, 150, 125]) == 50
    assert candidate(bottom = 5,top = 50,special = [10, 20, 30, 40]) == 10
    assert candidate(bottom = 1,top = 1000000000,special = [1000000000]) == 999999999
    assert candidate(bottom = 1,top = 1000000000,special = [1, 1000000000]) == 999999998
    assert candidate(bottom = 5,top = 25,special = [7, 13, 19]) == 6
    assert candidate(bottom = 1,top = 500,special = [250]) == 250
    assert candidate(bottom = 5,top = 20,special = [6, 8, 10, 12, 14, 16, 18]) == 2
    assert candidate(bottom = 1,top = 1000,special = [500, 750]) == 499
    assert candidate(bottom = 1,top = 1000,special = [500]) == 500
    assert candidate(bottom = 1,top = 50,special = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]) == 2
    assert candidate(bottom = 5,top = 15,special = [6, 11]) == 4
    assert candidate(bottom = 5,top = 15,special = [7, 10, 13]) == 2
    assert candidate(bottom = 10,top = 50,special = [15, 25, 35, 45]) == 9
    assert candidate(bottom = 10,top = 50,special = [15, 25, 35]) == 15
    assert candidate(bottom = 1,top = 50,special = [50]) == 49
    assert candidate(bottom = 1,top = 100,special = [2, 98]) == 95
    assert candidate(bottom = 5,top = 25,special = [10, 20]) == 9
    assert candidate(bottom = 1,top = 100,special = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100]) == 3
    assert candidate(bottom = 1,top = 100,special = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 81
    assert candidate(bottom = 1,top = 100,special = [50]) == 50
    assert candidate(bottom = 1,top = 1000,special = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 901
    assert candidate(bottom = 1,top = 100,special = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 100]) == 1
    assert candidate(bottom = 10,top = 20,special = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(bottom = 1,top = 1000000000,special = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000]) == 100000000
    assert candidate(bottom = 1,top = 1000,special = [10, 200, 300, 400, 500, 600, 700, 800, 900]) == 189
    assert candidate(bottom = 1,top = 50,special = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47]) == 3
    assert candidate(bottom = 100,top = 200,special = [120, 130, 140, 150, 160, 170, 180, 190]) == 20
    assert candidate(bottom = 1,top = 1000,special = [1, 1000]) == 998
    assert candidate(bottom = 1,top = 1000000000,special = [1, 500000000, 1000000000]) == 499999999
    assert candidate(bottom = 10,top = 20,special = [10, 12, 14, 16, 18, 20]) == 1
    assert candidate(bottom = 1,top = 1000,special = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 100
    assert candidate(bottom = 1,top = 1000000,special = [500000]) == 500000
    assert candidate(bottom = 5,top = 50,special = [15, 25, 35, 45]) == 10
    assert candidate(bottom = 50,top = 150,special = [51, 52, 53, 54, 55, 56, 57, 58, 59, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]) == 40
    assert candidate(bottom = 1,top = 50,special = [25]) == 25
    assert candidate(bottom = 1,top = 2000000000,special = [1000000000]) == 1000000000
    assert candidate(bottom = 10,top = 100,special = [15, 35, 60, 85]) == 24
    assert candidate(bottom = 1,top = 100,special = [1, 2, 3, 4, 5, 96, 97, 98, 99, 100]) == 90
    assert candidate(bottom = 10,top = 1000,special = [150, 250, 350, 450, 550, 650, 750, 850, 950]) == 140
    assert candidate(bottom = 5,top = 50,special = [10, 15, 20, 25, 30, 35, 40, 45]) == 5
    assert candidate(bottom = 10,top = 20,special = [12, 15, 18]) == 2
    assert candidate(bottom = 1,top = 100,special = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 1
    assert candidate(bottom = 1,top = 100,special = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 10
    assert candidate(bottom = 10,top = 50,special = [12, 15, 20, 25, 30, 35, 40, 45]) == 5
    assert candidate(bottom = 10,top = 10000,special = [500, 2500, 4500, 6500, 8500]) == 1999
    assert candidate(bottom = 1,top = 100,special = [99]) == 98
    assert candidate(bottom = 1,top = 100,special = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 61
    assert candidate(bottom = 1,top = 100,special = [1, 100]) == 98
    assert candidate(bottom = 10,top = 100,special = [20, 40, 60, 80]) == 20
    assert candidate(bottom = 1,top = 1000000,special = [1, 2, 3, 4, 5, 999995, 999996, 999997, 999998, 999999]) == 999989
    assert candidate(bottom = 1,top = 20,special = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 2
    assert candidate(bottom = 1,top = 20,special = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(bottom = 1,top = 10,special = [2, 4, 6, 8]) == 2
    assert candidate(bottom = 100,top = 200,special = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]) == 1
    assert candidate(bottom = 100,top = 500,special = [200, 300, 400]) == 100
    assert candidate(bottom = 1,top = 100,special = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 9
    assert candidate(bottom = 1,top = 20,special = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
    assert candidate(bottom = 10,top = 1000,special = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 100
    assert candidate(bottom = 1,top = 100,special = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 1
    assert candidate(bottom = 1,top = 50,special = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 29
    assert candidate(bottom = 20,top = 200,special = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 10
    assert candidate(bottom = 5,top = 50,special = [15, 25, 35, 45, 5, 40]) == 9
    assert candidate(bottom = 1,top = 100,special = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == 5
    assert candidate(bottom = 10,top = 50,special = [20, 30, 40]) == 10
    assert candidate(bottom = 1,top = 100,special = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 7
    assert candidate(bottom = 1,top = 10,special = [1, 3, 5, 7, 9]) == 1
    assert candidate(bottom = 1,top = 100,special = [5, 25, 45, 65, 85, 95]) == 19
    assert candidate(bottom = 10,top = 100,special = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 75
    assert candidate(bottom = 1,top = 100,special = [2, 25, 50, 75, 100]) == 24
    assert candidate(bottom = 1,top = 10,special = [2, 4, 6, 8, 10]) == 1
