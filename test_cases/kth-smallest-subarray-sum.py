def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 14) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 14) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 5, 5],k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 5, 5],k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 15) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 15) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 15) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 15) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],k = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],k = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 25) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 25) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 5501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 5501: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 55) == 55000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 55) == 55000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 190) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 190) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 40000, 30000, 20000, 10000, 5000, 4000, 3000, 2000, 1000],k = 45) == 112000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 40000, 30000, 20000, 10000, 5000, 4000, 3000, 2000, 1000],k = 45) == 112000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 55) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 55) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 300) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 300) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20000, 10000, 15000, 25000, 30000, 10000, 5000, 50000, 40000, 35000],k = 100) == 240001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20000, 10000, 15000, 25000, 30000, 10000, 5000, 50000, 40000, 35000],k = 100) == 240001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 55) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 55) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 100) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 100) == 153: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 78) == 2048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 78) == 2048: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],k = 25) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],k = 25) == 151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6],k = 20) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6],k = 20) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1000, 10000, 100000],k = 10) == 11101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1000, 10000, 100000],k = 10) == 11101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 210) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 210) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 36) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 36) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 35, 25, 15, 5, 5, 15, 25, 35, 45],k = 45) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 35, 25, 15, 5, 5, 15, 25, 35, 45],k = 45) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 300) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 300) == 211: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 30) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 30) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 3, 2, 4, 6, 5, 1, 8],k = 30) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 3, 2, 4, 6, 5, 1, 8],k = 30) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 85) == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 85) == 276: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 300) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 300) == 211: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 22, 44, 11, 55, 66, 77, 88, 99, 100],k = 50) == 485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 22, 44, 11, 55, 66, 77, 88, 99, 100],k = 50) == 485: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],k = 20) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],k = 20) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 600) == 326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 600) == 326: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 50) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 50) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 50000, 50000, 50000, 50000],k = 25) == 250001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 50000, 50000, 50000, 50000],k = 25) == 250001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 50) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 50) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10],k = 300) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10],k = 300) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 27) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 27) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 55) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 55) == 108: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 2, 5, 3, 7],k = 17) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 2, 5, 3, 7],k = 17) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20],k = 49) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20],k = 49) == 121: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 780) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 780) == 121: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500],k = 30) == 4501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500],k = 30) == 4501: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 55) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 55) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 100) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 100) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 50) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 50) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 210) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 210) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 551: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 66) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 66) == 121: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],k = 30) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],k = 30) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 100) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 100) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 100) == 16352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 100) == 16352: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 50000, 50000, 50000, 50000],k = 14) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 50000, 50000, 50000, 50000],k = 14) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 150) == 12001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 150) == 12001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 190) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 190) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 55) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 55) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 120) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 120) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1],k = 40) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1],k = 40) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 11, 5, 3, 8, 1, 4, 9, 6, 2, 13, 10, 12],k = 80) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 11, 5, 3, 8, 1, 4, 9, 6, 2, 13, 10, 12],k = 80) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 276) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 276) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 50) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 50) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 14) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 14) == 1400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],k = 45) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],k = 45) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 50) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 50) == 315: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 55) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 55) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 45) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 45) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 5, 4, 7, 6, 8, 9, 0],k = 80) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 5, 4, 7, 6, 8, 9, 0],k = 80) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6],k = 40) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6],k = 40) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9, 1, 2, 3, 4, 5, 6],k = 25) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9, 1, 2, 3, 4, 5, 6],k = 25) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 5000, 2500, 1250, 625],k = 14) == 18750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 5000, 2500, 1250, 625],k = 14) == 18750: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 150) == 323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 150) == 323: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 200) == 160000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 200) == 160000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 800) == 516
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 800) == 516: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000, 5000],k = 55) == 275000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000, 5000],k = 55) == 275000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 75) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 75) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 100) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 100) == 81: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 30, 40, 50],k = 14) == 140
    assert candidate(nums = [5, 4, 3, 2, 1],k = 15) == 15
    assert candidate(nums = [10, 20, 30, 40, 50],k = 1) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == 3
    assert candidate(nums = [3, 3, 5, 5],k = 7) == 10
    assert candidate(nums = [1, 2, 3, 4, 5],k = 10) == 9
    assert candidate(nums = [5, 5, 5, 5, 5],k = 15) == 25
    assert candidate(nums = [10, 20, 30, 40, 50],k = 15) == 150
    assert candidate(nums = [2, 1, 3],k = 4) == 3
    assert candidate(nums = [5, 5, 5, 5, 5],k = 1) == 5
    assert candidate(nums = [1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [10, 20, 30],k = 5) == 50
    assert candidate(nums = [1, 2, 3, 4, 5],k = 25) == 16
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 5501
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 55) == 55000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 190) == 15
    assert candidate(nums = [50000, 40000, 30000, 20000, 10000, 5000, 4000, 3000, 2000, 1000],k = 45) == 112000
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 55) == 100000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 300) == 13
    assert candidate(nums = [20000, 10000, 15000, 25000, 30000, 10000, 5000, 50000, 40000, 35000],k = 100) == 240001
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 55) == 55
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 100) == 153
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 78) == 2048
    assert candidate(nums = [50, 40, 30, 20, 10],k = 25) == 151
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6],k = 20) == 12
    assert candidate(nums = [1, 100, 1000, 10000, 100000],k = 10) == 11101
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 210) == 150
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 36) == 48
    assert candidate(nums = [45, 35, 25, 15, 5, 5, 15, 25, 35, 45],k = 45) == 125
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 300) == 211
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 30) == 105
    assert candidate(nums = [9, 7, 3, 2, 4, 6, 5, 1, 8],k = 30) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 21
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 85) == 276
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 300) == 211
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 45
    assert candidate(nums = [33, 22, 44, 11, 55, 66, 77, 88, 99, 100],k = 50) == 485
    assert candidate(nums = [5, 4, 3, 2, 1],k = 20) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 600) == 326
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 50) == 36
    assert candidate(nums = [50000, 50000, 50000, 50000, 50000],k = 25) == 250001
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 50) == 120
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10],k = 300) == 46
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 45) == 45
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 27) == 20
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 55) == 108
    assert candidate(nums = [1, 4, 2, 5, 3, 7],k = 17) == 15
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20],k = 49) == 121
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 780) == 121
    assert candidate(nums = [1000, 900, 800, 700, 600, 500],k = 30) == 4501
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 55) == 5500
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 100) == 37
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 50) == 225
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 13
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 210) == 400
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 551
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 66) == 121
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],k = 30) == 27
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 100) == 42
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 100) == 16352
    assert candidate(nums = [50000, 50000, 50000, 50000, 50000],k = 14) == 200000
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 150) == 12001
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 190) == 85
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 55) == 10
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 120) == 165
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 46
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1],k = 40) == 29
    assert candidate(nums = [7, 11, 5, 3, 8, 1, 4, 9, 6, 2, 13, 10, 12],k = 80) == 56
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 276) == 72
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 50) == 101
    assert candidate(nums = [100, 200, 300, 400, 500],k = 14) == 1400
    assert candidate(nums = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],k = 45) == 160
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 50) == 315
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 55) == 550
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 45) == 60
    assert candidate(nums = [2, 3, 1, 5, 4, 7, 6, 8, 9, 0],k = 80) == 46
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6],k = 40) == 57
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 55
    assert candidate(nums = [7, 8, 9, 1, 2, 3, 4, 5, 6],k = 25) == 15
    assert candidate(nums = [10000, 5000, 2500, 1250, 625],k = 14) == 18750
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 150) == 323
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 200) == 160000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 800) == 516
    assert candidate(nums = [50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000, 5000],k = 55) == 275000
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 75) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 100) == 81


