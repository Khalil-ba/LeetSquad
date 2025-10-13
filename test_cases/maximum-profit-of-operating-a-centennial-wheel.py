# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(customers = [50, 50, 50, 50, 50],boardingCost = 100,runningCost = 1) == 63
    assert candidate(customers = [5, 5, 0, 8, 2],boardingCost = 6,runningCost = 3) == 6
    assert candidate(customers = [0, 0, 0, 0, 0],boardingCost = 1,runningCost = 1) == -1
    assert candidate(customers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],boardingCost = 1,runningCost = 2) == -1
    assert candidate(customers = [0, 0, 0, 0],boardingCost = 10,runningCost = 5) == -1
    assert candidate(customers = [10, 9, 6],boardingCost = 6,runningCost = 4) == 7
    assert candidate(customers = [0, 0, 0, 0],boardingCost = 10,runningCost = 1) == -1
    assert candidate(customers = [8, 3],boardingCost = 5,runningCost = 6) == 3
    assert candidate(customers = [0, 0, 0, 0, 0],boardingCost = 1,runningCost = 10) == -1
    assert candidate(customers = [0, 0, 0, 0, 0],boardingCost = 5,runningCost = 1) == -1
    assert candidate(customers = [50, 50, 50, 50],boardingCost = 2,runningCost = 1) == 50
    assert candidate(customers = [50, 50, 50, 50, 50],boardingCost = 10,runningCost = 1) == 63
    assert candidate(customers = [3, 4, 0, 5, 1],boardingCost = 1,runningCost = 92) == -1
    assert candidate(customers = [5, 5, 0, 8, 7, 1, 4, 7, 3, 23],boardingCost = 43,runningCost = 59) == 16
    assert candidate(customers = [10, 10, 10, 10, 10],boardingCost = 5,runningCost = 4) == 13
    assert candidate(customers = [50, 50, 50, 50, 50],boardingCost = 100,runningCost = 50) == 63
    assert candidate(customers = [49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49],boardingCost = 1,runningCost = 1) == 343
    assert candidate(customers = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],boardingCost = 5,runningCost = 3) == 13
    assert candidate(customers = [0, 10, 0, 10, 0, 10, 0, 10, 0, 10],boardingCost = 1,runningCost = 99) == -1
    assert candidate(customers = [50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0],boardingCost = 10,runningCost = 20) == 125
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],boardingCost = 1,runningCost = 2) == 54
    assert candidate(customers = [10, 0, 0, 10, 0, 0, 10, 0, 0, 10],boardingCost = 6,runningCost = 4) == 12
    assert candidate(customers = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],boardingCost = 3,runningCost = 15) == -1
    assert candidate(customers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],boardingCost = 2,runningCost = 1) == 13
    assert candidate(customers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 100],boardingCost = 5,runningCost = 4) == 34
    assert candidate(customers = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],boardingCost = 5,runningCost = 8) == 50
    assert candidate(customers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],boardingCost = 2,runningCost = 3) == 53
    assert candidate(customers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],boardingCost = 1,runningCost = 1) == -1
    assert candidate(customers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],boardingCost = 10,runningCost = 5) == 138
    assert candidate(customers = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100],boardingCost = 5,runningCost = 1) == 35
    assert candidate(customers = [10, 20, 30, 40, 50],boardingCost = 50,runningCost = 1) == 38
    assert candidate(customers = [10, 20, 15, 5, 25],boardingCost = 4,runningCost = 7) == 19
    assert candidate(customers = [20, 10, 0, 30, 10, 0, 40, 10, 0, 50],boardingCost = 20,runningCost = 10) == 43
    assert candidate(customers = [30, 0, 10, 40, 20],boardingCost = 3,runningCost = 5) == 25
    assert candidate(customers = [50, 0, 50, 0, 50, 0, 50, 0, 50, 0],boardingCost = 10,runningCost = 5) == 63
    assert candidate(customers = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 100, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5],boardingCost = 10,runningCost = 20) == 337
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],boardingCost = 1,runningCost = 5) == -1
    assert candidate(customers = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],boardingCost = 1,runningCost = 1) == 10
    assert candidate(customers = [30, 20, 10, 0, 0, 0, 0, 0, 0, 0],boardingCost = 3,runningCost = 10) == 15
    assert candidate(customers = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90],boardingCost = 15,runningCost = 12) == 169
    assert candidate(customers = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0],boardingCost = 1,runningCost = 2) == 25
    assert candidate(customers = [10, 20, 30, 40, 50],boardingCost = 1,runningCost = 95) == -1
    assert candidate(customers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],boardingCost = 5,runningCost = 4) == 145
    assert candidate(customers = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25],boardingCost = 2,runningCost = 3) == 63
    assert candidate(customers = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0],boardingCost = 10,runningCost = 90) == -1
    assert candidate(customers = [4, 3, 2, 1, 0, 0, 0, 0, 0, 0],boardingCost = 50,runningCost = 2) == 4
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],boardingCost = 10,runningCost = 20) == 15
    assert candidate(customers = [40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40],boardingCost = 1,runningCost = 1) == 200
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],boardingCost = 2,runningCost = 3) == 15
    assert candidate(customers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],boardingCost = 5,runningCost = 4) == 25
    assert candidate(customers = [2, 5, 3, 1, 4, 6, 2, 3, 5, 1, 4, 2, 3, 6, 5, 1, 4, 2, 3, 6, 5],boardingCost = 3,runningCost = 5) == 22
    assert candidate(customers = [15, 25, 35, 45, 55],boardingCost = 10,runningCost = 8) == 44
    assert candidate(customers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],boardingCost = 5,runningCost = 4) == 20
    assert candidate(customers = [50, 25, 50, 25, 50, 25, 50, 25, 50, 25],boardingCost = 4,runningCost = 10) == 94
    assert candidate(customers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],boardingCost = 5,runningCost = 6) == -1
