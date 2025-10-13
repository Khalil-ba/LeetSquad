# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 25
    assert candidate(n = 100) == 20522904
    assert candidate(n = 10000) == 402613600
    assert candidate(n = 2) == 9
    assert candidate(n = 1) == 4
    assert candidate(n = 1000) == 500478595
    assert candidate(n = 10) == 20736
    assert candidate(n = 4000) == 984988507
    assert candidate(n = 7000) == 750848153
    assert candidate(n = 2000) == 329423452
    assert candidate(n = 7500) == 39764836
    assert candidate(n = 50) == 245481867
    assert candidate(n = 5) == 169
    assert candidate(n = 3000) == 511358621
    assert candidate(n = 30) == 30066266
    assert candidate(n = 4) == 64
    assert candidate(n = 1001) == 307206160
    assert candidate(n = 8) == 3025
    assert candidate(n = 250) == 172820552
    assert candidate(n = 8000) == 823868594
    assert candidate(n = 5000) == 851109891
    assert candidate(n = 9999) == 459963766
    assert candidate(n = 20) == 313679521
    assert candidate(n = 15) == 2550409
    assert candidate(n = 2500) == 968650195
    assert candidate(n = 9000) == 641644802
    assert candidate(n = 200) == 450435314
    assert candidate(n = 9) == 7921
    assert candidate(n = 6) == 441
    assert candidate(n = 6000) == 337759600
    assert candidate(n = 500) == 164765197
    assert candidate(n = 7) == 1156
    assert candidate(n = 25) == 580030458
