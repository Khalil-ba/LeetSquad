# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(coordinates = [[0, 0], [0, 1], [0, 2], [0, 3]]) == True
    assert candidate(coordinates = [[-10000, -10000], [0, 0], [10000, 10000]]) == True
    assert candidate(coordinates = [[-4, -3], [1, 0], [3, -1], [0, -1], [-5, 2]]) == False
    assert candidate(coordinates = [[0, 0], [5, 5], [10, 10], [15, 15]]) == True
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 4]]) == False
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 5]]) == False
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]) == False
    assert candidate(coordinates = [[-1, 0], [0, 1], [1, 2], [2, 3]]) == True
    assert candidate(coordinates = [[1, 2], [2, 1], [3, 0], [4, -1], [5, -2]]) == True
    assert candidate(coordinates = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3]]) == True
    assert candidate(coordinates = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]) == True
    assert candidate(coordinates = [[0, 0], [1, 1], [2, 2], [3, 3]]) == True
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == True
    assert candidate(coordinates = [[1, 1], [2, 2], [2, 3]]) == False
    assert candidate(coordinates = [[-4, -3], [-1, 1], [2, 5], [5, 9]]) == True
    assert candidate(coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == True
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == True
    assert candidate(coordinates = [[-1, -1], [0, 0], [1, 1], [2, 2]]) == True
    assert candidate(coordinates = [[0, 1], [1, 3], [-1, -1], [2, 5]]) == True
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 3], [4, 6]]) == False
    assert candidate(coordinates = [[1, 2], [2, 3], [3, 5]]) == False
    assert candidate(coordinates = [[-1, 0], [0, 1], [1, 0], [2, 1], [3, 0]]) == False
    assert candidate(coordinates = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]]) == True
    assert candidate(coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == True
    assert candidate(coordinates = [[-1, 0], [0, 1], [1, 2], [2, 3], [3, 4]]) == True
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == True
    assert candidate(coordinates = [[10, 5], [15, 10], [20, 15], [25, 20]]) == True
    assert candidate(coordinates = [[10000, 10000], [5000, 5000], [0, 0]]) == True
    assert candidate(coordinates = [[2, 4], [2, 5], [2, 6]]) == True
    assert candidate(coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]) == True
    assert candidate(coordinates = [[-1, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == True
    assert candidate(coordinates = [[5, -10], [10, -5], [15, 0], [20, 5], [25, 10]]) == True
    assert candidate(coordinates = [[-1, -2], [-2, -3], [-3, -4], [-4, -5], [-5, -6]]) == True
    assert candidate(coordinates = [[-10, 5], [-5, 10], [0, 15], [5, 20], [10, 25], [15, 30], [20, 35], [25, 40]]) == True
    assert candidate(coordinates = [[-2, -4], [-1, -2], [0, 0], [1, 2], [2, 4]]) == True
    assert candidate(coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == True
    assert candidate(coordinates = [[1000, 2000], [2000, 4000], [3000, 6000], [4000, 8000], [5000, 10000]]) == True
    assert candidate(coordinates = [[10, 20], [20, 40], [30, 60], [40, 80], [50, 100], [60, 120]]) == True
    assert candidate(coordinates = [[1, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9], [10, 11]]) == True
    assert candidate(coordinates = [[-5, -20], [0, -10], [5, 0], [10, 10], [15, 20]]) == True
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 8]]) == False
    assert candidate(coordinates = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]]) == True
    assert candidate(coordinates = [[-1, -2], [-2, -4], [-3, -6], [-4, -8], [-5, -10]]) == True
    assert candidate(coordinates = [[-10, 15], [-5, 10], [0, 5], [5, 0], [10, -5], [15, -10]]) == True
    assert candidate(coordinates = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16]]) == True
    assert candidate(coordinates = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11]]) == True
    assert candidate(coordinates = [[-2, 3], [-1, 4], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10]]) == True
    assert candidate(coordinates = [[10000, 10000], [5000, 5000], [0, 0], [-5000, -5000], [-10000, -10000]]) == True
    assert candidate(coordinates = [[-20, -30], [-10, -15], [0, 0], [10, 15], [20, 30]]) == True
    assert candidate(coordinates = [[-5, 5], [-10, 10], [-15, 15], [-20, 20], [-25, 25], [-30, 30]]) == True
    assert candidate(coordinates = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11], [7, 13], [8, 15]]) == True
    assert candidate(coordinates = [[-5, -10], [0, 0], [5, 10], [10, 20], [15, 30]]) == True
    assert candidate(coordinates = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == True
    assert candidate(coordinates = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35]]) == True
    assert candidate(coordinates = [[-3, -3], [-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2], [3, 3]]) == True
    assert candidate(coordinates = [[-2, 1], [-1, 3], [0, 5], [1, 7], [2, 9], [3, 11]]) == True
    assert candidate(coordinates = [[0, -10000], [10000, -10000], [20000, -10000], [30000, -10000]]) == True
    assert candidate(coordinates = [[-4, -2], [-2, 0], [0, 2], [2, 4], [4, 6]]) == True
    assert candidate(coordinates = [[-100, 100], [-50, 150], [0, 200], [50, 250], [100, 300]]) == True
    assert candidate(coordinates = [[-2, 2], [0, 0], [2, -2], [4, -4], [6, -6]]) == True
    assert candidate(coordinates = [[-1, -2], [1, 0], [3, 2], [5, 4], [7, 6], [9, 8]]) == True
    assert candidate(coordinates = [[-10, 15], [-5, 10], [0, 5], [5, 0], [10, -5]]) == True
    assert candidate(coordinates = [[5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == True
    assert candidate(coordinates = [[0, -10], [0, -5], [0, 0], [0, 5], [0, 10], [0, 15]]) == True
    assert candidate(coordinates = [[100, 200], [200, 400], [300, 600], [400, 800], [500, 1000]]) == True
    assert candidate(coordinates = [[0, 1], [1, 3], [2, 5], [3, 7], [4, 9]]) == True
    assert candidate(coordinates = [[-3, 7], [-2, 5], [-1, 3], [0, 1], [1, -1], [2, -3]]) == True
    assert candidate(coordinates = [[-1, -2], [1, 0], [3, 2], [5, 4], [7, 6], [9, 8], [11, 10]]) == True
    assert candidate(coordinates = [[-5, -5], [0, -2.5], [5, 0], [10, 2.5], [15, 5]]) == True
    assert candidate(coordinates = [[-500, 500], [-250, 750], [0, 1000], [250, 1250], [500, 1500]]) == True
    assert candidate(coordinates = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]]) == True
    assert candidate(coordinates = [[-1, 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == True
    assert candidate(coordinates = [[-10, 0], [-5, 0], [0, 0], [5, 0], [10, 0], [15, 0]]) == True
    assert candidate(coordinates = [[-2, -1], [0, 0], [2, 1], [4, 2], [6, 3], [8, 4]]) == True
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == True
    assert candidate(coordinates = [[-2, -3], [-1, -1], [0, 1], [1, 3], [2, 5], [3, 7]]) == True
    assert candidate(coordinates = [[-3, -3], [-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2], [3, 3]]) == True
    assert candidate(coordinates = [[-100, 200], [-200, 400], [-300, 600], [-400, 800], [-500, 1000]]) == True
    assert candidate(coordinates = [[-5, -10], [0, 0], [5, 10], [10, 20], [15, 30]]) == True
    assert candidate(coordinates = [[-5, -10], [-4, -8], [-3, -6], [-2, -4], [-1, -2], [0, 0]]) == True
    assert candidate(coordinates = [[-5, -5], [0, 0], [5, 5], [10, 10], [15, 15], [20, 20]]) == True
    assert candidate(coordinates = [[-100, 100], [-50, 50], [0, 0], [50, -50], [100, -100]]) == True
    assert candidate(coordinates = [[-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0]]) == True
    assert candidate(coordinates = [[-100, -100], [-50, -50], [0, 0], [50, 50], [100, 100]]) == True
    assert candidate(coordinates = [[-5, 5], [0, 10], [5, 15], [10, 20], [15, 25], [20, 30], [25, 35]]) == True
    assert candidate(coordinates = [[100, -200], [200, -400], [300, -600], [400, -800], [500, -1000]]) == True
    assert candidate(coordinates = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11], [6, 13], [7, 15], [8, 17], [9, 19], [10, 21]]) == True
    assert candidate(coordinates = [[-1, -2], [-2, -4], [-3, -6], [-4, -8], [-5, -10]]) == True
    assert candidate(coordinates = [[100, 100], [200, 200], [300, 300], [400, 401], [500, 500]]) == False
    assert candidate(coordinates = [[-100, 100], [100, -100], [0, 0]]) == True
    assert candidate(coordinates = [[2, 3], [4, 6], [6, 9], [8, 12], [10, 15]]) == True
    assert candidate(coordinates = [[-3, 3], [-6, 6], [-9, 9], [-12, 12], [-15, 15]]) == True
    assert candidate(coordinates = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]) == False
    assert candidate(coordinates = [[-10, -20], [0, 0], [10, 20], [20, 40], [30, 60]]) == True
    assert candidate(coordinates = [[1, 1], [3, 5], [5, 9], [7, 13], [9, 17]]) == True
    assert candidate(coordinates = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]) == True
    assert candidate(coordinates = [[-1, -5], [0, -2], [1, 1], [2, 4], [3, 7], [4, 10]]) == True
    assert candidate(coordinates = [[0, 1000], [1000, 1000], [2000, 1000], [3000, 1000], [4000, 1000]]) == True
    assert candidate(coordinates = [[-2, -3], [-1, -1], [0, 1], [1, 3], [2, 5]]) == True
    assert candidate(coordinates = [[1, 2], [2, 4], [4, 8], [8, 16], [16, 32], [32, 64]]) == True
    assert candidate(coordinates = [[-100, -200], [-200, -400], [-300, -600], [-400, -800], [-500, -1000]]) == True
    assert candidate(coordinates = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14]]) == True
    assert candidate(coordinates = [[1, 2], [4, 6], [7, 10], [10, 14], [13, 18], [16, 22], [19, 26]]) == True
    assert candidate(coordinates = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == True
    assert candidate(coordinates = [[-3, -6], [1, -2], [5, 2], [7, 3]]) == False
    assert candidate(coordinates = [[-100, 0], [0, 0], [100, 0], [200, 0], [300, 0]]) == True
    assert candidate(coordinates = [[-1000, 2000], [0, 0], [1000, -2000]]) == True
    assert candidate(coordinates = [[-5, -10], [0, 0], [5, 10], [10, 20], [15, 30], [20, 40]]) == True
    assert candidate(coordinates = [[-10, 0], [0, 5], [10, 10], [20, 15], [30, 20], [40, 25], [50, 30], [60, 35]]) == True
    assert candidate(coordinates = [[-1, 1], [0, 0], [1, -1], [2, -2], [3, -3]]) == True
    assert candidate(coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == True
    assert candidate(coordinates = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]) == True
    assert candidate(coordinates = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == True
    assert candidate(coordinates = [[-10, -10], [-5, -5], [0, 0], [5, 5], [10, 10]]) == True
    assert candidate(coordinates = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == True
    assert candidate(coordinates = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 6], [5, 8]]) == False
    assert candidate(coordinates = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 15]]) == False
    assert candidate(coordinates = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80]]) == True
    assert candidate(coordinates = [[-1, -1], [1, 1], [3, 3], [5, 5], [7, 7], [9, 9]]) == True
    assert candidate(coordinates = [[-1000, 0], [-500, 0], [0, 0], [500, 0], [1000, 0]]) == True
    assert candidate(coordinates = [[-10000, 10000], [-5000, 10000], [0, 10000], [5000, 10000], [10000, 10000]]) == True
    assert candidate(coordinates = [[5, 3], [10, 6], [15, 9], [20, 12], [25, 15]]) == True
    assert candidate(coordinates = [[1, 1], [2, 2], [3, 3], [4, 3], [5, 5]]) == False
    assert candidate(coordinates = [[-2, 4], [-1, 2], [0, 0], [1, -2], [2, -4]]) == True
    assert candidate(coordinates = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == True
