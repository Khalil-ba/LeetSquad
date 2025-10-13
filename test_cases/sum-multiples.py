# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 9) == 30
    assert candidate(n = 1) == 0
    assert candidate(n = 1000) == 272066
    assert candidate(n = 7) == 21
    assert candidate(n = 10) == 40
    assert candidate(n = 210) == 12075
    assert candidate(n = 666) == 121023
    assert candidate(n = 315) == 27090
    assert candidate(n = 100) == 2838
    assert candidate(n = 50) == 691
    assert candidate(n = 300) == 24321
    assert candidate(n = 333) == 30339
    assert candidate(n = 60) == 1024
    assert candidate(n = 30) == 274
    assert candidate(n = 550) == 82614
    assert candidate(n = 103) == 2940
    assert candidate(n = 840) == 191940
    assert candidate(n = 42) == 499
    assert candidate(n = 888) == 213532
    assert candidate(n = 101) == 2838
    assert candidate(n = 250) == 17152
    assert candidate(n = 789) == 169111
    assert candidate(n = 630) == 108045
    assert candidate(n = 999) == 271066
    assert candidate(n = 256) == 17659
    assert candidate(n = 20) == 119
    assert candidate(n = 150) == 6109
    assert candidate(n = 800) == 173877
    assert candidate(n = 15) == 81
    assert candidate(n = 200) == 10845
    assert candidate(n = 512) == 70927
    assert candidate(n = 750) == 153696
    assert candidate(n = 120) == 4071
    assert candidate(n = 499) == 67389
    assert candidate(n = 700) == 133342
    assert candidate(n = 500) == 67889
    assert candidate(n = 420) == 48090
    assert candidate(n = 84) == 1904
