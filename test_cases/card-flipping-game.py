# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(fronts = [1, 3, 5, 7],backs = [2, 4, 6, 8]) == 1
    assert candidate(fronts = [1, 1, 2, 2],backs = [2, 2, 1, 1]) == 1
    assert candidate(fronts = [1, 3, 5, 7],backs = [2, 4, 6, 8]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5],backs = [5, 4, 3, 2, 1]) == 1
    assert candidate(fronts = [1, 3, 5, 7, 9],backs = [2, 4, 6, 8, 10]) == 1
    assert candidate(fronts = [5, 6, 7, 8],backs = [8, 7, 6, 5]) == 5
    assert candidate(fronts = [1, 2, 3, 4, 5],backs = [5, 4, 3, 2, 1]) == 1
    assert candidate(fronts = [1],backs = [1]) == 0
    assert candidate(fronts = [1, 1, 1, 1],backs = [1, 1, 1, 1]) == 0
    assert candidate(fronts = [1000, 1000, 1000],backs = [1001, 1002, 1003]) == 1000
    assert candidate(fronts = [1, 1, 1, 1, 1],backs = [2, 2, 2, 2, 1]) == 2
    assert candidate(fronts = [2, 2, 2, 2],backs = [2, 2, 2, 2]) == 0
    assert candidate(fronts = [1, 2, 3],backs = [3, 2, 1]) == 1
    assert candidate(fronts = [1, 2, 3],backs = [3, 2, 1]) == 1
    assert candidate(fronts = [1, 1, 1, 2],backs = [1, 1, 2, 1]) == 2
    assert candidate(fronts = [1, 1, 1, 1],backs = [2, 2, 2, 2]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5],backs = [6, 7, 8, 9, 10]) == 1
    assert candidate(fronts = [1, 2, 4, 4, 7],backs = [1, 3, 4, 1, 3]) == 2
    assert candidate(fronts = [1000, 2000],backs = [2000, 1000]) == 1000
    assert candidate(fronts = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],backs = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 1
    assert candidate(fronts = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],backs = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 1
    assert candidate(fronts = [1, 2, 2, 3, 3, 4, 5, 6],backs = [6, 5, 4, 3, 2, 1, 2, 3]) == 1
    assert candidate(fronts = [2, 3, 2, 3, 2, 3],backs = [3, 2, 3, 2, 3, 2]) == 2
    assert candidate(fronts = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],backs = [8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 1
    assert candidate(fronts = [10, 20, 30, 40, 50, 60],backs = [60, 50, 40, 30, 20, 10]) == 10
    assert candidate(fronts = [1, 1, 1, 1],backs = [1, 1, 1, 1]) == 0
    assert candidate(fronts = [2000, 1999, 1998, 1997, 1996, 1995],backs = [1995, 1996, 1997, 1998, 1999, 2000]) == 1995
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],backs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 2
    assert candidate(fronts = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],backs = [109, 108, 107, 106, 105, 104, 103, 102, 101, 100]) == 100
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],backs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(fronts = [1000, 2000, 1500, 500, 1200],backs = [2000, 1000, 1500, 1000, 500]) == 500
    assert candidate(fronts = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],backs = [6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 1
    assert candidate(fronts = [1, 1, 1, 1, 1, 1],backs = [1, 1, 1, 1, 1, 1]) == 0
    assert candidate(fronts = [1, 2, 3, 4, 5],backs = [6, 7, 8, 9, 10]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],backs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(fronts = [10, 10, 10, 10, 10],backs = [1, 2, 3, 4, 5]) == 1
    assert candidate(fronts = [500, 501, 502, 503, 504],backs = [504, 503, 502, 501, 500]) == 500
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],backs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 10]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],backs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 1
    assert candidate(fronts = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],backs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
    assert candidate(fronts = [10, 10, 20, 30, 40, 50],backs = [50, 20, 10, 30, 40, 60]) == 10
    assert candidate(fronts = [2000, 1999, 1998, 1997, 1996],backs = [1995, 1994, 1993, 1992, 1991]) == 1991
    assert candidate(fronts = [500, 500, 500, 500, 500],backs = [500, 501, 502, 503, 504]) == 501
    assert candidate(fronts = [1, 1, 2, 2, 3, 3],backs = [3, 3, 1, 1, 2, 2]) == 1
    assert candidate(fronts = [2000, 1999, 1998, 1997, 1996],backs = [1995, 1996, 1997, 1998, 1999]) == 1995
    assert candidate(fronts = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009],backs = [1009, 1008, 1007, 1006, 1005, 1004, 1003, 1002, 1001, 1000]) == 1000
    assert candidate(fronts = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],backs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(fronts = [1, 3, 5, 7, 9],backs = [2, 4, 6, 8, 1000]) == 1
    assert candidate(fronts = [1, 1, 1, 2, 2, 2, 3, 3, 3],backs = [3, 2, 1, 3, 2, 1, 3, 2, 1]) == 0
    assert candidate(fronts = [2, 3, 5, 7, 11, 13],backs = [11, 13, 2, 3, 5, 7]) == 2
    assert candidate(fronts = [1, 1, 1, 1, 1],backs = [1, 1, 1, 1, 1]) == 0
    assert candidate(fronts = [1, 2, 3, 4, 5],backs = [1, 2, 3, 4, 5]) == 0
    assert candidate(fronts = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],backs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],backs = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 1
    assert candidate(fronts = [2, 3, 5, 7, 11, 13, 17, 19],backs = [19, 17, 13, 11, 7, 5, 3, 2]) == 2
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],backs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(fronts = [1, 3, 3, 7, 9],backs = [2, 3, 5, 7, 8]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],backs = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11]) == 1
    assert candidate(fronts = [1, 1, 2, 3, 4, 5],backs = [5, 4, 3, 2, 1, 1]) == 1
    assert candidate(fronts = [500, 501, 502, 503, 504, 505],backs = [505, 504, 503, 502, 501, 500]) == 500
    assert candidate(fronts = [1, 2, 3, 4, 5],backs = [2, 1, 4, 3, 5]) == 1
    assert candidate(fronts = [11, 22, 33, 44, 55],backs = [55, 44, 33, 22, 11]) == 11
    assert candidate(fronts = [5, 5, 5, 5, 5],backs = [5, 5, 5, 5, 5]) == 0
    assert candidate(fronts = [2, 3, 2, 4, 3, 4, 5, 6, 7, 8],backs = [8, 7, 6, 5, 4, 3, 2, 1, 2, 3]) == 1
    assert candidate(fronts = [1, 1, 1, 1, 1],backs = [2, 2, 2, 2, 2]) == 1
    assert candidate(fronts = [1, 1, 1, 1, 2, 2, 2, 2],backs = [2, 2, 2, 2, 1, 1, 1, 1]) == 1
    assert candidate(fronts = [1, 1, 2, 2, 3, 3],backs = [2, 2, 3, 3, 4, 4]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],backs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(fronts = [100, 200, 300, 400, 500],backs = [500, 400, 300, 200, 100]) == 100
    assert candidate(fronts = [10, 20, 30, 40, 50],backs = [50, 40, 30, 20, 10]) == 10
    assert candidate(fronts = [1500, 1600, 1700, 1800, 1900],backs = [1900, 1800, 1700, 1600, 1500]) == 1500
    assert candidate(fronts = [2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991],backs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(fronts = [1, 1, 2, 2, 3, 3],backs = [2, 2, 3, 3, 1, 1]) == 1
    assert candidate(fronts = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],backs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 11
    assert candidate(fronts = [100, 100, 200, 200, 300, 300],backs = [200, 200, 300, 300, 100, 100]) == 100
    assert candidate(fronts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],backs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 10
    assert candidate(fronts = [1, 2, 2, 3, 4],backs = [4, 3, 3, 2, 1]) == 1
    assert candidate(fronts = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],backs = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],backs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 11]) == 1
    assert candidate(fronts = [15, 15, 15, 15, 16],backs = [16, 15, 15, 15, 15]) == 16
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],backs = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(fronts = [1000, 2, 3, 4, 5],backs = [5, 1000, 3, 4, 2]) == 2
    assert candidate(fronts = [10, 20, 30, 40, 50, 60],backs = [10, 30, 50, 70, 90, 110]) == 20
    assert candidate(fronts = [101, 102, 103, 104, 105],backs = [106, 105, 104, 103, 102]) == 101
    assert candidate(fronts = [2000, 1999, 1998, 1997, 1996],backs = [1996, 1997, 1998, 1999, 2000]) == 1996
    assert candidate(fronts = [5, 5, 5, 5, 5, 5],backs = [6, 6, 6, 6, 6, 6]) == 5
    assert candidate(fronts = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4],backs = [4, 4, 4, 3, 3, 3, 2, 2, 2, 1]) == 1
    assert candidate(fronts = [1, 1, 1, 2, 2, 3],backs = [1, 2, 3, 3, 1, 1]) == 2
    assert candidate(fronts = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],backs = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 1
    assert candidate(fronts = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],backs = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]) == 1
    assert candidate(fronts = [2, 3, 5, 7, 11, 13],backs = [13, 11, 7, 5, 3, 2]) == 2
    assert candidate(fronts = [1000, 2000, 1000, 2000, 1000, 2000],backs = [2000, 1000, 2000, 1000, 2000, 1000]) == 1000
    assert candidate(fronts = [1, 1, 2, 2, 3, 3, 4, 4],backs = [1, 2, 1, 3, 2, 4, 3, 5]) == 2
    assert candidate(fronts = [2000, 2000, 2000, 2000, 2000],backs = [1, 2, 3, 4, 5]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],backs = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(fronts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],backs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 2
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],backs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == 10
    assert candidate(fronts = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],backs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5],backs = [5, 1, 4, 3, 2]) == 1
    assert candidate(fronts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],backs = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(fronts = [1, 1, 2, 2, 3, 3, 4, 4],backs = [2, 2, 1, 1, 4, 4, 3, 3]) == 1
    assert candidate(fronts = [1, 3, 5, 7, 9, 11],backs = [11, 9, 7, 5, 3, 1]) == 1
    assert candidate(fronts = [1, 2, 3, 2, 1, 4, 5],backs = [5, 4, 3, 3, 4, 1, 2]) == 1
    assert candidate(fronts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],backs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(fronts = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6],backs = [6, 5, 5, 4, 3, 3, 2, 1, 1, 1]) == 1
    assert candidate(fronts = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],backs = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 2
    assert candidate(fronts = [2, 4, 6, 8, 10],backs = [1, 3, 5, 7, 9]) == 1
