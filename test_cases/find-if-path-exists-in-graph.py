# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 1,edges = [],source = 0,destination = 0) == True
    assert candidate(n = 100,edges = [],source = 0,destination = 99) == False
    assert candidate(n = 25,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 0]],source = 15,destination = 10) == True
    assert candidate(n = 15,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],source = 14,destination = 0) == True
