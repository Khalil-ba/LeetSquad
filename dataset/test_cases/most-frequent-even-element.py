def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [29, 47, 21, 41, 13, 37, 25, 7]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 47, 21, 41, 13, 37, 25, 7]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 20, 10, 10, 20, 20, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 20, 10, 10, 20, 20, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 20, 10, 30, 30, 30, 20, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 20, 10, 30, 30, 30, 20, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 20, 10, 10, 20, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 20, 10, 10, 20, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6, 8, 8, 8, 8, 10, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6, 8, 8, 8, 8, 10, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 8, 8, 8, 10, 10, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 8, 8, 8, 10, 10, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 2, 4, 4, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 2, 4, 4, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 8, 8, 8, 10, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 8, 8, 8, 10, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 8, 8, 8, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 8, 8, 8, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 99998, 99998, 99996]) == 99998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 99998, 99998, 99996]) == 99998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 4, 4, 9, 2, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 4, 4, 9, 2, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 99998, 99998, 99998]) == 99998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 99998, 99998, 99998]) == 99998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 8, 8, 8, 10, 10, 10, 10, 12, 12, 12, 12, 12]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 8, 8, 8, 10, 10, 10, 10, 12, 12, 12, 12, 12]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 10000, 10000, 10000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 10000, 10000, 10000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 100, 200, 200, 300, 300, 300, 300]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 100, 200, 200, 300, 300, 300, 300]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 2, 2, 2, 4, 4, 4, 6, 6, 8, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 2, 2, 2, 4, 4, 4, 6, 6, 8, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 99998, 99998, 99996, 99996, 99996, 99994, 99994]) == 99996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 99998, 99998, 99996, 99996, 99996, 99994, 99994]) == 99996: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99998, 99998, 99998, 99996, 99996, 99994, 99994, 99994, 99992, 99992, 99992, 99992]) == 99992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99998, 99998, 99998, 99996, 99996, 99994, 99994, 99994, 99992, 99992, 99992, 99992]) == 99992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 50000, 50000, 50000, 50000, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 50000, 50000, 50000, 50000, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 10, 10, 10, 12, 12, 14, 14, 14, 16, 16, 16, 16]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 10, 10, 10, 12, 12, 14, 14, 14, 16, 16, 16, 16]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99998, 99998, 99996, 99996, 99996, 99994, 99994]) == 99996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99998, 99998, 99996, 99996, 99996, 99994, 99994]) == 99996: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 2, 2, 2, 4, 4, 4, 4, 6, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 2, 2, 2, 4, 4, 4, 4, 6, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 99998, 99998, 99998, 99996, 99996, 99994]) == 99998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 99998, 99998, 99998, 99996, 99996, 99994]) == 99998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 18, 18, 18, 20, 20, 20, 20, 22, 22, 22, 22, 24, 24, 24, 24]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 18, 18, 18, 20, 20, 20, 20, 22, 22, 22, 22, 24, 24, 24, 24]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200000, 200000, 199998, 199998, 199996, 199996, 199994, 199994, 199992, 199992, 199990, 199990, 199988]) == 199990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200000, 200000, 199998, 199998, 199996, 199996, 199994, 199994, 199992, 199992, 199990, 199990, 199988]) == 199990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 4, 4, 4, 6, 6, 6, 8, 8, 8, 10, 10, 10, 12, 12, 12, 14, 14, 14, 16, 16, 16, 18, 18, 18, 20, 20, 20, 22, 22, 22, 24, 24, 24, 26, 26, 26, 28, 28, 28, 30, 30, 30, 32, 32, 32, 34, 34, 34, 36, 36, 36, 38, 38, 38, 40, 40, 40, 42, 42, 42, 44, 44, 44, 46, 46, 46, 48, 48, 48, 50, 50, 50, 52, 52, 52, 54, 54, 54, 56, 56, 56, 58, 58, 58, 60, 60, 60, 62, 62, 62, 64, 64, 64, 66, 66, 66, 68, 68, 68, 70, 70, 70, 72, 72, 72, 74, 74, 74, 76, 76, 76, 78, 78, 78, 80, 80, 80, 82, 82, 82, 84, 84, 84, 86, 86, 86, 88, 88, 88, 90, 90, 90, 92, 92, 92, 94, 94, 94, 96, 96, 96, 98, 98, 98]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 4, 4, 4, 6, 6, 6, 8, 8, 8, 10, 10, 10, 12, 12, 12, 14, 14, 14, 16, 16, 16, 18, 18, 18, 20, 20, 20, 22, 22, 22, 24, 24, 24, 26, 26, 26, 28, 28, 28, 30, 30, 30, 32, 32, 32, 34, 34, 34, 36, 36, 36, 38, 38, 38, 40, 40, 40, 42, 42, 42, 44, 44, 44, 46, 46, 46, 48, 48, 48, 50, 50, 50, 52, 52, 52, 54, 54, 54, 56, 56, 56, 58, 58, 58, 60, 60, 60, 62, 62, 62, 64, 64, 64, 66, 66, 66, 68, 68, 68, 70, 70, 70, 72, 72, 72, 74, 74, 74, 76, 76, 76, 78, 78, 78, 80, 80, 80, 82, 82, 82, 84, 84, 84, 86, 86, 86, 88, 88, 88, 90, 90, 90, 92, 92, 92, 94, 94, 94, 96, 96, 96, 98, 98, 98]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 8, 10, 8, 6, 6, 8, 10, 10, 10, 10, 8]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 8, 10, 8, 6, 6, 8, 10, 10, 10, 10, 8]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 20, 20, 30, 30, 40, 40, 40, 50, 50, 50, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 20, 20, 30, 30, 40, 40, 40, 50, 50, 50, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 99998, 99998, 99998, 99996, 99996, 99996, 99996]) == 99996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 99998, 99998, 99998, 99996, 99996, 99996, 99996]) == 99996: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 50000, 100000, 50000, 20000, 20000, 20000, 20000]) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 50000, 100000, 50000, 20000, 20000, 20000, 20000]) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 8, 8, 6, 6, 8, 8, 6, 6, 8, 8, 8, 8, 6, 6, 6, 6, 6, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 8, 8, 6, 6, 8, 8, 6, 6, 8, 8, 8, 8, 6, 6, 6, 6, 6, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 20, 40, 40, 40, 40, 60, 60]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 20, 40, 40, 40, 40, 60, 60]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 18, 18, 20, 20, 20, 22, 22, 22, 24, 24, 24, 26, 26, 26, 28, 28, 28, 30, 30, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 18, 18, 20, 20, 20, 22, 22, 22, 24, 24, 24, 26, 26, 26, 28, 28, 28, 30, 30, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1048576, 1048576, 2097152, 2097152, 3145728, 3145728, 4194304, 4194304]) == 1048576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1048576, 1048576, 2097152, 2097152, 3145728, 3145728, 4194304, 4194304]) == 1048576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 3, 8, 6, 8, 5, 6, 6, 2, 2, 2, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 3, 8, 6, 8, 5, 6, 6, 2, 2, 2, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 2, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 2, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 12, 12, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 18, 20, 20, 20, 20, 20]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 12, 12, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 18, 20, 20, 20, 20, 20]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20000, 20000, 19998, 19998, 19996, 19996, 19994, 19994, 19992, 19992]) == 19992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20000, 20000, 19998, 19998, 19996, 19996, 19994, 19994, 19992, 19992]) == 19992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 4, 4, 4, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 4, 4, 4, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 12, 12, 14, 16, 18, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 12, 12, 14, 16, 18, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 20, 30, 30, 30, 40, 40, 40, 40]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 20, 30, 30, 30, 40, 40, 40, 40]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200000, 200000, 100000, 100000, 50000, 50000, 25000, 25000]) == 25000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200000, 200000, 100000, 100000, 50000, 50000, 25000, 25000]) == 25000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20000, 19998, 19998, 19996, 19996, 19996, 19994, 19994, 19992, 19992, 19992, 19992]) == 19992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20000, 19998, 19998, 19996, 19996, 19996, 19994, 19994, 19992, 19992, 19992, 19992]) == 19992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 8, 8, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 8, 8, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 4, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 4, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 99998, 99998, 99998, 99996, 99996, 99996, 99994, 99994, 99994, 99994]) == 99994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 99998, 99998, 99998, 99996, 99996, 99996, 99994, 99994, 99994, 99994]) == 99994: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 22, 24, 24, 26, 26, 28, 28, 30, 30, 32, 32, 34, 34, 36, 36, 38, 38, 40, 40, 42, 42, 44, 44, 46, 46, 48, 48, 50, 50, 52, 52, 54, 54, 56, 56, 58, 58, 60, 60, 62, 62, 64, 64, 66, 66, 68, 68, 70, 70, 72, 72, 74, 74, 76, 76, 78, 78, 80, 80, 82, 82, 84, 84, 86, 86, 88, 88, 90, 90, 92, 92, 94, 94, 96, 96, 98, 98, 100, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 22, 24, 24, 26, 26, 28, 28, 30, 30, 32, 32, 34, 34, 36, 36, 38, 38, 40, 40, 42, 42, 44, 44, 46, 46, 48, 48, 50, 50, 52, 52, 54, 54, 56, 56, 58, 58, 60, 60, 62, 62, 64, 64, 66, 66, 68, 68, 70, 70, 72, 72, 74, 74, 76, 76, 78, 78, 80, 80, 82, 82, 84, 84, 86, 86, 88, 88, 90, 90, 92, 92, 94, 94, 96, 96, 98, 98, 100, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 1000, 3000, 4000, 4000, 5000, 5000, 5000, 5000, 6000, 6000, 6000, 6000, 6000]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 1000, 3000, 4000, 4000, 5000, 5000, 5000, 5000, 6000, 6000, 6000, 6000, 6000]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 100000, 100000, 50000, 50000, 50000, 50000, 25000, 25000]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 100000, 100000, 50000, 50000, 50000, 50000, 25000, 25000]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 44, 44, 44, 44, 46, 46, 46, 46]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 44, 44, 44, 44, 46, 46, 46, 46]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 6, 6, 6, 4, 4, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 6, 6, 6, 4, 4, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5000, 4000, 3000, 2000, 1000, 1000, 2000, 3000, 4000, 5000, 5000, 4000, 3000, 2000, 1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5000, 4000, 3000, 2000, 1000, 1000, 2000, 3000, 4000, 5000, 5000, 4000, 3000, 2000, 1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 200, 200, 300, 300, 300, 400, 400, 400, 400, 500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700, 700, 700, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 200, 200, 300, 300, 300, 400, 400, 400, 400, 500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700, 700, 700, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 1000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [29, 47, 21, 41, 13, 37, 25, 7]) == -1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == -1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]) == 4
    assert candidate(nums = [8, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6]) == 8
    assert candidate(nums = [10, 20, 20, 10, 10, 20, 20, 10]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9]) == -1
    assert candidate(nums = [10, 20, 20, 10, 30, 30, 30, 20, 20]) == 20
    assert candidate(nums = [10, 20, 20, 10, 10, 20, 20]) == 20
    assert candidate(nums = [6, 6, 6, 6, 8, 8, 8, 8, 10, 10]) == 6
    assert candidate(nums = [6, 6, 6, 8, 8, 8, 10, 10, 10]) == 6
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 2
    assert candidate(nums = [0, 1, 2, 2, 4, 4, 1]) == 2
    assert candidate(nums = [2]) == 2
    assert candidate(nums = [6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == -1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13]) == -1
    assert candidate(nums = [6, 6, 6, 8, 8, 8, 10, 10]) == 6
    assert candidate(nums = [6, 6, 8, 8, 8, 10, 10, 10, 10]) == 10
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate(nums = [100000, 100000, 99998, 99998, 99996]) == 99998
    assert candidate(nums = [10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30]) == 10
    assert candidate(nums = [4, 4, 4, 9, 2, 4]) == 4
    assert candidate(nums = [100000, 100000, 99998, 99998, 99998]) == 99998
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2]) == 0
    assert candidate(nums = [2, 2, 2, 2, 2]) == 2
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30]) == 2
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 10
    assert candidate(nums = [99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2
    assert candidate(nums = [0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate(nums = [6, 6, 8, 8, 8, 10, 10, 10, 10, 12, 12, 12, 12, 12]) == 12
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 10000, 10000, 10000]) == 10000
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 2
    assert candidate(nums = [100, 200, 300, 400, 500, 100, 200, 200, 300, 300, 300, 300]) == 300
    assert candidate(nums = [0, 0, 0, 2, 2, 2, 4, 4, 4, 6, 6, 8, 8, 8, 8]) == 8
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [100000, 100000, 100000, 99998, 99998, 99996, 99996, 99996, 99994, 99994]) == 99996
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
    assert candidate(nums = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]) == 1500
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 4
    assert candidate(nums = [99998, 99998, 99998, 99996, 99996, 99994, 99994, 99994, 99992, 99992, 99992, 99992]) == 99992
    assert candidate(nums = [50000, 50000, 50000, 50000, 50000, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 50000
    assert candidate(nums = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 12
    assert candidate(nums = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == -1
    assert candidate(nums = [8, 8, 8, 8, 10, 10, 10, 12, 12, 14, 14, 14, 16, 16, 16, 16]) == 8
    assert candidate(nums = [100000, 99998, 99998, 99996, 99996, 99996, 99994, 99994]) == 99996
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100]) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums = [0, 0, 2, 2, 2, 4, 4, 4, 4, 6, 6]) == 4
    assert candidate(nums = [2, 2, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(nums = [100000, 100000, 100000, 99998, 99998, 99998, 99996, 99996, 99994]) == 99998
    assert candidate(nums = [18, 18, 18, 18, 20, 20, 20, 20, 22, 22, 22, 22, 24, 24, 24, 24]) == 18
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [200000, 200000, 199998, 199998, 199996, 199996, 199994, 199994, 199992, 199992, 199990, 199990, 199988]) == 199990
    assert candidate(nums = [2, 2, 2, 4, 4, 4, 6, 6, 6, 8, 8, 8, 10, 10, 10, 12, 12, 12, 14, 14, 14, 16, 16, 16, 18, 18, 18, 20, 20, 20, 22, 22, 22, 24, 24, 24, 26, 26, 26, 28, 28, 28, 30, 30, 30, 32, 32, 32, 34, 34, 34, 36, 36, 36, 38, 38, 38, 40, 40, 40, 42, 42, 42, 44, 44, 44, 46, 46, 46, 48, 48, 48, 50, 50, 50, 52, 52, 52, 54, 54, 54, 56, 56, 56, 58, 58, 58, 60, 60, 60, 62, 62, 62, 64, 64, 64, 66, 66, 66, 68, 68, 68, 70, 70, 70, 72, 72, 72, 74, 74, 74, 76, 76, 76, 78, 78, 78, 80, 80, 80, 82, 82, 82, 84, 84, 84, 86, 86, 86, 88, 88, 88, 90, 90, 90, 92, 92, 92, 94, 94, 94, 96, 96, 96, 98, 98, 98]) == 2
    assert candidate(nums = [6, 8, 10, 8, 6, 6, 8, 10, 10, 10, 10, 8]) == 10
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 2
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
    assert candidate(nums = [1, 1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19]) == -1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 4
    assert candidate(nums = [10, 10, 10, 20, 20, 30, 30, 40, 40, 40, 50, 50, 50, 50]) == 50
    assert candidate(nums = [100000, 100000, 99998, 99998, 99998, 99996, 99996, 99996, 99996]) == 99996
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 2
    assert candidate(nums = [100000, 50000, 100000, 50000, 20000, 20000, 20000, 20000]) == 20000
    assert candidate(nums = [2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [8, 6, 8, 8, 6, 6, 8, 8, 6, 6, 8, 8, 8, 8, 6, 6, 6, 6, 6, 6]) == 6
    assert candidate(nums = [10, 20, 10, 30, 20, 20, 40, 40, 40, 40, 60, 60]) == 40
    assert candidate(nums = [18, 18, 18, 20, 20, 20, 22, 22, 22, 24, 24, 24, 26, 26, 26, 28, 28, 28, 30, 30, 30]) == 18
    assert candidate(nums = [1048576, 1048576, 2097152, 2097152, 3145728, 3145728, 4194304, 4194304]) == 1048576
    assert candidate(nums = [8, 3, 8, 6, 8, 5, 6, 6, 2, 2, 2, 10, 10, 10, 10]) == 10
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == 2
    assert candidate(nums = [0, 2, 2, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate(nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]) == 4
    assert candidate(nums = [10, 10, 10, 12, 12, 14, 14, 14, 16, 16, 16, 16, 18, 18, 18, 18, 18, 20, 20, 20, 20, 20]) == 18
    assert candidate(nums = [20000, 20000, 19998, 19998, 19996, 19996, 19994, 19994, 19992, 19992]) == 19992
    assert candidate(nums = [2, 2, 4, 4, 4, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10, 10]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 12, 12, 14, 16, 18, 20]) == 10
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 2
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [10, 20, 20, 30, 30, 30, 40, 40, 40, 40]) == 40
    assert candidate(nums = [200000, 200000, 100000, 100000, 50000, 50000, 25000, 25000]) == 25000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18]) == 8
    assert candidate(nums = [20000, 19998, 19998, 19996, 19996, 19996, 19994, 19994, 19992, 19992, 19992, 19992]) == 19992
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 2
    assert candidate(nums = [2, 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 8, 8, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 10, 10, 10, 10, 10]) == 10
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(nums = [2, 4, 4, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12]) == 12
    assert candidate(nums = [100000, 100000, 99998, 99998, 99998, 99996, 99996, 99996, 99994, 99994, 99994, 99994]) == 99994
    assert candidate(nums = [2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, 22, 22, 24, 24, 26, 26, 28, 28, 30, 30, 32, 32, 34, 34, 36, 36, 38, 38, 40, 40, 42, 42, 44, 44, 46, 46, 48, 48, 50, 50, 52, 52, 54, 54, 56, 56, 58, 58, 60, 60, 62, 62, 64, 64, 66, 66, 68, 68, 70, 70, 72, 72, 74, 74, 76, 76, 78, 78, 80, 80, 82, 82, 84, 84, 86, 86, 88, 88, 90, 90, 92, 92, 94, 94, 96, 96, 98, 98, 100, 100]) == 2
    assert candidate(nums = [1000, 2000, 1000, 3000, 4000, 4000, 5000, 5000, 5000, 5000, 6000, 6000, 6000, 6000, 6000]) == 6000
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]) == 2
    assert candidate(nums = [100000, 100000, 100000, 50000, 50000, 50000, 50000, 25000, 25000]) == 50000
    assert candidate(nums = [42, 42, 42, 42, 44, 44, 44, 44, 46, 46, 46, 46]) == 42
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate(nums = [8, 8, 8, 6, 6, 6, 4, 4, 4, 4]) == 4
    assert candidate(nums = [5000, 4000, 3000, 2000, 1000, 1000, 2000, 3000, 4000, 5000, 5000, 4000, 3000, 2000, 1000]) == 1000
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 200, 200, 300, 300, 300, 400, 400, 400, 400, 500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700, 700, 700, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 1000


