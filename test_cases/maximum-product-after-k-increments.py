# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 5, 5, 5, 5],k = 5) == 7776
    assert candidate(nums = [1, 2, 3, 4],k = 3) == 108
    assert candidate(nums = [100000, 100000, 100000],k = 300000) == 944000007
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 94500000
    assert candidate(nums = [0, 4],k = 5) == 20
    assert candidate(nums = [0, 0, 0, 0],k = 10) == 36
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 540
    assert candidate(nums = [5, 5, 5, 5],k = 4) == 1296
    assert candidate(nums = [1, 1, 1, 1, 1],k = 10) == 243
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 508243680
    assert candidate(nums = [9, 9, 9, 9],k = 8) == 14641
    assert candidate(nums = [1000000],k = 1000000) == 2000000
    assert candidate(nums = [10, 10, 10],k = 5) == 1584
    assert candidate(nums = [6, 3, 3, 2],k = 2) == 216
    assert candidate(nums = [0, 0, 0, 0],k = 1) == 0
    assert candidate(nums = [1, 2, 3],k = 6) == 64
    assert candidate(nums = [1000000, 1000000],k = 1000000) == 999984257
    assert candidate(nums = [100000, 100000, 100000],k = 500000) == 830133340
    assert candidate(nums = [10, 20, 30],k = 15) == 15180
    assert candidate(nums = [1, 2, 3],k = 3) == 27
    assert candidate(nums = [1, 1, 1, 1],k = 10) == 144
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],k = 500000) == 800515855
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 10000) == 500226898
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 55) == 937424426
    assert candidate(nums = [100, 100, 100, 100, 100],k = 250) == 937499475
    assert candidate(nums = [1, 2, 3, 4, 5, 6],k = 10) == 18750
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 200) == 138022365
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 1000) == 24010000
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 100) == 858490890
    assert candidate(nums = [1, 1000000],k = 999999) == 999993007
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 45) == 1000000000
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 50) == 836777896
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 100) == 385000049
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 500) == 514152040
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 508243680
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 50) == 209024971
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 48999587
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 20) == 248832
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 100) == 4900
    assert candidate(nums = [100, 200, 300, 400, 500],k = 1000) == 999781257
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 100) == 460935215
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 414469870
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 60466176
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 20) == 786432
    assert candidate(nums = [999999, 999998, 999997, 999996],k = 10000) == 58871243
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 913512597
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 50) == 904899965
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 200) == 340513509
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 150) == 322349693
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 570617225
    assert candidate(nums = [1, 3, 5, 7, 9],k = 20) == 59049
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 30) == 176221081
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 235146240
    assert candidate(nums = [1, 10, 100, 1000, 10000],k = 10000) == 49587669
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995],k = 100000) == 817421264
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 50) == 999999937
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8],k = 200) == 73636025
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1024
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 50) == 608131681
    assert candidate(nums = [1, 3, 5, 7, 9],k = 25) == 100000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 937424426
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 50) == 73741817
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 100) == 911705284
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 30) == 60466176
    assert candidate(nums = [1, 10, 100, 1000, 10000],k = 100000) == 501184279
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 1048576
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 937424426
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000],k = 1000000) == 369628908
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 235146240
    assert candidate(nums = [1, 1000000],k = 999999) == 999993007
    assert candidate(nums = [1],k = 100000) == 100001
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],k = 1000000) == 679146511
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1000000) == 825247221
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 500000) == 249964681
    assert candidate(nums = [10, 20, 30, 40, 50],k = 100) == 312500000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 467201634
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 100000) == 346266448
    assert candidate(nums = [1, 2, 3, 4, 5],k = 10) == 3125
    assert candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996],k = 10000) == 607510375
    assert candidate(nums = [1000000, 999999, 999998],k = 1000000) == 448037452
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 50) == 73741817
    assert candidate(nums = [100000, 100000, 100000, 100000],k = 300000) == 765670962
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0],k = 25) == 983040
    assert candidate(nums = [10, 20, 30, 40, 50],k = 30) == 54000000
    assert candidate(nums = [1000000, 1000000, 1000000],k = 3000000) == 392
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000) == 461240680
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 105099888
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 30) == 191102976
    assert candidate(nums = [1, 2, 3, 4, 5],k = 20) == 16807
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 550731776
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 100) == 47899023
    assert candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996],k = 10000) == 233771963
    assert candidate(nums = [1, 10, 100, 1000, 10000],k = 50000) == 901582326
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 50) == 650386593
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1000) == 889950771
    assert candidate(nums = [10, 20, 30, 40, 50],k = 100) == 312500000
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500],k = 500000) == 180658830
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 5000) == 881212280
    assert candidate(nums = [100000, 100000, 100000],k = 300000) == 944000007
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 785571733
    assert candidate(nums = [1, 2, 3, 4, 5],k = 15) == 7776
