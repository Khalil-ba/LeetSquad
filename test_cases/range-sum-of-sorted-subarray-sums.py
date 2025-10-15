def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4],n = 4,left = 3,right = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4],n = 4,left = 3,right = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],n = 3,left = 1,right = 3) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],n = 3,left = 1,right = 3) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2],n = 3,left = 1,right = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2],n = 3,left = 1,right = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4],n = 4,left = 1,right = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4],n = 4,left = 1,right = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3],n = 4,left = 2,right = 8) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3],n = 4,left = 2,right = 8) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4],n = 4,left = 1,right = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4],n = 4,left = 1,right = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3],n = 3,left = 2,right = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3],n = 3,left = 2,right = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 1, 4],n = 4,left = 3,right = 7) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 1, 4],n = 4,left = 3,right = 7) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],n = 3,left = 2,right = 5) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],n = 3,left = 2,right = 5) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4],n = 3,left = 1,right = 6) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4],n = 3,left = 1,right = 6) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 3],n = 4,left = 2,right = 6) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 3],n = 4,left = 2,right = 6) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],n = 3,left = 1,right = 5) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],n = 3,left = 1,right = 5) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],n = 15,left = 60,right = 120) == 46215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],n = 15,left = 60,right = 120) == 46215: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 10,left = 25,right = 50) == 756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 10,left = 25,right = 50) == 756: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 20,right = 30) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 20,right = 30) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 10, 20, 25],n = 5,left = 1,right = 15) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 10, 20, 25],n = 5,left = 1,right = 15) == 520: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],n = 10,left = 25,right = 55) == 2334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],n = 10,left = 25,right = 55) == 2334: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 15,right = 45) == 6700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 15,right = 45) == 6700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 25,right = 75) == 10110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 25,right = 75) == 10110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],n = 5,left = 10,right = 20) == 6900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],n = 5,left = 10,right = 20) == 6900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 1,right = 100) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 1,right = 100) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],n = 5,left = 5,right = 15) == 960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],n = 5,left = 5,right = 15) == 960: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],n = 11,left = 15,right = 45) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],n = 11,left = 15,right = 45) == 460: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,left = 100,right = 200) == 11368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,left = 100,right = 200) == 11368: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],n = 15,left = 50,right = 100) == 5098
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],n = 15,left = 50,right = 100) == 5098: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 34, 45, 56, 67, 78, 89, 90, 100, 110],n = 10,left = 25,right = 60) == 12693
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 34, 45, 56, 67, 78, 89, 90, 100, 110],n = 10,left = 25,right = 60) == 12693: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],n = 9,left = 25,right = 35) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],n = 9,left = 25,right = 35) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],n = 5,left = 3,right = 12) == 610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],n = 5,left = 3,right = 12) == 610: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 10, 20],n = 4,left = 5,right = 12) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 10, 20],n = 4,left = 5,right = 12) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],n = 12,left = 30,right = 75) == 8471
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],n = 12,left = 30,right = 75) == 8471: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 25,right = 75) == 9910
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 25,right = 75) == 9910: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13],n = 7,left = 1,right = 28) == 588
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13],n = 7,left = 1,right = 28) == 588: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1],n = 5,left = 6,right = 16) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1],n = 5,left = 6,right = 16) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9],n = 5,left = 3,right = 7) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9],n = 5,left = 3,right = 7) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 1,right = 55) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 1,right = 55) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 7, 3, 8],n = 5,left = 3,right = 7) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 7, 3, 8],n = 5,left = 3,right = 7) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 10,left = 15,right = 40) == 497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 10,left = 15,right = 40) == 497: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],n = 10,left = 1,right = 100) == 1210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],n = 10,left = 1,right = 100) == 1210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 100, 98, 97, 96],n = 5,left = 10,right = 20) == 2158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 100, 98, 97, 96],n = 5,left = 10,right = 20) == 2158: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 15,left = 50,right = 150) == 9416
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 15,left = 50,right = 150) == 9416: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 53, 64, 75, 86, 97, 108, 119, 130, 141],n = 10,left = 15,right = 45) == 11216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 53, 64, 75, 86, 97, 108, 119, 130, 141],n = 10,left = 15,right = 45) == 11216: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 30,right = 70) == 9190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 30,right = 70) == 9190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 10,left = 30,right = 50) == 664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 10,left = 30,right = 50) == 664: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],n = 20,left = 150,right = 250) == 46005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],n = 20,left = 150,right = 250) == 46005: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],n = 11,left = 20,right = 40) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],n = 11,left = 20,right = 40) == 310: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],n = 10,left = 25,right = 50) == 7560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],n = 10,left = 25,right = 50) == 7560: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],n = 5,left = 1,right = 15) == 10500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],n = 5,left = 1,right = 15) == 10500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 10,right = 30) == 496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 10,right = 30) == 496: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 10,left = 50,right = 100) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 10,left = 50,right = 100) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5],n = 5,left = 1,right = 15) == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5],n = 5,left = 1,right = 15) == 245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54],n = 6,left = 10,right = 20) == 1260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54],n = 6,left = 10,right = 20) == 1260: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 15,right = 30) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 15,right = 30) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600],n = 6,left = 10,right = 30) == 16100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600],n = 6,left = 10,right = 30) == 16100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 10,left = 20,right = 40) == 44500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 10,left = 20,right = 40) == 44500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],n = 10,left = 50,right = 75) == 364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],n = 10,left = 50,right = 75) == 364: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 10,left = 30,right = 50) == 664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 10,left = 30,right = 50) == 664: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 8, 6, 2, 5, 4, 9, 1],n = 9,left = 20,right = 40) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 8, 6, 2, 5, 4, 9, 1],n = 9,left = 20,right = 40) == 480: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94],n = 6,left = 20,right = 30) == 1064
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94],n = 6,left = 20,right = 30) == 1064: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,left = 150,right = 250) == 9201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,left = 150,right = 250) == 9201: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],n = 10,left = 10,right = 30) == 5233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],n = 10,left = 10,right = 30) == 5233: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15,left = 50,right = 60) == 379
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15,left = 50,right = 60) == 379: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],n = 10,left = 20,right = 50) == 1036
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],n = 10,left = 20,right = 50) == 1036: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60],n = 6,left = 10,right = 20) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60],n = 6,left = 10,right = 20) == 1400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 25,right = 35) == 421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 25,right = 35) == 421: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],n = 5,left = 1,right = 25) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],n = 5,left = 1,right = 25) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 78, 12, 56, 90, 23, 45, 67, 89, 10],n = 10,left = 30,right = 60) == 8474
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 78, 12, 56, 90, 23, 45, 67, 89, 10],n = 10,left = 30,right = 60) == 8474: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60],n = 6,left = 10,right = 20) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60],n = 6,left = 10,right = 20) == 1400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],n = 11,left = 5,right = 20) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],n = 11,left = 5,right = 20) == 95: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 1,right = 100) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 1,right = 100) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 30,right = 40) == 2810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 30,right = 40) == 2810: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 10,left = 30,right = 45) == 908
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 10,left = 30,right = 45) == 908: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],n = 10,left = 55,right = 85) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],n = 10,left = 55,right = 85) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],n = 5,left = 10,right = 20) == 690
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],n = 5,left = 10,right = 20) == 690: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1],n = 5,left = 8,right = 12) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1],n = 5,left = 8,right = 12) == 68: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1],n = 7,left = 15,right = 25) == 179
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1],n = 7,left = 15,right = 25) == 179: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 15,left = 100,right = 200) == 2074
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 15,left = 100,right = 200) == 2074: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],n = 5,left = 1,right = 15) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],n = 5,left = 1,right = 15) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15,left = 50,right = 100) == 2715
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15,left = 50,right = 100) == 2715: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 45,right = 75) == 5010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 45,right = 75) == 5010: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 3, 5, 7, 2, 8],n = 6,left = 4,right = 12) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 3, 5, 7, 2, 8],n = 6,left = 4,right = 12) == 89: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 25,right = 50) == 133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 25,right = 50) == 133: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20],n = 20,left = 50,right = 150) == 6400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20],n = 20,left = 50,right = 150) == 6400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],n = 20,left = 100,right = 150) == 8103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],n = 20,left = 100,right = 150) == 8103: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45],n = 5,left = 7,right = 14) == 610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45],n = 5,left = 7,right = 14) == 610: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 20,left = 50,right = 100) == 232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 20,left = 50,right = 100) == 232: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],n = 5,left = 1,right = 15) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],n = 5,left = 1,right = 15) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],n = 10,left = 25,right = 50) == 410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],n = 10,left = 25,right = 50) == 410: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 55,right = 75) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 55,right = 75) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],n = 10,left = 5,right = 55) == 21600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],n = 10,left = 5,right = 55) == 21600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45],n = 5,left = 5,right = 15) == 810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45],n = 5,left = 5,right = 15) == 810: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],n = 15,left = 50,right = 100) == 5098
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],n = 15,left = 50,right = 100) == 5098: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 4, 2, 0, 8, 6, 4, 2, 0],n = 10,left = 20,right = 40) == 344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 4, 2, 0, 8, 6, 4, 2, 0],n = 10,left = 20,right = 40) == 344: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],n = 9,left = 10,right = 30) == 291
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],n = 9,left = 10,right = 30) == 291: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 25,right = 45) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 25,right = 45) == 97: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],n = 12,left = 50,right = 75) == 6660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],n = 12,left = 50,right = 75) == 6660: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65],n = 7,left = 15,right = 25) == 1585
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65],n = 7,left = 15,right = 25) == 1585: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 10, 20, 25],n = 5,left = 4,right = 10) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 10, 20, 25],n = 5,left = 4,right = 10) == 195: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 5, 2, 1],n = 8,left = 10,right = 35) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 5, 2, 1],n = 8,left = 10,right = 35) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100],n = 6,left = 20,right = 30) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100],n = 6,left = 20,right = 30) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 15,left = 50,right = 100) == 5430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 15,left = 50,right = 100) == 5430: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15,left = 100,right = 150) == 2074
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15,left = 100,right = 150) == 2074: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 5,right = 20) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 5,right = 20) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],n = 12,left = 40,right = 80) == 13083
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],n = 12,left = 40,right = 80) == 13083: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],n = 10,left = 5,right = 15) == 1520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],n = 10,left = 5,right = 15) == 1520: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],n = 20,left = 120,right = 200) == 19092
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],n = 20,left = 120,right = 200) == 19092: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4],n = 4,left = 3,right = 4) == 6
    assert candidate(nums = [10, 20, 30],n = 3,left = 1,right = 3) == 60
    assert candidate(nums = [5, 1, 2],n = 3,left = 1,right = 4) == 11
    assert candidate(nums = [1, 2, 3, 4],n = 4,left = 1,right = 5) == 13
    assert candidate(nums = [3, 3, 3, 3],n = 4,left = 2,right = 8) == 36
    assert candidate(nums = [1, 2, 3, 4],n = 4,left = 1,right = 10) == 50
    assert candidate(nums = [3, 3, 3],n = 3,left = 2,right = 5) == 18
    assert candidate(nums = [5, 2, 1, 4],n = 4,left = 3,right = 7) == 24
    assert candidate(nums = [10, 20, 30],n = 3,left = 2,right = 5) == 130
    assert candidate(nums = [5, 1, 4],n = 3,left = 1,right = 6) == 31
    assert candidate(nums = [5, 1, 2, 3],n = 4,left = 2,right = 6) == 18
    assert candidate(nums = [10, 20, 30],n = 3,left = 1,right = 5) == 140
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],n = 15,left = 60,right = 120) == 46215
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 10,left = 25,right = 50) == 756
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 20,right = 30) == 36
    assert candidate(nums = [5, 15, 10, 20, 25],n = 5,left = 1,right = 15) == 520
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],n = 10,left = 25,right = 55) == 2334
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 15,right = 45) == 6700
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 25,right = 75) == 10110
    assert candidate(nums = [100, 200, 300, 400, 500],n = 5,left = 10,right = 20) == 6900
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 1,right = 100) == 2200
    assert candidate(nums = [50, 40, 30, 20, 10],n = 5,left = 5,right = 15) == 960
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],n = 11,left = 15,right = 45) == 460
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,left = 100,right = 200) == 11368
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],n = 15,left = 50,right = 100) == 5098
    assert candidate(nums = [23, 34, 45, 56, 67, 78, 89, 90, 100, 110],n = 10,left = 25,right = 60) == 12693
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],n = 9,left = 25,right = 35) == 250
    assert candidate(nums = [10, 20, 30, 40, 50],n = 5,left = 3,right = 12) == 610
    assert candidate(nums = [5, 15, 10, 20],n = 4,left = 5,right = 12) == 200
    assert candidate(nums = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],n = 12,left = 30,right = 75) == 8471
    assert candidate(nums = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 25,right = 75) == 9910
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13],n = 7,left = 1,right = 28) == 588
    assert candidate(nums = [9, 7, 5, 3, 1],n = 5,left = 6,right = 16) == 155
    assert candidate(nums = [5, 6, 7, 8, 9],n = 5,left = 3,right = 7) == 48
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 1,right = 55) == 220
    assert candidate(nums = [5, 1, 7, 3, 8],n = 5,left = 3,right = 7) == 34
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 10,left = 15,right = 40) == 497
    assert candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],n = 10,left = 1,right = 100) == 1210
    assert candidate(nums = [99, 100, 98, 97, 96],n = 5,left = 10,right = 20) == 2158
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 15,left = 50,right = 150) == 9416
    assert candidate(nums = [42, 53, 64, 75, 86, 97, 108, 119, 130, 141],n = 10,left = 15,right = 45) == 11216
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 30,right = 70) == 9190
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 10,left = 30,right = 50) == 664
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],n = 20,left = 150,right = 250) == 46005
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],n = 11,left = 20,right = 40) == 310
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],n = 10,left = 25,right = 50) == 7560
    assert candidate(nums = [100, 200, 300, 400, 500],n = 5,left = 1,right = 15) == 10500
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 10,right = 30) == 496
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 10,left = 50,right = 100) == 30000
    assert candidate(nums = [9, 8, 7, 6, 5],n = 5,left = 1,right = 15) == 245
    assert candidate(nums = [9, 18, 27, 36, 45, 54],n = 6,left = 10,right = 20) == 1260
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 15,right = 30) == 46
    assert candidate(nums = [100, 200, 300, 400, 500, 600],n = 6,left = 10,right = 30) == 16100
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 10,left = 20,right = 40) == 44500
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],n = 10,left = 50,right = 75) == 364
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 10,left = 30,right = 50) == 664
    assert candidate(nums = [7, 3, 8, 6, 2, 5, 4, 9, 1],n = 9,left = 20,right = 40) == 480
    assert candidate(nums = [99, 98, 97, 96, 95, 94],n = 6,left = 20,right = 30) == 1064
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,left = 150,right = 250) == 9201
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],n = 10,left = 10,right = 30) == 5233
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15,left = 50,right = 60) == 379
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],n = 10,left = 20,right = 50) == 1036
    assert candidate(nums = [10, 20, 30, 40, 50, 60],n = 6,left = 10,right = 20) == 1400
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 25,right = 35) == 421
    assert candidate(nums = [10, 20, 30, 40, 50],n = 5,left = 1,right = 25) == 1050
    assert candidate(nums = [34, 78, 12, 56, 90, 23, 45, 67, 89, 10],n = 10,left = 30,right = 60) == 8474
    assert candidate(nums = [10, 20, 30, 40, 50, 60],n = 6,left = 10,right = 20) == 1400
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],n = 11,left = 5,right = 20) == 95
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 10,left = 1,right = 100) == 2200
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 30,right = 40) == 2810
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 10,left = 30,right = 45) == 908
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],n = 10,left = 55,right = 85) == 550
    assert candidate(nums = [50, 40, 30, 20, 10],n = 5,left = 10,right = 20) == 690
    assert candidate(nums = [9, 7, 5, 3, 1],n = 5,left = 8,right = 12) == 68
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1],n = 7,left = 15,right = 25) == 179
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],n = 15,left = 100,right = 200) == 2074
    assert candidate(nums = [50, 40, 30, 20, 10],n = 5,left = 1,right = 15) == 1050
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15,left = 50,right = 100) == 2715
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 45,right = 75) == 5010
    assert candidate(nums = [9, 3, 5, 7, 2, 8],n = 6,left = 4,right = 12) == 89
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 25,right = 50) == 133
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20],n = 20,left = 50,right = 150) == 6400
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],n = 20,left = 100,right = 150) == 8103
    assert candidate(nums = [5, 15, 25, 35, 45],n = 5,left = 7,right = 14) == 610
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 20,left = 50,right = 100) == 232
    assert candidate(nums = [1, 2, 3, 4, 5],n = 5,left = 1,right = 15) == 105
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],n = 10,left = 25,right = 50) == 410
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 10,left = 55,right = 75) == 550
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],n = 10,left = 5,right = 55) == 21600
    assert candidate(nums = [5, 15, 25, 35, 45],n = 5,left = 5,right = 15) == 810
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],n = 15,left = 50,right = 100) == 5098
    assert candidate(nums = [8, 6, 4, 2, 0, 8, 6, 4, 2, 0],n = 10,left = 20,right = 40) == 344
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],n = 9,left = 10,right = 30) == 291
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 25,right = 45) == 97
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],n = 12,left = 50,right = 75) == 6660
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65],n = 7,left = 15,right = 25) == 1585
    assert candidate(nums = [5, 15, 10, 20, 25],n = 5,left = 4,right = 10) == 195
    assert candidate(nums = [50, 40, 30, 20, 10, 5, 2, 1],n = 8,left = 10,right = 35) == 2000
    assert candidate(nums = [100, 100, 100, 100, 100, 100],n = 6,left = 20,right = 30) == 1100
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 15,left = 50,right = 100) == 5430
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15,left = 100,right = 150) == 2074
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],n = 10,left = 5,right = 20) == 27
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],n = 12,left = 40,right = 80) == 13083
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],n = 10,left = 5,right = 15) == 1520
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],n = 20,left = 120,right = 200) == 19092


