# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr1 = [10, 20, 30],arr2 = [5, 15, 25],d = 4) == 3
    assert candidate(arr1 = [-1000, 1000],arr2 = [-500, 500],d = 499) == 2
    assert candidate(arr1 = [4, 5, 8],arr2 = [10, 9, 1, 8],d = 2) == 2
    assert candidate(arr1 = [1, 4, 2, 3],arr2 = [-4, -3, 6, 10, 20, 30],d = 3) == 2
    assert candidate(arr1 = [-1, -2, -3],arr2 = [1, 2, 3],d = 2) == 2
    assert candidate(arr1 = [0, 0, 0, 0],arr2 = [1, 2, 3, 4],d = 0) == 4
    assert candidate(arr1 = [1000],arr2 = [-1000],d = 1999) == 1
    assert candidate(arr1 = [1],arr2 = [1],d = 0) == 0
    assert candidate(arr1 = [2, 1, 100, 3],arr2 = [-5, -2, 10, -3, 7],d = 6) == 1
    assert candidate(arr1 = [1, 2, 3],arr2 = [4, 5, 6],d = 0) == 3
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9, 10],d = 1) == 4
    assert candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],d = 49) == 0
    assert candidate(arr1 = [-1000, -900, -800, -700, -600],arr2 = [600, 700, 800, 900, 1000],d = 100) == 5
    assert candidate(arr1 = [-100, -200, -300],arr2 = [-50, -150, -250],d = 49) == 3
    assert candidate(arr1 = [500, 500, 500, 500, 500],arr2 = [500, 500, 500, 500, 500],d = 0) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [1, 2, 3, 4, 5],d = 5) == 4
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [10, 20, 30, 40, 50],d = 10) == 0
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 4, 6, 8, 10],d = 1) == 0
    assert candidate(arr1 = [500, 1000, 1500, 2000],arr2 = [400, 900, 1400, 1900],d = 100) == 0
    assert candidate(arr1 = [0, 100, 200, 300, 400],arr2 = [50, 150, 250, 350, 450],d = 50) == 0
    assert candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [50, 150, 250, 350, 450],d = 49) == 5
    assert candidate(arr1 = [0, 5, 10, 15, 20],arr2 = [3, 6, 9, 12, 18],d = 2) == 2
    assert candidate(arr1 = [500, 400, 300, 200, 100],arr2 = [0, 100, 200, 300, 400, 500],d = 99) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45, 55],d = 9) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45, 55],d = 4) == 5
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10],d = 0) == 5
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],d = 1) == 0
    assert candidate(arr1 = [0, 0, 0, 0],arr2 = [1, -1, 2, -2],d = 1) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9, 10],d = 0) == 5
    assert candidate(arr1 = [-100, -200, -300, -400, -500],arr2 = [100, 200, 300, 400, 500],d = 150) == 5
    assert candidate(arr1 = [-10, -20, -30],arr2 = [10, 20, 30],d = 19) == 3
    assert candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [90, 190, 290, 390, 490],d = 9) == 5
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 3, 5, 7, 9],d = 0) == 2
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],d = 0) == 5
    assert candidate(arr1 = [5, 5, 5, 5, 5],arr2 = [1, 2, 3, 4, 6],d = 1) == 0
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [0, 2, 4, 6, 8],d = 0) == 5
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],d = 3) == 3
    assert candidate(arr1 = [-10, -20, -30, -40],arr2 = [-11, -21, -31, -41],d = 0) == 4
    assert candidate(arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [5],d = 1) == 7
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],d = 0) == 1
    assert candidate(arr1 = [0, 0, 0, 0, 0],arr2 = [1, 2, 3, 4, 5],d = 0) == 5
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 2, 2, 2, 2],d = 0) == 5
    assert candidate(arr1 = [2, 4, 6, 8, 10],arr2 = [1, 3, 5, 7, 9],d = 1) == 0
    assert candidate(arr1 = [1000, -1000, 500, -500],arr2 = [1000, -1000, 500, -500],d = 0) == 0
    assert candidate(arr1 = [5, 10, 15, 20, 25],arr2 = [3, 6, 9, 12, 18],d = 2) == 2
    assert candidate(arr1 = [5, 15, 25, 35, 45],arr2 = [0, 10, 20, 30, 40],d = 4) == 5
    assert candidate(arr1 = [-1000, -500, 0, 500, 1000],arr2 = [-500, 0, 500],d = 499) == 2
    assert candidate(arr1 = [-1000, 1000, 500, -500],arr2 = [0, -2000, 2000, 1000],d = 500) == 1
    assert candidate(arr1 = [500, 400, 300, 200, 100],arr2 = [-100, -200, -300, -400, -500],d = 100) == 5
    assert candidate(arr1 = [100, 200, 300, 400],arr2 = [50, 150, 250, 350],d = 49) == 4
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],d = 8) == 1
    assert candidate(arr1 = [-500, -1000, -1500, -2000],arr2 = [-400, -900, -1400, -1900],d = 100) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [0, 0, 0, 0, 0],d = 1) == 4
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45, 55],d = 5) == 0
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10],d = 0) == 5
    assert candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [150, 250, 350, 450],d = 49) == 5
    assert candidate(arr1 = [0, 1, 2, 3, 4],arr2 = [0, 0, 0, 0, 0],d = 2) == 2
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],arr2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],d = 5) == 4
    assert candidate(arr1 = [0, 0, 0, 0],arr2 = [1, 2, 3, 4],d = 0) == 4
    assert candidate(arr1 = [-5, -10, -15, -20, -25],arr2 = [5, 10, 15, 20, 25],d = 4) == 5
    assert candidate(arr1 = [50, 51, 52, 53, 54, 55],arr2 = [50, 55],d = 0) == 4
    assert candidate(arr1 = [1, 1, 1, 1],arr2 = [2, 2, 2, 2],d = 1) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45],d = 5) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5],d = 1) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],d = 9) == 0
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [0, 2, 4, 6, 8],d = 1) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45],d = 4) == 5
    assert candidate(arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18],d = 0) == 5
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [10, 20, 30, 40, 50],d = 5) == 4
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5],d = 10) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [1, 2, 3, 4, 5],d = 0) == 0
    assert candidate(arr1 = [0, 0, 0, 0, 0],arr2 = [-1, -2, -3, -4, -5],d = 1) == 0
    assert candidate(arr1 = [100, 200, 300],arr2 = [95, 195, 295, 105, 205, 305],d = 5) == 0
    assert candidate(arr1 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],arr2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],d = 2) == 0
    assert candidate(arr1 = [-100, -90, -80, -70, -60, -50],arr2 = [-95, -85, -75, -65, -55],d = 4) == 6
    assert candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],d = 9) == 0
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [1, 1, 1, 1, 1],d = 1) == 0
    assert candidate(arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],d = 1) == 7
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [1, 2, 3, 4, 5],d = 0) == 0
    assert candidate(arr1 = [1000, -1000, 0],arr2 = [500, -500, 0],d = 500) == 0
    assert candidate(arr1 = [0, 10, 20, 30, 40],arr2 = [5, 15, 25, 35, 45],d = 5) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],d = 8) == 9
    assert candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],d = 0) == 10
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [10, 20, 30, 40, 50],d = 9) == 0
    assert candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15],arr2 = [2, 4, 6, 8, 10, 12, 14, 16],d = 1) == 0
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [5, 15, 25, 35, 45],d = 6) == 0
    assert candidate(arr1 = [0, 100, 200],arr2 = [50, 150, 250],d = 49) == 3
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [-1, -2, -3, -4, -5],d = 1) == 5
    assert candidate(arr1 = [1, 1, 1, 1],arr2 = [1],d = 1) == 0
    assert candidate(arr1 = [-50, -40, -30, -20, -10],arr2 = [-45, -35, -25, -15, -5],d = 4) == 5
    assert candidate(arr1 = [-10, -20, -30, -40, -50],arr2 = [-5, -15, -25, -35, -45, -55],d = 9) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [2, 4, 6, 8, 10],d = 1) == 0
    assert candidate(arr1 = [0, 0, 0, 0],arr2 = [0, 0, 0, 0],d = 0) == 0
    assert candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [50, 150, 250, 350, 450, 550],d = 49) == 5
    assert candidate(arr1 = [-100, -200, -300, -400, -500],arr2 = [-95, -195, -295, -395, -495, -595],d = 5) == 0
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 2, 2, 2, 2],d = 1) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [0, 6, 7, 8, 9],d = 1) == 3
    assert candidate(arr1 = [100, 200, 300, 400, 500],arr2 = [90, 190, 290, 390, 490],d = 5) == 5
    assert candidate(arr1 = [1, 10, 100, 1000],arr2 = [-1, -10, -100, -1000],d = 5) == 3
    assert candidate(arr1 = [100, 200, 300, 400],arr2 = [99, 199, 299, 399],d = 1) == 0
    assert candidate(arr1 = [1, 3, 5, 7, 9],arr2 = [2, 4, 6, 8, 10],d = 1) == 0
    assert candidate(arr1 = [-100, -200, -300, -400],arr2 = [-50, -150, -250, -350],d = 49) == 4
    assert candidate(arr1 = [5, 15, 25, 35],arr2 = [10, 20, 30, 40],d = 5) == 0
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9, 10],d = 1) == 4
    assert candidate(arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],arr2 = [1, 3, 5, 7, 9],d = 0) == 5
    assert candidate(arr1 = [1, 1, 1, 1, 1],arr2 = [2, 3, 4, 5, 6],d = 0) == 5
    assert candidate(arr1 = [1, 3, 5, 7, 9, 11, 13, 15],arr2 = [2, 4, 6, 8, 10, 12, 14, 16],d = 0) == 8
    assert candidate(arr1 = [-50, -40, -30, -20, -10],arr2 = [-60, -55, -45, -35, -25],d = 5) == 1
    assert candidate(arr1 = [10, 20, 30, 40, 50],arr2 = [15, 25, 35, 45, 55],d = 4) == 5
    assert candidate(arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],arr2 = [1, 11, 21, 31, 41, 51, 61, 71, 81],d = 9) == 0
    assert candidate(arr1 = [-100, -200, -300, -400, -500],arr2 = [-50, -150, -250, -350, -450],d = 49) == 5
    assert candidate(arr1 = [500, 400, 300, 200, 100],arr2 = [550, 450, 350, 250, 150],d = 49) == 5
    assert candidate(arr1 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],arr2 = [-5, 0, 5],d = 2) == 3
    assert candidate(arr1 = [1, 2, 3, 4, 5],arr2 = [6, 7, 8, 9, 10],d = 4) == 1
    assert candidate(arr1 = [-50, -25, 0, 25, 50],arr2 = [-30, -15, 15, 30],d = 14) == 3
