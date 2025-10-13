# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(milestones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(milestones = [3, 3, 3]) == 9
    assert candidate(milestones = [1, 1, 1, 1, 1]) == 5
    assert candidate(milestones = [10, 5, 1]) == 13
    assert candidate(milestones = [1000000000, 1, 1]) == 5
    assert candidate(milestones = [1, 2, 3]) == 6
    assert candidate(milestones = [5, 2, 1]) == 7
    assert candidate(milestones = [1000000000, 1000000000, 1000000000]) == 3000000000
    assert candidate(milestones = [1, 1, 1000000000]) == 5
    assert candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(milestones = [1]) == 1
    assert candidate(milestones = [1, 1000000000]) == 3
    assert candidate(milestones = [5, 5, 5, 5, 5, 5]) == 30
    assert candidate(milestones = [10, 1, 1]) == 5
    assert candidate(milestones = [1, 1000000000, 1]) == 5
    assert candidate(milestones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
    assert candidate(milestones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 200
    assert candidate(milestones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1023
    assert candidate(milestones = [1000000000, 1000000000, 1000000000]) == 3000000000
    assert candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
    assert candidate(milestones = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(milestones = [1000000000, 500000000, 100000000, 50000000, 10000000, 5000000, 1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]) == 1333333333
    assert candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(milestones = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 10000
    assert candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
    assert candidate(milestones = [1000000000, 999999999, 1, 2, 3, 4, 5]) == 2000000014
    assert candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(milestones = [100, 200, 300, 400]) == 1000
    assert candidate(milestones = [1000000000, 999999999, 888888888]) == 2888888887
    assert candidate(milestones = [1, 2, 3, 4, 5]) == 15
    assert candidate(milestones = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 1596
    assert candidate(milestones = [500000000, 500000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000000009
    assert candidate(milestones = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 1000
    assert candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 100]) == 181
    assert candidate(milestones = [10, 10, 10, 10, 10]) == 50
    assert candidate(milestones = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 550
    assert candidate(milestones = [999999999, 1, 1, 1]) == 7
    assert candidate(milestones = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 550000
    assert candidate(milestones = [1000000000, 1000000000, 1000000000, 1]) == 3000000001
    assert candidate(milestones = [10, 20, 30, 40, 50]) == 150
    assert candidate(milestones = [5, 5, 5, 5, 5, 5]) == 30
    assert candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 5000000001
    assert candidate(milestones = [10, 20, 30, 40, 50]) == 150
    assert candidate(milestones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(milestones = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 10000000001
    assert candidate(milestones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
    assert candidate(milestones = [100, 99, 98, 97, 96, 95]) == 585
    assert candidate(milestones = [999999999, 999999999, 1]) == 1999999999
    assert candidate(milestones = [1000000000, 500000000, 250000000, 125000000]) == 1750000001
    assert candidate(milestones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32767
    assert candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 90
    assert candidate(milestones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
    assert candidate(milestones = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5500
    assert candidate(milestones = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 9999999945
    assert candidate(milestones = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39
    assert candidate(milestones = [1000000000, 1000000000, 1000000000, 1000000000, 1]) == 4000000001
    assert candidate(milestones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 101
    assert candidate(milestones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 40
    assert candidate(milestones = [2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1]) == 35
    assert candidate(milestones = [500000000, 500000000, 1]) == 1000000001
    assert candidate(milestones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 80
    assert candidate(milestones = [999999999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 39
    assert candidate(milestones = [100, 150, 200, 250]) == 700
    assert candidate(milestones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(milestones = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 77
    assert candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 110
    assert candidate(milestones = [500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == 1597
    assert candidate(milestones = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 4000000003
    assert candidate(milestones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(milestones = [500000000, 500000000, 500000000, 500000000]) == 2000000000
    assert candidate(milestones = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(milestones = [1, 2, 4, 8, 16, 32, 64]) == 127
    assert candidate(milestones = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]) == 46365
    assert candidate(milestones = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]) == 680
    assert candidate(milestones = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 376
    assert candidate(milestones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 30
    assert candidate(milestones = [333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333, 333333333]) == 3333333330
    assert candidate(milestones = [100, 1, 100, 1, 100, 1]) == 303
