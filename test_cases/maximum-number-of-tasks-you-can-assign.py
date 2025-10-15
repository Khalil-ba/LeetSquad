def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300],workers = [50, 150, 250, 350],pills = 2,strength = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300],workers = [50, 150, 250, 350],pills = 2,strength = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30],workers = [30, 40, 50],pills = 0,strength = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30],workers = [30, 40, 50],pills = 0,strength = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 15, 30],workers = [0, 10, 10, 10, 10],pills = 3,strength = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 15, 30],workers = [0, 10, 10, 10, 10],pills = 3,strength = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300],workers = [100, 100, 100, 100, 100],pills = 2,strength = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300],workers = [100, 100, 100, 100, 100],pills = 2,strength = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 5,strength = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 5,strength = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 0,strength = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 0,strength = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5],workers = [1, 1, 1, 1],pills = 4,strength = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5],workers = [1, 1, 1, 1],pills = 4,strength = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300],workers = [150, 250, 350],pills = 1,strength = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300],workers = [150, 250, 350],pills = 1,strength = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 0,strength = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 0,strength = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300],workers = [150, 250, 350],pills = 2,strength = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300],workers = [150, 250, 350],pills = 2,strength = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50],workers = [5, 15, 25, 35, 45],pills = 2,strength = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50],workers = [5, 15, 25, 35, 45],pills = 2,strength = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 2,strength = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 2,strength = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 4],workers = [0, 0, 0],pills = 1,strength = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 4],workers = [0, 0, 0],pills = 1,strength = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50],workers = [1, 2, 3, 4, 5],pills = 5,strength = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50],workers = [1, 2, 3, 4, 5],pills = 5,strength = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50],workers = [5, 15, 25, 35, 45],pills = 0,strength = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50],workers = [5, 15, 25, 35, 45],pills = 0,strength = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 8, 7, 6, 5],workers = [4, 4, 4, 4, 4],pills = 5,strength = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 8, 7, 6, 5],workers = [4, 4, 4, 4, 4],pills = 5,strength = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 6, 7, 11],workers = [6, 8, 9],pills = 2,strength = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 6, 7, 11],workers = [6, 8, 9],pills = 2,strength = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1],pills = 5,strength = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1],pills = 5,strength = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50],workers = [5, 15, 25, 35, 45],pills = 5,strength = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50],workers = [5, 15, 25, 35, 45],pills = 5,strength = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 5,strength = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 5,strength = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1],workers = [1, 1, 1, 1],pills = 4,strength = 0) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1],workers = [1, 1, 1, 1],pills = 4,strength = 0) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 10, 100, 1000],workers = [1, 10, 100, 1000],pills = 2,strength = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 10, 100, 1000],workers = [1, 10, 100, 1000],pills = 2,strength = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 2, 1],workers = [0, 3, 3],pills = 1,strength = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 2, 1],workers = [0, 3, 3],pills = 1,strength = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1],pills = 0,strength = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1],pills = 0,strength = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],pills = 10,strength = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],pills = 10,strength = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pills = 0,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pills = 0,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],workers = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],pills = 10,strength = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],workers = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],pills = 10,strength = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 6, 9, 12, 15],workers = [3, 6, 9, 12, 15],pills = 2,strength = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 6, 9, 12, 15],workers = [3, 6, 9, 12, 15],pills = 2,strength = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000000000, 1000000000, 1000000000],workers = [1000000000, 1000000000, 1000000000],pills = 3,strength = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000000000, 1000000000, 1000000000],workers = [1000000000, 1000000000, 1000000000],pills = 3,strength = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1],pills = 3,strength = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1],pills = 3,strength = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],pills = 10,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],pills = 10,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [50, 100, 150, 200, 250],workers = [40, 80, 120, 160, 200],pills = 3,strength = 60) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [50, 100, 150, 200, 250],workers = [40, 80, 120, 160, 200],pills = 3,strength = 60) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],pills = 5,strength = 20) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],pills = 5,strength = 20) == 11: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],workers = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],pills = 5,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],workers = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],pills = 5,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500],workers = [100, 150, 200, 250, 300],pills = 2,strength = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500],workers = [100, 150, 200, 250, 300],pills = 2,strength = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pills = 10,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pills = 10,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 5,strength = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 5,strength = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5],workers = [1, 1, 1, 1, 1],pills = 5,strength = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5],workers = [1, 1, 1, 1, 1],pills = 5,strength = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 6, 9, 12, 15],workers = [3, 6, 9, 12, 15],pills = 0,strength = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 6, 9, 12, 15],workers = [3, 6, 9, 12, 15],pills = 0,strength = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [500000000, 500000000, 500000000, 500000000, 500000000],workers = [500000000, 500000000, 500000000, 500000000, 500000000],pills = 5,strength = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [500000000, 500000000, 500000000, 500000000, 500000000],workers = [500000000, 500000000, 500000000, 500000000, 500000000],pills = 5,strength = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9],workers = [10, 20, 30, 40, 50],pills = 2,strength = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9],workers = [10, 20, 30, 40, 50],pills = 2,strength = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pills = 5,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pills = 5,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000000000],workers = [999999999],pills = 1,strength = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000000000],workers = [999999999],pills = 1,strength = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5],workers = [10, 20, 30, 40, 50],pills = 2,strength = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5],workers = [10, 20, 30, 40, 50],pills = 2,strength = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],pills = 5,strength = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],pills = 5,strength = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000, 2000, 3000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 5,strength = 500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000, 2000, 3000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 5,strength = 500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 15, 25, 35, 45],workers = [1, 11, 21, 31, 41],pills = 2,strength = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 15, 25, 35, 45],workers = [1, 11, 21, 31, 41],pills = 2,strength = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],pills = 15,strength = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],pills = 15,strength = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 5,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 5,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],workers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],pills = 10,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],workers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],pills = 10,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400],pills = 10,strength = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400],pills = 10,strength = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 10,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 10,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000, 2000, 3000, 4000, 5000],workers = [500, 1000, 1500, 2000, 2500],pills = 4,strength = 1000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000, 2000, 3000, 4000, 5000],workers = [500, 1000, 1500, 2000, 2500],pills = 4,strength = 1000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50],workers = [10, 20, 30, 40, 50],pills = 0,strength = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50],workers = [10, 20, 30, 40, 50],pills = 0,strength = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],workers = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],pills = 7,strength = 50) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],workers = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],pills = 7,strength = 50) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],pills = 5,strength = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],pills = 5,strength = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15],workers = [2, 4, 6, 8, 10, 12, 14, 16],pills = 3,strength = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15],workers = [2, 4, 6, 8, 10, 12, 14, 16],pills = 3,strength = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 5,strength = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 5,strength = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 10, 15, 20, 25, 30],workers = [10, 15, 20, 25, 30, 35],pills = 3,strength = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 10, 15, 20, 25, 30],workers = [10, 15, 20, 25, 30, 35],pills = 3,strength = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 3,strength = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 3,strength = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 5,strength = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 5,strength = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],pills = 5,strength = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],pills = 5,strength = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500],workers = [150, 250, 350, 450, 550],pills = 3,strength = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500],workers = [150, 250, 350, 450, 550],pills = 3,strength = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 3,strength = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 3,strength = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pills = 5,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pills = 5,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 15, 25, 35, 45],workers = [1, 1, 1, 1, 1],pills = 5,strength = 40) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 15, 25, 35, 45],workers = [1, 1, 1, 1, 1],pills = 5,strength = 40) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],pills = 10,strength = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],pills = 10,strength = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 5,strength = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 5,strength = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [50, 50, 50, 50, 50],workers = [100, 100, 100, 100, 100],pills = 2,strength = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [50, 50, 50, 50, 50],workers = [100, 100, 100, 100, 100],pills = 2,strength = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [500, 400, 300, 200, 100],workers = [100, 200, 300, 400, 500],pills = 2,strength = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [500, 400, 300, 200, 100],workers = [100, 200, 300, 400, 500],pills = 2,strength = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 150, 200, 250, 300],workers = [50, 100, 150, 200, 250],pills = 2,strength = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 150, 200, 250, 300],workers = [50, 100, 150, 200, 250],pills = 2,strength = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pills = 5,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pills = 5,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],pills = 10,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],pills = 10,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500],workers = [100, 200, 300, 400, 500],pills = 5,strength = 500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500],workers = [100, 200, 300, 400, 500],pills = 5,strength = 500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 5,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 5,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],workers = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 7,strength = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],workers = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 7,strength = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pills = 5,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pills = 5,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [999999999, 999999998, 999999997, 999999996, 999999995],workers = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],pills = 2,strength = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [999999999, 999999998, 999999997, 999999996, 999999995],workers = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],pills = 2,strength = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 0,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 0,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 25, 50, 75, 100],workers = [10, 20, 30, 40, 50],pills = 3,strength = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 25, 50, 75, 100],workers = [10, 20, 30, 40, 50],pills = 3,strength = 20) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 0,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 0,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 10,strength = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 10,strength = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],workers = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800],pills = 10,strength = 200) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],workers = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800],pills = 10,strength = 200) == 20: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 5, 9, 13, 17, 21, 25],workers = [2, 6, 10, 14, 18, 22, 26],pills = 3,strength = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 5, 9, 13, 17, 21, 25],workers = [2, 6, 10, 14, 18, 22, 26],pills = 3,strength = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 4,strength = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 4,strength = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 5,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 5,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],workers = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],pills = 3,strength = 200) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],workers = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],pills = 3,strength = 200) == 11: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000, 2000, 3000, 4000, 5000],workers = [500, 1500, 2500, 3500, 4500],pills = 2,strength = 1000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000, 2000, 3000, 4000, 5000],workers = [500, 1500, 2500, 3500, 4500],pills = 2,strength = 1000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 10,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 10,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],pills = 5,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],pills = 5,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000000000, 1000000000],workers = [1000000000, 1000000000],pills = 1,strength = 0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000000000, 1000000000],workers = [1000000000, 1000000000],pills = 1,strength = 0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 10,strength = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 10,strength = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],pills = 5,strength = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],pills = 5,strength = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],pills = 5,strength = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],pills = 5,strength = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 0,strength = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 0,strength = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38],pills = 5,strength = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38],pills = 5,strength = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 5,strength = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 5,strength = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [90, 80, 70, 60, 50, 40, 30, 20, 10],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90],pills = 4,strength = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [90, 80, 70, 60, 50, 40, 30, 20, 10],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90],pills = 4,strength = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 0,strength = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 0,strength = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [50, 60, 70, 80, 90],workers = [40, 50, 60, 70, 80],pills = 3,strength = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [50, 60, 70, 80, 90],workers = [40, 50, 60, 70, 80],pills = 3,strength = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [500, 500, 500, 500, 500],workers = [250, 250, 250, 250, 250],pills = 5,strength = 250) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [500, 500, 500, 500, 500],workers = [250, 250, 250, 250, 250],pills = 5,strength = 250) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 10],workers = [1, 1, 1, 1, 1],pills = 5,strength = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 10],workers = [1, 1, 1, 1, 1],pills = 5,strength = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000000000, 1000000000, 1000000000],workers = [1000000000, 1000000000, 1000000000],pills = 1,strength = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000000000, 1000000000, 1000000000],workers = [1000000000, 1000000000, 1000000000],pills = 1,strength = 0) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],pills = 5,strength = 50) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],pills = 5,strength = 50) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],pills = 10,strength = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],pills = 10,strength = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500, 600],workers = [100, 200, 300, 400, 500, 600],pills = 0,strength = 0) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500, 600],workers = [100, 200, 300, 400, 500, 600],pills = 0,strength = 0) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000000000],workers = [1000000000],pills = 0,strength = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000000000],workers = [1000000000],pills = 0,strength = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 15, 25, 35, 45, 55],workers = [10, 20, 30, 40, 50, 60],pills = 3,strength = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 15, 25, 35, 45, 55],workers = [10, 20, 30, 40, 50, 60],pills = 3,strength = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1000000000],workers = [1000000000],pills = 1,strength = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1000000000],workers = [1000000000],pills = 1,strength = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 8, 7, 6, 5, 4, 3, 2, 1],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9],pills = 0,strength = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 8, 7, 6, 5, 4, 3, 2, 1],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9],pills = 0,strength = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],pills = 5,strength = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],pills = 5,strength = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9],workers = [2, 4, 6, 8, 10],pills = 2,strength = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9],workers = [2, 4, 6, 8, 10],pills = 2,strength = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10000, 20000, 30000, 40000, 50000],workers = [1000, 2000, 3000, 4000, 5000],pills = 5,strength = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10000, 20000, 30000, 40000, 50000],workers = [1000, 2000, 3000, 4000, 5000],pills = 5,strength = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],pills = 5,strength = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],pills = 5,strength = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500],pills = 5,strength = 500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500],pills = 5,strength = 500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [500000000, 500000000],workers = [500000000, 500000000],pills = 2,strength = 0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [500000000, 500000000],workers = [500000000, 500000000],pills = 2,strength = 0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [50, 100, 150, 200, 250],workers = [100, 150, 200, 250, 300],pills = 3,strength = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [50, 100, 150, 200, 250],workers = [100, 150, 200, 250, 300],pills = 3,strength = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 18, 27, 36, 45, 54],workers = [12, 24, 36, 48, 60, 72],pills = 5,strength = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 18, 27, 36, 45, 54],workers = [12, 24, 36, 48, 60, 72],pills = 5,strength = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 10],workers = [10, 10, 10, 10, 10],pills = 5,strength = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 10],workers = [10, 10, 10, 10, 10],pills = 5,strength = 0) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tasks = [100, 200, 300],workers = [50, 150, 250, 350],pills = 2,strength = 100) == 3
    assert candidate(tasks = [10, 20, 30],workers = [30, 40, 50],pills = 0,strength = 10) == 3
    assert candidate(tasks = [10, 15, 30],workers = [0, 10, 10, 10, 10],pills = 3,strength = 10) == 2
    assert candidate(tasks = [100, 200, 300],workers = [100, 100, 100, 100, 100],pills = 2,strength = 100) == 2
    assert candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 5,strength = 5) == 5
    assert candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 0,strength = 1) == 5
    assert candidate(tasks = [5, 5, 5, 5],workers = [1, 1, 1, 1],pills = 4,strength = 4) == 4
    assert candidate(tasks = [100, 200, 300],workers = [150, 250, 350],pills = 1,strength = 100) == 3
    assert candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 0,strength = 2) == 5
    assert candidate(tasks = [100, 200, 300],workers = [150, 250, 350],pills = 2,strength = 50) == 3
    assert candidate(tasks = [10, 20, 30, 40, 50],workers = [5, 15, 25, 35, 45],pills = 2,strength = 10) == 4
    assert candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 2,strength = 5) == 5
    assert candidate(tasks = [5, 4],workers = [0, 0, 0],pills = 1,strength = 5) == 1
    assert candidate(tasks = [10, 20, 30, 40, 50],workers = [1, 2, 3, 4, 5],pills = 5,strength = 10) == 1
    assert candidate(tasks = [10, 20, 30, 40, 50],workers = [5, 15, 25, 35, 45],pills = 0,strength = 10) == 4
    assert candidate(tasks = [9, 8, 7, 6, 5],workers = [4, 4, 4, 4, 4],pills = 5,strength = 5) == 5
    assert candidate(tasks = [3, 6, 7, 11],workers = [6, 8, 9],pills = 2,strength = 3) == 3
    assert candidate(tasks = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1],pills = 5,strength = 0) == 5
    assert candidate(tasks = [10, 20, 30, 40, 50],workers = [5, 15, 25, 35, 45],pills = 5,strength = 10) == 5
    assert candidate(tasks = [1, 2, 3, 4, 5],workers = [5, 5, 5, 5, 5],pills = 5,strength = 0) == 5
    assert candidate(tasks = [1, 1, 1, 1],workers = [1, 1, 1, 1],pills = 4,strength = 0) == 4
    assert candidate(tasks = [1, 10, 100, 1000],workers = [1, 10, 100, 1000],pills = 2,strength = 500) == 4
    assert candidate(tasks = [3, 2, 1],workers = [0, 3, 3],pills = 1,strength = 1) == 3
    assert candidate(tasks = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1],pills = 0,strength = 0) == 5
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],pills = 10,strength = 5) == 20
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pills = 0,strength = 1) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],workers = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],pills = 10,strength = 5) == 30
    assert candidate(tasks = [3, 6, 9, 12, 15],workers = [3, 6, 9, 12, 15],pills = 2,strength = 3) == 5
    assert candidate(tasks = [1000000000, 1000000000, 1000000000],workers = [1000000000, 1000000000, 1000000000],pills = 3,strength = 0) == 3
    assert candidate(tasks = [1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1],pills = 3,strength = 1) == 5
    assert candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],pills = 10,strength = 0) == 10
    assert candidate(tasks = [50, 100, 150, 200, 250],workers = [40, 80, 120, 160, 200],pills = 3,strength = 60) == 4
    assert candidate(tasks = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],pills = 5,strength = 20) == 11
    assert candidate(tasks = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],workers = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],pills = 5,strength = 1) == 10
    assert candidate(tasks = [100, 200, 300, 400, 500],workers = [100, 150, 200, 250, 300],pills = 2,strength = 100) == 4
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pills = 10,strength = 0) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 5,strength = 10) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5],workers = [1, 1, 1, 1, 1],pills = 5,strength = 4) == 5
    assert candidate(tasks = [3, 6, 9, 12, 15],workers = [3, 6, 9, 12, 15],pills = 0,strength = 10) == 5
    assert candidate(tasks = [500000000, 500000000, 500000000, 500000000, 500000000],workers = [500000000, 500000000, 500000000, 500000000, 500000000],pills = 5,strength = 0) == 5
    assert candidate(tasks = [1, 3, 5, 7, 9],workers = [10, 20, 30, 40, 50],pills = 2,strength = 5) == 5
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pills = 5,strength = 0) == 10
    assert candidate(tasks = [1000000000],workers = [999999999],pills = 1,strength = 1) == 1
    assert candidate(tasks = [1, 2, 3, 4, 5],workers = [10, 20, 30, 40, 50],pills = 2,strength = 5) == 5
    assert candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],pills = 5,strength = 100) == 9
    assert candidate(tasks = [1000, 2000, 3000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 5,strength = 500) == 1
    assert candidate(tasks = [5, 15, 25, 35, 45],workers = [1, 11, 21, 31, 41],pills = 2,strength = 10) == 4
    assert candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],pills = 15,strength = 1) == 15
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 5,strength = 1) == 10
    assert candidate(tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],workers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],pills = 10,strength = 0) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400],pills = 10,strength = 20) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 10,strength = 0) == 10
    assert candidate(tasks = [1000, 2000, 3000, 4000, 5000],workers = [500, 1000, 1500, 2000, 2500],pills = 4,strength = 1000) == 3
    assert candidate(tasks = [10, 20, 30, 40, 50],workers = [10, 20, 30, 40, 50],pills = 0,strength = 0) == 5
    assert candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],workers = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],pills = 7,strength = 50) == 15
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],pills = 5,strength = 5) == 10
    assert candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15],workers = [2, 4, 6, 8, 10, 12, 14, 16],pills = 3,strength = 2) == 8
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 5,strength = 2) == 10
    assert candidate(tasks = [5, 10, 15, 20, 25, 30],workers = [10, 15, 20, 25, 30, 35],pills = 3,strength = 5) == 6
    assert candidate(tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 3,strength = 5) == 10
    assert candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 5,strength = 50) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],pills = 5,strength = 10) == 20
    assert candidate(tasks = [100, 200, 300, 400, 500],workers = [150, 250, 350, 450, 550],pills = 3,strength = 100) == 5
    assert candidate(tasks = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 3,strength = 20) == 10
    assert candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pills = 5,strength = 1) == 10
    assert candidate(tasks = [5, 15, 25, 35, 45],workers = [1, 1, 1, 1, 1],pills = 5,strength = 40) == 4
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],pills = 10,strength = 4) == 10
    assert candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 5,strength = 50) == 10
    assert candidate(tasks = [50, 50, 50, 50, 50],workers = [100, 100, 100, 100, 100],pills = 2,strength = 10) == 5
    assert candidate(tasks = [500, 400, 300, 200, 100],workers = [100, 200, 300, 400, 500],pills = 2,strength = 100) == 5
    assert candidate(tasks = [100, 150, 200, 250, 300],workers = [50, 100, 150, 200, 250],pills = 2,strength = 50) == 4
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pills = 5,strength = 1) == 10
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],pills = 10,strength = 0) == 10
    assert candidate(tasks = [100, 200, 300, 400, 500],workers = [100, 200, 300, 400, 500],pills = 5,strength = 500) == 5
    assert candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 5,strength = 0) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],workers = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 7,strength = 3) == 15
    assert candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],pills = 5,strength = 0) == 10
    assert candidate(tasks = [999999999, 999999998, 999999997, 999999996, 999999995],workers = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],pills = 2,strength = 1) == 5
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 0,strength = 1) == 10
    assert candidate(tasks = [5, 25, 50, 75, 100],workers = [10, 20, 30, 40, 50],pills = 3,strength = 20) == 3
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 0,strength = 0) == 10
    assert candidate(tasks = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 10,strength = 9) == 10
    assert candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],workers = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800],pills = 10,strength = 200) == 20
    assert candidate(tasks = [1, 5, 9, 13, 17, 21, 25],workers = [2, 6, 10, 14, 18, 22, 26],pills = 3,strength = 1) == 7
    assert candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 4,strength = 10) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pills = 5,strength = 1) == 10
    assert candidate(tasks = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],workers = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],pills = 3,strength = 200) == 11
    assert candidate(tasks = [1000, 2000, 3000, 4000, 5000],workers = [500, 1500, 2500, 3500, 4500],pills = 2,strength = 1000) == 4
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 10,strength = 1) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],pills = 5,strength = 1) == 10
    assert candidate(tasks = [1000000000, 1000000000],workers = [1000000000, 1000000000],pills = 1,strength = 0) == 2
    assert candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],pills = 10,strength = 10) == 10
    assert candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],pills = 5,strength = 10) == 2
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],workers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],pills = 5,strength = 1) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],workers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 0,strength = 0) == 10
    assert candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],workers = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38],pills = 5,strength = 10) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],workers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pills = 5,strength = 10) == 20
    assert candidate(tasks = [90, 80, 70, 60, 50, 40, 30, 20, 10],workers = [10, 20, 30, 40, 50, 60, 70, 80, 90],pills = 4,strength = 20) == 9
    assert candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],pills = 0,strength = 100) == 10
    assert candidate(tasks = [50, 60, 70, 80, 90],workers = [40, 50, 60, 70, 80],pills = 3,strength = 10) == 4
    assert candidate(tasks = [500, 500, 500, 500, 500],workers = [250, 250, 250, 250, 250],pills = 5,strength = 250) == 5
    assert candidate(tasks = [10, 10, 10, 10, 10],workers = [1, 1, 1, 1, 1],pills = 5,strength = 9) == 5
    assert candidate(tasks = [1000000000, 1000000000, 1000000000],workers = [1000000000, 1000000000, 1000000000],pills = 1,strength = 0) == 3
    assert candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],pills = 5,strength = 50) == 9
    assert candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],pills = 10,strength = 100) == 10
    assert candidate(tasks = [100, 200, 300, 400, 500, 600],workers = [100, 200, 300, 400, 500, 600],pills = 0,strength = 0) == 6
    assert candidate(tasks = [1000000000],workers = [1000000000],pills = 0,strength = 0) == 1
    assert candidate(tasks = [5, 15, 25, 35, 45, 55],workers = [10, 20, 30, 40, 50, 60],pills = 3,strength = 10) == 6
    assert candidate(tasks = [1000000000],workers = [1000000000],pills = 1,strength = 0) == 1
    assert candidate(tasks = [9, 8, 7, 6, 5, 4, 3, 2, 1],workers = [1, 2, 3, 4, 5, 6, 7, 8, 9],pills = 0,strength = 2) == 9
    assert candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],pills = 5,strength = 10) == 10
    assert candidate(tasks = [1, 3, 5, 7, 9],workers = [2, 4, 6, 8, 10],pills = 2,strength = 1) == 5
    assert candidate(tasks = [10000, 20000, 30000, 40000, 50000],workers = [1000, 2000, 3000, 4000, 5000],pills = 5,strength = 10000) == 1
    assert candidate(tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],workers = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],pills = 5,strength = 5) == 9
    assert candidate(tasks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],workers = [100, 200, 300, 400, 500],pills = 5,strength = 500) == 5
    assert candidate(tasks = [500000000, 500000000],workers = [500000000, 500000000],pills = 2,strength = 0) == 2
    assert candidate(tasks = [50, 100, 150, 200, 250],workers = [100, 150, 200, 250, 300],pills = 3,strength = 50) == 5
    assert candidate(tasks = [9, 18, 27, 36, 45, 54],workers = [12, 24, 36, 48, 60, 72],pills = 5,strength = 6) == 6
    assert candidate(tasks = [10, 10, 10, 10, 10],workers = [10, 10, 10, 10, 10],pills = 5,strength = 0) == 5


