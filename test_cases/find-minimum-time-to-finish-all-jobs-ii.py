# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(jobs = [100, 200, 300],workers = [10, 20, 30]) == 10
    assert candidate(jobs = [1, 2, 3, 4],workers = [4, 3, 2, 1]) == 1
    assert candidate(jobs = [5, 2, 4],workers = [1, 7, 5]) == 2
    assert candidate(jobs = [3, 18, 15, 9],workers = [6, 5, 1, 3]) == 3
    assert candidate(jobs = [10, 20, 30, 40, 50],workers = [10, 10, 10, 10, 10]) == 5
    assert candidate(jobs = [5, 10, 15, 20, 25],workers = [5, 5, 5, 5, 5]) == 5
    assert candidate(jobs = [100, 200, 300, 400],workers = [50, 100, 150, 200]) == 2
    assert candidate(jobs = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1]) == 1
    assert candidate(jobs = [100000, 100000, 100000],workers = [1, 1, 1]) == 100000
    assert candidate(jobs = [10, 20, 30],workers = [5, 10, 15]) == 2
    assert candidate(jobs = [30, 20, 10],workers = [10, 20, 30]) == 1
    assert candidate(jobs = [1, 1, 1, 1],workers = [1, 1, 1, 1]) == 1
    assert candidate(jobs = [8, 6, 7, 5, 3, 0, 9],workers = [2, 3, 5, 7, 11, 13, 17]) == 1
    assert candidate(jobs = [1000, 2000, 3000, 4000, 5000],workers = [100, 200, 300, 400, 500]) == 10
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],workers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 2
    assert candidate(jobs = [12345, 67890, 54321, 98765, 43210],workers = [123, 456, 789, 1011, 1213]) == 101
    assert candidate(jobs = [1, 10, 100, 1000, 10000],workers = [10000, 1000, 100, 10, 1]) == 1
    assert candidate(jobs = [100, 100, 100, 100, 100],workers = [10, 10, 10, 10, 10]) == 10
    assert candidate(jobs = [99, 98, 97, 96, 95, 94, 93],workers = [100, 99, 98, 97, 96, 95, 94]) == 1
    assert candidate(jobs = [100000, 100000, 100000, 100000],workers = [1, 1, 1, 1]) == 100000
    assert candidate(jobs = [33, 67, 99, 1, 45, 78, 22, 56],workers = [2, 3, 4, 5, 6, 7, 8, 9]) == 11
    assert candidate(jobs = [100000, 1, 99999, 2],workers = [50000, 50000, 50000, 50000]) == 2
    assert candidate(jobs = [100000, 100000, 100000, 100000, 100000],workers = [100000, 100000, 100000, 100000, 100000]) == 1
    assert candidate(jobs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1
    assert candidate(jobs = [123, 456, 789, 101112, 131415],workers = [10, 20, 30, 40, 50]) == 2629
    assert candidate(jobs = [9, 7, 5, 3, 1],workers = [2, 4, 6, 8, 10]) == 1
    assert candidate(jobs = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111],workers = [11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999]) == 1
    assert candidate(jobs = [150, 200, 250, 300, 350],workers = [10, 20, 30, 40, 50]) == 15
    assert candidate(jobs = [1, 3, 5, 7, 9],workers = [2, 4, 6, 8, 10]) == 1
    assert candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
    assert candidate(jobs = [50, 100, 150, 200, 250],workers = [10, 20, 30, 40, 50]) == 5
    assert candidate(jobs = [50, 40, 30, 20, 10],workers = [5, 10, 15, 20, 25]) == 2
    assert candidate(jobs = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 1
    assert candidate(jobs = [5, 10, 15, 20, 25, 30],workers = [6, 12, 18, 24, 30, 36]) == 1
    assert candidate(jobs = [34, 67, 89, 23, 56],workers = [12, 45, 78, 90, 32]) == 2
    assert candidate(jobs = [100000, 90000, 80000, 70000, 60000],workers = [10000, 20000, 30000, 40000, 50000]) == 6
    assert candidate(jobs = [100000, 50000, 25000, 12500, 6250],workers = [1, 2, 4, 8, 16]) == 6250
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
    assert candidate(jobs = [5, 15, 25, 35, 45],workers = [10, 20, 30, 40, 50]) == 1
    assert candidate(jobs = [10, 20, 30, 40, 50],workers = [5, 10, 15, 20, 25]) == 2
    assert candidate(jobs = [40, 60, 80, 100, 120],workers = [20, 40, 60, 80, 100]) == 2
    assert candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(jobs = [5, 15, 25, 35, 45, 55, 65],workers = [10, 20, 30, 40, 50, 60, 70]) == 1
    assert candidate(jobs = [100000, 100000, 100000, 100000, 100000],workers = [1, 1, 1, 1, 1]) == 100000
    assert candidate(jobs = [3, 5, 8, 10, 15],workers = [1, 3, 5, 7, 9]) == 3
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(jobs = [34, 56, 78, 90, 12],workers = [45, 32, 89, 10, 67]) == 2
    assert candidate(jobs = [100000, 50000, 25000, 12500, 6250],workers = [10000, 20000, 25000, 31250, 62500]) == 2
    assert candidate(jobs = [500, 400, 300, 200, 100],workers = [100, 200, 300, 400, 500]) == 1
    assert candidate(jobs = [50, 40, 30, 20, 10],workers = [25, 20, 15, 10, 5]) == 2
    assert candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1
    assert candidate(jobs = [2, 4, 6, 8, 10],workers = [1, 3, 5, 7, 9]) == 2
    assert candidate(jobs = [500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500, 600]) == 5
    assert candidate(jobs = [10000, 10000, 10000, 10000, 10000],workers = [1, 1, 1, 1, 1]) == 10000
    assert candidate(jobs = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
    assert candidate(jobs = [150, 225, 300, 375, 450],workers = [50, 75, 100, 125, 150]) == 3
    assert candidate(jobs = [50, 25, 75, 100, 125],workers = [25, 20, 50, 10, 125]) == 3
    assert candidate(jobs = [300, 600, 900, 1200],workers = [150, 300, 450, 600]) == 2
    assert candidate(jobs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(jobs = [1000, 1000, 1000, 1000, 1000],workers = [1, 1, 1, 1, 1]) == 1000
    assert candidate(jobs = [1000, 500, 250, 125],workers = [125, 250, 500, 1000]) == 1
    assert candidate(jobs = [101, 202, 303, 404, 505],workers = [100, 200, 300, 400, 500]) == 2
    assert candidate(jobs = [1000, 2000, 3000, 4000, 5000],workers = [500, 1000, 1500, 2000, 2500]) == 2
    assert candidate(jobs = [99999, 88888, 77777, 66666, 55555],workers = [10000, 20000, 30000, 40000, 50000]) == 6
    assert candidate(jobs = [3, 1, 7, 4, 9],workers = [2, 8, 3, 6, 5]) == 2
    assert candidate(jobs = [1000, 999, 998, 997, 996],workers = [1, 2, 3, 4, 5]) == 996
    assert candidate(jobs = [15, 25, 35, 45, 55],workers = [10, 20, 30, 40, 50]) == 2
    assert candidate(jobs = [10, 20, 30, 40, 50],workers = [5, 10, 15, 20, 25]) == 2
    assert candidate(jobs = [1, 2, 3, 4, 5],workers = [999, 998, 997, 996, 995]) == 1
    assert candidate(jobs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(jobs = [34, 67, 89, 23, 56, 78, 90, 12, 34, 56],workers = [12, 23, 34, 45, 56, 67, 78, 89, 90, 100]) == 1
    assert candidate(jobs = [33333, 66666, 99999, 22222, 55555],workers = [11111, 22222, 33333, 44444, 55555]) == 2
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(jobs = [1, 2, 3, 4, 5],workers = [5, 4, 3, 2, 1]) == 1
    assert candidate(jobs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 1
    assert candidate(jobs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(jobs = [99999, 99998, 99997, 99996, 99995],workers = [1, 2, 3, 4, 5]) == 99995
    assert candidate(jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(jobs = [50, 50, 50, 50, 50, 50],workers = [10, 10, 10, 10, 10, 10]) == 5
    assert candidate(jobs = [1000, 2000, 3000, 4000],workers = [500, 1500, 2500, 3500]) == 2
    assert candidate(jobs = [50, 40, 30, 20, 10],workers = [10, 20, 30, 40, 50]) == 1
    assert candidate(jobs = [1, 1, 1, 1, 1],workers = [1000, 1000, 1000, 1000, 1000]) == 1
    assert candidate(jobs = [50, 40, 30, 20, 10],workers = [25, 20, 15, 10, 5]) == 2
    assert candidate(jobs = [1000, 2000, 3000, 4000, 5000],workers = [250, 500, 750, 1000, 1250]) == 4
    assert candidate(jobs = [9, 18, 27, 36, 45, 54],workers = [1, 2, 3, 4, 5, 6]) == 9
    assert candidate(jobs = [999, 1000, 1001, 1002, 1003],workers = [1, 2, 3, 4, 5]) == 999
    assert candidate(jobs = [345, 678, 901, 234, 567],workers = [456, 789, 101, 234, 567]) == 3
