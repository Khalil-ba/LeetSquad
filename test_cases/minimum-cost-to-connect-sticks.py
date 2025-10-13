# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(sticks = [1, 8, 3, 5]) == 30
    assert candidate(sticks = [10, 1, 2, 8, 5]) == 53
    assert candidate(sticks = [5, 4, 3, 2, 1]) == 33
    assert candidate(sticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 173
    assert candidate(sticks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 340
    assert candidate(sticks = [1, 1, 1, 1, 1]) == 12
    assert candidate(sticks = [100, 200, 300]) == 900
    assert candidate(sticks = [2, 4, 3]) == 14
    assert candidate(sticks = [5]) == 0
    assert candidate(sticks = [10, 20, 30, 40, 50]) == 330
    assert candidate(sticks = [1]) == 0
    assert candidate(sticks = [1, 2147483647]) == 2147483648
    assert candidate(sticks = [10, 20, 30, 40]) == 190
    assert candidate(sticks = [100, 200, 300, 400]) == 1900
    assert candidate(sticks = [1, 1, 2, 2, 3, 3]) == 30
    assert candidate(sticks = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 339835
    assert candidate(sticks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 824
    assert candidate(sticks = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 629
    assert candidate(sticks = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 11, 12, 14, 13, 15, 16]) == 516
    assert candidate(sticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 444
    assert candidate(sticks = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 4080
    assert candidate(sticks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 173
    assert candidate(sticks = [100, 1, 10, 1000, 10000]) == 12344
    assert candidate(sticks = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 143
    assert candidate(sticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 170
    assert candidate(sticks = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 135
    assert candidate(sticks = [10, 20, 30, 40, 50, 60]) == 510
    assert candidate(sticks = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1999
    assert candidate(sticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 4440
    assert candidate(sticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 440
    assert candidate(sticks = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 16368
    assert candidate(sticks = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 17300
    assert candidate(sticks = [9999, 1, 2, 3, 4]) == 10028
    assert candidate(sticks = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 173000
    assert candidate(sticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1730
    assert candidate(sticks = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5]) == 3493
    assert candidate(sticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 173
    assert candidate(sticks = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == 4755
    assert candidate(sticks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 104
    assert candidate(sticks = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990]) == 339801
    assert candidate(sticks = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 864
    assert candidate(sticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 8640
    assert candidate(sticks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 156
    assert candidate(sticks = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 2035
    assert candidate(sticks = [2, 2, 3, 3, 5, 5, 7, 7, 11, 11, 13, 13, 17, 17, 19, 19]) == 574
    assert candidate(sticks = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 34000
    assert candidate(sticks = [2, 5, 7, 10, 12, 15]) == 123
    assert candidate(sticks = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 714
    assert candidate(sticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1730
    assert candidate(sticks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 44400
    assert candidate(sticks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 1078
    assert candidate(sticks = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981, 9980, 9979, 9978, 9977, 9976, 9975, 9974, 9973, 9972, 9971, 9970]) == 1537675
    assert candidate(sticks = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 96
    assert candidate(sticks = [100, 200, 300, 400, 500]) == 3300
    assert candidate(sticks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 17300
    assert candidate(sticks = [5, 8, 12, 19, 22, 27, 33, 39, 41, 50, 61, 75, 89, 98, 100]) == 2424
    assert candidate(sticks = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 176
    assert candidate(sticks = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 1211
    assert candidate(sticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 696
    assert candidate(sticks = [45, 23, 89, 34, 67, 23, 56, 78, 90, 12]) == 1633
    assert candidate(sticks = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 173
    assert candidate(sticks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 295
    assert candidate(sticks = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 888
    assert candidate(sticks = [7, 8, 9, 10, 11, 12, 13, 14, 15]) == 312
    assert candidate(sticks = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 33801
    assert candidate(sticks = [3, 6, 8, 9, 10, 11, 12, 15, 17, 19, 21]) == 438
    assert candidate(sticks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 102
    assert candidate(sticks = [5, 4, 3, 2, 1]) == 33
    assert candidate(sticks = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 17300
    assert candidate(sticks = [1, 10000, 2, 9999, 3, 9998, 4, 9997, 5, 9996]) == 130049
    assert candidate(sticks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 88
    assert candidate(sticks = [1000, 100, 10, 1, 10000]) == 12344
    assert candidate(sticks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 17300
    assert candidate(sticks = [10, 20, 30, 40, 50]) == 330
    assert candidate(sticks = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 65518
    assert candidate(sticks = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 166
    assert candidate(sticks = [10, 15, 20, 25, 30, 35, 40]) == 475
    assert candidate(sticks = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 1211
    assert candidate(sticks = [9, 4, 4, 8, 9, 9, 0, 0, 1, 1]) == 126
    assert candidate(sticks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 44400
    assert candidate(sticks = [5, 9, 12, 13, 16, 18, 20, 22, 25, 28]) == 543
    assert candidate(sticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 444
    assert candidate(sticks = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == 46324
    assert candidate(sticks = [2, 5, 8, 9, 10]) == 75
