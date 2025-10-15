def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(difficulty = [68, 35, 52, 47, 86],profit = [67, 17, 17, 26, 86],worker = [68, 37, 50, 76, 33]) == 177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [68, 35, 52, 47, 86],profit = [67, 17, 17, 26, 86],worker = [68, 37, 50, 76, 33]) == 177: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 15, 25],profit = [100, 150, 250],worker = [20, 25, 30]) == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 15, 25],profit = [100, 150, 250],worker = [20, 25, 30]) == 650: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [66, 1, 28, 73, 56, 30, 96, 82, 21, 63],profit = [68, 40, 84, 84, 89, 46, 68, 105, 27, 68],worker = [40, 57, 88, 27, 11, 93, 8, 40, 20, 75]) == 716
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [66, 1, 28, 73, 56, 30, 96, 82, 21, 63],profit = [68, 40, 84, 84, 89, 46, 68, 105, 27, 68],worker = [40, 57, 88, 27, 11, 93, 8, 40, 20, 75]) == 716: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30],profit = [60, 50, 40],worker = [40, 25, 20]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30],profit = [60, 50, 40],worker = [40, 25, 20]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [66, 1, 21, 88, 76, 13, 11, 60, 20, 35, 96, 77, 6, 46, 93],profit = [67, 68, 69, 55, 73, 60, 59, 66, 70, 58, 74, 72, 67, 68, 71],worker = [65, 91, 33, 52, 78]) == 356
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [66, 1, 21, 88, 76, 13, 11, 60, 20, 35, 96, 77, 6, 46, 93],profit = [67, 68, 69, 55, 73, 60, 59, 66, 70, 58, 74, 72, 67, 68, 71],worker = [65, 91, 33, 52, 78]) == 356: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [85, 47, 57],profit = [24, 66, 99],worker = [40, 25, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [85, 47, 57],profit = [24, 66, 99],worker = [40, 25, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100],profit = [100],worker = [100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100],profit = [100],worker = [100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30],profit = [100, 200, 300],worker = [15, 25, 35]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30],profit = [100, 200, 300],worker = [15, 25, 35]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [2, 4, 6, 8, 10],profit = [10, 20, 30, 40, 50],worker = [4, 5, 6, 7]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [2, 4, 6, 8, 10],profit = [10, 20, 30, 40, 50],worker = [4, 5, 6, 7]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 9, 10, 7, 4],profit = [4, 1, 10, 3, 9],worker = [4, 5, 6, 7, 8, 9, 10]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 9, 10, 7, 4],profit = [4, 1, 10, 3, 9],worker = [4, 5, 6, 7, 8, 9, 10]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 10, 15],profit = [10, 20, 30],worker = [5, 10, 15, 20]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 10, 15],profit = [10, 20, 30],worker = [5, 10, 15, 20]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5],profit = [1, 2, 3, 4, 5],worker = [5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5],profit = [1, 2, 3, 4, 5],worker = [5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 1, 1],profit = [1, 2, 3],worker = [1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 1, 1],profit = [1, 2, 3],worker = [1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [68, 35, 52, 47, 86],profit = [67, 17, 1, 50, 76],worker = [36, 99, 24, 79, 50]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [68, 35, 52, 47, 86],profit = [67, 17, 1, 50, 76],worker = [36, 99, 24, 79, 50]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 15, 25, 35, 45, 55],profit = [10, 20, 30, 40, 50, 60],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 15, 25, 35, 45, 55],profit = [10, 20, 30, 40, 50, 60],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 830
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 830: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],profit = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],worker = [1, 3, 5, 7, 9, 11, 13, 15]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],profit = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],worker = [1, 3, 5, 7, 9, 11, 13, 15]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97],profit = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5],worker = [20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]) == 870
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97],profit = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5],worker = [20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]) == 870: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5],profit = [10, 2, 15, 4, 25],worker = [1, 2, 3, 4, 5]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5],profit = [10, 2, 15, 4, 25],worker = [1, 2, 3, 4, 5]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 2, 10, 3, 8],profit = [20, 10, 30, 5, 40],worker = [3, 15, 10, 2, 8]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 2, 10, 3, 8],profit = [20, 10, 30, 5, 40],worker = [3, 15, 10, 2, 8]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 1, 1, 1, 1],profit = [100, 200, 300, 400, 500],worker = [1, 1, 1, 1, 1]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 1, 1, 1, 1],profit = [100, 200, 300, 400, 500],worker = [1, 1, 1, 1, 1]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],worker = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],worker = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100, 200, 300, 400, 500],profit = [1000, 900, 800, 700, 600],worker = [250, 150, 350, 450, 550]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100, 200, 300, 400, 500],profit = [1000, 900, 800, 700, 600],worker = [250, 150, 350, 450, 550]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50],profit = [10, 10, 10, 10, 10],worker = [5, 15, 25, 35, 45, 55]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50],profit = [10, 10, 10, 10, 10],worker = [5, 15, 25, 35, 45, 55]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],worker = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],worker = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 10, 15, 20, 25],profit = [10, 20, 30, 40, 50],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 10, 15, 20, 25],profit = [10, 20, 30, 40, 50],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 290: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [2, 2, 2, 2, 2],profit = [50, 50, 50, 50, 50],worker = [2, 2, 2, 2, 2]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [2, 2, 2, 2, 2],profit = [50, 50, 50, 50, 50],worker = [2, 2, 2, 2, 2]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],worker = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],worker = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 5, 7, 10, 15],profit = [2, 8, 10, 4, 6],worker = [1, 3, 5, 7, 9, 11, 13, 15]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 5, 7, 10, 15],profit = [2, 8, 10, 4, 6],worker = [1, 3, 5, 7, 9, 11, 13, 15]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650],worker = [3, 6, 8, 12, 16, 18, 22, 26, 28, 32, 36, 38]) == 3900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650],worker = [3, 6, 8, 12, 16, 18, 22, 26, 28, 32, 36, 38]) == 3900: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],profit = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],worker = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],profit = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],worker = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5],profit = [100000, 90000, 80000, 70000, 60000],worker = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 2500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5],profit = [100000, 90000, 80000, 70000, 60000],worker = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 2500000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 5, 10, 15, 20],profit = [500, 400, 300, 200, 100],worker = [25, 20, 15, 10, 5]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 5, 10, 15, 20],profit = [500, 400, 300, 200, 100],worker = [25, 20, 15, 10, 5]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [1, 3, 5, 7, 9]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [1, 3, 5, 7, 9]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5],profit = [1, 2, 3, 4, 5],worker = [5, 5, 5, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5],profit = [1, 2, 3, 4, 5],worker = [5, 5, 5, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 10, 100, 1000, 10000],profit = [10000, 1000, 100, 10, 1],worker = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]) == 90000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 10, 100, 1000, 10000],profit = [10000, 1000, 100, 10, 1],worker = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]) == 90000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [20, 10, 30, 40, 50],profit = [100, 50, 200, 150, 250],worker = [5, 15, 25, 35, 45, 55]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [20, 10, 30, 40, 50],profit = [100, 50, 200, 150, 250],worker = [5, 15, 25, 35, 45, 55]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100000, 10000, 1000, 100, 10],profit = [1, 10, 100, 1000, 10000],worker = [50, 500, 5000, 50000, 100000]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100000, 10000, 1000, 100, 10],profit = [1, 10, 100, 1000, 10000],worker = [50, 500, 5000, 50000, 100000]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 5, 5],profit = [10, 20, 30],worker = [5, 5, 5]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 5, 5],profit = [10, 20, 30],worker = [5, 5, 5]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50],profit = [10, 20, 30, 40, 50],worker = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50],profit = [10, 20, 30, 40, 50],worker = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 14250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 14250: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 4500: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [50, 25, 75, 100, 125],profit = [10, 20, 30, 40, 50],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [50, 25, 75, 100, 125],profit = [10, 20, 30, 40, 50],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 430: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [100, 200, 100, 300, 200, 400, 300, 500, 400, 600],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [100, 200, 100, 300, 200, 400, 300, 500, 400, 600],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100000],profit = [100000],worker = [100000]) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100000],profit = [100000],worker = [100000]) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [30, 20, 10],profit = [3, 2, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [30, 20, 10],profit = [3, 2, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50],profit = [5, 15, 25, 35, 45],worker = [10, 25, 35, 45, 55]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50],profit = [5, 15, 25, 35, 45],worker = [10, 25, 35, 45, 55]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50],profit = [50, 40, 30, 20, 10],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50],profit = [50, 40, 30, 20, 10],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 2, 1, 8, 3, 7, 4, 6, 9, 10],profit = [50, 20, 10, 80, 30, 70, 40, 60, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 2, 1, 8, 3, 7, 4, 6, 9, 10],profit = [50, 20, 10, 80, 30, 70, 40, 60, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [50, 40, 30, 20, 10, 50, 40, 30, 20, 10],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [50, 40, 30, 20, 10, 50, 40, 30, 20, 10],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100, 50, 150, 200, 250],profit = [300, 200, 400, 500, 600],worker = [200, 300, 100, 150, 250, 50]) == 2600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100, 50, 150, 200, 250],profit = [300, 200, 400, 500, 600],worker = [200, 300, 100, 150, 250, 50]) == 2600: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [50, 40, 30, 20, 10],profit = [1000, 900, 800, 700, 600],worker = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [50, 40, 30, 20, 10],profit = [1000, 900, 800, 700, 600],worker = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 8000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [3, 6, 12, 24, 48],profit = [10, 20, 40, 80, 160],worker = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [3, 6, 12, 24, 48],profit = [10, 20, 40, 80, 160],worker = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 630: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 750: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [5, 8, 3, 10, 2, 7, 6, 9, 1, 4],worker = [1, 3, 5, 7, 9]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [5, 8, 3, 10, 2, 7, 6, 9, 1, 4],worker = [1, 3, 5, 7, 9]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100, 150, 200],profit = [10, 20, 30],worker = [50, 100, 125, 150, 175, 200, 250]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100, 150, 200],profit = [10, 20, 30],worker = [50, 100, 125, 150, 175, 200, 250]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50],profit = [50, 40, 30, 20, 10],worker = [5, 15, 25, 35, 45, 55]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50],profit = [50, 40, 30, 20, 10],worker = [5, 15, 25, 35, 45, 55]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 10, 100, 1000, 10000],profit = [10, 100, 1000, 10000, 100000],worker = [1, 5, 50, 500, 5000, 10000, 15000]) == 211120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 10, 100, 1000, 10000],profit = [10, 100, 1000, 10000, 100000],worker = [1, 5, 50, 500, 5000, 10000, 15000]) == 211120: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],worker = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],worker = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 15, 25, 35, 45],profit = [10, 20, 30, 40, 50],worker = [1, 10, 20, 30, 40, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 15, 25, 35, 45],profit = [10, 20, 30, 40, 50],worker = [1, 10, 20, 30, 40, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],profit = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],profit = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [99999, 89999, 79999, 69999, 59999, 49999, 39999, 29999, 19999, 9999]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [99999, 89999, 79999, 69999, 59999, 49999, 39999, 29999, 19999, 9999]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [50000, 40000, 30000, 20000, 10000],profit = [100, 200, 300, 400, 500],worker = [50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000, 5000]) == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [50000, 40000, 30000, 20000, 10000],profit = [100, 200, 300, 400, 500],worker = [50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000, 5000]) == 4500: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5],profit = [5, 4, 3, 2, 1],worker = [1, 2, 3, 4, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5],profit = [5, 4, 3, 2, 1],worker = [1, 2, 3, 4, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],profit = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],profit = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 380: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [100000, 100000, 100000],profit = [100000, 100000, 100000],worker = [100000, 100000, 100000]) == 300000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [100000, 100000, 100000],profit = [100000, 100000, 100000],worker = [100000, 100000, 100000]) == 300000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 4, 8, 6, 9, 10, 12, 14, 16, 18],profit = [30, 20, 80, 60, 90, 100, 110, 120, 130, 140],worker = [5, 7, 9, 11, 13, 15, 17, 19, 21]) == 920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 4, 8, 6, 9, 10, 12, 14, 16, 18],profit = [30, 20, 80, 60, 90, 100, 110, 120, 130, 140],worker = [5, 7, 9, 11, 13, 15, 17, 19, 21]) == 920: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [10000, 20000, 30000, 40000, 50000],profit = [100, 200, 300, 400, 500],worker = [5000, 15000, 25000, 35000, 45000, 55000]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [10000, 20000, 30000, 40000, 50000],profit = [100, 200, 300, 400, 500],worker = [5000, 15000, 25000, 35000, 45000, 55000]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(difficulty = [5, 10, 15, 20],profit = [50, 30, 20, 60],worker = [5, 10, 15, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(difficulty = [5, 10, 15, 20],profit = [50, 30, 20, 60],worker = [5, 10, 15, 20]) == 210: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(difficulty = [68, 35, 52, 47, 86],profit = [67, 17, 17, 26, 86],worker = [68, 37, 50, 76, 33]) == 177
    assert candidate(difficulty = [10, 15, 25],profit = [100, 150, 250],worker = [20, 25, 30]) == 650
    assert candidate(difficulty = [66, 1, 28, 73, 56, 30, 96, 82, 21, 63],profit = [68, 40, 84, 84, 89, 46, 68, 105, 27, 68],worker = [40, 57, 88, 27, 11, 93, 8, 40, 20, 75]) == 716
    assert candidate(difficulty = [10, 20, 30],profit = [60, 50, 40],worker = [40, 25, 20]) == 180
    assert candidate(difficulty = [66, 1, 21, 88, 76, 13, 11, 60, 20, 35, 96, 77, 6, 46, 93],profit = [67, 68, 69, 55, 73, 60, 59, 66, 70, 58, 74, 72, 67, 68, 71],worker = [65, 91, 33, 52, 78]) == 356
    assert candidate(difficulty = [85, 47, 57],profit = [24, 66, 99],worker = [40, 25, 25]) == 0
    assert candidate(difficulty = [100],profit = [100],worker = [100]) == 100
    assert candidate(difficulty = [10, 20, 30],profit = [100, 200, 300],worker = [15, 25, 35]) == 600
    assert candidate(difficulty = [2, 4, 6, 8, 10],profit = [10, 20, 30, 40, 50],worker = [4, 5, 6, 7]) == 100
    assert candidate(difficulty = [5, 9, 10, 7, 4],profit = [4, 1, 10, 3, 9],worker = [4, 5, 6, 7, 8, 9, 10]) == 64
    assert candidate(difficulty = [5, 10, 15],profit = [10, 20, 30],worker = [5, 10, 15, 20]) == 90
    assert candidate(difficulty = [1, 2, 3, 4, 5],profit = [1, 2, 3, 4, 5],worker = [5, 4, 3, 2, 1]) == 15
    assert candidate(difficulty = [1, 1, 1],profit = [1, 2, 3],worker = [1, 1, 1]) == 9
    assert candidate(difficulty = [68, 35, 52, 47, 86],profit = [67, 17, 1, 50, 76],worker = [36, 99, 24, 79, 50]) == 210
    assert candidate(difficulty = [5, 15, 25, 35, 45, 55],profit = [10, 20, 30, 40, 50, 60],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 450
    assert candidate(difficulty = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 830
    assert candidate(difficulty = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1000
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],profit = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],worker = [1, 3, 5, 7, 9, 11, 13, 15]) == 1200
    assert candidate(difficulty = [50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97],profit = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5],worker = [20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]) == 870
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1000
    assert candidate(difficulty = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
    assert candidate(difficulty = [1, 2, 3, 4, 5],profit = [10, 2, 15, 4, 25],worker = [1, 2, 3, 4, 5]) == 75
    assert candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1050
    assert candidate(difficulty = [5, 2, 10, 3, 8],profit = [20, 10, 30, 5, 40],worker = [3, 15, 10, 2, 8]) == 140
    assert candidate(difficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1900
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1000
    assert candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 10000
    assert candidate(difficulty = [1, 1, 1, 1, 1],profit = [100, 200, 300, 400, 500],worker = [1, 1, 1, 1, 1]) == 2500
    assert candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 100
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],worker = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]) == 1200
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550
    assert candidate(difficulty = [100, 200, 300, 400, 500],profit = [1000, 900, 800, 700, 600],worker = [250, 150, 350, 450, 550]) == 5000
    assert candidate(difficulty = [10, 20, 30, 40, 50],profit = [10, 10, 10, 10, 10],worker = [5, 15, 25, 35, 45, 55]) == 50
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],worker = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 300
    assert candidate(difficulty = [5, 10, 15, 20, 25],profit = [10, 20, 30, 40, 50],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 290
    assert candidate(difficulty = [2, 2, 2, 2, 2],profit = [50, 50, 50, 50, 50],worker = [2, 2, 2, 2, 2]) == 250
    assert candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 11
    assert candidate(difficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],profit = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 180
    assert candidate(difficulty = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
    assert candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],worker = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 100
    assert candidate(difficulty = [1, 5, 7, 10, 15],profit = [2, 8, 10, 4, 6],worker = [1, 3, 5, 7, 9, 11, 13, 15]) == 62
    assert candidate(difficulty = [1, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650],worker = [3, 6, 8, 12, 16, 18, 22, 26, 28, 32, 36, 38]) == 3900
    assert candidate(difficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100
    assert candidate(difficulty = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],profit = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],worker = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10000
    assert candidate(difficulty = [1, 2, 3, 4, 5],profit = [100000, 90000, 80000, 70000, 60000],worker = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 2500000
    assert candidate(difficulty = [1, 5, 10, 15, 20],profit = [500, 400, 300, 200, 100],worker = [25, 20, 15, 10, 5]) == 2500
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [1, 3, 5, 7, 9]) == 2500
    assert candidate(difficulty = [1, 2, 3, 4, 5],profit = [1, 2, 3, 4, 5],worker = [5, 5, 5, 5, 5]) == 25
    assert candidate(difficulty = [1, 10, 100, 1000, 10000],profit = [10000, 1000, 100, 10, 1],worker = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]) == 90000
    assert candidate(difficulty = [20, 10, 30, 40, 50],profit = [100, 50, 200, 150, 250],worker = [5, 15, 25, 35, 45, 55]) == 800
    assert candidate(difficulty = [100000, 10000, 1000, 100, 10],profit = [1, 10, 100, 1000, 10000],worker = [50, 500, 5000, 50000, 100000]) == 50000
    assert candidate(difficulty = [5, 5, 5],profit = [10, 20, 30],worker = [5, 5, 5]) == 90
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
    assert candidate(difficulty = [10, 20, 30, 40, 50],profit = [10, 20, 30, 40, 50],worker = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 250
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 14250
    assert candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 4500
    assert candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5500
    assert candidate(difficulty = [50, 25, 75, 100, 125],profit = [10, 20, 30, 40, 50],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 430
    assert candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [100, 200, 100, 300, 200, 400, 300, 500, 400, 600],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5000
    assert candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 100
    assert candidate(difficulty = [100000],profit = [100000],worker = [100000]) == 100000
    assert candidate(difficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100
    assert candidate(difficulty = [30, 20, 10],profit = [3, 2, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(difficulty = [10, 20, 30, 40, 50],profit = [5, 15, 25, 35, 45],worker = [10, 25, 35, 45, 55]) == 125
    assert candidate(difficulty = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007, 50008, 50009]) == 0
    assert candidate(difficulty = [10, 20, 30, 40, 50],profit = [50, 40, 30, 20, 10],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 500
    assert candidate(difficulty = [5, 2, 1, 8, 3, 7, 4, 6, 9, 10],profit = [50, 20, 10, 80, 30, 70, 40, 60, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [50, 40, 30, 20, 10, 50, 40, 30, 20, 10],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 300
    assert candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1000
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(difficulty = [100, 50, 150, 200, 250],profit = [300, 200, 400, 500, 600],worker = [200, 300, 100, 150, 250, 50]) == 2600
    assert candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]) == 450
    assert candidate(difficulty = [50, 40, 30, 20, 10],profit = [1000, 900, 800, 700, 600],worker = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 8000
    assert candidate(difficulty = [3, 6, 12, 24, 48],profit = [10, 20, 40, 80, 160],worker = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 630
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 750
    assert candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1100
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [5, 8, 3, 10, 2, 7, 6, 9, 1, 4],worker = [1, 3, 5, 7, 9]) == 43
    assert candidate(difficulty = [100, 150, 200],profit = [10, 20, 30],worker = [50, 100, 125, 150, 175, 200, 250]) == 120
    assert candidate(difficulty = [10, 20, 30, 40, 50],profit = [50, 40, 30, 20, 10],worker = [5, 15, 25, 35, 45, 55]) == 250
    assert candidate(difficulty = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 60
    assert candidate(difficulty = [1, 10, 100, 1000, 10000],profit = [10, 100, 1000, 10000, 100000],worker = [1, 5, 50, 500, 5000, 10000, 15000]) == 211120
    assert candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],worker = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1000
    assert candidate(difficulty = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],worker = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210]) == 55
    assert candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],worker = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
    assert candidate(difficulty = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],worker = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 10
    assert candidate(difficulty = [5, 15, 25, 35, 45],profit = [10, 20, 30, 40, 50],worker = [1, 10, 20, 30, 40, 50]) == 150
    assert candidate(difficulty = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],profit = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profit = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],worker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 400
    assert candidate(difficulty = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 550
    assert candidate(difficulty = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [99999, 89999, 79999, 69999, 59999, 49999, 39999, 29999, 19999, 9999]) == 900
    assert candidate(difficulty = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 550
    assert candidate(difficulty = [50000, 40000, 30000, 20000, 10000],profit = [100, 200, 300, 400, 500],worker = [50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000, 5000]) == 4500
    assert candidate(difficulty = [1, 2, 3, 4, 5],profit = [5, 4, 3, 2, 1],worker = [1, 2, 3, 4, 5]) == 25
    assert candidate(difficulty = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],profit = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],worker = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 380
    assert candidate(difficulty = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],profit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],worker = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 600
    assert candidate(difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],worker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(difficulty = [100000, 100000, 100000],profit = [100000, 100000, 100000],worker = [100000, 100000, 100000]) == 300000
    assert candidate(difficulty = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],profit = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],worker = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 6000
    assert candidate(difficulty = [5, 4, 8, 6, 9, 10, 12, 14, 16, 18],profit = [30, 20, 80, 60, 90, 100, 110, 120, 130, 140],worker = [5, 7, 9, 11, 13, 15, 17, 19, 21]) == 920
    assert candidate(difficulty = [10000, 20000, 30000, 40000, 50000],profit = [100, 200, 300, 400, 500],worker = [5000, 15000, 25000, 35000, 45000, 55000]) == 1500
    assert candidate(difficulty = [5, 10, 15, 20],profit = [50, 30, 20, 60],worker = [5, 10, 15, 20]) == 210


