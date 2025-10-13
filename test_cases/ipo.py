# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(k = 1,w = 10,profits = [5, 6],capital = [4, 0]) == 16
    assert candidate(k = 5,w = 10,profits = [5, 4, 3, 2, 1],capital = [1, 2, 3, 4, 5]) == 25
    assert candidate(k = 2,w = 3,profits = [8, 10, 6],capital = [2, 5, 0]) == 21
    assert candidate(k = 4,w = 0,profits = [1, 1, 1, 1],capital = [0, 0, 0, 0]) == 4
    assert candidate(k = 5,w = 0,profits = [1, 2, 3, 4, 5],capital = [0, 1, 2, 3, 4]) == 15
    assert candidate(k = 5,w = 0,profits = [10, 20, 30, 40, 50],capital = [0, 0, 0, 0, 0]) == 150
    assert candidate(k = 1,w = 10,profits = [1, 2, 3],capital = [5, 5, 5]) == 13
    assert candidate(k = 1,w = 5,profits = [1, 2, 3],capital = [3, 4, 5]) == 8
    assert candidate(k = 3,w = 0,profits = [1, 2, 3],capital = [0, 1, 2]) == 6
    assert candidate(k = 3,w = 0,profits = [10, 20, 30],capital = [0, 0, 0]) == 60
    assert candidate(k = 2,w = 1,profits = [1, 2, 3],capital = [1, 1, 2]) == 6
    assert candidate(k = 1,w = 100,profits = [1000, 2000, 3000],capital = [1000, 2000, 3000]) == 100
    assert candidate(k = 3,w = 3,profits = [1, 2, 3, 4, 5],capital = [0, 1, 2, 3, 4]) == 15
    assert candidate(k = 2,w = 0,profits = [1, 2, 3],capital = [0, 1, 1]) == 4
    assert candidate(k = 10,w = 1,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    assert candidate(k = 2,w = 3,profits = [5, 6, 4, 3, 2],capital = [2, 3, 4, 5, 6]) == 14
    assert candidate(k = 3,w = 2,profits = [5, 4, 3, 2, 1],capital = [5, 4, 3, 2, 1]) == 13
    assert candidate(k = 2,w = 5,profits = [100, 200, 300, 400, 500],capital = [0, 0, 0, 0, 0]) == 905
    assert candidate(k = 5,w = 20,profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],capital = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 3720
    assert candidate(k = 6,w = 1,profits = [1, 2, 3, 4, 5, 6, 7],capital = [0, 1, 2, 3, 4, 5, 6]) == 28
    assert candidate(k = 3,w = 0,profits = [10, 10, 10, 10, 10],capital = [0, 0, 0, 0, 0]) == 30
    assert candidate(k = 5,w = 100,profits = [10, 20, 30, 40, 50],capital = [10, 20, 30, 40, 50]) == 250
    assert candidate(k = 4,w = 0,profits = [100, 200, 300, 400, 500],capital = [0, 1, 2, 3, 4]) == 1300
    assert candidate(k = 1,w = 1,profits = [100, 200, 300, 400, 500],capital = [0, 0, 0, 0, 0]) == 501
    assert candidate(k = 10,w = 10000,profits = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],capital = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 65000
    assert candidate(k = 4,w = 0,profits = [10, 20, 30, 40],capital = [0, 10, 20, 30]) == 100
    assert candidate(k = 20,w = 1000,profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],capital = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 22000
    assert candidate(k = 3,w = 1,profits = [10, 20, 30, 40, 50],capital = [1, 2, 3, 4, 5]) == 101
    assert candidate(k = 5,w = 0,profits = [1, 10, 100, 1000, 10000],capital = [0, 0, 0, 0, 0]) == 11111
    assert candidate(k = 4,w = 10,profits = [100, 200, 300, 400],capital = [50, 50, 50, 50]) == 10
    assert candidate(k = 3,w = 50,profits = [100, 200, 300, 400, 500],capital = [50, 50, 50, 50, 50]) == 1250
    assert candidate(k = 5,w = 0,profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],capital = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 4000
    assert candidate(k = 7,w = 50,profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capital = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 540
    assert candidate(k = 7,w = 5,profits = [5, 10, 15, 20, 25, 30, 35, 40],capital = [0, 1, 2, 3, 4, 5, 6, 7]) == 180
    assert candidate(k = 10,w = 50000,profits = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],capital = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 600000
    assert candidate(k = 3,w = 3,profits = [1, 1, 1, 1, 1],capital = [0, 1, 2, 3, 4]) == 6
    assert candidate(k = 10,w = 5,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(k = 5,w = 5,profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capital = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 405
    assert candidate(k = 1,w = 0,profits = [10000, 9000, 8000, 7000, 6000],capital = [0, 1000, 2000, 3000, 4000]) == 10000
    assert candidate(k = 4,w = 1500,profits = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500],capital = [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]) == 15000
    assert candidate(k = 10,w = 1,profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],capital = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5501
    assert candidate(k = 5,w = 1,profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capital = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1
    assert candidate(k = 5,w = 1,profits = [1, 2, 3, 4, 5],capital = [0, 1, 2, 3, 4]) == 16
    assert candidate(k = 10,w = 0,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 10
    assert candidate(k = 10,w = 100,profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],capital = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5600
    assert candidate(k = 7,w = 5,profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capital = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 495
    assert candidate(k = 10,w = 5,profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capital = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 60
    assert candidate(k = 3,w = 10,profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capital = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 280
    assert candidate(k = 3,w = 15,profits = [5, 10, 15, 20, 25],capital = [5, 10, 15, 20, 25]) == 75
    assert candidate(k = 3,w = 20,profits = [10, 10, 10, 10, 10],capital = [15, 15, 15, 15, 15]) == 50
    assert candidate(k = 5,w = 1000,profits = [5000, 1000, 2000, 1500, 3000, 4000, 6000, 7000, 8000, 9000],capital = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]) == 36000
    assert candidate(k = 15,w = 10,profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],capital = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 1210
    assert candidate(k = 5,w = 0,profits = [500, 400, 300, 200, 100],capital = [100, 200, 300, 400, 500]) == 0
    assert candidate(k = 4,w = 10,profits = [5, 2, 10, 8, 1],capital = [3, 4, 1, 10, 5]) == 35
    assert candidate(k = 3,w = 1,profits = [5, 4, 3, 2, 1],capital = [0, 1, 2, 3, 4]) == 13
    assert candidate(k = 4,w = 2,profits = [1, 2, 3, 4, 5, 6, 7, 8],capital = [0, 1, 2, 3, 4, 5, 6, 7]) == 26
    assert candidate(k = 5,w = 10,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15
    assert candidate(k = 7,w = 0,profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],capital = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0
    assert candidate(k = 3,w = 1000,profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],capital = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 1100
    assert candidate(k = 3,w = 0,profits = [10, 20, 30, 40, 50],capital = [0, 0, 0, 0, 0]) == 120
    assert candidate(k = 3,w = 5,profits = [10, 15, 20, 25, 30],capital = [0, 0, 0, 0, 0]) == 80
    assert candidate(k = 3,w = 100,profits = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],capital = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1450
    assert candidate(k = 1,w = 0,profits = [10000, 20000, 30000],capital = [10000, 20000, 30000]) == 0
    assert candidate(k = 5,w = 1000,profits = [500, 750, 1000, 1250, 1500],capital = [250, 500, 750, 1000, 1250]) == 6000
    assert candidate(k = 4,w = 10,profits = [5, 5, 5, 5, 5, 5],capital = [0, 0, 0, 0, 0, 0]) == 30
    assert candidate(k = 3,w = 20,profits = [100, 200, 300, 400, 500],capital = [10, 20, 30, 40, 50]) == 1120
    assert candidate(k = 10,w = 100,profits = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],capital = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 375
    assert candidate(k = 10,w = 10,profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capital = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 560
    assert candidate(k = 4,w = 10,profits = [5, 8, 7, 10, 9, 12],capital = [0, 5, 4, 9, 8, 10]) == 49
    assert candidate(k = 3,w = 10,profits = [50, 40, 30, 20, 10],capital = [5, 10, 15, 20, 25]) == 130
    assert candidate(k = 5,w = 20,profits = [100, 200, 300, 400, 500, 600],capital = [150, 250, 350, 450, 550, 650]) == 20
    assert candidate(k = 2,w = 0,profits = [5, 5, 5, 5, 5, 5],capital = [1, 2, 3, 4, 5, 6]) == 0
    assert candidate(k = 3,w = 5,profits = [1, 3, 2, 5, 4],capital = [0, 2, 3, 6, 4]) == 17
    assert candidate(k = 3,w = 10,profits = [5, 4, 3, 2, 1],capital = [10, 20, 30, 40, 50]) == 15
    assert candidate(k = 6,w = 5,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    assert candidate(k = 7,w = 5,profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capital = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 475
    assert candidate(k = 3,w = 5,profits = [6, 7, 8, 9, 10, 11],capital = [0, 1, 2, 3, 4, 5]) == 35
    assert candidate(k = 10,w = 0,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(k = 2,w = 100,profits = [50, 75, 25, 100, 125],capital = [0, 100, 50, 200, 150]) == 300
    assert candidate(k = 5,w = 5,profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capital = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5
    assert candidate(k = 2,w = 3,profits = [1, 2, 3, 4, 5],capital = [2, 3, 4, 5, 6]) == 9
    assert candidate(k = 5,w = 100,profits = [10, 20, 30, 40, 50],capital = [50, 50, 50, 50, 50]) == 250
    assert candidate(k = 3,w = 50,profits = [100, 200, 300, 400, 500],capital = [50, 100, 150, 200, 250]) == 950
    assert candidate(k = 3,w = 0,profits = [100, 200, 300, 400, 500],capital = [50, 100, 150, 200, 250]) == 0
    assert candidate(k = 3,w = 10,profits = [100, 200, 300, 400, 500],capital = [0, 0, 0, 0, 0]) == 1210
    assert candidate(k = 2,w = 500,profits = [150, 250, 350, 450, 550],capital = [50, 150, 250, 350, 450]) == 1500
    assert candidate(k = 5,w = 10,profits = [5, 6, 7, 8, 9],capital = [2, 3, 4, 5, 6]) == 45
    assert candidate(k = 7,w = 2,profits = [1, 2, 3, 4, 5, 6, 7, 8],capital = [0, 1, 2, 3, 4, 5, 6, 7]) == 37
    assert candidate(k = 5,w = 0,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 5
    assert candidate(k = 6,w = 3,profits = [1, 2, 3, 4, 5, 6, 7],capital = [1, 2, 3, 4, 5, 6, 7]) == 30
    assert candidate(k = 3,w = 10,profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capital = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 37
    assert candidate(k = 5,w = 5,profits = [3, 4, 5, 1, 2],capital = [1, 2, 3, 4, 5]) == 20
    assert candidate(k = 3,w = 5,profits = [10, 20, 30, 40, 50],capital = [0, 1, 2, 3, 4]) == 125
    assert candidate(k = 5,w = 100,profits = [200, 300, 400, 500, 600],capital = [50, 100, 150, 200, 250]) == 2100
    assert candidate(k = 100,w = 0,profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capital = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 55
    assert candidate(k = 3,w = 20,profits = [10, 20, 30, 40, 50],capital = [5, 10, 15, 20, 25]) == 140
    assert candidate(k = 3,w = 1,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 4
    assert candidate(k = 1,w = 1000000000,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1000000001
    assert candidate(k = 1,w = 100,profits = [1, 2, 3, 4, 5],capital = [0, 0, 0, 0, 0]) == 105
    assert candidate(k = 3,w = 5,profits = [2, 3, 5, 6, 8],capital = [1, 2, 3, 5, 6]) == 24
    assert candidate(k = 5,w = 0,profits = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],capital = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
    assert candidate(k = 5,w = 10,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 15
    assert candidate(k = 2,w = 100,profits = [100, 200, 300, 400, 500],capital = [0, 0, 0, 0, 0]) == 1000
    assert candidate(k = 4,w = 2,profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capital = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 12
    assert candidate(k = 3,w = 500,profits = [100, 200, 300, 400, 500, 600, 700, 800],capital = [0, 100, 200, 300, 400, 500, 600, 700]) == 2600
    assert candidate(k = 5,w = 10,profits = [100, 200, 300, 400, 500],capital = [1, 2, 3, 4, 5]) == 1510
    assert candidate(k = 2,w = 5,profits = [10, 15, 20, 25, 30],capital = [0, 5, 10, 15, 20]) == 50
    assert candidate(k = 5,w = 0,profits = [10, 20, 30, 40, 50],capital = [100, 50, 200, 300, 400]) == 0
    assert candidate(k = 2,w = 5,profits = [10, 10, 10, 10, 10],capital = [0, 0, 0, 0, 0]) == 25
    assert candidate(k = 5,w = 0,profits = [1, 2, 3, 4, 5, 6],capital = [0, 1, 1, 2, 2, 3]) == 19
    assert candidate(k = 5,w = 500,profits = [100, 200, 300, 400, 500],capital = [0, 0, 0, 0, 0]) == 2000
    assert candidate(k = 6,w = 10,profits = [1, 2, 3, 4, 5, 6],capital = [0, 2, 4, 6, 8, 10]) == 31
    assert candidate(k = 5,w = 3,profits = [10, 2, 11, 1, 4],capital = [3, 1, 5, 0, 2]) == 31
    assert candidate(k = 4,w = 0,profits = [100, 200, 300, 400],capital = [50, 150, 250, 350]) == 0
    assert candidate(k = 5,w = 50,profits = [10, 20, 30, 40, 50],capital = [10, 20, 30, 40, 50]) == 200
    assert candidate(k = 5,w = 50,profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capital = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 450
    assert candidate(k = 4,w = 5,profits = [6, 7, 8, 9, 10],capital = [0, 5, 10, 15, 20]) == 39
    assert candidate(k = 5,w = 10,profits = [1, 3, 5, 7, 9],capital = [0, 2, 3, 5, 8]) == 35
    assert candidate(k = 3,w = 5,profits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capital = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 5
    assert candidate(k = 4,w = 10,profits = [10, 20, 30, 40, 50],capital = [0, 10, 20, 30, 40]) == 150
    assert candidate(k = 3,w = 10,profits = [15, 25, 35, 45, 55, 65, 75, 85, 95],capital = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == 265
    assert candidate(k = 2,w = 1000,profits = [1000, 1000, 1000, 1000, 1000],capital = [0, 100, 200, 300, 400]) == 3000
    assert candidate(k = 4,w = 1,profits = [4, 5, 6, 7, 8, 9],capital = [2, 3, 4, 5, 6, 7]) == 1
    assert candidate(k = 4,w = 10,profits = [1, 5, 7, 10, 12],capital = [3, 7, 10, 14, 17]) == 44
    assert candidate(k = 5,w = 100,profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],capital = [50, 40, 30, 20, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 750
    assert candidate(k = 3,w = 1000,profits = [300, 500, 700, 100, 200, 400, 600, 800],capital = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500]) == 2500
    assert candidate(k = 4,w = 1000,profits = [900, 800, 700, 600, 500],capital = [500, 600, 700, 800, 900]) == 4000
    assert candidate(k = 3,w = 0,profits = [10, 20, 30, 40, 50],capital = [1, 2, 3, 4, 5]) == 0
    assert candidate(k = 15,w = 500,profits = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750],capital = [200, 150, 100, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 6500
    assert candidate(k = 2,w = 5,profits = [10, 20, 30, 40, 50],capital = [1, 2, 3, 4, 5]) == 95
    assert candidate(k = 5,w = 10,profits = [10, 20, 30, 40, 50],capital = [5, 15, 25, 35, 45]) == 160
