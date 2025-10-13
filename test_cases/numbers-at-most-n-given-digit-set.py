# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(digits = ['1', '4', '9'],n = 1000000000) == 29523
    assert candidate(digits = ['7'],n = 8) == 1
    assert candidate(digits = ['1', '2', '3'],n = 123) == 18
    assert candidate(digits = ['2', '3', '5'],n = 250) == 18
    assert candidate(digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],n = 999) == 819
    assert candidate(digits = ['3', '4', '5'],n = 1000) == 39
    assert candidate(digits = ['1', '3', '5', '7'],n = 100) == 20
    assert candidate(digits = ['1', '2', '3'],n = 123456789) == 14214
    assert candidate(digits = ['1', '3', '5', '7'],n = 100000000) == 87380
    assert candidate(digits = ['2', '4', '6', '8'],n = 5000) == 212
    assert candidate(digits = ['2', '4'],n = 100) == 6
    assert candidate(digits = ['2', '4', '6', '8'],n = 468246824) == 198406
    assert candidate(digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],n = 1000000000) == 435848049
    assert candidate(digits = ['1', '3', '5', '7', '9'],n = 99999) == 3905
    assert candidate(digits = ['1', '5', '9'],n = 99999) == 363
    assert candidate(digits = ['2', '3', '6', '7', '8'],n = 123456789) == 488280
    assert candidate(digits = ['1', '2', '3', '4'],n = 1000) == 84
    assert candidate(digits = ['5', '9'],n = 555555555) == 511
    assert candidate(digits = ['2', '5', '9'],n = 10000) == 120
    assert candidate(digits = ['2', '4', '8'],n = 888888888) == 29523
    assert candidate(digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],n = 999999999) == 435848049
    assert candidate(digits = ['3', '6', '9'],n = 333699) == 381
    assert candidate(digits = ['1', '2', '3'],n = 10000) == 120
    assert candidate(digits = ['1', '2', '3', '4'],n = 5000) == 340
    assert candidate(digits = ['2', '4', '6', '8'],n = 1000000) == 5460
    assert candidate(digits = ['1', '3', '5', '7', '9'],n = 555555555) == 1464843
    assert candidate(digits = ['1', '2', '3', '4', '5'],n = 9999) == 780
    assert candidate(digits = ['4', '5', '6'],n = 456) == 18
    assert candidate(digits = ['1', '3', '5', '7', '9'],n = 500000000) == 1269530
    assert candidate(digits = ['1', '2', '5'],n = 100000) == 363
    assert candidate(digits = ['1', '2'],n = 212121212) == 852
    assert candidate(digits = ['1', '2', '3'],n = 111111111) == 9841
    assert candidate(digits = ['2', '3', '7', '8'],n = 5000) == 212
    assert candidate(digits = ['2', '6', '9'],n = 123456789) == 9840
    assert candidate(digits = ['1', '3', '7', '9'],n = 123456789) == 103764
    assert candidate(digits = ['2', '6', '8'],n = 100000) == 363
    assert candidate(digits = ['2', '5', '8'],n = 500) == 21
    assert candidate(digits = ['1', '2', '3', '4', '5'],n = 5000) == 655
    assert candidate(digits = ['8', '9'],n = 999999999) == 1022
    assert candidate(digits = ['1', '2', '3', '4'],n = 43210) == 1252
    assert candidate(digits = ['1', '9'],n = 999999999) == 1022
    assert candidate(digits = ['2', '6', '8'],n = 4500) == 66
    assert candidate(digits = ['1', '3', '5'],n = 555555555) == 29523
    assert candidate(digits = ['1', '4', '7', '9'],n = 123456789) == 103764
    assert candidate(digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],n = 123456789) == 54481005
    assert candidate(digits = ['5'],n = 1000000000) == 9
    assert candidate(digits = ['1', '9'],n = 1000000000) == 1022
    assert candidate(digits = ['1', '6', '8'],n = 5678) == 66
    assert candidate(digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],n = 123456789) == 54481005
    assert candidate(digits = ['1', '3', '5', '7', '9'],n = 99999) == 3905
    assert candidate(digits = ['2', '4', '6', '8'],n = 888888888) == 349524
    assert candidate(digits = ['1', '2', '3', '4', '5'],n = 100000) == 3905
    assert candidate(digits = ['1', '2', '4', '8'],n = 1024) == 84
    assert candidate(digits = ['1', '2', '3', '4'],n = 987654321) == 349524
    assert candidate(digits = ['1', '5', '7', '9'],n = 1579) == 112
    assert candidate(digits = ['2', '6', '8'],n = 2688) == 57
    assert candidate(digits = ['1', '3', '5', '7'],n = 777777777) == 349524
    assert candidate(digits = ['9'],n = 999999999) == 9
    assert candidate(digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],n = 111111111) == 48427561
    assert candidate(digits = ['1'],n = 1000000000) == 9
    assert candidate(digits = ['1', '3', '5', '7', '9'],n = 563827194) == 1503905
    assert candidate(digits = ['2', '6', '9'],n = 1000000) == 1092
    assert candidate(digits = ['1', '2', '3'],n = 1111) == 40
    assert candidate(digits = ['1', '6', '8'],n = 1000000000) == 29523
    assert candidate(digits = ['5', '7', '9'],n = 100000) == 363
    assert candidate(digits = ['4', '8'],n = 888) == 14
    assert candidate(digits = ['1', '2', '3'],n = 333) == 39
    assert candidate(digits = ['1', '2', '5'],n = 1111) == 40
    assert candidate(digits = ['1', '2'],n = 1024) == 14
    assert candidate(digits = ['5', '8'],n = 5885) == 21
    assert candidate(digits = ['6', '7', '8'],n = 99999) == 363
    assert candidate(digits = ['1', '2', '3', '4'],n = 9999) == 340
    assert candidate(digits = ['3', '5', '7', '9'],n = 1000000) == 5460
    assert candidate(digits = ['2', '3', '5', '7'],n = 777777777) == 349524
    assert candidate(digits = ['1', '2', '3', '4', '5'],n = 12345) == 975
    assert candidate(digits = ['1', '7', '9'],n = 979797) == 1001
    assert candidate(digits = ['1', '2', '3', '4', '5', '6'],n = 654321) == 54121
    assert candidate(digits = ['1', '3', '5', '7', '9'],n = 987654321) == 2363280
    assert candidate(digits = ['1', '2', '5'],n = 1000000000) == 29523
    assert candidate(digits = ['1', '4', '9'],n = 100000000) == 9840
    assert candidate(digits = ['1', '5', '9'],n = 1000000000) == 29523
    assert candidate(digits = ['3', '9'],n = 393939) == 84
    assert candidate(digits = ['1', '2'],n = 1024) == 14
    assert candidate(digits = ['1', '5', '9'],n = 999999999) == 29523
    assert candidate(digits = ['1', '3', '5', '7'],n = 777777777) == 349524
    assert candidate(digits = ['1', '3', '5', '7', '9'],n = 123456789) == 566405
    assert candidate(digits = ['1', '2', '3', '4', '5'],n = 50000) == 3280
    assert candidate(digits = ['1', '3', '5', '7', '9'],n = 20000) == 1405
    assert candidate(digits = ['1', '3', '7'],n = 77777777) == 9840
    assert candidate(digits = ['5', '7', '9'],n = 888888888) == 22962
    assert candidate(digits = ['1', '2', '4', '8'],n = 999999999) == 349524
    assert candidate(digits = ['3', '7', '8'],n = 378378378) == 13626
    assert candidate(digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],n = 999999999) == 435848049
    assert candidate(digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],n = 987654321) == 429794605
    assert candidate(digits = ['3', '7', '9'],n = 999999999) == 29523
    assert candidate(digits = ['1', '2', '3'],n = 321) == 34
    assert candidate(digits = ['3', '7', '8'],n = 1234) == 39
    assert candidate(digits = ['1', '5', '9'],n = 987654321) == 27336
    assert candidate(digits = ['1', '3', '5', '7', '9'],n = 999999999) == 2441405
    assert candidate(digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'],n = 987654321) == 429794605
    assert candidate(digits = ['2', '3', '7', '8'],n = 8732) == 313
    assert candidate(digits = ['2', '4', '6', '8'],n = 100000000) == 87380
    assert candidate(digits = ['1'],n = 1000000) == 6
    assert candidate(digits = ['3', '5', '7'],n = 100000000) == 9840
    assert candidate(digits = ['2', '6', '7'],n = 10000) == 120
    assert candidate(digits = ['1', '3', '7', '9'],n = 50000) == 852
    assert candidate(digits = ['1', '2', '3', '4', '5'],n = 222222222) == 976562
    assert candidate(digits = ['1', '9'],n = 500000000) == 766
    assert candidate(digits = ['1', '3', '5'],n = 999999999) == 29523
    assert candidate(digits = ['1', '5', '7', '8'],n = 100000) == 1364
    assert candidate(digits = ['1', '9'],n = 1000000000) == 1022
    assert candidate(digits = ['5', '6', '7'],n = 777777777) == 29523
    assert candidate(digits = ['3', '5', '7'],n = 357357) == 504
