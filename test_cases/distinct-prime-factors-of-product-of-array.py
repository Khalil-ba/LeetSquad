# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [100, 200, 300, 400]) == 3
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [256, 512, 1024, 2048]) == 1
    assert candidate(nums = [1000, 500, 250, 125]) == 2
    assert candidate(nums = [2, 3, 5, 7, 11, 13]) == 6
    assert candidate(nums = [60, 120, 180, 240, 300]) == 3
    assert candidate(nums = [31, 37, 41, 43, 47, 53]) == 6
    assert candidate(nums = [2, 4, 3, 7, 10, 6]) == 4
    assert candidate(nums = [29, 31, 37, 41]) == 4
    assert candidate(nums = [1000, 500, 250, 125]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50]) == 3
    assert candidate(nums = [100, 200, 300]) == 3
    assert candidate(nums = [2, 4, 8, 16]) == 1
    assert candidate(nums = [997, 991, 983, 977, 971]) == 5
    assert candidate(nums = [3, 5, 7, 11, 13]) == 5
    assert candidate(nums = [60, 120, 180, 240]) == 3
    assert candidate(nums = [49, 49, 49, 49]) == 1
    assert candidate(nums = [999, 1000]) == 4
    assert candidate(nums = [7, 14, 21, 28, 35]) == 4
    assert candidate(nums = [31, 31, 31, 31, 31]) == 1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 10
    assert candidate(nums = [5, 10, 15, 20]) == 3
    assert candidate(nums = [3, 9, 27, 81]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [61, 67, 71, 73, 79, 83, 89, 97]) == 8
    assert candidate(nums = [15, 21, 27, 33, 39]) == 5
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 4
    assert candidate(nums = [17, 19, 23, 29, 31, 37, 41]) == 7
    assert candidate(nums = [1023, 2046, 3069, 4092, 5115]) == 5
    assert candidate(nums = [111, 222, 333, 444, 555]) == 4
    assert candidate(nums = [15, 21, 35, 55, 77, 105]) == 4
    assert candidate(nums = [221, 247, 299, 323, 377, 413]) == 7
    assert candidate(nums = [29, 29, 29, 29, 29, 29, 29, 29, 29, 29]) == 1
    assert candidate(nums = [1009, 1013, 1019, 1021, 1031]) == 5
    assert candidate(nums = [84, 90, 120, 140, 182]) == 5
    assert candidate(nums = [987, 1597, 2584, 4181, 6765]) == 12
    assert candidate(nums = [50, 75, 100, 125, 150]) == 3
    assert candidate(nums = [60, 105, 140, 210, 231]) == 5
    assert candidate(nums = [101, 103, 107, 109, 113, 127]) == 6
    assert candidate(nums = [210, 154, 90]) == 5
    assert candidate(nums = [29, 31, 37, 41, 43]) == 5
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]) == 20
    assert candidate(nums = [19, 23, 29, 31, 37, 41, 43, 47]) == 8
    assert candidate(nums = [123, 456, 789, 101112, 131415]) == 9
    assert candidate(nums = [36, 45, 60, 72, 84, 90]) == 4
    assert candidate(nums = [121, 143, 169, 187, 221]) == 3
    assert candidate(nums = [100, 200, 300, 400, 500]) == 3
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384]) == 1
    assert candidate(nums = [13195, 206772, 3249006, 5125130]) == 12
    assert candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 9
    assert candidate(nums = [500, 700, 900, 1100, 1300, 1500]) == 6
    assert candidate(nums = [2310, 30030, 510510, 9699690]) == 8
    assert candidate(nums = [123, 456, 789, 101112]) == 7
    assert candidate(nums = [121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 8
    assert candidate(nums = [60, 84, 90, 120, 180, 240]) == 4
    assert candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]) == 4
    assert candidate(nums = [30, 45, 60, 75, 90]) == 3
    assert candidate(nums = [29, 31, 37, 41, 43, 47]) == 6
    assert candidate(nums = [840, 945, 1260, 1575]) == 4
    assert candidate(nums = [98, 112, 147, 196, 294]) == 3
    assert candidate(nums = [961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975]) == 19
    assert candidate(nums = [231, 308, 396, 462]) == 4
    assert candidate(nums = [987, 654, 321, 876, 543, 210]) == 9
    assert candidate(nums = [231, 462, 693, 924, 1155]) == 5
    assert candidate(nums = [1024, 512, 256, 128]) == 1
    assert candidate(nums = [8, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102]) == 7
    assert candidate(nums = [49, 64, 81, 100, 121, 144, 169, 196, 225]) == 6
    assert candidate(nums = [128, 256, 512, 1024, 2048]) == 1
    assert candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53]) == 10
    assert candidate(nums = [30, 42, 60, 70, 105]) == 4
    assert candidate(nums = [19, 31, 37, 41, 43, 47, 53, 59]) == 8
    assert candidate(nums = [25, 49, 121, 169, 289, 361]) == 6
    assert candidate(nums = [729, 512, 343, 243, 125]) == 4
    assert candidate(nums = [1024, 2048, 4096, 8192]) == 1
    assert candidate(nums = [169, 441, 729, 1089, 1369]) == 5
    assert candidate(nums = [15, 21, 33, 55, 77]) == 4
    assert candidate(nums = [997, 991, 983, 977, 971, 967, 953, 947, 941, 937]) == 10
    assert candidate(nums = [1000, 500, 250, 125, 62, 31]) == 3
    assert candidate(nums = [171, 195, 221, 255, 285, 323]) == 5
    assert candidate(nums = [18, 30, 45, 60, 75]) == 3
    assert candidate(nums = [81, 125, 243, 343, 625]) == 3
    assert candidate(nums = [840, 924, 1008, 1092, 1176, 1260]) == 6
    assert candidate(nums = [37, 41, 43, 47, 53, 59, 61, 67, 71, 73]) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600]) == 3
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 25
    assert candidate(nums = [210, 231, 273, 308, 330, 364]) == 6
    assert candidate(nums = [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 8
    assert candidate(nums = [60, 105, 140, 210, 300]) == 4
    assert candidate(nums = [97, 101, 103, 107, 109, 113]) == 6
    assert candidate(nums = [81, 243, 729, 2187, 6561]) == 1
    assert candidate(nums = [2310, 5005, 7735, 1155]) == 7
    assert candidate(nums = [840, 1260, 720, 5040]) == 4
    assert candidate(nums = [65, 130, 260, 520, 1040, 2080]) == 3
    assert candidate(nums = [256, 512, 1024, 2048, 4096]) == 1
    assert candidate(nums = [83, 89, 97, 101, 103, 107, 109, 113, 127, 131]) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700]) == 4
    assert candidate(nums = [123, 456, 789, 1011, 1213]) == 7
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31]) == 8
    assert candidate(nums = [8192, 16384, 32768, 65536]) == 1
    assert candidate(nums = [3125, 625, 125, 25]) == 1
    assert candidate(nums = [256, 512, 1024, 2048, 4096, 8192]) == 1
    assert candidate(nums = [97, 98, 99, 100, 101]) == 7
    assert candidate(nums = [89, 107, 127, 137, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]) == 20
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 5
    assert candidate(nums = [504, 1008, 2016, 4032]) == 3
    assert candidate(nums = [1023, 500, 729]) == 5
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 5, 5, 5, 7, 7, 7, 11, 11, 11]) == 5
    assert candidate(nums = [60, 84, 90, 120, 210]) == 4
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 10
    assert candidate(nums = [49, 64, 81, 100, 121, 144]) == 5
    assert candidate(nums = [997, 991, 983, 977, 971]) == 5
    assert candidate(nums = [30030, 30030, 30030, 30030, 30030]) == 6
    assert candidate(nums = [12, 15, 21, 28, 45]) == 4
    assert candidate(nums = [55, 77, 91, 1001, 1365]) == 5
    assert candidate(nums = [625, 1250, 2500, 5000, 10000]) == 2
