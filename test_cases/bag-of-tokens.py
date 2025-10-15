def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400],power = 200) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400],power = 200) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400],power = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400],power = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [71, 55, 82],power = 54) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [71, 55, 82],power = 54) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400],power = 500) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400],power = 500) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100],power = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100],power = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [],power = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [],power = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [50, 50, 50, 50, 50],power = 150) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [50, 50, 50, 50, 50],power = 150) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400, 500],power = 250) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400, 500],power = 250) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [50, 100, 150, 200, 250],power = 200) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [50, 100, 150, 200, 250],power = 200) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [80, 90, 95],power = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [80, 90, 95],power = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 150, 200, 250, 300],power = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 150, 200, 250, 300],power = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400, 500],power = 300) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400, 500],power = 300) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [],power = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [],power = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1000, 2000, 3000, 4000],power = 1500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1000, 2000, 3000, 4000],power = 1500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5],power = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5],power = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400],power = 300) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400],power = 300) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [200, 100],power = 150) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [200, 100],power = 150) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [50, 100, 150, 200, 250],power = 200) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [50, 100, 150, 200, 250],power = 200) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],power = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],power = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [50, 50, 50, 50],power = 150) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [50, 50, 50, 50],power = 150) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [71, 55, 82],power = 54) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [71, 55, 82],power = 54) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [500],power = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [500],power = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [200, 100],power = 150) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [200, 100],power = 150) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [75, 150, 225, 300, 375, 450],power = 225) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [75, 150, 225, 300, 375, 450],power = 225) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 10, 15, 20],power = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 10, 15, 20],power = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [],power = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [],power = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [7, 8, 9, 10, 11],power = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [7, 8, 9, 10, 11],power = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],power = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],power = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 100, 100, 100, 100, 100],power = 300) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 100, 100, 100, 100, 100],power = 300) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5],power = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5],power = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 100, 100, 100],power = 300) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 100, 100, 100],power = 300) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400],power = 400) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400],power = 400) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400],power = 200) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400],power = 200) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],power = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],power = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 250) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 250) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],power = 1500) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],power = 1500) == 16: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 500) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 500) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000],power = 1000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000],power = 1000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],power = 200) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],power = 200) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],power = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],power = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 550) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 550) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 5000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 5000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],power = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],power = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [25, 50, 75, 100, 125, 150, 175, 200],power = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [25, 50, 75, 100, 125, 150, 175, 200],power = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],power = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],power = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],power = 100) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],power = 100) == 11: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],power = 1000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],power = 1000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],power = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],power = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],power = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],power = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 10, 100, 1000, 10000, 100000],power = 50000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 10, 100, 1000, 10000, 100000],power = 50000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 1500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 1500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],power = 75) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],power = 75) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],power = 1000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],power = 1000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],power = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],power = 100) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],power = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],power = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 1000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 1000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 10, 20, 25, 50, 100],power = 55) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 10, 20, 25, 50, 100],power = 55) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],power = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],power = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],power = 1024) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],power = 1024) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],power = 500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],power = 500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 7, 8, 10, 12],power = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 7, 8, 10, 12],power = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],power = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],power = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],power = 1000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],power = 1000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],power = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],power = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],power = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],power = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 250) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 250) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400, 500],power = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400, 500],power = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 75) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 75) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [300, 200, 100, 400, 500],power = 250) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [300, 200, 100, 400, 500],power = 250) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],power = 200) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],power = 200) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],power = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],power = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [500, 400, 300, 200, 100, 50, 25, 10],power = 1000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [500, 400, 300, 200, 100, 50, 25, 10],power = 1000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],power = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],power = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],power = 250) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],power = 250) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [90, 95, 100, 105, 110, 115, 120, 125, 130, 135],power = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [90, 95, 100, 105, 110, 115, 120, 125, 130, 135],power = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 70) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 70) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 100) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 100) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],power = 100) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],power = 100) == 11: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],power = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],power = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],power = 50) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],power = 50) == 11: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],power = 500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],power = 500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 1000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 1000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],power = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],power = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],power = 200) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],power = 200) == 10: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 10, 100, 1000, 10000],power = 5000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 10, 100, 1000, 10000],power = 5000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],power = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],power = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],power = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],power = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],power = 100) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],power = 100) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],power = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],power = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],power = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],power = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [300, 200, 400, 100, 500],power = 250) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [300, 200, 400, 100, 500],power = 250) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],power = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],power = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 300) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 300) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],power = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],power = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],power = 200) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],power = 200) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [500, 200, 300, 100, 400, 600, 700, 800, 900, 1000],power = 400) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [500, 200, 300, 100, 400, 600, 700, 800, 900, 1000],power = 400) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tokens = [300, 200, 100, 400, 500, 600],power = 350) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tokens = [300, 200, 100, 400, 500, 600],power = 350) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tokens = [100, 200, 300, 400],power = 200) == 2
    assert candidate(tokens = [100, 200, 300, 400],power = 100) == 1
    assert candidate(tokens = [71, 55, 82],power = 54) == 0
    assert candidate(tokens = [100, 200, 300, 400],power = 500) == 2
    assert candidate(tokens = [100],power = 50) == 0
    assert candidate(tokens = [],power = 0) == 0
    assert candidate(tokens = [50, 50, 50, 50, 50],power = 150) == 3
    assert candidate(tokens = [100, 200, 300, 400, 500],power = 250) == 2
    assert candidate(tokens = [50, 100, 150, 200, 250],power = 200) == 2
    assert candidate(tokens = [80, 90, 95],power = 100) == 1
    assert candidate(tokens = [100, 150, 200, 250, 300],power = 100) == 1
    assert candidate(tokens = [100, 200, 300, 400, 500],power = 300) == 2
    assert candidate(tokens = [],power = 1000) == 0
    assert candidate(tokens = [1000, 2000, 3000, 4000],power = 1500) == 1
    assert candidate(tokens = [1, 2, 3, 4, 5],power = 3) == 2
    assert candidate(tokens = [100, 200, 300, 400],power = 300) == 2
    assert candidate(tokens = [200, 100],power = 150) == 1
    assert candidate(tokens = [50, 100, 150, 200, 250],power = 200) == 2
    assert candidate(tokens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],power = 5) == 5
    assert candidate(tokens = [50, 50, 50, 50],power = 150) == 3
    assert candidate(tokens = [71, 55, 82],power = 54) == 0
    assert candidate(tokens = [500],power = 1000) == 1
    assert candidate(tokens = [200, 100],power = 150) == 1
    assert candidate(tokens = [75, 150, 225, 300, 375, 450],power = 225) == 2
    assert candidate(tokens = [5, 10, 15, 20],power = 50) == 4
    assert candidate(tokens = [],power = 100) == 0
    assert candidate(tokens = [7, 8, 9, 10, 11],power = 20) == 2
    assert candidate(tokens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],power = 0) == 0
    assert candidate(tokens = [100, 100, 100, 100, 100, 100],power = 300) == 3
    assert candidate(tokens = [1, 2, 3, 4, 5],power = 5) == 3
    assert candidate(tokens = [100, 100, 100, 100],power = 300) == 3
    assert candidate(tokens = [100, 200, 300, 400],power = 400) == 2
    assert candidate(tokens = [100, 200, 300, 400],power = 200) == 2
    assert candidate(tokens = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],power = 10) == 3
    assert candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 250) == 4
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],power = 1500) == 16
    assert candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 500) == 4
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 500) == 9
    assert candidate(tokens = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000],power = 1000) == 8
    assert candidate(tokens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],power = 200) == 6
    assert candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],power = 30) == 7
    assert candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 550) == 4
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 50) == 4
    assert candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 5000) == 9
    assert candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],power = 10) == 6
    assert candidate(tokens = [25, 50, 75, 100, 125, 150, 175, 200],power = 100) == 3
    assert candidate(tokens = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],power = 100) == 4
    assert candidate(tokens = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],power = 100) == 11
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],power = 1000) == 14
    assert candidate(tokens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],power = 5) == 5
    assert candidate(tokens = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],power = 10000) == 1
    assert candidate(tokens = [1, 10, 100, 1000, 10000, 100000],power = 50000) == 5
    assert candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 1500) == 5
    assert candidate(tokens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],power = 75) == 9
    assert candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],power = 1000) == 9
    assert candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],power = 100) == 13
    assert candidate(tokens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],power = 100) == 5
    assert candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 1000) == 5
    assert candidate(tokens = [5, 10, 20, 25, 50, 100],power = 55) == 4
    assert candidate(tokens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],power = 50) == 4
    assert candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],power = 1024) == 10
    assert candidate(tokens = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],power = 500) == 5
    assert candidate(tokens = [5, 7, 8, 10, 12],power = 15) == 2
    assert candidate(tokens = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],power = 25) == 5
    assert candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],power = 1000) == 9
    assert candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],power = 10) == 8
    assert candidate(tokens = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],power = 10) == 5
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 250) == 6
    assert candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 100) == 4
    assert candidate(tokens = [100, 200, 300, 400, 500],power = 1) == 0
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 75) == 6
    assert candidate(tokens = [300, 200, 100, 400, 500],power = 250) == 2
    assert candidate(tokens = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],power = 200) == 4
    assert candidate(tokens = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],power = 10) == 9
    assert candidate(tokens = [500, 400, 300, 200, 100, 50, 25, 10],power = 1000) == 6
    assert candidate(tokens = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],power = 1023) == 10
    assert candidate(tokens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],power = 500) == 4
    assert candidate(tokens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],power = 250) == 10
    assert candidate(tokens = [90, 95, 100, 105, 110, 115, 120, 125, 130, 135],power = 100) == 1
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 70) == 6
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 100) == 6
    assert candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],power = 100) == 11
    assert candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],power = 15) == 5
    assert candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],power = 50) == 11
    assert candidate(tokens = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],power = 500) == 5
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],power = 1000) == 13
    assert candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],power = 20) == 7
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 10) == 4
    assert candidate(tokens = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],power = 200) == 10
    assert candidate(tokens = [1, 10, 100, 1000, 10000],power = 5000) == 4
    assert candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],power = 10) == 4
    assert candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],power = 100) == 14
    assert candidate(tokens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],power = 100) == 6
    assert candidate(tokens = [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],power = 100) == 1
    assert candidate(tokens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],power = 150) == 5
    assert candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],power = 5) == 4
    assert candidate(tokens = [300, 200, 400, 100, 500],power = 250) == 2
    assert candidate(tokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],power = 25) == 6
    assert candidate(tokens = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],power = 300) == 4
    assert candidate(tokens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],power = 15) == 6
    assert candidate(tokens = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],power = 200) == 4
    assert candidate(tokens = [500, 200, 300, 100, 400, 600, 700, 800, 900, 1000],power = 400) == 4
    assert candidate(tokens = [300, 200, 100, 400, 500, 600],power = 350) == 2


