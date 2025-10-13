# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(skill = [1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 4000
    assert candidate(skill = [1, 1, 2, 2, 3, 3, 4, 4]) == 20
    assert candidate(skill = [1, 1, 2, 3]) == -1
    assert candidate(skill = [1, 2, 3, 4, 5, 6, 7, 8]) == 60
    assert candidate(skill = [5, 5, 5, 5, 5, 5]) == 75
    assert candidate(skill = [15, 15, 15, 15, 15, 15, 15, 15]) == 900
    assert candidate(skill = [3, 4]) == 12
    assert candidate(skill = [2, 3, 3, 2, 2, 3]) == 18
    assert candidate(skill = [4, 4, 4, 4]) == 32
    assert candidate(skill = [3, 2, 5, 1, 3, 4]) == 22
    assert candidate(skill = [10, 10, 10, 10]) == 200
    assert candidate(skill = [1000, 1000, 1, 1, 2, 2]) == -1
    assert candidate(skill = [1, 2, 3, 4, 5, 6]) == 28
    assert candidate(skill = [1, 2, 3, 3, 2, 1]) == 10
    assert candidate(skill = [1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 4000
    assert candidate(skill = [10, 20, 30, 40, 50, 60]) == 2800
    assert candidate(skill = [500, 500, 500, 500, 500, 500, 500, 500]) == 1000000
    assert candidate(skill = [1, 3, 5, 7, 9, 11]) == 73
    assert candidate(skill = [1000, 1, 999, 2, 500, 501]) == 253498
    assert candidate(skill = [500, 500, 1, 999, 2, 998, 3, 997]) == 255986
    assert candidate(skill = [1, 2, 3, 6, 4, 5]) == 28
    assert candidate(skill = [250, 750, 500, 500, 750, 250, 500, 500]) == 875000
    assert candidate(skill = [1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(skill = [1, 1000, 500, 500, 250, 750, 100, 900]) == -1
    assert candidate(skill = [100, 100, 200, 200, 300, 300, 400, 400, 500, 500]) == 350000
    assert candidate(skill = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995, 6, 994, 7, 993, 8, 992, 9, 991, 10, 990]) == 54615
    assert candidate(skill = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 182
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 18200
    assert candidate(skill = [1, 999, 3, 997, 5, 995, 7, 993, 9, 991, 11, 989, 13, 987, 15, 985]) == 63320
    assert candidate(skill = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 512
    assert candidate(skill = [200, 300, 200, 300, 200, 300, 200, 300]) == 240000
    assert candidate(skill = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 728
    assert candidate(skill = [333, 667, 333, 667, 333, 667, 333, 667, 333, 667, 333, 667, 333, 667, 333, 667]) == 1776888
    assert candidate(skill = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(skill = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 252
    assert candidate(skill = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == 14960
    assert candidate(skill = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5, 994, 6]) == 20909
    assert candidate(skill = [10, 1, 5, 15, 7, 3, 9, 11]) == -1
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 11000
    assert candidate(skill = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]) == 1512
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 40800
    assert candidate(skill = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 216
    assert candidate(skill = [2, 8, 3, 7, 4, 6, 5, 5]) == 86
    assert candidate(skill = [333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348]) == 927352
    assert candidate(skill = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 182
    assert candidate(skill = [23, 42, 31, 57, 5, 19, 6, 49, 12, 35, 29, 10, 50, 40, 21, 33]) == -1
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 70, 80]) == 6000
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60]) == 5600
    assert candidate(skill = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 5000
    assert candidate(skill = [8, 1, 8, 1, 8, 1, 8, 1]) == 32
    assert candidate(skill = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200]) == -1
    assert candidate(skill = [250, 250, 500, 500, 750, 750, 1000, 1000]) == 1250000
    assert candidate(skill = [300, 700, 200, 800, 100, 900, 400, 600, 500, 500]) == 950000
    assert candidate(skill = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 1250000
    assert candidate(skill = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 200
    assert candidate(skill = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 441
    assert candidate(skill = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 20000
    assert candidate(skill = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 6000
    assert candidate(skill = [123, 321, 213, 312, 132, 231, 213, 132]) == -1
    assert candidate(skill = [6, 3, 9, 2, 8, 4, 5, 7, 1, 10, 11, 12, 13, 14, 15, 16]) == 408
    assert candidate(skill = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 3080
    assert candidate(skill = [8, 6, 4, 2, 10, 12, 14, 16, 18, 20]) == 440
    assert candidate(skill = [1, 1000, 2, 999, 3, 998, 4, 997]) == 9980
    assert candidate(skill = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 84
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 18200
    assert candidate(skill = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 110
    assert candidate(skill = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 84
    assert candidate(skill = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 770
    assert candidate(skill = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 1500000
    assert candidate(skill = [499, 501, 498, 502, 497, 503, 496, 504]) == 999970
    assert candidate(skill = [1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14, 16]) == 408
    assert candidate(skill = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 5994
    assert candidate(skill = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 7992
    assert candidate(skill = [5, 1, 4, 3, 2, 6]) == 28
    assert candidate(skill = [333, 333, 333, 333, 334, 334, 334, 334]) == 444888
    assert candidate(skill = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 770
    assert candidate(skill = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]) == 500000
    assert candidate(skill = [10, 10, 10, 10, 10, 10, 10, 10]) == 400
    assert candidate(skill = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 510
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 77000
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 11000
    assert candidate(skill = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 408
    assert candidate(skill = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 384
    assert candidate(skill = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 335
    assert candidate(skill = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 14985
    assert candidate(skill = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5, 994, 6, 993, 7, 992, 8, 991, 9, 990, 10]) == 54615
    assert candidate(skill = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
    assert candidate(skill = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]) == 375000
    assert candidate(skill = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 280
    assert candidate(skill = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995]) == 14945
    assert candidate(skill = [100, 200, 300, 400, 100, 200, 300, 400, 500, 600, 500, 600]) == 560000
    assert candidate(skill = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
    assert candidate(skill = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 490
    assert candidate(skill = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 2000000
    assert candidate(skill = [15, 16, 15, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 1820
    assert candidate(skill = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 600
    assert candidate(skill = [100, 200, 300, 400, 500, 600, 700, 800]) == 600000
    assert candidate(skill = [999, 1, 999, 1, 999, 1, 999, 1]) == 3996
    assert candidate(skill = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
    assert candidate(skill = [600, 400, 600, 400, 600, 400, 600, 400, 600, 400, 600, 400]) == 1440000
    assert candidate(skill = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 5000
    assert candidate(skill = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
    assert candidate(skill = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 288
    assert candidate(skill = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 8000
    assert candidate(skill = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 220
    assert candidate(skill = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(skill = [1, 9, 1, 9, 1, 9, 1, 9]) == 36
    assert candidate(skill = [300, 700, 200, 800, 400, 600, 100, 900, 500, 500, 400, 600]) == 1190000
    assert candidate(skill = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 335
    assert candidate(skill = [150, 250, 150, 250, 150, 250, 150, 250, 150, 250]) == 187500
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 22000
    assert candidate(skill = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 200
    assert candidate(skill = [1000, 1, 999, 2, 998, 3, 997, 4]) == 9980
    assert candidate(skill = [8, 1, 5, 3, 4, 7, 2, 6, 9, 10, 12, 11]) == 182
    assert candidate(skill = [10, 1, 10, 1, 10, 1, 10, 1]) == 40
    assert candidate(skill = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 125
    assert candidate(skill = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 40800
    assert candidate(skill = [5, 5, 5, 5, 5, 5, 5, 5]) == 100
    assert candidate(skill = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 20000
    assert candidate(skill = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 40
    assert candidate(skill = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]) == -1
    assert candidate(skill = [250, 750, 250, 750, 250, 750, 250, 750, 250, 750, 250, 750, 250, 750, 250, 750]) == 1500000
