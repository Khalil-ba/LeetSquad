def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],k = 100000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],k = 100000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5],k = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5],k = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8],k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8],k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],k = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],k = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 2, 4, 3],k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 2, 4, 3],k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10],k = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10],k = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],k = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],k = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 3, 6, 5, 4],k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 3, 6, 5, 4],k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14],k = 14) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14],k = 14) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 0, 100000, 0, 100000, 0, 100000, 0],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 0, 100000, 0, 100000, 0, 100000, 0],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992],k = 99999) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992],k = 99999) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992],k = 100000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992],k = 100000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 0, 49999, 1, 49998, 2, 49997, 3, 49996, 4, 49995, 5, 49994, 6, 49993, 7],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 0, 49999, 1, 49998, 2, 49997, 3, 49996, 4, 49995, 5, 49994, 6, 49993, 7],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80],k = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80],k = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],k = 160) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],k = 160) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 7, 8, 6],k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 7, 8, 6],k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 16) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 16) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 1200) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 1200) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 3, 0, 5, 0, 7, 0, 9],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 3, 0, 5, 0, 7, 0, 9],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 1, 99999, 1, 99999, 1, 99999, 1],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 1, 99999, 1, 99999, 1, 99999, 1],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240],k = 240) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240],k = 240) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 55) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 55) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],k = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],k = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 100000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 100000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 0],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 0],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 100000, 0, 0, 0, 0, 100000, 100000, 100000, 100000],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 100000, 0, 0, 0, 0, 100000, 100000, 100000, 100000],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 8) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 8) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40],k = 40) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40],k = 40) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 500, 400, 300, 200, 100, 0],k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 500, 400, 300, 200, 100, 0],k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 0, 50000, 0, 50000, 0, 50000, 0, 50000, 0],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 0, 50000, 0, 50000, 0, 50000, 0, 50000, 0],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 20000, 30000, 40000, 50000, 40000, 30000, 20000, 10000, 0],k = 50000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 20000, 30000, 40000, 50000, 40000, 30000, 20000, 10000, 0],k = 50000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30000, 20000, 10000, 0, 10000, 20000, 30000, 40000, 50000, 60000, 50000, 40000, 30000, 20000, 10000, 0],k = 60000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30000, 20000, 10000, 0, 10000, 20000, 30000, 40000, 50000, 60000, 50000, 40000, 30000, 20000, 10000, 0],k = 60000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112],k = 112) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112],k = 112) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 59) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 59) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 24, 42, 24, 42, 24, 42, 24, 42, 24, 42, 24],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 24, 42, 24, 42, 24, 42, 24, 42, 24, 42, 24],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 19) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 19) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 5, 15, 5, 20, 5, 25, 5, 30],k = 30) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 5, 15, 5, 20, 5, 25, 5, 30],k = 30) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000, 0],k = 5000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000, 0],k = 5000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5],k = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5],k = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 500, 400, 300, 200, 100],k = 500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 500, 400, 300, 200, 100],k = 500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 23) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 23) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 4, 5, 3, 2, 5, 4],k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 4, 5, 3, 2, 5, 4],k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],k = 80) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],k = 80) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 4, 1, 0, 2, 3, 4, 1, 0, 2, 3, 4, 1, 0],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 4, 1, 0, 2, 3, 4, 1, 0, 2, 3, 4, 1, 0],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 7, 9, 2, 8, 4, 6, 0],k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 7, 9, 2, 8, 4, 6, 0],k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 16) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 16) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 31) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 31) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 0],k = 60) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 0],k = 60) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 2, 4, 6, 7, 8],k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 2, 4, 6, 7, 8],k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4],k = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4],k = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0],k = 99999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0],k = 99999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],k = 100000) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5],k = 10) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8],k = 8) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],k = 15) == 3
    assert candidate(nums = [1, 0, 1, 2, 4, 3],k = 4) == 2
    assert candidate(nums = [5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 4
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 0
    assert candidate(nums = [0, 2, 4, 6, 8, 10],k = 10) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],k = 100) == 4
    assert candidate(nums = [0, 1, 2, 3, 3, 6, 5, 4],k = 6) == 2
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1],k = 1) == 0
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2],k = 2) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14],k = 14) == 3
    assert candidate(nums = [100000, 0, 100000, 0, 100000, 0, 100000, 0],k = 100000) == 0
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3],k = 3) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 9) == 0
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992],k = 99999) == 3
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992],k = 100000) == 3
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 9
    assert candidate(nums = [50000, 0, 49999, 1, 49998, 2, 49997, 3, 49996, 4, 49995, 5, 49994, 6, 49993, 7],k = 100000) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0
    assert candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80],k = 100) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],k = 160) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 14
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 9) == 4
    assert candidate(nums = [1, 3, 2, 4, 5, 7, 8, 6],k = 8) == 1
    assert candidate(nums = [99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0],k = 100000) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 16) == 7
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 1200) == 5
    assert candidate(nums = [0, 1, 0, 3, 0, 5, 0, 7, 0, 9],k = 10) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 20) == 9
    assert candidate(nums = [99999, 1, 99999, 1, 99999, 1, 99999, 1],k = 100000) == 0
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240],k = 240) == 14
    assert candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],k = 55) == 5
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],k = 6) == 7
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 11) == 5
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 30) == 7
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 100000) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 0],k = 100) == 0
    assert candidate(nums = [100000, 100000, 100000, 100000, 0, 0, 0, 0, 100000, 100000, 100000, 100000],k = 100000) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 8) == 6
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40],k = 40) == 3
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 2) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 500, 400, 300, 200, 100, 0],k = 1000) == 0
    assert candidate(nums = [50000, 0, 50000, 0, 50000, 0, 50000, 0, 50000, 0],k = 100000) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 9
    assert candidate(nums = [10000, 20000, 30000, 40000, 50000, 40000, 30000, 20000, 10000, 0],k = 50000) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 10) == 4
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2],k = 10) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 4
    assert candidate(nums = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 15) == 7
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == 0
    assert candidate(nums = [30000, 20000, 10000, 0, 10000, 20000, 30000, 40000, 50000, 60000, 50000, 40000, 30000, 20000, 10000, 0],k = 60000) == 3
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 2) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112],k = 112) == 7
    assert candidate(nums = [99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0],k = 100000) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 59) == 14
    assert candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],k = 4) == 4
    assert candidate(nums = [42, 24, 42, 24, 42, 24, 42, 24, 42, 24, 42, 24],k = 100) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 19) == 4
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 30) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 4
    assert candidate(nums = [5, 10, 5, 15, 5, 20, 5, 25, 5, 30],k = 30) == 4
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000, 0],k = 5000) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5],k = 9) == 5
    assert candidate(nums = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1],k = 3) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 500, 400, 300, 200, 100],k = 500) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 20) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 23) == 5
    assert candidate(nums = [1, 3, 2, 3, 4, 5, 3, 2, 5, 4],k = 5) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 8
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 20) == 4
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],k = 80) == 7
    assert candidate(nums = [2, 1, 3, 4, 1, 0, 2, 3, 4, 1, 0, 2, 3, 4, 1, 0],k = 4) == 3
    assert candidate(nums = [5, 1, 3, 7, 9, 2, 8, 4, 6, 0],k = 10) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 16) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],k = 31) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 12) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 20) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10, 0],k = 60) == 0
    assert candidate(nums = [1, 3, 5, 2, 4, 6, 7, 8],k = 8) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4],k = 9) == 5
    assert candidate(nums = [99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0, 99999, 0],k = 99999) == 0
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1) == 0


