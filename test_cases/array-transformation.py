def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 2, 3, 1]) == [1, 2, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 2, 3, 1]) == [1, 2, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2, 5, 4, 6, 7, 8, 7, 6]) == [3, 2, 2, 4, 5, 6, 7, 7, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2, 5, 4, 6, 7, 8, 7, 6]) == [3, 2, 2, 4, 5, 6, 7, 7, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 5, 3, 8, 9, 10]) == [10, 5, 5, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 5, 3, 8, 9, 10]) == [10, 5, 5, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 6, 7, 8, 7, 9]) == [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 6, 7, 8, 7, 9]) == [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 1, 2, 9, 2, 8]) == [8, 2, 2, 5, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 1, 2, 9, 2, 8]) == [8, 2, 2, 5, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 3, 1]) == [1, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 3, 1]) == [1, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 6, 3, 4, 3, 5]) == [1, 4, 4, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 6, 3, 4, 3, 5]) == [1, 4, 4, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 2, 2, 1, 3]) == [3, 2, 2, 2, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 2, 2, 1, 3]) == [3, 2, 2, 2, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 4, 2, 3, 3, 3, 2, 4, 9]) == [9, 4, 3, 3, 3, 3, 3, 4, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 4, 2, 3, 3, 3, 2, 4, 9]) == [9, 4, 3, 3, 3, 3, 3, 4, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 2, 3, 4]) == [6, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 2, 3, 4]) == [6, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 1, 2, 3, 4, 6, 4, 5]) == [5, 3, 2, 2, 3, 4, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 1, 2, 3, 4, 6, 4, 5]) == [5, 3, 2, 2, 3, 4, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1]) == [1, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1]) == [1, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [1, 99, 99, 98, 97, 96, 95, 94, 93, 92, 91]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [1, 99, 99, 98, 97, 96, 95, 94, 93, 92, 91]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == [1, 5, 5, 5, 5, 5, 5, 5, 6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == [1, 5, 5, 5, 5, 5, 5, 5, 6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 4, 2, 8, 3, 7, 6]) == [5, 3, 3, 3, 5, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 4, 2, 8, 3, 7, 6]) == [5, 3, 3, 3, 5, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 4, 3, 5, 3, 4, 3, 5, 3, 4, 3]) == [3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 4, 3, 5, 3, 4, 3, 5, 3, 4, 3]) == [3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [1, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [1, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 1, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [3, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 1, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [3, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == [1, 99, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == [1, 99, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 50]) == [50, 2, 2, 3, 4, 5, 6, 7, 8, 9, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 50]) == [50, 2, 2, 3, 4, 5, 6, 7, 8, 9, 50]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 5, 3, 1, 2, 4, 6, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [7, 5, 3, 2, 2, 4, 6, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 5, 3, 1, 2, 4, 6, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [7, 5, 3, 2, 2, 4, 6, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 15, 25, 10, 20, 15, 25, 10, 20]) == [10, 17, 18, 18, 17, 17, 18, 18, 18, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 15, 25, 10, 20, 15, 25, 10, 20]) == [10, 17, 18, 18, 17, 17, 18, 18, 18, 20]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == [10, 9, 5, 5, 5, 5, 5, 5, 5, 5, 6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == [10, 9, 5, 5, 5, 5, 5, 5, 5, 5, 6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 3, 2, 4, 6, 7, 8, 9, 10]) == [5, 2, 2, 3, 4, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 3, 2, 4, 6, 7, 8, 9, 10]) == [5, 2, 2, 3, 4, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 4, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 4, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 8, 9, 1, 2, 3, 4, 5, 6, 7]) == [7, 8, 8, 2, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 8, 9, 1, 2, 3, 4, 5, 6, 7]) == [7, 8, 8, 2, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 6, 6, 6, 6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 25, 75, 50, 75, 25, 50, 75, 25, 50]) == [50, 50, 62, 62, 62, 50, 50, 50, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 25, 75, 50, 75, 25, 50, 75, 25, 50]) == [50, 50, 62, 62, 62, 50, 50, 50, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 2, 8, 9, 4, 6, 3, 5, 1, 10]) == [7, 7, 8, 8, 5, 5, 4, 4, 4, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 2, 8, 9, 4, 6, 3, 5, 1, 10]) == [7, 7, 8, 8, 5, 5, 4, 4, 4, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 6, 9, 4, 7, 5, 10, 3, 8, 2, 9, 1]) == [8, 8, 7, 6, 6, 6, 6, 6, 5, 5, 5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 6, 9, 4, 7, 5, 10, 3, 8, 2, 9, 1]) == [8, 8, 7, 6, 6, 6, 6, 6, 5, 5, 5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1]) == [1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1]) == [1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 5, 10, 5, 10, 5, 10]) == [10, 8, 8, 8, 8, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 5, 10, 5, 10, 5, 10]) == [10, 8, 8, 8, 8, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 5, 15, 7, 20, 6, 25]) == [10, 10, 11, 11, 13, 13, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 5, 15, 7, 20, 6, 25]) == [10, 10, 11, 11, 13, 13, 25]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10]) == [1, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 50, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10]) == [1, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 50, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 51, 51, 51, 51, 51, 51, 51, 51, 96]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 51, 51, 51, 51, 51, 51, 51, 51, 96]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 100, 1, 99, 2, 98, 3, 97, 4, 96]) == [50, 50, 50, 50, 50, 50, 50, 50, 51, 96]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 100, 1, 99, 2, 98, 3, 97, 4, 96]) == [50, 50, 50, 50, 50, 50, 50, 50, 51, 96]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 1, 100, 1, 100, 1, 100]) == [100, 51, 51, 51, 51, 51, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 1, 100, 1, 100, 1, 100]) == [100, 51, 51, 51, 51, 51, 100]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9, 9, 9, 7, 5, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9, 9, 9, 7, 5, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 6, 6, 6, 6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1, 10, 9]) == [8, 7, 6, 5, 4, 3, 2, 2, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1, 10, 9]) == [8, 7, 6, 5, 4, 3, 2, 2, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 3, 3, 3, 2, 2, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 3, 3, 3, 2, 2, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 51, 52, 53, 54, 53, 52, 51, 50]) == [50, 51, 52, 53, 53, 53, 52, 51, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 51, 52, 53, 54, 53, 52, 51, 50]) == [50, 51, 52, 53, 53, 53, 52, 51, 50]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]) == [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]) == [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 12, 10, 14, 11, 15, 13, 16]) == [8, 11, 11, 12, 13, 14, 14, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 12, 10, 14, 11, 15, 13, 16]) == [8, 11, 11, 12, 13, 14, 14, 16]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 3, 2, 1, 1]) == [1, 1, 2, 3, 3, 3, 2, 1, 1, 2, 3, 3, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 3, 2, 1, 1]) == [1, 1, 2, 3, 3, 3, 2, 1, 1, 2, 3, 3, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 2, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 2, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == [1, 1, 2, 2, 1, 1, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == [1, 1, 2, 2, 1, 1, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1]) == [1, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1]) == [1, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 9, 8, 9, 8, 9, 8, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 9, 8, 9, 8, 9, 8, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 3, 4, 3]) == [1, 2, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 3, 4, 3]) == [1, 2, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == [100, 50, 50, 50, 50, 50, 50, 50, 50, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == [100, 50, 50, 50, 50, 50, 50, 50, 50, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 1, 5, 2, 6, 3, 5, 4, 7, 5]) == [7, 3, 3, 4, 4, 4, 4, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 1, 5, 2, 6, 3, 5, 4, 7, 5]) == [7, 3, 3, 4, 4, 4, 4, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 51, 52, 53, 54, 55, 54, 53, 52, 51]) == [50, 51, 52, 53, 54, 54, 54, 53, 52, 51]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 51, 52, 53, 54, 55, 54, 53, 52, 51]) == [50, 51, 52, 53, 54, 54, 54, 53, 52, 51]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [6, 6, 6, 6, 6, 5, 5, 5, 5, 5]) == [6, 6, 6, 6, 6, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [6, 6, 6, 6, 6, 5, 5, 5, 5, 5]) == [6, 6, 6, 6, 6, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [1, 2, 3, 3, 4, 4, 5, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [1, 2, 3, 3, 4, 4, 5, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 8, 6, 9, 7, 10, 8, 11, 9]) == [5, 7, 7, 8, 8, 9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 8, 6, 9, 7, 10, 8, 11, 9]) == [5, 7, 7, 8, 8, 9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5]) == [1, 51, 51, 51, 51, 51, 51, 50, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5]) == [1, 51, 51, 51, 51, 51, 51, 50, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 11, 10, 9, 8]) == [5, 6, 7, 8, 9, 10, 10, 10, 9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 11, 10, 9, 8]) == [5, 6, 7, 8, 9, 10, 10, 10, 9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 7, 1, 9, 2, 8, 4, 10, 6]) == [5, 5, 5, 5, 5, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 7, 1, 9, 2, 8, 4, 10, 6]) == [5, 5, 5, 5, 5, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 4, 2, 7, 3, 6, 8, 9]) == [5, 3, 3, 3, 5, 5, 6, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 4, 2, 7, 3, 6, 8, 9]) == [5, 3, 3, 3, 5, 5, 6, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 5, 1, 4, 1, 3, 1, 2]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 5, 1, 4, 1, 3, 1, 2]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == [10, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == [10, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 8, 7, 6]) == [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 8, 7, 6]) == [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]) == [7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]) == [7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 3, 2, 1, 2, 3, 2, 1, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 3, 2, 1, 2, 3, 2, 1, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 1, 49, 2, 48, 3, 47, 4, 46, 5]) == [50, 25, 25, 25, 25, 25, 25, 25, 25, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 1, 49, 2, 48, 3, 47, 4, 46, 5]) == [50, 25, 25, 25, 25, 25, 25, 25, 25, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == [5, 6, 7, 8, 9, 9, 2, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == [5, 6, 7, 8, 9, 9, 2, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]) == [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]) == [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [10, 15, 15, 25, 25, 35, 35, 45, 45, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [10, 15, 15, 25, 25, 35, 35, 45, 45, 60]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 4, 4, 3, 2, 2, 2, 3, 4, 4, 4, 3, 2, 2, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 4, 4, 3, 2, 2, 2, 3, 4, 4, 4, 3, 2, 2, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5, 6]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5, 6]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [10, 6, 6, 6, 6, 5, 5, 5, 5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [10, 6, 6, 6, 6, 5, 5, 5, 5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 11, 12, 13, 14, 13, 12, 11, 10]) == [10, 11, 12, 13, 13, 13, 12, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 11, 12, 13, 14, 13, 12, 11, 10]) == [10, 11, 12, 13, 13, 13, 12, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 6, 6, 7, 8, 9, 9, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 6, 6, 7, 8, 9, 9, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == [5, 4, 4, 4, 4, 4, 4, 4, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == [5, 4, 4, 4, 4, 4, 4, 4, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 6, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 6, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 2, 8, 0, 6, 4, 2, 0, 6, 8, 4, 2, 8, 0, 6, 4, 2]) == [3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 8, 8, 8, 3, 3, 3, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 7, 7, 5, 2, 2, 8, 8, 4, 4, 7, 7, 6, 6, 6, 6, 9, 9, 5, 5, 5, 1, 1, 5, 5, 2, 2, 7, 7, 7, 6, 4, 4, 5, 5, 3, 2, 2, 7, 7, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 2, 2, 6, 6, 4, 4, 4, 4, 4, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 2, 8, 0, 6, 4, 2, 0, 6, 8, 4, 2, 8, 0, 6, 4, 2]) == [3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 8, 8, 8, 3, 3, 3, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 7, 7, 5, 2, 2, 8, 8, 4, 4, 7, 7, 6, 6, 6, 6, 9, 9, 5, 5, 5, 1, 1, 5, 5, 2, 2, 7, 7, 7, 6, 4, 4, 5, 5, 3, 2, 2, 7, 7, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 2, 2, 6, 6, 4, 4, 4, 4, 4, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 2, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 2, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 9, 3, 7, 4, 8, 2, 6]) == [5, 5, 5, 5, 5, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 9, 3, 7, 4, 8, 2, 6]) == [5, 5, 5, 5, 5, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 51, 49, 52, 48, 53, 47, 54, 46, 55, 45, 56, 44, 57, 43, 58, 42, 59, 41, 60]) == [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 51, 49, 52, 48, 53, 47, 54, 46, 55, 45, 56, 44, 57, 43, 58, 42, 59, 41, 60]) == [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 51, 51, 51, 51, 51, 51, 51, 51, 96]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 51, 51, 51, 51, 51, 51, 51, 51, 96]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 4, 4, 3, 2, 2, 2, 3, 4, 4, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 4, 4, 3, 2, 2, 2, 3, 4, 4, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 1, 51, 2, 52, 3, 53, 4, 54, 5, 55, 6, 56, 7, 57, 8, 58, 9, 59, 10]) == [50, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 1, 51, 2, 52, 3, 53, 4, 54, 5, 55, 6, 56, 7, 57, 8, 58, 9, 59, 10]) == [50, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 5, 3, 7, 4, 8, 5, 9, 6, 10]) == [1, 4, 4, 5, 6, 6, 7, 7, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 5, 3, 7, 4, 8, 5, 9, 6, 10]) == [1, 4, 4, 5, 6, 6, 7, 7, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 6, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 6, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 1, 4, 2, 5, 3, 6, 4, 7]) == [2, 2, 2, 3, 3, 4, 4, 5, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 1, 4, 2, 5, 3, 6, 4, 7]) == [2, 2, 2, 3, 3, 4, 4, 5, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 1, 6, 3, 7, 2, 8, 4, 7, 3, 6, 5]) == [8, 4, 4, 5, 5, 5, 6, 6, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 1, 6, 3, 7, 2, 8, 4, 7, 3, 6, 5]) == [8, 4, 4, 5, 5, 5, 6, 6, 5, 5, 5, 5]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [1, 3, 2, 2, 3, 1]) == [1, 2, 2, 2, 2, 1]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(arr = [3, 1, 2, 5, 4, 6, 7, 8, 7, 6]) == [3, 2, 2, 4, 5, 6, 7, 7, 7, 6]
    assert candidate(arr = [10, 5, 3, 8, 9, 10]) == [10, 5, 5, 8, 9, 10]
    assert candidate(arr = [1, 3, 2, 5, 4, 6, 7, 8, 7, 9]) == [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
    assert candidate(arr = [8, 1, 2, 9, 2, 8]) == [8, 2, 2, 5, 6, 8]
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(arr = [1, 3, 2, 3, 1]) == [1, 2, 2, 2, 1]
    assert candidate(arr = [1, 6, 3, 4, 3, 5]) == [1, 4, 4, 4, 4, 5]
    assert candidate(arr = [3, 1, 2, 2, 1, 3]) == [3, 2, 2, 2, 2, 3]
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5]
    assert candidate(arr = [9, 4, 2, 3, 3, 3, 2, 4, 9]) == [9, 4, 3, 3, 3, 3, 3, 4, 9]
    assert candidate(arr = [6, 2, 3, 4]) == [6, 3, 3, 4]
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(arr = [5, 3, 1, 2, 3, 4, 6, 4, 5]) == [5, 3, 2, 2, 3, 4, 5, 5, 5]
    assert candidate(arr = [1, 2, 3, 2, 1]) == [1, 2, 2, 2, 1]
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(arr = [3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
    assert candidate(arr = [1, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [1, 99, 99, 98, 97, 96, 95, 94, 93, 92, 91]
    assert candidate(arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == [1, 5, 5, 5, 5, 5, 5, 5, 6, 10]
    assert candidate(arr = [5, 1, 4, 2, 8, 3, 7, 6]) == [5, 3, 3, 3, 5, 6, 6, 6]
    assert candidate(arr = [3, 4, 3, 5, 3, 4, 3, 5, 3, 4, 3]) == [3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3]
    assert candidate(arr = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]
    assert candidate(arr = [1, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [1, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1]
    assert candidate(arr = [3, 2, 1, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [3, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
    assert candidate(arr = [1, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == [1, 99, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert candidate(arr = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    assert candidate(arr = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 50]) == [50, 2, 2, 3, 4, 5, 6, 7, 8, 9, 50]
    assert candidate(arr = [7, 5, 3, 1, 2, 4, 6, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [7, 5, 3, 2, 2, 4, 6, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(arr = [10, 20, 15, 25, 10, 20, 15, 25, 10, 20]) == [10, 17, 18, 18, 17, 17, 18, 18, 18, 20]
    assert candidate(arr = [10, 9, 1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == [10, 9, 5, 5, 5, 5, 5, 5, 5, 5, 6, 10]
    assert candidate(arr = [5, 1, 3, 2, 4, 6, 7, 8, 9, 10]) == [5, 2, 2, 3, 4, 6, 7, 8, 9, 10]
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 4, 4, 3, 2, 1]
    assert candidate(arr = [7, 8, 9, 1, 2, 3, 4, 5, 6, 7]) == [7, 8, 8, 2, 2, 3, 4, 5, 6, 7]
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(arr = [50, 25, 75, 50, 75, 25, 50, 75, 25, 50]) == [50, 50, 62, 62, 62, 50, 50, 50, 50, 50]
    assert candidate(arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(arr = [7, 2, 8, 9, 4, 6, 3, 5, 1, 10]) == [7, 7, 8, 8, 5, 5, 4, 4, 4, 10]
    assert candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    assert candidate(arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(arr = [8, 6, 9, 4, 7, 5, 10, 3, 8, 2, 9, 1]) == [8, 8, 7, 6, 6, 6, 6, 6, 5, 5, 5, 1]
    assert candidate(arr = [1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1]) == [1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1]
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(arr = [10, 5, 10, 5, 10, 5, 10]) == [10, 8, 8, 8, 8, 8, 10]
    assert candidate(arr = [10, 5, 15, 7, 20, 6, 25]) == [10, 10, 11, 11, 13, 13, 25]
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10]) == [1, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 50, 10]
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 51, 51, 51, 51, 51, 51, 51, 51, 96]
    assert candidate(arr = [50, 100, 1, 99, 2, 98, 3, 97, 4, 96]) == [50, 50, 50, 50, 50, 50, 50, 50, 51, 96]
    assert candidate(arr = [100, 1, 100, 1, 100, 1, 100]) == [100, 51, 51, 51, 51, 51, 100]
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9, 9, 9, 7, 5, 3, 1]
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1, 10, 9]) == [8, 7, 6, 5, 4, 3, 2, 2, 9, 9]
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 3, 3, 3, 2, 2, 2, 2, 2, 1]
    assert candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
    assert candidate(arr = [50, 51, 52, 53, 54, 53, 52, 51, 50]) == [50, 51, 52, 53, 53, 53, 52, 51, 50]
    assert candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 1]
    assert candidate(arr = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]) == [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]
    assert candidate(arr = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(arr = [8, 12, 10, 14, 11, 15, 13, 16]) == [8, 11, 11, 12, 13, 14, 14, 16]
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(arr = [1, 1, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 3, 2, 1, 1]) == [1, 1, 2, 3, 3, 3, 2, 1, 1, 2, 3, 3, 3, 2, 1, 1]
    assert candidate(arr = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 2, 2, 3, 4, 5]
    assert candidate(arr = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == [1, 1, 2, 2, 1, 1, 2, 2, 1, 1]
    assert candidate(arr = [1, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1]) == [1, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1, 1]
    assert candidate(arr = [9, 8, 9, 8, 9, 8, 9, 8, 9]) == [9, 9, 9, 9, 9, 9, 9, 9, 9]
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 3, 4, 3]) == [1, 2, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(arr = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
    assert candidate(arr = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == [100, 50, 50, 50, 50, 50, 50, 50, 50, 5]
    assert candidate(arr = [7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(arr = [7, 1, 5, 2, 6, 3, 5, 4, 7, 5]) == [7, 3, 3, 4, 4, 4, 4, 5, 5, 5]
    assert candidate(arr = [50, 51, 52, 53, 54, 55, 54, 53, 52, 51]) == [50, 51, 52, 53, 54, 54, 54, 53, 52, 51]
    assert candidate(arr = [6, 6, 6, 6, 6, 5, 5, 5, 5, 5]) == [6, 6, 6, 6, 6, 5, 5, 5, 5, 5]
    assert candidate(arr = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    assert candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [1, 2, 3, 3, 4, 4, 5, 5, 6, 7]
    assert candidate(arr = [5, 8, 6, 9, 7, 10, 8, 11, 9]) == [5, 7, 7, 8, 8, 9, 9, 9, 9]
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5]) == [1, 51, 51, 51, 51, 51, 51, 50, 5]
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 11, 10, 9, 8]) == [5, 6, 7, 8, 9, 10, 10, 10, 9, 8]
    assert candidate(arr = [5, 3, 7, 1, 9, 2, 8, 4, 10, 6]) == [5, 5, 5, 5, 5, 6, 6, 6, 6, 6]
    assert candidate(arr = [5, 1, 4, 2, 7, 3, 6, 8, 9]) == [5, 3, 3, 3, 5, 5, 6, 8, 9]
    assert candidate(arr = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 5, 1, 4, 1, 3, 1, 2]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
    assert candidate(arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == [10, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(arr = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 8, 7, 6]) == [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 8, 7, 6]
    assert candidate(arr = [7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]) == [7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6]
    assert candidate(arr = [2, 1, 3, 2, 1, 2, 3, 2, 1, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(arr = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1]) == [2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 1]
    assert candidate(arr = [50, 1, 49, 2, 48, 3, 47, 4, 46, 5]) == [50, 25, 25, 25, 25, 25, 25, 25, 25, 5]
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == [5, 6, 7, 8, 9, 9, 2, 2, 3, 4]
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]) == [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]
    assert candidate(arr = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [10, 15, 15, 25, 25, 35, 35, 45, 45, 60]
    assert candidate(arr = [1, 2, 3, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1]
    assert candidate(arr = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 4, 4, 3, 2, 2, 2, 3, 4, 4, 4, 3, 2, 2, 2, 3, 4, 5]
    assert candidate(arr = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5, 6]) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6]
    assert candidate(arr = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [10, 6, 6, 6, 6, 5, 5, 5, 5, 1]
    assert candidate(arr = [10, 11, 12, 13, 14, 13, 12, 11, 10]) == [10, 11, 12, 13, 13, 13, 12, 11, 10]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 6, 6, 7, 8, 9, 9, 1]
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(arr = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == [5, 4, 4, 4, 4, 4, 4, 4, 4, 3]
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 6, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5]
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 2, 8, 0, 6, 4, 2, 0, 6, 8, 4, 2, 8, 0, 6, 4, 2]) == [3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 8, 8, 8, 3, 3, 3, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 7, 7, 5, 2, 2, 8, 8, 4, 4, 7, 7, 6, 6, 6, 6, 9, 9, 5, 5, 5, 1, 1, 5, 5, 2, 2, 7, 7, 7, 6, 4, 4, 5, 5, 3, 2, 2, 7, 7, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 2, 2, 6, 6, 4, 4, 4, 4, 4, 4, 2]
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    assert candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 2, 2, 3, 4, 5]
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
    assert candidate(arr = [5, 1, 9, 3, 7, 4, 8, 2, 6]) == [5, 5, 5, 5, 5, 6, 6, 6, 6]
    assert candidate(arr = [50, 51, 49, 52, 48, 53, 47, 54, 46, 55, 45, 56, 44, 57, 43, 58, 42, 59, 41, 60]) == [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60]
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 51, 51, 51, 51, 51, 51, 51, 51, 96]
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 4, 4, 3, 2, 2, 2, 3, 4, 4, 4, 3, 2, 1]
    assert candidate(arr = [50, 1, 51, 2, 52, 3, 53, 4, 54, 5, 55, 6, 56, 7, 57, 8, 58, 9, 59, 10]) == [50, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 10]
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(arr = [3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9]
    assert candidate(arr = [1, 5, 3, 7, 4, 8, 5, 9, 6, 10]) == [1, 4, 4, 5, 6, 6, 7, 7, 8, 10]
    assert candidate(arr = [9, 8, 7, 6, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 6, 6, 7, 8, 9]
    assert candidate(arr = [2, 3, 1, 4, 2, 5, 3, 6, 4, 7]) == [2, 2, 2, 3, 3, 4, 4, 5, 5, 7]
    assert candidate(arr = [8, 1, 6, 3, 7, 2, 8, 4, 7, 3, 6, 5]) == [8, 4, 4, 5, 5, 5, 6, 6, 5, 5, 5, 5]


