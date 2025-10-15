def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [2, 10, 7, 5, 4, 1, 8, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 10, 7, 5, 4, 1, 8, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 50000, -50000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 50000, -50000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 50000, -50000, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 50000, -50000, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -4, 19, 1, 8, -2, -3, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -4, 19, 1, 8, -2, -3, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 4, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 4, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 97, 95, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 65, 63, 61, 59, 57, 55, 53, 51]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 97, 95, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 65, 63, 61, 59, 57, 55, 53, 51]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990, -99989, -99988, -99987, -99986, -99985, -99984, -99983, -99982, -99981, -99980, -99979, -99978, -99977, -99976, -99975, -99974, -99973, -99972, -99971, -99970, 100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990, -99989, -99988, -99987, -99986, -99985, -99984, -99983, -99982, -99981, -99980, -99979, -99978, -99977, -99976, -99975, -99974, -99973, -99972, -99971, -99970, 100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50000, 49999, -49999, 49998, -49998, 49997, -49997, 49996, -49996, 49995]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50000, 49999, -49999, 49998, -49998, 49997, -49997, 49996, -49996, 49995]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 5, 4, 6, 7, 8, 9, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 5, 4, 6, 7, 8, 9, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-7, 10, 5, -3, 2, 8, 0, -1, 6, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-7, 10, 5, -3, 2, 8, 0, -1, 6, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 1, 9, 5, 2, 8, 4, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 1, 9, 5, 2, 8, 4, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 0, -10, -20, -30, 40, 50, 60, 70, 80, 90, 100]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 0, -10, -20, -30, 40, 50, 60, 70, 80, 90, 100]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 99999, 2, 99998, 3, 99997, 4, 99996, 5, 99995]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 99999, 2, 99998, 3, 99997, 4, 99996, 5, 99995]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -5, -3, -7, -2, -6, -4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -5, -3, -7, -2, -6, -4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 3, 5, 2, 7, 6, 1, 8, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 3, 5, 2, 7, 6, 1, 8, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000, 75000, -75000, 12500, -12500]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000, 75000, -75000, 12500, -12500]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 5, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 5, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 8, 3, 7, 6, 4, 10, 1, 9]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 8, 3, 7, 6, 4, 10, 1, 9]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 2, 3, 6, 8, 7, 10, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 2, 3, 6, 8, 7, 10, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -10, -3, -1, -8, -2, -7, -4, -6, -9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -10, -3, -1, -8, -2, -7, -4, -6, -9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 3, 8, 5, 2, 7, 4, 6, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 3, 8, 5, 2, 7, 4, 6, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 100, 10, 1, 0, -1, -10, -100, -1000, 500, 50, 5, 0.5, 0.05, 0.005, 0.0005, 5e-05]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 100, 10, 1, 0, -1, -10, -100, -1000, 500, 50, 5, 0.5, 0.05, 0.005, 0.0005, 5e-05]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500, 6250, -6250]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500, 6250, -6250]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 8, 6, 7, 3, 5, 1, 9, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 8, 6, 7, 3, 5, 1, 9, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100000, 100000, 1, -1, 50000, -50000, 99999, -99999, 42, -42]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100000, 100000, 1, -1, 50000, -50000, 99999, -99999, 42, -42]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 5, 2, 8, 6, 4, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 5, 2, 8, 6, 4, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 18, 19, 16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 18, 19, 16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 3, 15, 1, 12, 7, 8, 6, 10, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 3, 15, 1, 12, 7, 8, 6, 10, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 7, 17, 27, 37, 47, 57, 67, 77, 87, 97, 6, 16, 26, 36, 46, 56, 66, 76, 86, 96, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 4, 14, 24, 34, 44, 54, 64, 74, 84, 94, 3, 13, 23, 33, 43, 53, 63, 73, 83, 93, 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 1, 11, 21, 31, 41, 51, 61, 71, 81, 91]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 7, 17, 27, 37, 47, 57, 67, 77, 87, 97, 6, 16, 26, 36, 46, 56, 66, 76, 86, 96, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 4, 14, 24, 34, 44, 54, 64, 74, 84, 94, 3, 13, 23, 33, 43, 53, 63, 73, 83, 93, 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 1, 11, 21, 31, 41, 51, 61, 71, 81, 91]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996, 6, 99995, 7, 99994, 8, 99993, 9, 99992, 10, 99991, 11, 99990, 12, 99989, 13, 99988, 14, 99987, 15, 99986, 16, 99985, 17, 99984, 18, 99983, 19, 99982, 20, 99981, 21, 99980, 22, 99979, 23, 99978, 24, 99977, 25, 99976, 26, 99975, 27, 99974, 28, 99973, 29, 99972, 30, 99971]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996, 6, 99995, 7, 99994, 8, 99993, 9, 99992, 10, 99991, 11, 99990, 12, 99989, 13, 99988, 14, 99987, 15, 99986, 16, 99985, 17, 99984, 18, 99983, 19, 99982, 20, 99981, 21, 99980, 22, 99979, 23, 99978, 24, 99977, 25, 99976, 26, 99975, 27, 99974, 28, 99973, 29, 99972, 30, 99971]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [2, 10, 7, 5, 4, 1, 8, 6]) == 5
    assert candidate(nums = [100000, -100000, 50000, -50000]) == 2
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 2
    assert candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(nums = [101]) == 1
    assert candidate(nums = [3, 1, 2, 4, 5]) == 3
    assert candidate(nums = [100000, -100000, 50000, -50000, 0]) == 2
    assert candidate(nums = [0, -4, 19, 1, 8, -2, -3, 5]) == 3
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5]) == 2
    assert candidate(nums = [1, 3, 2]) == 2
    assert candidate(nums = [3, 1]) == 2
    assert candidate(nums = [3, 2, 1]) == 2
    assert candidate(nums = [5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
    assert candidate(nums = [-1, 1]) == 2
    assert candidate(nums = [5, 3, 1, 2, 4]) == 3
    assert candidate(nums = [5, 3, 1, 4, 2]) == 3
    assert candidate(nums = [99, 97, 95, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 65, 63, 61, 59, 57, 55, 53, 51]) == 2
    assert candidate(nums = [-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990, -99989, -99988, -99987, -99986, -99985, -99984, -99983, -99982, -99981, -99980, -99979, -99978, -99977, -99976, -99975, -99974, -99973, -99972, -99971, -99970, 100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970]) == 32
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 2
    assert candidate(nums = [-50000, 49999, -49999, 49998, -49998, 49997, -49997, 49996, -49996, 49995]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [3, 1, 2, 5, 4, 6, 7, 8, 9, 10]) == 3
    assert candidate(nums = [-7, 10, 5, -3, 2, 8, 0, -1, 6, 4]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 2
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
    assert candidate(nums = [3, 7, 1, 9, 5, 2, 8, 4, 6]) == 4
    assert candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500]) == 6
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 2
    assert candidate(nums = [30, 20, 10, 0, -10, -20, -30, 40, 50, 60, 70, 80, 90, 100]) == 8
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [1, 99999, 2, 99998, 3, 99997, 4, 99996, 5, 99995]) == 2
    assert candidate(nums = [-1, -5, -3, -7, -2, -6, -4]) == 4
    assert candidate(nums = [100, 200, 300, 400, 500, -100, -200, -300, -400, -500, 0]) == 7
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14]) == 13
    assert candidate(nums = [9, 3, 5, 2, 7, 6, 1, 8, 4]) == 4
    assert candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000, 75000, -75000, 12500, -12500]) == 2
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == 2
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 2
    assert candidate(nums = [3, 1, 2, 5, 4]) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1]) == 2
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 2
    assert candidate(nums = [5, 2, 8, 3, 7, 6, 4, 10, 1, 9]) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 2
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 2
    assert candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 2
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 2
    assert candidate(nums = [5, 1, 4, 2, 3, 6, 8, 7, 10, 9]) == 4
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [-5, -10, -3, -1, -8, -2, -7, -4, -6, -9]) == 4
    assert candidate(nums = [3, 1, 2]) == 2
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -1]) == 2
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7]) == 22
    assert candidate(nums = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]) == 2
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, 0]) == 3
    assert candidate(nums = [1, 10, 3, 8, 5, 2, 7, 4, 6, 9]) == 2
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 6
    assert candidate(nums = [1000, 100, 10, 1, 0, -1, -10, -100, -1000, 500, 50, 5, 0.5, 0.05, 0.005, 0.0005, 5e-05]) == 9
    assert candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500, 6250, -6250]) == 2
    assert candidate(nums = [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2
    assert candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
    assert candidate(nums = [10, 2, 8, 6, 7, 3, 5, 1, 9, 4]) == 4
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 11
    assert candidate(nums = [-100000, 100000, 1, -1, 50000, -50000, 99999, -99999, 42, -42]) == 2
    assert candidate(nums = [7, 3, 5, 2, 8, 6, 4, 1]) == 4
    assert candidate(nums = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 2
    assert candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert candidate(nums = [20, 18, 19, 16, 17, 14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 1]) == 2
    assert candidate(nums = [9, 3, 15, 1, 12, 7, 8, 6, 10, 2]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6]) == 3
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 7, 17, 27, 37, 47, 57, 67, 77, 87, 97, 6, 16, 26, 36, 46, 56, 66, 76, 86, 96, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 4, 14, 24, 34, 44, 54, 64, 74, 84, 94, 3, 13, 23, 33, 43, 53, 63, 73, 83, 93, 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 1, 11, 21, 31, 41, 51, 61, 71, 81, 91]) == 20
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 2
    assert candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996, 6, 99995, 7, 99994, 8, 99993, 9, 99992, 10, 99991, 11, 99990, 12, 99989, 13, 99988, 14, 99987, 15, 99986, 16, 99985, 17, 99984, 18, 99983, 19, 99982, 20, 99981, 21, 99980, 22, 99979, 23, 99978, 24, 99977, 25, 99976, 26, 99975, 27, 99974, 28, 99973, 29, 99972, 30, 99971]) == 2
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 2


