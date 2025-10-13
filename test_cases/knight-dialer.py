# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 46
    assert candidate(n = 100) == 540641702
    assert candidate(n = 50) == 267287516
    assert candidate(n = 2500) == 851996060
    assert candidate(n = 5000) == 406880451
    assert candidate(n = 2) == 20
    assert candidate(n = 1) == 10
    assert candidate(n = 500) == 84202957
    assert candidate(n = 1000) == 88106097
    assert candidate(n = 10) == 14912
    assert candidate(n = 5) == 240
    assert candidate(n = 3131) == 136006598
    assert candidate(n = 4000) == 315083963
    assert candidate(n = 1600) == 585618181
    assert candidate(n = 4750) == 955420830
    assert candidate(n = 4600) == 152432289
    assert candidate(n = 2000) == 71794716
    assert candidate(n = 3750) == 17358003
    assert candidate(n = 2400) == 248946071
    assert candidate(n = 3333) == 857043783
    assert candidate(n = 3500) == 624537543
    assert candidate(n = 3000) == 447863713
    assert candidate(n = 30) == 986742198
    assert candidate(n = 1200) == 823605881
    assert candidate(n = 4900) == 790356323
    assert candidate(n = 2750) == 49052199
    assert candidate(n = 1800) == 159765442
    assert candidate(n = 2800) == 779464575
    assert candidate(n = 250) == 296754066
    assert candidate(n = 4250) == 12437801
    assert candidate(n = 20) == 58689536
    assert candidate(n = 1250) == 926597988
    assert candidate(n = 3132) == 915594565
    assert candidate(n = 800) == 709497038
    assert candidate(n = 15) == 944000
    assert candidate(n = 4999) == 659158877
    assert candidate(n = 200) == 38950354
    assert candidate(n = 400) == 23117445
    assert candidate(n = 1234) == 758728301
    assert candidate(n = 750) == 185434245
    assert candidate(n = 4500) == 756988614
    assert candidate(n = 1500) == 487569438
