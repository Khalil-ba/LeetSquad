# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(capacity = [2, 3, 4, 5],rocks = [1, 2, 4, 4],additionalRocks = 2) == 3
    assert candidate(capacity = [1, 2, 3],rocks = [0, 0, 0],additionalRocks = 5) == 2
    assert candidate(capacity = [3, 2, 1],rocks = [0, 0, 0],additionalRocks = 5) == 2
    assert candidate(capacity = [1, 1, 1],rocks = [0, 0, 0],additionalRocks = 3) == 3
    assert candidate(capacity = [3, 9, 8],rocks = [0, 2, 5],additionalRocks = 6) == 2
    assert candidate(capacity = [5, 5, 5, 5],rocks = [0, 0, 0, 0],additionalRocks = 10) == 2
    assert candidate(capacity = [1, 1, 1, 1],rocks = [1, 1, 1, 1],additionalRocks = 1) == 4
    assert candidate(capacity = [3, 3, 3],rocks = [3, 0, 0],additionalRocks = 3) == 2
    assert candidate(capacity = [10, 2, 2],rocks = [2, 2, 0],additionalRocks = 100) == 3
    assert candidate(capacity = [5, 5, 5],rocks = [0, 0, 0],additionalRocks = 10) == 2
    assert candidate(capacity = [1, 1, 1, 1],rocks = [1, 1, 1, 1],additionalRocks = 4) == 4
    assert candidate(capacity = [5, 5, 5],rocks = [0, 0, 0],additionalRocks = 15) == 3
    assert candidate(capacity = [3, 3, 3],rocks = [1, 2, 3],additionalRocks = 2) == 2
    assert candidate(capacity = [20, 20, 20, 20, 20, 20],rocks = [0, 5, 10, 15, 20, 25],additionalRocks = 30) == 5
    assert candidate(capacity = [1, 3, 5, 7, 9],rocks = [0, 1, 2, 3, 4],additionalRocks = 10) == 4
    assert candidate(capacity = [100, 200, 300, 400, 500],rocks = [0, 0, 0, 0, 0],additionalRocks = 1500) == 5
    assert candidate(capacity = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 2500) == 9
    assert candidate(capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 5) == 5
    assert candidate(capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 5) == 5
    assert candidate(capacity = [10, 10, 10, 10, 10],rocks = [0, 0, 0, 0, 0],additionalRocks = 45) == 4
    assert candidate(capacity = [5, 8, 10, 15, 20],rocks = [0, 4, 7, 10, 15],additionalRocks = 20) == 4
    assert candidate(capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 55) == 10
    assert candidate(capacity = [100, 200, 300, 400, 500],rocks = [50, 150, 250, 350, 450],additionalRocks = 500) == 5
    assert candidate(capacity = [1, 2, 3, 4, 5, 6],rocks = [0, 0, 0, 0, 0, 0],additionalRocks = 20) == 5
    assert candidate(capacity = [500000000, 500000000, 500000000],rocks = [0, 0, 0],additionalRocks = 1000000000) == 2
    assert candidate(capacity = [10, 20, 30, 40, 50],rocks = [10, 20, 30, 40, 0],additionalRocks = 50) == 5
    assert candidate(capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],rocks = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4],additionalRocks = 15) == 6
    assert candidate(capacity = [10, 20, 30, 40, 50],rocks = [1, 2, 3, 4, 5],additionalRocks = 90) == 4
    assert candidate(capacity = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],rocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],additionalRocks = 5) == 5
    assert candidate(capacity = [10, 10, 10, 10, 10],rocks = [0, 0, 0, 0, 0],additionalRocks = 30) == 3
    assert candidate(capacity = [5, 5, 5, 5, 5],rocks = [1, 2, 3, 4, 5],additionalRocks = 10) == 5
    assert candidate(capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 5) == 5
    assert candidate(capacity = [100, 200, 300, 400, 500],rocks = [90, 180, 270, 360, 450],additionalRocks = 100) == 4
    assert candidate(capacity = [10, 10, 10, 10, 10],rocks = [5, 5, 5, 5, 5],additionalRocks = 25) == 5
    assert candidate(capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],rocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],additionalRocks = 10) == 10
    assert candidate(capacity = [1000000000, 500000000, 250000000],rocks = [0, 0, 0],additionalRocks = 1500000000) == 2
    assert candidate(capacity = [2, 4, 6, 8, 10],rocks = [0, 1, 2, 3, 4],additionalRocks = 10) == 3
    assert candidate(capacity = [1000000000, 1000000000, 1000000000],rocks = [0, 0, 0],additionalRocks = 2000000000) == 2
    assert candidate(capacity = [50, 50, 50, 50, 50],rocks = [0, 0, 0, 0, 0],additionalRocks = 100) == 2
    assert candidate(capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 10) == 10
    assert candidate(capacity = [10, 20, 30, 40, 50],rocks = [0, 0, 0, 0, 0],additionalRocks = 150) == 5
    assert candidate(capacity = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 10) == 4
    assert candidate(capacity = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],rocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],additionalRocks = 300) == 10
    assert candidate(capacity = [999999999, 1],rocks = [0, 0],additionalRocks = 1000000000) == 2
    assert candidate(capacity = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 550) == 10
    assert candidate(capacity = [100, 100, 100, 100],rocks = [100, 100, 100, 100],additionalRocks = 100) == 4
    assert candidate(capacity = [2, 4, 6, 8, 10],rocks = [1, 1, 1, 1, 1],additionalRocks = 15) == 3
    assert candidate(capacity = [50, 50, 50, 50, 50],rocks = [10, 20, 30, 40, 50],additionalRocks = 100) == 5
    assert candidate(capacity = [9, 8, 7, 6, 5, 4, 3, 2, 1],rocks = [1, 2, 3, 4, 5, 6, 7, 8, 9],additionalRocks = 20) == 9
    assert candidate(capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 10) == 10
    assert candidate(capacity = [5, 15, 25, 35, 45],rocks = [2, 8, 14, 20, 26],additionalRocks = 120) == 5
    assert candidate(capacity = [100, 200, 300, 400, 500],rocks = [0, 100, 200, 300, 400],additionalRocks = 500) == 5
    assert candidate(capacity = [5, 10, 15, 20, 25, 30, 35],rocks = [0, 0, 0, 0, 0, 0, 0],additionalRocks = 105) == 6
    assert candidate(capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],rocks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],additionalRocks = 45) == 10
    assert candidate(capacity = [1, 3, 5, 7, 9],rocks = [0, 0, 0, 0, 0],additionalRocks = 25) == 5
    assert candidate(capacity = [1, 2, 4, 8, 16, 32, 64, 128],rocks = [0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 255) == 8
    assert candidate(capacity = [10, 20, 30, 40, 50],rocks = [0, 0, 0, 0, 0],additionalRocks = 100) == 4
    assert candidate(capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],rocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],additionalRocks = 1) == 10
    assert candidate(capacity = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],rocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],additionalRocks = 55) == 10
    assert candidate(capacity = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25],rocks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],additionalRocks = 50) == 10
    assert candidate(capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],rocks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],additionalRocks = 15) == 10
    assert candidate(capacity = [100, 200, 300, 400, 500],rocks = [50, 100, 150, 200, 250],additionalRocks = 500) == 4
    assert candidate(capacity = [10, 10, 10, 10, 10],rocks = [5, 5, 5, 5, 5],additionalRocks = 15) == 3
    assert candidate(capacity = [100, 200, 300, 400, 500],rocks = [50, 100, 150, 200, 250],additionalRocks = 1000) == 5
    assert candidate(capacity = [1000000000, 1000000000],rocks = [0, 1],additionalRocks = 1999999999) == 2
    assert candidate(capacity = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],rocks = [999999999, 999999998, 999999997, 999999996, 999999995],additionalRocks = 10000000000) == 5
    assert candidate(capacity = [1000000000, 1000000000, 1000000000],rocks = [0, 0, 0],additionalRocks = 3000000000) == 3
    assert candidate(capacity = [1, 2, 4, 8, 16, 32],rocks = [0, 1, 3, 7, 15, 31],additionalRocks = 63) == 6
    assert candidate(capacity = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 50) == 5
    assert candidate(capacity = [10, 10, 10, 10, 10],rocks = [9, 8, 7, 6, 5],additionalRocks = 5) == 2
    assert candidate(capacity = [10, 10, 10, 10, 10],rocks = [0, 2, 4, 6, 8],additionalRocks = 15) == 3
    assert candidate(capacity = [1000, 2000, 3000, 4000, 5000],rocks = [500, 1000, 1500, 2000, 2500],additionalRocks = 5000) == 4
    assert candidate(capacity = [100, 200, 300, 400, 500],rocks = [50, 100, 150, 200, 250],additionalRocks = 100) == 1
    assert candidate(capacity = [100, 200, 300],rocks = [50, 100, 150],additionalRocks = 200) == 2
    assert candidate(capacity = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],rocks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],additionalRocks = 100) == 19
    assert candidate(capacity = [3, 6, 9, 12, 15],rocks = [0, 3, 6, 9, 12],additionalRocks = 20) == 5
    assert candidate(capacity = [10, 20, 30, 40, 50],rocks = [1, 2, 3, 4, 5],additionalRocks = 80) == 3
    assert candidate(capacity = [1000000000, 1000000000, 1000000000],rocks = [0, 0, 0],additionalRocks = 2000000000) == 2
    assert candidate(capacity = [10, 15, 20, 25, 30],rocks = [0, 5, 10, 20, 25],additionalRocks = 50) == 5
    assert candidate(capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],rocks = [0, 2, 4, 6, 8, 10, 0, 0, 0, 0],additionalRocks = 20) == 9
    assert candidate(capacity = [1000000, 2000000, 3000000, 4000000, 5000000],rocks = [100000, 200000, 300000, 400000, 500000],additionalRocks = 5000000) == 2
    assert candidate(capacity = [100, 100, 100, 100],rocks = [99, 98, 97, 96],additionalRocks = 4) == 2
    assert candidate(capacity = [1, 2, 3, 4, 5],rocks = [0, 1, 2, 3, 4],additionalRocks = 10) == 5
    assert candidate(capacity = [10, 20, 30, 40, 50],rocks = [10, 20, 30, 40, 50],additionalRocks = 100) == 5
    assert candidate(capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],rocks = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],additionalRocks = 5) == 5
    assert candidate(capacity = [100, 200, 300, 400, 500],rocks = [90, 190, 290, 390, 490],additionalRocks = 50) == 5
    assert candidate(capacity = [1000000000, 1000000000, 1000000000],rocks = [500000000, 500000000, 500000000],additionalRocks = 1500000000) == 3
    assert candidate(capacity = [10, 10, 10, 10, 10],rocks = [0, 0, 0, 0, 0],additionalRocks = 25) == 2
    assert candidate(capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 5) == 2
    assert candidate(capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 55) == 10
    assert candidate(capacity = [10, 20, 30, 40, 50],rocks = [9, 19, 29, 39, 49],additionalRocks = 5) == 5
    assert candidate(capacity = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],rocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],additionalRocks = 45) == 10
    assert candidate(capacity = [7, 7, 7, 7, 7, 7, 7],rocks = [1, 2, 3, 4, 5, 6, 0],additionalRocks = 14) == 4
    assert candidate(capacity = [5, 5, 5, 5, 5],rocks = [0, 1, 2, 3, 4],additionalRocks = 10) == 4
    assert candidate(capacity = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 55) == 10
    assert candidate(capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],rocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],additionalRocks = 5) == 1
    assert candidate(capacity = [10, 10, 10, 10, 10],rocks = [1, 2, 3, 4, 5],additionalRocks = 15) == 2
    assert candidate(capacity = [100, 200, 300, 400, 500],rocks = [10, 20, 30, 40, 50],additionalRocks = 1000) == 4
    assert candidate(capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],rocks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],additionalRocks = 55) == 10
    assert candidate(capacity = [10, 20, 30, 40, 50],rocks = [0, 5, 10, 15, 20],additionalRocks = 100) == 5
    assert candidate(capacity = [100000000, 100000000, 100000000],rocks = [50000000, 50000000, 50000000],additionalRocks = 100000000) == 2
    assert candidate(capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],rocks = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4],additionalRocks = 25) == 12
    assert candidate(capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],rocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],additionalRocks = 10) == 10
