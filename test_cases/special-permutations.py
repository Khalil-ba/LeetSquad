# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [31, 62, 93, 124, 155]) == 0
    assert candidate(nums = [2, 3, 6]) == 2
    assert candidate(nums = [17, 34, 51, 68, 85]) == 0
    assert candidate(nums = [7, 14, 28, 56, 112]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 0
    assert candidate(nums = [5, 10, 20, 40]) == 24
    assert candidate(nums = [11, 22, 33, 44]) == 4
    assert candidate(nums = [1, 4, 3]) == 2
    assert candidate(nums = [2, 4, 8, 16]) == 24
    assert candidate(nums = [19, 38, 57, 76, 95]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 0
    assert candidate(nums = [3, 5, 15, 7]) == 0
    assert candidate(nums = [4, 2, 6, 3]) == 2
    assert candidate(nums = [7, 14, 28, 56, 112, 224]) == 720
    assert candidate(nums = [2, 4, 8, 16, 32]) == 120
    assert candidate(nums = [7, 14, 28, 21]) == 4
    assert candidate(nums = [13, 26, 39, 52, 65]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25]) == 0
    assert candidate(nums = [29, 58, 87, 116, 145]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55]) == 0
    assert candidate(nums = [23, 46, 69, 92, 115]) == 0
    assert candidate(nums = [3, 9, 27, 81]) == 24
    assert candidate(nums = [3, 5, 15, 75]) == 12
    assert candidate(nums = [4, 6, 12, 24]) == 12
    assert candidate(nums = [2, 4, 6, 8]) == 4
    assert candidate(nums = [2, 3, 6, 12, 18, 36]) == 336
    assert candidate(nums = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]) == 227020758
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126]) == 0
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182]) == 0
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238]) == 0
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112]) == 0
    assert candidate(nums = [2, 3, 5, 6, 10, 15, 30]) == 120
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 0
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56]) == 0
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238]) == 0
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969]) == 178290591
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154]) == 0
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126]) == 0
    assert candidate(nums = [5, 10, 20, 25, 50, 100, 125, 200, 250, 500]) == 136208
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == 0
    assert candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133]) == 0
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969]) == 178290591
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == 0
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35]) == 0
    assert candidate(nums = [12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304]) == 178290591
    assert candidate(nums = [2, 3, 6, 9, 12, 18, 24]) == 280
    assert candidate(nums = [1, 3, 9, 27, 81, 243]) == 720
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 0
    assert candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350]) == 0
    assert candidate(nums = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]) == 334499784
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 178290591
    assert candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 178290591
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == 3628800
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 0
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182]) == 0
    assert candidate(nums = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323]) == 178290591
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 0
    assert candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512]) == 40320
    assert candidate(nums = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125]) == 362880
    assert candidate(nums = [2, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78]) == 0
    assert candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42]) == 4
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == 0
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024]) == 40320
    assert candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 273, 294]) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 3628800
    assert candidate(nums = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240]) == 39916800
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135]) == 0
    assert candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 178290591
    assert candidate(nums = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480, 40960]) == 178290591
    assert candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322]) == 0
    assert candidate(nums = [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584, 7168, 14336, 28672, 57344]) == 178290591
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 0
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266, 285]) == 0
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == 3628800
    assert candidate(nums = [2, 3, 5, 6, 10, 15, 30, 60, 120, 240, 480, 720, 1440, 2880]) == 180479895
    assert candidate(nums = [5, 10, 20, 25, 50]) == 20
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154]) == 0
    assert candidate(nums = [2, 6, 18, 54, 162, 486, 1458, 4374, 13122, 39366, 118098, 354294, 1062882, 3188646]) == 178290591
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 178290591
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156]) == 0
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 0
    assert candidate(nums = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]) == 0
    assert candidate(nums = [29, 58, 87, 116, 145, 174, 203, 232, 261, 290, 319, 348, 377, 406]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176]) == 0
