# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums1 = [10],nums2 = [5]) == -5
    assert candidate(nums1 = [100, 200, 300],nums2 = [150, 250, 350]) == 50
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == 5
    assert candidate(nums1 = [7, 7, 7],nums2 = [10, 10, 10]) == 3
    assert candidate(nums1 = [50, 50, 50, 50],nums2 = [55, 55, 55, 55]) == 5
    assert candidate(nums1 = [1000, 0, 500],nums2 = [900, 1000, 400]) == 400
    assert candidate(nums1 = [500, 500, 500],nums2 = [500, 500, 500]) == 0
    assert candidate(nums1 = [5, 10, 15],nums2 = [8, 13, 18]) == 3
    assert candidate(nums1 = [0, 0, 0],nums2 = [3, 3, 3]) == 3
    assert candidate(nums1 = [2, 6, 4],nums2 = [9, 7, 5]) == 3
    assert candidate(nums1 = [999, 999, 999],nums2 = [1000, 1000, 1000]) == 1
    assert candidate(nums1 = [500, 500, 500],nums2 = [400, 400, 400]) == -100
    assert candidate(nums1 = [1000, 0, 500],nums2 = [900, 100, 400]) == 100
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 3
    assert candidate(nums1 = [999, 999, 999, 999],nums2 = [899, 899, 899, 899]) == -100
    assert candidate(nums1 = [999, 999, 999, 999],nums2 = [994, 994, 994, 994]) == -5
    assert candidate(nums1 = [500, 500, 500, 500, 500],nums2 = [450, 450, 450, 450, 450]) == -50
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [7, 9, 11, 13, 15]) == 5
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0],nums2 = [7, 7, 7, 7, 7, 7, 7]) == 7
    assert candidate(nums1 = [999, 998, 997, 996, 995],nums2 = [994, 993, 992, 991, 990]) == -5
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [20, 30, 40, 50, 60]) == 10
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900],nums2 = [90, 190, 290, 390, 490, 590, 690, 790, 890]) == -10
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [15, 25, 35, 45, 55, 65]) == 5
    assert candidate(nums1 = [500, 500, 500, 500, 500],nums2 = [0, 0, 0, 0, 0]) == -500
    assert candidate(nums1 = [123, 456, 789],nums2 = [126, 459, 792]) == 3
    assert candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [5, 15, 25, 35, 45]) == 0
    assert candidate(nums1 = [500, 600, 700, 800, 900],nums2 = [450, 550, 650, 750, 850]) == -50
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 11, 21, 31, 41]) == -9
    assert candidate(nums1 = [999, 998, 997, 996],nums2 = [900, 899, 898, 897]) == -99
    assert candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [12, 19, 26, 33, 40]) == 5
    assert candidate(nums1 = [100, 100, 100, 100],nums2 = [200, 200, 200, 200]) == 100
    assert candidate(nums1 = [990, 980, 970, 960, 950],nums2 = [1000, 990, 980, 970, 960]) == 10
    assert candidate(nums1 = [50, 25, 12, 6, 3, 1],nums2 = [100, 75, 62, 56, 53, 51]) == 50
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [10, 15, 20, 25, 30, 35]) == 5
    assert candidate(nums1 = [123, 456, 789],nums2 = [128, 461, 794]) == 5
    assert candidate(nums1 = [800, 700, 600, 500, 400, 300],nums2 = [900, 800, 700, 600, 500, 400]) == 100
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14],nums2 = [7, 9, 11, 13, 15, 17, 19]) == 5
    assert candidate(nums1 = [999, 998, 997, 996],nums2 = [994, 993, 992, 991]) == -5
    assert candidate(nums1 = [250, 350, 450, 550, 650],nums2 = [245, 345, 445, 545, 645]) == -5
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [0, 5, 10, 15, 20, 25]) == -5
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(nums1 = [999, 998, 997, 996, 995],nums2 = [1000, 999, 998, 997, 996]) == 1
    assert candidate(nums1 = [300, 300, 300, 300, 300, 300],nums2 = [200, 200, 200, 200, 200, 200]) == -100
    assert candidate(nums1 = [7, 7, 7, 7, 7, 7],nums2 = [12, 12, 12, 12, 12, 12]) == 5
    assert candidate(nums1 = [123, 456, 789],nums2 = [130, 463, 796]) == 7
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [0, 0, 0, 0, 0]) == -5
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [50, 150, 250, 350]) == -50
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [200, 300, 400, 500, 600]) == 100
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 150, 250, 350, 450]) == -50
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 10
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == -50
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [6, 8, 10, 12, 14]) == 5
    assert candidate(nums1 = [450, 440, 430],nums2 = [400, 390, 380]) == -50
    assert candidate(nums1 = [0, 2, 4, 6, 8, 10],nums2 = [100, 102, 104, 106, 108, 110]) == 100
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == -5
    assert candidate(nums1 = [1000, 500, 250, 125, 62, 31, 15],nums2 = [1005, 505, 255, 130, 67, 36, 20]) == 5
    assert candidate(nums1 = [100, 200, 300],nums2 = [50, 150, 250]) == -50
    assert candidate(nums1 = [0, 100, 200, 300, 400],nums2 = [1, 101, 201, 301, 401]) == 1
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [101, 101, 102, 102, 103, 103]) == 100
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 1
    assert candidate(nums1 = [999, 998, 997, 996],nums2 = [996, 995, 994, 993]) == -3
    assert candidate(nums1 = [50, 100, 150, 200, 250],nums2 = [40, 90, 140, 190, 240]) == -10
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900],nums2 = [105, 205, 305, 405, 505, 605, 705, 805, 905]) == 5
    assert candidate(nums1 = [50, 100, 150, 200, 250, 300],nums2 = [50, 100, 150, 200, 250, 300]) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [0, 10, 20, 30, 40]) == -10
    assert candidate(nums1 = [50, 150, 250, 350, 450, 550],nums2 = [100, 200, 300, 400, 500, 600]) == 50
    assert candidate(nums1 = [50, 100, 150, 200, 250],nums2 = [45, 95, 145, 195, 245]) == -5
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [101, 101, 101, 101, 101]) == 100
    assert candidate(nums1 = [500, 400, 300, 200, 100],nums2 = [510, 410, 310, 210, 110]) == 10
    assert candidate(nums1 = [250, 500, 750, 1000],nums2 = [300, 550, 800, 1050]) == 50
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5],nums2 = [5, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums1 = [200, 400, 600, 800, 1000],nums2 = [150, 350, 550, 750, 950]) == -50
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 5
    assert candidate(nums1 = [999, 998, 997, 996, 995, 994, 993],nums2 = [1000, 999, 998, 997, 996, 995, 994]) == 1
    assert candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [0, 5, 10, 15, 20]) == -5
    assert candidate(nums1 = [5, 15, 25, 35, 45, 55, 65],nums2 = [-5, 5, 15, 25, 35, 45, 55]) == -10
    assert candidate(nums1 = [250, 250, 250, 250],nums2 = [300, 300, 300, 300]) == 50
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 105]) == 5
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [90, 190, 290, 390, 490]) == -10
    assert candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [0, 7, 14, 21, 28]) == -7
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [150, 250, 350, 450, 550]) == 50
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == 5
    assert candidate(nums1 = [250, 300, 350, 400, 450, 500],nums2 = [200, 250, 300, 350, 400, 450]) == -50
    assert candidate(nums1 = [123, 456, 789],nums2 = [223, 556, 889]) == 100
    assert candidate(nums1 = [999, 998, 997, 996],nums2 = [1000, 999, 998, 997]) == 1
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [6, 6, 7, 7, 8, 8]) == 5
    assert candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [15, 20, 25, 30, 35]) == 10
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [11, 12, 13, 14, 15]) == 10
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [15, 25, 35, 45, 55]) == 5
    assert candidate(nums1 = [500, 400, 300, 200, 100],nums2 = [400, 300, 200, 100, 0]) == -100
    assert candidate(nums1 = [250, 300, 350, 400],nums2 = [300, 350, 400, 450]) == 50
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10]) == 9
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [4, 4, 5, 5, 6, 6]) == 3
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [95, 195, 295, 395, 495, 595]) == -5
    assert candidate(nums1 = [0, 100, 200, 300, 400],nums2 = [100, 200, 300, 400, 500]) == 100
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 5
    assert candidate(nums1 = [999, 888, 777, 666, 555],nums2 = [1000, 889, 778, 667, 556]) == 1
