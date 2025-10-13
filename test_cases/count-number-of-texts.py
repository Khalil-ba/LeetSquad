# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(pressedKeys = "99999999") == 108
    assert candidate(pressedKeys = "3333") == 7
    assert candidate(pressedKeys = "33") == 2
    assert candidate(pressedKeys = "4444") == 7
    assert candidate(pressedKeys = "555555") == 24
    assert candidate(pressedKeys = "9999999") == 56
    assert candidate(pressedKeys = "888888888") == 149
    assert candidate(pressedKeys = "888888") == 24
    assert candidate(pressedKeys = "7777777") == 56
    assert candidate(pressedKeys = "66") == 2
    assert candidate(pressedKeys = "55555") == 13
    assert candidate(pressedKeys = "888") == 4
    assert candidate(pressedKeys = "33344455566677778889999") == 65536
    assert candidate(pressedKeys = "2222") == 7
    assert candidate(pressedKeys = "7777") == 8
    assert candidate(pressedKeys = "77777777") == 108
    assert candidate(pressedKeys = "8888") == 7
    assert candidate(pressedKeys = "6666666") == 44
    assert candidate(pressedKeys = "23456789") == 1
    assert candidate(pressedKeys = "666") == 4
    assert candidate(pressedKeys = "22233") == 8
    assert candidate(pressedKeys = "555") == 4
    assert candidate(pressedKeys = "9999999999") == 401
    assert candidate(pressedKeys = "44444") == 13
    assert candidate(pressedKeys = "333333") == 24
    assert candidate(pressedKeys = "99999") == 15
    assert candidate(pressedKeys = "88888") == 13
    assert candidate(pressedKeys = "222222222222222222222222222222222222") == 82876089
    assert candidate(pressedKeys = "9999888777666555444333222111") == 524288
    assert candidate(pressedKeys = "777777777777777777777777777777777777") == 312882411
    assert candidate(pressedKeys = "2222222222222222222222222222222222227777777777777777777777777777777") == 168766023
    assert candidate(pressedKeys = "2223333333333333333333333333333333334444444444444444444444444444444") == 151530826
    assert candidate(pressedKeys = "234567898765432345678987654323456789876543234567898765432") == 1
    assert candidate(pressedKeys = "7773333322225555555555444446666688888") == 219119992
    assert candidate(pressedKeys = "222222222222222222222222222222222222444444444444444444444444444") == 964547839
    assert candidate(pressedKeys = "9999999999999999999999999999999999999999999999999999999999999999999") == 831813694
    assert candidate(pressedKeys = "55555555555555555555555555555555555577777777777777777777777777777778888888888888888888888888888888") == 60492310
    assert candidate(pressedKeys = "333322225555444466668888") == 117649
