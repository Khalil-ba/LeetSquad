def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1],limit = 3,goal = -4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1],limit = 3,goal = -4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],limit = 1,goal = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],limit = 1,goal = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -10, 9, 1],limit = 100,goal = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -10, 9, 1],limit = 100,goal = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0],limit = 1,goal = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0],limit = 1,goal = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],limit = 5,goal = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],limit = 5,goal = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2],limit = 2,goal = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2],limit = 2,goal = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1],limit = 1,goal = -9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1],limit = 1,goal = -9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -5, -5],limit = 5,goal = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -5, -5],limit = 5,goal = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],limit = 5,goal = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],limit = 5,goal = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30],limit = 15,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30],limit = 15,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, -250000, 125000, -62500, 31250, -15625],limit = 100000,goal = 1000000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, -250000, 125000, -62500, 31250, -15625],limit = 100000,goal = 1000000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000],limit = 100000,goal = 1500000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000],limit = 100000,goal = 1500000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, -999999, 999998, -999998, 999997, -999997],limit = 1000000,goal = -1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, -999999, 999998, -999998, 999997, -999997],limit = 1000000,goal = -1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 500000, -500000],limit = 1000000,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 500000, -500000],limit = 1000000,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 2,goal = -15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 2,goal = -15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = -10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = -10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],limit = 10,goal = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],limit = 10,goal = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5],limit = 2,goal = -10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5],limit = 2,goal = -10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 200, -200, 300, -300],limit = 100,goal = -1500) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 200, -200, 300, -300],limit = 100,goal = -1500) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 3,goal = 0) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 3,goal = 0) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],limit = 1000000,goal = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],limit = 1000000,goal = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5],limit = 5,goal = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5],limit = 5,goal = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999999, 999999],limit = 1000000,goal = -2999997) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999999, 999999],limit = 1000000,goal = -2999997) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, -15, 20, -25, 30, -35, 40, -45, 50],limit = 10,goal = 100) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, -15, 20, -25, 30, -35, 40, -45, 50],limit = 10,goal = 100) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, -999999, 999999, -999999, 999999, -999999],limit = 1000000,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, -999999, 999999, -999999, 999999, -999999],limit = 1000000,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1],limit = 3,goal = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1],limit = 3,goal = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 1,goal = -20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 1,goal = -20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 1,goal = 55) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 1,goal = 55) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 1000000],limit = 1000000,goal = 3000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 1000000],limit = 1000000,goal = 3000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 3,goal = -50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 3,goal = -50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, -654321, 111111, -222222, 333333, -444444],limit = 500000,goal = -1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, -654321, 111111, -222222, 333333, -444444],limit = 500000,goal = -1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999998, 999997, 999996],limit = 999999,goal = 3999990) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999998, 999997, 999996],limit = 999999,goal = 3999990) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 500000],limit = 1000000,goal = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 500000],limit = 1000000,goal = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000],limit = 1000,goal = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000],limit = 1000,goal = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 10,goal = 55) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 10,goal = 55) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5],limit = 10,goal = -15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5],limit = 10,goal = -15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30],limit = 5,goal = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30],limit = 5,goal = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000],limit = 100000,goal = 1000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000],limit = 100000,goal = 1000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 1,goal = -5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 1,goal = -5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],limit = 1,goal = -15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],limit = 1,goal = -15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, -2000000, -3000000],limit = 1000000,goal = -10000000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, -2000000, -3000000],limit = 1000000,goal = -10000000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25],limit = 100,goal = 200) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25],limit = 100,goal = 200) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 50,goal = 500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 50,goal = 500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],limit = 5,goal = -10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],limit = 5,goal = -10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50],limit = 50,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50],limit = 50,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 500000],limit = 1000000,goal = 1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 500000],limit = 1000000,goal = 1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, -123456, 234567, -234567],limit = 100000,goal = -345678) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, -123456, 234567, -234567],limit = 100000,goal = -345678) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],limit = 3,goal = -15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],limit = 3,goal = -15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, -654321, 789012, -321098],limit = 100000,goal = 500000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, -654321, 789012, -321098],limit = 100000,goal = 500000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 100, -100, 100],limit = 100,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 100, -100, 100],limit = 100,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100000, 100000, -100000, 100000, -100000],limit = 100000,goal = 50000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100000, 100000, -100000, 100000, -100000],limit = 100000,goal = 50000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 500000, -500000],limit = 100000,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 500000, -500000],limit = 100000,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],limit = 100,goal = 1500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],limit = 100,goal = 1500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 5,goal = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 5,goal = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 1,goal = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 1,goal = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100000, 50000, 25000, -12500, 6250],limit = 10000,goal = -100000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100000, 50000, 25000, -12500, 6250],limit = 10000,goal = -100000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 100000],limit = 100000,goal = 600000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 100000],limit = 100000,goal = 600000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 2000, -2000, 3000],limit = 1000,goal = 5000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 2000, -2000, 3000],limit = 1000,goal = 5000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5],limit = 5,goal = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5],limit = 5,goal = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 1,goal = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 1,goal = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 5, -5, 5, -5],limit = 5,goal = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 5, -5, 5, -5],limit = 5,goal = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000],limit = 500000,goal = 2000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000],limit = 500000,goal = 2000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 10,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 10,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 5,goal = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 5,goal = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],limit = 10,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],limit = 10,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 1,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 1,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-999999, -999999, -999999],limit = 1000000,goal = 2999997) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-999999, -999999, -999999],limit = 1000000,goal = 2999997) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 1,goal = -15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 1,goal = -15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 3,goal = 0) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 3,goal = 0) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1],limit = 3,goal = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1],limit = 3,goal = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 2,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 2,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1],limit = 1,goal = -1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1],limit = 1,goal = -1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 50,goal = 0) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 50,goal = 0) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 5,goal = 55) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 5,goal = 55) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],limit = 2,goal = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],limit = 2,goal = 20) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 3, 2, -4, 1],limit = 5,goal = -10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 3, 2, -4, 1],limit = 5,goal = -10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, -999999, 999999, -999999, 999999],limit = 1000000,goal = 4999995) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, -999999, 999999, -999999, 999999],limit = 1000000,goal = 4999995) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 100, -100, 100, -100],limit = 50,goal = 0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 100, -100, 100, -100],limit = 50,goal = 0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],limit = 2,goal = 0) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],limit = 2,goal = 0) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 3,goal = 55) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 3,goal = 55) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000],limit = 500000,goal = 500000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000],limit = 500000,goal = 500000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 5,goal = -55) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 5,goal = -55) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1],limit = 1,goal = -1000000) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1],limit = 1,goal = -1000000) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 2,goal = -30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 2,goal = -30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 3,goal = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 3,goal = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-999999, -999999, -999999, -999999, -999999],limit = 1000000,goal = -5000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-999999, -999999, -999999, -999999, -999999],limit = 1000000,goal = -5000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5],limit = 5,goal = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5],limit = 5,goal = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999999, 999999, 999999, 999999],limit = 1000000,goal = 5000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999999, 999999, 999999, 999999],limit = 1000000,goal = 5000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, -1000000, -1000000, -1000000, -1000000],limit = 1000000,goal = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, -1000000, -1000000, -1000000, -1000000],limit = 1000000,goal = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 10,goal = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 10,goal = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, -234567, 345678, -456789, 567890],limit = 100000,goal = 123456789) == 1232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, -234567, 345678, -456789, 567890],limit = 100000,goal = 123456789) == 1232: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-999999, -999998, -999997, -999996],limit = 999999,goal = -3999990) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-999999, -999998, -999997, -999996],limit = 999999,goal = -3999990) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40],limit = 15,goal = 0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40],limit = 15,goal = 0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 10,goal = -55) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 10,goal = -55) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000],limit = 1000000,goal = 10000000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000],limit = 1000000,goal = 10000000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500000, 500000, 500000, 500000],limit = 1000000,goal = 500000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500000, 500000, 500000, 500000],limit = 1000000,goal = 500000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],limit = 1000000,goal = 10000000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],limit = 1000000,goal = 10000000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],limit = 100,goal = 500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],limit = 100,goal = 500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 2,goal = -20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 2,goal = -20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 5,goal = 0) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 5,goal = 0) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],limit = 10,goal = 150) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],limit = 10,goal = 150) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],limit = 5,goal = 150) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],limit = 5,goal = 150) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, -1, 1],limit = 3,goal = -4) == 2
    assert candidate(nums = [1, 2, 3],limit = 1,goal = 6) == 0
    assert candidate(nums = [1, -10, 9, 1],limit = 100,goal = 0) == 1
    assert candidate(nums = [0, 0, 0],limit = 1,goal = 3) == 3
    assert candidate(nums = [0, 0, 0, 0],limit = 5,goal = 10) == 2
    assert candidate(nums = [2, 2, 2],limit = 2,goal = 6) == 0
    assert candidate(nums = [-3, -2, -1],limit = 1,goal = -9) == 3
    assert candidate(nums = [-5, -5, -5],limit = 5,goal = 15) == 6
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],limit = 5,goal = 50) == 10
    assert candidate(nums = [10, -10, 20, -20, 30, -30],limit = 15,goal = 0) == 0
    assert candidate(nums = [500000, -250000, 125000, -62500, 31250, -15625],limit = 100000,goal = 1000000) == 7
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000],limit = 100000,goal = 1500000) == 0
    assert candidate(nums = [999999, -999999, 999998, -999998, 999997, -999997],limit = 1000000,goal = -1000000) == 1
    assert candidate(nums = [1000000, -1000000, 500000, -500000],limit = 1000000,goal = 0) == 0
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 2,goal = -15) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = -10) == 20
    assert candidate(nums = [5, 10, 15, 20, 25],limit = 10,goal = 100) == 3
    assert candidate(nums = [1, -2, 3, -4, 5],limit = 2,goal = -10) == 7
    assert candidate(nums = [100, -100, 200, -200, 300, -300],limit = 100,goal = -1500) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 3,goal = 0) == 19
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],limit = 1000000,goal = 0) == 5
    assert candidate(nums = [5, -5, 5, -5, 5, -5],limit = 5,goal = 10) == 2
    assert candidate(nums = [999999, 999999, 999999],limit = 1000000,goal = -2999997) == 6
    assert candidate(nums = [5, 10, -15, 20, -25, 30, -35, 40, -45, 50],limit = 10,goal = 100) == 7
    assert candidate(nums = [999999, -999999, 999999, -999999, 999999, -999999],limit = 1000000,goal = 0) == 0
    assert candidate(nums = [-5, -4, -3, -2, -1],limit = 3,goal = 15) == 10
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 1,goal = -20) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 1,goal = 55) == 0
    assert candidate(nums = [1000000, -1000000, 1000000],limit = 1000000,goal = 3000000) == 2
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 3,goal = -50) == 2
    assert candidate(nums = [123456, -654321, 111111, -222222, 333333, -444444],limit = 500000,goal = -1000000) == 1
    assert candidate(nums = [999999, 999998, 999997, 999996],limit = 999999,goal = 3999990) == 0
    assert candidate(nums = [1000000, -1000000, 500000],limit = 1000000,goal = 0) == 1
    assert candidate(nums = [1000, -1000, 1000, -1000],limit = 1000,goal = 1000) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 10,goal = 55) == 0
    assert candidate(nums = [5, -5, 5, -5, 5],limit = 10,goal = -15) == 2
    assert candidate(nums = [10, -10, 20, -20, 30, -30],limit = 5,goal = 15) == 3
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000],limit = 100000,goal = 1000000) == 5
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 1,goal = -5) == 5
    assert candidate(nums = [1, 2, 3, 4, 5],limit = 1,goal = -15) == 30
    assert candidate(nums = [-1000000, -2000000, -3000000],limit = 1000000,goal = -10000000) == 4
    assert candidate(nums = [100, -50, 25],limit = 100,goal = 200) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 15) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 50,goal = 500) == 1
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],limit = 5,goal = -10) == 2
    assert candidate(nums = [100, -100, 50, -50],limit = 50,goal = 0) == 0
    assert candidate(nums = [1000000, -1000000, 500000],limit = 1000000,goal = 1000000) == 1
    assert candidate(nums = [123456, -123456, 234567, -234567],limit = 100000,goal = -345678) == 4
    assert candidate(nums = [-1, -2, -3, -4, -5],limit = 3,goal = -15) == 0
    assert candidate(nums = [123456, -654321, 789012, -321098],limit = 100000,goal = 500000) == 6
    assert candidate(nums = [-100, 100, -100, 100],limit = 100,goal = 0) == 0
    assert candidate(nums = [-100000, 100000, -100000, 100000, -100000],limit = 100000,goal = 50000) == 2
    assert candidate(nums = [1000000, -1000000, 500000, -500000],limit = 100000,goal = 0) == 0
    assert candidate(nums = [100, 200, 300, 400, 500],limit = 100,goal = 1500) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 5,goal = 50) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 1,goal = 5) == 5
    assert candidate(nums = [-100000, 50000, 25000, -12500, 6250],limit = 10000,goal = -100000) == 7
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000],limit = 100000,goal = 600000) == 1
    assert candidate(nums = [1000, -1000, 2000, -2000, 3000],limit = 1000,goal = 5000) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 10) == 0
    assert candidate(nums = [5, -5, 5, -5],limit = 5,goal = 10) == 2
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 1,goal = 1) == 1
    assert candidate(nums = [-5, 5, -5, 5, -5],limit = 5,goal = 0) == 1
    assert candidate(nums = [1000000],limit = 500000,goal = 2000000) == 2
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 10,goal = 0) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 5,goal = 10) == 0
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],limit = 10,goal = 0) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 1,goal = 0) == 0
    assert candidate(nums = [-999999, -999999, -999999],limit = 1000000,goal = 2999997) == 6
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 1,goal = -15) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 3,goal = 0) == 19
    assert candidate(nums = [-1, -1, -1, -1, -1],limit = 3,goal = 5) == 4
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],limit = 2,goal = 0) == 0
    assert candidate(nums = [1, -1, 1, -1, 1],limit = 1,goal = -1) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],limit = 50,goal = 0) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 5,goal = 55) == 0
    assert candidate(nums = [1, 2, 3, 4, 5],limit = 2,goal = 20) == 3
    assert candidate(nums = [-5, 3, 2, -4, 1],limit = 5,goal = -10) == 2
    assert candidate(nums = [999999, -999999, 999999, -999999, 999999],limit = 1000000,goal = 4999995) == 4
    assert candidate(nums = [-100, 100, -100, 100, -100],limit = 50,goal = 0) == 2
    assert candidate(nums = [1, 2, 3, 4, 5],limit = 2,goal = 0) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 3,goal = 55) == 0
    assert candidate(nums = [1000000, 1000000, 1000000],limit = 500000,goal = 500000) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 5,goal = -55) == 0
    assert candidate(nums = [-1, 0, 1],limit = 1,goal = -1000000) == 1000000
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 2,goal = -30) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 3,goal = 20) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 5) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 1,goal = 20) == 10
    assert candidate(nums = [-999999, -999999, -999999, -999999, -999999],limit = 1000000,goal = -5000000) == 1
    assert candidate(nums = [1, -2, 3, -4, 5],limit = 5,goal = 0) == 1
    assert candidate(nums = [999999, 999999, 999999, 999999, 999999],limit = 1000000,goal = 5000000) == 1
    assert candidate(nums = [-1000000, -1000000, -1000000, -1000000, -1000000],limit = 1000000,goal = 0) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],limit = 10,goal = 5) == 1
    assert candidate(nums = [123456, -234567, 345678, -456789, 567890],limit = 100000,goal = 123456789) == 1232
    assert candidate(nums = [-999999, -999998, -999997, -999996],limit = 999999,goal = -3999990) == 0
    assert candidate(nums = [-10, 20, -30, 40],limit = 15,goal = 0) == 2
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],limit = 10,goal = -55) == 0
    assert candidate(nums = [1000000, 2000000, 3000000],limit = 1000000,goal = 10000000) == 4
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000],limit = 1000000,goal = 500000) == 2
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],limit = 1000000,goal = 10000000) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],limit = 100,goal = 500) == 5
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],limit = 2,goal = -20) == 5
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],limit = 5,goal = 0) == 11
    assert candidate(nums = [-10, -20, -30, -40, -50],limit = 10,goal = 150) == 30
    assert candidate(nums = [10, 20, 30, 40, 50],limit = 5,goal = 150) == 0


