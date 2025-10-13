# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(numPeople = 18) == 4862
    assert candidate(numPeople = 16) == 1430
    assert candidate(numPeople = 8) == 14
    assert candidate(numPeople = 12) == 132
    assert candidate(numPeople = 20) == 16796
    assert candidate(numPeople = 10) == 42
    assert candidate(numPeople = 4) == 2
    assert candidate(numPeople = 14) == 429
    assert candidate(numPeople = 6) == 5
    assert candidate(numPeople = 900) == 876537848
    assert candidate(numPeople = 128) == 887145589
    assert candidate(numPeople = 256) == 707292517
    assert candidate(numPeople = 600) == 718512182
    assert candidate(numPeople = 32) == 35357670
    assert candidate(numPeople = 800) == 497153305
    assert candidate(numPeople = 64) == 488309750
    assert candidate(numPeople = 2) == 1
    assert candidate(numPeople = 60) == 475387402
    assert candidate(numPeople = 50) == 946367425
    assert candidate(numPeople = 40) == 564120378
    assert candidate(numPeople = 70) == 93302951
    assert candidate(numPeople = 80) == 602941373
    assert candidate(numPeople = 512) == 962620544
    assert candidate(numPeople = 768) == 696991831
    assert candidate(numPeople = 90) == 205311759
    assert candidate(numPeople = 450) == 113566864
    assert candidate(numPeople = 100) == 265470434
    assert candidate(numPeople = 30) == 9694845
    assert candidate(numPeople = 750) == 309104184
    assert candidate(numPeople = 22) == 58786
    assert candidate(numPeople = 26) == 742900
    assert candidate(numPeople = 24) == 208012
    assert candidate(numPeople = 400) == 868596491
    assert candidate(numPeople = 700) == 834169133
    assert candidate(numPeople = 500) == 217193473
    assert candidate(numPeople = 300) == 516266904
    assert candidate(numPeople = 200) == 558488487
