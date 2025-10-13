# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 1, 1, 1]) == False
    assert candidate(nums = [1, 3, 5, 7, 9]) == False
    assert candidate(nums = [5, 7, 9, 11]) == False
    assert candidate(nums = [7, 11, 13, 14]) == False
    assert candidate(nums = [3, 6, 9, 12, 15]) == True
    assert candidate(nums = [11, 13, 15, 17]) == False
    assert candidate(nums = [1, 2, 3, 4, 5]) == True
    assert candidate(nums = [2, 4, 8, 16]) == True
    assert candidate(nums = [6, 12, 18, 24, 30]) == True
    assert candidate(nums = [5, 7, 11, 13]) == False
    assert candidate(nums = [9, 18, 27, 36]) == True
    assert candidate(nums = [2, 2, 2, 2]) == True
    assert candidate(nums = [8, 16, 32]) == True
    assert candidate(nums = [6, 12, 18, 24]) == True
    assert candidate(nums = [32, 64, 128, 256]) == True
    assert candidate(nums = [3, 5]) == False
    assert candidate(nums = [5, 10, 15, 20]) == True
    assert candidate(nums = [1, 2, 4, 8, 16, 32]) == True
    assert candidate(nums = [1, 2]) == False
    assert candidate(nums = [5, 7, 9, 11, 13]) == False
    assert candidate(nums = [7, 14, 21, 28]) == True
    assert candidate(nums = [10, 20, 30, 40]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == False
    assert candidate(nums = [10, 18, 22, 34, 50, 62]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == True
    assert candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]) == True
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == True
    assert candidate(nums = [32, 64, 128, 256]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == True
    assert candidate(nums = [7, 15, 23, 31, 39, 47, 55, 63, 71, 79]) == False
    assert candidate(nums = [31, 63, 127, 255, 511, 1023, 2047]) == False
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]) == False
    assert candidate(nums = [2, 3, 4, 6, 8, 10]) == True
    assert candidate(nums = [14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133]) == True
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == True
    assert candidate(nums = [32, 64, 128, 256, 512, 1024]) == True
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == True
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == True
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == True
    assert candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == True
    assert candidate(nums = [10, 20, 40, 80, 160, 320]) == True
    assert candidate(nums = [101, 102, 104, 108, 112]) == True
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == True
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == True
    assert candidate(nums = [3, 6, 9, 12, 15]) == True
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39]) == False
    assert candidate(nums = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240]) == True
    assert candidate(nums = [15, 23, 31, 39, 47, 55, 63, 71, 79, 87, 95, 103, 111, 119, 127]) == False
    assert candidate(nums = [7, 14, 21, 28, 35]) == True
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == True
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512]) == True
    assert candidate(nums = [2, 3, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]) == True
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72]) == True
    assert candidate(nums = [11, 14, 19, 22, 27, 30, 35, 38, 43]) == True
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == False
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == True
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == True
    assert candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]) == True
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == True
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]) == True
    assert candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == True
    assert candidate(nums = [10, 14, 18, 22, 26]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == True
    assert candidate(nums = [17, 33, 65, 129, 257]) == False
    assert candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024]) == True
    assert candidate(nums = [10, 12, 14, 16, 18, 20, 22]) == True
    assert candidate(nums = [31, 62, 124, 248, 496, 992, 1984, 3968, 7936, 15872, 31744, 63488, 126976, 253952, 507904]) == True
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == True
    assert candidate(nums = [101, 102, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192]) == True
    assert candidate(nums = [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78]) == True
    assert candidate(nums = [17, 34, 51, 68, 85]) == True
    assert candidate(nums = [63, 62, 61, 60, 59, 58, 57, 56, 55, 54]) == True
    assert candidate(nums = [17, 19, 21, 23, 25, 27, 29, 31]) == False
    assert candidate(nums = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == False
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == True
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == False
    assert candidate(nums = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16]) == True
    assert candidate(nums = [2, 3, 6, 12, 24, 48]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(nums = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == False
    assert candidate(nums = [10, 20, 30, 40, 50]) == True
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(nums = [4, 12, 20, 28, 36, 44, 52]) == True
    assert candidate(nums = [129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == True
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(nums = [33, 35, 37, 39, 41, 43, 45, 47, 49, 51]) == False
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42]) == True
    assert candidate(nums = [1, 3, 5, 7, 8, 9, 11]) == False
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]) == True
    assert candidate(nums = [101, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128]) == True
    assert candidate(nums = [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == True
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == True
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == True
    assert candidate(nums = [32, 64, 128, 256, 512]) == True
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152]) == True
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == False
    assert candidate(nums = [10, 12, 14, 16, 18, 20]) == True
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == True
    assert candidate(nums = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15]) == True
    assert candidate(nums = [101, 102, 104, 105, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126]) == True
    assert candidate(nums = [25, 30, 40, 50, 60, 70]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
    assert candidate(nums = [16, 32, 64, 128, 256]) == True
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == False
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == True
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61]) == False
    assert candidate(nums = [101, 104, 109, 112, 117, 120, 125, 128]) == True
    assert candidate(nums = [30, 42, 54, 66, 78, 90]) == True
    assert candidate(nums = [10, 12, 14, 16, 18, 20, 22, 24]) == True
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == True
    assert candidate(nums = [51, 53, 57, 61, 65, 69, 73, 77]) == False
    assert candidate(nums = [65, 130, 195, 260, 325, 390, 455, 520, 585, 650]) == True
