# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(times = [[5, 10], [1, 3], [2, 6], [7, 8]],targetFriend = 1) == 0
    assert candidate(times = [[5, 10], [1, 2], [3, 8]],targetFriend = 2) == 0
    assert candidate(times = [[2, 7], [7, 9], [1, 5]],targetFriend = 2) == 0
    assert candidate(times = [[1, 2], [2, 3], [3, 4], [4, 5]],targetFriend = 3) == 0
    assert candidate(times = [[8, 12], [1, 6], [3, 5], [9, 10]],targetFriend = 2) == 1
    assert candidate(times = [[2, 5], [3, 7], [4, 9], [5, 10]],targetFriend = 2) == 2
    assert candidate(times = [[5, 15], [1, 20], [10, 25]],targetFriend = 2) == 2
    assert candidate(times = [[10, 20], [20, 30], [15, 25], [5, 15]],targetFriend = 2) == 0
    assert candidate(times = [[2, 5], [3, 9], [4, 7], [5, 8]],targetFriend = 2) == 2
    assert candidate(times = [[5, 10], [1, 3], [4, 8], [6, 9]],targetFriend = 3) == 2
    assert candidate(times = [[10, 20], [5, 10], [15, 25]],targetFriend = 1) == 0
    assert candidate(times = [[1, 4], [2, 3], [4, 6]],targetFriend = 1) == 1
    assert candidate(times = [[5, 10], [1, 3], [4, 6], [6, 7]],targetFriend = 1) == 0
    assert candidate(times = [[1, 3], [2, 5], [3, 6], [4, 7]],targetFriend = 2) == 0
    assert candidate(times = [[2, 5], [1, 3], [6, 7], [4, 8]],targetFriend = 1) == 0
    assert candidate(times = [[3, 10], [1, 5], [2, 6]],targetFriend = 0) == 2
    assert candidate(times = [[1, 2], [2, 5], [4, 7], [7, 9]],targetFriend = 0) == 0
    assert candidate(times = [[3, 4], [1, 5], [2, 6], [5, 7], [4, 8], [6, 9]],targetFriend = 3) == 0
    assert candidate(times = [[5, 8], [12, 15], [10, 14], [20, 25], [1, 4], [16, 18], [6, 9], [19, 22], [3, 7], [11, 13]],targetFriend = 8) == 1
    assert candidate(times = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26]],targetFriend = 6) == 0
    assert candidate(times = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100], [11, 110], [12, 120]],targetFriend = 11) == 10
    assert candidate(times = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92]],targetFriend = 8) == 8
    assert candidate(times = [[1, 10], [2, 5], [3, 7], [8, 12], [6, 9], [11, 13]],targetFriend = 5) == 0
    assert candidate(times = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91], [11, 90], [12, 89], [13, 88], [14, 87], [15, 86]],targetFriend = 7) == 7
    assert candidate(times = [[10, 20], [5, 15], [1, 10], [16, 30], [21, 40]],targetFriend = 3) == 1
    assert candidate(times = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14]],targetFriend = 2) == 2
    assert candidate(times = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]],targetFriend = 6) == 2
    assert candidate(times = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],targetFriend = 8) == 0
    assert candidate(times = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],targetFriend = 5) == 0
    assert candidate(times = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26], [27, 28]],targetFriend = 7) == 0
    assert candidate(times = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]],targetFriend = 0) == 0
    assert candidate(times = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10]],targetFriend = 9) == 0
    assert candidate(times = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],targetFriend = 9) == 0
    assert candidate(times = [[5, 10], [1, 6], [7, 12], [15, 20], [2, 8]],targetFriend = 4) == 1
    assert candidate(times = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10]],targetFriend = 3) == 3
    assert candidate(times = [[3, 20], [1, 5], [7, 15], [10, 18], [2, 8], [13, 17]],targetFriend = 3) == 1
    assert candidate(times = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],targetFriend = 4) == 0
    assert candidate(times = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30], [31, 32], [33, 34], [35, 36], [37, 38], [39, 40], [41, 42], [43, 44], [45, 46], [47, 48], [49, 50]],targetFriend = 22) == 0
    assert candidate(times = [[1, 5], [2, 3], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11]],targetFriend = 5) == 1
    assert candidate(times = [[10, 20], [1, 6], [3, 11], [7, 14], [15, 25]],targetFriend = 4) == 0
    assert candidate(times = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91], [11, 90], [12, 89], [13, 88], [14, 87], [15, 86], [16, 85], [17, 84], [18, 83], [19, 82], [20, 81]],targetFriend = 15) == 15
    assert candidate(times = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91], [11, 90], [12, 89], [13, 88], [14, 87], [15, 86]],targetFriend = 10) == 10
    assert candidate(times = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]],targetFriend = 6) == 0
    assert candidate(times = [[1, 50], [2, 49], [3, 48], [4, 47], [5, 46], [6, 45], [7, 44], [8, 43], [9, 42], [10, 41]],targetFriend = 9) == 9
    assert candidate(times = [[1, 10], [2, 5], [3, 4], [6, 9], [7, 11]],targetFriend = 4) == 2
    assert candidate(times = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]],targetFriend = 9) == 0
    assert candidate(times = [[1, 10], [2, 12], [3, 14], [4, 16], [5, 18], [6, 20]],targetFriend = 2) == 2
    assert candidate(times = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996], [6, 995], [7, 994], [8, 993], [9, 992], [10, 991]],targetFriend = 9) == 9
    assert candidate(times = [[3, 8], [1, 5], [2, 6], [7, 10], [4, 9], [6, 12], [8, 15]],targetFriend = 2) == 1
    assert candidate(times = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30], [31, 32], [33, 34], [35, 36], [37, 38], [39, 40]],targetFriend = 19) == 0
    assert candidate(times = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90]],targetFriend = 4) == 0
    assert candidate(times = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14]],targetFriend = 10) == 0
    assert candidate(times = [[10, 20], [5, 15], [1, 8], [21, 25], [11, 18]],targetFriend = 2) == 0
    assert candidate(times = [[2, 4], [6, 8], [10, 12], [1, 3], [5, 7], [9, 11]],targetFriend = 0) == 1
    assert candidate(times = [[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],targetFriend = 5) == 0
    assert candidate(times = [[1, 10], [2, 5], [6, 12], [3, 9], [7, 15]],targetFriend = 2) == 1
    assert candidate(times = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95]],targetFriend = 5) == 5
    assert candidate(times = [[1, 5], [2, 3], [4, 7], [5, 8], [6, 9], [7, 10], [8, 11], [9, 12], [10, 13], [11, 14], [12, 15]],targetFriend = 7) == 2
    assert candidate(times = [[1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]],targetFriend = 5) == 2
    assert candidate(times = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40]],targetFriend = 5) == 0
    assert candidate(times = [[1, 30], [2, 25], [3, 20], [4, 15], [5, 10], [6, 28], [7, 24], [8, 22], [9, 29], [10, 18], [11, 21], [12, 27], [13, 23], [14, 26], [15, 19], [16, 17]],targetFriend = 4) == 4
    assert candidate(times = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996], [6, 9995], [7, 9994], [8, 9993], [9, 9992], [10, 9991]],targetFriend = 9) == 9
    assert candidate(times = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],targetFriend = 0) == 0
    assert candidate(times = [[10, 20], [30, 40], [20, 30], [5, 15], [45, 55], [50, 60]],targetFriend = 4) == 0
    assert candidate(times = [[1, 100], [2, 99], [3, 98], [4, 97], [5, 96], [6, 95], [7, 94], [8, 93], [9, 92], [10, 91]],targetFriend = 9) == 9
    assert candidate(times = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]],targetFriend = 9) == 1
    assert candidate(times = [[1, 500], [2, 499], [3, 498], [4, 497], [5, 496], [6, 495], [7, 494], [8, 493], [9, 492], [10, 491], [11, 490], [12, 489], [13, 488], [14, 487], [15, 486]],targetFriend = 13) == 13
    assert candidate(times = [[10, 20], [15, 25], [5, 15], [20, 30], [25, 35], [0, 10]],targetFriend = 2) == 1
    assert candidate(times = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80]],targetFriend = 3) == 0
    assert candidate(times = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100], [100, 110]],targetFriend = 4) == 0
    assert candidate(times = [[10, 30], [20, 40], [30, 50], [40, 60], [50, 70], [60, 80], [70, 90], [80, 100], [90, 110], [100, 120], [110, 130], [120, 140], [130, 150], [140, 160], [150, 170], [160, 180], [170, 190], [180, 200], [190, 210], [200, 220]],targetFriend = 9) == 1
    assert candidate(times = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40], [40, 45], [45, 50]],targetFriend = 0) == 0
    assert candidate(times = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40]],targetFriend = 3) == 0
    assert candidate(times = [[5, 10], [10, 15], [15, 20], [20, 25], [25, 30], [30, 35], [35, 40], [40, 45], [45, 50], [50, 55]],targetFriend = 8) == 0
    assert candidate(times = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10], [11, 10]],targetFriend = 10) == 0
    assert candidate(times = [[1, 100], [2, 30], [3, 40], [4, 50], [5, 60], [6, 70], [7, 80], [8, 90], [9, 100]],targetFriend = 5) == 5
    assert candidate(times = [[1, 30], [2, 29], [3, 28], [4, 27], [5, 26], [6, 25], [7, 24], [8, 23], [9, 22], [10, 21]],targetFriend = 5) == 5
    assert candidate(times = [[1, 20], [2, 19], [3, 18], [4, 17], [5, 16], [6, 15], [7, 14], [8, 13], [9, 12], [10, 11]],targetFriend = 6) == 6
    assert candidate(times = [[1, 10000], [2, 9999], [3, 9998], [4, 9997], [5, 9996], [6, 9995], [7, 9994]],targetFriend = 6) == 6
    assert candidate(times = [[1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [9, 18], [10, 19]],targetFriend = 9) == 0
    assert candidate(times = [[1, 3], [3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15], [15, 17], [17, 19], [19, 21]],targetFriend = 5) == 0
    assert candidate(times = [[1, 10], [11, 20], [2, 19], [12, 18], [3, 17]],targetFriend = 3) == 3
    assert candidate(times = [[1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12]],targetFriend = 4) == 4
    assert candidate(times = [[3, 8], [5, 10], [1, 4], [7, 12], [9, 15]],targetFriend = 3) == 2
    assert candidate(times = [[1, 10], [2, 12], [3, 14], [4, 16], [5, 18], [6, 20], [7, 22], [8, 24], [9, 26], [10, 28]],targetFriend = 9) == 0
    assert candidate(times = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90]],targetFriend = 5) == 0
    assert candidate(times = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]],targetFriend = 5) == 0
    assert candidate(times = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21]],targetFriend = 9) == 0
    assert candidate(times = [[1, 5], [1, 4], [1, 3], [1, 2], [2, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7]],targetFriend = 8) == 0
    assert candidate(times = [[10, 25], [20, 30], [5, 15], [15, 20], [1, 10], [25, 35], [30, 40], [5, 10], [15, 20]],targetFriend = 5) == 0
    assert candidate(times = [[1, 10], [2, 5], [3, 6], [7, 12], [8, 9], [4, 11]],targetFriend = 2) == 2
    assert candidate(times = [[1, 100], [2, 50], [3, 30], [4, 20], [5, 10], [6, 5], [7, 3]],targetFriend = 0) == 0
    assert candidate(times = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],targetFriend = 8) == 0
    assert candidate(times = [[1, 10], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]],targetFriend = 4) == 4
    assert candidate(times = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14]],targetFriend = 7) == 3
    assert candidate(times = [[5, 10], [1, 6], [11, 16], [21, 26], [10, 15], [6, 11], [16, 21], [26, 31], [2, 7], [7, 12]],targetFriend = 8) == 1
    assert candidate(times = [[1, 20], [2, 19], [3, 18], [4, 17], [5, 16], [6, 15], [7, 14], [8, 13], [9, 12], [10, 11], [21, 40], [22, 39], [23, 38], [24, 37], [25, 36], [26, 35], [27, 34], [28, 33], [29, 32], [30, 31]],targetFriend = 15) == 5
    assert candidate(times = [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60]],targetFriend = 5) == 0
    assert candidate(times = [[5, 10], [10, 20], [15, 25], [20, 30], [25, 35], [30, 40]],targetFriend = 3) == 0
    assert candidate(times = [[5, 10], [1, 2], [3, 4], [6, 7], [8, 9], [10, 11]],targetFriend = 1) == 0
    assert candidate(times = [[10, 20], [5, 15], [1, 11], [25, 35], [30, 40]],targetFriend = 4) == 1
