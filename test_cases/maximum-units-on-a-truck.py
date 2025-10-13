# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(boxTypes = [[1, 3], [2, 2], [3, 1]],truckSize = 4) == 8
    assert candidate(boxTypes = [[1, 1], [2, 2], [3, 3], [4, 4]],truckSize = 1) == 4
    assert candidate(boxTypes = [[2, 1], [4, 4], [3, 3]],truckSize = 5) == 19
    assert candidate(boxTypes = [[10, 1], [20, 2], [30, 3]],truckSize = 50) == 130
    assert candidate(boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]],truckSize = 10) == 91
    assert candidate(boxTypes = [[1, 100], [2, 99], [3, 98], [4, 97]],truckSize = 10) == 980
    assert candidate(boxTypes = [[10, 1], [5, 2], [3, 3]],truckSize = 10) == 21
    assert candidate(boxTypes = [[100, 1], [99, 2], [98, 3], [97, 4]],truckSize = 200) == 692
    assert candidate(boxTypes = [[10, 1]],truckSize = 10) == 10
    assert candidate(boxTypes = [[1, 1000], [1000, 1]],truckSize = 500) == 1499
    assert candidate(boxTypes = [[1, 100], [2, 90], [3, 80], [4, 70], [5, 60]],truckSize = 10) == 800
    assert candidate(boxTypes = [[5, 5], [5, 5], [5, 5], [5, 5]],truckSize = 15) == 75
    assert candidate(boxTypes = [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5]],truckSize = 15) == 62
    assert candidate(boxTypes = [[2, 1000], [1, 900], [2, 800], [1, 700], [2, 600], [1, 500], [2, 400], [1, 300], [2, 200], [1, 100]],truckSize = 10) == 7300
    assert candidate(boxTypes = [[9, 1], [8, 2], [7, 3], [6, 4], [5, 5], [4, 6], [3, 7], [2, 8], [1, 9]],truckSize = 20) == 115
    assert candidate(boxTypes = [[5, 10], [1, 15], [3, 12], [2, 14], [4, 8]],truckSize = 15) == 161
    assert candidate(boxTypes = [[7, 10], [5, 3], [2, 6], [8, 1]],truckSize = 20) == 103
    assert candidate(boxTypes = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],truckSize = 15) == 35
    assert candidate(boxTypes = [[5, 10], [4, 20], [3, 30], [2, 40], [1, 50]],truckSize = 15) == 350
    assert candidate(boxTypes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],truckSize = 5) == 40
    assert candidate(boxTypes = [[9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],truckSize = 30) == 174
    assert candidate(boxTypes = [[999, 1], [1, 999], [500, 500], [250, 250], [125, 125]],truckSize = 1000) == 329248
    assert candidate(boxTypes = [[1, 5], [2, 3], [3, 2], [4, 1]],truckSize = 10) == 21
    assert candidate(boxTypes = [[50, 10], [100, 9], [150, 8], [200, 7], [250, 6], [300, 5]],truckSize = 800) == 5750
    assert candidate(boxTypes = [[50, 5], [30, 6], [20, 7]],truckSize = 100) == 570
    assert candidate(boxTypes = [[3, 100], [2, 200], [1, 300], [5, 400]],truckSize = 5) == 2000
    assert candidate(boxTypes = [[20, 5], [15, 10], [10, 15], [5, 20], [1, 25]],truckSize = 35) == 445
    assert candidate(boxTypes = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]],truckSize = 20) == 18900
    assert candidate(boxTypes = [[10, 10], [10, 20], [10, 30], [10, 40], [10, 50]],truckSize = 40) == 1400
    assert candidate(boxTypes = [[50, 10], [30, 20], [20, 30], [10, 40], [5, 50]],truckSize = 120) == 2350
    assert candidate(boxTypes = [[200, 1], [100, 2], [150, 3], [50, 4], [250, 5]],truckSize = 500) == 2000
    assert candidate(boxTypes = [[100, 1], [50, 2], [25, 3], [10, 4], [5, 5], [1, 6]],truckSize = 150) == 305
    assert candidate(boxTypes = [[20, 25], [15, 30], [10, 35], [5, 40]],truckSize = 50) == 1500
    assert candidate(boxTypes = [[10, 10], [5, 7], [15, 5], [20, 3]],truckSize = 25) == 185
    assert candidate(boxTypes = [[50, 10], [30, 20], [20, 30], [10, 40]],truckSize = 100) == 2000
    assert candidate(boxTypes = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],truckSize = 150) == 5500
    assert candidate(boxTypes = [[1, 900], [2, 800], [3, 700], [4, 600], [5, 500], [6, 400], [7, 300], [8, 200], [9, 100]],truckSize = 15) == 9500
    assert candidate(boxTypes = [[1, 999], [2, 998], [3, 997], [4, 996], [5, 995], [6, 994], [7, 993], [8, 992], [9, 991], [10, 990]],truckSize = 20) == 19915
    assert candidate(boxTypes = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],truckSize = 55) == 220
    assert candidate(boxTypes = [[30, 20], [20, 15], [10, 10], [40, 5], [50, 2]],truckSize = 100) == 1200
    assert candidate(boxTypes = [[10, 30], [20, 20], [30, 10], [40, 5], [50, 1]],truckSize = 60) == 1000
    assert candidate(boxTypes = [[50, 10], [40, 20], [30, 30], [20, 40], [10, 50]],truckSize = 120) == 3200
    assert candidate(boxTypes = [[500, 1000], [400, 900], [300, 800], [200, 700], [100, 600]],truckSize = 1200) == 1100000
    assert candidate(boxTypes = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],truckSize = 150) == 1450
    assert candidate(boxTypes = [[100, 10], [200, 9], [150, 8], [50, 7], [25, 6]],truckSize = 300) == 2800
    assert candidate(boxTypes = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],truckSize = 50) == 215
    assert candidate(boxTypes = [[500, 100], [300, 200], [200, 300], [100, 400]],truckSize = 800) == 180000
    assert candidate(boxTypes = [[50, 100], [25, 200], [75, 50], [100, 250]],truckSize = 200) == 36250
    assert candidate(boxTypes = [[1, 999], [999, 1]],truckSize = 1000) == 1998
    assert candidate(boxTypes = [[7, 9], [7, 8], [7, 7], [7, 6], [7, 5], [7, 4], [7, 3], [7, 2], [7, 1]],truckSize = 20) == 161
    assert candidate(boxTypes = [[3, 8], [5, 7], [2, 9], [6, 10], [4, 5]],truckSize = 15) == 130
    assert candidate(boxTypes = [[5, 10], [4, 20], [3, 30], [2, 40], [1, 50], [1, 60], [1, 70], [1, 80], [1, 90], [1, 100]],truckSize = 20) == 750
    assert candidate(boxTypes = [[50, 20], [100, 15], [150, 10], [200, 5], [250, 1]],truckSize = 500) == 5000
    assert candidate(boxTypes = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996]],truckSize = 15) == 14960
    assert candidate(boxTypes = [[5, 10], [5, 20], [5, 30], [5, 40], [5, 50], [5, 60], [5, 70], [5, 80], [5, 90], [5, 100]],truckSize = 25) == 2000
    assert candidate(boxTypes = [[10, 1000], [9, 900], [8, 800], [7, 700], [6, 600], [5, 500], [4, 400], [3, 300], [2, 200], [1, 100]],truckSize = 25) == 22900
    assert candidate(boxTypes = [[100, 5], [200, 2], [50, 10], [150, 3]],truckSize = 350) == 1550
    assert candidate(boxTypes = [[50, 100], [40, 99], [30, 98], [20, 97], [10, 96], [5, 95]],truckSize = 160) == 15275
    assert candidate(boxTypes = [[1, 500], [1, 400], [1, 300], [1, 200], [1, 100]],truckSize = 2) == 900
    assert candidate(boxTypes = [[3, 9], [2, 8], [5, 7], [1, 6], [4, 5]],truckSize = 15) == 104
    assert candidate(boxTypes = [[10, 20], [20, 10], [30, 5], [40, 2], [50, 1]],truckSize = 100) == 630
    assert candidate(boxTypes = [[300, 1], [200, 2], [100, 3], [50, 4], [25, 5]],truckSize = 700) == 1325
    assert candidate(boxTypes = [[1, 1000], [2, 999], [3, 998], [4, 997], [5, 996]],truckSize = 15) == 14960
    assert candidate(boxTypes = [[5, 15], [10, 12], [20, 9], [30, 7], [40, 5], [50, 3]],truckSize = 150) == 920
    assert candidate(boxTypes = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],truckSize = 500) == 3740
    assert candidate(boxTypes = [[5, 15], [20, 3], [5, 20], [10, 7]],truckSize = 25) == 260
    assert candidate(boxTypes = [[100, 10], [50, 20], [20, 30], [10, 40]],truckSize = 200) == 3000
    assert candidate(boxTypes = [[100, 2], [200, 3], [300, 4], [400, 5], [500, 6]],truckSize = 1000) == 5400
    assert candidate(boxTypes = [[100, 1], [50, 2], [25, 3], [12, 4], [6, 5], [3, 6], [1, 7]],truckSize = 200) == 378
    assert candidate(boxTypes = [[50, 10], [40, 9], [30, 8], [20, 7], [10, 6], [5, 5], [1, 4]],truckSize = 160) == 1329
    assert candidate(boxTypes = [[100, 500], [50, 1000], [10, 2000]],truckSize = 200) == 120000
    assert candidate(boxTypes = [[10, 10], [9, 9], [8, 8], [7, 7], [6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],truckSize = 50) == 374
    assert candidate(boxTypes = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],truckSize = 500) == 37400
    assert candidate(boxTypes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],truckSize = 10) == 55
    assert candidate(boxTypes = [[1, 500], [2, 400], [3, 300], [4, 200], [5, 100]],truckSize = 10) == 3000
    assert candidate(boxTypes = [[30, 4], [10, 20], [15, 5]],truckSize = 50) == 375
    assert candidate(boxTypes = [[100, 10], [200, 9], [300, 8], [400, 7]],truckSize = 1000) == 8000
    assert candidate(boxTypes = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],truckSize = 1) == 50
    assert candidate(boxTypes = [[10, 100], [5, 200], [3, 300], [2, 400], [1, 500]],truckSize = 20) == 4100
    assert candidate(boxTypes = [[10, 5], [5, 10], [15, 3]],truckSize = 18) == 109
    assert candidate(boxTypes = [[10, 5], [20, 8], [30, 2], [5, 9]],truckSize = 40) == 265
    assert candidate(boxTypes = [[10, 10], [20, 9], [30, 8], [40, 7], [50, 6], [60, 5], [70, 4], [80, 3], [90, 2], [100, 1]],truckSize = 250) == 1560
    assert candidate(boxTypes = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5]],truckSize = 30) == 120
    assert candidate(boxTypes = [[1, 1000], [2, 900], [3, 800], [4, 700], [5, 600], [6, 500], [7, 400], [8, 300], [9, 200], [10, 100]],truckSize = 15) == 11000
    assert candidate(boxTypes = [[10, 100], [20, 200], [30, 300], [40, 400], [50, 500], [60, 600], [70, 700], [80, 800], [90, 900]],truckSize = 300) == 230000
    assert candidate(boxTypes = [[500, 500], [500, 500], [500, 500]],truckSize = 1000) == 500000
    assert candidate(boxTypes = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],truckSize = 1000) == 4400
    assert candidate(boxTypes = [[50, 20], [30, 15], [40, 10], [20, 5]],truckSize = 100) == 1650
    assert candidate(boxTypes = [[10, 5], [20, 3], [30, 4], [40, 2], [50, 1]],truckSize = 100) == 310
    assert candidate(boxTypes = [[10, 500], [20, 450], [30, 400], [40, 350], [50, 300], [60, 250], [70, 200], [80, 150], [90, 100], [100, 50]],truckSize = 200) == 67500
    assert candidate(boxTypes = [[3, 2], [2, 5], [6, 1], [10, 3]],truckSize = 12) == 40
    assert candidate(boxTypes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],truckSize = 30) == 266
    assert candidate(boxTypes = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [10, 6], [9, 7], [8, 8], [7, 9], [6, 10]],truckSize = 50) == 340
    assert candidate(boxTypes = [[100, 10], [200, 5], [300, 1]],truckSize = 500) == 2200
    assert candidate(boxTypes = [[1, 100], [10, 90], [100, 80], [1000, 70], [10000, 60]],truckSize = 5000) == 312340
    assert candidate(boxTypes = [[10, 5], [9, 4], [8, 3], [7, 2], [6, 1]],truckSize = 20) == 89
    assert candidate(boxTypes = [[100, 1], [100, 2], [100, 3], [100, 4], [100, 5]],truckSize = 250) == 1050
    assert candidate(boxTypes = [[50, 10], [50, 20], [50, 30], [50, 40], [50, 50]],truckSize = 150) == 6000
    assert candidate(boxTypes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],truckSize = 15) == 145
    assert candidate(boxTypes = [[50, 1], [200, 2], [100, 3], [30, 4], [10, 5]],truckSize = 250) == 690
    assert candidate(boxTypes = [[1, 1000], [1, 999], [1, 998], [1, 997], [1, 996], [1, 995], [1, 994], [1, 993], [1, 992], [1, 991]],truckSize = 10) == 9955
    assert candidate(boxTypes = [[10, 100], [20, 90], [30, 80], [40, 70], [50, 60]],truckSize = 200) == 11000
    assert candidate(boxTypes = [[100, 100], [90, 90], [80, 80], [70, 70], [60, 60], [50, 50]],truckSize = 500) == 35500
    assert candidate(boxTypes = [[20, 1], [20, 2], [20, 3], [20, 4], [20, 5], [20, 6], [20, 7], [20, 8], [20, 9], [20, 10]],truckSize = 100) == 800
