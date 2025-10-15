def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(heights = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 100, 1, 100, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 100, 1, 100, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 5, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 5, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 1, 2, 3, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 1, 2, 3, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 4, 2, 1, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 4, 2, 1, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 3, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 3, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 99, 98, 97, 96]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 99, 98, 97, 96]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 3, 3, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 3, 3, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 1, 20, 2, 30, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 1, 20, 2, 30, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 2, 3, 1, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 2, 3, 1, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 1, 2, 2, 3, 3]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 1, 2, 2, 3, 3]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 2, 5, 3, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 2, 5, 3, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [30, 20, 10, 50, 40, 15, 5, 25, 35, 45]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [30, 20, 10, 50, 40, 15, 5, 25, 35, 45]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 5, 3, 2, 1, 5, 4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 5, 3, 2, 1, 5, 4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 2, 2, 1, 1, 1, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 2, 2, 1, 1, 1, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [34, 23, 12, 45, 67, 89, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [34, 23, 12, 45, 67, 89, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 1, 2, 4, 6, 5, 8, 7, 10, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 1, 2, 4, 6, 5, 8, 7, 10, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 2, 1, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 2, 1, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(heights = [99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 1, 100, 2, 100, 3, 100, 4, 100, 5, 100, 6, 100, 7, 100, 8, 100, 9, 100, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 1, 100, 2, 100, 3, 100, 4, 100, 5, 100, 6, 100, 7, 100, 8, 100, 9, 100, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 2, 1, 3, 2, 3, 1, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 2, 1, 3, 2, 3, 1, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 3, 8, 6, 7, 2, 4, 1, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 3, 8, 6, 7, 2, 4, 1, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(heights = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70, 90, 80, 100, 90, 110]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70, 90, 80, 100, 90, 110]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [30, 10, 20, 40, 60, 50, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [30, 10, 20, 40, 60, 50, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 3, 4, 1, 2, 3, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 3, 4, 1, 2, 3, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [34, 56, 23, 89, 12, 33, 21, 67, 45, 90]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [34, 56, 23, 89, 12, 33, 21, 67, 45, 90]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 2, 5, 4, 7, 6, 8, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 2, 5, 4, 7, 6, 8, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 2, 1, 1, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 2, 1, 1, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [7, 8, 9, 10, 11, 5, 6, 4, 3, 2, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [7, 8, 9, 10, 11, 5, 6, 4, 3, 2, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2, 1, 1, 2, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2, 1, 1, 2, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(heights = [1]) == 0
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(heights = [1, 2, 1, 2]) == 2
    assert candidate(heights = [3, 3, 3, 3, 3]) == 0
    assert candidate(heights = [1, 2, 3, 4, 5]) == 0
    assert candidate(heights = [1, 100, 1, 100, 1]) == 2
    assert candidate(heights = [3, 2, 1]) == 2
    assert candidate(heights = [1, 2, 3, 5, 4]) == 2
    assert candidate(heights = [5, 1, 2, 3, 4]) == 5
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4]) == 0
    assert candidate(heights = [1, 1, 4, 2, 1, 3]) == 3
    assert candidate(heights = [1, 2, 2, 3, 3, 4]) == 0
    assert candidate(heights = [100, 99, 98, 97, 96]) == 4
    assert candidate(heights = [3, 1, 2]) == 3
    assert candidate(heights = [1, 1, 1, 1, 1]) == 0
    assert candidate(heights = [1, 3, 2]) == 2
    assert candidate(heights = [3, 3, 3, 3, 3, 3]) == 0
    assert candidate(heights = [10, 20, 30, 40, 50]) == 0
    assert candidate(heights = [1, 2, 2, 3, 3, 4, 4]) == 0
    assert candidate(heights = [10, 1, 20, 2, 30, 3]) == 6
    assert candidate(heights = [5, 2, 3, 1, 4]) == 3
    assert candidate(heights = [1, 3, 2, 4, 5]) == 2
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 1, 2, 2, 3, 3]) == 24
    assert candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1]) == 20
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 35
    assert candidate(heights = [1, 3, 2, 2, 5, 3, 4]) == 5
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(heights = [30, 20, 10, 50, 40, 15, 5, 25, 35, 45]) == 10
    assert candidate(heights = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == 0
    assert candidate(heights = [1, 3, 2, 4, 5, 3, 2, 1, 5, 4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1]) == 16
    assert candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 0
    assert candidate(heights = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]) == 0
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 0
    assert candidate(heights = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4]) == 49
    assert candidate(heights = [2, 2, 2, 1, 1, 1, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 6
    assert candidate(heights = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(heights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0
    assert candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 10
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(heights = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10]) == 20
    assert candidate(heights = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
    assert candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 20
    assert candidate(heights = [34, 23, 12, 45, 67, 89, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90]) == 13
    assert candidate(heights = [3, 1, 2, 4, 6, 5, 8, 7, 10, 9]) == 9
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 0
    assert candidate(heights = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(heights = [3, 2, 1, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 18
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2]) == 16
    assert candidate(heights = [99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100]) == 56
    assert candidate(heights = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 108
    assert candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 18
    assert candidate(heights = [10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(heights = [100, 1, 100, 2, 100, 3, 100, 4, 100, 5, 100, 6, 100, 7, 100, 8, 100, 9, 100, 10]) == 15
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 0
    assert candidate(heights = [50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53]) == 0
    assert candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == 50
    assert candidate(heights = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 18
    assert candidate(heights = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 24
    assert candidate(heights = [3, 3, 2, 1, 3, 2, 3, 1, 3]) == 5
    assert candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 62
    assert candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(heights = [5, 3, 8, 6, 7, 2, 4, 1, 9, 10]) == 8
    assert candidate(heights = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(heights = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == 30
    assert candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 10
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(heights = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 0
    assert candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 16
    assert candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 19
    assert candidate(heights = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 18
    assert candidate(heights = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(heights = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 20
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
    assert candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 0
    assert candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 18
    assert candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(heights = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 0
    assert candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 0
    assert candidate(heights = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70, 90, 80, 100, 90, 110]) == 18
    assert candidate(heights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 18
    assert candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20
    assert candidate(heights = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10]) == 17
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(heights = [30, 10, 20, 40, 60, 50, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 17
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
    assert candidate(heights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 18
    assert candidate(heights = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34]) == 0
    assert candidate(heights = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 40
    assert candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16
    assert candidate(heights = [5, 3, 4, 1, 2, 3, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 17
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
    assert candidate(heights = [34, 56, 23, 89, 12, 33, 21, 67, 45, 90]) == 7
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 24
    assert candidate(heights = [1, 3, 2, 2, 5, 4, 7, 6, 8, 9]) == 6
    assert candidate(heights = [3, 3, 2, 1, 1, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4]) == 16
    assert candidate(heights = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 12
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(heights = [7, 8, 9, 10, 11, 5, 6, 4, 3, 2, 1]) == 11
    assert candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20
    assert candidate(heights = [2, 1, 2, 1, 1, 2, 2, 1]) == 4
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
    assert candidate(heights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 15
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 26
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(heights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 38
    assert candidate(heights = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0


