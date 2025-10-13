# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 30) == 13697484
    assert candidate(n = 99) == 75763854
    assert candidate(n = 75) == 918450925
    assert candidate(n = 20) == 344376809
    assert candidate(n = 2) == 1
    assert candidate(n = 19) == 445364737
    assert candidate(n = 100) == 682289015
    assert candidate(n = 50) == 451768713
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 17280
    assert candidate(n = 5) == 12
    assert candidate(n = 97) == 519081041
    assert candidate(n = 3) == 2
    assert candidate(n = 61) == 250895270
    assert candidate(n = 47) == 627742601
    assert candidate(n = 70) == 892906519
    assert candidate(n = 60) == 125049738
    assert candidate(n = 40) == 965722612
    assert candidate(n = 4) == 4
    assert candidate(n = 37) == 546040181
    assert candidate(n = 98) == 892915734
    assert candidate(n = 73) == 78238453
    assert candidate(n = 80) == 405243354
    assert candidate(n = 89) == 673469112
    assert candidate(n = 85) == 430788419
    assert candidate(n = 83) == 913651722
    assert candidate(n = 90) == 448961084
