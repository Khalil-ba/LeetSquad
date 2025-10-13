# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [4, 6, 8, 10, 12]) == 1
    assert candidate(nums = [2, 4, 6, 8, 10, 12]) == 1
    assert candidate(nums = [1, 1, 1, 1]) == -1
    assert candidate(nums = [2, 3, 5, 7, 11]) == 5
    assert candidate(nums = [7, 14, 28, 56, 112]) == 1
    assert candidate(nums = [10, 5, 20, 2, 8]) == 1
    assert candidate(nums = [15, 25, 35, 5]) == 1
    assert candidate(nums = [29, 29, 29, 29, 29]) == 1
    assert candidate(nums = [2]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [1, 2, 1]) == -1
    assert candidate(nums = [12, 15, 18]) == 1
    assert candidate(nums = [7, 7, 7, 7, 7]) == 1
    assert candidate(nums = [6, 10, 3, 15]) == 1
    assert candidate(nums = [100, 200, 400, 800, 1600]) == 1
    assert candidate(nums = [2, 3, 6, 9, 18]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [2, 3, 6, 9, 12]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [10, 5, 25, 20]) == 1
    assert candidate(nums = [2, 4, 8, 16, 32]) == 1
    assert candidate(nums = [2, 6, 3, 4, 3]) == 2
    assert candidate(nums = [7, 14, 28, 21, 35]) == 1
    assert candidate(nums = [100000]) == 1
    assert candidate(nums = [13, 26, 39, 52, 65]) == 1
    assert candidate(nums = [3, 5]) == 2
    assert candidate(nums = [6, 9, 12, 15]) == 1
    assert candidate(nums = [13, 17, 19, 23]) == 4
    assert candidate(nums = [6, 9, 12, 15, 18]) == 1
    assert candidate(nums = [7, 7, 7, 7]) == 1
    assert candidate(nums = [7, 14, 21, 28]) == 1
    assert candidate(nums = [3, 9, 27, 81]) == 1
    assert candidate(nums = [18, 24, 30, 42]) == 1
    assert candidate(nums = [10, 20, 30, 40]) == 1
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256]) == 1
    assert candidate(nums = [2, 3, 6, 9, 18, 27, 54]) == 1
    assert candidate(nums = [6, 10, 15, 30, 60, 120, 240]) == 1
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]) == 1
    assert candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297]) == 1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 1
    assert candidate(nums = [21, 35, 105, 175, 350, 700]) == 1
    assert candidate(nums = [8, 12, 16, 20, 24, 28]) == 1
    assert candidate(nums = [12, 15, 20, 25, 30, 35, 40, 45]) == 1
    assert candidate(nums = [9, 12, 15, 18, 21, 24, 27, 30]) == 1
    assert candidate(nums = [21, 7, 14, 42, 28, 14]) == 1
    assert candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54]) == 1
    assert candidate(nums = [9, 27, 81, 243, 729, 2187]) == 1
    assert candidate(nums = [21, 14, 49, 7, 98, 14, 42]) == 1
    assert candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]) == 1
    assert candidate(nums = [12, 15, 21, 25, 30]) == 1
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 1
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400]) == 1
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75]) == 1
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 1
    assert candidate(nums = [42, 28, 14, 7, 1]) == -1
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105]) == 1
    assert candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896]) == 1
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97]) == 2
    assert candidate(nums = [7, 49, 343, 2401, 16807, 117649]) == 1
    assert candidate(nums = [9, 27, 81, 243, 729]) == 1
    assert candidate(nums = [27, 27, 27, 27, 27, 27, 27, 27, 27, 27]) == 1
    assert candidate(nums = [6, 9, 12, 15, 18, 21, 24]) == 1
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49]) == 1
    assert candidate(nums = [48, 72, 96, 120, 144, 168, 192, 216, 240, 264]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300]) == 1
    assert candidate(nums = [7, 49, 42, 14, 70, 35, 28, 21, 14, 7]) == 1
    assert candidate(nums = [18, 24, 30, 36, 42, 48, 54, 60, 66, 72]) == 1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 1
    assert candidate(nums = [2, 6, 3, 4, 3, 8, 12, 16]) == 1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == 1
    assert candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]) == 1
    assert candidate(nums = [15, 25, 35, 55, 65]) == 1
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 1
    assert candidate(nums = [100, 200, 400, 500, 1000, 2000]) == 1
    assert candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]) == 1
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707]) == 1
    assert candidate(nums = [6, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72]) == 1
    assert candidate(nums = [30, 45, 60, 75, 90]) == 1
    assert candidate(nums = [8, 12, 16, 4, 24, 32]) == 1
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131]) == 7
    assert candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150]) == 1
    assert candidate(nums = [17, 51, 85, 102, 136, 204, 255]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == -1
    assert candidate(nums = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13]) == 1
    assert candidate(nums = [18, 24, 30, 36, 42]) == 1
    assert candidate(nums = [18, 27, 36, 45, 54, 63, 72, 81, 90, 99]) == 1
    assert candidate(nums = [42, 63, 84, 105, 126, 147, 168]) == 1
    assert candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) == 1
    assert candidate(nums = [18, 27, 36, 45, 54, 63, 72, 81]) == 1
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 1
    assert candidate(nums = [15, 21, 35, 7, 10]) == 1
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175]) == 1
    assert candidate(nums = [100, 25, 50, 75, 125, 175, 225]) == 1
    assert candidate(nums = [9, 81, 27, 243, 729, 81]) == 1
    assert candidate(nums = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120]) == 1
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]) == 1
    assert candidate(nums = [42, 56, 70, 84, 98, 112, 126, 140, 154, 168]) == 1
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120]) == 1
    assert candidate(nums = [2, 6, 3, 4, 3, 8, 12, 6, 3, 9]) == 2
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170]) == 1
    assert candidate(nums = [81, 27, 9, 3, 1, 3, 9, 27, 81]) == 1
    assert candidate(nums = [100, 150, 200, 250, 300]) == 1
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180]) == 1
    assert candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 1
    assert candidate(nums = [20, 40, 60, 80, 100, 120]) == 1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 1
    assert candidate(nums = [7, 14, 28, 56, 112]) == 1
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == 1
    assert candidate(nums = [105, 210, 315, 420, 525, 630, 735, 840, 945, 1050]) == 1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 25
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 1
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 11
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 10
    assert candidate(nums = [15, 25, 35, 45, 55]) == 1
    assert candidate(nums = [3, 9, 27, 81, 243, 729]) == 1
    assert candidate(nums = [7, 49, 343, 2401, 16807]) == 1
    assert candidate(nums = [9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 1
    assert candidate(nums = [72, 12, 18, 24, 36, 60]) == 1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == 1
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66]) == 1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(nums = [6, 10, 15, 21, 28, 35]) == 2
    assert candidate(nums = [1000, 500, 250, 125, 625, 3125, 15625]) == 1
    assert candidate(nums = [21, 35, 49, 63, 77, 91]) == 1
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 21
    assert candidate(nums = [7, 49, 343, 2401, 16807, 117649]) == 1
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561]) == 1
    assert candidate(nums = [97, 101, 103, 107, 109, 113, 127, 131, 137, 139]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31]) == 8
    assert candidate(nums = [22, 33, 44, 55, 66, 77, 88, 99]) == 1
    assert candidate(nums = [100, 50, 25, 125, 200, 500]) == 1
    assert candidate(nums = [1500, 2250, 3000, 3750, 4500, 5250, 6000, 6750, 7500, 8250]) == 1
    assert candidate(nums = [5, 15, 25, 35, 45, 55]) == 1
    assert candidate(nums = [10, 15, 20, 25, 30, 35]) == 1
    assert candidate(nums = [60, 12, 24, 48, 18]) == 1
    assert candidate(nums = [6, 3, 9, 12, 18, 24, 30, 36, 42, 48]) == 1
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 1
    assert candidate(nums = [15, 30, 18, 45, 25, 10]) == 1
    assert candidate(nums = [18, 30, 42, 54, 60]) == 1
    assert candidate(nums = [6, 9, 12, 15, 18, 21, 24, 27, 30]) == 1
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 1
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 1
    assert candidate(nums = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44]) == 1
    assert candidate(nums = [24, 48, 72, 96, 120, 144, 168, 192, 216, 240]) == 1
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1
    assert candidate(nums = [20, 30, 40, 50, 60, 70, 80]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140]) == 1
    assert candidate(nums = [33, 11, 22, 44, 88, 176, 352]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [15, 21, 35, 49, 63, 77, 91, 105, 119, 133]) == 2
    assert candidate(nums = [18, 24, 36, 48, 60]) == 1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [14, 21, 28, 35, 42, 49, 56, 63, 70, 77]) == 1
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 10
    assert candidate(nums = [25, 45, 65, 85, 105]) == 1
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 1
    assert candidate(nums = [14, 28, 42, 56, 70, 84]) == 1
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 1
    assert candidate(nums = [84, 168, 252, 336, 420, 504, 588, 672, 756, 840, 924, 1008, 1092, 1176, 1260, 1344, 1428, 1512, 1608, 1692]) == 1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19]) == 8
