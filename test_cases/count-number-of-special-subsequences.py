# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [0, 0, 1, 1, 2]) == 9
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2]) == 0
    assert candidate(nums = [0, 0, 0, 1, 1, 2]) == 21
    assert candidate(nums = [2, 2, 0, 0]) == 0
    assert candidate(nums = [0, 1, 2, 2]) == 3
    assert candidate(nums = [0, 1, 2, 2, 2]) == 7
    assert candidate(nums = [1, 2, 2, 0, 0, 1]) == 0
    assert candidate(nums = [0, 1, 2, 1, 2, 0, 1, 2]) == 19
    assert candidate(nums = [0, 1, 0, 1, 2]) == 5
    assert candidate(nums = [0, 1, 1, 1, 2, 2, 2]) == 49
    assert candidate(nums = [2, 1, 0, 1, 0, 2, 0]) == 1
    assert candidate(nums = [0, 1, 2, 0, 1, 0, 1, 2]) == 19
    assert candidate(nums = [2, 0, 1, 2, 0, 1, 2]) == 7
    assert candidate(nums = [2, 0, 1, 0, 1, 2]) == 5
    assert candidate(nums = [2, 0, 1, 0, 1, 2, 0, 1, 2]) == 27
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 2]) == 63
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 0, 1, 2, 0, 1, 2, 0]) == 7
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 2, 2]) == 51
    assert candidate(nums = [0, 1, 2, 0, 1, 2]) == 7
    assert candidate(nums = [0, 1, 2]) == 1
    assert candidate(nums = [0, 0, 1, 2, 1, 2]) == 15
    assert candidate(nums = [0, 0, 1, 1, 2, 2]) == 27
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 2, 2, 2]) == 119
    assert candidate(nums = [0, 0, 0, 1, 2, 2]) == 21
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2]) == 343
    assert candidate(nums = [0, 1, 0, 1, 2, 0, 1, 2]) == 27
    assert candidate(nums = [0, 1, 1, 2, 2, 2]) == 21
    assert candidate(nums = [1, 2, 0]) == 0
    assert candidate(nums = [2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]) == 735
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 375309442
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2]) == 21567
    assert candidate(nums = [0, 0, 0, 0, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2]) == 9975
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 554508028
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 25039
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 133432831
    assert candidate(nums = [0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 207
    assert candidate(nums = [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0]) == 351
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 14415
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == 2048383
    assert candidate(nums = [0, 1, 0, 2, 0, 1, 0, 2, 1, 2]) == 55
    assert candidate(nums = [0, 1, 1, 0, 2, 2, 1, 1, 0, 2, 0, 1, 2]) == 135
    assert candidate(nums = [0, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]) == 6399
    assert candidate(nums = [2, 1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]) == 735
    assert candidate(nums = [0, 1, 2, 2, 0, 1, 2, 2, 0, 1, 2, 2, 0, 1, 2, 2, 0, 1, 2, 2]) == 3519
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 14175
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 0, 1, 2, 0, 1, 2]) == 2335
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2]) == 3999
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 0, 1, 2, 2]) == 3279
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]) == 1575
    assert candidate(nums = [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0]) == 0
    assert candidate(nums = [0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2]) == 71
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 0, 0, 0, 2, 2, 2, 1, 1, 1, 0, 0, 0]) == 0
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 2, 2, 0, 0, 1, 1, 2, 2, 2]) == 1647
    assert candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 2]) == 423
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]) == 26775
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 29295
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 2, 2]) == 135
    assert candidate(nums = [2, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 1]) == 0
    assert candidate(nums = [0, 0, 0, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 0, 1, 2]) == 4047
    assert candidate(nums = [0, 1, 2, 0, 1, 2, 0, 1, 2]) == 31
    assert candidate(nums = [2, 2, 2, 1, 1, 0, 0, 0, 0]) == 0
    assert candidate(nums = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 1023
    assert candidate(nums = [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 70599160
    assert candidate(nums = [0, 0, 1, 1, 1, 1, 2, 2, 0, 0, 1, 1, 2]) == 495
    assert candidate(nums = [0, 1, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2]) == 63
    assert candidate(nums = [0, 1, 1, 2, 0, 1, 2, 2, 1, 2, 0, 1, 2, 2, 1, 0, 1, 2, 2]) == 2847
    assert candidate(nums = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2]) == 675
    assert candidate(nums = [0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2]) == 127
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]) == 1575
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 2, 2, 2, 2]) == 255
    assert candidate(nums = [2, 0, 0, 0, 1, 1, 1, 2, 2, 2]) == 343
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 250047
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2]) == 8575
    assert candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2]) == 651
    assert candidate(nums = [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 18943
    assert candidate(nums = [0, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2]) == 4609
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 534776319
    assert candidate(nums = [0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 303
    assert candidate(nums = [0, 1, 1, 2, 2, 2, 2, 2, 0, 1, 2, 0, 1, 2, 2]) == 855
    assert candidate(nums = [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 2815
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]) == 3375
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 4287
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]) == 20223
    assert candidate(nums = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 2815
    assert candidate(nums = [2, 2, 0, 0, 0, 1, 1, 1, 2, 2]) == 147
    assert candidate(nums = [2, 0, 0, 1, 1, 1, 2, 2, 2, 2, 0, 0, 1, 1, 2, 2]) == 1647
    assert candidate(nums = [0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 831
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 29791
    assert candidate(nums = [2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 451143
    assert candidate(nums = [2, 2, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 335
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 2, 0, 1, 2]) == 1855
    assert candidate(nums = [0, 1, 1, 1, 2, 2, 2, 2, 0, 1, 2]) == 227
    assert candidate(nums = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 0, 1, 2]) == 1447
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 0, 0, 1, 1, 2, 2, 2, 2]) == 16095
    assert candidate(nums = [0, 1, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]) == 7039
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]) == 351
    assert candidate(nums = [0, 1, 2, 0, 0, 1, 1, 1, 2, 2, 0, 1, 2]) == 479
    assert candidate(nums = [2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]) == 2943
    assert candidate(nums = [2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]) == 735
    assert candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 2, 2]) == 975
    assert candidate(nums = [2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 2, 2]) == 2239
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]) == 6727
    assert candidate(nums = [0, 0, 0, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0]) == 49
    assert candidate(nums = [0, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]) == 783
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]) == 704511
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2]) == 527
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 0, 0, 1, 1, 2, 2, 2, 2]) == 28639
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2]) == 735
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]) == 2943
    assert candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 2]) == 315
    assert candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 1323
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]) == 3375
    assert candidate(nums = [0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2]) == 3087
    assert candidate(nums = [0, 1, 2, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2]) == 167
    assert candidate(nums = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 351
    assert candidate(nums = [2, 1, 0, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2]) == 7423
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2]) == 4335
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 0, 1, 2]) == 3151
    assert candidate(nums = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 18943
    assert candidate(nums = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 274431
    assert candidate(nums = [0, 0, 1, 1, 2, 0, 1, 2, 0, 1, 2]) == 151
    assert candidate(nums = [0, 0, 0, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2]) == 3591
    assert candidate(nums = [2, 2, 2, 0, 0, 0, 1, 1, 1]) == 0
    assert candidate(nums = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]) == 111
    assert candidate(nums = [0, 0, 0, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2]) == 3367
