# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr = [1, 2, 3, 4]) == 20
    assert candidate(arr = [3, 2, 1]) == 8
    assert candidate(arr = [15, 13, 5, 3, 15]) == 500
    assert candidate(arr = [4, 11]) == 44
    assert candidate(arr = [7, 12, 8, 10]) == 284
    assert candidate(arr = [3, 5, 6, 2, 5]) == 85
    assert candidate(arr = [7, 10, 2, 8, 1]) == 174
    assert candidate(arr = [8, 12, 15, 2, 5, 7]) == 426
    assert candidate(arr = [1, 2, 3, 4, 5]) == 40
    assert candidate(arr = [6, 2, 4]) == 32
    assert candidate(arr = [3, 5, 1, 2, 4]) == 45
    assert candidate(arr = [15, 13, 5, 3, 16, 17, 18]) == 1093
    assert candidate(arr = [2, 3, 1, 4]) == 21
    assert candidate(arr = [3, 5, 2, 1, 4]) == 45
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1120
    assert candidate(arr = [5, 4, 7, 2, 11, 6]) == 212
    assert candidate(arr = [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1120
    assert candidate(arr = [5, 7, 8, 6, 2, 3]) == 163
    assert candidate(arr = [5, 4, 3, 2, 1, 6, 7]) == 112
    assert candidate(arr = [5, 2, 3, 1, 4, 6, 7]) == 113
    assert candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1]) == 168
    assert candidate(arr = [13, 15, 7, 9, 8, 11, 14, 12, 5, 6, 2, 3, 1, 4, 10]) == 1216
    assert candidate(arr = [13, 7, 11, 10, 15, 2, 1, 12, 8, 6, 5, 9, 3, 4]) == 1037
    assert candidate(arr = [5, 10, 9, 2, 3, 15, 12, 8]) == 599
    assert candidate(arr = [7, 1, 9, 8, 4, 2, 5]) == 210
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15]) == 1120
    assert candidate(arr = [15, 9, 5, 6, 11, 8, 12, 13, 14, 7, 10, 4, 3, 2, 1]) == 1221
    assert candidate(arr = [12, 4, 6, 1, 5, 9, 7]) == 284
    assert candidate(arr = [11, 13, 10, 9, 2, 15, 5, 12, 7, 14]) == 1098
    assert candidate(arr = [2, 3, 5, 7, 11, 13, 17, 19]) == 820
    assert candidate(arr = [10, 12, 7, 5, 4, 1, 6]) == 300
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40]) == 4200
    assert candidate(arr = [5, 3, 2, 7, 9, 10, 8]) == 289
    assert candidate(arr = [13, 5, 1, 12, 8, 9]) == 401
    assert candidate(arr = [7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 11, 12, 13, 14, 15]) == 1134
    assert candidate(arr = [2, 1, 3, 4, 5, 6, 7]) == 112
    assert candidate(arr = [10, 5, 15, 3, 8, 7]) == 400
    assert candidate(arr = [10, 1, 14, 7, 13, 3, 5, 2, 8, 6, 4, 9, 11, 12]) == 1019
    assert candidate(arr = [8, 3, 9, 6, 1, 10, 2]) == 266
    assert candidate(arr = [7, 11, 14, 13, 5, 15, 10]) == 838
    assert candidate(arr = [13, 7, 12, 1, 8, 5, 9, 4]) == 504
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == 301
    assert candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2668
    assert candidate(arr = [8, 5, 1, 9, 2, 4, 3, 10, 6, 7, 11, 12, 14, 13, 15]) == 1177
    assert candidate(arr = [3, 15, 2, 8, 9, 11, 5, 10, 7, 6, 12, 4]) == 864
    assert candidate(arr = [10, 5, 15, 20, 12]) == 740
    assert candidate(arr = [1, 3, 2, 6, 8, 5, 4, 7, 9, 10]) == 348
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80]) == 16800
    assert candidate(arr = [2, 15, 8, 3, 10, 6, 7, 4, 11, 1, 9, 5, 12, 14, 13]) == 1229
    assert candidate(arr = [13, 15, 1, 5, 3]) == 290
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 4046
    assert candidate(arr = [3, 4, 5, 2, 6, 7, 8, 1]) == 178
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 33000
    assert candidate(arr = [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 480
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 220
    assert candidate(arr = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 330
    assert candidate(arr = [10, 2, 5, 1, 3]) == 78
    assert candidate(arr = [11, 6, 5, 9, 3, 8, 2, 4, 7]) == 371
    assert candidate(arr = [14, 10, 1, 2, 15, 12, 8]) == 648
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1120
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1120
    assert candidate(arr = [12, 7, 11, 14, 10, 13, 6]) == 767
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(arr = [5, 1, 3, 2, 10, 7, 4]) == 172
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(arr = [5, 3, 8, 6, 2, 4, 1, 9]) == 211
    assert candidate(arr = [7, 14, 4, 14, 13, 2, 6, 13]) == 791
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 330
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 24000
    assert candidate(arr = [5, 3, 8, 1, 4, 7]) == 143
    assert candidate(arr = [13, 12, 8, 14, 15, 16, 17, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11]) == 1718
    assert candidate(arr = [6, 9, 4, 10, 5, 8, 7, 3, 11, 1, 12, 2, 13, 14, 15]) == 1202
    assert candidate(arr = [1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8]) == 1260
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1320
    assert candidate(arr = [13, 15, 1, 7, 2]) == 321
    assert candidate(arr = [8, 3, 1, 14, 10, 6, 7, 2, 13, 9, 5, 4, 11, 12]) == 1029
    assert candidate(arr = [1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9]) == 1188
    assert candidate(arr = [12, 15, 8, 3, 10, 6]) == 494
    assert candidate(arr = [15, 13, 11, 9, 7, 5, 3, 1]) == 553
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1120
    assert candidate(arr = [15, 10, 2, 3, 5, 1, 8, 6, 14, 7]) == 642
    assert candidate(arr = [15, 8, 3, 10, 6, 7, 4, 11, 1, 9, 2, 12, 5, 14, 13]) == 1232
    assert candidate(arr = [3, 5, 1, 9, 2, 4, 8, 10, 6, 7, 11, 12, 14, 13, 15]) == 1181
    assert candidate(arr = [2, 9, 3, 5, 6, 4]) == 141
    assert candidate(arr = [8, 5, 3, 2, 4, 6, 7]) == 166
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15]) == 553
    assert candidate(arr = [10, 6, 8, 3, 4, 12, 5, 14]) == 520
    assert candidate(arr = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2548
    assert candidate(arr = [1, 5, 2, 3, 6, 4, 7]) == 122
    assert candidate(arr = [8, 5, 9, 3, 6]) == 184
    assert candidate(arr = [7, 4, 9, 2, 5, 1, 8]) == 218
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 800
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 240
    assert candidate(arr = [8, 6, 10, 5, 12, 9, 7, 3, 11, 1, 4]) == 661
    assert candidate(arr = [12, 7, 4, 9, 2, 8, 5, 3]) == 342
    assert candidate(arr = [10, 15, 1, 2, 18, 9, 6]) == 668
    assert candidate(arr = [7, 6, 8, 2, 10, 5, 1, 3, 9, 4]) == 383
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 1360
    assert candidate(arr = [6, 9, 3, 7, 5, 1, 4]) == 197
    assert candidate(arr = [6, 5, 8, 10, 3, 9, 1, 14, 13, 2, 4, 7, 11, 12, 15]) == 1217
    assert candidate(arr = [4, 7, 10, 2, 13, 15, 5, 3, 8, 6, 9, 1, 14, 12, 11]) == 1263
    assert candidate(arr = [8, 9, 3, 8, 15, 2]) == 333
    assert candidate(arr = [1, 100, 1, 100, 1, 100]) == 20300
    assert candidate(arr = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 3831
    assert candidate(arr = [8, 3, 6, 1, 4, 7, 10, 2, 9, 5]) == 377
    assert candidate(arr = [8, 9, 10, 7, 6, 5, 4, 3, 2, 1]) == 344
    assert candidate(arr = [5, 3, 8, 6, 2, 4, 7, 1, 10, 9]) == 362
    assert candidate(arr = [7, 8, 6, 5, 4, 3, 2, 1]) == 174
