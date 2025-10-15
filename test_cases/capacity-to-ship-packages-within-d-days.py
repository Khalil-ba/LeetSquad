def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(weights = [10, 50, 100, 100, 50, 10],days = 2) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 50, 100, 100, 50, 10],days = 2) == 160: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],days = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],days = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 50, 100, 100, 50, 10],days = 3) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 50, 100, 100, 50, 10],days = 3) == 160: {e}')
    
    total += 1
    try:
        result = candidate(weights = [3, 2, 2, 4, 1, 4],days = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [3, 2, 2, 4, 1, 4],days = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 1, 1],days = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 1, 1],days = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],days = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],days = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 5, 5, 5, 5],days = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 5, 5, 5, 5],days = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(weights = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],days = 5) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],days = 5) == 83: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],days = 4) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],days = 4) == 170: {e}')
    
    total += 1
    try:
        result = candidate(weights = [4, 3, 2, 5, 8, 2, 3, 5, 6, 1, 2, 4, 3, 7, 5],days = 8) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [4, 3, 2, 5, 8, 2, 3, 5, 6, 1, 2, 4, 3, 7, 5],days = 8) == 10: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],days = 5) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],days = 5) == 52: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],days = 6) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],days = 6) == 48: {e}')
    
    total += 1
    try:
        result = candidate(weights = [9, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 3) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [9, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 3) == 39: {e}')
    
    total += 1
    try:
        result = candidate(weights = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450],days = 2) == 2250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450],days = 2) == 2250: {e}')
    
    total += 1
    try:
        result = candidate(weights = [30, 40, 20, 5, 10, 80, 25, 45, 60, 35, 50, 20, 40, 30, 50, 15],days = 8) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [30, 40, 20, 5, 10, 80, 25, 45, 60, 35, 50, 20, 40, 30, 50, 15],days = 8) == 90: {e}')
    
    total += 1
    try:
        result = candidate(weights = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300],days = 3) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300],days = 3) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 7) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 7) == 23: {e}')
    
    total += 1
    try:
        result = candidate(weights = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],days = 4) == 850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],days = 4) == 850: {e}')
    
    total += 1
    try:
        result = candidate(weights = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],days = 5) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],days = 5) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(weights = [150, 300, 450, 600, 750, 900, 1050],days = 3) == 1650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [150, 300, 450, 600, 750, 900, 1050],days = 3) == 1650: {e}')
    
    total += 1
    try:
        result = candidate(weights = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250],days = 5) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250],days = 5) == 750: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],days = 3) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],days = 3) == 210: {e}')
    
    total += 1
    try:
        result = candidate(weights = [3, 5, 8, 4, 2, 10, 1, 7, 6, 9, 11, 13, 15, 12, 14],days = 6) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [3, 5, 8, 4, 2, 10, 1, 7, 6, 9, 11, 13, 15, 12, 14],days = 6) == 26: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],days = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],days = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 3) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 3) == 42: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 5, 9, 14, 20, 25, 30, 35, 40, 45, 50],days = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 5, 9, 14, 20, 25, 30, 35, 40, 45, 50],days = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 15) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 15) == 20: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],days = 2) == 28000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],days = 2) == 28000: {e}')
    
    total += 1
    try:
        result = candidate(weights = [30, 50, 20, 40, 60, 10, 90, 80, 70, 100, 120, 130, 110, 140],days = 6) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [30, 50, 20, 40, 60, 10, 90, 80, 70, 100, 120, 130, 110, 140],days = 6) == 240: {e}')
    
    total += 1
    try:
        result = candidate(weights = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],days = 4) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],days = 4) == 90: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],days = 6) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],days = 6) == 500: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 10, 20, 30, 25, 40, 15, 10, 5, 30],days = 3) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 10, 20, 30, 25, 40, 15, 10, 5, 30],days = 3) == 65: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],days = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],days = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100],days = 5) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100],days = 5) == 500: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 5) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 5) == 28: {e}')
    
    total += 1
    try:
        result = candidate(weights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],days = 30) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],days = 30) == 100: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 5) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 5) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(weights = [47, 2, 20, 7, 2, 19, 23, 30, 6, 12, 9, 4, 30, 26, 8, 7],days = 10) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [47, 2, 20, 7, 2, 19, 23, 30, 6, 12, 9, 4, 30, 26, 8, 7],days = 10) == 47: {e}')
    
    total += 1
    try:
        result = candidate(weights = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],days = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],days = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 15, 10, 15, 10, 15, 10, 15],days = 6) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 15, 10, 15, 10, 15, 10, 15],days = 6) == 25: {e}')
    
    total += 1
    try:
        result = candidate(weights = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],days = 5) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],days = 5) == 155: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 100, 200, 300, 100, 200, 300, 1, 2, 3, 100, 200, 300, 100, 200, 300, 1, 2, 3],days = 7) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 100, 200, 300, 100, 200, 300, 1, 2, 3, 100, 200, 300, 100, 200, 300, 1, 2, 3],days = 7) == 500: {e}')
    
    total += 1
    try:
        result = candidate(weights = [30, 50, 20, 100, 5, 75, 30, 25, 10, 60, 40, 80, 90, 10, 20],days = 7) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [30, 50, 20, 100, 5, 75, 30, 25, 10, 60, 40, 80, 90, 10, 20],days = 7) == 120: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],days = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],days = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(weights = [500, 400, 300, 200, 100, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1],days = 5) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [500, 400, 300, 200, 100, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1],days = 5) == 500: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 5) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 5) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],days = 2) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],days = 2) == 500: {e}')
    
    total += 1
    try:
        result = candidate(weights = [300, 200, 100, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1, 1, 1],days = 7) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [300, 200, 100, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1, 1, 1],days = 7) == 300: {e}')
    
    total += 1
    try:
        result = candidate(weights = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250],days = 10) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250],days = 10) == 500: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 5, 1, 7, 8, 12, 4, 7],days = 6) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 5, 1, 7, 8, 12, 4, 7],days = 6) == 12: {e}')
    
    total += 1
    try:
        result = candidate(weights = [300, 200, 100, 200, 300, 100, 200, 300, 100, 200],days = 4) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [300, 200, 100, 200, 300, 100, 200, 300, 100, 200],days = 4) == 600: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],days = 3) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],days = 3) == 420: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 4) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 4) == 57: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 7) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 7) == 23: {e}')
    
    total += 1
    try:
        result = candidate(weights = [4, 3, 5, 6, 8, 10, 3, 1, 5, 6],days = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [4, 3, 5, 6, 8, 10, 3, 1, 5, 6],days = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(weights = [48, 99, 37, 11, 37, 42, 46, 20, 7, 13, 11, 50, 88, 33, 60, 10],days = 7) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [48, 99, 37, 11, 37, 42, 46, 20, 7, 13, 11, 50, 88, 33, 60, 10],days = 7) == 103: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 3) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 3) == 70: {e}')
    
    total += 1
    try:
        result = candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],days = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],days = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],days = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],days = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 5, 2, 7, 3, 4, 11, 6, 9],days = 4) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 5, 2, 7, 3, 4, 11, 6, 9],days = 4) == 15: {e}')
    
    total += 1
    try:
        result = candidate(weights = [300, 200, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],days = 15) == 470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [300, 200, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],days = 15) == 470: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],days = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],days = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],days = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],days = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],days = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],days = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(weights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],days = 15) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],days = 15) == 100: {e}')
    
    total += 1
    try:
        result = candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],days = 7) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],days = 7) == 100: {e}')
    
    total += 1
    try:
        result = candidate(weights = [25, 47, 42, 77, 72, 46, 42, 44, 63, 59, 51, 55, 53, 91, 93, 95, 97, 99],days = 10) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [25, 47, 42, 77, 72, 46, 42, 44, 63, 59, 51, 55, 53, 91, 93, 95, 97, 99],days = 10) == 149: {e}')
    
    total += 1
    try:
        result = candidate(weights = [91, 41, 54, 63, 17, 5, 58, 57, 98, 46],days = 10) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [91, 41, 54, 63, 17, 5, 58, 57, 98, 46],days = 10) == 98: {e}')
    
    total += 1
    try:
        result = candidate(weights = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],days = 5) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],days = 5) == 32: {e}')
    
    total += 1
    try:
        result = candidate(weights = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450],days = 15) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450],days = 15) == 900: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 10) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 10) == 28: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 2) == 2800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 2) == 2800: {e}')
    
    total += 1
    try:
        result = candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 3) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 3) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(weights = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450],days = 5) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450],days = 5) == 900: {e}')
    
    total += 1
    try:
        result = candidate(weights = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],days = 10) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],days = 10) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(weights = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 10) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 10) == 27: {e}')
    
    total += 1
    try:
        result = candidate(weights = [150, 100, 50, 200, 250, 300, 100, 50, 200, 150],days = 3) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [150, 100, 50, 200, 250, 300, 100, 50, 200, 150],days = 3) == 550: {e}')
    
    total += 1
    try:
        result = candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 9) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 9) == 31: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(weights = [10, 50, 100, 100, 50, 10],days = 2) == 160
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],days = 5) == 15
    assert candidate(weights = [10, 50, 100, 100, 50, 10],days = 3) == 160
    assert candidate(weights = [3, 2, 2, 4, 1, 4],days = 3) == 6
    assert candidate(weights = [1, 2, 3, 1, 1],days = 4) == 3
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],days = 5) == 2
    assert candidate(weights = [5, 5, 5, 5, 5],days = 2) == 15
    assert candidate(weights = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],days = 5) == 83
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],days = 4) == 170
    assert candidate(weights = [4, 3, 2, 5, 8, 2, 3, 5, 6, 1, 2, 4, 3, 7, 5],days = 8) == 10
    assert candidate(weights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],days = 5) == 52
    assert candidate(weights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],days = 6) == 48
    assert candidate(weights = [9, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 3) == 39
    assert candidate(weights = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450],days = 2) == 2250
    assert candidate(weights = [30, 40, 20, 5, 10, 80, 25, 45, 60, 35, 50, 20, 40, 30, 50, 15],days = 8) == 90
    assert candidate(weights = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300],days = 3) == 1200
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 7) == 23
    assert candidate(weights = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],days = 4) == 850
    assert candidate(weights = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],days = 5) == 1000
    assert candidate(weights = [150, 300, 450, 600, 750, 900, 1050],days = 3) == 1650
    assert candidate(weights = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250],days = 5) == 750
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],days = 3) == 210
    assert candidate(weights = [3, 5, 8, 4, 2, 10, 1, 7, 6, 9, 11, 13, 15, 12, 14],days = 6) == 26
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],days = 15) == 7
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 3) == 42
    assert candidate(weights = [1, 5, 9, 14, 20, 25, 30, 35, 40, 45, 50],days = 10) == 50
    assert candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 15) == 20
    assert candidate(weights = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],days = 2) == 28000
    assert candidate(weights = [30, 50, 20, 40, 60, 10, 90, 80, 70, 100, 120, 130, 110, 140],days = 6) == 240
    assert candidate(weights = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],days = 4) == 90
    assert candidate(weights = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],days = 6) == 500
    assert candidate(weights = [5, 10, 20, 30, 25, 40, 15, 10, 5, 30],days = 3) == 65
    assert candidate(weights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],days = 10) == 20
    assert candidate(weights = [100, 200, 300, 100, 200, 300, 100, 200, 300, 100],days = 5) == 500
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 5) == 28
    assert candidate(weights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],days = 30) == 100
    assert candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 5) == 1500
    assert candidate(weights = [47, 2, 20, 7, 2, 19, 23, 30, 6, 12, 9, 4, 30, 26, 8, 7],days = 10) == 47
    assert candidate(weights = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],days = 5) == 30
    assert candidate(weights = [10, 15, 10, 15, 10, 15, 10, 15],days = 6) == 25
    assert candidate(weights = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],days = 5) == 155
    assert candidate(weights = [1, 2, 3, 100, 200, 300, 100, 200, 300, 1, 2, 3, 100, 200, 300, 100, 200, 300, 1, 2, 3],days = 7) == 500
    assert candidate(weights = [30, 50, 20, 100, 5, 75, 30, 25, 10, 60, 40, 80, 90, 10, 20],days = 7) == 120
    assert candidate(weights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],days = 2) == 28
    assert candidate(weights = [500, 400, 300, 200, 100, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1],days = 5) == 500
    assert candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 5) == 1500
    assert candidate(weights = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],days = 2) == 500
    assert candidate(weights = [300, 200, 100, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1, 1, 1],days = 7) == 300
    assert candidate(weights = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250],days = 10) == 500
    assert candidate(weights = [10, 5, 1, 7, 8, 12, 4, 7],days = 6) == 12
    assert candidate(weights = [300, 200, 100, 200, 300, 100, 200, 300, 100, 200],days = 4) == 600
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],days = 3) == 420
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 4) == 57
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],days = 7) == 23
    assert candidate(weights = [4, 3, 5, 6, 8, 10, 3, 1, 5, 6],days = 5) == 13
    assert candidate(weights = [48, 99, 37, 11, 37, 42, 46, 20, 7, 13, 11, 50, 88, 33, 60, 10],days = 7) == 103
    assert candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 3) == 70
    assert candidate(weights = [9, 8, 7, 6, 5, 4, 3, 2, 1],days = 5) == 11
    assert candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 5) == 40
    assert candidate(weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],days = 15) == 10
    assert candidate(weights = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],days = 10) == 3
    assert candidate(weights = [10, 5, 2, 7, 3, 4, 11, 6, 9],days = 4) == 15
    assert candidate(weights = [300, 200, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],days = 15) == 470
    assert candidate(weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],days = 20) == 1
    assert candidate(weights = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],days = 10) == 6
    assert candidate(weights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],days = 10) == 15
    assert candidate(weights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],days = 15) == 100
    assert candidate(weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],days = 7) == 100
    assert candidate(weights = [25, 47, 42, 77, 72, 46, 42, 44, 63, 59, 51, 55, 53, 91, 93, 95, 97, 99],days = 10) == 149
    assert candidate(weights = [91, 41, 54, 63, 17, 5, 58, 57, 98, 46],days = 10) == 98
    assert candidate(weights = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],days = 5) == 32
    assert candidate(weights = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450],days = 15) == 900
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 10) == 28
    assert candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 2) == 2800
    assert candidate(weights = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],days = 3) == 2100
    assert candidate(weights = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450],days = 5) == 900
    assert candidate(weights = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],days = 10) == 1000
    assert candidate(weights = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 10) == 27
    assert candidate(weights = [150, 100, 50, 200, 250, 300, 100, 50, 200, 150],days = 3) == 550
    assert candidate(weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],days = 9) == 31


