# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),low = 6,high = 10) == 23
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),low = 7,high = 15) == 32
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 17, 23, 27, 32, 38]),low = 10,high = 30) == 179
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 7, 13, 17, 22, 27, 32, 37]),low = 10,high = 27) == 149
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 1,high = 100) == 775
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, 5, 15, 30, 45, 55, 65, 85, 95, 105, 115, 135, 145, 155, 165, 185, 195, 1, 9, 13, 18, 22, 35, 42, 48, 52, 58, 63, 67, 72, 78, 82, 88, 92, 98, 102, 108, 112, 118, 122, 128, 132, 138, 142, 148, 152, 158, 162, 168, 172, 178, 182, 188, 192, 198]),low = 40,high = 160) == 3900
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 50,high = 90) == 485
    assert candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 10, None, None, 45, 55, 65, 75, None]),low = 30,high = 70) == 415
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 22, 28, 32, 40]),low = 10,high = 30) == 180
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 100,high = 200) == 0
    assert candidate(root = tree_node([2, 1, 3, None, None, None, 4]),low = 3,high = 4) == 7
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 35, 50, 5, 12, 18, 25, 32, 40, 48, 55]),low = 10,high = 50) == 380
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 80, 110, 130, 160, 180]),low = 60,high = 140) == 680
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),low = 2,high = 13) == 90
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 110, 140, 160, 180]),low = 30,high = 140) == 775
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 80, 5, 15, 30, 40, 55, 65, 70, 85]),low = 20,high = 70) == 360
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),low = 4,high = 12) == 7
    assert candidate(root = tree_node([25, 15, 30, 10, 20, 28, 35, 5, 12, 17, 22, 27, 32, 38, 1, 7, 11, 14, 16, 19, 21, 24, 26, 29, 31, 33, 37, 39]),low = 15,high = 25) == 163
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, None, None, None, None, None, None, None, None]),low = 2,high = 8) == 35
    assert candidate(root = tree_node([15, 14, 16, 13, 15, 15, 17, 12, 14, 14, 15, 16, 16, 17, 18]),low = 13,high = 17) == 197
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190]),low = 50,high = 150) == 900
    assert candidate(root = tree_node([75, 50, 100, 25, 60, 80, 125, 10, 30, 55, 65, 70, 85, 105, 150, 5, 15, 20, 28, 40, 57, 63, 68, 72, 82, 88, 102, 110, 130, 140, 160, 175, 3, 8, 12, 18, 22, 27, 32, 42, 51, 59, 62, 66, 71, 74, 76, 81, 87, 90, 95, 101, 108, 112, 115, 120, 127, 132, 135, 138, 142, 145, 148, 152, 155, 158, 162, 165, 168, 170, 178, 182, 185, 188, 190, 192, 195, 198, 200]),low = 60,high = 130) == 2803
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 15, 35, 65, 85, 115, 135, 165, 185, 10, 20, 40, 55, 70, 80, 90, 110, 120, 130, 140, 150, 160, 170, 180, 190]),low = 50,high = 150) == 1790
    assert candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75]),low = 25,high = 65) == 405
    assert candidate(root = tree_node([15, 9, 25, 7, 12, 22, 30, 5, 8, 11, 13, 20, 24, 27, 33]),low = 12,high = 24) == 106
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 17, 22, 28, 32, 38]),low = 15,high = 35) == 224
    assert candidate(root = tree_node([2, 1, 3]),low = 1,high = 3) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),low = 5,high = 10) == 7
    assert candidate(root = tree_node([50, 30, 70, 10, 40, 60, 80, 5, 15, 35, 45, 55, 65, 75, 85]),low = 20,high = 70) == 450
    assert candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, 16, 19, 21, 24, 28, 35]),low = 15,high = 25) == 180
    assert candidate(root = tree_node([200, 100, 300, 50, 250, 350, 450, 25, 75, 150, 225, 275, 325, 375, 425, 475]),low = 75,high = 325) == 1575
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 45, 48, 55]),low = 20,high = 45) == 240
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, 8, None, None, 11, 14]),low = 3,high = 14) == 52
    assert candidate(root = tree_node([1, 0, 2]),low = 1,high = 3) == 3
    assert candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 10, 25, 35, 50, 65, 85, 95, 110]),low = 50,high = 90) == 420
    assert candidate(root = tree_node([80, 40, 120, 20, 60, 100, 140, 10, 30, 50, 70, 90, 110, 130, 150]),low = 50,high = 110) == 560
    assert candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),low = 5,high = 13) == 44
    assert candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 7, 11, 14, 16, 19, 22, 28]),low = 10,high = 20) == 135
    assert candidate(root = tree_node([10, 15, 3, 7, None, 18]),low = 7,high = 15) == 32
    assert candidate(root = tree_node([1, 0, 2, None, 3, None, None]),low = 1,high = 2) == 3
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 15, 30, 40, 55, 65, 80, 95]),low = 20,high = 80) == 515
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 55,high = 85) == 345
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, None, 10]),low = 3,high = 8) == 26
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 20, 30, 45, 55, 68, 80, 93, 3, 9, 15, 22, 28, 35, 40, 50, 60, 65, 70, 78, 85, 90, 96, 4, 8, 11, 13, 18, 24, 26, 29, 32, 34, 36, 39, 42, 48, 52, 58, 63, 67, 72, 75, 77, 82, 88, 91, 94, 98, 1, 5, 7, 10, 14, 17, 19, 21, 23, 25, 27, 31, 33, 38, 41, 43, 47, 51, 53, 57, 61, 64, 66, 69, 71, 73, 74, 76, 79, 81, 83, 86, 89, 92, 95, 97, 99]),low = 20,high = 60) == 924
    assert candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, 15, 25, 35, 45, 55, 65, 75, 85]),low = 35,high = 65) == 350
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 85, 110, 140, 160, 180]),low = 40,high = 140) == 745
    assert candidate(root = tree_node([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75]),low = 10,high = 80) == 595
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 35, 50, 5, 12, 17, 22, 32, 38, 40, 55, None, None, None, None, None, None, 9, None, 14, None, None, 16, None, None, None, None, 31, None, None, 37, None, None, 39, None, None, None, 53, None, None, None, 58]),low = 25,high = 40) == 172
    assert candidate(root = tree_node([8, 3, 10, None, 1, 6, None, 4, 7, 13, None, None, 14]),low = 2,high = 15) == 47
    assert candidate(root = tree_node([20, 15, 25, 10, 17, 22, 30, 5, 12, None, None, 18, 23, None, None, None, None, 2, 11]),low = 10,high = 23) == 148
    assert candidate(root = tree_node([9, 4, 17, 3, 6, 15, 22, None, None, None, 8, None, 16, None, None, 20]),low = 5,high = 16) == 54
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 45,high = 65) == 275
    assert candidate(root = tree_node([1, 3, 2]),low = 1,high = 3) == 3
    assert candidate(root = tree_node([30, 20, 40, 15, 25, 35, 45, 10, 18, 23, 27, 33, 37, 42, 47]),low = 25,high = 35) == 150
    assert candidate(root = tree_node([10, 5, None, 3, 7, 6, None]),low = 5,high = 10) == 22
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 22, 35, 43, 48, 55, 2, 7, 11, 14, 16, 18, 21, 23, 32, 37, 41, 44, 47, 49, 52, 53, 57, 58, 60]),low = 15,high = 50) == 693
    assert candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 16, None, None, 19, None]),low = 15,high = 25) == 116
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 15,high = 40) == 140
    assert candidate(root = tree_node([4, 2, 9, 1, 3, 8, 10, None, None, None, None, 5, 7]),low = 3,high = 8) == 20
    assert candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, 15, 27, 35, 55, 65, 85, 100]),low = 20,high = 70) == 347
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 35,high = 80) == 430
    assert candidate(root = tree_node([70, 35, 105, 15, 55, 85, 120, 10, 25, 45, 65, 75, 95, 110, 130, 8, 12, 22, 40, 50, 60, 72, 78, 88, 92, 108, 115, 125, 135]),low = 20,high = 115) == 1490
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 23, 28, 33, 38, 45]),low = 12,high = 38) == 277
    assert candidate(root = tree_node([1, 0, 2, 3, None, None, None, None, 4]),low = 0,high = 3) == 3
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 5,high = 50) == 245
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 10,high = 95) == 775
    assert candidate(root = tree_node([50, 30, 80, 15, 40, 60, 90, 10, 20, 35, 45, 55, 65, 85, 95]),low = 30,high = 60) == 315
    assert candidate(root = tree_node([15, 9, 20, 7, 13, 18, 23, 5, 8, 11, 14, 17, 21, 22, 24]),low = 10,high = 20) == 108
    assert candidate(root = tree_node([50, 20, 70, 10, 30, 60, 80, 5, 15, 25, 35, 55, 65, 75, 85, 2, 8, None, None, None, 18, None, None, 28, None, 32, 38, None, None, None, None, 52, 58, None, None, None, 62, 68, None, None, None, 72, 78, None, None, None, 82, None, 88]),low = 15,high = 65) == 495
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 43, 48, 55]),low = 15,high = 50) == 369
    assert candidate(root = tree_node([500, 250, 750, 125, 375, 625, 875, 63, 188, 313, 438, 563, 688, 813, 938, 42, 94]),low = 125,high = 750) == 4815
    assert candidate(root = tree_node([1]),low = 1,high = 1) == 1
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 130, 160, 180]),low = 30,high = 160) == 1070
    assert candidate(root = tree_node([3, 1, 4, None, 2]),low = 1,high = 3) == 6
    assert candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),low = 6,high = 10) == 31
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 48, None, None, None, None, None, None, None, None, None, None]),low = 12,high = 40) == 195
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 48, 3, 7, 11, 16, 23, 28, 37, 42, 47, 49]),low = 10,high = 45) == 380
    assert candidate(root = tree_node([75, 50, 100, 25, 60, 80, 120, 10, 35, 55, 65, 78, 90, 110, 130]),low = 40,high = 100) == 653
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20]),low = 1,high = 20) == 54
    assert candidate(root = tree_node([50, 25, 75, 10, 35, 60, 90, 5, 15, 30, 40, 55, 65, 80, 95]),low = 25,high = 75) == 435
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 180]),low = 40,high = 140) == 790
