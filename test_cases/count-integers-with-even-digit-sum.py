# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(num = 30) == 14
    assert candidate(num = 10) == 4
    assert candidate(num = 999) == 499
    assert candidate(num = 500) == 249
    assert candidate(num = 4) == 2
    assert candidate(num = 2) == 1
    assert candidate(num = 1) == 0
    assert candidate(num = 100) == 49
    assert candidate(num = 750) == 375
    assert candidate(num = 1000) == 499
    assert candidate(num = 432) == 215
    assert candidate(num = 666) == 333
    assert candidate(num = 456) == 227
    assert candidate(num = 250) == 124
    assert candidate(num = 345) == 172
    assert candidate(num = 99) == 49
    assert candidate(num = 222) == 111
    assert candidate(num = 200) == 100
    assert candidate(num = 444) == 222
    assert candidate(num = 555) == 277
    assert candidate(num = 888) == 444
    assert candidate(num = 123) == 61
    assert candidate(num = 789) == 394
    assert candidate(num = 333) == 166
    assert candidate(num = 375) == 187
    assert candidate(num = 256) == 127
    assert candidate(num = 800) == 400
    assert candidate(num = 678) == 338
    assert candidate(num = 623) == 311
    assert candidate(num = 600) == 300
    assert candidate(num = 777) == 388
    assert candidate(num = 850) == 424
    assert candidate(num = 899) == 449
    assert candidate(num = 299) == 149
