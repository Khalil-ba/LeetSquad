# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(height = 6,width = 6,tree = [3, 3],squirrel = [5, 0],nuts = [[3, 3], [1, 1], [5, 5], [0, 0]]) == 27
    assert candidate(height = 10,width = 10,tree = [5, 5],squirrel = [0, 0],nuts = [[9, 9], [0, 0], [5, 5]]) == 26
    assert candidate(height = 100,width = 100,tree = [50, 50],squirrel = [99, 99],nuts = [[49, 49], [51, 51]]) == 102
    assert candidate(height = 10,width = 10,tree = [5, 5],squirrel = [0, 0],nuts = [[9, 9], [5, 5], [0, 0]]) == 26
    assert candidate(height = 10,width = 10,tree = [5, 5],squirrel = [0, 0],nuts = [[9, 9], [8, 8], [7, 7]]) == 46
    assert candidate(height = 6,width = 8,tree = [3, 4],squirrel = [0, 0],nuts = [[1, 2], [3, 5], [5, 6], [4, 1]]) == 25
    assert candidate(height = 1,width = 3,tree = [0, 1],squirrel = [0, 0],nuts = [[0, 2]]) == 3
    assert candidate(height = 3,width = 3,tree = [1, 1],squirrel = [2, 2],nuts = [[0, 0], [2, 2]]) == 6
    assert candidate(height = 3,width = 3,tree = [1, 1],squirrel = [2, 2],nuts = [[0, 0], [1, 0], [0, 1]]) == 10
    assert candidate(height = 5,width = 7,tree = [2, 2],squirrel = [4, 4],nuts = [[3, 0], [2, 5]]) == 12
    assert candidate(height = 10,width = 10,tree = [5, 5],squirrel = [0, 0],nuts = [[9, 9], [0, 9], [9, 0]]) == 52
    assert candidate(height = 10,width = 10,tree = [5, 5],squirrel = [9, 9],nuts = [[5, 5], [8, 8], [4, 4]]) == 12
    assert candidate(height = 4,width = 4,tree = [2, 2],squirrel = [3, 3],nuts = [[0, 0], [3, 3], [2, 2], [1, 1]]) == 14
    assert candidate(height = 3,width = 3,tree = [1, 1],squirrel = [0, 0],nuts = [[2, 2], [1, 0]]) == 6
    assert candidate(height = 3,width = 3,tree = [1, 1],squirrel = [0, 0],nuts = [[2, 2], [1, 2], [2, 1]]) == 10
    assert candidate(height = 4,width = 4,tree = [2, 2],squirrel = [3, 3],nuts = [[1, 1], [1, 2], [2, 1]]) == 10
    assert candidate(height = 3,width = 3,tree = [1, 1],squirrel = [0, 0],nuts = [[2, 2], [1, 1], [0, 0]]) == 6
    assert candidate(height = 8,width = 8,tree = [4, 4],squirrel = [7, 7],nuts = [[1, 1], [1, 7], [7, 1], [7, 7], [2, 2], [2, 6], [6, 2], [6, 6], [3, 3], [5, 5], [4, 1], [4, 7], [1, 4], [7, 4]]) == 106
    assert candidate(height = 100,width = 100,tree = [50, 50],squirrel = [1, 1],nuts = [[99, 99], [80, 80], [70, 70], [60, 60], [50, 50], [40, 40], [30, 30], [20, 20], [10, 10], [0, 0]]) == 938
    assert candidate(height = 30,width = 30,tree = [15, 15],squirrel = [10, 10],nuts = [[20, 20], [10, 20], [20, 10], [10, 10], [15, 20], [20, 15], [15, 10]]) == 100
    assert candidate(height = 15,width = 15,tree = [7, 7],squirrel = [0, 0],nuts = [[14, 14], [13, 13], [12, 12], [11, 11], [10, 10]]) == 114
    assert candidate(height = 50,width = 50,tree = [25, 25],squirrel = [49, 49],nuts = [[0, 0], [0, 49], [49, 0], [25, 25], [24, 24], [26, 26]]) == 304
    assert candidate(height = 100,width = 100,tree = [50, 50],squirrel = [0, 0],nuts = [[99, 99], [98, 98], [97, 97], [96, 96], [95, 95]]) == 1040
    assert candidate(height = 20,width = 15,tree = [10, 10],squirrel = [1, 1],nuts = [[5, 5], [10, 5], [5, 10], [15, 15], [0, 0], [19, 14]]) == 108
    assert candidate(height = 20,width = 20,tree = [10, 10],squirrel = [0, 0],nuts = [[19, 19], [18, 18], [17, 17], [16, 16], [15, 15]]) == 160
    assert candidate(height = 20,width = 20,tree = [10, 10],squirrel = [0, 0],nuts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 344
    assert candidate(height = 50,width = 50,tree = [25, 25],squirrel = [0, 0],nuts = [[25, 0], [0, 25], [25, 50], [50, 25], [10, 10], [40, 40], [15, 15], [35, 35], [20, 20], [30, 30]]) == 430
    assert candidate(height = 60,width = 60,tree = [30, 30],squirrel = [55, 5],nuts = [[25, 25], [10, 10], [40, 40], [5, 5], [55, 55], [15, 15], [45, 45], [20, 20], [35, 35], [50, 50]]) == 600
    assert candidate(height = 15,width = 15,tree = [7, 7],squirrel = [14, 14],nuts = [[5, 5], [10, 10], [2, 2], [12, 12], [0, 0], [14, 0], [0, 14], [8, 8]]) == 142
    assert candidate(height = 80,width = 80,tree = [40, 40],squirrel = [5, 75],nuts = [[20, 20], [60, 60], [10, 10], [70, 70], [30, 30], [50, 50], [15, 15], [65, 65], [25, 25], [55, 55], [35, 35], [45, 45]]) == 850
    assert candidate(height = 30,width = 15,tree = [15, 7],squirrel = [1, 1],nuts = [[25, 5], [10, 10], [1, 14], [29, 14], [14, 1], [29, 1]]) == 170
    assert candidate(height = 50,width = 50,tree = [25, 25],squirrel = [0, 50],nuts = [[20, 20], [30, 30], [10, 10], [40, 40], [25, 25], [15, 15], [35, 35], [5, 5], [45, 45]]) == 410
    assert candidate(height = 50,width = 50,tree = [30, 30],squirrel = [0, 0],nuts = [[45, 45], [46, 46], [47, 47], [48, 48], [49, 49], [40, 40], [35, 35], [30, 30], [25, 25], [20, 20]]) == 480
    assert candidate(height = 60,width = 60,tree = [30, 30],squirrel = [59, 59],nuts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 958
    assert candidate(height = 20,width = 20,tree = [10, 10],squirrel = [1, 1],nuts = [[2, 2], [18, 18], [5, 5], [15, 15], [0, 0], [19, 19]]) == 162
    assert candidate(height = 100,width = 100,tree = [50, 50],squirrel = [99, 99],nuts = [[0, 0], [99, 0], [0, 99], [50, 50], [49, 49], [51, 51], [50, 49], [50, 51], [49, 50], [51, 50], [50, 48], [50, 52], [48, 50], [52, 50]]) == 628
    assert candidate(height = 50,width = 50,tree = [25, 25],squirrel = [40, 40],nuts = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 850
    assert candidate(height = 10,width = 10,tree = [5, 5],squirrel = [0, 9],nuts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 0], [9, 0], [0, 9]]) == 127
    assert candidate(height = 10,width = 10,tree = [5, 5],squirrel = [1, 1],nuts = [[9, 9], [8, 8], [7, 7], [6, 6], [5, 4], [4, 5]]) == 50
    assert candidate(height = 30,width = 30,tree = [15, 15],squirrel = [29, 29],nuts = [[14, 14], [16, 16], [15, 14], [15, 16], [14, 15], [16, 15]]) == 40
    assert candidate(height = 12,width = 12,tree = [6, 6],squirrel = [11, 11],nuts = [[0, 0], [11, 0], [0, 11], [3, 3], [8, 8], [6, 1], [1, 6]]) == 108
    assert candidate(height = 90,width = 90,tree = [45, 45],squirrel = [10, 10],nuts = [[30, 30], [60, 60], [15, 15], [75, 75], [20, 20], [65, 65], [25, 25], [70, 70], [35, 35], [50, 50], [80, 80]]) == 870
    assert candidate(height = 40,width = 40,tree = [20, 20],squirrel = [1, 1],nuts = [[39, 39], [38, 38], [37, 37], [36, 36], [35, 35], [34, 34], [33, 33]]) == 486
    assert candidate(height = 12,width = 12,tree = [6, 6],squirrel = [11, 0],nuts = [[5, 5], [7, 7], [3, 3], [9, 9], [2, 2], [10, 10], [1, 1], [8, 8], [4, 4], [6, 0], [0, 6], [11, 11]]) == 143
    assert candidate(height = 20,width = 20,tree = [10, 10],squirrel = [0, 0],nuts = [[5, 5], [15, 15], [2, 18], [18, 2], [10, 0], [0, 10]]) == 144
    assert candidate(height = 10,width = 10,tree = [4, 4],squirrel = [9, 0],nuts = [[0, 0], [0, 9], [9, 0], [9, 9], [4, 4]]) == 63
    assert candidate(height = 15,width = 15,tree = [7, 7],squirrel = [14, 14],nuts = [[7, 0], [7, 14], [0, 7], [14, 7], [5, 5], [10, 10]]) == 76
    assert candidate(height = 15,width = 30,tree = [7, 15],squirrel = [0, 0],nuts = [[0, 30], [1, 29], [2, 28], [3, 27], [4, 26], [5, 25], [6, 24], [7, 23], [8, 22], [9, 21], [10, 20], [11, 19], [12, 18], [13, 17], [14, 16]]) == 360
    assert candidate(height = 40,width = 40,tree = [20, 20],squirrel = [5, 35],nuts = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19], [20, 20]]) == 230
    assert candidate(height = 8,width = 8,tree = [4, 4],squirrel = [7, 0],nuts = [[1, 1], [2, 2], [3, 3], [5, 5], [6, 6], [7, 7], [0, 0], [1, 7], [7, 1], [3, 6]]) == 89
    assert candidate(height = 40,width = 40,tree = [20, 20],squirrel = [39, 0],nuts = [[19, 19], [21, 21], [39, 39], [0, 0], [1, 1], [38, 38], [2, 2], [37, 37], [3, 3], [36, 36], [4, 4], [35, 35], [5, 5], [34, 34], [6, 6], [33, 33], [7, 7], [32, 32], [8, 8], [31, 31], [9, 9], [30, 30], [10, 10], [29, 29], [11, 11], [28, 28]]) == 1351
    assert candidate(height = 12,width = 12,tree = [6, 6],squirrel = [0, 0],nuts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [0, 11], [11, 0]]) == 156
    assert candidate(height = 30,width = 30,tree = [15, 15],squirrel = [29, 29],nuts = [[15, 0], [0, 15], [15, 30], [30, 15], [20, 20], [10, 10], [5, 5]]) == 200
    assert candidate(height = 15,width = 15,tree = [7, 7],squirrel = [14, 14],nuts = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == 126
    assert candidate(height = 15,width = 20,tree = [10, 10],squirrel = [1, 1],nuts = [[5, 5], [14, 14], [0, 0], [19, 19], [7, 7], [12, 12]]) == 114
    assert candidate(height = 10,width = 10,tree = [2, 2],squirrel = [9, 9],nuts = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [8, 8]]) == 78
    assert candidate(height = 15,width = 15,tree = [14, 14],squirrel = [0, 0],nuts = [[7, 7], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [13, 13], [12, 12], [11, 11], [10, 10], [9, 9], [8, 8]]) == 340
    assert candidate(height = 100,width = 100,tree = [50, 50],squirrel = [99, 99],nuts = [[50, 0], [0, 50], [50, 100], [100, 50], [25, 25], [75, 75], [10, 10], [90, 90], [5, 5], [95, 95], [40, 40], [60, 60], [15, 15], [85, 85], [20, 20], [80, 80], [25, 25], [75, 75], [30, 30], [70, 70]]) == 2158
    assert candidate(height = 40,width = 40,tree = [20, 20],squirrel = [39, 39],nuts = [[10, 10], [30, 30], [5, 5], [35, 35], [15, 15], [25, 25], [20, 20], [5, 35], [35, 5], [15, 25]]) == 358
    assert candidate(height = 50,width = 50,tree = [25, 25],squirrel = [0, 0],nuts = [[49, 49], [48, 48], [47, 47], [46, 46], [45, 45], [44, 44], [43, 43]]) == 638
    assert candidate(height = 30,width = 30,tree = [15, 15],squirrel = [10, 20],nuts = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [10, 25], [25, 10]]) == 170
    assert candidate(height = 20,width = 20,tree = [10, 10],squirrel = [0, 0],nuts = [[19, 19], [0, 19], [19, 0], [9, 9], [10, 9], [9, 10], [8, 8], [11, 11], [12, 12], [7, 7], [6, 6], [13, 13], [14, 14], [5, 5], [4, 4], [15, 15], [16, 16], [3, 3], [2, 2], [17, 17]]) == 360
    assert candidate(height = 70,width = 70,tree = [35, 35],squirrel = [69, 0],nuts = [[34, 34], [36, 36], [69, 69], [0, 0], [1, 1], [68, 68], [2, 2], [67, 67], [3, 3], [66, 66], [4, 4], [65, 65], [5, 5], [64, 64], [6, 6], [63, 63], [7, 7], [62, 62], [8, 8], [61, 61]]) == 2203
    assert candidate(height = 75,width = 75,tree = [37, 37],squirrel = [60, 60],nuts = [[50, 50], [20, 20], [10, 10], [5, 5], [74, 74], [65, 65], [55, 55], [45, 45]]) == 674
    assert candidate(height = 100,width = 100,tree = [50, 50],squirrel = [99, 0],nuts = [[49, 49], [51, 51], [99, 99], [0, 0], [1, 1], [98, 98], [2, 2], [97, 97], [3, 3], [96, 96], [4, 4], [95, 95], [5, 5], [94, 94], [6, 6], [93, 93]]) == 2611
    assert candidate(height = 7,width = 7,tree = [3, 3],squirrel = [6, 6],nuts = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 0], [1, 6], [2, 0], [2, 6], [3, 0], [3, 6], [4, 0], [4, 6], [5, 0], [5, 6], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5]]) == 200
    assert candidate(height = 7,width = 7,tree = [3, 3],squirrel = [0, 3],nuts = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]]) == 117
    assert candidate(height = 25,width = 25,tree = [12, 12],squirrel = [5, 5],nuts = [[20, 20], [21, 21], [22, 22], [23, 23], [24, 24], [15, 15], [10, 10]]) == 226
    assert candidate(height = 20,width = 20,tree = [10, 10],squirrel = [5, 5],nuts = [[0, 0], [20, 20], [10, 0], [0, 10], [20, 0], [0, 20]]) == 190
    assert candidate(height = 15,width = 15,tree = [7, 7],squirrel = [0, 14],nuts = [[0, 0], [0, 14], [14, 0], [14, 14], [7, 0], [7, 14], [0, 7], [14, 7], [5, 5], [9, 9]]) == 170
    assert candidate(height = 50,width = 50,tree = [25, 25],squirrel = [49, 0],nuts = [[24, 24], [26, 26], [49, 49], [0, 0], [1, 1], [48, 48]]) == 391
    assert candidate(height = 20,width = 20,tree = [15, 15],squirrel = [0, 0],nuts = [[10, 10], [10, 0], [0, 10], [20, 20], [5, 5], [15, 5], [5, 15]]) == 190
    assert candidate(height = 80,width = 80,tree = [40, 40],squirrel = [79, 0],nuts = [[39, 39], [41, 41], [79, 79], [0, 0], [1, 1], [78, 78], [2, 2], [77, 77], [3, 3], [76, 76], [4, 4], [75, 75], [5, 5], [74, 74], [6, 6], [73, 73], [7, 7], [72, 72], [8, 8], [71, 71], [9, 9], [70, 70], [10, 10], [69, 69], [11, 11], [68, 68], [12, 12], [67, 67], [13, 13], [66, 66], [14, 14], [65, 65], [15, 15], [64, 64]]) == 4103
    assert candidate(height = 10,width = 10,tree = [5, 5],squirrel = [9, 0],nuts = [[0, 0], [0, 9], [9, 0], [9, 9], [5, 0], [0, 5], [5, 9], [9, 5], [3, 3], [6, 6], [4, 4], [7, 7], [2, 2], [8, 8], [1, 1], [8, 1], [1, 8]]) == 191
    assert candidate(height = 20,width = 20,tree = [10, 10],squirrel = [0, 0],nuts = [[9, 9], [11, 11], [0, 20], [20, 0], [19, 19], [1, 1], [18, 18]]) == 176
    assert candidate(height = 30,width = 30,tree = [15, 15],squirrel = [29, 0],nuts = [[14, 14], [16, 16], [29, 29], [0, 0], [1, 1], [28, 28], [2, 2], [27, 27], [3, 3], [26, 26]]) == 423
    assert candidate(height = 8,width = 8,tree = [7, 7],squirrel = [0, 0],nuts = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 0]]) == 88
    assert candidate(height = 50,width = 50,tree = [25, 25],squirrel = [49, 49],nuts = [[26, 26], [24, 24], [25, 26], [25, 24], [24, 25], [26, 25]]) == 60
