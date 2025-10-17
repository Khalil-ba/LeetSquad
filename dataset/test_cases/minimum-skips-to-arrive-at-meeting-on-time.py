def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10],speed = 5,hoursBefore = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10],speed = 5,hoursBefore = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1],speed = 1,hoursBefore = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1],speed = 1,hoursBefore = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5],speed = 10,hoursBefore = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5],speed = 10,hoursBefore = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1],speed = 1,hoursBefore = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1],speed = 1,hoursBefore = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [7, 3, 5, 5],speed = 1,hoursBefore = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [7, 3, 5, 5],speed = 1,hoursBefore = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5],speed = 1,hoursBefore = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5],speed = 1,hoursBefore = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1],speed = 1,hoursBefore = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1],speed = 1,hoursBefore = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10],speed = 10,hoursBefore = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10],speed = 10,hoursBefore = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5],speed = 5,hoursBefore = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5],speed = 5,hoursBefore = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1],speed = 1,hoursBefore = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1],speed = 1,hoursBefore = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [7, 3, 5, 5],speed = 2,hoursBefore = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [7, 3, 5, 5],speed = 2,hoursBefore = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 2],speed = 4,hoursBefore = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 2],speed = 4,hoursBefore = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 100000, 100000],speed = 100000,hoursBefore = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 100000, 100000],speed = 100000,hoursBefore = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10],speed = 5,hoursBefore = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10],speed = 5,hoursBefore = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5],speed = 10,hoursBefore = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5],speed = 10,hoursBefore = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],speed = 2,hoursBefore = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],speed = 2,hoursBefore = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],speed = 15,hoursBefore = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],speed = 15,hoursBefore = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 1000,hoursBefore = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 1000,hoursBefore = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5],speed = 2,hoursBefore = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5],speed = 2,hoursBefore = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 2,hoursBefore = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 2,hoursBefore = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],speed = 10000,hoursBefore = 99) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],speed = 10000,hoursBefore = 99) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = 5,hoursBefore = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = 5,hoursBefore = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = 25,hoursBefore = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = 25,hoursBefore = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],speed = 5,hoursBefore = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],speed = 5,hoursBefore = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],speed = 10,hoursBefore = 40) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],speed = 10,hoursBefore = 40) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5],speed = 100,hoursBefore = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5],speed = 100,hoursBefore = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 3,hoursBefore = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 3,hoursBefore = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],speed = 100,hoursBefore = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],speed = 100,hoursBefore = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = 2,hoursBefore = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = 2,hoursBefore = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = 5,hoursBefore = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = 5,hoursBefore = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],speed = 1,hoursBefore = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],speed = 1,hoursBefore = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 21, 30, 40, 50, 60, 70, 80, 90, 100],speed = 10,hoursBefore = 55) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 21, 30, 40, 50, 60, 70, 80, 90, 100],speed = 10,hoursBefore = 55) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = 2,hoursBefore = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = 2,hoursBefore = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],speed = 100000,hoursBefore = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],speed = 100000,hoursBefore = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],speed = 5,hoursBefore = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],speed = 5,hoursBefore = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 5,hoursBefore = 35) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 5,hoursBefore = 35) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = 15,hoursBefore = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = 15,hoursBefore = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = 100,hoursBefore = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = 100,hoursBefore = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [123, 456, 789, 101, 202, 303],speed = 100,hoursBefore = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [123, 456, 789, 101, 202, 303],speed = 100,hoursBefore = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 29) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 29) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1],speed = 4,hoursBefore = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1],speed = 4,hoursBefore = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 6, 9, 12, 15, 18, 21],speed = 5,hoursBefore = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 6, 9, 12, 15, 18, 21],speed = 5,hoursBefore = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 3,hoursBefore = 12) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 3,hoursBefore = 12) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25],speed = 5,hoursBefore = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25],speed = 5,hoursBefore = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 3,hoursBefore = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 3,hoursBefore = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],speed = 100,hoursBefore = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],speed = 100,hoursBefore = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],speed = 2,hoursBefore = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],speed = 2,hoursBefore = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = 1,hoursBefore = 105) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = 1,hoursBefore = 105) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 19) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 19) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [7, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5],speed = 2,hoursBefore = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [7, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5],speed = 2,hoursBefore = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = 10,hoursBefore = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = 10,hoursBefore = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = 2,hoursBefore = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = 2,hoursBefore = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],speed = 100,hoursBefore = 60) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],speed = 100,hoursBefore = 60) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [7, 3, 5, 5, 7, 3, 5, 5],speed = 2,hoursBefore = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [7, 3, 5, 5, 7, 3, 5, 5],speed = 2,hoursBefore = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400],speed = 100,hoursBefore = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400],speed = 100,hoursBefore = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 5,hoursBefore = 12) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 5,hoursBefore = 12) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980],speed = 99999,hoursBefore = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980],speed = 99999,hoursBefore = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = 3,hoursBefore = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = 3,hoursBefore = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 1,hoursBefore = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 1,hoursBefore = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 25,hoursBefore = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 25,hoursBefore = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 7, 5, 3, 1],speed = 4,hoursBefore = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 7, 5, 3, 1],speed = 4,hoursBefore = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = 7,hoursBefore = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = 7,hoursBefore = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],speed = 10,hoursBefore = 13) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],speed = 10,hoursBefore = 13) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25, 30, 35],speed = 7,hoursBefore = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25, 30, 35],speed = 7,hoursBefore = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10000, 20000, 30000, 40000, 50000],speed = 10000,hoursBefore = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10000, 20000, 30000, 40000, 50000],speed = 10000,hoursBefore = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 15,hoursBefore = 30) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 15,hoursBefore = 30) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [3, 8, 2, 7, 5],speed = 4,hoursBefore = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [3, 8, 2, 7, 5],speed = 4,hoursBefore = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],speed = 100000,hoursBefore = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],speed = 100000,hoursBefore = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 5,hoursBefore = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 5,hoursBefore = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = 3,hoursBefore = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = 3,hoursBefore = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 3, 2, 4, 5],speed = 3,hoursBefore = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 3, 2, 4, 5],speed = 3,hoursBefore = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(dist = [999, 1000, 1001, 1002, 1003],speed = 1,hoursBefore = 5000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [999, 1000, 1001, 1002, 1003],speed = 1,hoursBefore = 5000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 2000, 3000, 4000],speed = 1000,hoursBefore = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 2000, 3000, 4000],speed = 1000,hoursBefore = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 90000, 80000, 70000, 60000],speed = 50000,hoursBefore = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 90000, 80000, 70000, 60000],speed = 50000,hoursBefore = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50],speed = 15,hoursBefore = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50],speed = 15,hoursBefore = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100000, 100000, 100000],speed = 100000,hoursBefore = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100000, 100000, 100000],speed = 100000,hoursBefore = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 15,hoursBefore = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 15,hoursBefore = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],speed = 1,hoursBefore = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],speed = 1,hoursBefore = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 50,hoursBefore = 35) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 50,hoursBefore = 35) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 30) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 30) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25],speed = 5,hoursBefore = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25],speed = 5,hoursBefore = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 3,hoursBefore = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 3,hoursBefore = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 45) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 45) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [99999, 99998, 99997, 99996],speed = 100000,hoursBefore = 399990) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [99999, 99998, 99997, 99996],speed = 100000,hoursBefore = 399990) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],speed = 5,hoursBefore = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],speed = 5,hoursBefore = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],speed = 9,hoursBefore = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],speed = 9,hoursBefore = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [50, 100, 150, 200, 250],speed = 50,hoursBefore = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [50, 100, 150, 200, 250],speed = 50,hoursBefore = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 10,hoursBefore = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 10,hoursBefore = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],speed = 3,hoursBefore = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],speed = 3,hoursBefore = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 10, 15, 20, 25],speed = 5,hoursBefore = 14) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 10, 15, 20, 25],speed = 5,hoursBefore = 14) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = 1,hoursBefore = 1500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = 1,hoursBefore = 1500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 4, 3, 2, 1],speed = 1,hoursBefore = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 4, 3, 2, 1],speed = 1,hoursBefore = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 2,hoursBefore = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 2,hoursBefore = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 5,hoursBefore = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 5,hoursBefore = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [5, 15, 25, 35, 45],speed = 10,hoursBefore = 12) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [5, 15, 25, 35, 45],speed = 10,hoursBefore = 12) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500],speed = 50,hoursBefore = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500],speed = 50,hoursBefore = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 500,hoursBefore = 12) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 500,hoursBefore = 12) == 4: {e}')
    
    total += 1
    try:
        result = candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],speed = 30,hoursBefore = 35) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],speed = 30,hoursBefore = 35) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],speed = 50,hoursBefore = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],speed = 50,hoursBefore = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 55) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 55) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 2000, 3000, 4000, 5000],speed = 1000,hoursBefore = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 2000, 3000, 4000, 5000],speed = 1000,hoursBefore = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(dist = [1000, 2000, 3000, 4000, 5000],speed = 1000,hoursBefore = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(dist = [1000, 2000, 3000, 4000, 5000],speed = 1000,hoursBefore = 15) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(dist = [10, 10, 10],speed = 5,hoursBefore = 6) == 0
    assert candidate(dist = [1, 1, 1, 1, 1],speed = 1,hoursBefore = 3) == -1
    assert candidate(dist = [5, 5, 5, 5, 5],speed = 10,hoursBefore = 2) == -1
    assert candidate(dist = [1, 1, 1, 1],speed = 1,hoursBefore = 4) == 0
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 10) == 0
    assert candidate(dist = [7, 3, 5, 5],speed = 1,hoursBefore = 10) == -1
    assert candidate(dist = [1, 2, 3, 4, 5],speed = 1,hoursBefore = 20) == 0
    assert candidate(dist = [1, 1, 1, 1, 1],speed = 1,hoursBefore = 4) == -1
    assert candidate(dist = [10, 10, 10],speed = 10,hoursBefore = 3) == 0
    assert candidate(dist = [5, 5, 5, 5, 5],speed = 5,hoursBefore = 5) == 0
    assert candidate(dist = [1, 1, 1, 1],speed = 1,hoursBefore = 3) == -1
    assert candidate(dist = [7, 3, 5, 5],speed = 2,hoursBefore = 10) == 2
    assert candidate(dist = [1, 3, 2],speed = 4,hoursBefore = 2) == 1
    assert candidate(dist = [100000, 100000, 100000],speed = 100000,hoursBefore = 3) == 0
    assert candidate(dist = [10, 10, 10],speed = 5,hoursBefore = 5) == -1
    assert candidate(dist = [5, 5, 5, 5, 5],speed = 10,hoursBefore = 3) == 2
    assert candidate(dist = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],speed = 2,hoursBefore = 15) == -1
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],speed = 15,hoursBefore = 15) == -1
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 1000,hoursBefore = 5) == -1
    assert candidate(dist = [7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5, 7, 3, 5, 5],speed = 2,hoursBefore = 100) == -1
    assert candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 2,hoursBefore = 10) == -1
    assert candidate(dist = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],speed = 10000,hoursBefore = 99) == -1
    assert candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = 5,hoursBefore = 20) == 8
    assert candidate(dist = [10, 20, 30, 40, 50],speed = 25,hoursBefore = 10) == 0
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],speed = 5,hoursBefore = 50) == -1
    assert candidate(dist = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 9) == -1
    assert candidate(dist = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],speed = 10,hoursBefore = 40) == -1
    assert candidate(dist = [1, 2, 3, 4, 5],speed = 100,hoursBefore = 1) == 4
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 3,hoursBefore = 100) == -1
    assert candidate(dist = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],speed = 100,hoursBefore = 20) == 7
    assert candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = 2,hoursBefore = 100) == -1
    assert candidate(dist = [10, 20, 30, 40, 50],speed = 5,hoursBefore = 30) == 0
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],speed = 1,hoursBefore = 50) == -1
    assert candidate(dist = [10, 21, 30, 40, 50, 60, 70, 80, 90, 100],speed = 10,hoursBefore = 55) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = 2,hoursBefore = 50) == -1
    assert candidate(dist = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],speed = 100000,hoursBefore = 9) == -1
    assert candidate(dist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],speed = 5,hoursBefore = 20) == -1
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 5,hoursBefore = 35) == -1
    assert candidate(dist = [10, 20, 30, 40, 50],speed = 15,hoursBefore = 15) == 0
    assert candidate(dist = [100, 200, 300, 400, 500],speed = 100,hoursBefore = 10) == -1
    assert candidate(dist = [123, 456, 789, 101, 202, 303],speed = 100,hoursBefore = 15) == -1
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 29) == -1
    assert candidate(dist = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1],speed = 4,hoursBefore = 5) == 6
    assert candidate(dist = [3, 6, 9, 12, 15, 18, 21],speed = 5,hoursBefore = 15) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 3,hoursBefore = 12) == -1
    assert candidate(dist = [5, 10, 15, 20, 25],speed = 5,hoursBefore = 10) == -1
    assert candidate(dist = [9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 3,hoursBefore = 10) == -1
    assert candidate(dist = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],speed = 100,hoursBefore = 9) == -1
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 15) == -1
    assert candidate(dist = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],speed = 2,hoursBefore = 30) == 10
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = 1,hoursBefore = 105) == -1
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 20) == 0
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 19) == -1
    assert candidate(dist = [7, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5, 3, 7, 5, 3, 5, 5],speed = 2,hoursBefore = 50) == -1
    assert candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = 10,hoursBefore = 6) == 4
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 100) == -1
    assert candidate(dist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],speed = 2,hoursBefore = 15) == -1
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],speed = 100,hoursBefore = 60) == -1
    assert candidate(dist = [7, 3, 5, 5, 7, 3, 5, 5],speed = 2,hoursBefore = 15) == -1
    assert candidate(dist = [100, 200, 300, 400],speed = 100,hoursBefore = 8) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 5,hoursBefore = 12) == 4
    assert candidate(dist = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980],speed = 99999,hoursBefore = 10) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],speed = 3,hoursBefore = 20) == -1
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 1,hoursBefore = 1000) == 0
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 25,hoursBefore = 20) == -1
    assert candidate(dist = [9, 7, 5, 3, 1],speed = 4,hoursBefore = 5) == -1
    assert candidate(dist = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],speed = 7,hoursBefore = 25) == -1
    assert candidate(dist = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],speed = 10,hoursBefore = 13) == -1
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 25) == -1
    assert candidate(dist = [5, 10, 15, 20, 25, 30, 35],speed = 7,hoursBefore = 20) == 5
    assert candidate(dist = [10000, 20000, 30000, 40000, 50000],speed = 10000,hoursBefore = 15) == 0
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 15,hoursBefore = 30) == -1
    assert candidate(dist = [3, 8, 2, 7, 5],speed = 4,hoursBefore = 10) == 0
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 50) == -1
    assert candidate(dist = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],speed = 100000,hoursBefore = 5) == 5
    assert candidate(dist = [9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 5,hoursBefore = 15) == 0
    assert candidate(dist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],speed = 3,hoursBefore = 30) == 0
    assert candidate(dist = [1, 3, 2, 4, 5],speed = 3,hoursBefore = 5) == 3
    assert candidate(dist = [999, 1000, 1001, 1002, 1003],speed = 1,hoursBefore = 5000) == -1
    assert candidate(dist = [100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 4) == 0
    assert candidate(dist = [100000, 100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 4) == -1
    assert candidate(dist = [1000, 2000, 3000, 4000],speed = 1000,hoursBefore = 10) == 0
    assert candidate(dist = [100000, 100000, 100000, 100000, 100000],speed = 100000,hoursBefore = 5) == 0
    assert candidate(dist = [100000, 90000, 80000, 70000, 60000],speed = 50000,hoursBefore = 10) == 0
    assert candidate(dist = [10, 20, 30, 40, 50],speed = 15,hoursBefore = 12) == 0
    assert candidate(dist = [100000, 100000, 100000],speed = 100000,hoursBefore = 2) == -1
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],speed = 15,hoursBefore = 25) == -1
    assert candidate(dist = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],speed = 1,hoursBefore = 100) == -1
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 50,hoursBefore = 35) == -1
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 30) == -1
    assert candidate(dist = [5, 10, 15, 20, 25],speed = 5,hoursBefore = 15) == 0
    assert candidate(dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],speed = 3,hoursBefore = 25) == 0
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 45) == -1
    assert candidate(dist = [99999, 99998, 99997, 99996],speed = 100000,hoursBefore = 399990) == 0
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 10) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],speed = 5,hoursBefore = 25) == -1
    assert candidate(dist = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],speed = 9,hoursBefore = 8) == -1
    assert candidate(dist = [50, 100, 150, 200, 250],speed = 50,hoursBefore = 10) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 10,hoursBefore = 5) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],speed = 3,hoursBefore = 25) == -1
    assert candidate(dist = [5, 10, 15, 20, 25],speed = 5,hoursBefore = 14) == -1
    assert candidate(dist = [100, 200, 300, 400, 500],speed = 1,hoursBefore = 1500) == 0
    assert candidate(dist = [5, 4, 3, 2, 1],speed = 1,hoursBefore = 15) == 0
    assert candidate(dist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],speed = 1,hoursBefore = 20) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 2,hoursBefore = 15) == -1
    assert candidate(dist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],speed = 5,hoursBefore = 10) == -1
    assert candidate(dist = [5, 15, 25, 35, 45],speed = 10,hoursBefore = 12) == -1
    assert candidate(dist = [100, 200, 300, 400, 500],speed = 50,hoursBefore = 25) == -1
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 500,hoursBefore = 12) == 4
    assert candidate(dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],speed = 30,hoursBefore = 35) == -1
    assert candidate(dist = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],speed = 50,hoursBefore = 20) == -1
    assert candidate(dist = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],speed = 100,hoursBefore = 55) == 0
    assert candidate(dist = [1000, 2000, 3000, 4000, 5000],speed = 1000,hoursBefore = 20) == 0
    assert candidate(dist = [1000, 2000, 3000, 4000, 5000],speed = 1000,hoursBefore = 15) == 0


