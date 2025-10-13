# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(piles = [5, 3, 1]) == True
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7]) == False
    assert candidate(piles = [7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(piles = [1, 2, 3]) == False
    assert candidate(piles = [1]) == True
    assert candidate(piles = [1, 3, 5, 7]) == False
    assert candidate(piles = [3, 3, 3, 3]) == False
    assert candidate(piles = [2, 2, 2]) == True
    assert candidate(piles = [1, 2, 3, 4]) == True
    assert candidate(piles = [7, 7, 7]) == True
    assert candidate(piles = [2, 2, 2, 2]) == False
    assert candidate(piles = [7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(piles = [4, 1, 2]) == True
    assert candidate(piles = [4, 4, 4, 4]) == False
    assert candidate(piles = [1, 1]) == False
    assert candidate(piles = [2, 2, 2, 2, 2, 2, 2]) == True
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 7]) == True
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 2]) == True
    assert candidate(piles = [7, 1, 3, 5, 2]) == True
    assert candidate(piles = [2, 2, 2, 2, 2, 2]) == False
    assert candidate(piles = [4, 2, 1, 3]) == True
    assert candidate(piles = [2, 4, 6]) == False
    assert candidate(piles = [1, 2, 2, 3, 3, 4]) == True
    assert candidate(piles = [1, 2, 2, 3, 4, 5, 6]) == True
    assert candidate(piles = [1, 1, 2, 2, 3, 3, 4]) == True
    assert candidate(piles = [1, 3, 3]) == True
    assert candidate(piles = [1, 2, 3, 4, 3, 2, 1]) == True
    assert candidate(piles = [1, 1, 1, 1, 1, 1]) == False
    assert candidate(piles = [4, 4, 4, 4, 4, 4, 4]) == True
    assert candidate(piles = [2, 3, 5, 7, 11]) == True
    assert candidate(piles = [2, 3, 4, 5, 6]) == True
    assert candidate(piles = [2, 2, 2, 2, 2, 2, 1]) == True
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13]) == True
    assert candidate(piles = [7, 7, 7, 7]) == False
    assert candidate(piles = [4, 5, 6, 7, 1]) == True
    assert candidate(piles = [5, 4, 3, 2, 1, 1, 1]) == True
    assert candidate(piles = [1, 2, 2, 3, 4, 4, 5]) == True
    assert candidate(piles = [1, 3, 5]) == True
    assert candidate(piles = [4, 4, 4, 3, 3, 2, 1]) == True
    assert candidate(piles = [7, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(piles = [5, 5, 5, 5, 1]) == True
    assert candidate(piles = [7, 7, 5, 5, 3, 3, 1]) == True
    assert candidate(piles = [5, 5, 5, 4, 4, 3]) == True
    assert candidate(piles = [3, 3, 2, 2, 1, 1]) == False
    assert candidate(piles = [2, 3, 3, 2]) == False
    assert candidate(piles = [6, 5, 4, 3, 2, 1]) == True
    assert candidate(piles = [1, 1, 1, 1, 2, 2, 2]) == True
    assert candidate(piles = [4, 4, 3, 3, 2, 2, 1]) == True
    assert candidate(piles = [3, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(piles = [6, 6, 6, 1, 1]) == True
    assert candidate(piles = [6, 3, 5, 2, 4, 1, 7]) == False
    assert candidate(piles = [6, 5, 4, 3, 2, 1, 1]) == True
    assert candidate(piles = [7, 1, 2, 3, 4, 5, 6]) == False
    assert candidate(piles = [5, 5, 5, 5, 1]) == True
    assert candidate(piles = [4, 4, 4, 1]) == True
    assert candidate(piles = [7, 1, 2, 3, 4, 5, 6]) == False
    assert candidate(piles = [3, 3, 2, 1]) == True
    assert candidate(piles = [6, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(piles = [5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(piles = [2, 2, 2, 2, 1]) == True
    assert candidate(piles = [1, 3, 5, 7]) == False
    assert candidate(piles = [6, 3, 1, 4]) == False
    assert candidate(piles = [1, 2, 2, 3, 4, 5, 6]) == True
    assert candidate(piles = [3, 5, 5, 5]) == True
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(piles = [1, 2, 2, 1, 1]) == True
    assert candidate(piles = [4, 4, 4, 4, 4, 4, 3]) == True
    assert candidate(piles = [1, 1, 2, 3, 4]) == True
    assert candidate(piles = [7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(piles = [3, 3, 3, 3, 3, 3, 3]) == True
    assert candidate(piles = [2, 4, 6]) == False
    assert candidate(piles = [6, 3, 4, 2, 1]) == True
    assert candidate(piles = [3, 3, 3, 3, 3]) == True
    assert candidate(piles = [7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(piles = [6, 3, 1, 2, 5]) == True
    assert candidate(piles = [4, 3, 2, 2, 2, 2, 2]) == True
    assert candidate(piles = [1, 3, 3, 3]) == True
    assert candidate(piles = [3, 3, 3, 1, 1]) == True
    assert candidate(piles = [6, 6, 6, 6, 6, 6, 6]) == True
