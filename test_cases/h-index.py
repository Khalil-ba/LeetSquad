# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(citations = [10, 8, 5, 4, 3]) == 4
    assert candidate(citations = [1]) == 1
    assert candidate(citations = [3, 0, 6, 1, 5]) == 3
    assert candidate(citations = [0, 1, 2, 3, 4]) == 2
    assert candidate(citations = [1000, 999, 998, 997, 996]) == 5
    assert candidate(citations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(citations = [0, 0, 0, 0, 0]) == 0
    assert candidate(citations = [8, 8, 8, 8, 8, 8, 8]) == 7
    assert candidate(citations = [10, 10, 10, 10]) == 4
    assert candidate(citations = [1, 3, 1]) == 1
    assert candidate(citations = [100, 0, 1, 2]) == 2
    assert candidate(citations = [11, 15, 0, 6, 9, 12]) == 5
    assert candidate(citations = [0, 1, 2, 3, 4, 5]) == 3
    assert candidate(citations = [11, 15]) == 2
    assert candidate(citations = [1, 2, 3, 4, 5, 6]) == 3
    assert candidate(citations = [6, 5, 4, 3, 2, 1]) == 3
    assert candidate(citations = [4, 4, 4, 4, 3]) == 4
    assert candidate(citations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(citations = [0]) == 0
    assert candidate(citations = [1, 2, 3, 4, 5]) == 3
    assert candidate(citations = [0, 0, 0, 0]) == 0
    assert candidate(citations = [1000, 1000, 1000]) == 3
    assert candidate(citations = [5, 5, 5, 5, 5]) == 5
    assert candidate(citations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(citations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(citations = [34, 23, 12, 45, 67, 89, 100, 99, 88, 77, 66, 55, 44, 33, 22, 11, 0]) == 14
    assert candidate(citations = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 7
    assert candidate(citations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 10
    assert candidate(citations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(citations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(citations = [10, 8, 5, 4, 3, 1, 0]) == 4
    assert candidate(citations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 6
    assert candidate(citations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 1
    assert candidate(citations = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 20
    assert candidate(citations = [100, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 11
    assert candidate(citations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 14
    assert candidate(citations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(citations = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 19
    assert candidate(citations = [0, 1000, 2000, 3000, 4000, 5000]) == 5
    assert candidate(citations = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 15
    assert candidate(citations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(citations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]) == 1
    assert candidate(citations = [1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0]) == 10
    assert candidate(citations = [10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9
    assert candidate(citations = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9
    assert candidate(citations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 1
    assert candidate(citations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 19
    assert candidate(citations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 5
    assert candidate(citations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(citations = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 3
    assert candidate(citations = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(citations = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 2
    assert candidate(citations = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12]) == 6
    assert candidate(citations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
    assert candidate(citations = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]) == 31
    assert candidate(citations = [0, 1000, 2, 500, 3, 750, 4, 250, 5, 125]) == 5
    assert candidate(citations = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(citations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(citations = [25, 20, 15, 10, 5, 0, 0, 0, 0, 0]) == 5
    assert candidate(citations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10
    assert candidate(citations = [10, 8, 5, 4, 3, 2, 1, 0]) == 4
    assert candidate(citations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(citations = [0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000]) == 5
    assert candidate(citations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(citations = [500, 250, 125, 62, 31, 15, 7, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 7
    assert candidate(citations = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(citations = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 10
    assert candidate(citations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(citations = [100, 50, 25, 10, 5, 2]) == 5
    assert candidate(citations = [50, 40, 30, 20, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 5
    assert candidate(citations = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(citations = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 5
    assert candidate(citations = [1, 0, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15
    assert candidate(citations = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 14
    assert candidate(citations = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 10
    assert candidate(citations = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 5
    assert candidate(citations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 8
    assert candidate(citations = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9
    assert candidate(citations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 15
