# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(values = [10, 10, 10, 10],labels = [1, 1, 1, 1],numWanted = 3,useLimit = 2) == 20
    assert candidate(values = [10, 10, 10, 10],labels = [1, 2, 3, 4],numWanted = 4,useLimit = 1) == 40
    assert candidate(values = [9, 8, 8, 7, 6],labels = [0, 0, 0, 1, 1],numWanted = 3,useLimit = 1) == 16
    assert candidate(values = [10, 20, 30, 40, 50],labels = [1, 2, 3, 4, 5],numWanted = 5,useLimit = 1) == 150
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 5,useLimit = 1) == 40
    assert candidate(values = [10, 20, 30, 40, 50],labels = [1, 1, 1, 1, 1],numWanted = 3,useLimit = 2) == 90
    assert candidate(values = [1, 2, 3, 4, 5],labels = [1, 1, 1, 1, 1],numWanted = 3,useLimit = 1) == 5
    assert candidate(values = [1, 2, 3, 4, 5],labels = [1, 2, 3, 4, 5],numWanted = 5,useLimit = 1) == 15
    assert candidate(values = [5, 4, 3, 2, 1],labels = [1, 3, 3, 3, 2],numWanted = 3,useLimit = 2) == 12
    assert candidate(values = [5, 4, 3, 2, 1],labels = [1, 1, 2, 2, 3],numWanted = 3,useLimit = 1) == 9
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 5,useLimit = 2) == 19
    assert candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 5,useLimit = 1) == 400
    assert candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],numWanted = 5,useLimit = 2) == 2800
    assert candidate(values = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],labels = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],numWanted = 5,useLimit = 2) == 80
    assert candidate(values = [5, 10, 15, 20, 25, 30],labels = [1, 2, 1, 3, 2, 3],numWanted = 4,useLimit = 2) == 90
    assert candidate(values = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 5,useLimit = 1) == 1937
    assert candidate(values = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],labels = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3],numWanted = 6,useLimit = 3) == 220
    assert candidate(values = [25, 25, 25, 25, 25, 25],labels = [1, 1, 1, 1, 1, 1],numWanted = 4,useLimit = 1) == 25
    assert candidate(values = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 8,useLimit = 2) == 120
    assert candidate(values = [30, 20, 10, 30, 20, 10, 30, 20, 10],labels = [1, 2, 3, 1, 2, 3, 1, 2, 3],numWanted = 5,useLimit = 2) == 110
    assert candidate(values = [3, 5, 1, 3, 5, 3, 5, 3, 5, 3],labels = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],numWanted = 6,useLimit = 2) == 18
    assert candidate(values = [10, 20, 30, 40, 50],labels = [1, 1, 1, 1, 2],numWanted = 3,useLimit = 2) == 120
    assert candidate(values = [50, 40, 30, 20, 10],labels = [1, 2, 2, 3, 3],numWanted = 4,useLimit = 1) == 110
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 10,useLimit = 2) == 39
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],numWanted = 5,useLimit = 2) == 40
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],numWanted = 8,useLimit = 2) == 57
    assert candidate(values = [20, 18, 17, 16, 15, 14, 13, 12, 11, 10],labels = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],numWanted = 4,useLimit = 1) == 71
    assert candidate(values = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],numWanted = 10,useLimit = 3) == 105
    assert candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 5,useLimit = 1) == 100
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],numWanted = 5,useLimit = 1) == 19
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2],numWanted = 8,useLimit = 2) == 680
    assert candidate(values = [10000, 10000, 9999, 9999, 9998, 9998, 9997, 9997, 9996, 9996],labels = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],numWanted = 8,useLimit = 2) == 79988
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 15,useLimit = 3) == 195
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9],labels = [1, 2, 1, 2, 1, 2, 1, 2, 1],numWanted = 3,useLimit = 1) == 17
    assert candidate(values = [9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [1, 1, 2, 2, 3, 3, 4, 4, 5],numWanted = 5,useLimit = 2) == 35
    assert candidate(values = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 15,useLimit = 2) == 270
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 10,useLimit = 1) == 55
    assert candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 3,useLimit = 1) == 100
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],numWanted = 6,useLimit = 3) == 390
    assert candidate(values = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 15,useLimit = 2) == 195
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 7,useLimit = 1) == 49
    assert candidate(values = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 5,useLimit = 2) == 38
    assert candidate(values = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],numWanted = 15,useLimit = 3) == 138
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 5,useLimit = 1) == 1
    assert candidate(values = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],labels = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],numWanted = 6,useLimit = 3) == 90
    assert candidate(values = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 8,useLimit = 1) == 80
    assert candidate(values = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],numWanted = 8,useLimit = 3) == 60
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 5,useLimit = 10) == 400
    assert candidate(values = [100, 50, 200, 150, 100],labels = [1, 2, 1, 2, 1],numWanted = 2,useLimit = 1) == 350
    assert candidate(values = [10, 20, 30, 40, 50],labels = [1, 1, 2, 2, 3],numWanted = 2,useLimit = 1) == 90
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],labels = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3],numWanted = 6,useLimit = 2) == 30
    assert candidate(values = [25, 20, 15, 10, 5],labels = [1, 2, 3, 4, 5],numWanted = 3,useLimit = 1) == 60
    assert candidate(values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 5,useLimit = 1) == 75
    assert candidate(values = [20, 15, 10, 5, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19],labels = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],numWanted = 10,useLimit = 3) == 147
    assert candidate(values = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],labels = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],numWanted = 8,useLimit = 3) == 84
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],numWanted = 5,useLimit = 2) == 34
    assert candidate(values = [9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9],numWanted = 3,useLimit = 1) == 24
    assert candidate(values = [50, 40, 30, 20, 10, 50, 40, 30, 20, 10],labels = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],numWanted = 5,useLimit = 2) == 210
    assert candidate(values = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],numWanted = 10,useLimit = 2) == 105
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 5,useLimit = 1) == 25
    assert candidate(values = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 5,useLimit = 3) == 35
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 5,useLimit = 1) == 100
    assert candidate(values = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 8,useLimit = 1) == 16
    assert candidate(values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4],numWanted = 7,useLimit = 2) == 40
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5],labels = [1, 2, 3, 4, 5, 6, 7, 8],numWanted = 6,useLimit = 1) == 30
    assert candidate(values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 5,useLimit = 2) == 38
    assert candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],numWanted = 5,useLimit = 3) == 360
    assert candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 10,useLimit = 1) == 550
    assert candidate(values = [9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [0, 1, 0, 1, 0, 1, 0, 1, 0],numWanted = 4,useLimit = 1) == 17
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],labels = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],numWanted = 8,useLimit = 3) == 75
    assert candidate(values = [15, 10, 10, 5, 5, 5, 5],labels = [1, 1, 2, 2, 2, 3, 3],numWanted = 5,useLimit = 2) == 45
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 7,useLimit = 1) == 35
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],numWanted = 10,useLimit = 3) == 131
    assert candidate(values = [9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [0, 1, 0, 1, 0, 1, 0, 1, 0],numWanted = 5,useLimit = 2) == 30
    assert candidate(values = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 5,useLimit = 1) == 50
    assert candidate(values = [15, 12, 11, 10, 9, 8],labels = [1, 1, 2, 2, 3, 3],numWanted = 4,useLimit = 2) == 48
    assert candidate(values = [500, 400, 300, 200, 100],labels = [1, 2, 3, 4, 5],numWanted = 3,useLimit = 1) == 1200
    assert candidate(values = [100, 80, 60, 40, 20],labels = [1, 1, 1, 1, 1],numWanted = 5,useLimit = 3) == 240
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],labels = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],numWanted = 6,useLimit = 2) == 450
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 7,useLimit = 3) == 490
    assert candidate(values = [5, 9, 1, 9, 8, 5, 7, 8, 2, 1],labels = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3],numWanted = 6,useLimit = 2) == 46
    assert candidate(values = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],labels = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],numWanted = 5,useLimit = 1) == 60
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],numWanted = 4,useLimit = 3) == 20
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],numWanted = 5,useLimit = 2) == 40
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],numWanted = 5,useLimit = 3) == 5
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],numWanted = 10,useLimit = 2) == 46
    assert candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 5,useLimit = 2) == 1900
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],numWanted = 10,useLimit = 1) == 50
    assert candidate(values = [5, 10, 15, 20, 25, 30, 35, 40],labels = [1, 1, 2, 2, 3, 3, 4, 4],numWanted = 4,useLimit = 2) == 130
    assert candidate(values = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numWanted = 5,useLimit = 1) == 100
    assert candidate(values = [9, 8, 7, 6, 5, 4, 3, 2, 1],labels = [0, 0, 0, 1, 1, 1, 2, 2, 2],numWanted = 5,useLimit = 2) == 31
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],numWanted = 5,useLimit = 1) == 10
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],numWanted = 10,useLimit = 2) == 155
    assert candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],labels = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],numWanted = 5,useLimit = 2) == 340
    assert candidate(values = [30, 25, 20, 15, 10, 5],labels = [1, 2, 3, 4, 5, 6],numWanted = 4,useLimit = 1) == 90
    assert candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],labels = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],numWanted = 5,useLimit = 3) == 360
    assert candidate(values = [20, 18, 15, 12, 10, 8, 6, 4, 2],labels = [1, 1, 2, 2, 3, 3, 4, 4, 5],numWanted = 5,useLimit = 2) == 75
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],labels = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],numWanted = 5,useLimit = 1) == 40
    assert candidate(values = [30, 20, 10, 10, 20, 30],labels = [1, 1, 2, 2, 3, 3],numWanted = 5,useLimit = 1) == 70
