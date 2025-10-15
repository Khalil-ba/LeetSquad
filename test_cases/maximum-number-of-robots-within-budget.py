def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(chargeTimes = [7, 1, 3, 9, 2],runningCosts = [8, 6, 4, 5, 0],budget = 30) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [7, 1, 3, 9, 2],runningCosts = [8, 6, 4, 5, 0],budget = 30) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1],runningCosts = [100000, 100000, 100000, 100000, 100000],budget = 500000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1],runningCosts = [100000, 100000, 100000, 100000, 100000],budget = 500000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [7, 7, 7, 7],runningCosts = [1, 1, 1, 1],budget = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [7, 7, 7, 7],runningCosts = [1, 1, 1, 1],budget = 20) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [100000, 100000, 100000, 100000, 100000],budget = 1000000000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [100000, 100000, 100000, 100000, 100000],budget = 1000000000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5],runningCosts = [1, 2, 3, 4, 5],budget = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5],runningCosts = [1, 2, 3, 4, 5],budget = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100000, 100000, 100000],runningCosts = [1, 1, 1],budget = 300001) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100000, 100000, 100000],runningCosts = [1, 1, 1],budget = 300001) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 11, 2, 7],runningCosts = [3, 9, 1, 10],budget = 30) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 11, 2, 7],runningCosts = [3, 9, 1, 10],budget = 30) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [11, 12, 19],runningCosts = [10, 8, 7],budget = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [11, 12, 19],runningCosts = [10, 8, 7],budget = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3],runningCosts = [10, 20, 30],budget = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3],runningCosts = [10, 20, 30],budget = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5],runningCosts = [5, 4, 3, 2, 1],budget = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5],runningCosts = [5, 4, 3, 2, 1],budget = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 5, 5, 5, 5],runningCosts = [1, 1, 1, 1, 1],budget = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 5, 5, 5, 5],runningCosts = [1, 1, 1, 1, 1],budget = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [3, 6, 1, 3, 4],runningCosts = [2, 1, 3, 4, 5],budget = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [3, 6, 1, 3, 4],runningCosts = [2, 1, 3, 4, 5],budget = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100000, 100000, 100000],runningCosts = [100000, 100000, 100000],budget = 100000000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100000, 100000, 100000],runningCosts = [100000, 100000, 100000],budget = 100000000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 3, 2, 4, 5, 3, 2, 1, 4, 5],runningCosts = [5, 1, 4, 2, 3, 5, 1, 4, 2, 3],budget = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 3, 2, 4, 5, 3, 2, 1, 4, 5],runningCosts = [5, 1, 4, 2, 3, 5, 1, 4, 2, 3],budget = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 30) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 30) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],budget = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],budget = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [20, 10, 15, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],budget = 300) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [20, 10, 15, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],budget = 300) == 7: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [3, 6, 1, 3, 4, 5, 7, 8, 9, 10, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],runningCosts = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [3, 6, 1, 3, 4, 5, 7, 8, 9, 10, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],runningCosts = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 40) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 40) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 300) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 300) == 10: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 1000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 1000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],runningCosts = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 500) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],runningCosts = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 500) == 9: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [3, 7, 9, 8, 5, 6, 2, 4],runningCosts = [10, 8, 5, 3, 9, 6, 7, 2],budget = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [3, 7, 9, 8, 5, 6, 2, 4],runningCosts = [10, 8, 5, 3, 9, 6, 7, 2],budget = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 20, 30, 40, 50],runningCosts = [5, 15, 25, 35, 45],budget = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 20, 30, 40, 50],runningCosts = [5, 15, 25, 35, 45],budget = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 15, 20, 25, 30],runningCosts = [1, 2, 3, 4, 5],budget = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 15, 20, 25, 30],runningCosts = [1, 2, 3, 4, 5],budget = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],budget = 500005) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],budget = 500005) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],runningCosts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 500) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],runningCosts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 500) == 9: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100, 90, 80, 70, 60],budget = 250) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100, 90, 80, 70, 60],budget = 250) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100, 200, 300, 400, 500],runningCosts = [5, 5, 5, 5, 5],budget = 1500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100, 200, 300, 400, 500],runningCosts = [5, 5, 5, 5, 5],budget = 1500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [3, 6, 1, 3, 4, 9, 12, 8, 10, 5],runningCosts = [2, 1, 3, 4, 5, 1, 2, 3, 4, 5],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [3, 6, 1, 3, 4, 9, 12, 8, 10, 5],runningCosts = [2, 1, 3, 4, 5, 1, 2, 3, 4, 5],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5],runningCosts = [10000, 10000, 10000, 10000, 10000],budget = 50000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5],runningCosts = [10000, 10000, 10000, 10000, 10000],budget = 50000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 500) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 500) == 9: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],runningCosts = [5, 9, 2, 6, 5, 3, 5, 9, 1, 4, 1],budget = 150) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],runningCosts = [5, 9, 2, 6, 5, 3, 5, 9, 1, 4, 1],budget = 150) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10000, 20000, 30000, 40000, 50000],runningCosts = [1000, 2000, 3000, 4000, 5000],budget = 100000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10000, 20000, 30000, 40000, 50000],runningCosts = [1000, 2000, 3000, 4000, 5000],budget = 100000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [1, 1, 1, 1, 1],budget = 500005) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [1, 1, 1, 1, 1],budget = 500005) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],runningCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],budget = 1000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],runningCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],budget = 1000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 10000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 10000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 10, 100, 1000, 10000],runningCosts = [1, 10, 100, 1000, 10000],budget = 111111) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 10, 100, 1000, 10000],runningCosts = [1, 10, 100, 1000, 10000],budget = 111111) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],budget = 1000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],budget = 1000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 55) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 55) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5],budget = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5],budget = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100, 200, 300, 400, 500],runningCosts = [5, 10, 15, 20, 25],budget = 1000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100, 200, 300, 400, 500],runningCosts = [5, 10, 15, 20, 25],budget = 1000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 25) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 25) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 45) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 45) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [50, 25, 75, 100, 125, 200, 150, 225, 300, 350],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 1000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [50, 25, 75, 100, 125, 200, 150, 225, 300, 350],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 1000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 5, 1, 5, 1, 5],runningCosts = [1, 1, 1, 1, 1, 1],budget = 12) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 5, 1, 5, 1, 5],runningCosts = [1, 1, 1, 1, 1, 1],budget = 12) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 1000000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 1000000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 15, 10, 20, 25, 30, 35, 40, 45, 50],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 15, 10, 20, 25, 30, 35, 40, 45, 50],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [50, 40, 30, 20, 10],runningCosts = [1, 2, 3, 4, 5],budget = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [50, 40, 30, 20, 10],runningCosts = [1, 2, 3, 4, 5],budget = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 45) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 45) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [50, 40, 30, 20, 10],runningCosts = [1, 2, 3, 4, 5],budget = 200) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [50, 40, 30, 20, 10],runningCosts = [1, 2, 3, 4, 5],budget = 200) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [100000, 100000, 100000, 100000, 100000],budget = 500000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [100000, 100000, 100000, 100000, 100000],budget = 500000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100, 200, 300, 400, 500],runningCosts = [50, 40, 30, 20, 10],budget = 1000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100, 200, 300, 400, 500],runningCosts = [50, 40, 30, 20, 10],budget = 1000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],budget = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],budget = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 5000010) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 5000010) == 10: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 20, 30, 40, 50],runningCosts = [1, 2, 3, 4, 5],budget = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 20, 30, 40, 50],runningCosts = [1, 2, 3, 4, 5],budget = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6],budget = 300) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6],budget = 300) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],budget = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],budget = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100, 200, 300, 400, 500, 600],runningCosts = [1, 2, 3, 4, 5, 6],budget = 1500) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100, 200, 300, 400, 500, 600],runningCosts = [1, 2, 3, 4, 5, 6],budget = 1500) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [9, 7, 5, 11, 13, 2, 8],runningCosts = [4, 8, 12, 16, 20, 24, 28],budget = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [9, 7, 5, 11, 13, 2, 8],runningCosts = [4, 8, 12, 16, 20, 24, 28],budget = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 1500) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 1500) == 13: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 3, 2, 5, 4],runningCosts = [5, 3, 6, 2, 4],budget = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 3, 2, 5, 4],runningCosts = [5, 3, 6, 2, 4],budget = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 200) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 200) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70],runningCosts = [1, 2, 3, 4, 5, 6, 7],budget = 200) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70],runningCosts = [1, 2, 3, 4, 5, 6, 7],budget = 200) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [50, 40, 30, 20, 10],runningCosts = [1, 2, 3, 4, 5],budget = 300) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [50, 40, 30, 20, 10],runningCosts = [1, 2, 3, 4, 5],budget = 300) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 150) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 150) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 1000000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 1000000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100000, 90000, 80000, 70000, 60000],runningCosts = [10000, 9000, 8000, 7000, 6000],budget = 10000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100000, 90000, 80000, 70000, 60000],runningCosts = [10000, 9000, 8000, 7000, 6000],budget = 10000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 250) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 250) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 200) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 200) == 10: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],runningCosts = [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3],budget = 200) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],runningCosts = [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3],budget = 200) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [20, 18, 15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [20, 18, 15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 100) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 100) == 7: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [1, 1, 1, 1, 1],budget = 500000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [1, 1, 1, 1, 1],budget = 500000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1000, 2000, 3000, 4000, 5000],runningCosts = [5, 5, 5, 5, 5],budget = 10000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1000, 2000, 3000, 4000, 5000],runningCosts = [5, 5, 5, 5, 5],budget = 10000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 300) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 300) == 16: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 500) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 500) == 10: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],runningCosts = [9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3],budget = 200) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],runningCosts = [9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3],budget = 200) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],budget = 250) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],budget = 250) == 7: {e}')
    
    total += 1
    try:
        result = candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 50) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(chargeTimes = [7, 1, 3, 9, 2],runningCosts = [8, 6, 4, 5, 0],budget = 30) == 2
    assert candidate(chargeTimes = [1, 1, 1, 1, 1],runningCosts = [100000, 100000, 100000, 100000, 100000],budget = 500000) == 2
    assert candidate(chargeTimes = [7, 7, 7, 7],runningCosts = [1, 1, 1, 1],budget = 20) == 3
    assert candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [100000, 100000, 100000, 100000, 100000],budget = 1000000000000) == 5
    assert candidate(chargeTimes = [1, 2, 3, 4, 5],runningCosts = [1, 2, 3, 4, 5],budget = 20) == 2
    assert candidate(chargeTimes = [100000, 100000, 100000],runningCosts = [1, 1, 1],budget = 300001) == 3
    assert candidate(chargeTimes = [5, 11, 2, 7],runningCosts = [3, 9, 1, 10],budget = 30) == 2
    assert candidate(chargeTimes = [11, 12, 19],runningCosts = [10, 8, 7],budget = 19) == 0
    assert candidate(chargeTimes = [1, 2, 3],runningCosts = [10, 20, 30],budget = 100) == 2
    assert candidate(chargeTimes = [1, 2, 3, 4, 5],runningCosts = [5, 4, 3, 2, 1],budget = 20) == 2
    assert candidate(chargeTimes = [5, 5, 5, 5, 5],runningCosts = [1, 1, 1, 1, 1],budget = 15) == 3
    assert candidate(chargeTimes = [3, 6, 1, 3, 4],runningCosts = [2, 1, 3, 4, 5],budget = 25) == 3
    assert candidate(chargeTimes = [100000, 100000, 100000],runningCosts = [100000, 100000, 100000],budget = 100000000000) == 3
    assert candidate(chargeTimes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 500) == 4
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 4
    assert candidate(chargeTimes = [1, 3, 2, 4, 5, 3, 2, 1, 4, 5],runningCosts = [5, 1, 4, 2, 3, 5, 1, 4, 2, 3],budget = 25) == 3
    assert candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 20) == 4
    assert candidate(chargeTimes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 30) == 4
    assert candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],budget = 100) == 4
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 2
    assert candidate(chargeTimes = [20, 10, 15, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],budget = 300) == 7
    assert candidate(chargeTimes = [3, 6, 1, 3, 4, 5, 7, 8, 9, 10, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],runningCosts = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],budget = 100) == 5
    assert candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 40) == 3
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 20) == 4
    assert candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 300) == 10
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 1000) == 10
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],runningCosts = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 500) == 9
    assert candidate(chargeTimes = [3, 7, 9, 8, 5, 6, 2, 4],runningCosts = [10, 8, 5, 3, 9, 6, 7, 2],budget = 50) == 2
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 100) == 5
    assert candidate(chargeTimes = [10, 20, 30, 40, 50],runningCosts = [5, 15, 25, 35, 45],budget = 500) == 4
    assert candidate(chargeTimes = [10, 15, 20, 25, 30],runningCosts = [1, 2, 3, 4, 5],budget = 50) == 3
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],budget = 500005) == 2
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],runningCosts = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 500) == 9
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 4
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 100, 90, 80, 70, 60],budget = 250) == 3
    assert candidate(chargeTimes = [100, 200, 300, 400, 500],runningCosts = [5, 5, 5, 5, 5],budget = 1500) == 5
    assert candidate(chargeTimes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 30) == 5
    assert candidate(chargeTimes = [3, 6, 1, 3, 4, 9, 12, 8, 10, 5],runningCosts = [2, 1, 3, 4, 5, 1, 2, 3, 4, 5],budget = 100) == 5
    assert candidate(chargeTimes = [1, 2, 3, 4, 5],runningCosts = [10000, 10000, 10000, 10000, 10000],budget = 50000) == 2
    assert candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 500) == 9
    assert candidate(chargeTimes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],runningCosts = [5, 9, 2, 6, 5, 3, 5, 9, 1, 4, 1],budget = 150) == 6
    assert candidate(chargeTimes = [10000, 20000, 30000, 40000, 50000],runningCosts = [1000, 2000, 3000, 4000, 5000],budget = 100000) == 4
    assert candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [1, 1, 1, 1, 1],budget = 500005) == 5
    assert candidate(chargeTimes = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],runningCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],budget = 1000) == 6
    assert candidate(chargeTimes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 10000) == 10
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 100) == 5
    assert candidate(chargeTimes = [1, 10, 100, 1000, 10000],runningCosts = [1, 10, 100, 1000, 10000],budget = 111111) == 5
    assert candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 50) == 4
    assert candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],budget = 1000) == 9
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 55) == 4
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 5) == 2
    assert candidate(chargeTimes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5],budget = 100) == 3
    assert candidate(chargeTimes = [100, 200, 300, 400, 500],runningCosts = [5, 10, 15, 20, 25],budget = 1000) == 5
    assert candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 25) == 4
    assert candidate(chargeTimes = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 45) == 3
    assert candidate(chargeTimes = [50, 25, 75, 100, 125, 200, 150, 225, 300, 350],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 1000) == 5
    assert candidate(chargeTimes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 2
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 5) == 2
    assert candidate(chargeTimes = [1, 5, 1, 5, 1, 5],runningCosts = [1, 1, 1, 1, 1, 1],budget = 12) == 2
    assert candidate(chargeTimes = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 1000000) == 10
    assert candidate(chargeTimes = [5, 15, 10, 20, 25, 30, 35, 40, 45, 50],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 100) == 5
    assert candidate(chargeTimes = [50, 40, 30, 20, 10],runningCosts = [1, 2, 3, 4, 5],budget = 100) == 4
    assert candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 45) == 3
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 3
    assert candidate(chargeTimes = [50, 40, 30, 20, 10],runningCosts = [1, 2, 3, 4, 5],budget = 200) == 5
    assert candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [100000, 100000, 100000, 100000, 100000],budget = 500000) == 2
    assert candidate(chargeTimes = [100, 200, 300, 400, 500],runningCosts = [50, 40, 30, 20, 10],budget = 1000) == 4
    assert candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 100) == 5
    assert candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],budget = 500) == 4
    assert candidate(chargeTimes = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 5000010) == 10
    assert candidate(chargeTimes = [10, 20, 30, 40, 50],runningCosts = [1, 2, 3, 4, 5],budget = 100) == 4
    assert candidate(chargeTimes = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6],budget = 300) == 2
    assert candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],budget = 50) == 3
    assert candidate(chargeTimes = [100, 200, 300, 400, 500, 600],runningCosts = [1, 2, 3, 4, 5, 6],budget = 1500) == 6
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 100) == 5
    assert candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],budget = 100) == 5
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 15) == 3
    assert candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 500) == 4
    assert candidate(chargeTimes = [9, 7, 5, 11, 13, 2, 8],runningCosts = [4, 8, 12, 16, 20, 24, 28],budget = 100) == 3
    assert candidate(chargeTimes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 1500) == 13
    assert candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],runningCosts = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 50) == 3
    assert candidate(chargeTimes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 50) == 4
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 100) == 5
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 10) == 3
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 20) == 4
    assert candidate(chargeTimes = [1, 3, 2, 5, 4],runningCosts = [5, 3, 6, 2, 4],budget = 20) == 2
    assert candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 100) == 5
    assert candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 200) == 6
    assert candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70],runningCosts = [1, 2, 3, 4, 5, 6, 7],budget = 200) == 6
    assert candidate(chargeTimes = [50, 40, 30, 20, 10],runningCosts = [1, 2, 3, 4, 5],budget = 300) == 5
    assert candidate(chargeTimes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],runningCosts = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],budget = 150) == 6
    assert candidate(chargeTimes = [9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9],budget = 30) == 3
    assert candidate(chargeTimes = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 1000000) == 10
    assert candidate(chargeTimes = [100000, 90000, 80000, 70000, 60000],runningCosts = [10000, 9000, 8000, 7000, 6000],budget = 10000000) == 5
    assert candidate(chargeTimes = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 250) == 3
    assert candidate(chargeTimes = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 200) == 10
    assert candidate(chargeTimes = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],runningCosts = [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3],budget = 200) == 5
    assert candidate(chargeTimes = [20, 18, 15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],runningCosts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],budget = 100) == 4
    assert candidate(chargeTimes = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 100) == 7
    assert candidate(chargeTimes = [100000, 100000, 100000, 100000, 100000],runningCosts = [1, 1, 1, 1, 1],budget = 500000) == 5
    assert candidate(chargeTimes = [1000, 2000, 3000, 4000, 5000],runningCosts = [5, 5, 5, 5, 5],budget = 10000) == 5
    assert candidate(chargeTimes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 300) == 16
    assert candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],budget = 500) == 10
    assert candidate(chargeTimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],runningCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],budget = 500) == 4
    assert candidate(chargeTimes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 150) == 5
    assert candidate(chargeTimes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],runningCosts = [9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3],budget = 200) == 6
    assert candidate(chargeTimes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],budget = 250) == 7
    assert candidate(chargeTimes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],runningCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],budget = 50) == 4


