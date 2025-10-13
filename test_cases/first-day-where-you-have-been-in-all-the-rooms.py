# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nextVisit = [0, 0, 2]) == 6
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5]) == 10
    assert candidate(nextVisit = [0, 2, 1, 0, 1, 2]) == 52
    assert candidate(nextVisit = [0, 1, 1, 1, 1]) == 16
    assert candidate(nextVisit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1022
    assert candidate(nextVisit = [0, 1, 0, 1, 0, 1]) == 42
    assert candidate(nextVisit = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 712
    assert candidate(nextVisit = [0, 1, 2, 3, 2, 1, 0, 1, 2, 3]) == 230
    assert candidate(nextVisit = [0, 1, 0, 2]) == 10
    assert candidate(nextVisit = [0, 1, 2, 0]) == 6
    assert candidate(nextVisit = [0, 1, 1, 1, 1, 1]) == 32
    assert candidate(nextVisit = [0, 1, 1, 0, 1, 1, 0]) == 72
    assert candidate(nextVisit = [0, 1, 0, 2, 1]) == 18
    assert candidate(nextVisit = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 682
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 0]) == 10
    assert candidate(nextVisit = [0, 2, 2, 2, 2, 2]) == 20
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18
    assert candidate(nextVisit = [0, 2, 1, 0]) == 12
    assert candidate(nextVisit = [0, 1, 1, 0, 1, 2]) == 36
    assert candidate(nextVisit = [0, 1, 1, 0]) == 8
    assert candidate(nextVisit = [0, 2, 1, 0, 1]) == 26
    assert candidate(nextVisit = [0, 0]) == 2
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]) == 328
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0, 0, 0, 0]) == 670
    assert candidate(nextVisit = [0, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == 192
    assert candidate(nextVisit = [0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 579139391
    assert candidate(nextVisit = [0, 1, 0, 3, 2, 5, 4, 7, 6, 9]) == 58
    assert candidate(nextVisit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1022
    assert candidate(nextVisit = [0, 0, 2, 1, 4, 3, 5, 6, 7, 8, 9]) == 98
    assert candidate(nextVisit = [0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0]) == 599186
    assert candidate(nextVisit = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == 358
    assert candidate(nextVisit = [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18]) == 56
    assert candidate(nextVisit = [0, 1, 0, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 633246732
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 38
    assert candidate(nextVisit = [0, 2, 1, 2, 3, 4, 5, 4, 3, 2]) == 178
    assert candidate(nextVisit = [0, 2, 1, 3, 1, 2, 4, 2, 1, 3, 1, 2, 4, 2, 1, 3, 1, 2, 4, 2, 1, 3, 1, 2, 4, 2, 1, 3, 1, 2, 4, 2, 1, 3, 1, 2, 4]) == 449162187
    assert candidate(nextVisit = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 110
    assert candidate(nextVisit = [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2]) == 786434
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2044
    assert candidate(nextVisit = [0, 1, 0, 3, 2, 1, 4, 5, 2, 3, 6, 7, 8, 9]) == 3802
    assert candidate(nextVisit = [0, 2, 1, 0, 4, 3, 2, 1, 0]) == 176
    assert candidate(nextVisit = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 524288
    assert candidate(nextVisit = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 90
    assert candidate(nextVisit = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 562740
    assert candidate(nextVisit = [0, 2, 1, 0, 3, 2, 1, 0, 4, 3, 2, 1, 0]) == 4912
    assert candidate(nextVisit = [0, 3, 5, 3, 4, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 0]) == 11288
    assert candidate(nextVisit = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 19]) == 262148
    assert candidate(nextVisit = [0, 2, 1, 0, 3, 2, 1, 0, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 6, 5, 4, 3, 2, 1, 0]) == 40131408
    assert candidate(nextVisit = [0, 1, 0, 2, 1, 0, 3, 2, 1, 0, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 6, 5, 4, 3, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 0]) == 13851577
    assert candidate(nextVisit = [0, 2, 1, 3, 1, 2, 5, 4, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]) == 269566
    assert candidate(nextVisit = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 461127067
    assert candidate(nextVisit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1048574
    assert candidate(nextVisit = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 44739242
    assert candidate(nextVisit = [0, 1, 0, 2, 1, 0, 3, 2, 1, 0]) == 556
    assert candidate(nextVisit = [0, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 594736
    assert candidate(nextVisit = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 701096
    assert candidate(nextVisit = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 786430
    assert candidate(nextVisit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1048574
    assert candidate(nextVisit = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 699050
    assert candidate(nextVisit = [0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9]) == 198234
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10258
    assert candidate(nextVisit = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 712
    assert candidate(nextVisit = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 260
    assert candidate(nextVisit = [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 28010
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 41964584
    assert candidate(nextVisit = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]) == 308
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 63550
    assert candidate(nextVisit = [0, 1, 1, 3, 2, 2, 5]) == 34
    assert candidate(nextVisit = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 311766262
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 38954
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0]) == 18
    assert candidate(nextVisit = [0, 1, 0, 2, 3, 2, 5, 4]) == 82
    assert candidate(nextVisit = [0, 2, 1, 0, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9]) == 438546
    assert candidate(nextVisit = [0, 1, 2, 3, 2, 3, 4, 3, 4, 5]) == 154
    assert candidate(nextVisit = [5, 4, 3, 2, 1, 0]) == 48
    assert candidate(nextVisit = [0, 1, 0, 3, 0, 1, 0, 5, 0, 1, 0, 3, 0, 1, 0, 7, 0, 1, 0, 3, 0, 1]) == 1543578
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 3, 2, 3, 4, 5]) == 106
    assert candidate(nextVisit = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 717916156
    assert candidate(nextVisit = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 57521884
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10258
    assert candidate(nextVisit = [0, 1, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16, 0, 18, 0, 20]) == 5114
    assert candidate(nextVisit = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]) == 438
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3]) == 123366
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20126903
    assert candidate(nextVisit = [5, 0, 4, 1, 3, 2, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 514496163
    assert candidate(nextVisit = [0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4, 0, 0, 5, 0, 0, 6, 0, 0, 7, 0, 0, 8, 0, 0, 9, 0, 0, 10]) == 943314207
    assert candidate(nextVisit = [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3]) == 229862
    assert candidate(nextVisit = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 317428
    assert candidate(nextVisit = [0, 2, 1, 0, 3, 4, 5]) == 60
    assert candidate(nextVisit = [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 66670
    assert candidate(nextVisit = [0, 2, 1, 2, 0, 0, 0, 3, 4, 2, 5]) == 1312
    assert candidate(nextVisit = [0, 2, 4, 6, 8, 0, 2, 4, 6, 8]) == 812
    assert candidate(nextVisit = [0, 1, 0, 3, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 89816588
    assert candidate(nextVisit = [0, 2, 1, 0, 3, 2, 1]) == 80
    assert candidate(nextVisit = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 25]) == 2657202
    assert candidate(nextVisit = [0, 3, 1, 0, 2, 0, 3, 1, 0, 2, 0, 3, 1, 0, 2, 0, 3, 1, 0, 2, 0, 3, 1, 0, 2, 0, 3, 1, 0, 2, 0]) == 558657481
    assert candidate(nextVisit = [0, 5, 2, 4, 3, 1, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 212
    assert candidate(nextVisit = [0, 2, 1, 2, 3, 2, 1, 2, 3, 4]) == 430
    assert candidate(nextVisit = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17, 0, 18, 0, 19, 0, 20, 0, 21, 0, 22, 0, 23, 0, 24, 0]) == 855298880
    assert candidate(nextVisit = [0, 2, 4, 6, 8, 0, 2, 4, 6, 8]) == 812
    assert candidate(nextVisit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 40
    assert candidate(nextVisit = [0, 2, 1, 0, 3, 2, 5, 4, 7, 6, 9, 8]) == 788
    assert candidate(nextVisit = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 512
    assert candidate(nextVisit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 640520038
    assert candidate(nextVisit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 147483632
    assert candidate(nextVisit = [0, 1, 2, 0, 3, 2, 5, 6, 7, 8, 9, 10, 0]) == 220
    assert candidate(nextVisit = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 590
    assert candidate(nextVisit = [0, 3, 2, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 38
    assert candidate(nextVisit = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 512
    assert candidate(nextVisit = [0, 1, 0, 1, 2, 3, 4, 5, 6, 7]) == 334
