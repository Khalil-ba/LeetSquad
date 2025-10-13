# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr = [10, 20, 30, 40, 50],pieces = [[10, 20], [30, 40, 50]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5],pieces = [[2, 3], [1, 4], [5]]) == False
    assert candidate(arr = [91, 4, 64, 78],pieces = [[78], [4, 64], [91]]) == True
    assert candidate(arr = [49, 18, 16],pieces = [[16, 18, 49]]) == False
    assert candidate(arr = [15, 88],pieces = [[88], [15]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5],pieces = [[2], [4, 5], [3], [1]]) == True
    assert candidate(arr = [5, 9, 13, 17, 21, 25],pieces = [[5, 9, 13], [17, 21, 25]]) == True
    assert candidate(arr = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],pieces = [[101, 102], [103, 104], [105, 106], [107, 108], [109, 110]]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14],pieces = [[2, 4], [6, 8], [10, 12], [14]]) == True
    assert candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],pieces = [[100, 99], [98, 97], [96, 95, 94], [93, 92], [91]]) == True
    assert candidate(arr = [91, 4, 64, 78, 100, 50],pieces = [[78, 100], [91, 4], [64], [50]]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],pieces = [[1, 3, 5, 7], [9, 11], [13, 15, 17, 19], [21, 23, 25], [27, 29]]) == True
    assert candidate(arr = [8, 16, 24, 32, 40, 48, 56, 64],pieces = [[8, 16, 24], [32, 40, 48], [56, 64]]) == True
    assert candidate(arr = [100, 200, 300, 400, 500, 600],pieces = [[100, 200], [300, 400], [500, 600]]) == True
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99],pieces = [[11, 22], [33, 44, 55], [66, 77, 88, 99]]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40],pieces = [[5, 10, 15], [20, 25], [30, 35, 40]]) == True
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pieces = [[100], [200, 300], [400, 500, 600], [700, 800], [900, 1000]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pieces = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],pieces = [[1, 3, 5], [7, 9, 11], [13, 15, 17, 19]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pieces = [[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]) == True
    assert candidate(arr = [23, 32, 45, 54, 67, 76, 89, 98],pieces = [[23, 32], [45, 54, 67], [76, 89], [98]]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],pieces = [[1, 3], [5, 7, 9], [11, 13], [15, 17, 19]]) == True
    assert candidate(arr = [3, 1, 2, 5, 4],pieces = [[3, 1], [2, 5], [4]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9],pieces = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]) == True
    assert candidate(arr = [8, 6, 7, 5, 3, 0, 9],pieces = [[8, 6], [7, 5], [3, 0], [9]]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pieces = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]) == True
    assert candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],pieces = [[100, 99], [98, 97, 96], [95, 94, 93], [92, 91]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pieces = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11], [12, 13, 14, 15]]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pieces = [[2, 4], [6, 8, 10], [12, 14], [16, 18, 20]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pieces = [[1, 2, 3], [4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14, 15]]) == True
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],pieces = [[9], [8], [7], [6], [5], [4], [3], [2], [1]]) == True
    assert candidate(arr = [42, 13, 56, 78, 91, 100],pieces = [[42], [13, 56], [78], [91, 100]]) == True
    assert candidate(arr = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],pieces = [[21, 22], [23, 24], [25, 26], [27, 28], [29, 30]]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90],pieces = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]) == True
    assert candidate(arr = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],pieces = [[12, 14, 16], [18, 20], [22, 24, 26, 28, 30]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pieces = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == True
    assert candidate(arr = [99, 88, 77, 66, 55, 44, 33, 22, 11],pieces = [[99], [88], [77], [66], [55], [44], [33], [22], [11]]) == True
    assert candidate(arr = [20, 30, 10, 50, 40],pieces = [[20, 30], [10, 50], [40]]) == True
    assert candidate(arr = [7, 14, 28, 21, 42],pieces = [[7, 14, 28], [21, 42]]) == True
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],pieces = [[100, 90], [80, 70, 60, 50], [40, 30, 20, 10]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pieces = [[3, 4], [1, 2], [7, 8], [5, 6], [9, 10]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],pieces = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == True
    assert candidate(arr = [42, 43, 44, 45, 46, 47, 48, 49, 50],pieces = [[42, 43], [44, 45, 46], [47, 48], [49, 50]]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],pieces = [[1, 3, 5], [7, 9], [11, 13], [15, 17, 19]]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40],pieces = [[5], [10, 15], [20, 25, 30], [35, 40]]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15],pieces = [[1, 3, 5], [7, 9], [11, 13, 15]]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],pieces = [[1], [3, 5], [7, 9], [11, 13], [15, 17, 19]]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90],pieces = [[10], [20], [30], [40], [50], [60], [70], [80], [90]]) == True
    assert candidate(arr = [101, 102, 103, 104, 105, 106],pieces = [[101, 102, 103], [104, 105], [106]]) == True
    assert candidate(arr = [2, 5, 3, 8, 9, 4],pieces = [[2, 5], [3], [8, 9], [4]]) == True
    assert candidate(arr = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],pieces = [[99, 98, 97], [96, 95, 94], [93, 92, 91, 90]]) == True
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27],pieces = [[3, 6, 9], [12, 15], [18, 21, 24, 27]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9],pieces = [[1, 2], [3, 4, 5], [6, 7, 8], [9]]) == True
    assert candidate(arr = [3, 5, 7, 9, 11, 13, 15],pieces = [[3, 5, 7], [9, 11], [13, 15]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pieces = [[1, 2], [3, 4, 5], [6, 7], [8, 9, 10]]) == True
    assert candidate(arr = [3, 5, 7, 9, 11, 13, 15],pieces = [[3, 5, 7], [9], [11, 13, 15]]) == True
    assert candidate(arr = [100, 99, 98, 97, 96],pieces = [[97, 98], [96], [99], [100]]) == False
    assert candidate(arr = [7, 14, 21, 28, 35, 42],pieces = [[7], [14], [21], [28], [35], [42]]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30],pieces = [[10, 15], [5], [20, 25, 30]]) == True
    assert candidate(arr = [5, 6, 1, 2, 3, 4],pieces = [[5, 6], [1, 2], [3, 4]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pieces = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == True
    assert candidate(arr = [100, 99, 98, 97, 96, 95],pieces = [[100], [99, 98], [97, 96, 95]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pieces = [[1, 2], [3, 4, 5], [6, 7, 8, 9, 10]]) == True
    assert candidate(arr = [100, 99, 98, 97, 96, 95],pieces = [[100, 99], [98, 97], [96, 95]]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],pieces = [[1, 3, 5], [7, 9, 11], [13, 15, 17], [19, 21]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pieces = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35],pieces = [[5, 10, 15], [20], [25, 30, 35]]) == True
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99],pieces = [[11, 22, 33], [44, 55], [66, 77, 88, 99]]) == True
    assert candidate(arr = [70, 80, 90, 100, 110, 120],pieces = [[70, 80], [90, 100], [110, 120]]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70],pieces = [[10, 20], [30, 40, 50], [60, 70]]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],pieces = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110], [120, 130, 140, 150]]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pieces = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]) == True
    assert candidate(arr = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34],pieces = [[25, 26], [27, 28, 29], [30, 31, 32, 33], [34]]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],pieces = [[5, 10, 15], [20, 25, 30], [35, 40, 45], [50]]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16],pieces = [[2, 4], [6, 8, 10], [12, 14, 16]]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pieces = [[2, 4], [6, 8, 10], [12, 14], [16, 18, 20]]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pieces = [[2, 4, 6], [8, 10, 12], [14, 16, 18], [20]]) == True
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21],pieces = [[3, 6], [9, 12], [15, 18], [21]]) == True
    assert candidate(arr = [5, 4, 3, 2, 1],pieces = [[5], [4, 3], [2, 1]]) == True
    assert candidate(arr = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],pieces = [[31, 32], [33, 34], [35, 36], [37, 38], [39, 40]]) == True
    assert candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],pieces = [[100, 99], [98, 97], [96, 95], [94, 93], [92, 91]]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pieces = [[2, 4, 6], [8, 10], [12, 14, 16, 18, 20]]) == True
    assert candidate(arr = [23, 29, 20, 32, 45, 67],pieces = [[23, 29, 20], [32], [45, 67]]) == True
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56],pieces = [[7, 14, 21, 28], [35, 42], [49, 56]]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9],pieces = [[1, 2], [3, 4], [5, 6], [7, 8], [9]]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],pieces = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]) == True
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],pieces = [[9, 8, 7], [6, 5], [4, 3, 2], [1]]) == True
    assert candidate(arr = [5, 1, 3, 7, 8, 2, 4, 9, 6],pieces = [[1, 3], [5], [7, 8], [2, 4], [9, 6]]) == True
    assert candidate(arr = [100, 200, 300, 400, 500],pieces = [[100], [200, 300], [400, 500]]) == True
    assert candidate(arr = [5, 3, 8, 9, 10, 15, 20],pieces = [[5], [3, 8, 9], [10, 15], [20]]) == True
    assert candidate(arr = [4, 2, 5, 3, 6, 1, 7],pieces = [[4, 2], [5], [3, 6], [1, 7]]) == True
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99],pieces = [[11, 22], [33, 44], [55, 66], [77, 88, 99]]) == True
    assert candidate(arr = [42, 24, 66, 33, 55, 77],pieces = [[42], [24, 66], [33, 55], [77]]) == True
    assert candidate(arr = [8, 6, 7, 5, 3, 0, 9],pieces = [[8, 6], [7, 5, 3], [0, 9]]) == True
    assert candidate(arr = [5, 1, 3, 9, 7, 6],pieces = [[5, 1], [3, 9], [7, 6]]) == True
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100],pieces = [[11, 22], [33, 44], [55, 66], [77, 88], [99, 100]]) == True
    assert candidate(arr = [60, 70, 80, 90, 100, 110, 120],pieces = [[60, 70, 80], [90, 100], [110, 120]]) == True
    assert candidate(arr = [8, 6, 7, 5, 3, 0, 9],pieces = [[8, 6, 7], [5, 3], [0, 9]]) == True
    assert candidate(arr = [23, 45, 67, 89, 90, 12, 34, 56],pieces = [[23, 45], [67, 89, 90], [12, 34, 56]]) == True
