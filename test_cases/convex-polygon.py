# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(points = [[1, 0], [0, 0], [0, 1]]) == True
    assert candidate(points = [[1, 1], [2, 3], [3, 2], [4, 1], [4, 3], [3, 4], [1, 4]]) == False
    assert candidate(points = [[-1, -1], [1, 1], [0, 0]]) == True
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [1, 0], [0, 1]]) == False
    assert candidate(points = [[0, 0], [1, 0], [2, 1], [1, 1]]) == True
    assert candidate(points = [[0, 0], [1, 0], [1, 1], [0, 1]]) == True
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4]]) == True
    assert candidate(points = [[-1, 0], [0, 1], [1, 0], [0, -1]]) == True
    assert candidate(points = [[1, 2], [2, 3], [3, 1]]) == True
    assert candidate(points = [[1, 1], [1, 3], [3, 3], [3, 1]]) == True
    assert candidate(points = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]) == False
    assert candidate(points = [[1, 1], [2, 3], [3, 2]]) == True
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0]]) == True
    assert candidate(points = [[1, 1], [2, 2], [3, 1], [2, 0]]) == True
    assert candidate(points = [[1, 2], [2, 3], [3, 1], [4, 2], [5, 1]]) == False
    assert candidate(points = [[1, 1], [2, 3], [3, 2], [4, 4], [5, 3]]) == False
    assert candidate(points = [[0, 0], [0, 5], [5, 5], [5, 0]]) == True
    assert candidate(points = [[0, 0], [2, 0], [2, 2], [0, 2], [1, 1]]) == False
    assert candidate(points = [[10, 0], [10, 10], [0, 10], [0, 0], [5, 5], [2, 2], [8, 8]]) == False
    assert candidate(points = [[-5, 0], [-4, -1], [-2, 1], [2, 0], [3, -1], [1, -2]]) == False
    assert candidate(points = [[1, 1], [3, 3], [2, 2], [4, 4], [3, 5], [2, 4], [1, 3]]) == True
    assert candidate(points = [[0, 0], [2, 0], [3, 1], [2, 2], [1, 2], [0, 2], [-1, 1], [0, 0]]) == True
    assert candidate(points = [[-5, -5], [-5, 5], [5, 5], [0, 0], [5, -5]]) == False
    assert candidate(points = [[0, 0], [0, 4], [2, 4], [2, 0], [1, 1], [1, 3]]) == False
    assert candidate(points = [[1, 0], [2, 2], [3, 1], [2, -1], [1, -1], [0, 1]]) == False
    assert candidate(points = [[1, 1], [2, 1], [2, 2], [3, 2], [3, 3], [2, 3], [2, 4], [1, 4], [1, 3], [0, 3], [0, 2], [1, 2]]) == False
    assert candidate(points = [[0, 0], [1, 0], [1, 1], [0, 1], [0.5, 0.5]]) == False
    assert candidate(points = [[0, 0], [0, 1], [1, 1], [1, 0], [0.5, 0.5], [0.5, 0.25]]) == False
    assert candidate(points = [[-5, 0], [-5, 5], [0, 5], [0, 0], [5, 0], [5, 5]]) == False
    assert candidate(points = [[0, 0], [2, 1], [2, 3], [1, 4], [-1, 3], [-1, 1]]) == True
    assert candidate(points = [[0, 0], [1, 2], [2, 0], [1, 1], [0, 2]]) == False
    assert candidate(points = [[-5, -5], [5, 5], [5, -5], [-5, 5]]) == False
    assert candidate(points = [[-3, 0], [0, 3], [3, 0], [0, -3]]) == True
    assert candidate(points = [[1, 0], [2, 1], [1, 2], [0, 1], [1, 0]]) == True
    assert candidate(points = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 0]]) == True
    assert candidate(points = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [8, 9], [6, 7], [4, 5]]) == True
    assert candidate(points = [[5, 0], [3, 2], [0, 0], [1, 2], [2, 0], [4, 2], [3, 4]]) == False
    assert candidate(points = [[1, 0], [0, 1], [-1, 0], [0, -1], [0.5, 0.5]]) == False
    assert candidate(points = [[0, 0], [1, 2], [2, 2], [2, 3], [1, 4], [0, 3], [0, 2]]) == False
    assert candidate(points = [[-4, 0], [-2, -2], [-2, -4], [0, -2], [2, -4], [2, -2], [4, 0], [2, 2], [2, 4], [0, 2], [-2, 4]]) == False
    assert candidate(points = [[-1, -1], [-1, 2], [2, -1], [2, 2]]) == False
    assert candidate(points = [[-3, -1], [-2, -3], [-1, -2], [1, 0], [2, 1], [0, -2]]) == False
    assert candidate(points = [[-1000, -1000], [-1000, 0], [0, 0], [0, -1000], [500, 500]]) == False
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [1, 3], [0, 2], [0, 1]]) == True
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 6], [3, 5], [2, 6], [1, 5]]) == False
    assert candidate(points = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2], [-1, 1]]) == True
    assert candidate(points = [[0, 0], [0, 10], [5, 5], [10, 10], [10, 0]]) == False
    assert candidate(points = [[-2, -2], [-2, 2], [2, 2], [2, -2], [0, 1]]) == False
    assert candidate(points = [[0, 0], [5, 0], [5, 5], [0, 5], [2, 2], [3, 3]]) == True
    assert candidate(points = [[1, 1], [2, 2], [3, 1], [2, 0], [1, 1]]) == True
    assert candidate(points = [[0, 0], [2, 0], [2, 2], [1, 3], [0, 2]]) == True
    assert candidate(points = [[1, 1], [2, 2], [3, 1], [2, 0], [1, 0], [0, 1]]) == False
    assert candidate(points = [[1, 1], [2, 2], [3, 1], [2, -1], [1, -1], [0, 0], [1, 0], [2, 0], [3, 0]]) == False
    assert candidate(points = [[-1, 1], [-2, 1], [-3, 0], [-2, -1], [-1, -1], [0, -1], [0, 1]]) == True
    assert candidate(points = [[0, 0], [2, 0], [1, 1], [1, 0]]) == False
    assert candidate(points = [[1, 2], [3, 4], [5, 3], [4, 1], [2, 2], [4, 5]]) == False
    assert candidate(points = [[1, 1], [2, 3], [3, 2], [2, 1], [1, 2]]) == False
    assert candidate(points = [[-1, 0], [0, 1], [1, 0], [0, -1], [-0.5, 0.5]]) == False
    assert candidate(points = [[-1, 0], [1, 0], [0, 1], [-1, -1], [1, -1]]) == False
    assert candidate(points = [[10, 0], [10, 10], [0, 10], [5, 5], [0, 0]]) == False
    assert candidate(points = [[-1, -1], [1, -1], [1, 1], [-1, 1], [0, 0]]) == False
    assert candidate(points = [[-3, 2], [-2, -1], [-1, 2], [0, -1], [1, 2], [2, -1], [3, 2]]) == False
    assert candidate(points = [[5, 0], [5, 4], [1, 4], [0, 2], [1, 0], [2, 0], [3, 0], [4, 0]]) == True
    assert candidate(points = [[-1, 1], [0, 2], [1, 1], [0, 0]]) == True
    assert candidate(points = [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [1, 2], [0, 2], [-1, 2], [-1, 1], [-1, 0]]) == False
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == True
    assert candidate(points = [[0, 0], [1, 1], [2, 0], [2, 2], [1, 3], [0, 2]]) == False
    assert candidate(points = [[0, 0], [1, 0], [1, 1], [0, 1], [-1, 0]]) == True
    assert candidate(points = [[0, 0], [1, 0], [2, 1], [2, 2], [1, 3], [0, 2]]) == True
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [1, 1], [0, 1], [0.5, 0.5], [1.5, 0.5]]) == False
    assert candidate(points = [[1, 1], [2, 2], [3, 1], [4, 2], [5, 1], [6, 2], [7, 1]]) == False
    assert candidate(points = [[0, 0], [5, 0], [5, 5], [0, 5], [-2, 2]]) == True
    assert candidate(points = [[0, 0], [1, 1], [2, 0], [1, -1], [0, -1], [0, 0]]) == True
    assert candidate(points = [[-2, -2], [-1, -1], [-2, 0], [0, -2], [0, 0]]) == True
    assert candidate(points = [[10, 10], [20, 10], [20, 20], [15, 25], [10, 20], [10, 10]]) == True
    assert candidate(points = [[0, 0], [1, 0], [2, 1], [2, 2], [3, 2], [3, 3], [2, 4], [1, 3], [0, 2]]) == False
    assert candidate(points = [[0, 0], [1, 1], [2, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]) == False
    assert candidate(points = [[-5, -5], [-4, -4], [-3, -5], [-4, -6]]) == True
    assert candidate(points = [[-2, 0], [-3, -1], [-1, -1], [-1, -2], [-2, -2], [-3, -2]]) == False
    assert candidate(points = [[-3, 0], [-2, 1], [-1, 0], [0, 1], [1, 0], [2, 1], [3, 0], [2, -1], [1, 0], [0, -1], [-1, 0], [-2, -1]]) == False
    assert candidate(points = [[0, 0], [2, 0], [3, 2], [2, 4], [0, 4], [1, 2]]) == False
    assert candidate(points = [[1, 2], [3, 4], [5, 3], [4, 1], [2, 3]]) == False
    assert candidate(points = [[1, 1], [2, 2], [3, 1], [3, 0], [2, -1], [1, -1], [0, 0]]) == True
    assert candidate(points = [[0, 0], [2, 0], [3, 1], [2, 2], [0, 2], [-1, 1]]) == True
    assert candidate(points = [[-5, 0], [-5, 5], [0, 5], [5, 0], [5, -5], [0, -5]]) == True
    assert candidate(points = [[1, 1], [2, 1], [3, 2], [4, 1], [3, 0], [2, 0], [1, 0]]) == False
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 1], [3, 0], [2, -1], [1, -1], [0, -1]]) == True
    assert candidate(points = [[0, 0], [1, 0], [1, 1], [0, 1], [0.5, 0.25], [0.25, 0.5]]) == False
    assert candidate(points = [[0, 0], [2, 0], [3, 1], [3, 2], [2, 3], [1, 2], [0, 1], [1, 1]]) == False
    assert candidate(points = [[1, 1], [2, 3], [4, 5], [5, 4], [4, 2], [3, 1]]) == True
    assert candidate(points = [[1, 0], [2, 0], [3, 1], [2, 1], [1, 2], [0, 1], [0, 0]]) == False
    assert candidate(points = [[0, 0], [2, 1], [3, 3], [1, 4], [-1, 3], [-2, 1]]) == True
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4, 3], [3, 2], [2, 1]]) == True
    assert candidate(points = [[0, 0], [5, 0], [5, 5], [2, 5], [2, 3], [0, 3]]) == False
    assert candidate(points = [[0, 0], [5, 0], [5, 5], [0, 5], [2, 2]]) == False
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == True
    assert candidate(points = [[1, 0], [2, 1], [2, 3], [1, 4], [0, 3], [0, 1]]) == True
    assert candidate(points = [[1, 1], [4, 1], [4, 5], [2, 5], [2, 3], [0, 5], [0, 1], [2, 1]]) == False
    assert candidate(points = [[-1, 1], [-1, 3], [2, 2], [1, 0], [0, 0]]) == True
    assert candidate(points = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 1], [-1, 1], [-1, 2], [-2, 1]]) == False
    assert candidate(points = [[100, 100], [100, 200], [200, 200], [200, 150], [150, 150], [150, 100]]) == False
    assert candidate(points = [[0, 0], [0, 1], [1, 1], [2, 1], [2, 0], [1, 0], [1, 1], [0, 1]]) == False
    assert candidate(points = [[0, 0], [4, 0], [4, 4], [2, 5], [0, 4]]) == True
    assert candidate(points = [[-1, -1], [1, -1], [1, 1], [-1, 1], [0, 2]]) == False
    assert candidate(points = [[0, 0], [1, 0], [1, 1], [0.5, 2], [0, 1]]) == True
    assert candidate(points = [[1, 2], [2, 3], [3, 2], [2, 1], [1, 2], [2, 3], [3, 2], [2, 1]]) == True
    assert candidate(points = [[-1, 1], [-2, 0], [-1, -1], [1, -1], [2, 0], [1, 1]]) == True
    assert candidate(points = [[1, 0], [0, 1], [1, 1], [0, -1], [-1, 0]]) == False
    assert candidate(points = [[-5, -5], [-5, 0], [0, 0], [0, -5]]) == True
    assert candidate(points = [[-2, -2], [-2, -1], [-1, -2], [-1, -1], [0, 0], [0, 1], [1, 0], [1, 1]]) == False
    assert candidate(points = [[-1, 1], [-2, 2], [-1, 3], [1, 3], [2, 2], [1, 1]]) == True
    assert candidate(points = [[1, 1], [2, 2], [3, 1], [3, 2], [2, 3], [1, 2]]) == False
