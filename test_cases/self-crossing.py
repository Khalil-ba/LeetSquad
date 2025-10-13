# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(distance = [3, 5, 3, 4, 3, 4]) == True
    assert candidate(distance = [3, 3, 3, 2, 1]) == False
    assert candidate(distance = [1, 2, 3, 4, 1, 2, 3, 4]) == True
    assert candidate(distance = [1, 1, 1, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(distance = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(distance = [3, 3, 3, 2, 1, 1]) == False
    assert candidate(distance = [1, 1, 1, 1, 1, 1]) == True
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(distance = [1, 2, 2, 3, 4, 4, 5, 5]) == False
    assert candidate(distance = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]) == True
    assert candidate(distance = [6, 6, 6, 6, 6, 1]) == True
    assert candidate(distance = [3, 3, 3, 2, 2, 3, 4]) == True
    assert candidate(distance = [1, 2, 3, 4]) == False
    assert candidate(distance = [1, 2, 3, 4, 5, 6]) == False
    assert candidate(distance = [2, 1, 1, 2]) == True
    assert candidate(distance = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8]) == False
    assert candidate(distance = [5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(distance = [1, 2, 3, 4, 5]) == False
    assert candidate(distance = [1, 1, 2, 2, 3, 3]) == False
    assert candidate(distance = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == False
    assert candidate(distance = [10, 2, 10, 1, 10, 2, 10]) == True
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 3, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 2, 3, 4, 5, 4, 3, 2, 1, 1]) == True
    assert candidate(distance = [10, 10, 1, 1, 10, 10, 1, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [3, 1, 3, 1, 3, 1, 3]) == True
    assert candidate(distance = [1, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == True
    assert candidate(distance = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2]) == True
    assert candidate(distance = [1, 3, 2, 2, 1, 1, 1, 1, 1]) == True
    assert candidate(distance = [10, 1, 1, 10, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 1]) == False
    assert candidate(distance = [3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == True
    assert candidate(distance = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1]) == True
    assert candidate(distance = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(distance = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == True
    assert candidate(distance = [1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 1]) == False
    assert candidate(distance = [5, 5, 5, 5, 1, 5, 5, 5, 5, 1, 5, 5, 5, 5, 1, 5, 5, 5, 5, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [5, 10, 10, 5, 5, 10, 10, 5, 5, 10, 10]) == True
    assert candidate(distance = [1, 2, 3, 4, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == True
    assert candidate(distance = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2]) == True
    assert candidate(distance = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == True
    assert candidate(distance = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == False
    assert candidate(distance = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1]) == False
    assert candidate(distance = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19]) == False
    assert candidate(distance = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11]) == True
    assert candidate(distance = [5, 5, 1, 1, 5, 5, 1, 1, 5, 5, 1, 1, 5, 5, 1, 1]) == True
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(distance = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7]) == True
    assert candidate(distance = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(distance = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == True
    assert candidate(distance = [3, 3, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1]) == False
    assert candidate(distance = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == True
    assert candidate(distance = [2, 3, 1, 4, 3, 2, 1]) == True
    assert candidate(distance = [8, 2, 8, 2, 8, 2, 8, 2, 8, 2]) == True
    assert candidate(distance = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 5, 5, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(distance = [5, 1, 2, 3, 4, 5, 6, 4, 3, 2, 1]) == True
    assert candidate(distance = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1]) == False
    assert candidate(distance = [2, 3, 1, 1, 2, 1, 1, 2, 3, 2]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [10, 10, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 3, 3, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == False
    assert candidate(distance = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(distance = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == True
    assert candidate(distance = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False
    assert candidate(distance = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(distance = [5, 6, 7, 8, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1]) == False
    assert candidate(distance = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]) == True
    assert candidate(distance = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == True
    assert candidate(distance = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == False
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(distance = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(distance = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 1, 1, 1, 1]) == True
    assert candidate(distance = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == True
    assert candidate(distance = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(distance = [5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 5, 5, 5]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 100]) == False
    assert candidate(distance = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(distance = [1, 3, 3, 2, 1, 2, 1]) == True
    assert candidate(distance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8]) == True
    assert candidate(distance = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(distance = [5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
