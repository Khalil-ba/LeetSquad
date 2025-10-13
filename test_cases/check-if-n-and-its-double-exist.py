# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr = [2, 4, 6, 8, 10]) == True
    assert candidate(arr = [6, 10, 1, 0, -3, 3]) == True
    assert candidate(arr = [-3, -6, -1, 0, 1, 2, 3]) == True
    assert candidate(arr = [-2, -4, -6, -8, -10]) == True
    assert candidate(arr = [100, 200, 300, 400, 500]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64]) == True
    assert candidate(arr = [-10, -20, -5, -3]) == True
    assert candidate(arr = [1, 2, 3, 6, 12]) == True
    assert candidate(arr = [0, 0]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(arr = [-10, 10]) == False
    assert candidate(arr = [10, 2, 5, 3]) == True
    assert candidate(arr = [1, 2, 3, 4, 5]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6]) == True
    assert candidate(arr = [1, 2, 4, 8, 16]) == True
    assert candidate(arr = [-2, 0, 10, -19, 4, 6, -8]) == False
    assert candidate(arr = [1, 3, 5, 7, 9]) == False
    assert candidate(arr = [3, 1, 7, 11]) == False
    assert candidate(arr = [-10, -20, -30, -40, -50]) == True
    assert candidate(arr = [-10, -5, -3, -1, 2]) == True
    assert candidate(arr = [10, 5, 15, 20, 25]) == True
    assert candidate(arr = [1, -1, 2, -2, 4, -4, 8, -8, 16, -16]) == True
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8]) == True
    assert candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == True
    assert candidate(arr = [2, 1, 4, 2, 8, 4, 16]) == True
    assert candidate(arr = [1, 2, 3, 5, 6, 10, 20, 40]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == True
    assert candidate(arr = [-100, -50, -25, -12, -6, -3, -1, 0, 1, 2, 4]) == True
    assert candidate(arr = [4, 8, 16, 32, 64, 128, 256, 512]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5]) == True
    assert candidate(arr = [-1, -2, -3, -4, -5, -10, -20]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == True
    assert candidate(arr = [0, 0, 0, 0]) == True
    assert candidate(arr = [100, 50, 25, 12, 6, 3, 1]) == True
    assert candidate(arr = [101, 202, 50, 25, 12, 6, 3]) == True
    assert candidate(arr = [1000, 501, 250, 125, 62, 31, 15, 7, 3, 1]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 60]) == True
    assert candidate(arr = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) == False
    assert candidate(arr = [100, 50, 25, 125, 625, 3125]) == True
    assert candidate(arr = [-1, 2, -3, 6, -4, 8]) == False
    assert candidate(arr = [-10, -20, 5, 3, 15]) == True
    assert candidate(arr = [100, 200, 300, 400, 500, 250, 125]) == True
    assert candidate(arr = [-1, -2, -3, -6, -12]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == True
    assert candidate(arr = [100, 50, 25, 12.5, 6.25, 3.125, 1.5625]) == True
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [1, 0, 2, 0, 4, 0, 8, 0]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200]) == True
    assert candidate(arr = [3, 6, 9, 18, 27, 54, 81]) == True
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56]) == True
    assert candidate(arr = [1, 2, 3, 6, 9, 18, 36, 72]) == True
    assert candidate(arr = [-1, -2, -3, -4, -5]) == True
    assert candidate(arr = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == True
    assert candidate(arr = [1, 5, 10, 15, 20, 25, 50, 100]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == True
    assert candidate(arr = [2, 4, 8, 16, 32, 64, 128, 256, 512]) == True
    assert candidate(arr = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == True
    assert candidate(arr = [1, 2, 3, 6, 12, 24, 48, 96, 192, 384]) == True
    assert candidate(arr = [-1, -2, -4, -8, -16]) == True
    assert candidate(arr = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == True
    assert candidate(arr = [0, 0, 1, 2, 4]) == True
    assert candidate(arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 220, 330, 440, 550, 660, 770, 880, 990, 1100]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 38]) == True
    assert candidate(arr = [1, 2, 3, 5, 6, 10, 15, 20, 30, 60]) == True
    assert candidate(arr = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]) == True
    assert candidate(arr = [-2, 2, -4, 4, -8, 8, -16, 16]) == True
    assert candidate(arr = [-10, -5, -15, -20, -25]) == True
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == True
    assert candidate(arr = [-1, 1, -2, 2, -4, 4, 8, -8]) == True
    assert candidate(arr = [0, 1, 2, 3, 6, 12, 24, 48, 96]) == True
    assert candidate(arr = [13, 26, 52, 104, 208, 416]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(arr = [-5, 10, -15, 20, -25, 50, -75]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 50, 75]) == True
    assert candidate(arr = [21, 42, 84, 168, 336, 672, 1344]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == True
    assert candidate(arr = [5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560]) == True
    assert candidate(arr = [6, 12, 18, 24, 48]) == True
    assert candidate(arr = [1, 0, 2, 0, 4, 0, 8, 0, 16, 0]) == True
    assert candidate(arr = [1, 2, 3, 6, 12, 24, 48, 96]) == True
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 40]) == True
    assert candidate(arr = [1000, -500, 250, -125, 62.5, 31.25]) == True
    assert candidate(arr = [-1, 2, -2, 4, -4, 8]) == True
    assert candidate(arr = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == True
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
    assert candidate(arr = [1, 5, 25, 125, 625, 3125, 15625, 78125]) == False
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == True
    assert candidate(arr = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 8]) == True
    assert candidate(arr = [15, 30, 45, 90, 135, 270]) == True
    assert candidate(arr = [-10, -5, -1, -2, -3, -4, -6, -8, -12, -16]) == True
    assert candidate(arr = [100, 200, 300, 400, 500, 1000, 2000]) == True
    assert candidate(arr = [10, 20, 40, 80, 160, 320, 640]) == True
    assert candidate(arr = [-10, -5, 0, 5, 10]) == True
    assert candidate(arr = [-10, -20, -30, -40, -50, -100, -200, -300]) == True
    assert candidate(arr = [-3, -6, -9, -12, -15, -18, -21, -24]) == True
    assert candidate(arr = [3, 6, 12, 24, 48, 96, 192, 384]) == True
    assert candidate(arr = [0, 0, 0, 0, 0]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(arr = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == True
    assert candidate(arr = [-5, -10, -15, -20, -25, -30, -35, -40, -45]) == True
    assert candidate(arr = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]) == False
    assert candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16]) == True
    assert candidate(arr = [100, 200, 300, 400, 500, 10]) == True
    assert candidate(arr = [11, 22, 44, 88, 176, 352, 704]) == True
    assert candidate(arr = [0, 0, 0, 0, 0]) == True
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24]) == True
    assert candidate(arr = [100, 51, 25, 12, 6, 3, 1]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 17, 19, 21]) == False
    assert candidate(arr = [0, 1, 2, 4, 8, 16, 32]) == True
    assert candidate(arr = [0, 0, 0, 0, 0, 0]) == True
    assert candidate(arr = [1, 3, 9, 27, 81, 243, 729]) == False
    assert candidate(arr = [0, 1, 2, 3, 4, 8, 16]) == True
    assert candidate(arr = [5, 10, 15, 20, 25, 50, 100]) == True
    assert candidate(arr = [9, 18, 36, 72, 144, 288, 576]) == True
    assert candidate(arr = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == True
    assert candidate(arr = [1, 3, 5, 7, 9, 18, 36, 72]) == True
    assert candidate(arr = [7, 14, 28, 56, 112, 224, 448]) == True
    assert candidate(arr = [1000, 500, 250, 125, 62.5]) == True
    assert candidate(arr = [1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 768]) == True
    assert candidate(arr = [100, 50, 25, 12, 6, 3, 1, 0]) == True
    assert candidate(arr = [1, 5, 10, 20, 25, 50, 100]) == True
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]) == True
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == True
    assert candidate(arr = [-2, -4, -6, -8, -16]) == True
    assert candidate(arr = [-10, -20, -30, -200, -300, -150]) == True
    assert candidate(arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == True
    assert candidate(arr = [0, 1, 2, 4, 8, 16, 32, 64]) == True
    assert candidate(arr = [1, 2, 3, 5, 6, 10, 15, 20, 30, 60, 120, 240]) == True
    assert candidate(arr = [100, 50, 25, 12, 6, 3, 1, 0, -1, -2, -4]) == True
    assert candidate(arr = [7, 14, 28, 56, 112, 224]) == True
    assert candidate(arr = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == True
    assert candidate(arr = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == True
    assert candidate(arr = [7, 14, 28, 56, 112, 224, 448, 896]) == True
    assert candidate(arr = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 115]) == True
    assert candidate(arr = [10, 5, 15, 20, 2, 25, 50]) == True
    assert candidate(arr = [-2, -4, -1, -3, -5, -10]) == True
    assert candidate(arr = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == True
    assert candidate(arr = [-1, -2, -4, -8, -16, -32, -64]) == True
    assert candidate(arr = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32]) == True
    assert candidate(arr = [1, 2, 3, 6, 9, 18, 27, 54]) == True
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == True
    assert candidate(arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == True
    assert candidate(arr = [1, 0, 2, 0, 4, 0, 8, 0, 16, 0, 32, 0, 64, 0, 128, 0]) == True
    assert candidate(arr = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == True
    assert candidate(arr = [-2, -4, -8, -16, -32, -64, -128]) == True
