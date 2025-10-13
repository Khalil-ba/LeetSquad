# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(m = 5,n = 4,ops = [[2, 2]]) == 4
    assert candidate(m = 1,n = 1,ops = []) == 1
    assert candidate(m = 2,n = 2,ops = [[2, 2], [1, 1], [2, 2]]) == 1
    assert candidate(m = 1,n = 1,ops = [[1, 1]]) == 1
    assert candidate(m = 4,n = 5,ops = [[1, 1], [2, 2], [3, 3]]) == 1
    assert candidate(m = 1,n = 1,ops = [[1, 1], [1, 1], [1, 1]]) == 1
    assert candidate(m = 4,n = 5,ops = [[2, 3], [3, 4]]) == 6
    assert candidate(m = 5,n = 5,ops = [[4, 4], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(m = 3,n = 3,ops = [[2, 2], [3, 3]]) == 4
    assert candidate(m = 3,n = 3,ops = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]) == 4
    assert candidate(m = 2,n = 2,ops = [[2, 1], [1, 2]]) == 1
    assert candidate(m = 10000,n = 10000,ops = [[10000, 10000], [5000, 5000]]) == 25000000
    assert candidate(m = 2,n = 2,ops = [[1, 2], [2, 1]]) == 1
    assert candidate(m = 5,n = 5,ops = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(m = 3,n = 3,ops = []) == 9
    assert candidate(m = 12,n = 14,ops = [[6, 7], [9, 10], [4, 5], [11, 12], [3, 4]]) == 12
    assert candidate(m = 6,n = 6,ops = [[3, 3], [3, 3], [3, 3], [3, 3]]) == 9
    assert candidate(m = 6,n = 6,ops = [[2, 3], [3, 4], [4, 5], [5, 6]]) == 6
    assert candidate(m = 12,n = 12,ops = [[4, 4], [8, 8], [6, 6], [12, 12], [2, 2], [10, 10]]) == 4
    assert candidate(m = 9,n = 11,ops = [[6, 7], [3, 4], [8, 9], [2, 2], [5, 5]]) == 4
    assert candidate(m = 10,n = 10,ops = [[5, 5], [3, 3], [8, 8]]) == 9
    assert candidate(m = 3,n = 6,ops = [[1, 2], [2, 3], [3, 4], [2, 5], [1, 6]]) == 2
    assert candidate(m = 7,n = 6,ops = [[5, 5], [3, 3], [2, 2], [4, 4], [6, 6]]) == 4
    assert candidate(m = 4,n = 7,ops = [[2, 3], [3, 4], [1, 2], [4, 5]]) == 2
    assert candidate(m = 7,n = 5,ops = [[3, 3], [5, 4], [2, 2], [4, 3], [3, 3], [5, 5]]) == 4
    assert candidate(m = 5000,n = 5000,ops = [[2500, 2500], [2500, 2500], [2500, 2500], [2500, 2500], [2500, 2500]]) == 6250000
    assert candidate(m = 7,n = 3,ops = [[5, 2], [6, 1], [7, 3], [4, 3]]) == 4
    assert candidate(m = 12,n = 8,ops = [[8, 6], [6, 4], [4, 2], [2, 1]]) == 2
    assert candidate(m = 6,n = 5,ops = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(m = 7,n = 5,ops = [[4, 3], [6, 2], [7, 5]]) == 8
    assert candidate(m = 8,n = 7,ops = [[6, 6], [4, 5], [2, 3], [1, 1]]) == 1
    assert candidate(m = 15,n = 10,ops = [[5, 5], [10, 10], [3, 3], [1, 1], [7, 7], [8, 8]]) == 1
    assert candidate(m = 5,n = 5,ops = [[1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 1
    assert candidate(m = 10,n = 1,ops = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 1
    assert candidate(m = 6,n = 6,ops = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == 1
    assert candidate(m = 40000,n = 40000,ops = [[20000, 20000], [15000, 15000], [10000, 10000]]) == 100000000
    assert candidate(m = 20,n = 15,ops = [[10, 10], [5, 5], [15, 15], [8, 8], [12, 12], [7, 7]]) == 25
    assert candidate(m = 9,n = 6,ops = [[4, 4], [5, 5], [6, 6], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(m = 10,n = 10,ops = [[5, 5], [7, 7], [3, 3], [2, 2]]) == 4
    assert candidate(m = 4000,n = 4000,ops = [[2000, 2000], [1000, 1000], [3000, 3000], [500, 500]]) == 250000
    assert candidate(m = 8,n = 6,ops = [[2, 3], [4, 4], [3, 5], [5, 6]]) == 6
    assert candidate(m = 9,n = 9,ops = [[9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(m = 50,n = 50,ops = [[25, 25], [20, 20], [15, 15], [10, 10], [5, 5]]) == 25
    assert candidate(m = 15,n = 10,ops = [[5, 5], [5, 10], [10, 5], [10, 10]]) == 25
    assert candidate(m = 2000,n = 3000,ops = [[1000, 1500], [500, 1000], [1500, 2000], [750, 1250]]) == 500000
    assert candidate(m = 20,n = 10,ops = [[10, 5], [9, 4], [8, 3], [7, 2], [6, 1]]) == 6
    assert candidate(m = 8,n = 8,ops = [[8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(m = 20,n = 10,ops = [[10, 5], [15, 3], [20, 10]]) == 30
    assert candidate(m = 8,n = 8,ops = [[2, 2], [4, 4], [6, 6], [8, 8], [4, 4], [6, 6], [2, 2]]) == 4
    assert candidate(m = 7,n = 7,ops = [[7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(m = 10,n = 10,ops = [[5, 5], [4, 4], [6, 6], [7, 7]]) == 16
    assert candidate(m = 5,n = 6,ops = [[3, 3], [4, 4], [2, 2]]) == 4
    assert candidate(m = 12,n = 9,ops = [[3, 3], [6, 6], [9, 9], [4, 4], [7, 7], [5, 5]]) == 9
    assert candidate(m = 16,n = 10,ops = [[10, 8], [8, 6], [6, 4], [4, 2], [2, 1]]) == 2
    assert candidate(m = 10,n = 15,ops = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 25
    assert candidate(m = 10000,n = 10000,ops = [[9000, 9000], [8000, 8000], [7000, 7000]]) == 49000000
    assert candidate(m = 9,n = 10,ops = [[3, 5], [6, 7], [2, 4], [8, 9], [5, 6], [4, 8], [7, 10]]) == 8
    assert candidate(m = 100,n = 100,ops = [[50, 50], [75, 75], [25, 25], [100, 100]]) == 625
    assert candidate(m = 10000,n = 10000,ops = [[5000, 5000], [2500, 2500], [7500, 7500]]) == 6250000
    assert candidate(m = 8,n = 6,ops = [[6, 5], [5, 4], [4, 3], [3, 2], [2, 1]]) == 2
    assert candidate(m = 7,n = 8,ops = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 1
    assert candidate(m = 8,n = 8,ops = [[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2]]) == 4
    assert candidate(m = 20,n = 20,ops = [[10, 10], [15, 15], [5, 5], [12, 12], [18, 18], [8, 8]]) == 25
    assert candidate(m = 2,n = 4,ops = [[1, 1], [2, 2], [1, 4], [2, 1]]) == 1
    assert candidate(m = 4,n = 5,ops = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 1], [2, 2], [3, 3]]) == 1
    assert candidate(m = 20,n = 10,ops = [[5, 3], [10, 5], [15, 7], [20, 9]]) == 15
    assert candidate(m = 40000,n = 40000,ops = [[20000, 20000], [30000, 30000]]) == 400000000
    assert candidate(m = 5,n = 6,ops = [[3, 4], [2, 3], [4, 5]]) == 6
    assert candidate(m = 3000,n = 2000,ops = [[1000, 1000], [2000, 1500], [500, 500], [1500, 1000]]) == 250000
    assert candidate(m = 5,n = 5,ops = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 1
    assert candidate(m = 5,n = 5,ops = [[3, 4], [4, 3], [2, 5], [5, 2], [1, 1]]) == 1
    assert candidate(m = 6,n = 3,ops = [[2, 1], [3, 2], [4, 3]]) == 2
    assert candidate(m = 4000,n = 4000,ops = [[2000, 2000], [3000, 3000], [1000, 1000], [4000, 4000]]) == 1000000
    assert candidate(m = 6,n = 6,ops = [[3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3]]) == 9
    assert candidate(m = 5000,n = 4000,ops = [[4000, 3000], [3500, 2500], [3000, 2000], [2500, 1500], [2000, 1000]]) == 2000000
    assert candidate(m = 40000,n = 40000,ops = [[20000, 20000], [30000, 30000], [40000, 40000]]) == 400000000
    assert candidate(m = 10000,n = 10000,ops = [[9000, 9000], [8000, 8000], [7000, 7000], [6000, 6000]]) == 36000000
    assert candidate(m = 3000,n = 2000,ops = [[1500, 1000], [2500, 1500], [500, 500], [3000, 2000]]) == 250000
    assert candidate(m = 8,n = 8,ops = [[6, 6], [7, 7], [4, 4], [5, 5], [3, 3]]) == 9
    assert candidate(m = 20,n = 20,ops = [[10, 10], [15, 15], [5, 5], [20, 20], [8, 8]]) == 25
    assert candidate(m = 5000,n = 3000,ops = [[2500, 1500], [4000, 2500], [1000, 500], [5000, 3000]]) == 500000
    assert candidate(m = 6,n = 6,ops = [[3, 4], [4, 5], [5, 6], [2, 3]]) == 6
    assert candidate(m = 8,n = 6,ops = [[3, 3], [5, 4], [7, 6]]) == 9
    assert candidate(m = 4,n = 4,ops = [[4, 4], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(m = 6,n = 4,ops = [[2, 3], [4, 2], [5, 1]]) == 2
    assert candidate(m = 10,n = 10,ops = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1
    assert candidate(m = 8,n = 8,ops = [[6, 7], [7, 8], [4, 5], [5, 6], [3, 4], [4, 5], [2, 3], [3, 4]]) == 6
    assert candidate(m = 10,n = 10,ops = [[5, 5], [7, 7], [9, 9], [8, 8]]) == 25
    assert candidate(m = 2000,n = 1000,ops = [[1000, 500], [1500, 750], [500, 250], [2000, 1000]]) == 125000
    assert candidate(m = 10,n = 10,ops = [[5, 5], [7, 7], [8, 8], [9, 9], [10, 10]]) == 25
    assert candidate(m = 8,n = 5,ops = [[2, 3], [4, 5], [6, 4], [7, 3], [5, 2]]) == 4
    assert candidate(m = 15,n = 15,ops = [[10, 10], [12, 12], [14, 14], [15, 15], [1, 1], [2, 2], [3, 3]]) == 1
    assert candidate(m = 15,n = 15,ops = [[10, 10], [5, 5], [12, 12], [7, 7], [8, 8]]) == 25
    assert candidate(m = 1,n = 10,ops = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 1
    assert candidate(m = 2,n = 2,ops = [[1, 1], [1, 2], [2, 1], [2, 2]]) == 1
    assert candidate(m = 100,n = 100,ops = [[50, 50], [25, 25], [75, 75], [90, 90]]) == 625
    assert candidate(m = 15,n = 10,ops = [[3, 5], [4, 6], [10, 8], [15, 10]]) == 15
    assert candidate(m = 5,n = 4,ops = [[2, 3], [3, 4], [4, 5]]) == 6
    assert candidate(m = 10,n = 10,ops = [[5, 5], [3, 3], [7, 7], [2, 2], [8, 8]]) == 4
    assert candidate(m = 10,n = 10,ops = [[9, 9], [8, 8], [7, 7], [6, 6], [5, 5]]) == 25
    assert candidate(m = 5,n = 5,ops = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 1
    assert candidate(m = 10,n = 15,ops = [[5, 5], [7, 7], [3, 3]]) == 9
    assert candidate(m = 20,n = 15,ops = [[10, 10], [5, 5], [15, 15], [12, 12]]) == 25
    assert candidate(m = 5,n = 4,ops = [[3, 2], [4, 3], [2, 4]]) == 4
    assert candidate(m = 1,n = 10000,ops = [[1, 1], [1, 1], [1, 1], [1, 1]]) == 1
    assert candidate(m = 1000,n = 1000,ops = [[500, 500], [999, 999], [1, 1], [500, 500]]) == 1
    assert candidate(m = 12,n = 15,ops = [[6, 6], [5, 5], [7, 7], [8, 8], [9, 9], [10, 10]]) == 25
    assert candidate(m = 15,n = 20,ops = [[10, 15], [12, 18], [5, 10], [3, 4]]) == 12
    assert candidate(m = 10000,n = 1,ops = [[1, 1], [1, 1], [1, 1], [1, 1]]) == 1
    assert candidate(m = 100,n = 100,ops = [[50, 50], [75, 75], [25, 25]]) == 625
    assert candidate(m = 5,n = 4,ops = [[2, 2], [3, 3], [1, 4]]) == 2
    assert candidate(m = 5,n = 4,ops = [[2, 2], [3, 3], [4, 4], [1, 1]]) == 1
