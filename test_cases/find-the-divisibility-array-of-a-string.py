# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(word = "1111111111",m = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(word = "998244353",m = 3) == [1, 1, 0, 0, 0, 1, 1, 0, 0]
    assert candidate(word = "00000",m = 1) == [1, 1, 1, 1, 1]
    assert candidate(word = "1010",m = 10) == [0, 1, 0, 1]
    assert candidate(word = "00000",m = 5) == [1, 1, 1, 1, 1]
    assert candidate(word = "1111111111",m = 11) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
