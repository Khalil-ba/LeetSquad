# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(matrix = [[1]],target = 1) == 1
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6]],target = 12) == 1
    assert candidate(matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]],target = -9) == 1
    assert candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],target = 0) == 36
    assert candidate(matrix = [[1, 2], [3, 4]],target = 3) == 2
    assert candidate(matrix = [[904]],target = 0) == 0
    assert candidate(matrix = [[1, -1, 0], [0, 0, 0], [0, 0, 0]],target = -1) == 6
    assert candidate(matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]],target = 0) == 4
    assert candidate(matrix = [[1, -1], [-1, 1]],target = 0) == 5
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 15) == 4
    assert candidate(matrix = [[1, -1, 1, -1], [-1, 1, -1, 1], [1, -1, 1, -1], [-1, 1, -1, 1]],target = 0) == 64
    assert candidate(matrix = [[-1, 0, 1, -1, 1], [0, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]],target = 0) == 128
    assert candidate(matrix = [[5, 1, 2, 3], [1, 6, 4, 5], [2, 4, 7, 8], [3, 5, 8, 9]],target = 18) == 0
    assert candidate(matrix = [[1, -1, 1, -1], [1, -1, 1, -1], [-1, 1, -1, 1], [-1, 1, -1, 1]],target = 0) == 52
    assert candidate(matrix = [[1, 2], [3, 4], [5, 6], [7, 8]],target = 10) == 2
    assert candidate(matrix = [[-1, 2, -3, 4], [-2, 3, -4, 5], [-3, 4, -5, 6], [-4, 5, -6, 7]],target = 10) == 0
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],target = 45) == 2
    assert candidate(matrix = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]],target = -3) == 6
    assert candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],target = 0) == 100
    assert candidate(matrix = [[-1, 1, -1], [1, -1, 1], [-1, 1, -1]],target = 0) == 20
    assert candidate(matrix = [[10, 20, 10], [20, 30, 20], [10, 20, 10]],target = 60) == 0
    assert candidate(matrix = [[1, 2], [2, 1], [1, 2], [2, 1]],target = 3) == 10
    assert candidate(matrix = [[1, 2], [3, 4], [5, 6], [7, 8]],target = 10) == 2
    assert candidate(matrix = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]],target = 10) == 2
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 15) == 4
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],target = 21) == 4
    assert candidate(matrix = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]],target = 15) == 6
    assert candidate(matrix = [[5, 1, -2, 4], [2, 1, 0, 3], [-1, 3, -1, 2], [0, 2, 1, -1]],target = 3) == 10
    assert candidate(matrix = [[-1, 1, 2, -1], [1, 1, -1, 1], [-2, -2, 1, 2]],target = 0) == 8
    assert candidate(matrix = [[1000, -1000, 1000], [-1000, 1000, -1000], [1000, -1000, 1000]],target = 0) == 20
    assert candidate(matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],target = 4) == 17
    assert candidate(matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]],target = -5) == 2
    assert candidate(matrix = [[1, -1, 0], [0, 1, -1], [-1, 0, 1]],target = 0) == 19
    assert candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],target = 0) == 60
    assert candidate(matrix = [[-1, 2, -3, 4, 5], [2, -1, 3, -4, 6], [-3, 2, -1, 4, -5], [4, -3, 2, -1, 5]],target = 3) == 19
    assert candidate(matrix = [[1, 0, 1], [0, -1, 0], [1, 0, 1]],target = 2) == 4
    assert candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],target = 20) == 1
    assert candidate(matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]],target = 6) == 8
    assert candidate(matrix = [[5, -1, 3], [-3, 0, 5], [3, -2, -1]],target = 4) == 3
    assert candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],target = 0) == 100
    assert candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],target = -15) == 4
    assert candidate(matrix = [[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]],target = 5) == 6
    assert candidate(matrix = [[-10, 20, -30], [40, -50, 60], [-70, 80, -90]],target = -50) == 2
    assert candidate(matrix = [[-1, 0, 1], [2, 3, 4], [5, 6, 7]],target = 10) == 0
    assert candidate(matrix = [[1, -2, 3, -4], [-4, 3, -2, 1], [2, -3, 4, -5], [-5, 4, -3, 2]],target = -6) == 4
    assert candidate(matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]],target = 12) == 3
    assert candidate(matrix = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]],target = 1) == 40
    assert candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],target = 25) == 0
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],target = 30) == 0
    assert candidate(matrix = [[10, -10, 20, -20], [-10, 10, -20, 20], [20, -20, 30, -30], [-20, 20, -30, 30]],target = 0) == 52
    assert candidate(matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],target = 150) == 4
    assert candidate(matrix = [[1, -2, 3, -4, 5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20]],target = 5) == 10
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],target = 60) == 3
    assert candidate(matrix = [[5, 5, 5], [5, 5, 5], [5, 5, 5]],target = 15) == 6
    assert candidate(matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0], [1, 0, 1], [0, 1, 0]],target = 1) == 33
    assert candidate(matrix = [[1, 0, -1, 1], [2, 3, 2, -1], [-1, -1, -1, -1], [1, 1, 1, 1]],target = 1) == 18
    assert candidate(matrix = [[-10, -20, -30], [-20, -30, -40], [-30, -40, -50]],target = -70) == 4
    assert candidate(matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]],target = 2) == 8
    assert candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],target = 30) == 4
    assert candidate(matrix = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],target = 1500) == 4
    assert candidate(matrix = [[-1, 2, -3, 4], [-5, 6, -7, 8], [9, -10, 11, -12], [-13, 14, -15, 16]],target = 0) == 9
    assert candidate(matrix = [[1, 0, 1], [0, -2, 3]],target = 2) == 2
    assert candidate(matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],target = 150) == 4
    assert candidate(matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]],target = 3) == 6
    assert candidate(matrix = [[1, 2, -3, 4], [-1, 0, 2, 1], [3, -2, 1, 4], [0, 1, -1, 2]],target = 5) == 4
    assert candidate(matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6], [6, 5, 4]],target = 9) == 3
    assert candidate(matrix = [[-1, 2, 3], [-4, 5, -6], [7, -8, 9]],target = 5) == 3
    assert candidate(matrix = [[-1, 2, -3, 4, -5], [5, -6, 7, -8, 9], [-9, 10, -11, 12, -13], [14, -15, 16, -17, 18], [-19, 20, -21, 22, -23]],target = 0) == 36
    assert candidate(matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5]],target = 9) == 4
    assert candidate(matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],target = -15) == 4
    assert candidate(matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0], [1, 1, 1], [0, 1, 0]],target = 1) == 30
    assert candidate(matrix = [[1, 2, -1, -4, -20], [2, 3, -2, -3, -15], [3, 4, -3, -2, -10], [4, 5, -4, -1, -5]],target = -5) == 9
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],target = 30) == 2
    assert candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],target = 24) == 3
    assert candidate(matrix = [[10, 20, 30], [20, 30, 40], [30, 40, 50]],target = 70) == 4
    assert candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],target = 0) == 36
    assert candidate(matrix = [[1, 2], [3, 4], [5, 6]],target = 10) == 2
    assert candidate(matrix = [[-1, 2, -3, 4], [2, -2, 1, 1], [-1, 3, -2, 2], [1, -1, 2, -2]],target = 0) == 16
    assert candidate(matrix = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]],target = 2) == 56
    assert candidate(matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]],target = 1) == 16
    assert candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],target = 10) == 3
    assert candidate(matrix = [[1, -1, 1], [-1, 1, -1], [1, -1, 1]],target = 0) == 20
