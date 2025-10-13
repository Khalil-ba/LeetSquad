# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 246
    assert candidate(n = 1000) == 650420578
    assert candidate(n = 100) == 905790447
    assert candidate(n = 2500) == 80958521
    assert candidate(n = 4) == 1122
    assert candidate(n = 4999) == 134620719
    assert candidate(n = 5000) == 30228214
    assert candidate(n = 2) == 54
    assert candidate(n = 1) == 12
    assert candidate(n = 500) == 350959293
    assert candidate(n = 50) == 151149117
    assert candidate(n = 10) == 10107954
    assert candidate(n = 5) == 5118
    assert candidate(n = 4000) == 685933196
    assert candidate(n = 12) == 210323922
    assert candidate(n = 2000) == 897054912
    assert candidate(n = 3750) == 477003884
    assert candidate(n = 3500) == 28484708
    assert candidate(n = 3000) == 313837042
    assert candidate(n = 30) == 462032897
    assert candidate(n = 16) == 62485141
    assert candidate(n = 10000) == 779575021
    assert candidate(n = 8) == 485778
    assert candidate(n = 250) == 601916395
    assert candidate(n = 999) == 672393158
    assert candidate(n = 32) == 554911778
    assert candidate(n = 20) == 690883140
    assert candidate(n = 11) == 46107966
    assert candidate(n = 15) == 963045241
    assert candidate(n = 200) == 693684710
    assert candidate(n = 1234) == 18988659
    assert candidate(n = 750) == 493513580
    assert candidate(n = 4500) == 471193061
    assert candidate(n = 6) == 23346
    assert candidate(n = 7) == 106494
    assert candidate(n = 25) == 676744457
    assert candidate(n = 1500) == 814277332
