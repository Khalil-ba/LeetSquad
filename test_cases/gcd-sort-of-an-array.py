# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [12, 15, 18, 20, 25]) == True
    assert candidate(nums = [7, 21, 3]) == True
    assert candidate(nums = [8, 4, 12, 6]) == True
    assert candidate(nums = [2, 3, 5, 7, 11]) == True
    assert candidate(nums = [2, 4, 6, 8, 10]) == True
    assert candidate(nums = [1, 2, 3, 4]) == True
    assert candidate(nums = [18, 9, 27, 3, 6]) == True
    assert candidate(nums = [3, 9, 6, 18, 27]) == True
    assert candidate(nums = [1, 2, 3, 4, 5]) == True
    assert candidate(nums = [37, 49, 111, 143, 169]) == True
    assert candidate(nums = [100, 200, 400, 800, 1600]) == True
    assert candidate(nums = [22, 44, 11, 66, 33]) == True
    assert candidate(nums = [100, 200, 300, 400, 500]) == True
    assert candidate(nums = [83, 97, 101, 103, 107]) == True
    assert candidate(nums = [100000, 99998, 99999, 99997, 99996]) == False
    assert candidate(nums = [10, 5, 9, 3, 15]) == True
    assert candidate(nums = [105, 70, 30, 210, 42]) == True
    assert candidate(nums = [30, 42, 70, 105, 35]) == True
    assert candidate(nums = [5, 2, 6, 2]) == False
    assert candidate(nums = [56, 72, 88, 104, 120, 136, 152]) == True
    assert candidate(nums = [121, 132, 143, 154, 165, 176, 187, 198, 209]) == True
    assert candidate(nums = [48, 64, 80, 96, 112]) == True
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119]) == True
    assert candidate(nums = [210, 315, 420, 525, 630, 735]) == True
    assert candidate(nums = [105, 45, 63, 21, 315]) == True
    assert candidate(nums = [100, 50, 25, 125, 200, 150]) == True
    assert candidate(nums = [91, 182, 273, 364, 455]) == True
    assert candidate(nums = [121, 132, 143, 154, 165, 176]) == True
    assert candidate(nums = [16, 32, 48, 64, 80, 96, 112, 128, 144]) == True
    assert candidate(nums = [70, 35, 28, 56, 14, 18]) == True
    assert candidate(nums = [14, 21, 28, 35, 42, 49, 56, 63, 70]) == True
    assert candidate(nums = [32, 48, 64, 80, 96, 112]) == True
    assert candidate(nums = [31, 62, 93, 124, 155, 186, 217, 248, 279, 310]) == True
    assert candidate(nums = [30, 25, 20, 15, 10, 5]) == True
    assert candidate(nums = [30, 45, 60, 75, 90, 105]) == True
    assert candidate(nums = [44, 55, 66, 77, 88, 99, 110, 121]) == True
    assert candidate(nums = [15, 20, 25, 30, 35]) == True
    assert candidate(nums = [33, 66, 99, 132, 165]) == True
    assert candidate(nums = [49, 14, 7, 98, 28]) == True
    assert candidate(nums = [6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189]) == True
    assert candidate(nums = [49, 42, 28, 35, 70]) == True
    assert candidate(nums = [123, 246, 369, 492, 615, 738, 861, 984]) == True
    assert candidate(nums = [84, 126, 168, 210, 252, 294, 336, 378, 420]) == True
    assert candidate(nums = [84, 28, 42, 70, 56]) == True
    assert candidate(nums = [101, 202, 303, 404, 505, 606]) == True
    assert candidate(nums = [56, 14, 28, 7, 98, 49]) == True
    assert candidate(nums = [45, 30, 60, 90, 120, 150]) == True
    assert candidate(nums = [100, 50, 75, 25, 150]) == True
    assert candidate(nums = [15, 25, 35, 45, 55, 65]) == True
    assert candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184]) == True
    assert candidate(nums = [121, 221, 143, 169, 13]) == True
    assert candidate(nums = [100, 200, 300, 400, 500]) == True
    assert candidate(nums = [462, 882, 924, 1092, 1260]) == True
    assert candidate(nums = [360, 720, 1080, 1440, 1800, 2160]) == True
    assert candidate(nums = [1000, 500, 250, 125, 625]) == True
    assert candidate(nums = [48, 120, 180, 240, 300]) == True
    assert candidate(nums = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240]) == True
    assert candidate(nums = [210, 70, 35, 14, 105]) == True
    assert candidate(nums = [1024, 2048, 512, 256, 128]) == True
    assert candidate(nums = [56, 112, 168, 224, 280]) == True
    assert candidate(nums = [100, 25, 50, 20, 40]) == True
    assert candidate(nums = [24, 36, 48, 12, 60]) == True
    assert candidate(nums = [99, 33, 66, 22, 11, 132]) == True
    assert candidate(nums = [21, 42, 63, 84, 105]) == True
    assert candidate(nums = [13, 26, 39, 52, 65, 78]) == True
    assert candidate(nums = [30, 45, 60, 75, 90]) == True
    assert candidate(nums = [77, 154, 231, 308, 385]) == True
    assert candidate(nums = [91, 130, 169, 182, 273, 338]) == True
    assert candidate(nums = [22, 15, 45, 33, 10, 55]) == True
    assert candidate(nums = [18, 27, 36, 45, 54, 63, 72, 81, 90]) == True
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]) == True
    assert candidate(nums = [171, 342, 513, 684, 855]) == True
    assert candidate(nums = [33, 55, 66, 88, 110, 121, 132, 143]) == True
    assert candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == True
    assert candidate(nums = [45, 90, 135, 180, 225]) == True
    assert candidate(nums = [20, 40, 60, 80, 100, 120, 140, 160, 180]) == True
    assert candidate(nums = [100, 50, 25, 20, 125]) == True
    assert candidate(nums = [18, 24, 30, 36, 42]) == True
    assert candidate(nums = [1000, 250, 500, 200, 750, 125, 375, 625, 875, 1250]) == True
    assert candidate(nums = [102, 136, 170, 204, 238, 272, 306, 340, 374]) == True
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190]) == True
    assert candidate(nums = [27, 54, 81, 108, 135, 162, 189, 216]) == True
    assert candidate(nums = [119, 238, 357, 476, 595]) == True
    assert candidate(nums = [81, 27, 54, 162, 324, 486]) == True
    assert candidate(nums = [84, 12, 14, 21, 63]) == True
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105]) == True
    assert candidate(nums = [18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108]) == True
    assert candidate(nums = [49, 63, 77, 91, 105, 119, 133, 147, 161, 175, 189, 203, 217]) == True
    assert candidate(nums = [72, 108, 144, 180, 216, 252, 288, 324, 360, 396]) == True
    assert candidate(nums = [225, 150, 100, 50, 25, 75]) == True
    assert candidate(nums = [121, 110, 99, 88, 77, 66, 55, 44, 33, 22, 11]) == True
    assert candidate(nums = [22, 44, 66, 88, 110, 132, 154, 176, 198]) == True
    assert candidate(nums = [1000, 500, 250, 125, 2000]) == True
    assert candidate(nums = [135, 90, 45, 60, 30]) == True
    assert candidate(nums = [9, 18, 27, 36, 45, 54]) == True
    assert candidate(nums = [17, 34, 51, 68, 85]) == True
    assert candidate(nums = [105, 15, 35, 21, 63]) == True
    assert candidate(nums = [81, 135, 207, 279, 351, 423]) == True
    assert candidate(nums = [36, 48, 60, 72, 84, 96]) == True
    assert candidate(nums = [180, 120, 90, 60, 45, 30, 20, 15, 10, 5]) == True
    assert candidate(nums = [28, 14, 42, 70, 98]) == True
    assert candidate(nums = [17, 19, 23, 29, 31, 37]) == True
    assert candidate(nums = [81, 27, 54, 108, 162]) == True
    assert candidate(nums = [121, 11, 22, 33, 44, 55]) == True
    assert candidate(nums = [165, 330, 495, 660, 825]) == True
    assert candidate(nums = [49, 98, 147, 196, 245]) == True
    assert candidate(nums = [121, 44, 88, 22, 176]) == True
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85]) == True
    assert candidate(nums = [100, 101, 102, 103, 104, 105]) == True
    assert candidate(nums = [17, 19, 23, 29, 31]) == True
    assert candidate(nums = [315, 105, 35, 7, 14, 21, 42, 63, 84]) == True
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == True
    assert candidate(nums = [13, 26, 39, 52, 65]) == True
    assert candidate(nums = [15, 25, 35, 45, 55]) == True
    assert candidate(nums = [7, 49, 343, 2401, 16807]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152]) == True
    assert candidate(nums = [14, 21, 35, 49, 70]) == True
    assert candidate(nums = [33, 66, 99, 132, 165, 198]) == True
    assert candidate(nums = [18, 24, 30, 36, 42, 48]) == True
    assert candidate(nums = [22, 44, 66, 88, 110]) == True
    assert candidate(nums = [84, 56, 28, 14, 7, 49, 35]) == True
    assert candidate(nums = [48, 64, 80, 96, 112, 128]) == True
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768]) == True
    assert candidate(nums = [56, 63, 70, 77, 84, 91]) == True
    assert candidate(nums = [99, 33, 66, 132, 264]) == True
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250]) == True
    assert candidate(nums = [77, 91, 143, 1001, 1001, 143]) == True
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700]) == True
    assert candidate(nums = [77, 55, 99, 110, 132]) == True
    assert candidate(nums = [30, 45, 60, 15, 90]) == True
    assert candidate(nums = [72, 24, 16, 8, 40]) == True
    assert candidate(nums = [42, 21, 7, 14, 28]) == True
    assert candidate(nums = [77, 143, 169, 187, 209, 221, 247, 299, 323, 341]) == True
    assert candidate(nums = [15, 20, 25, 30, 35, 40, 45, 50]) == True
    assert candidate(nums = [121, 143, 169, 187, 209]) == True
    assert candidate(nums = [14, 21, 28, 35, 42, 49, 56, 63]) == True
    assert candidate(nums = [14, 21, 28, 35, 42, 49]) == True
    assert candidate(nums = [49, 147, 245, 343, 441, 539]) == True
    assert candidate(nums = [22, 15, 10, 18, 30]) == True
    assert candidate(nums = [64, 32, 16, 8, 4, 2, 1]) == False
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]) == True
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81]) == True
    assert candidate(nums = [16, 32, 64, 128, 256, 512, 1024]) == True
    assert candidate(nums = [102, 204, 306, 408, 510]) == True
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000]) == True
    assert candidate(nums = [60, 120, 180, 240, 300, 360]) == True
    assert candidate(nums = [42, 28, 70, 14, 35]) == True
    assert candidate(nums = [22, 33, 44, 55, 66]) == True
    assert candidate(nums = [77, 49, 35, 21, 14, 7]) == True
    assert candidate(nums = [23, 46, 69, 92, 115]) == True
    assert candidate(nums = [16, 8, 4, 2, 1]) == False
    assert candidate(nums = [101, 202, 303, 404, 505]) == True
    assert candidate(nums = [102, 68, 34, 17, 51, 85]) == True
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117]) == True
    assert candidate(nums = [100, 105, 140, 210, 70]) == True
    assert candidate(nums = [11, 22, 33, 44, 55, 66]) == True
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153]) == True
    assert candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384]) == True
    assert candidate(nums = [1000, 500, 250, 125, 2000, 10000, 2500]) == True
    assert candidate(nums = [30, 45, 60, 75, 90, 105, 120]) == True
    assert candidate(nums = [12, 18, 24, 30, 36, 42]) == True
    assert candidate(nums = [25, 45, 65, 85, 105]) == True
    assert candidate(nums = [100, 200, 150, 300, 250]) == True
    assert candidate(nums = [14, 28, 42, 56, 70]) == True
    assert candidate(nums = [81, 135, 225, 315, 405, 525, 675]) == True
    assert candidate(nums = [121, 132, 220, 110, 55]) == True
