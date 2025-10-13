# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [50, 50],experience = [50, 50]) == 52
    assert candidate(initialEnergy = 5,initialExperience = 3,energy = [1, 4, 3, 2],experience = [2, 6, 3, 1]) == 8
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [100],experience = [100]) == 200
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [50, 25, 25],experience = [50, 25, 25]) == 1
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 20, 30],experience = [10, 20, 30]) == 11
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [100],experience = [100]) == 2
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [50, 50],experience = [50, 50]) == 1
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [1, 1, 1, 1],experience = [1, 1, 1, 1]) == 0
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],experience = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(initialEnergy = 2,initialExperience = 4,energy = [1],experience = [3]) == 0
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [1, 1, 1, 1],experience = [1, 1, 1, 1]) == 5
    assert candidate(initialEnergy = 99,initialExperience = 99,energy = [100],experience = [100]) == 4
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],experience = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 71
    assert candidate(initialEnergy = 50,initialExperience = 25,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],experience = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 6
    assert candidate(initialEnergy = 30,initialExperience = 25,energy = [10, 15, 20, 5, 10],experience = [20, 15, 10, 25, 15]) == 31
    assert candidate(initialEnergy = 40,initialExperience = 40,energy = [20, 20, 20, 20],experience = [20, 20, 20, 20]) == 41
    assert candidate(initialEnergy = 30,initialExperience = 20,energy = [10, 20, 30, 40, 50],experience = [1, 2, 3, 4, 5]) == 121
    assert candidate(initialEnergy = 15,initialExperience = 8,energy = [7, 7, 7, 7, 7, 7],experience = [6, 6, 6, 6, 6, 6]) == 28
    assert candidate(initialEnergy = 70,initialExperience = 40,energy = [5, 15, 25, 35, 45],experience = [45, 35, 25, 15, 5]) == 62
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],experience = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 135
    assert candidate(initialEnergy = 2,initialExperience = 2,energy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],experience = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(initialEnergy = 20,initialExperience = 25,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],experience = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(initialEnergy = 10,initialExperience = 5,energy = [5, 6, 7, 8],experience = [1, 2, 3, 4]) == 17
    assert candidate(initialEnergy = 20,initialExperience = 5,energy = [10, 15, 5, 20],experience = [3, 7, 10, 2]) == 31
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 20, 30, 40],experience = [5, 15, 25, 35]) == 51
    assert candidate(initialEnergy = 40,initialExperience = 25,energy = [10, 15, 10, 20, 15, 25],experience = [25, 20, 15, 10, 25, 20]) == 57
    assert candidate(initialEnergy = 30,initialExperience = 30,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],experience = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 181
    assert candidate(initialEnergy = 10,initialExperience = 20,energy = [1, 3, 5, 7, 9],experience = [9, 7, 5, 3, 1]) == 16
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 51
    assert candidate(initialEnergy = 50,initialExperience = 30,energy = [40, 35, 20, 10, 5],experience = [25, 20, 15, 10, 5]) == 61
    assert candidate(initialEnergy = 70,initialExperience = 30,energy = [20, 10, 30, 5, 20],experience = [15, 25, 10, 20, 5]) == 16
    assert candidate(initialEnergy = 20,initialExperience = 15,energy = [10, 20, 30],experience = [5, 15, 25]) == 41
    assert candidate(initialEnergy = 1,initialExperience = 10,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9],experience = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(initialEnergy = 20,initialExperience = 15,energy = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],experience = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5]) == 76
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [25, 25, 25, 25],experience = [20, 20, 20, 20]) == 51
    assert candidate(initialEnergy = 15,initialExperience = 10,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],experience = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 42
    assert candidate(initialEnergy = 25,initialExperience = 15,energy = [8, 7, 6, 5, 4, 3, 2, 1],experience = [1, 2, 3, 4, 5, 6, 7, 8]) == 12
    assert candidate(initialEnergy = 5,initialExperience = 5,energy = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],experience = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 26
    assert candidate(initialEnergy = 10,initialExperience = 15,energy = [3, 2, 6, 1],experience = [8, 4, 2, 7]) == 3
    assert candidate(initialEnergy = 20,initialExperience = 25,energy = [10, 10, 10, 10],experience = [25, 26, 27, 28]) == 22
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [5, 15, 25, 35],experience = [30, 20, 10, 5]) == 92
    assert candidate(initialEnergy = 30,initialExperience = 30,energy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],experience = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 0
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],experience = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 47
    assert candidate(initialEnergy = 30,initialExperience = 50,energy = [10, 20, 30],experience = [25, 20, 15]) == 31
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],experience = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 91
    assert candidate(initialEnergy = 15,initialExperience = 20,energy = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]) == 46
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [20, 30, 40, 50, 60, 70, 80, 90, 100],experience = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 441
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [10, 20, 30, 40, 50],experience = [1, 2, 3, 4, 5]) == 141
    assert candidate(initialEnergy = 25,initialExperience = 25,energy = [20, 15, 10, 5],experience = [5, 10, 15, 20]) == 26
    assert candidate(initialEnergy = 30,initialExperience = 20,energy = [15, 25, 10],experience = [10, 15, 25]) == 21
    assert candidate(initialEnergy = 50,initialExperience = 30,energy = [10, 20, 15, 25],experience = [5, 25, 20, 30]) == 21
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [99, 98, 97, 96, 95],experience = [95, 96, 97, 98, 99]) == 580
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [10, 20, 30, 40],experience = [40, 30, 20, 10]) == 140
    assert candidate(initialEnergy = 10,initialExperience = 5,energy = [3, 2, 6, 1],experience = [5, 4, 3, 2]) == 4
    assert candidate(initialEnergy = 5,initialExperience = 5,energy = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],experience = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 26
    assert candidate(initialEnergy = 5,initialExperience = 5,energy = [1, 2, 3, 4, 5],experience = [5, 4, 3, 2, 1]) == 12
    assert candidate(initialEnergy = 60,initialExperience = 30,energy = [20, 20, 20, 20, 20],experience = [20, 20, 20, 20, 20]) == 41
    assert candidate(initialEnergy = 75,initialExperience = 40,energy = [40, 30, 20, 10, 5],experience = [50, 40, 30, 20, 10]) == 42
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [25, 10, 10, 5],experience = [20, 25, 30, 10]) == 1
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],experience = [51, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 408
    assert candidate(initialEnergy = 10,initialExperience = 5,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],experience = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 52
    assert candidate(initialEnergy = 20,initialExperience = 10,energy = [25, 15, 5, 10, 20],experience = [30, 20, 10, 5, 15]) == 77
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],experience = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 947
    assert candidate(initialEnergy = 1,initialExperience = 100,energy = [0, 0, 0, 0],experience = [99, 98, 97, 96]) == 0
    assert candidate(initialEnergy = 30,initialExperience = 30,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],experience = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 26
    assert candidate(initialEnergy = 5,initialExperience = 3,energy = [1, 2, 3, 4, 5],experience = [5, 4, 3, 2, 1]) == 14
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [5, 6, 7, 8],experience = [15, 14, 13, 12]) == 23
    assert candidate(initialEnergy = 80,initialExperience = 60,energy = [15, 20, 25, 30, 35],experience = [65, 70, 75, 80, 85]) == 52
    assert candidate(initialEnergy = 40,initialExperience = 30,energy = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],experience = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 61
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [50, 30, 20],experience = [20, 30, 50]) == 1
    assert candidate(initialEnergy = 25,initialExperience = 25,energy = [13, 14, 15, 16, 17],experience = [17, 16, 15, 14, 13]) == 51
    assert candidate(initialEnergy = 30,initialExperience = 30,energy = [29, 28, 27, 26, 25],experience = [25, 26, 27, 28, 29]) == 106
    assert candidate(initialEnergy = 20,initialExperience = 20,energy = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 31
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [50, 25, 12, 6, 3, 1],experience = [1, 3, 6, 12, 25, 50]) == 0
    assert candidate(initialEnergy = 80,initialExperience = 70,energy = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 471
    assert candidate(initialEnergy = 100,initialExperience = 1,energy = [99, 99, 99],experience = [98, 97, 96]) == 296
    assert candidate(initialEnergy = 10,initialExperience = 15,energy = [3, 4, 5, 6, 7],experience = [5, 6, 7, 8, 9]) == 16
    assert candidate(initialEnergy = 20,initialExperience = 10,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],experience = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 37
    assert candidate(initialEnergy = 50,initialExperience = 20,energy = [25, 25, 25, 25],experience = [15, 15, 15, 15]) == 51
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 20, 30, 40],experience = [40, 30, 20, 10]) == 51
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],experience = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 212
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [50, 40, 30, 20, 10],experience = [10, 20, 30, 40, 50]) == 51
    assert candidate(initialEnergy = 60,initialExperience = 25,energy = [20, 20, 20, 20],experience = [15, 25, 35, 45]) == 21
    assert candidate(initialEnergy = 60,initialExperience = 40,energy = [10, 20, 30, 40],experience = [40, 30, 20, 10]) == 42
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],experience = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 20, 30, 40],experience = [45, 35, 25, 15]) == 51
    assert candidate(initialEnergy = 3,initialExperience = 4,energy = [2, 5, 7, 8],experience = [5, 3, 6, 10]) == 22
    assert candidate(initialEnergy = 50,initialExperience = 10,energy = [30, 20, 10, 5, 25],experience = [15, 25, 5, 10, 30]) == 47
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [99, 1, 1],experience = [1, 99, 1]) == 199
    assert candidate(initialEnergy = 20,initialExperience = 20,energy = [10, 20, 30, 40],experience = [15, 15, 15, 15]) == 81
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [99, 99, 99, 99],experience = [99, 99, 99, 99]) == 297
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [90, 80, 70, 60, 50, 40, 30, 20, 10],experience = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 459
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [25, 25, 25, 25],experience = [20, 30, 20, 30]) == 51
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [10, 10, 10, 10],experience = [11, 12, 13, 14]) == 33
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [10, 20, 30, 40, 50],experience = [50, 40, 30, 20, 10]) == 200
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [1, 3, 2, 4, 5, 3, 2, 1],experience = [2, 1, 3, 2, 1, 4, 3, 2]) == 23
    assert candidate(initialEnergy = 100,initialExperience = 1,energy = [98, 1, 0, 0, 0],experience = [98, 1, 0, 0, 0]) == 98
    assert candidate(initialEnergy = 30,initialExperience = 25,energy = [5, 15, 25, 35, 45],experience = [40, 35, 30, 25, 20]) == 112
    assert candidate(initialEnergy = 20,initialExperience = 10,energy = [5, 10, 15, 20],experience = [8, 6, 4, 2]) == 31
    assert candidate(initialEnergy = 50,initialExperience = 30,energy = [10, 20, 30, 40],experience = [20, 30, 40, 50]) == 51
    assert candidate(initialEnergy = 15,initialExperience = 20,energy = [3, 3, 3, 3, 3],experience = [1, 2, 3, 4, 5]) == 1
    assert candidate(initialEnergy = 10,initialExperience = 50,energy = [25, 25, 25, 25],experience = [51, 52, 53, 54]) == 93
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [10, 20, 30],experience = [30, 20, 10]) == 90
    assert candidate(initialEnergy = 50,initialExperience = 100,energy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],experience = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 6
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [1, 2, 3, 4, 5],experience = [1, 2, 3, 4, 5]) == 16
    assert candidate(initialEnergy = 30,initialExperience = 15,energy = [5, 10, 15, 20, 25],experience = [10, 15, 20, 25, 30]) == 46
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [25, 25, 25, 25],experience = [25, 25, 25, 25]) == 51
    assert candidate(initialEnergy = 60,initialExperience = 60,energy = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],experience = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 532
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [5, 5, 5, 5],experience = [5, 5, 5, 5]) == 11
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 56
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 20, 30],experience = [15, 25, 35]) == 11
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [5, 5, 5, 5, 5],experience = [1, 2, 3, 4, 5]) == 16
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [1, 1, 1],experience = [1, 1, 1]) == 4
    assert candidate(initialEnergy = 1,initialExperience = 100,energy = [1, 1, 1],experience = [1, 1, 1]) == 3
    assert candidate(initialEnergy = 1,initialExperience = 50,energy = [50, 50, 50, 50],experience = [1, 1, 1, 1]) == 200
    assert candidate(initialEnergy = 100,initialExperience = 1,energy = [100],experience = [1]) == 2
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [50, 25, 25],experience = [50, 25, 25]) == 1
    assert candidate(initialEnergy = 5,initialExperience = 5,energy = [2, 3, 4],experience = [4, 3, 2]) == 5
    assert candidate(initialEnergy = 30,initialExperience = 30,energy = [10, 20, 10],experience = [5, 15, 10]) == 11
    assert candidate(initialEnergy = 15,initialExperience = 15,energy = [5, 5, 5],experience = [5, 5, 5]) == 1
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 20, 30, 40],experience = [10, 20, 30, 40]) == 51
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [50, 50],experience = [50, 50]) == 52
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [1, 1, 1, 1],experience = [1, 1, 1, 1]) == 5
    assert candidate(initialEnergy = 20,initialExperience = 20,energy = [5, 5, 5, 5, 5],experience = [5, 5, 5, 5, 5]) == 6
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [50, 40, 30],experience = [30, 40, 50]) == 71
    assert candidate(initialEnergy = 50,initialExperience = 1,energy = [25, 25, 25],experience = [25, 25, 25]) == 51
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [5, 4, 3, 2, 1],experience = [1, 2, 3, 4, 5]) == 16
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [10, 10, 10],experience = [10, 10, 10]) == 22
    assert candidate(initialEnergy = 50,initialExperience = 1,energy = [1, 1, 1, 1],experience = [50, 50, 50, 50]) == 50
    assert candidate(initialEnergy = 1,initialExperience = 100,energy = [1],experience = [100]) == 2
    assert candidate(initialEnergy = 20,initialExperience = 20,energy = [10, 10, 10],experience = [10, 10, 10]) == 11
    assert candidate(initialEnergy = 100,initialExperience = 1,energy = [99, 98, 97],experience = [97, 98, 99]) == 292
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 10, 10, 10, 10],experience = [10, 10, 10, 10, 10]) == 1
    assert candidate(initialEnergy = 1,initialExperience = 100,energy = [1, 1, 1, 1],experience = [1, 1, 1, 1]) == 4
    assert candidate(initialEnergy = 5,initialExperience = 5,energy = [3, 2, 1],experience = [1, 2, 3]) == 2
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],experience = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(initialEnergy = 5,initialExperience = 5,energy = [10, 10, 10],experience = [10, 10, 10]) == 32
    assert candidate(initialEnergy = 30,initialExperience = 10,energy = [10, 10, 10],experience = [5, 5, 5]) == 1
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],experience = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [1, 2, 3, 4, 5],experience = [5, 4, 3, 2, 1]) == 6
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [25, 25, 25, 25],experience = [25, 25, 25, 25]) == 51
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [1, 2, 3, 4, 5],experience = [5, 4, 3, 2, 1]) == 6
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],experience = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 20, 30],experience = [15, 25, 35]) == 11
    assert candidate(initialEnergy = 10,initialExperience = 1,energy = [2, 3, 4, 5],experience = [3, 4, 5, 6]) == 8
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [10, 20, 30],experience = [30, 20, 10]) == 0
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [50, 30],experience = [40, 60]) == 0
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [5, 5, 5, 5],experience = [5, 5, 5, 5]) == 11
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [1, 2, 3],experience = [1, 2, 3]) == 7
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [1, 1, 1, 1],experience = [1, 1, 1, 1]) == 0
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [10, 9, 8, 7],experience = [7, 8, 9, 10]) == 25
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [50, 25, 25],experience = [50, 25, 25]) == 52
    assert candidate(initialEnergy = 3,initialExperience = 3,energy = [1, 1, 1, 1],experience = [1, 1, 1, 1]) == 2
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [50, 50, 50],experience = [50, 50, 50]) == 102
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [50, 50, 50],experience = [30, 30, 30]) == 51
    assert candidate(initialEnergy = 20,initialExperience = 20,energy = [10, 10],experience = [10, 10]) == 1
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [10, 10, 10],experience = [10, 10, 10]) == 22
    assert candidate(initialEnergy = 10,initialExperience = 1,energy = [10, 10, 10],experience = [1, 1, 1]) == 22
    assert candidate(initialEnergy = 30,initialExperience = 10,energy = [15, 15, 15],experience = [5, 5, 5]) == 16
    assert candidate(initialEnergy = 60,initialExperience = 50,energy = [30, 20, 10],experience = [10, 20, 30]) == 1
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 20, 30],experience = [5, 15, 25]) == 11
    assert candidate(initialEnergy = 1,initialExperience = 1,energy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],experience = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    assert candidate(initialEnergy = 100,initialExperience = 100,energy = [50, 40, 30],experience = [10, 20, 30]) == 21
    assert candidate(initialEnergy = 3,initialExperience = 3,energy = [1, 1, 3, 3],experience = [3, 3, 1, 1]) == 7
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [10, 20, 30],experience = [5, 15, 25]) == 11
    assert candidate(initialEnergy = 1,initialExperience = 50,energy = [25, 25, 25],experience = [25, 25, 25]) == 75
    assert candidate(initialEnergy = 100,initialExperience = 1,energy = [1, 1, 1],experience = [1, 1, 1]) == 1
    assert candidate(initialEnergy = 50,initialExperience = 50,energy = [50],experience = [50]) == 2
    assert candidate(initialEnergy = 10,initialExperience = 10,energy = [5, 5, 5],experience = [5, 5, 5]) == 6
