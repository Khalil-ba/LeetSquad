# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [42, 56, 14]) == 14
    assert candidate(nums = [1, 1000]) == 1
    assert candidate(nums = [17, 23, 37, 41]) == 1
    assert candidate(nums = [3, 3]) == 3
    assert candidate(nums = [7, 5, 6, 8, 3]) == 1
    assert candidate(nums = [1000, 1000]) == 1000
    assert candidate(nums = [48, 18, 30]) == 6
    assert candidate(nums = [10, 20, 30, 40, 50]) == 10
    assert candidate(nums = [100, 200, 300, 400, 500]) == 100
    assert candidate(nums = [17, 23, 19, 29, 31]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5]) == 5
    assert candidate(nums = [1000, 1]) == 1
    assert candidate(nums = [48, 18]) == 6
    assert candidate(nums = [2, 5, 6, 9, 10]) == 2
    assert candidate(nums = [48, 180, 120, 240]) == 48
    assert candidate(nums = [54, 24, 36]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [56, 98, 140, 224, 336]) == 56
    assert candidate(nums = [81, 27, 9, 3, 1]) == 1
    assert candidate(nums = [22, 44, 66, 88, 110, 132, 154]) == 22
    assert candidate(nums = [27, 54, 81, 108, 135, 162, 189]) == 27
    assert candidate(nums = [1024, 512, 256, 128, 64]) == 64
    assert candidate(nums = [999, 1000]) == 1
    assert candidate(nums = [4096, 2048, 1024, 512, 256, 128]) == 128
    assert candidate(nums = [84, 60, 48, 36, 24]) == 12
    assert candidate(nums = [81, 27, 54, 162, 81]) == 27
    assert candidate(nums = [29, 29, 29, 29, 29, 29]) == 29
    assert candidate(nums = [83, 166, 332, 664, 996]) == 83
    assert candidate(nums = [123456, 234567, 345678, 456789, 567891, 678912, 789123, 891234, 912345]) == 3
    assert candidate(nums = [999, 333, 666, 111, 222]) == 111
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136]) == 17
    assert candidate(nums = [1000, 1, 500, 250, 750, 200]) == 1
    assert candidate(nums = [60, 48, 36, 24, 12, 6, 3, 1]) == 1
    assert candidate(nums = [441, 49, 147, 343, 735]) == 49
    assert candidate(nums = [1, 1000, 2, 999, 3, 998]) == 1
    assert candidate(nums = [1000, 10, 50, 250, 500]) == 10
    assert candidate(nums = [44, 55, 66, 77, 88, 99]) == 11
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 15
    assert candidate(nums = [999, 998, 997, 996, 995]) == 1
    assert candidate(nums = [100, 200, 300, 400, 500]) == 100
    assert candidate(nums = [31, 62, 93, 124, 155]) == 31
    assert candidate(nums = [77, 143, 209, 286, 187]) == 11
    assert candidate(nums = [42, 42, 42, 42, 42]) == 42
    assert candidate(nums = [98, 49, 147, 245, 343, 441, 539]) == 49
    assert candidate(nums = [17, 23, 29, 31, 37]) == 1
    assert candidate(nums = [13, 13, 13, 13, 13, 13, 13]) == 13
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]) == 13
    assert candidate(nums = [999, 888, 777, 666, 555]) == 111
    assert candidate(nums = [1000, 750, 500, 250]) == 250
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260]) == 13
    assert candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111]) == 111111
    assert candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876]) == 2
    assert candidate(nums = [123, 246, 369, 492, 615, 738, 861, 984, 1107, 1230, 1353, 1476, 1599, 1722, 1845, 1968, 2091, 2214, 2337, 2460]) == 123
    assert candidate(nums = [54, 24, 36, 48, 60]) == 12
    assert candidate(nums = [1000, 1000, 1000, 1000]) == 1000
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 2
    assert candidate(nums = [999, 333, 111, 37, 1]) == 1
    assert candidate(nums = [231, 105, 77, 49, 33, 11, 7]) == 7
    assert candidate(nums = [77, 49, 14, 21, 28]) == 7
    assert candidate(nums = [997, 991, 983, 977, 971, 967, 953, 941, 929, 919, 907, 887, 883]) == 1
    assert candidate(nums = [50, 75, 100, 125, 150, 175, 200]) == 50
    assert candidate(nums = [123456, 234567, 345678, 456789, 567890]) == 2
    assert candidate(nums = [210, 231, 273, 308, 357, 399]) == 21
    assert candidate(nums = [17, 34, 51, 68, 85]) == 17
    assert candidate(nums = [1, 1000]) == 1
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170]) == 17
    assert candidate(nums = [100, 150, 200, 250, 300]) == 100
    assert candidate(nums = [650, 520, 390, 780, 260]) == 260
    assert candidate(nums = [100, 200, 300, 400, 500, 600]) == 100
    assert candidate(nums = [17, 19, 23, 29, 31]) == 1
    assert candidate(nums = [123456, 987654, 111111, 222222, 333333]) == 3
    assert candidate(nums = [123, 456, 789, 987, 654]) == 3
    assert candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264]) == 33
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [101010, 202020, 303030, 404040, 505050, 606060, 707070, 808080, 909090]) == 101010
    assert candidate(nums = [13, 26, 39, 52, 65]) == 13
    assert candidate(nums = [12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 12
    assert candidate(nums = [17, 34, 51, 68, 85, 102]) == 17
    assert candidate(nums = [1, 1000, 2, 500, 4]) == 1
    assert candidate(nums = [29, 58, 87, 116, 145, 174, 203, 232, 261, 290, 319, 348, 377, 406, 435, 464, 493, 522, 551, 580]) == 29
    assert candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == 1
    assert candidate(nums = [256, 512, 1024, 2048, 4096]) == 256
    assert candidate(nums = [77, 49, 14, 28, 35, 56]) == 7
    assert candidate(nums = [123, 456, 789, 1011, 1213]) == 1
    assert candidate(nums = [500, 500, 500, 500, 500, 500]) == 500
    assert candidate(nums = [24, 36, 48, 60, 72, 84, 96]) == 24
    assert candidate(nums = [1000, 750, 500, 250, 125, 62, 31]) == 1
    assert candidate(nums = [999, 888, 777, 666, 555, 444, 333, 222, 111]) == 111
    assert candidate(nums = [41, 82, 123, 164, 205, 246, 287, 328]) == 41
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006]) == 1001
    assert candidate(nums = [1, 1000, 500, 250, 125, 62, 31, 15]) == 1
    assert candidate(nums = [84, 112, 168, 224, 280]) == 28
    assert candidate(nums = [56, 98, 140, 182, 224]) == 56
    assert candidate(nums = [840, 1764, 4620, 10920]) == 840
    assert candidate(nums = [77, 154, 231, 308, 385, 462, 539, 616]) == 77
    assert candidate(nums = [60, 120, 180, 240, 300, 360]) == 60
    assert candidate(nums = [840, 756, 630, 504, 420]) == 420
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108]) == 12
    assert candidate(nums = [49, 63, 28, 91, 35]) == 7
    assert candidate(nums = [1000, 500, 250, 125, 62]) == 2
    assert candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums = [27, 81, 54, 162, 243]) == 27
    assert candidate(nums = [101, 202, 303, 404, 505]) == 101
    assert candidate(nums = [27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441]) == 27
    assert candidate(nums = [29, 58, 87, 116, 145, 174, 203]) == 29
    assert candidate(nums = [1024, 2048, 3072, 4096, 5120]) == 1024
    assert candidate(nums = [24, 36, 48, 60, 72, 84]) == 12
    assert candidate(nums = [840, 756, 672, 588, 504, 420, 336, 252, 168, 84]) == 84
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909]) == 101
    assert candidate(nums = [997, 991, 983, 977, 971]) == 1
    assert candidate(nums = [8317, 16634, 24951, 33268, 41585, 49902, 58219]) == 8317
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == 101
    assert candidate(nums = [101, 103, 107, 109, 113, 127, 131, 137]) == 1
    assert candidate(nums = [987, 654, 321, 123, 456, 789]) == 3
    assert candidate(nums = [101, 103, 107, 109, 113]) == 1
    assert candidate(nums = [23, 47, 17, 53, 31, 19, 89, 73]) == 1
