# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 5
    assert candidate(n = 100) == 190242381
    assert candidate(n = 4) == 11
    assert candidate(n = 2) == 2
    assert candidate(n = 1) == 1
    assert candidate(n = 500) == 603582422
    assert candidate(n = 1000) == 979232805
    assert candidate(n = 10) == 1255
    assert candidate(n = 5) == 24
    assert candidate(n = 12) == 6105
    assert candidate(n = 125) == 562894970
    assert candidate(n = 50) == 451995198
    assert candidate(n = 650) == 5517492
    assert candidate(n = 300) == 768506587
    assert candidate(n = 123) == 215563687
    assert candidate(n = 550) == 727269359
    assert candidate(n = 600) == 771568221
    assert candidate(n = 450) == 795340037
    assert candidate(n = 501) == 210280741
    assert candidate(n = 700) == 637136622
    assert candidate(n = 250) == 872044590
    assert candidate(n = 999) == 326038248
    assert candidate(n = 89) == 469785861
    assert candidate(n = 20) == 3418626
    assert candidate(n = 150) == 773955023
    assert candidate(n = 800) == 177362789
    assert candidate(n = 200) == 627399438
    assert candidate(n = 400) == 517656200
    assert candidate(n = 750) == 533845494
    assert candidate(n = 6) == 53
