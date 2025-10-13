# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 2,leftChild = [1, 0],rightChild = [-1, -1]) == False
    assert candidate(n = 3,leftChild = [1, -1, -1],rightChild = [2, -1, -1]) == True
    assert candidate(n = 3,leftChild = [1, 0, -1],rightChild = [-1, -1, -1]) == False
    assert candidate(n = 1,leftChild = [-1],rightChild = [-1]) == True
    assert candidate(n = 4,leftChild = [1, -1, 3, -1],rightChild = [2, -1, -1, -1]) == True
    assert candidate(n = 4,leftChild = [1, -1, 3, -1],rightChild = [2, 3, -1, -1]) == False
    assert candidate(n = 5,leftChild = [1, 2, 3, 4, -1],rightChild = [-1, -1, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, 3, 4, 5, -1],rightChild = [-1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, 3, -1, -1, -1],rightChild = [4, 5, -1, -1, -1, -1]) == True
    assert candidate(n = 3,leftChild = [1, 2, -1],rightChild = [-1, -1, 1]) == False
    assert candidate(n = 5,leftChild = [1, 3, -1, -1, -1],rightChild = [2, 4, -1, -1, -1]) == True
    assert candidate(n = 5,leftChild = [1, 2, -1, -1, -1],rightChild = [3, 4, -1, -1, -1]) == True
    assert candidate(n = 13,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1]) == True
    assert candidate(n = 5,leftChild = [1, 2, -1, -1, -1],rightChild = [3, 4, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, 3, 4, 5, -1],rightChild = [-1, -1, -1, -1, 3, -1]) == False
    assert candidate(n = 5,leftChild = [1, 2, -1, -1, -1],rightChild = [2, -1, -1, -1, -1]) == False
    assert candidate(n = 5,leftChild = [1, -1, 2, 0, -1],rightChild = [-1, 2, -1, -1, -1]) == False
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, -1, -1, 3, 4],rightChild = [-1, -1, 5, -1, -1, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, 3, 4, -1, -1, -1],rightChild = [5, 6, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, -1, -1, -1, -1, -1, -1],rightChild = [5, 6, 7, 8, -1, 9, -1, -1, -1, -1]) == True
    assert candidate(n = 5,leftChild = [1, 2, 3, -1, -1],rightChild = [-1, -1, -1, 4, 0]) == False
    assert candidate(n = 6,leftChild = [1, 2, 3, -1, 5, -1],rightChild = [2, 3, 4, -1, -1, -1]) == False
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, -1, 6, 7, -1],rightChild = [-1, 5, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 5,leftChild = [1, -1, -1, -1, 2],rightChild = [-1, 3, 4, -1, -1]) == False
    assert candidate(n = 6,leftChild = [1, 2, -1, -1, -1, -1],rightChild = [3, 4, 5, 0, -1, -1]) == False
    assert candidate(n = 8,leftChild = [1, 2, 3, -1, -1, -1, -1, -1],rightChild = [-1, -1, -1, 4, -1, 5, 6, 7]) == False
    assert candidate(n = 7,leftChild = [1, 2, -1, -1, -1, -1, -1],rightChild = [-1, -1, 3, 4, 5, 6, -1]) == True
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, 5, -1, 6, 7],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1]) == False
    assert candidate(n = 9,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, 5, 6, 7, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1],rightChild = [-1, 6, 7, -1, -1, 8, -1, -1, 9, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, 3, -1, -1, -1],rightChild = [-1, -1, 4, -1, 5, -1]) == True
    assert candidate(n = 5,leftChild = [1, -1, -1, -1, -1],rightChild = [2, 3, 4, -1, -1]) == True
    assert candidate(n = 8,leftChild = [1, 2, 3, -1, -1, -1, 6, -1],rightChild = [3, 4, 5, -1, -1, -1, -1, -1]) == False
    assert candidate(n = 12,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 9,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, -1],rightChild = [2, 3, 4, 5, 6, 7, 8, -1, -1]) == False
    assert candidate(n = 10,leftChild = [1, 2, -1, -1, 5, 6, 7, 8, 9, -1],rightChild = [-1, 3, 4, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 8,leftChild = [1, 2, 3, -1, -1, -1, -1, -1],rightChild = [2, 3, 4, -1, -1, -1, -1, 7]) == False
    assert candidate(n = 7,leftChild = [1, 2, 3, 4, 5, -1, -1],rightChild = [-1, -1, -1, -1, 6, -1, -1]) == True
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, 5, 6, -1, -1],rightChild = [-1, -1, -1, -1, -1, -1, 7, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, -1, -1, 4, -1],rightChild = [-1, 3, -1, 5, -1, -1]) == False
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, -1, -1, -1, -1, -1],rightChild = [2, 3, 4, 5, 6, -1, -1]) == False
    assert candidate(n = 5,leftChild = [1, 2, -1, -1, -1],rightChild = [3, 4, 2, -1, -1]) == False
    assert candidate(n = 5,leftChild = [1, 3, -1, -1, -1],rightChild = [-1, 2, 4, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, -1, 4, -1, -1],rightChild = [-1, -1, 3, -1, 5, -1]) == True
    assert candidate(n = 9,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, 3, -1, -1, 0],rightChild = [-1, -1, -1, -1, -1, -1]) == False
    assert candidate(n = 5,leftChild = [1, 2, 3, -1, -1],rightChild = [-1, -1, -1, 4, -1]) == True
    assert candidate(n = 8,leftChild = [1, 2, -1, 3, 4, 5, -1, -1],rightChild = [-1, -1, -1, -1, 6, 7, -1, -1]) == False
    assert candidate(n = 11,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1],rightChild = [3, 4, 5, 6, 7, 8, 9, -1, -1, -1]) == False
    assert candidate(n = 6,leftChild = [1, 2, 3, -1, 4, -1],rightChild = [-1, -1, -1, 5, -1, -1]) == False
    assert candidate(n = 8,leftChild = [1, -1, 3, 5, -1, 7, -1, -1],rightChild = [2, 4, 6, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, -1, -1, -1, -1],rightChild = [-1, -1, 3, 4, 5, -1]) == True
    assert candidate(n = 6,leftChild = [1, -1, -1, 2, -1, -1],rightChild = [2, 3, 4, -1, 5, -1]) == False
    assert candidate(n = 6,leftChild = [1, 2, 3, 4, -1, -1],rightChild = [-1, -1, -1, -1, 5, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, -1, -1, -1, -1],rightChild = [3, 4, -1, -1, -1, 5]) == False
    assert candidate(n = 8,leftChild = [1, -1, 2, -1, 3, 4, -1, -1],rightChild = [-1, 5, -1, 6, 7, -1, -1, -1]) == False
    assert candidate(n = 8,leftChild = [1, 2, -1, -1, -1, -1, 6, 7],rightChild = [3, 4, 5, -1, -1, -1, -1, -1]) == False
    assert candidate(n = 6,leftChild = [1, -1, -1, -1, -1, -1],rightChild = [2, 3, 4, 5, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, 3, 4, 5, -1],rightChild = [-1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, -1, -1, -1, -1],rightChild = [5, -1, 6, -1, 7, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, -1, 3, 5, -1, -1],rightChild = [2, 4, -1, -1, -1, -1]) == True
    assert candidate(n = 10,leftChild = [1, -1, 2, -1, 3, -1, 4, -1, 5, -1],rightChild = [2, 3, 4, 5, 6, 7, 8, 9, -1, -1]) == False
    assert candidate(n = 7,leftChild = [1, -1, -1, 5, -1, -1, -1],rightChild = [2, 3, 4, 6, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, -1, -1, -1, -1],rightChild = [3, 4, -1, -1, 5, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, 3, -1, -1, 5, 6],rightChild = [-1, -1, -1, 4, -1, -1, -1]) == False
    assert candidate(n = 5,leftChild = [1, 2, -1, -1, -1],rightChild = [-1, 3, -1, 4, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, -1, 4, 5, -1, -1],rightChild = [-1, -1, -1, -1, -1, 6, -1]) == False
    assert candidate(n = 7,leftChild = [1, 2, -1, -1, 4, -1, -1],rightChild = [3, -1, 5, 6, -1, -1, -1]) == False
    assert candidate(n = 5,leftChild = [1, 2, -1, -1, -1],rightChild = [-1, 3, 4, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, -1, 2, -1, 3, -1],rightChild = [-1, -1, -1, -1, -1, 4]) == False
    assert candidate(n = 10,leftChild = [1, -1, 3, -1, -1, 6, -1, -1, -1, -1],rightChild = [2, 4, 5, 7, 8, 9, -1, -1, -1, -1]) == True
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, -1, -1, -1, 7, -1, 9],rightChild = [-1, -1, -1, -1, 5, 6, 8, -1, -1, -1]) == False
    assert candidate(n = 6,leftChild = [1, 2, -1, -1, -1, -1],rightChild = [3, 4, -1, -1, 5, -1]) == True
    assert candidate(n = 9,leftChild = [1, 2, 3, 4, -1, -1, -1, 7, -1],rightChild = [-1, -1, -1, -1, 5, 6, 8, -1, -1]) == False
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, -1, -1, -1, -1, -1, -1],rightChild = [-1, 5, 6, 7, -1, 8, 9, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, 3, -1, -1, -1],rightChild = [-1, -1, -1, 4, 5, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, 3, -1, -1, -1],rightChild = [2, 3, 4, -1, -1, -1]) == False
    assert candidate(n = 12,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, 3, 4, -1, -1],rightChild = [-1, -1, 5, -1, 3, -1]) == False
    assert candidate(n = 6,leftChild = [1, -1, 3, -1, -1, -1],rightChild = [2, -1, -1, 4, 5, -1]) == True
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, 5, 6, -1, -1, 8, -1],rightChild = [-1, -1, -1, -1, -1, -1, 7, -1, -1, 9]) == False
    assert candidate(n = 7,leftChild = [1, -1, -1, -1, -1, -1, -1],rightChild = [2, 3, 4, 5, 6, -1, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, 3, -1, 5, -1, -1],rightChild = [4, -1, -1, -1, 6, -1, -1]) == True
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, 5, 6, -1, -1],rightChild = [-1, -1, -1, -1, -1, -1, 7, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, -1, -1, -1, -1, -1],rightChild = [3, 4, 5, 6, -1, -1, -1]) == True
    assert candidate(n = 5,leftChild = [1, 2, 3, 4, -1],rightChild = [-1, -1, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, -1, -1, -1, 4],rightChild = [2, -1, 3, -1, 5, -1]) == False
    assert candidate(n = 7,leftChild = [1, 2, 3, 4, -1, -1, -1],rightChild = [5, -1, 4, -1, -1, -1, -1]) == False
    assert candidate(n = 5,leftChild = [1, 2, -1, -1, 4],rightChild = [-1, -1, -1, 3, -1]) == False
    assert candidate(n = 9,leftChild = [1, 2, 3, 4, 5, 6, -1, -1, -1],rightChild = [-1, -1, -1, -1, -1, -1, 7, 8, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, 3, -1, -1, -1, -1],rightChild = [4, 5, 6, -1, -1, -1, -1]) == True
    assert candidate(n = 5,leftChild = [1, 2, -1, 3, -1],rightChild = [4, -1, -1, -1, -1]) == False
    assert candidate(n = 7,leftChild = [1, -1, 2, 3, -1, 4, -1],rightChild = [-1, -1, -1, 5, 6, -1, -1]) == False
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, 5, 6, -1, -1],rightChild = [7, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 9,leftChild = [1, 2, 3, -1, -1, -1, -1, -1, -1],rightChild = [4, 5, 6, 7, 8, -1, -1, -1, -1]) == True
    assert candidate(n = 12,leftChild = [1, 2, -1, 4, -1, 6, -1, -1, 8, -1, -1, -1],rightChild = [-1, 3, 5, -1, 7, -1, 9, -1, 10, -1, 11, -1]) == False
    assert candidate(n = 5,leftChild = [1, -1, -1, -1, -1],rightChild = [2, -1, 3, -1, 4]) == False
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, 5, 6, 7, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, -1, 9],rightChild = [2, -1, -1, -1, 5, 6, -1, -1, 9, -1]) == False
    assert candidate(n = 8,leftChild = [1, 2, -1, -1, -1, -1, -1, -1],rightChild = [2, 3, 4, 5, 6, 7, -1, -1]) == False
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, -1, -1, -1, -1],rightChild = [-1, -1, -1, -1, 5, 6, 7, -1]) == True
    assert candidate(n = 5,leftChild = [1, -1, -1, -1, -1],rightChild = [2, 3, 4, -1, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, 3, 4, 5, -1, -1],rightChild = [-1, -1, -1, 6, -1, -1, -1]) == True
    assert candidate(n = 9,leftChild = [1, 2, -1, 4, -1, -1, 7, -1, -1],rightChild = [-1, 3, -1, -1, 5, 6, -1, -1, 8]) == False
    assert candidate(n = 8,leftChild = [1, 2, -1, -1, -1, -1, -1, -1],rightChild = [3, 4, 5, 6, 7, -1, -1, -1]) == True
    assert candidate(n = 5,leftChild = [1, 2, -1, -1, -1],rightChild = [2, 4, 3, -1, -1]) == False
    assert candidate(n = 10,leftChild = [1, 2, -1, -1, -1, -1, -1, -1, -1, -1],rightChild = [3, 4, 5, 6, 7, 8, 9, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, -1, 2, -1, -1, -1],rightChild = [2, -1, 3, 4, 5, -1]) == False
    assert candidate(n = 5,leftChild = [1, 2, -1, 4, -1],rightChild = [-1, -1, 3, -1, -1]) == True
    assert candidate(n = 10,leftChild = [1, 2, -1, -1, 3, 4, -1, 5, 6, -1],rightChild = [-1, -1, -1, 3, 5, 6, 7, 8, 9, -1]) == False
    assert candidate(n = 8,leftChild = [1, 2, -1, -1, -1, 3, 5, -1],rightChild = [4, -1, -1, -1, 6, -1, 7, -1]) == True
    assert candidate(n = 8,leftChild = [1, -1, -1, 4, -1, -1, -1, -1],rightChild = [2, 3, 5, -1, 6, 7, -1, -1]) == True
    assert candidate(n = 9,leftChild = [1, 2, 3, 4, 5, 6, -1, 8, -1],rightChild = [-1, -1, -1, -1, -1, -1, 7, -1, -1]) == True
    assert candidate(n = 11,leftChild = [1, 2, -1, 4, 5, 6, -1, 8, -1, -1, -1],rightChild = [-1, 3, -1, 7, -1, -1, 9, -1, 10, -1, -1]) == True
    assert candidate(n = 8,leftChild = [1, 2, -1, -1, -1, 6, 7, -1],rightChild = [-1, -1, 3, 4, 5, -1, -1, -1]) == True
    assert candidate(n = 9,leftChild = [1, 2, -1, 4, 5, -1, -1, -1, -1],rightChild = [-1, -1, 3, -1, -1, 6, -1, -1, 7]) == False
    assert candidate(n = 8,leftChild = [1, 2, -1, 3, 4, 5, 6, -1],rightChild = [-1, -1, -1, -1, -1, 7, -1, -1]) == False
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, -1, -1, 6, 7],rightChild = [5, -1, -1, -1, -1, -1, -1, -1]) == False
    assert candidate(n = 6,leftChild = [1, 2, 3, 4, -1, -1],rightChild = [5, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 10,leftChild = [1, -1, 2, 3, -1, 4, 5, 6, 7, 8],rightChild = [-1, 2, 3, -1, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(n = 5,leftChild = [1, -1, -1, -1, -1],rightChild = [-1, 2, 3, 4, -1]) == True
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1],rightChild = [2, 3, 4, 5, 6, 7, 8, 9, -1, -1]) == False
    assert candidate(n = 7,leftChild = [1, 2, -1, -1, -1, 5, 6],rightChild = [2, -1, 3, 4, -1, -1, -1]) == False
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, 5, -1, 6, 7, 8, -1],rightChild = [-1, -1, -1, -1, 9, -1, -1, -1, -1, -1]) == False
    assert candidate(n = 8,leftChild = [1, 2, 3, 4, -1, 6, 7, -1],rightChild = [5, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, 3, 4, 5, 6, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 7,leftChild = [1, 2, 3, 4, 5, -1, -1],rightChild = [-1, 6, -1, -1, -1, -1, -1]) == True
    assert candidate(n = 4,leftChild = [1, -1, -1, -1],rightChild = [2, 3, 0, -1]) == False
    assert candidate(n = 6,leftChild = [1, -1, 3, -1, -1, 4],rightChild = [2, 5, -1, -1, -1, -1]) == True
    assert candidate(n = 11,leftChild = [1, 2, 3, 4, -1, -1, -1, -1, -1, -1, -1],rightChild = [5, 6, 7, 8, 9, -1, 10, -1, -1, -1, -1]) == True
    assert candidate(n = 6,leftChild = [1, 2, -1, -1, -1, 4],rightChild = [3, -1, -1, -1, 5, -1]) == False
    assert candidate(n = 6,leftChild = [1, -1, 2, 3, -1, -1],rightChild = [-1, -1, -1, 4, -1, 5]) == False
    assert candidate(n = 10,leftChild = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1],rightChild = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0]) == False
