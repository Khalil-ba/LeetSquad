# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(piles = [1, 2, 3, 4, 5],k = 10) == 5
    assert candidate(piles = [10, 10, 10, 10],k = 4) == 20
    assert candidate(piles = [5, 4, 9],k = 2) == 12
    assert candidate(piles = [10, 10, 10],k = 1) == 25
    assert candidate(piles = [100, 200, 300],k = 10) == 57
    assert candidate(piles = [4, 3, 6, 7],k = 3) == 12
    assert candidate(piles = [100, 200, 300],k = 1) == 450
    assert candidate(piles = [10000, 10000, 10000],k = 10000) == 3
    assert candidate(piles = [100, 200, 300],k = 2) == 350
    assert candidate(piles = [100, 100, 100],k = 10) == 33
    assert candidate(piles = [1],k = 1) == 1
    assert candidate(piles = [10000, 10000, 10000],k = 10000) == 3
    assert candidate(piles = [10, 10, 10],k = 5) == 11
    assert candidate(piles = [1, 2, 3, 4, 5],k = 5) == 8
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 15
    assert candidate(piles = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930],k = 5000) == 10
    assert candidate(piles = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 1],k = 100) == 25
    assert candidate(piles = [5000, 5000, 5000, 5000, 5000],k = 25000) == 5
    assert candidate(piles = [1000, 500, 250, 125],k = 10) == 252
    assert candidate(piles = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 100) == 20
    assert candidate(piles = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 100) == 10
    assert candidate(piles = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 50) == 1441
    assert candidate(piles = [9999, 9998, 9997, 9996, 9995],k = 100) == 5
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(piles = [1000, 999, 998, 997, 996, 995],k = 15) == 1123
    assert candidate(piles = [10000, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19],k = 50) == 149
    assert candidate(piles = [9999],k = 10000) == 1
    assert candidate(piles = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000) == 10
    assert candidate(piles = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 100) == 10
    assert candidate(piles = [1, 10, 100, 1000, 10000],k = 100) == 5
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 50) == 10
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 117
    assert candidate(piles = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991],k = 1000) == 10
    assert candidate(piles = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 1000) == 20
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 32
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 10
    assert candidate(piles = [1, 100, 1000, 10000, 10000, 1000, 100, 1],k = 50000) == 8
    assert candidate(piles = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 100) == 50
    assert candidate(piles = [50, 25, 75, 200, 150],k = 5) == 201
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 20
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 20
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 20
    assert candidate(piles = [10000, 1000, 100, 10, 1],k = 15000) == 5
    assert candidate(piles = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1000) == 20
    assert candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 200) == 10
    assert candidate(piles = [5000, 5000, 5000, 5000, 5000],k = 1000) == 5
    assert candidate(piles = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 1000) == 10
    assert candidate(piles = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256, 256, 512, 512],k = 100) == 20
    assert candidate(piles = [9999, 10000, 10001],k = 10000) == 3
    assert candidate(piles = [1000, 500, 250, 125, 63, 32, 16, 8, 4, 2, 1],k = 30) == 63
    assert candidate(piles = [999, 1000, 1001, 1002, 1003],k = 10) == 1253
    assert candidate(piles = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 2500) == 20
    assert candidate(piles = [10000, 5000, 2500, 1250, 625],k = 20) == 785
    assert candidate(piles = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 30) == 63
    assert candidate(piles = [5000, 5000, 5000, 5000, 5000],k = 100000) == 5
    assert candidate(piles = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 1000) == 20
    assert candidate(piles = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 20
    assert candidate(piles = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],k = 50) == 1441
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 100) == 15
    assert candidate(piles = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 500) == 20
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 20
    assert candidate(piles = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 20) == 253
    assert candidate(piles = [9999, 9999, 9999, 9999],k = 100000) == 4
    assert candidate(piles = [1, 10, 100, 1000, 10000],k = 10) == 315
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 20
    assert candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1000) == 10
    assert candidate(piles = [500, 300, 200, 100],k = 5) == 400
    assert candidate(piles = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 30) == 31
    assert candidate(piles = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111],k = 10000) == 9
    assert candidate(piles = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 100) == 11
    assert candidate(piles = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 5000) == 31
    assert candidate(piles = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 50) == 3130
    assert candidate(piles = [5000, 4000, 3000, 2000, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 100) == 16
    assert candidate(piles = [1048576, 1048576, 1048576, 1048576, 1048576, 1048576, 1048576, 1048576, 1048576, 1048576],k = 100000) == 10
    assert candidate(piles = [10, 15, 20, 25, 30, 35, 40, 45, 50],k = 100) == 9
    assert candidate(piles = [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],k = 10000) == 20
    assert candidate(piles = [9999, 1, 2, 3, 4, 5],k = 10) == 25
    assert candidate(piles = [1000, 1000, 1000, 1000, 1000],k = 50) == 5
    assert candidate(piles = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 100) == 10
    assert candidate(piles = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 5000) == 10
    assert candidate(piles = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 50000) == 10
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 30
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 100) == 20
