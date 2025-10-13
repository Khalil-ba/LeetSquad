# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(robot = [5, 1, 3],factory = [[2, 3]]) == 5
    assert candidate(robot = [5, 5, 5, 5],factory = [[5, 4]]) == 0
    assert candidate(robot = [-3, 0, 3],factory = [[-2, 1], [2, 1], [5, 2]]) == 5
    assert candidate(robot = [-1, -3, 2, 4, 5],factory = [[-2, 1], [2, 2], [6, 2]]) == 7
    assert candidate(robot = [-5, -2, 0, 2, 5],factory = [[-3, 2], [1, 3]]) == 9
    assert candidate(robot = [5, 8, 15],factory = [[10, 2], [16, 1]]) == 8
    assert candidate(robot = [10, 20, 30, 40],factory = [[5, 2], [15, 2], [25, 2]]) == 30
    assert candidate(robot = [-10, 0, 10],factory = [[-5, 1], [0, 2], [5, 1]]) == 10
    assert candidate(robot = [5, 2, -5],factory = [[-2, 2], [2, 2]]) == 6
    assert candidate(robot = [10, -10, 0],factory = [[0, 3]]) == 20
    assert candidate(robot = [0, 4, 6],factory = [[2, 2], [6, 2]]) == 4
    assert candidate(robot = [3, 7, 12, 15],factory = [[2, 3], [10, 2]]) == 13
    assert candidate(robot = [-3, 0, 3],factory = [[-2, 1], [2, 2]]) == 4
    assert candidate(robot = [1, -1],factory = [[-2, 1], [2, 1]]) == 2
    assert candidate(robot = [-20, -10, 0, 10, 20],factory = [[-15, 2], [0, 1], [15, 2]]) == 20
    assert candidate(robot = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],factory = [[-5, 2], [-15, 2], [-25, 2], [-35, 2], [-45, 2], [-55, 2], [-65, 2], [-75, 2], [-85, 2], [-95, 2]]) == 50
    assert candidate(robot = [-15, -10, -5, 0, 5, 10, 15],factory = [[-12, 2], [-7, 2], [-2, 2], [3, 2], [8, 2], [13, 2]]) == 15
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],factory = [[5, 3], [10, 4], [15, 3]]) == 45
    assert candidate(robot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],factory = [[2, 2], [5, 2], [8, 2]]) == inf
    assert candidate(robot = [-1, -2, -3, -4, -5],factory = [[-10, 3], [0, 2], [10, 1]]) == 21
    assert candidate(robot = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],factory = [[5, 3], [15, 3], [25, 3], [35, 3], [45, 3], [55, 3], [65, 3], [75, 3], [85, 3], [95, 3], [105, 3], [115, 3], [125, 3], [135, 3]]) == 75
    assert candidate(robot = [0, 2, 4, 6, 8, 10],factory = [[1, 1], [3, 1], [5, 1], [7, 1], [9, 1], [11, 1]]) == 6
    assert candidate(robot = [100, 200, 300, 400, 500],factory = [[50, 1], [150, 2], [250, 2], [350, 2], [450, 1], [550, 1]]) == 250
    assert candidate(robot = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],factory = [[0, 2], [6, 3], [12, 3], [18, 2]]) == 16
    assert candidate(robot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],factory = [[0, 5], [5, 5]]) == 20
    assert candidate(robot = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],factory = [[-3, 3], [0, 4], [3, 3]]) == 12
    assert candidate(robot = [-10, -5, 0, 5, 10, 15, 20, 25, 30, 35],factory = [[-7, 2], [2, 3], [17, 2], [32, 2]]) == inf
    assert candidate(robot = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40],factory = [[-10, 2], [5, 3], [20, 3], [35, 2]]) == 50
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],factory = [[0, 2], [4, 2], [8, 2], [12, 2]]) == inf
    assert candidate(robot = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],factory = [[5, 3], [15, 3], [25, 3]]) == inf
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],factory = [[0, 3], [5, 4], [10, 3]]) == 13
    assert candidate(robot = [-100, -50, 0, 50, 100],factory = [[-75, 2], [-25, 1], [25, 1], [75, 2]]) == 125
    assert candidate(robot = [10, 20, 30, 40, 50, 60, 70, 80, 90],factory = [[0, 3], [10, 3], [20, 3], [30, 3], [40, 3], [50, 3], [60, 3], [70, 3], [80, 3], [90, 3]]) == 0
    assert candidate(robot = [-2, -1, 0, 1, 2, 3, 4],factory = [[-3, 2], [0, 3], [3, 2]]) == 7
    assert candidate(robot = [-2, -1, 0, 1, 2],factory = [[-3, 1], [-1, 1], [1, 1], [3, 1]]) == inf
    assert candidate(robot = [-10, -5, 0, 5, 10, 15, 20],factory = [[-20, 1], [-10, 2], [0, 3], [10, 2], [20, 1]]) == 15
    assert candidate(robot = [-100, -50, 0, 50, 100],factory = [[-75, 2], [0, 2], [75, 2]]) == 100
    assert candidate(robot = [-100, -50, 0, 50, 100, 150],factory = [[-75, 3], [25, 2], [125, 2]]) == 150
    assert candidate(robot = [-100, -50, 0, 50, 100, 150, 200],factory = [[-75, 2], [-25, 2], [25, 2], [75, 2], [125, 2], [175, 2]]) == 175
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],factory = [[0, 5], [5, 5], [10, 5], [15, 5]]) == 60
    assert candidate(robot = [-20, -10, 0, 10, 20],factory = [[-15, 1], [-5, 2], [5, 3], [15, 1]]) == 25
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9],factory = [[2, 3], [5, 3], [8, 3]]) == 6
    assert candidate(robot = [-20, -10, 0, 10, 20],factory = [[-15, 2], [0, 3], [15, 2]]) == 20
    assert candidate(robot = [100, 200, 300, 400, 500],factory = [[50, 2], [150, 1], [250, 2], [350, 1], [450, 1]]) == 250
    assert candidate(robot = [1, 3, 5, 7, 9, 11],factory = [[2, 2], [6, 2], [10, 2]]) == 6
    assert candidate(robot = [1, 3, 5, 7, 9],factory = [[2, 2], [4, 2], [6, 2], [8, 2], [10, 1]]) == 5
    assert candidate(robot = [10, 20, 30, 40, 50, 60],factory = [[15, 2], [35, 2], [55, 2]]) == 30
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],factory = [[2, 3], [6, 3], [10, 3], [14, 3]]) == inf
    assert candidate(robot = [-20, -10, 0, 10, 20],factory = [[-15, 2], [-5, 3], [5, 2], [15, 1]]) == 25
    assert candidate(robot = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],factory = [[0, 10]]) == 10
    assert candidate(robot = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10],factory = [[-105, 2], [-95, 2], [-85, 2], [-75, 2], [-65, 2], [-55, 2], [-45, 2], [-35, 2], [-25, 2], [-15, 2]]) == 50
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],factory = [[0, 10]]) == 55
    assert candidate(robot = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],factory = [[10, 2], [20, 2], [30, 2], [40, 2]]) == inf
    assert candidate(robot = [10, 20, 30, 40],factory = [[15, 2], [25, 2], [35, 2]]) == 20
    assert candidate(robot = [-10, -5, 0, 5, 10, 15, 20],factory = [[-7, 2], [-2, 2], [3, 2], [8, 2]]) == 35
    assert candidate(robot = [-20, -10, 0, 10, 20],factory = [[-15, 2], [0, 3], [15, 1]]) == 25
    assert candidate(robot = [-20, -15, -10, -5, 0, 5, 10, 15, 20],factory = [[-15, 2], [-10, 2], [-5, 2], [0, 2], [5, 2], [10, 2], [15, 2]]) == 10
    assert candidate(robot = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],factory = [[-6, 3], [0, 5], [6, 3]]) == 18
    assert candidate(robot = [1, 3, 5, 7, 9],factory = [[2, 1], [4, 1], [6, 1], [8, 1]]) == inf
    assert candidate(robot = [-5, -3, -1, 1, 3, 5],factory = [[-10, 1], [-5, 2], [0, 3], [5, 2], [10, 1]]) == 6
    assert candidate(robot = [-5, -3, -1, 1, 3, 5, 7, 9],factory = [[-4, 1], [0, 3], [4, 2]]) == inf
    assert candidate(robot = [1, 3, 5, 7, 9],factory = [[0, 2], [4, 2], [8, 2]]) == 5
    assert candidate(robot = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],factory = [[3, 3], [9, 3], [15, 3], [21, 3]]) == 25
    assert candidate(robot = [10, 10, 10, 10],factory = [[10, 1], [10, 1], [10, 1], [10, 1]]) == 0
    assert candidate(robot = [1, 4, 7, 10, 13, 16, 19, 22, 25],factory = [[3, 3], [9, 3], [15, 3], [21, 3]]) == 16
    assert candidate(robot = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],factory = [[5, 2], [15, 2], [25, 2], [35, 2], [45, 2], [55, 2], [65, 2], [75, 2], [85, 2], [95, 2]]) == 50
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],factory = [[0, 2], [5, 3], [10, 5]]) == 16
    assert candidate(robot = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],factory = [[150, 3], [500, 4], [850, 3]]) == 900
    assert candidate(robot = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],factory = [[-5, 5], [0, 5], [5, 5]]) == 25
    assert candidate(robot = [-5, 0, 5, 10, 15, 20],factory = [[-10, 1], [0, 3], [10, 2], [20, 1]]) == 15
    assert candidate(robot = [-50, -25, 0, 25, 50],factory = [[-75, 3], [0, 2], [75, 1]]) == 125
    assert candidate(robot = [-10, -5, 0, 5, 10],factory = [[-15, 2], [-10, 1], [0, 3], [10, 2], [15, 1]]) == 10
    assert candidate(robot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],factory = [[0, 5], [5, 5], [10, 5], [15, 5]]) == 40
    assert candidate(robot = [-100, -200, -300, -400, -500],factory = [[-50, 2], [-150, 1], [-250, 2], [-350, 1], [-450, 1]]) == 250
    assert candidate(robot = [-100, -50, 0, 50, 100],factory = [[-75, 1], [-25, 1], [25, 1], [75, 1]]) == inf
    assert candidate(robot = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10],factory = [[-95, 2], [-85, 2], [-75, 2], [-65, 2], [-55, 2], [-45, 2], [-35, 2], [-25, 2], [-15, 2], [-5, 2]]) == 50
    assert candidate(robot = [-100, -50, 0, 50, 100],factory = [[-75, 2], [-25, 2], [25, 2], [75, 1]]) == 125
    assert candidate(robot = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],factory = [[-10, 6], [0, 5]]) == 60
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],factory = [[0, 5], [10, 5]]) == 25
    assert candidate(robot = [-10, -5, 0, 5, 10, 15, 20, 25],factory = [[-15, 2], [0, 3], [15, 3], [25, 1]]) == 25
    assert candidate(robot = [100, 200, 300, 400, 500],factory = [[50, 1], [150, 2], [250, 2], [350, 1], [450, 1]]) == 250
    assert candidate(robot = [-10, -5, 0, 5, 10, 15],factory = [[-8, 2], [2, 3], [12, 2]]) == 15
    assert candidate(robot = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],factory = [[-5, 5], [5, 5]]) == 50
    assert candidate(robot = [0, 10, 20, 30, 40, 50, 60],factory = [[5, 3], [15, 3], [25, 3], [35, 3], [45, 3]]) == 45
    assert candidate(robot = [-1, 0, 1],factory = [[-2, 1], [2, 1], [0, 1]]) == 2
    assert candidate(robot = [-9, -6, -3, 0, 3, 6, 9],factory = [[-8, 2], [-2, 2], [2, 2], [8, 1]]) == 12
    assert candidate(robot = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],factory = [[0, 5], [10, 5], [20, 5]]) == 26
    assert candidate(robot = [0, 10, 20, 30, 40, 50, 60],factory = [[5, 1], [15, 2], [25, 2], [35, 1], [45, 2], [55, 1]]) == 35
    assert candidate(robot = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],factory = [[-4, 3], [2, 4], [7, 3], [11, 3]]) == 22
    assert candidate(robot = [-1, -2, -3, -4, -5],factory = [[-3, 3], [0, 2]]) == 6
    assert candidate(robot = [0, 2, 4, 6, 8, 10, 12],factory = [[1, 2], [5, 2], [9, 2], [13, 1]]) == 7
    assert candidate(robot = [100, 200, 300, 400, 500],factory = [[50, 1], [150, 1], [250, 1], [350, 1], [450, 1]]) == 250
    assert candidate(robot = [-5, -3, -1, 1, 3, 5],factory = [[-10, 1], [-6, 2], [-2, 2], [2, 2], [6, 1]]) == 6
    assert candidate(robot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],factory = [[5, 5], [15, 5]]) == 45
    assert candidate(robot = [-20, -10, 0, 10, 20],factory = [[-25, 2], [-15, 3], [-5, 2], [5, 3], [15, 2], [25, 1]]) == 25
    assert candidate(robot = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],factory = [[-60, 3], [-40, 4], [-20, 4], [0, 4], [20, 4], [40, 3]]) == 60
    assert candidate(robot = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],factory = [[0, 2], [4, 2], [8, 2], [12, 2], [16, 2]]) == 20
    assert candidate(robot = [1, 3, 5, 7, 9],factory = [[0, 3], [6, 2], [12, 1]]) == 9
    assert candidate(robot = [-100, -50, 0, 50, 100],factory = [[-150, 2], [-100, 2], [-50, 2], [0, 2], [50, 2], [100, 2], [150, 2]]) == 0
    assert candidate(robot = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],factory = [[0, 2], [5, 2], [10, 2], [15, 2], [20, 2]]) == 14
