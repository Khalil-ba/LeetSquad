# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 90
    assert candidate(n = 250) == 418733499
    assert candidate(n = 100) == 14159051
    assert candidate(n = 4) == 2520
    assert candidate(n = 2) == 6
    assert candidate(n = 20) == 580270580
    assert candidate(n = 1) == 1
    assert candidate(n = 500) == 764678010
    assert candidate(n = 50) == 784760423
    assert candidate(n = 10) == 850728840
    assert candidate(n = 5) == 113400
    assert candidate(n = 12) == 67543367
    assert candidate(n = 125) == 129345050
    assert candidate(n = 110) == 120658916
    assert candidate(n = 300) == 234038968
    assert candidate(n = 60) == 988537746
    assert candidate(n = 30) == 920731808
    assert candidate(n = 450) == 586675271
    assert candidate(n = 80) == 189044563
    assert candidate(n = 175) == 82390790
    assert candidate(n = 495) == 498394413
    assert candidate(n = 8) == 729647433
    assert candidate(n = 18) == 368349166
    assert candidate(n = 75) == 149163518
    assert candidate(n = 350) == 436707893
    assert candidate(n = 150) == 707081203
    assert candidate(n = 15) == 621371750
    assert candidate(n = 200) == 880584563
    assert candidate(n = 400) == 467993882
    assert candidate(n = 499) == 496638171
    assert candidate(n = 55) == 22089728
    assert candidate(n = 25) == 586091532
