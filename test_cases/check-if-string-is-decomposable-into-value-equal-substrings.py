# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "7777777777777777") == False
    assert candidate(s = "666666666666666") == False
    assert candidate(s = "111111") == False
    assert candidate(s = "999999999999999999") == False
    assert candidate(s = "55555555555555") == True
    assert candidate(s = "00011111222") == True
    assert candidate(s = "11") == True
    assert candidate(s = "3333333333") == False
    assert candidate(s = "011100022233") == False
    assert candidate(s = "000111000") == False
    assert candidate(s = "88888888888888888") == True
    assert candidate(s = "22222222") == True
    assert candidate(s = "444444444444") == False
    assert candidate(s = "122111") == False
