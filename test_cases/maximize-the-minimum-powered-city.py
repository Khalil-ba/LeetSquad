def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 4, 5, 0],r = 1,k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 4, 5, 0],r = 1,k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0],r = 2,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0],r = 2,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0],r = 2,k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0],r = 2,k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 5, 7, 9],r = 2,k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 5, 7, 9],r = 2,k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(stations = [3, 3, 3, 3, 3],r = 1,k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [3, 3, 3, 3, 3],r = 1,k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50],r = 3,k = 20) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50],r = 3,k = 20) == 120: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 0, 1, 0, 1, 0, 1],r = 2,k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 0, 1, 0, 1, 0, 1],r = 2,k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0],r = 2,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0],r = 2,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0],r = 2,k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0],r = 2,k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50],r = 3,k = 100) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50],r = 3,k = 100) == 200: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],r = 3,k = 15) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],r = 3,k = 15) == 27: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 5, 5, 5, 5],r = 2,k = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 5, 5, 5, 5],r = 2,k = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50],r = 2,k = 10) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50],r = 2,k = 10) == 70: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 0, 3, 0, 2],r = 2,k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 0, 3, 0, 2],r = 2,k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(stations = [4, 4, 4, 4],r = 0,k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [4, 4, 4, 4],r = 0,k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 3,k = 15) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 3,k = 15) == 27: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 5,k = 150) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 5,k = 150) == 360: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],r = 5,k = 300) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],r = 5,k = 300) == 480: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(stations = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],r = 1,k = 10) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],r = 1,k = 10) == 22: {e}')
    
    total += 1
    try:
        result = candidate(stations = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],r = 5,k = 100) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],r = 5,k = 100) == 68: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 0,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 0,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 25) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 25) == 12: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],r = 1,k = 50) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],r = 1,k = 50) == 37: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],r = 5,k = 300) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],r = 5,k = 300) == 405: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],r = 5,k = 30) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],r = 5,k = 30) == 45: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 0,k = 50) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 0,k = 50) == 36: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 1,k = 500) == 262
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 1,k = 500) == 262: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 1,k = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 1,k = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 5,k = 5000) == 7100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 5,k = 5000) == 7100: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],r = 3,k = 150) == 185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],r = 3,k = 150) == 185: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 4,k = 50) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 4,k = 50) == 52: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 0, 2, 5, 4, 2, 1, 0, 5],r = 2,k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 0, 2, 5, 4, 2, 1, 0, 5],r = 2,k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],r = 2,k = 50000) == 41500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],r = 2,k = 50000) == 41500: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 1,k = 45) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 1,k = 45) == 25: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 10,k = 50) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 10,k = 50) == 61: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 5,k = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 5,k = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0],r = 3,k = 50) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0],r = 3,k = 50) == 35: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],r = 5,k = 1000000) == 1600000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],r = 5,k = 1000000) == 1600000: {e}')
    
    total += 1
    try:
        result = candidate(stations = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],r = 4,k = 30) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],r = 4,k = 30) == 60: {e}')
    
    total += 1
    try:
        result = candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],r = 3,k = 50) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],r = 3,k = 50) == 40: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 4,k = 100) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 4,k = 100) == 60: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 2,k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 2,k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 0, 0, 0, 0, 1],r = 2,k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 0, 0, 0, 0, 1],r = 2,k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0],r = 2,k = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0],r = 2,k = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],r = 2,k = 100) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],r = 2,k = 100) == 145: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],r = 1,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],r = 1,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 10,k = 500) == 566
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 10,k = 500) == 566: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 3,k = 150) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 3,k = 150) == 250: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],r = 6,k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],r = 6,k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],r = 4,k = 1000) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],r = 4,k = 1000) == 900: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 4,k = 250) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 4,k = 250) == 400: {e}')
    
    total += 1
    try:
        result = candidate(stations = [50, 40, 30, 20, 10],r = 1,k = 50) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [50, 40, 30, 20, 10],r = 1,k = 50) == 80: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 5,k = 150) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 5,k = 150) == 138: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 3,k = 100) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 3,k = 100) == 80: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 2,k = 60) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 2,k = 60) == 120: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 4,k = 500) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 4,k = 500) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100000, 0, 100000, 0, 100000, 0, 100000],r = 3,k = 500000) == 700000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100000, 0, 100000, 0, 100000, 0, 100000],r = 3,k = 500000) == 700000: {e}')
    
    total += 1
    try:
        result = candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 4,k = 30) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 4,k = 30) == 37: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],r = 5,k = 5000) == 11000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],r = 5,k = 5000) == 11000: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],r = 2,k = 50) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],r = 2,k = 50) == 39: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 1,k = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 1,k = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 4,k = 250) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 4,k = 250) == 400: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 0,k = 45) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 0,k = 45) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],r = 2,k = 25) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],r = 2,k = 25) == 18: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 0, 100, 0, 100],r = 2,k = 50) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 0, 100, 0, 100],r = 2,k = 50) == 250: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 1,k = 100) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 1,k = 100) == 125: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 4,k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 4,k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 2,k = 20) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 2,k = 20) == 26: {e}')
    
    total += 1
    try:
        result = candidate(stations = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],r = 5,k = 100) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],r = 5,k = 100) == 350: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 7,k = 100) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 7,k = 100) == 134: {e}')
    
    total += 1
    try:
        result = candidate(stations = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],r = 3,k = 100) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],r = 3,k = 100) == 160: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 1,k = 100) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 1,k = 100) == 40: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 1,k = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 1,k = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 2,k = 30) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 2,k = 30) == 28: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],r = 3,k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],r = 3,k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55],r = 1,k = 100) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55],r = 1,k = 100) == 110: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 8,k = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 8,k = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 1,k = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 1,k = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],r = 4,k = 20000) == 35000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],r = 4,k = 20000) == 35000: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],r = 1,k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],r = 1,k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 3,k = 30) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 3,k = 30) == 33: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],r = 3,k = 150) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],r = 3,k = 150) == 125: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],r = 2,k = 20) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],r = 2,k = 20) == 26: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 4,k = 20) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 4,k = 20) == 35: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0, 0],r = 1,k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0, 0],r = 1,k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],r = 5,k = 200) == 305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],r = 5,k = 200) == 305: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 2,k = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 2,k = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stations = [9, 7, 5, 3, 1, 0, 2, 4, 6, 8],r = 4,k = 25) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [9, 7, 5, 3, 1, 0, 2, 4, 6, 8],r = 4,k = 25) == 35: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 2, 5, 7, 8, 6, 4, 9, 0],r = 2,k = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 2, 5, 7, 8, 6, 4, 9, 0],r = 2,k = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 5,k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 5,k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 40, 30, 20, 10],r = 2,k = 50) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 40, 30, 20, 10],r = 2,k = 50) == 85: {e}')
    
    total += 1
    try:
        result = candidate(stations = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],r = 5,k = 20) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],r = 5,k = 20) == 43: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 0, 100, 0, 100, 0, 100],r = 2,k = 200) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 0, 100, 0, 100, 0, 100],r = 2,k = 200) == 300: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 5,k = 25) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 5,k = 25) == 46: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],r = 3,k = 100) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],r = 3,k = 100) == 73: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0],r = 4,k = 100) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0],r = 4,k = 100) == 300: {e}')
    
    total += 1
    try:
        result = candidate(stations = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],r = 3,k = 100) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],r = 3,k = 100) == 190: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],r = 0,k = 500) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],r = 0,k = 500) == 100: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 50) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 50) == 35: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 4,k = 500) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 4,k = 500) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 5,k = 2000) == 4100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 5,k = 2000) == 4100: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 2, 5, 4, 6, 7, 8, 9, 0],r = 2,k = 20) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 2, 5, 4, 6, 7, 8, 9, 0],r = 2,k = 20) == 21: {e}')
    
    total += 1
    try:
        result = candidate(stations = [0, 0, 0, 0, 0],r = 1,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [0, 0, 0, 0, 0],r = 1,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1],r = 3,k = 25) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1],r = 3,k = 25) == 32: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 2, 1, 4, 1, 2, 3],r = 2,k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 2, 1, 4, 1, 2, 3],r = 2,k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000],r = 1,k = 10000) == 3751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000],r = 1,k = 10000) == 3751: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(stations = [1, 2, 4, 5, 0],r = 1,k = 2) == 5
    assert candidate(stations = [0, 0, 0, 0, 0],r = 2,k = 5) == 5
    assert candidate(stations = [0, 0, 0, 0, 0],r = 2,k = 10) == 10
    assert candidate(stations = [1, 3, 5, 7, 9],r = 2,k = 5) == 14
    assert candidate(stations = [3, 3, 3, 3, 3],r = 1,k = 5) == 8
    assert candidate(stations = [10, 20, 30, 40, 50],r = 3,k = 20) == 120
    assert candidate(stations = [1, 0, 1, 0, 1, 0, 1],r = 2,k = 3) == 3
    assert candidate(stations = [0, 0, 0, 0],r = 2,k = 5) == 5
    assert candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 2) == 3
    assert candidate(stations = [0, 0, 0, 0],r = 2,k = 10) == 10
    assert candidate(stations = [10, 20, 30, 40, 50],r = 3,k = 100) == 200
    assert candidate(stations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],r = 3,k = 15) == 27
    assert candidate(stations = [5, 5, 5, 5, 5],r = 2,k = 5) == 20
    assert candidate(stations = [10, 20, 30, 40, 50],r = 2,k = 10) == 70
    assert candidate(stations = [1, 0, 3, 0, 2],r = 2,k = 3) == 7
    assert candidate(stations = [4, 4, 4, 4],r = 0,k = 3) == 4
    assert candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 3,k = 15) == 27
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 5,k = 150) == 360
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],r = 5,k = 300) == 480
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 10) == 5
    assert candidate(stations = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],r = 1,k = 10) == 22
    assert candidate(stations = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],r = 5,k = 100) == 68
    assert candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 4) == 2
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 20) == 20
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 0,k = 5) == 1
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 25) == 12
    assert candidate(stations = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],r = 1,k = 50) == 37
    assert candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],r = 5,k = 300) == 405
    assert candidate(stations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],r = 5,k = 30) == 45
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 0,k = 50) == 36
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 20) == 10
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 1,k = 500) == 262
    assert candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 1,k = 50) == 25
    assert candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 5,k = 5000) == 7100
    assert candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],r = 3,k = 150) == 185
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 4,k = 50) == 52
    assert candidate(stations = [1, 3, 0, 2, 5, 4, 2, 1, 0, 5],r = 2,k = 10) == 10
    assert candidate(stations = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],r = 2,k = 50000) == 41500
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 1,k = 45) == 25
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 10,k = 50) == 61
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 5,k = 10) == 11
    assert candidate(stations = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0],r = 3,k = 50) == 35
    assert candidate(stations = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],r = 5,k = 1000000) == 1600000
    assert candidate(stations = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],r = 4,k = 30) == 60
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],r = 3,k = 50) == 40
    assert candidate(stations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 4,k = 100) == 60
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 2,k = 10) == 5
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 10) == 15
    assert candidate(stations = [1, 0, 0, 0, 0, 1],r = 2,k = 3) == 2
    assert candidate(stations = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0],r = 2,k = 10) == 12
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],r = 2,k = 100) == 145
    assert candidate(stations = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],r = 1,k = 5) == 2
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 10,k = 500) == 566
    assert candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 3,k = 150) == 250
    assert candidate(stations = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],r = 6,k = 10) == 6
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],r = 4,k = 1000) == 900
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 4,k = 250) == 400
    assert candidate(stations = [50, 40, 30, 20, 10],r = 1,k = 50) == 80
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 5,k = 150) == 138
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 3,k = 100) == 80
    assert candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 2,k = 60) == 120
    assert candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 4,k = 500) == 2000
    assert candidate(stations = [100000, 0, 100000, 0, 100000, 0, 100000],r = 3,k = 500000) == 700000
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 4,k = 30) == 37
    assert candidate(stations = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],r = 5,k = 5000) == 11000
    assert candidate(stations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],r = 2,k = 50) == 39
    assert candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 1,k = 10) == 13
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 4,k = 250) == 400
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 0,k = 45) == 10
    assert candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 10) == 3
    assert candidate(stations = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],r = 2,k = 25) == 18
    assert candidate(stations = [100, 0, 100, 0, 100],r = 2,k = 50) == 250
    assert candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 1,k = 100) == 125
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 4,k = 10) == 10
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 2,k = 20) == 26
    assert candidate(stations = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],r = 5,k = 100) == 350
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 7,k = 100) == 134
    assert candidate(stations = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],r = 3,k = 100) == 160
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 1,k = 100) == 40
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 1,k = 10) == 12
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 2,k = 30) == 28
    assert candidate(stations = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],r = 3,k = 5) == 3
    assert candidate(stations = [5, 15, 25, 35, 45, 55],r = 1,k = 100) == 110
    assert candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 3) == 4
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 8,k = 20) == 19
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 1,k = 10) == 2
    assert candidate(stations = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],r = 4,k = 20000) == 35000
    assert candidate(stations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],r = 1,k = 5) == 8
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 50) == 25
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 3,k = 30) == 33
    assert candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],r = 3,k = 150) == 125
    assert candidate(stations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],r = 2,k = 20) == 26
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 4,k = 20) == 35
    assert candidate(stations = [0, 0, 0, 0, 0, 0],r = 1,k = 10) == 5
    assert candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],r = 5,k = 200) == 305
    assert candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 2) == 3
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 2,k = 20) == 10
    assert candidate(stations = [9, 7, 5, 3, 1, 0, 2, 4, 6, 8],r = 4,k = 25) == 35
    assert candidate(stations = [1, 3, 2, 5, 7, 8, 6, 4, 9, 0],r = 2,k = 10) == 14
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 5,k = 20) == 20
    assert candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 5) == 2
    assert candidate(stations = [10, 20, 30, 40, 50, 40, 30, 20, 10],r = 2,k = 50) == 85
    assert candidate(stations = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],r = 5,k = 20) == 43
    assert candidate(stations = [100, 0, 100, 0, 100, 0, 100],r = 2,k = 200) == 300
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 5,k = 25) == 46
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],r = 3,k = 100) == 73
    assert candidate(stations = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0],r = 4,k = 100) == 300
    assert candidate(stations = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],r = 3,k = 100) == 190
    assert candidate(stations = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],r = 0,k = 500) == 100
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 50) == 35
    assert candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 4,k = 500) == 2000
    assert candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 5,k = 2000) == 4100
    assert candidate(stations = [1, 3, 2, 5, 4, 6, 7, 8, 9, 0],r = 2,k = 20) == 21
    assert candidate(stations = [0, 0, 0, 0, 0],r = 1,k = 5) == 2
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1],r = 3,k = 25) == 32
    assert candidate(stations = [1, 3, 2, 1, 4, 1, 2, 3],r = 2,k = 5) == 8
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 20) == 20
    assert candidate(stations = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000],r = 1,k = 10000) == 3751


