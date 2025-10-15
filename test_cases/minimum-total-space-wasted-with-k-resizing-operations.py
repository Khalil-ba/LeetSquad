def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30],k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30],k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 0) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 0) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 300, 200, 350],k = 2) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 300, 200, 350],k = 2) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 30, 20],k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 30, 20],k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 0) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 0) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 0) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 0) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 0) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 0) == 450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 6, 10],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 6, 10],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20],k = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20],k = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 30, 25, 40],k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 30, 25, 40],k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 30, 25, 15],k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 30, 25, 15],k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 200, 100, 400, 300, 200, 500, 400, 300, 600, 500, 400, 700, 600, 500, 800, 700, 600, 900, 800, 700, 1000, 900, 800, 1100, 1000, 900, 1200, 1100, 1000, 1300, 1200, 1100, 1400, 1300, 1200, 1500, 1400, 1300, 1600, 1500, 1400, 1700, 1600, 1500, 1800, 1700, 1600, 1900, 1800, 1700, 2000, 1900, 1800, 2100, 2000, 1900, 2200, 2100, 2000, 2300, 2200, 2100, 2400, 2300, 2200],k = 30) == 4800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 200, 100, 400, 300, 200, 500, 400, 300, 600, 500, 400, 700, 600, 500, 800, 700, 600, 900, 800, 700, 1000, 900, 800, 1100, 1000, 900, 1200, 1100, 1000, 1300, 1200, 1100, 1400, 1300, 1200, 1500, 1400, 1300, 1600, 1500, 1400, 1700, 1600, 1500, 1800, 1700, 1600, 1900, 1800, 1700, 2000, 1900, 1800, 2100, 2000, 1900, 2200, 2100, 2000, 2300, 2200, 2100, 2400, 2300, 2200],k = 30) == 4800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 100) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 100) == inf: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 14) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 14) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 10) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 10) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 4, 7, 8, 6, 9],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 4, 7, 8, 6, 9],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 15, 10, 5, 15, 20, 25, 30, 35, 40, 45, 50],k = 2) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 15, 10, 5, 15, 20, 25, 30, 35, 40, 45, 50],k = 2) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 4) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 4) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 200, 100, 50, 25, 125, 62, 31, 15, 7, 3, 1],k = 5) == 186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 200, 100, 50, 25, 125, 62, 31, 15, 7, 3, 1],k = 5) == 186: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 300, 250, 350, 400],k = 2) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 300, 250, 350, 400],k = 2) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 25, 40, 35, 50, 45, 60, 55],k = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 25, 40, 35, 50, 45, 60, 55],k = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 0) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 0) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000],k = 9) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000],k = 9) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 3) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 3) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 5) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 5) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 9) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 9) == 495: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 9) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 9) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200) == inf: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110, 105],k = 3) == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110, 105],k = 3) == 215: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 100, 300, 250, 200, 350, 400, 300],k = 3) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 100, 300, 250, 200, 350, 400, 300],k = 3) == 450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 10) == 1985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 10) == 1985: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 0) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 0) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 750000, 250000, 100000],k = 2) == 400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 750000, 250000, 100000],k = 2) == 400000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 4) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 4) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35, 45],k = 6) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35, 45],k = 6) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],k = 5) == 140629
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],k = 5) == 140629: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 6) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 6) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 5) == 73729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 5) == 73729: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 300, 250, 400, 350],k = 2) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 300, 250, 400, 350],k = 2) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500],k = 2) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500],k = 2) == 450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100],k = 5) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100],k = 5) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 20, 10, 40, 30, 20, 50, 40, 30, 20, 60, 50, 40, 30],k = 5) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 20, 10, 40, 30, 20, 50, 40, 30, 20, 60, 50, 40, 30],k = 5) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 9) == 977778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 9) == 977778: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 150, 100, 50, 150, 200, 250, 300, 350, 400],k = 3) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 150, 100, 50, 150, 200, 250, 300, 350, 400],k = 3) == 350: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 400000, 300000, 200000, 100000, 100000, 200000, 300000, 400000, 500000, 100000, 200000, 300000, 400000, 500000, 100000, 200000, 300000, 400000, 500000],k = 7) == 1400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 400000, 300000, 200000, 100000, 100000, 200000, 300000, 400000, 500000, 100000, 200000, 300000, 400000, 500000, 100000, 200000, 300000, 400000, 500000],k = 7) == 1400000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 5) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 5) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205],k = 7) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205],k = 7) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],k = 10) == 3788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],k = 10) == 3788: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 30, 5, 40, 25, 60, 35, 70, 45, 80, 55, 90, 65, 100, 75, 110, 85, 120, 95, 130, 105, 140, 115, 150, 125, 160, 135, 170, 145, 180, 155],k = 8) == 515
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 30, 5, 40, 25, 60, 35, 70, 45, 80, 55, 90, 65, 100, 75, 110, 85, 120, 95, 130, 105, 140, 115, 150, 125, 160, 135, 170, 145, 180, 155],k = 8) == 515: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 10, 20, 30, 40, 50],k = 3) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 10, 20, 30, 40, 50],k = 3) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],k = 25) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],k = 25) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 4) == 488889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 4) == 488889: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 300, 250, 400],k = 2) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 300, 250, 400],k = 2) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 9) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 9) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9],k = 25) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9],k = 25) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 15) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 15) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 100, 250, 200, 150, 300],k = 2) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 100, 250, 200, 150, 300],k = 2) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 100, 200, 100, 200, 100, 200, 100, 200, 100],k = 4) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 100, 200, 100, 200, 100, 200, 100, 200, 100],k = 4) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996],k = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996],k = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 10) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 10) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 50, 25, 10, 5, 2, 1, 1, 2, 5, 10, 25, 50, 100, 200, 300, 400, 500],k = 10) == 264
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 50, 25, 10, 5, 2, 1, 1, 2, 5, 10, 25, 50, 100, 200, 300, 400, 500],k = 10) == 264: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110, 105, 120, 115, 130, 125, 140, 135, 150, 145, 160, 155, 170, 165, 180, 175, 190, 185, 200, 195, 210, 205, 220, 215, 230, 225, 240, 235, 250, 245, 260, 255, 270, 265, 280, 275, 290, 285, 300, 295, 310, 305, 320, 315, 330, 325, 340, 335, 350, 345, 360, 355, 370, 365, 380, 375, 390, 385, 400, 395, 410, 405],k = 100) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110, 105, 120, 115, 130, 125, 140, 135, 150, 145, 160, 155, 170, 165, 180, 175, 190, 185, 200, 195, 210, 205, 220, 215, 230, 225, 240, 235, 250, 245, 260, 255, 270, 265, 280, 275, 290, 285, 300, 295, 310, 305, 320, 315, 330, 325, 340, 335, 350, 345, 360, 355, 370, 365, 380, 375, 390, 385, 400, 395, 410, 405],k = 100) == inf: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 110, 80, 120, 70, 130, 60, 140, 50, 150, 40, 160, 30, 170, 20, 180, 10, 190, 0],k = 5) == 820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 110, 80, 120, 70, 130, 60, 140, 50, 150, 40, 160, 30, 170, 20, 180, 10, 190, 0],k = 5) == 820: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 7) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 7) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 30, 20, 25, 35, 40, 45, 50],k = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 30, 20, 25, 35, 40, 45, 50],k = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 0) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 0) == 450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 15, 10, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85],k = 5) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 15, 10, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85],k = 5) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000, 4500, 6000],k = 5) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000, 4500, 6000],k = 5) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 10, 10, 10, 10],k = 2) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30],k = 3) == 10
    assert candidate(nums = [10, 20, 30],k = 1) == 10
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 0) == 45
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7],k = 3) == 3
    assert candidate(nums = [100, 200, 150, 300, 200, 350],k = 2) == 250
    assert candidate(nums = [10, 20, 15, 30, 20],k = 2) == 15
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 0) == 90
    assert candidate(nums = [1, 2, 3, 4, 5],k = 4) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
    assert candidate(nums = [100, 200, 300, 400, 500],k = 0) == 1000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 0) == 450
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500],k = 4) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 10
    assert candidate(nums = [5, 8, 6, 10],k = 1) == 5
    assert candidate(nums = [1, 3, 5, 7, 9],k = 4) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 0
    assert candidate(nums = [5, 5, 5, 5, 5],k = 0) == 0
    assert candidate(nums = [1000000, 1000000, 1000000],k = 2) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 40
    assert candidate(nums = [10, 20],k = 0) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 5
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 0
    assert candidate(nums = [20, 10, 30, 25, 40],k = 2) == 15
    assert candidate(nums = [5, 5, 5, 5, 5, 5],k = 0) == 0
    assert candidate(nums = [20, 10, 30, 25, 15],k = 2) == 15
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 4
    assert candidate(nums = [300, 200, 100, 400, 300, 200, 500, 400, 300, 600, 500, 400, 700, 600, 500, 800, 700, 600, 900, 800, 700, 1000, 900, 800, 1100, 1000, 900, 1200, 1100, 1000, 1300, 1200, 1100, 1400, 1300, 1200, 1500, 1400, 1300, 1600, 1500, 1400, 1700, 1600, 1500, 1800, 1700, 1600, 1900, 1800, 1700, 2000, 1900, 1800, 2100, 2000, 1900, 2200, 2100, 2000, 2300, 2200, 2100, 2400, 2300, 2200],k = 30) == 4800
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 100) == inf
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 14) == 15
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 10) == 33
    assert candidate(nums = [3, 5, 4, 7, 8, 6, 9],k = 2) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 18
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 120
    assert candidate(nums = [20, 15, 10, 5, 15, 20, 25, 30, 35, 40, 45, 50],k = 2) == 65
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 4) == 50
    assert candidate(nums = [300, 200, 100, 50, 25, 125, 62, 31, 15, 7, 3, 1],k = 5) == 186
    assert candidate(nums = [100, 200, 150, 300, 250, 350, 400],k = 2) == 250
    assert candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5) == 50
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 0
    assert candidate(nums = [10, 20, 30, 25, 40, 35, 50, 45, 60, 55],k = 4) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 0) == 190
    assert candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000],k = 9) == 5000
    assert candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 0) == 0
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 3) == 30
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4) == 90
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 5) == 24
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 9) == 495
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994],k = 3) == 3
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],k = 0) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 9) == 29
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 50
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200) == inf
    assert candidate(nums = [20, 10, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110, 105],k = 3) == 215
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 0
    assert candidate(nums = [100, 200, 150, 100, 300, 250, 200, 350, 400, 300],k = 3) == 450
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 10) == 1985
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 0) == 1900
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 90
    assert candidate(nums = [1000000, 500000, 750000, 250000, 100000],k = 2) == 400000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 4) == 150
    assert candidate(nums = [10, 5, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35, 45],k = 6) == 45
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 0
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],k = 5) == 140629
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 6) == 12
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],k = 5) == 73729
    assert candidate(nums = [100, 200, 150, 300, 250, 400, 350],k = 2) == 250
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 5) == 120
    assert candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500],k = 2) == 450
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100],k = 5) == 80
    assert candidate(nums = [10, 20, 30, 20, 10, 40, 30, 20, 50, 40, 30, 20, 60, 50, 40, 30],k = 5) == 130
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 9) == 977778
    assert candidate(nums = [200, 150, 100, 50, 150, 200, 250, 300, 350, 400],k = 3) == 350
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 0) == 0
    assert candidate(nums = [500000, 400000, 300000, 200000, 100000, 100000, 200000, 300000, 400000, 500000, 100000, 200000, 300000, 400000, 500000, 100000, 200000, 300000, 400000, 500000],k = 7) == 1400000
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 5) == 81
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205],k = 7) == 160
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],k = 10) == 3788
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5) == 0
    assert candidate(nums = [20, 10, 30, 5, 40, 25, 60, 35, 70, 45, 80, 55, 90, 65, 100, 75, 110, 85, 120, 95, 130, 105, 140, 115, 150, 125, 160, 135, 170, 145, 180, 155],k = 8) == 515
    assert candidate(nums = [10, 20, 10, 30, 10, 20, 30, 40, 50],k = 3) == 50
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],k = 25) == 48
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 10
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 4) == 488889
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 0) == 0
    assert candidate(nums = [100, 200, 150, 300, 250, 400],k = 2) == 200
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 9) == 45
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9],k = 25) == 119
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 15) == 140
    assert candidate(nums = [100, 200, 150, 100, 250, 200, 150, 300],k = 2) == 400
    assert candidate(nums = [200, 100, 200, 100, 200, 100, 200, 100, 200, 100],k = 4) == 300
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996],k = 0) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 10) == 90
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 1200
    assert candidate(nums = [500, 400, 300, 200, 100, 50, 25, 10, 5, 2, 1, 1, 2, 5, 10, 25, 50, 100, 200, 300, 400, 500],k = 10) == 264
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 9
    assert candidate(nums = [10, 20, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110, 105, 120, 115, 130, 125, 140, 135, 150, 145, 160, 155, 170, 165, 180, 175, 190, 185, 200, 195, 210, 205, 220, 215, 230, 225, 240, 235, 250, 245, 260, 255, 270, 265, 280, 275, 290, 285, 300, 295, 310, 305, 320, 315, 330, 325, 340, 335, 350, 345, 360, 355, 370, 365, 380, 375, 390, 385, 400, 395, 410, 405],k = 100) == inf
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 90
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 8
    assert candidate(nums = [100, 90, 110, 80, 120, 70, 130, 60, 140, 50, 150, 40, 160, 30, 170, 20, 180, 10, 190, 0],k = 5) == 820
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 7) == 16
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 10) == 100
    assert candidate(nums = [10, 20, 15, 30, 20, 25, 35, 40, 45, 50],k = 4) == 30
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],k = 5) == 9
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 0) == 450
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 6
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 0
    assert candidate(nums = [20, 15, 10, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85],k = 5) == 100
    assert candidate(nums = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000, 4500, 6000],k = 5) == 2000
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 0) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0


