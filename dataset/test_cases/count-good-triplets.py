def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [3, 0, 1, 1, 9, 7],a = 7,b = 2,c = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 0, 1, 1, 9, 7],a = 7,b = 2,c = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9],a = 2,b = 3,c = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9],a = 2,b = 3,c = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3],a = 0,b = 0,c = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3],a = 0,b = 0,c = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50],a = 5,b = 10,c = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50],a = 5,b = 10,c = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50],a = 15,b = 25,c = 35) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50],a = 15,b = 25,c = 35) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0],a = 0,b = 0,c = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0],a = 0,b = 0,c = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50],a = 15,b = 15,c = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50],a = 15,b = 15,c = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50],a = 10,b = 10,c = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50],a = 10,b = 10,c = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9],a = 2,b = 2,c = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9],a = 2,b = 2,c = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0],a = 1,b = 1,c = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0],a = 1,b = 1,c = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0],a = 1,b = 1,c = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0],a = 1,b = 1,c = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 6, 8, 10, 14, 15, 18, 20, 22],a = 4,b = 3,c = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 6, 8, 10, 14, 15, 18, 20, 22],a = 4,b = 3,c = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 12, 15, 19, 22, 25, 28, 31, 34],a = 5,b = 7,c = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 12, 15, 19, 22, 25, 28, 31, 34],a = 5,b = 7,c = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],a = 1,b = 1,c = 2) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],a = 1,b = 1,c = 2) == 88: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 12, 15, 18, 22, 25, 28, 31],a = 5,b = 5,c = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 12, 15, 18, 22, 25, 28, 31],a = 5,b = 5,c = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],a = 2,b = 2,c = 4) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],a = 2,b = 2,c = 4) == 44: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 20, 20, 30, 40, 50, 60, 70, 80],a = 5,b = 5,c = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 20, 20, 30, 40, 50, 60, 70, 80],a = 5,b = 5,c = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 1, 5, 3, 6, 4, 2, 8, 9],a = 2,b = 3,c = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 1, 5, 3, 6, 4, 2, 8, 9],a = 2,b = 3,c = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],a = 2,b = 2,c = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],a = 2,b = 2,c = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],a = 0,b = 0,c = 0) == 1140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],a = 0,b = 0,c = 0) == 1140: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900],a = 150,b = 250,c = 350) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900],a = 150,b = 250,c = 350) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 12, 15, 20, 22, 25],a = 5,b = 6,c = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 12, 15, 20, 22, 25],a = 5,b = 6,c = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],a = 0,b = 0,c = 0) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],a = 0,b = 0,c = 0) == 120: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],a = 10,b = 20,c = 30) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],a = 10,b = 20,c = 30) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],a = 5,b = 10,c = 15) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],a = 5,b = 10,c = 15) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 8, 10, 15, 17],a = 5,b = 3,c = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 8, 10, 15, 17],a = 5,b = 3,c = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33],a = 4,b = 4,c = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33],a = 4,b = 4,c = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],a = 1,b = 1,c = 2) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],a = 1,b = 1,c = 2) == 54: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 10, 15, 10, 15, 10, 15],a = 5,b = 5,c = 10) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 10, 15, 10, 15, 10, 15],a = 5,b = 5,c = 10) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],a = 100,b = 200,c = 300) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],a = 100,b = 200,c = 300) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0],a = 100,b = 200,c = 300) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0],a = 100,b = 200,c = 300) == 17: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 7, 5, 3, 1, 2, 4, 6, 8, 0],a = 1,b = 2,c = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 7, 5, 3, 1, 2, 4, 6, 8, 0],a = 1,b = 2,c = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],a = 2,b = 2,c = 3) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],a = 2,b = 2,c = 3) == 37: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 3, 19, 5, 11, 13, 17, 15, 2, 9],a = 6,b = 5,c = 10) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 3, 19, 5, 11, 13, 17, 15, 2, 9],a = 6,b = 5,c = 10) == 24: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],a = 1,b = 1,c = 2) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],a = 1,b = 1,c = 2) == 132: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],a = 0,b = 0,c = 0) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],a = 0,b = 0,c = 0) == 120: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],a = 2,b = 3,c = 4) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],a = 2,b = 3,c = 4) == 58: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 2, 3, 6, 9, 10, 12],a = 3,b = 4,c = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 2, 3, 6, 9, 10, 12],a = 3,b = 4,c = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],a = 1,b = 2,c = 3) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],a = 1,b = 2,c = 3) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],a = 1,b = 1,c = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],a = 1,b = 1,c = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900],a = 100,b = 100,c = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900],a = 100,b = 100,c = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600],a = 50,b = 100,c = 150) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600],a = 50,b = 100,c = 150) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],a = 1,b = 1,c = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],a = 1,b = 1,c = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],a = 150,b = 200,c = 250) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],a = 150,b = 200,c = 250) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],a = 20,b = 30,c = 40) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],a = 20,b = 30,c = 40) == 64: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],a = 5,b = 5,c = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],a = 5,b = 5,c = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],a = 0,b = 0,c = 0) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],a = 0,b = 0,c = 0) == 120: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 0,b = 0,c = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 0,b = 0,c = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 3,b = 3,c = 3) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 3,b = 3,c = 3) == 324: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],a = 1,b = 1,c = 2) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],a = 1,b = 1,c = 2) == 120: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 9, 1, 3, 13, 12, 7],a = 6,b = 4,c = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 9, 1, 3, 13, 12, 7],a = 6,b = 4,c = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],a = 2,b = 2,c = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],a = 2,b = 2,c = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 1,b = 1,c = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 1,b = 1,c = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],a = 1,b = 1,c = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],a = 1,b = 1,c = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 12, 15, 20, 25, 30, 35, 40, 45, 50],a = 5,b = 10,c = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 12, 15, 20, 25, 30, 35, 40, 45, 50],a = 5,b = 10,c = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 12, 15, 16, 20, 25, 30],a = 7,b = 5,c = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 12, 15, 16, 20, 25, 30],a = 7,b = 5,c = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],a = 4,b = 8,c = 12) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],a = 4,b = 8,c = 12) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],a = 0,b = 0,c = 0) == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],a = 0,b = 0,c = 0) == 455: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],a = 4,b = 8,c = 12) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],a = 4,b = 8,c = 12) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50],a = 15,b = 25,c = 35) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50],a = 15,b = 25,c = 35) == 17: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 4, 4, 4, 4, 4, 4, 4, 4],a = 0,b = 0,c = 0) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 4, 4, 4, 4, 4, 4, 4, 4],a = 0,b = 0,c = 0) == 84: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],a = 1,b = 1,c = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],a = 1,b = 1,c = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 5, 1, 2, 10, 9, 10, 6],a = 4,b = 4,c = 7) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 5, 1, 2, 10, 9, 10, 6],a = 4,b = 4,c = 7) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],a = 0,b = 0,c = 0) == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],a = 0,b = 0,c = 0) == 455: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 7, 8, 2, 1, 9, 6, 4, 10],a = 5,b = 5,c = 5) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 7, 8, 2, 1, 9, 6, 4, 10],a = 5,b = 5,c = 5) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30],a = 10,b = 20,c = 30) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30],a = 10,b = 20,c = 30) == 166: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],a = 9,b = 19,c = 29) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],a = 9,b = 19,c = 29) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],a = 4,b = 5,c = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],a = 4,b = 5,c = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],a = 5,b = 5,c = 5) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],a = 5,b = 5,c = 5) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],a = 15,b = 15,c = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],a = 15,b = 15,c = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],a = 10,b = 10,c = 10) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],a = 10,b = 10,c = 10) == 120: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],a = 2,b = 3,c = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],a = 2,b = 3,c = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 3, 2, 4, 8, 7, 6, 9, 0],a = 3,b = 3,c = 5) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 3, 2, 4, 8, 7, 6, 9, 0],a = 3,b = 3,c = 5) == 34: {e}')
    
    total += 1
    try:
        result = candidate(arr = [34, 23, 54, 28, 90, 56, 78, 45, 12, 67],a = 20,b = 25,c = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [34, 23, 54, 28, 90, 56, 78, 45, 12, 67],a = 20,b = 25,c = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],a = 5,b = 10,c = 15) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],a = 5,b = 10,c = 15) == 17: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],a = 1,b = 1,c = 1) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],a = 1,b = 1,c = 1) == 120: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 3, 8, 1, 4, 6, 5, 2, 9, 0],a = 1,b = 1,c = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 3, 8, 1, 4, 6, 5, 2, 9, 0],a = 1,b = 1,c = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 15, 15, 20, 20, 20, 25, 25, 25],a = 5,b = 5,c = 10) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 15, 15, 20, 20, 20, 25, 25, 25],a = 5,b = 5,c = 10) == 66: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],a = 0,b = 0,c = 0) == 1140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],a = 0,b = 0,c = 0) == 1140: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],a = 1,b = 1,c = 2) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],a = 1,b = 1,c = 2) == 100: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],a = 10,b = 20,c = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],a = 10,b = 20,c = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 2, 4, 3, 7, 6, 9, 1],a = 3,b = 4,c = 5) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 2, 4, 3, 7, 6, 9, 1],a = 3,b = 4,c = 5) == 35: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30, 40, 50, 60, 70, 80, 90, 100, 110],a = 10,b = 10,c = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30, 40, 50, 60, 70, 80, 90, 100, 110],a = 10,b = 10,c = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2],a = 0,b = 0,c = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2],a = 0,b = 0,c = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],a = 15,b = 25,c = 35) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],a = 15,b = 25,c = 35) == 17: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 1,b = 1,c = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 1,b = 1,c = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],a = 4,b = 5,c = 6) == 214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],a = 4,b = 5,c = 6) == 214: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],a = 10,b = 10,c = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],a = 10,b = 10,c = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],a = 4,b = 6,c = 8) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],a = 4,b = 6,c = 8) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 1, 3, 2, 10, 1, 4],a = 1,b = 2,c = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 1, 3, 2, 10, 1, 4],a = 1,b = 2,c = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],a = 100,b = 150,c = 200) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],a = 100,b = 150,c = 200) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10],a = 3,b = 3,c = 4) == 152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10],a = 3,b = 3,c = 4) == 152: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],a = 15,b = 20,c = 25) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],a = 15,b = 20,c = 25) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],a = 1,b = 1,c = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],a = 1,b = 1,c = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10],a = 1,b = 1,c = 2) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10],a = 1,b = 1,c = 2) == 112: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],a = 3,b = 4,c = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],a = 3,b = 4,c = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],a = 1,b = 2,c = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],a = 1,b = 2,c = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],a = 1,b = 1,c = 2) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],a = 1,b = 1,c = 2) == 124: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 4, 1, 3, 6, 2],a = 2,b = 3,c = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 4, 1, 3, 6, 2],a = 2,b = 3,c = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 12, 15, 16, 23, 42],a = 5,b = 7,c = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 12, 15, 16, 23, 42],a = 5,b = 7,c = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 0,b = 0,c = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 0,b = 0,c = 0) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [3, 0, 1, 1, 9, 7],a = 7,b = 2,c = 3) == 4
    assert candidate(arr = [1, 3, 5, 7, 9],a = 2,b = 3,c = 4) == 3
    assert candidate(arr = [1, 1, 2, 2, 3],a = 0,b = 0,c = 1) == 0
    assert candidate(arr = [10, 20, 30, 40, 50],a = 5,b = 10,c = 15) == 0
    assert candidate(arr = [10, 20, 30, 40, 50],a = 15,b = 25,c = 35) == 5
    assert candidate(arr = [0, 0, 0, 0, 0],a = 0,b = 0,c = 0) == 10
    assert candidate(arr = [10, 20, 30, 40, 50],a = 15,b = 15,c = 15) == 0
    assert candidate(arr = [10, 20, 30, 40, 50],a = 10,b = 10,c = 10) == 0
    assert candidate(arr = [1, 3, 5, 7, 9],a = 2,b = 2,c = 2) == 0
    assert candidate(arr = [0, 0, 0, 0, 0],a = 1,b = 1,c = 1) == 10
    assert candidate(arr = [0, 0, 0, 0],a = 1,b = 1,c = 1) == 4
    assert candidate(arr = [1, 5, 6, 8, 10, 14, 15, 18, 20, 22],a = 4,b = 3,c = 5) == 8
    assert candidate(arr = [5, 8, 12, 15, 19, 22, 25, 28, 31, 34],a = 5,b = 7,c = 10) == 14
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],a = 1,b = 1,c = 2) == 88
    assert candidate(arr = [5, 8, 12, 15, 18, 22, 25, 28, 31],a = 5,b = 5,c = 10) == 7
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],a = 2,b = 2,c = 4) == 44
    assert candidate(arr = [10, 20, 20, 20, 30, 40, 50, 60, 70, 80],a = 5,b = 5,c = 10) == 1
    assert candidate(arr = [7, 1, 5, 3, 6, 4, 2, 8, 9],a = 2,b = 3,c = 4) == 20
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],a = 2,b = 2,c = 2) == 8
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],a = 0,b = 0,c = 0) == 1140
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900],a = 150,b = 250,c = 350) == 13
    assert candidate(arr = [5, 8, 12, 15, 20, 22, 25],a = 5,b = 6,c = 7) == 4
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],a = 0,b = 0,c = 0) == 120
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],a = 10,b = 20,c = 30) == 25
    assert candidate(arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],a = 5,b = 10,c = 15) == 25
    assert candidate(arr = [5, 8, 8, 10, 15, 17],a = 5,b = 3,c = 8) == 5
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33],a = 4,b = 4,c = 8) == 7
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],a = 1,b = 1,c = 2) == 54
    assert candidate(arr = [15, 10, 15, 10, 15, 10, 15],a = 5,b = 5,c = 10) == 35
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],a = 100,b = 200,c = 300) == 15
    assert candidate(arr = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0],a = 100,b = 200,c = 300) == 17
    assert candidate(arr = [9, 7, 5, 3, 1, 2, 4, 6, 8, 0],a = 1,b = 2,c = 3) == 8
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],a = 2,b = 2,c = 3) == 37
    assert candidate(arr = [7, 3, 19, 5, 11, 13, 17, 15, 2, 9],a = 6,b = 5,c = 10) == 24
    assert candidate(arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],a = 1,b = 1,c = 2) == 132
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],a = 0,b = 0,c = 0) == 120
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],a = 2,b = 3,c = 4) == 58
    assert candidate(arr = [5, 8, 2, 3, 6, 9, 10, 12],a = 3,b = 4,c = 5) == 16
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],a = 1,b = 2,c = 3) == 25
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],a = 1,b = 1,c = 1) == 0
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900],a = 100,b = 100,c = 100) == 0
    assert candidate(arr = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600],a = 50,b = 100,c = 150) == 6
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],a = 1,b = 1,c = 1) == 0
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],a = 150,b = 200,c = 250) == 8
    assert candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],a = 20,b = 30,c = 40) == 64
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],a = 5,b = 5,c = 5) == 120
    assert candidate(arr = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],a = 0,b = 0,c = 0) == 120
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 0,b = 0,c = 1) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 3,b = 3,c = 3) == 324
    assert candidate(arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],a = 1,b = 1,c = 2) == 120
    assert candidate(arr = [4, 9, 1, 3, 13, 12, 7],a = 6,b = 4,c = 10) == 8
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],a = 2,b = 2,c = 4) == 8
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 1,b = 1,c = 2) == 8
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],a = 1,b = 1,c = 1) == 0
    assert candidate(arr = [8, 12, 15, 20, 25, 30, 35, 40, 45, 50],a = 5,b = 10,c = 15) == 15
    assert candidate(arr = [5, 8, 12, 15, 16, 20, 25, 30],a = 7,b = 5,c = 10) == 12
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],a = 4,b = 8,c = 12) == 15
    assert candidate(arr = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],a = 0,b = 0,c = 0) == 455
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],a = 4,b = 8,c = 12) == 25
    assert candidate(arr = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50],a = 15,b = 25,c = 35) == 17
    assert candidate(arr = [4, 4, 4, 4, 4, 4, 4, 4, 4],a = 0,b = 0,c = 0) == 84
    assert candidate(arr = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],a = 1,b = 1,c = 2) == 9
    assert candidate(arr = [2, 5, 1, 2, 10, 9, 10, 6],a = 4,b = 4,c = 7) == 15
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],a = 0,b = 0,c = 0) == 455
    assert candidate(arr = [5, 3, 7, 8, 2, 1, 9, 6, 4, 10],a = 5,b = 5,c = 5) == 60
    assert candidate(arr = [10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30],a = 10,b = 20,c = 30) == 166
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],a = 9,b = 19,c = 29) == 0
    assert candidate(arr = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],a = 4,b = 5,c = 6) == 0
    assert candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],a = 5,b = 5,c = 5) == 60
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],a = 15,b = 15,c = 20) == 8
    assert candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],a = 10,b = 10,c = 10) == 120
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],a = 2,b = 3,c = 5) == 8
    assert candidate(arr = [1, 5, 3, 2, 4, 8, 7, 6, 9, 0],a = 3,b = 3,c = 5) == 34
    assert candidate(arr = [34, 23, 54, 28, 90, 56, 78, 45, 12, 67],a = 20,b = 25,c = 30) == 15
    assert candidate(arr = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],a = 5,b = 10,c = 15) == 17
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],a = 1,b = 1,c = 1) == 120
    assert candidate(arr = [7, 3, 8, 1, 4, 6, 5, 2, 9, 0],a = 1,b = 1,c = 2) == 3
    assert candidate(arr = [15, 15, 15, 20, 20, 20, 25, 25, 25],a = 5,b = 5,c = 10) == 66
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],a = 0,b = 0,c = 0) == 1140
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],a = 1,b = 1,c = 2) == 100
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],a = 10,b = 20,c = 30) == 15
    assert candidate(arr = [5, 8, 2, 4, 3, 7, 6, 9, 1],a = 3,b = 4,c = 5) == 35
    assert candidate(arr = [30, 40, 50, 60, 70, 80, 90, 100, 110],a = 10,b = 10,c = 20) == 7
    assert candidate(arr = [2, 2, 2, 2, 2],a = 0,b = 0,c = 0) == 10
    assert candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],a = 15,b = 25,c = 35) == 17
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 1,b = 1,c = 1) == 0
    assert candidate(arr = [1, 4, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],a = 4,b = 5,c = 6) == 214
    assert candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],a = 10,b = 10,c = 20) == 8
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],a = 4,b = 6,c = 8) == 11
    assert candidate(arr = [8, 1, 3, 2, 10, 1, 4],a = 1,b = 2,c = 3) == 4
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],a = 100,b = 150,c = 200) == 8
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10],a = 3,b = 3,c = 4) == 152
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],a = 15,b = 20,c = 25) == 8
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],a = 1,b = 1,c = 1) == 0
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10],a = 1,b = 1,c = 2) == 112
    assert candidate(arr = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],a = 3,b = 4,c = 5) == 0
    assert candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],a = 1,b = 2,c = 3) == 15
    assert candidate(arr = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],a = 1,b = 1,c = 2) == 124
    assert candidate(arr = [5, 1, 4, 1, 3, 6, 2],a = 2,b = 3,c = 5) == 14
    assert candidate(arr = [5, 8, 12, 15, 16, 23, 42],a = 5,b = 7,c = 10) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],a = 0,b = 0,c = 0) == 0


