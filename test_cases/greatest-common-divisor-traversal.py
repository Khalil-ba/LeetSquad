# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [2, 3, 6]) == True
    assert candidate(nums = [100, 200, 300, 400]) == True
    assert candidate(nums = [1, 1, 1]) == False
    assert candidate(nums = [1, 1, 1, 1]) == False
    assert candidate(nums = [7, 14, 21, 35]) == True
    assert candidate(nums = [30, 15, 10, 5]) == True
    assert candidate(nums = [2, 4, 6, 8, 10]) == True
    assert candidate(nums = [2, 6, 8, 12, 18, 24]) == True
    assert candidate(nums = [3, 9, 5]) == False
    assert candidate(nums = [7, 11, 13, 17]) == False
    assert candidate(nums = [1]) == True
    assert candidate(nums = [2, 5, 7, 11, 13]) == False
    assert candidate(nums = [1, 2, 3, 4, 5]) == False
    assert candidate(nums = [2, 4, 8, 16]) == True
    assert candidate(nums = [13, 17, 19, 23, 29]) == False
    assert candidate(nums = [60, 120, 180, 240]) == True
    assert candidate(nums = [10, 15, 20, 25]) == True
    assert candidate(nums = [4, 3, 12, 8]) == True
    assert candidate(nums = [2, 2, 2, 2]) == True
    assert candidate(nums = [7, 11, 13, 17, 19]) == False
    assert candidate(nums = [60, 30, 20, 10]) == True
    assert candidate(nums = [100000]) == True
    assert candidate(nums = [5, 10, 15, 20, 25]) == True
    assert candidate(nums = [5, 10, 15, 20]) == True
    assert candidate(nums = [11, 22, 33, 44, 55]) == True
    assert candidate(nums = [3, 5, 7, 11, 13, 17]) == False
    assert candidate(nums = [30, 42, 70, 105]) == True
    assert candidate(nums = [7, 14, 28, 35]) == True
    assert candidate(nums = [100000, 100000, 100000, 100000]) == True
    assert candidate(nums = [2, 2, 3, 3, 5, 5, 7, 7, 11, 11, 13, 13, 17, 17, 19, 19, 23, 23, 29, 29]) == False
    assert candidate(nums = [30, 42, 70, 105, 210]) == True
    assert candidate(nums = [30, 42, 56, 70, 84, 98, 112, 126, 140, 154]) == True
    assert candidate(nums = [220, 330, 440, 550, 660, 770, 880, 990, 1100, 1210]) == True
    assert candidate(nums = [143, 169, 187, 221, 247, 299, 323, 341, 377, 391, 413, 437, 451, 473, 517, 551, 583, 611, 629, 667]) == False
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == True
    assert candidate(nums = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == False
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == True
    assert candidate(nums = [49, 147, 245, 343, 7203]) == True
    assert candidate(nums = [30, 45, 60, 75, 90, 105]) == True
    assert candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == True
    assert candidate(nums = [20, 25, 40, 50, 100]) == True
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == True
    assert candidate(nums = [44, 55, 66, 77, 88, 99, 110, 121]) == True
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == True
    assert candidate(nums = [2048, 4096, 6144, 8192, 10240, 12288, 14336, 16384, 18432, 20480]) == True
    assert candidate(nums = [121, 143, 169, 187, 209, 221, 247, 253]) == True
    assert candidate(nums = [101, 103, 107, 109, 113, 127]) == False
    assert candidate(nums = [49, 98, 147, 196, 245, 294, 343, 392, 441, 490]) == True
    assert candidate(nums = [105, 210, 315, 420, 525, 630, 735]) == True
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400]) == True
    assert candidate(nums = [10, 15, 21, 35, 70, 105]) == True
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197]) == False
    assert candidate(nums = [30, 42, 70, 105]) == True
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == False
    assert candidate(nums = [2, 3, 5, 6, 10, 15, 30]) == True
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == True
    assert candidate(nums = [840, 1680, 2520, 3360, 4200]) == True
    assert candidate(nums = [42, 56, 70, 84, 98, 112, 126, 140]) == True
    assert candidate(nums = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == False
    assert candidate(nums = [100, 200, 300, 400, 500]) == True
    assert candidate(nums = [81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841, 961, 1089]) == False
    assert candidate(nums = [6, 10, 15, 21, 26, 33, 35, 39, 42, 55]) == True
    assert candidate(nums = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31, 33]) == False
    assert candidate(nums = [83160, 166320, 249480, 332640, 415800, 498960, 582120, 665280, 748440, 831600]) == False
    assert candidate(nums = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126]) == True
    assert candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(nums = [21, 35, 70, 105]) == True
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == False
    assert candidate(nums = [14, 21, 28, 35, 42, 49, 56]) == True
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == False
    assert candidate(nums = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165]) == True
    assert candidate(nums = [30, 45, 60, 75, 90]) == True
    assert candidate(nums = [99, 100, 101, 102, 103, 104, 105]) == False
    assert candidate(nums = [84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672]) == True
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131]) == False
    assert candidate(nums = [6, 10, 15, 21, 25, 35]) == True
    assert candidate(nums = [49, 98, 147, 196, 245, 294]) == True
    assert candidate(nums = [12345, 54321, 67890, 98765, 123456, 234567, 345678]) == False
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024]) == True
    assert candidate(nums = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == True
    assert candidate(nums = [4, 6, 8, 12, 18, 24, 36, 48, 72, 144]) == True
    assert candidate(nums = [10001, 10003, 10007, 10009, 10013, 10021, 10031, 10037, 10039, 10061]) == False
    assert candidate(nums = [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009]) == False
    assert candidate(nums = [72, 108, 144, 180, 216, 252, 288, 324, 360, 396, 432, 468, 504, 540, 576]) == True
    assert candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192]) == True
    assert candidate(nums = [33, 55, 77, 99, 121, 143, 165, 187, 209, 231]) == True
    assert candidate(nums = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == False
    assert candidate(nums = [84, 90, 120, 140, 210]) == True
    assert candidate(nums = [9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147]) == False
    assert candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120]) == True
    assert candidate(nums = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == True
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]) == False
    assert candidate(nums = [6, 10, 15, 30, 60, 120]) == True
    assert candidate(nums = [210, 330, 420, 550, 660, 770, 880, 990, 1100, 1210]) == True
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == False
    assert candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == True
    assert candidate(nums = [210, 231, 273, 308, 330, 364]) == True
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [49, 441, 729, 1029, 1323, 1681, 2079, 2521, 2997, 3529, 4041, 4561]) == False
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == False
    assert candidate(nums = [15, 25, 35, 45, 55]) == True
    assert candidate(nums = [2310, 2730, 2310, 2730, 2310, 2730, 2310, 2730, 2310, 2730]) == True
    assert candidate(nums = [18, 24, 30, 36, 42, 48, 54, 60]) == True
    assert candidate(nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]) == False
    assert candidate(nums = [15, 21, 35, 105]) == True
    assert candidate(nums = [42, 77, 105, 140, 175, 210, 245, 280, 315, 350]) == True
    assert candidate(nums = [21, 35, 49, 63, 105]) == True
    assert candidate(nums = [48, 72, 108, 144, 180, 216]) == True
    assert candidate(nums = [18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102]) == True
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
    assert candidate(nums = [84, 126, 168, 210, 252, 294, 336, 378, 420, 462]) == True
    assert candidate(nums = [210, 420, 630, 840, 1050, 1260, 1470, 1680, 1890, 2100, 2310, 2520, 2730, 2940, 3150, 3360, 3570, 3780, 3990, 4200]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(nums = [36, 48, 60, 72, 84, 96, 108, 120, 132, 144]) == True
    assert candidate(nums = [210, 154, 385, 770]) == True
    assert candidate(nums = [315, 630, 945, 1260, 1575, 1890, 2205, 2520, 2835, 3150]) == True
    assert candidate(nums = [44, 88, 132, 176, 220]) == True
    assert candidate(nums = [12, 15, 20, 25, 30, 35, 40, 45, 50, 60]) == True
    assert candidate(nums = [1, 1, 1, 1, 1]) == False
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == True
    assert candidate(nums = [9, 27, 81, 243, 729, 2187, 6561, 19683]) == True
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125]) == True
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173]) == False
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40]) == True
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == False
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == True
    assert candidate(nums = [6, 15, 10, 30, 21, 42, 70, 105, 140, 210]) == True
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == True
    assert candidate(nums = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]) == True
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19]) == False
