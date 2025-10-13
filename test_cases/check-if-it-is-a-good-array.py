# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [7, 13, 19]) == True
    assert candidate(nums = [100, 200, 300, 400]) == False
    assert candidate(nums = [7, 13, 19, 29]) == True
    assert candidate(nums = [29, 6, 10]) == True
    assert candidate(nums = [7, 14, 21, 35]) == False
    assert candidate(nums = [2, 4, 6, 8, 10]) == False
    assert candidate(nums = [7, 14, 21, 28]) == False
    assert candidate(nums = [2, 3, 5]) == True
    assert candidate(nums = [1]) == True
    assert candidate(nums = [1000000000]) == False
    assert candidate(nums = [11, 22, 33, 44]) == False
    assert candidate(nums = [3, 6]) == False
    assert candidate(nums = [12, 5, 7, 23]) == True
    assert candidate(nums = [1000000000, 1000000000, 1000000000]) == False
    assert candidate(nums = [100, 200, 300]) == False
    assert candidate(nums = [5, 5, 5, 5]) == False
    assert candidate(nums = [1, 2, 3, 4, 5]) == True
    assert candidate(nums = [3, 5, 7, 11, 13]) == True
    assert candidate(nums = [17, 19, 23, 29]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == False
    assert candidate(nums = [8, 12, 16, 20]) == False
    assert candidate(nums = [7, 14, 21, 28, 35]) == False
    assert candidate(nums = [5, 10, 15]) == False
    assert candidate(nums = [5, 10, 15, 20, 25]) == False
    assert candidate(nums = [11, 22, 33, 44, 55]) == False
    assert candidate(nums = [1, 2, 3]) == True
    assert candidate(nums = [11, 13, 17, 19]) == True
    assert candidate(nums = [5]) == False
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1]) == True
    assert candidate(nums = [123456789, 987654321, 246813579, 864204864]) == False
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == False
    assert candidate(nums = [97, 101, 103, 107, 109, 113, 127, 131, 137, 139]) == True
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == False
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == False
    assert candidate(nums = [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]) == True
    assert candidate(nums = [13195, 26390, 39585, 52780, 65975, 79170, 92365, 105560, 118755, 131950]) == False
    assert candidate(nums = [13, 17, 19, 23, 29]) == True
    assert candidate(nums = [1000000007, 1000000009, 1000000021, 1000000033, 1000000037, 1000000087, 1000000093]) == True
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139]) == True
    assert candidate(nums = [111111111, 222222222, 333333333, 444444444]) == False
    assert candidate(nums = [4, 9, 25, 49, 121, 169, 289, 361]) == True
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == False
    assert candidate(nums = [9973, 9967, 9959, 9949, 9941, 9931, 9929, 9923, 9919, 9907]) == True
    assert candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]) == False
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == False
    assert candidate(nums = [13, 17, 19, 23, 29]) == True
    assert candidate(nums = [131, 137, 139, 149, 151, 157, 163, 167, 173, 179]) == True
    assert candidate(nums = [8, 14, 21, 35, 56]) == True
    assert candidate(nums = [999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == False
    assert candidate(nums = [17, 23, 19, 5, 3, 2]) == True
    assert candidate(nums = [7, 21, 35, 56, 112, 140]) == False
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == False
    assert candidate(nums = [13, 17, 19, 23, 29, 31]) == True
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == True
    assert candidate(nums = [8, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72]) == False
    assert candidate(nums = [1000000007, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]) == True
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333]) == False
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == False
    assert candidate(nums = [41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == True
    assert candidate(nums = [1000000007, 1000000009, 1000000011]) == True
    assert candidate(nums = [101, 103, 107, 109, 113]) == True
    assert candidate(nums = [42, 105, 210, 35]) == False
    assert candidate(nums = [1000000007, 1000000009, 1000000021]) == True
    assert candidate(nums = [49, 77, 91, 119, 133, 161, 187, 203, 221, 247, 259, 287, 301, 329, 343, 371, 399, 413, 437, 469, 497, 511, 539, 553, 581]) == True
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [3, 5, 8, 11, 19]) == True
    assert candidate(nums = [555, 1110, 1665, 2220, 2775]) == False
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == True
    assert candidate(nums = [999999999, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]) == True
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000]) == False
    assert candidate(nums = [15, 21, 35, 525, 630]) == True
    assert candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]) == False
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == True
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == False
    assert candidate(nums = [17, 23, 41, 59]) == True
    assert candidate(nums = [1000000000, 999999999, 1, 2]) == True
    assert candidate(nums = [8, 12, 18, 24, 30, 36, 42, 48, 54]) == False
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == False
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29]) == True
    assert candidate(nums = [1000000001, 1000000003, 1000000007, 1000000009]) == True
    assert candidate(nums = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == False
    assert candidate(nums = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == True
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == False
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == True
    assert candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == False
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == True
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]) == False
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]) == False
    assert candidate(nums = [123, 456, 789, 101, 137]) == True
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == False
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == False
    assert candidate(nums = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == True
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == False
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]) == True
    assert candidate(nums = [13, 17, 19, 23, 29, 31]) == True
    assert candidate(nums = [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == True
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == True
    assert candidate(nums = [35, 105, 175, 245, 315]) == False
    assert candidate(nums = [97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]) == True
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152]) == False
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == True
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == True
    assert candidate(nums = [17, 29, 41, 53, 67, 83]) == True
    assert candidate(nums = [3, 9, 27, 81, 243]) == False
    assert candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200]) == False
    assert candidate(nums = [1000000001, 1000000002, 1000000003, 1000000004]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == True
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == False
    assert candidate(nums = [31, 37, 41, 43, 47, 53, 59]) == True
    assert candidate(nums = [123456789, 987654321, 234567891, 345678912]) == False
    assert candidate(nums = [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]) == True
    assert candidate(nums = [111111111, 222222222, 333333333, 444444444, 555555555]) == False
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561]) == False
    assert candidate(nums = [500000000, 500000001, 500000002, 500000003, 500000004, 500000005, 500000006, 500000007, 500000008, 500000009]) == True
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == True
    assert candidate(nums = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020]) == True
    assert candidate(nums = [41, 43, 47, 53, 59, 61]) == True
    assert candidate(nums = [101, 202, 303, 404, 505]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191]) == True
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]) == False
    assert candidate(nums = [1000000007, 2, 3, 5, 7]) == True
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == True
    assert candidate(nums = [333333333, 666666667, 333333333, 666666667, 333333333, 666666667, 333333333, 666666667, 333333333, 666666667]) == True
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == True
    assert candidate(nums = [97, 1, 101, 1, 103, 1, 107, 1, 109, 1]) == True
    assert candidate(nums = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == True
    assert candidate(nums = [71, 113, 151, 199, 239, 283, 317, 359, 401, 443]) == True
    assert candidate(nums = [1000000007, 1000000009, 1000000021, 1000000033]) == True
    assert candidate(nums = [17, 31, 41, 43, 59, 61]) == True
    assert candidate(nums = [101, 103, 107, 109, 113]) == True
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == False
    assert candidate(nums = [15, 21, 25, 35, 45]) == True
    assert candidate(nums = [100, 101, 102, 103, 104]) == True
    assert candidate(nums = [3, 5, 7, 11, 13, 17]) == True
