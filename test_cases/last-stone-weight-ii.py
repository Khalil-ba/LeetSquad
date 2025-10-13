# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(stones = [10, 10, 10, 10, 10]) == 10
    assert candidate(stones = [3, 9, 7, 3]) == 2
    assert candidate(stones = [1, 2, 3, 4, 5]) == 1
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0
    assert candidate(stones = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(stones = [100, 1]) == 99
    assert candidate(stones = [31, 26, 33, 21, 40]) == 5
    assert candidate(stones = [15, 10, 5, 10, 10]) == 0
    assert candidate(stones = [1, 100, 100, 1]) == 0
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(stones = [10, 10, 10, 10]) == 0
    assert candidate(stones = [1]) == 1
    assert candidate(stones = [2, 7, 4, 1, 8, 1]) == 1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(stones = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 65
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0
    assert candidate(stones = [9, 3, 9, 8, 7, 8, 5, 4]) == 1
    assert candidate(stones = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]) == 5
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
    assert candidate(stones = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9
    assert candidate(stones = [50, 25, 25, 75, 100, 50]) == 25
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 0
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 1
    assert candidate(stones = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == 1
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 0
    assert candidate(stones = [49, 98, 147, 196, 245, 294, 343, 392, 441, 490]) == 49
    assert candidate(stones = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40]) == 15
    assert candidate(stones = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 0
    assert candidate(stones = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1
    assert candidate(stones = [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == 0
    assert candidate(stones = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6, 700, 7, 800, 8, 900, 9, 1000, 10, 1100, 11, 1200, 12, 1300, 13, 1400, 14]) == 1
    assert candidate(stones = [8, 14, 22, 26, 28, 30, 35, 40, 43, 45, 47, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1
    assert candidate(stones = [45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(stones = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 5
    assert candidate(stones = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91, 11, 90, 12, 89, 13, 88]) == 1
    assert candidate(stones = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 1
    assert candidate(stones = [10, 22, 33, 44, 55, 66, 77, 88, 99, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 0
    assert candidate(stones = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(stones = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 0
    assert candidate(stones = [80, 20, 60, 40, 30, 70, 50, 10, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290]) == 10
    assert candidate(stones = [88, 77, 66, 55, 44, 33, 22, 11, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300]) == 0
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
    assert candidate(stones = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(stones = [8, 3, 5, 7, 11, 9, 14, 16, 2, 6]) == 1
    assert candidate(stones = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 95
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(stones = [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(stones = [8, 8, 8, 8, 8, 8, 8, 8]) == 0
    assert candidate(stones = [50, 50, 50, 50, 50, 50, 50]) == 50
    assert candidate(stones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1
    assert candidate(stones = [8, 6, 7, 5, 3, 0, 9]) == 0
    assert candidate(stones = [12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(stones = [99, 1, 100, 1, 100, 1, 100, 1, 100]) == 95
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(stones = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(stones = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 1
    assert candidate(stones = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 0
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(stones = [29, 10, 15, 30, 25, 5]) == 4
    assert candidate(stones = [10, 14, 10, 4, 7, 12]) == 1
    assert candidate(stones = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 1
    assert candidate(stones = [5, 8, 12, 9, 15, 20, 18]) == 1
    assert candidate(stones = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]) == 1
    assert candidate(stones = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 0
    assert candidate(stones = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 0
    assert candidate(stones = [100, 1, 2, 3, 99]) == 1
    assert candidate(stones = [20, 30, 40, 50, 60, 70]) == 10
    assert candidate(stones = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 72
    assert candidate(stones = [30, 20, 10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(stones = [100, 1, 99, 2, 98, 3, 97, 4]) == 0
    assert candidate(stones = [29, 22, 24, 27, 30, 31, 28, 25, 21, 20]) == 1
    assert candidate(stones = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 1
    assert candidate(stones = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0
    assert candidate(stones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(stones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 0
    assert candidate(stones = [20, 15, 10, 5, 30, 25, 40, 50]) == 5
    assert candidate(stones = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 8888889
    assert candidate(stones = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 5
    assert candidate(stones = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 0
    assert candidate(stones = [100, 50, 25, 12, 6, 3, 1]) == 3
    assert candidate(stones = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0
    assert candidate(stones = [25, 25, 25, 25, 25, 25, 25, 25]) == 0
    assert candidate(stones = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 0
    assert candidate(stones = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 55
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10]) == 0
    assert candidate(stones = [50, 49, 51, 48, 52]) == 44
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
    assert candidate(stones = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 100]) == 13
    assert candidate(stones = [8, 14, 17, 31, 56, 13, 29]) == 2
    assert candidate(stones = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 50
    assert candidate(stones = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 1
    assert candidate(stones = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(stones = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 1
    assert candidate(stones = [2, 3, 7, 8, 10, 12, 15, 18, 20, 25]) == 0
    assert candidate(stones = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 50
    assert candidate(stones = [100, 99, 98, 97, 96, 95]) == 1
