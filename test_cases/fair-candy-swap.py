# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(aliceSizes = [3, 7],bobSizes = [1, 9]) == None
    assert candidate(aliceSizes = [10, 20, 30],bobSizes = [5, 15, 25]) == None
    assert candidate(aliceSizes = [1, 1],bobSizes = [2, 2]) == [1, 2]
    assert candidate(aliceSizes = [5, 4, 3],bobSizes = [7, 8, 9]) == [3, 9]
    assert candidate(aliceSizes = [4, 1, 2, 1],bobSizes = [1, 2, 2, 10]) == None
    assert candidate(aliceSizes = [1, 3, 5, 7],bobSizes = [2, 4, 6, 8]) == None
    assert candidate(aliceSizes = [1, 2, 5],bobSizes = [2, 4]) == [5, 4]
    assert candidate(aliceSizes = [35, 17, 4, 24, 19],bobSizes = [68, 32, 20, 92, 21]) == None
    assert candidate(aliceSizes = [1, 2],bobSizes = [2, 3]) == [1, 2]
    assert candidate(aliceSizes = [3, 4],bobSizes = [2, 5]) == None
    assert candidate(aliceSizes = [2],bobSizes = [1, 3]) == [2, 3]
    assert candidate(aliceSizes = [35, 17, 4, 24, 10],bobSizes = [66, 56, 5, 1, 58]) == [10, 58]
    assert candidate(aliceSizes = [4, 1, 2, 1],bobSizes = [1, 2, 2, 3]) == [1, 1]
    assert candidate(aliceSizes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == None
    assert candidate(aliceSizes = [1, 3, 5, 7, 9, 11, 13, 15],bobSizes = [2, 4, 6, 8, 10, 12, 14, 16]) == None
    assert candidate(aliceSizes = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],bobSizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [5, 30]
    assert candidate(aliceSizes = [10000, 20000, 30000, 40000],bobSizes = [5000, 15000, 25000, 35000]) == None
    assert candidate(aliceSizes = [12345, 67890, 54321, 98765],bobSizes = [23456, 78901, 1234, 5678]) == None
    assert candidate(aliceSizes = [55555, 44444, 33333, 22222, 11111],bobSizes = [99999, 88888, 77777, 66666, 55555]) == None
    assert candidate(aliceSizes = [100, 200, 300, 400, 500],bobSizes = [90, 190, 290, 390, 490]) == None
    assert candidate(aliceSizes = [100, 200, 300, 400],bobSizes = [150, 250, 350, 450]) == None
    assert candidate(aliceSizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],bobSizes = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115]) == None
    assert candidate(aliceSizes = [5, 20, 10, 30],bobSizes = [15, 25, 35, 5]) == None
    assert candidate(aliceSizes = [2, 4, 6, 8, 10, 12],bobSizes = [1, 3, 5, 7, 9, 11, 13]) == None
    assert candidate(aliceSizes = [100, 200, 300, 400],bobSizes = [150, 250, 350, 450, 550]) == None
    assert candidate(aliceSizes = [50000, 25000, 12500, 6250, 3125],bobSizes = [45000, 22500, 11250, 5625, 2812]) == None
    assert candidate(aliceSizes = [100, 200, 300, 400],bobSizes = [50, 150, 250, 350]) == None
    assert candidate(aliceSizes = [101, 202, 303, 404, 505, 606, 707, 808, 909],bobSizes = [99, 198, 297, 396, 495, 594, 693, 792, 891]) == None
    assert candidate(aliceSizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],bobSizes = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]) == None
    assert candidate(aliceSizes = [100000, 50000, 25000, 12500, 6250],bobSizes = [105000, 55000, 27500, 13750, 6875]) == None
    assert candidate(aliceSizes = [100000, 1, 2, 3],bobSizes = [99999, 4, 5, 6]) == [1, 5]
    assert candidate(aliceSizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],bobSizes = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == [300, 50]
    assert candidate(aliceSizes = [9, 18, 27, 36, 45],bobSizes = [12, 24, 36, 48, 60]) == None
    assert candidate(aliceSizes = [100, 200, 300, 400, 500],bobSizes = [50, 150, 250, 350, 450]) == None
    assert candidate(aliceSizes = [9, 18, 27, 36, 45],bobSizes = [10, 20, 30, 40, 50]) == None
    assert candidate(aliceSizes = [99, 198, 297, 396, 495],bobSizes = [100, 200, 300, 400, 500]) == None
    assert candidate(aliceSizes = [100, 200, 300, 400, 500, 600, 700],bobSizes = [75, 175, 275, 375, 475, 575, 675]) == None
    assert candidate(aliceSizes = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],bobSizes = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40]) == None
    assert candidate(aliceSizes = [10, 20, 30, 40, 50],bobSizes = [5, 15, 25, 35, 45]) == None
    assert candidate(aliceSizes = [1000, 2000, 3000, 4000, 5000],bobSizes = [1500, 2500, 3500, 4500, 5500]) == None
    assert candidate(aliceSizes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],bobSizes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == [8, 1]
    assert candidate(aliceSizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000],bobSizes = [5000, 15000, 25000, 35000, 45000, 55000, 65000, 75000, 85000]) == None
    assert candidate(aliceSizes = [100, 200, 300, 400, 500, 600, 700, 800],bobSizes = [150, 250, 350, 450, 550, 650, 750, 850, 950]) == None
    assert candidate(aliceSizes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],bobSizes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [1, 6]
    assert candidate(aliceSizes = [99999, 88888, 77777, 66666, 55555],bobSizes = [11111, 22222, 33333, 44444, 66666, 77777, 88888]) == [99999, 77777]
    assert candidate(aliceSizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],bobSizes = [1500, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10500]) == [1000, 3500]
    assert candidate(aliceSizes = [101, 203, 305, 407, 509],bobSizes = [102, 204, 306, 408, 510]) == None
    assert candidate(aliceSizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bobSizes = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == None
    assert candidate(aliceSizes = [10, 20, 30, 40],bobSizes = [5, 15, 25, 35, 45, 55]) == None
    assert candidate(aliceSizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobSizes = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == None
    assert candidate(aliceSizes = [1, 5, 9, 13, 17, 21],bobSizes = [2, 6, 10, 14, 18, 22]) == None
    assert candidate(aliceSizes = [50, 51, 52, 53, 54, 55, 56],bobSizes = [49, 50, 51, 52, 53, 54, 55]) == [52, 49]
    assert candidate(aliceSizes = [88, 44, 22, 11, 55, 33, 66, 99, 77],bobSizes = [132, 66, 33, 22, 110, 44, 88, 11, 77]) == [88, 132]
    assert candidate(aliceSizes = [23456, 78901, 34567, 89012],bobSizes = [65432, 12345, 54321, 98765]) == None
    assert candidate(aliceSizes = [10000, 20000, 30000, 40000, 50000, 60000],bobSizes = [15000, 25000, 35000, 45000, 55000, 65000]) == [10000, 25000]
    assert candidate(aliceSizes = [1000, 2000, 3000, 4000, 5000],bobSizes = [5500, 6500, 7500, 8500]) == [1000, 7500]
    assert candidate(aliceSizes = [500, 600, 700, 800, 900],bobSizes = [100, 200, 300, 400, 1400]) == None
    assert candidate(aliceSizes = [99, 199, 299, 399, 499, 599, 699, 799, 899, 999],bobSizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == None
    assert candidate(aliceSizes = [3, 5, 7, 9, 11, 13, 15, 17, 19],bobSizes = [4, 6, 8, 10, 12, 14, 16, 18, 20]) == [3, 8]
    assert candidate(aliceSizes = [12345, 6789, 2468, 1357, 9753],bobSizes = [8642, 7531, 9513, 5791, 6842]) == None
    assert candidate(aliceSizes = [23, 45, 67, 89, 101, 123, 145],bobSizes = [34, 56, 78, 90, 112, 134, 156]) == None
    assert candidate(aliceSizes = [100000, 100000, 100000, 100000, 100000],bobSizes = [50000, 50000, 50000, 50000, 50000, 50000, 50000]) == None
    assert candidate(aliceSizes = [50, 100, 150, 200, 250, 300],bobSizes = [60, 110, 160, 210, 260, 310]) == None
    assert candidate(aliceSizes = [10000, 20000, 30000, 40000],bobSizes = [5000, 6000, 7000, 8000]) == None
    assert candidate(aliceSizes = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9],bobSizes = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]) == None
    assert candidate(aliceSizes = [10000, 20000, 30000, 40000, 50000],bobSizes = [5000, 15000, 25000, 35000, 45000, 55000]) == [10000, 25000]
    assert candidate(aliceSizes = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],bobSizes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [17, 2]
    assert candidate(aliceSizes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == None
    assert candidate(aliceSizes = [1000, 2000, 3000, 4000],bobSizes = [500, 1500, 2500, 3500]) == None
    assert candidate(aliceSizes = [1000, 2000, 3000, 4000, 5000],bobSizes = [1100, 2100, 3100, 4100, 5100]) == None
    assert candidate(aliceSizes = [1, 3, 5, 7, 9, 11],bobSizes = [2, 4, 6, 8, 10, 12]) == [1, 4]
    assert candidate(aliceSizes = [1, 1, 1, 1, 10000],bobSizes = [5000, 5000, 5000, 5000, 5000]) == None
    assert candidate(aliceSizes = [99990, 1, 2, 3, 4, 5],bobSizes = [100000, 6, 7, 8, 9, 10]) == None
    assert candidate(aliceSizes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000],bobSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == None
    assert candidate(aliceSizes = [10000, 20000, 30000],bobSizes = [15000, 25000, 35000]) == None
    assert candidate(aliceSizes = [7, 2, 5, 3, 8, 1, 4, 6, 9, 10],bobSizes = [12, 15, 14, 11, 13, 10, 9, 8, 7, 6]) == None
    assert candidate(aliceSizes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],bobSizes = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [1, 6]
    assert candidate(aliceSizes = [50000, 10000, 30000, 20000, 40000],bobSizes = [15000, 25000, 35000, 45000, 55000]) == None
    assert candidate(aliceSizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],bobSizes = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150]) == None
    assert candidate(aliceSizes = [100, 200, 300],bobSizes = [50, 100, 150, 200, 250, 300]) == None
    assert candidate(aliceSizes = [5, 10, 15, 20, 25, 30, 35],bobSizes = [7, 14, 21, 28, 35, 42, 49]) == None
    assert candidate(aliceSizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000],bobSizes = [500, 1500, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 10500, 11500, 12500, 13500]) == [4000, 500]
    assert candidate(aliceSizes = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],bobSizes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == None
    assert candidate(aliceSizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobSizes = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [30, 5]
    assert candidate(aliceSizes = [1000, 2000, 3000, 4000],bobSizes = [1500, 2500, 3500, 500]) == None
    assert candidate(aliceSizes = [100000, 200000, 300000, 400000, 500000],bobSizes = [50000, 150000, 250000, 350000, 450000]) == None
    assert candidate(aliceSizes = [1000, 2000, 3000, 4000, 5000],bobSizes = [500, 1500, 2500, 3500, 4500]) == None
    assert candidate(aliceSizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],bobSizes = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == None
    assert candidate(aliceSizes = [10, 20, 30, 40, 50],bobSizes = [5, 15, 25, 35, 45]) == None
    assert candidate(aliceSizes = [15, 25, 35, 45, 55, 65],bobSizes = [14, 24, 34, 44, 54, 64]) == None
    assert candidate(aliceSizes = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],bobSizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == None
    assert candidate(aliceSizes = [10, 20, 30, 40, 50],bobSizes = [15, 25, 35, 45, 55]) == None
    assert candidate(aliceSizes = [1, 10, 100, 1000, 10000],bobSizes = [2, 20, 200, 2000, 20000]) == None
