# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(houses = [1, 5],heaters = [2]) == 3
    assert candidate(houses = [1],heaters = [1]) == 0
    assert candidate(houses = [10, 20, 30, 40, 50],heaters = [15, 45]) == 15
    assert candidate(houses = [10, 20, 30, 40, 50],heaters = [5, 15, 25, 35, 45]) == 5
    assert candidate(houses = [1, 3, 5, 7, 9],heaters = [2, 6]) == 3
    assert candidate(houses = [1, 3, 5, 7, 9],heaters = [2, 6, 10]) == 1
    assert candidate(houses = [28, 8, 9, 26, 18, 25, 13, 19, 16, 11, 27, 24, 23, 17, 15, 22, 6, 10, 5, 3],heaters = [20, 1, 15, 10]) == 8
    assert candidate(houses = [10, 20, 30, 40, 50],heaters = [15, 25, 35, 45]) == 5
    assert candidate(houses = [1, 2, 3, 4, 5],heaters = [1, 5]) == 2
    assert candidate(houses = [1, 1000000000],heaters = [500000000]) == 500000000
    assert candidate(houses = [1, 2, 3],heaters = [2]) == 1
    assert candidate(houses = [1, 3, 5, 7, 9],heaters = [2, 6, 8]) == 1
    assert candidate(houses = [282475249, 622690073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923],heaters = [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 622890097, 429201176]) == 161379218
    assert candidate(houses = [1, 3, 5, 7, 9],heaters = [2, 8]) == 3
    assert candidate(houses = [1, 2, 3, 4, 5],heaters = [3]) == 2
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],heaters = [1, 10]) == 4
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9],heaters = [1, 9]) == 4
    assert candidate(houses = [10, 20, 30, 40, 50],heaters = [15, 35]) == 15
    assert candidate(houses = [1, 2, 3, 4],heaters = [1, 4]) == 1
    assert candidate(houses = [1, 4, 6, 9],heaters = [1, 10]) == 4
    assert candidate(houses = [1, 9],heaters = [5]) == 4
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],heaters = [2, 6, 10, 14, 18]) == 1
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],heaters = [5, 55, 105]) == 25
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],heaters = [25, 55, 85, 115, 145]) == 15
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],heaters = [5]) == 5
    assert candidate(houses = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],heaters = [1, 97]) == 48
    assert candidate(houses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],heaters = [150, 350, 550, 750, 950]) == 50
    assert candidate(houses = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],heaters = [200, 400, 600, 800]) == 200
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],heaters = [25, 50]) == 24
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],heaters = [10, 100]) == 40
    assert candidate(houses = [100, 150, 200, 250, 300, 350, 400, 450, 500],heaters = [200, 400]) == 100
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],heaters = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 5
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],heaters = [15, 45, 75, 105, 135]) == 15
    assert candidate(houses = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],heaters = [500000000]) == 500000000
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],heaters = [10, 20, 30, 40]) == 9
    assert candidate(houses = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],heaters = [500]) == 500
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50],heaters = [1, 25, 50]) == 12
    assert candidate(houses = [1, 5, 10, 20, 30, 50, 60, 80, 90, 100],heaters = [15, 45, 75]) == 25
    assert candidate(houses = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],heaters = [10, 60, 100]) == 25
    assert candidate(houses = [1, 5, 10, 15, 20],heaters = [12, 25]) == 11
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],heaters = [10, 20, 30]) == 9
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],heaters = [1, 99]) == 49
    assert candidate(houses = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],heaters = [10, 40, 70, 100]) == 15
    assert candidate(houses = [1, 100, 200, 300, 400, 500],heaters = [50, 250, 450]) == 50
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],heaters = [2, 10, 18, 26]) == 3
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],heaters = [1, 8, 15]) == 3
    assert candidate(houses = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],heaters = [8, 22, 48]) == 13
    assert candidate(houses = [1, 5, 9, 15, 20, 25, 30, 35, 40],heaters = [10, 20, 30]) == 10
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],heaters = [2, 6, 14, 18]) == 3
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],heaters = [5, 10, 15, 20]) == 4
    assert candidate(houses = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],heaters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
    assert candidate(houses = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],heaters = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 50
    assert candidate(houses = [5, 15, 25, 35, 45, 55],heaters = [10, 40]) == 15
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],heaters = [5, 15]) == 5
    assert candidate(houses = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],heaters = [50, 150, 250]) == 50
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],heaters = [1, 3, 5, 7, 9, 11, 13, 15]) == 1
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],heaters = [1, 20]) == 9
    assert candidate(houses = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],heaters = [50, 550, 950]) == 250
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],heaters = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
    assert candidate(houses = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],heaters = [500000000, 1000000000]) == 499999999
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],heaters = [2, 10, 18]) == 3
    assert candidate(houses = [100, 200, 300, 400, 500],heaters = [50, 250, 450]) == 50
    assert candidate(houses = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130],heaters = [25, 75, 125]) == 25
    assert candidate(houses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],heaters = [150, 450, 750]) == 250
    assert candidate(houses = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],heaters = [20, 40, 60, 80]) == 15
    assert candidate(houses = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],heaters = [5, 15, 25]) == 5
    assert candidate(houses = [1, 3, 5, 7, 9],heaters = [2, 4, 6, 8]) == 1
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],heaters = [10, 100, 190, 290]) == 40
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],heaters = [10, 11]) == 9
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],heaters = [10, 20]) == 9
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],heaters = [1, 15]) == 7
    assert candidate(houses = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],heaters = [10, 30, 40]) == 9
    assert candidate(houses = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],heaters = [5, 25, 45, 65, 85]) == 15
    assert candidate(houses = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],heaters = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 10
    assert candidate(houses = [1, 3, 7, 12, 17, 23, 30],heaters = [4, 9, 25]) == 8
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],heaters = [5, 10]) == 5
    assert candidate(houses = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120],heaters = [1, 60, 120]) == 30
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],heaters = [10, 20, 30]) == 9
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],heaters = [1, 30]) == 14
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],heaters = [1, 15]) == 7
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],heaters = [5, 100, 195]) == 45
    assert candidate(houses = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],heaters = [5, 100]) == 45
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],heaters = [1, 20]) == 9
    assert candidate(houses = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],heaters = [10, 40, 70]) == 25
    assert candidate(houses = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],heaters = [5, 25, 45]) == 10
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],heaters = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 1
    assert candidate(houses = [1, 1000000000],heaters = [500000000]) == 500000000
    assert candidate(houses = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],heaters = [1, 99]) == 49
    assert candidate(houses = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],heaters = [10, 30, 50, 70, 90]) == 5
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],heaters = [15, 45, 75]) == 25
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],heaters = [2, 6, 10, 14, 18, 22, 26]) == 3
    assert candidate(houses = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],heaters = [50, 100, 150, 200]) == 49
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],heaters = [5, 15, 25]) == 5
    assert candidate(houses = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],heaters = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(houses = [1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],heaters = [50, 500, 5000, 50000, 500000, 5000000, 50000000, 500000000, 1500000000]) == 500000000
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],heaters = [5, 15, 20]) == 5
    assert candidate(houses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],heaters = [150, 450, 750]) == 250
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],heaters = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 1
    assert candidate(houses = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],heaters = [10, 40, 80]) == 15
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],heaters = [10, 130]) == 60
    assert candidate(houses = [1, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],heaters = [1, 50, 100]) == 25
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],heaters = [3, 7]) == 3
    assert candidate(houses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],heaters = [25, 75, 125]) == 25
    assert candidate(houses = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],heaters = [7, 23, 37]) == 13
    assert candidate(houses = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],heaters = [5, 25, 45]) == 10
    assert candidate(houses = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],heaters = [100, 300, 500, 700, 900]) == 50
    assert candidate(houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],heaters = [3, 8, 13]) == 2
    assert candidate(houses = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],heaters = [5, 95, 195]) == 45
