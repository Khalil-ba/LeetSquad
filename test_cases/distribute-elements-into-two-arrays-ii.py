def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 5, 4, 9, 8, 7, 6, 10]) == [3, 1, 9, 8, 7, 6, 2, 5, 4, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 5, 4, 9, 8, 7, 6, 10]) == [3, 1, 9, 8, 7, 6, 2, 5, 4, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 80, 70, 60, 50, 40, 30, 20, 10, 90]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 80, 70, 60, 50, 40, 30, 20, 10, 90]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 4, 3, 20, 15]) == [7, 4, 3, 10, 20, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 4, 3, 20, 15]) == [7, 4, 3, 10, 20, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 20, 15, 25, 30]) == [10, 20, 15, 5, 25, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 20, 15, 25, 30]) == [10, 20, 15, 5, 25, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == [1000000000, 1000000000, 1, 1, 1000000000, 1, 1, 1000000000, 1000000000, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == [1000000000, 1000000000, 1, 1, 1000000000, 1, 1, 1000000000, 1000000000, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 14, 3, 1, 2]) == [5, 3, 1, 2, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 14, 3, 1, 2]) == [5, 3, 1, 2, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10]) == [9, 8, 2, 7, 3, 6, 4, 5, 1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10]) == [9, 8, 2, 7, 3, 6, 4, 5, 1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 3]) == [2, 3, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 3]) == [2, 3, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 8, 7, 6, 5, 4, 3, 2, 1, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 8, 7, 6, 5, 4, 3, 2, 1, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3]) == [3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3]) == [3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 13, 12, 11, 15, 14, 17, 16, 19, 18, 20, 21, 22, 23, 24, 25]) == [1, 6, 5, 4, 10, 13, 12, 11, 19, 18, 21, 23, 25, 3, 2, 9, 8, 7, 15, 14, 17, 16, 20, 22, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 13, 12, 11, 15, 14, 17, 16, 19, 18, 20, 21, 22, 23, 24, 25]) == [1, 6, 5, 4, 10, 13, 12, 11, 19, 18, 21, 23, 25, 3, 2, 9, 8, 7, 15, 14, 17, 16, 20, 22, 24]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 1000000000, 2, 1000000000, 3, 1000000000, 4, 1000000000]) == [1000000000, 1000000000, 2, 3, 1000000000, 1, 1000000000, 1000000000, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 1000000000, 2, 1000000000, 3, 1000000000, 4, 1000000000]) == [1000000000, 1000000000, 2, 3, 1000000000, 1, 1000000000, 1000000000, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16]) == [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 20, 19, 18, 17, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16]) == [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 20, 19, 18, 17, 16]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 75, 12, 37, 62, 88, 43, 59, 100, 20, 90, 30, 80, 40, 70, 60, 50, 10, 95]) == [50, 75, 12, 37, 62, 43, 59, 20, 30, 40, 10, 25, 88, 100, 90, 80, 70, 60, 50, 95]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 75, 12, 37, 62, 88, 43, 59, 100, 20, 90, 30, 80, 40, 70, 60, 50, 10, 95]) == [50, 75, 12, 37, 62, 43, 59, 20, 30, 40, 10, 25, 88, 100, 90, 80, 70, 60, 50, 95]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996, 6, 999999995, 7, 999999994, 8, 999999993, 9, 999999992, 10, 999999991]) == [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996, 6, 999999995, 7, 999999994, 8, 999999993, 9, 999999992, 10, 999999991]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996, 6, 999999995, 7, 999999994, 8, 999999993, 9, 999999992, 10, 999999991]) == [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996, 6, 999999995, 7, 999999994, 8, 999999993, 9, 999999992, 10, 999999991]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 30, 5, 25, 15, 35, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 40]) == [20, 30, 5, 25, 15, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 10, 35, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 30, 5, 25, 15, 35, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 40]) == [20, 30, 5, 25, 15, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 10, 35, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 40]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [5, 3, 2, 1, 9, 4, 6, 7, 8, 10, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [5, 3, 2, 1, 9, 4, 6, 7, 8, 10, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 45, 50, 55, 5, 60, 65, 70]) == [10, 25, 30, 5, 45, 55, 60, 70, 20, 15, 35, 40, 50, 5, 65]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 45, 50, 55, 5, 60, 65, 70]) == [10, 25, 30, 5, 45, 55, 60, 70, 20, 15, 35, 40, 50, 5, 65]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == [1, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == [1, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 2, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 2, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 7, 2, 4, 1, 9, 10]) == [5, 8, 6, 7, 2, 4, 1, 3, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 7, 2, 4, 1, 9, 10]) == [5, 8, 6, 7, 2, 4, 1, 3, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 101, 98, 102, 97, 103, 96, 104, 95, 105, 94, 106, 93, 107]) == [100, 101, 98, 97, 96, 95, 94, 93, 99, 102, 103, 104, 105, 106, 107]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 101, 98, 102, 97, 103, 96, 104, 95, 105, 94, 106, 93, 107]) == [100, 101, 98, 97, 96, 95, 94, 93, 99, 102, 103, 104, 105, 106, 107]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [25, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [25, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == [5, 9, 2, 8, 3, 7, 4, 6, 1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == [5, 9, 2, 8, 3, 7, 4, 6, 1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24]) == [1, 5, 4, 9, 8, 13, 12, 17, 16, 21, 20, 25, 24, 3, 2, 7, 6, 11, 10, 15, 14, 19, 18, 23, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24]) == [1, 5, 4, 9, 8, 13, 12, 17, 16, 21, 20, 25, 24, 3, 2, 7, 6, 11, 10, 15, 14, 19, 18, 23, 22]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == [5, 7, 9, 1, 3, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 5, 7, 9, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == [5, 7, 9, 1, 3, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 5, 7, 9, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [109, 108, 107, 106, 105, 104, 103, 102, 101, 100]) == [109, 107, 106, 105, 104, 103, 102, 101, 100, 108]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [109, 108, 107, 106, 105, 104, 103, 102, 101, 100]) == [109, 107, 106, 105, 104, 103, 102, 101, 100, 108]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == [2, 1, 7, 6, 11, 10, 15, 14, 19, 18, 3, 5, 4, 9, 8, 13, 12, 17, 16, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == [2, 1, 7, 6, 11, 10, 15, 14, 19, 18, 3, 5, 4, 9, 8, 13, 12, 17, 16, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [3, 2, 1, 3, 1, 2, 1, 3, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [3, 2, 1, 3, 1, 2, 1, 3, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19, 20]) == [10, 11, 2, 3, 14, 5, 16, 7, 18, 9, 1, 12, 13, 4, 15, 6, 17, 8, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19, 20]) == [10, 11, 2, 3, 14, 5, 16, 7, 18, 9, 1, 12, 13, 4, 15, 6, 17, 8, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 30, 50, 70, 90, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 40, 60, 80, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 30, 50, 70, 90, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 40, 60, 80, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == [10, 20, 2, 3, 50, 5, 1, 30, 40, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == [10, 20, 2, 3, 50, 5, 1, 30, 40, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == [1, 5, 9, 4, 8, 3, 7, 2, 6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == [1, 5, 9, 4, 8, 3, 7, 2, 6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [1000000000, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [1000000000, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999999]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 1, 6, 11, 16, 21, 3, 8, 13, 18, 23, 4, 9, 14, 19, 24, 7, 12, 17, 22, 26]) == [5, 15, 25, 1, 11, 21, 3, 8, 13, 18, 23, 4, 9, 14, 19, 24, 7, 12, 17, 22, 10, 20, 6, 16, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 1, 6, 11, 16, 21, 3, 8, 13, 18, 23, 4, 9, 14, 19, 24, 7, 12, 17, 22, 26]) == [5, 15, 25, 1, 11, 21, 3, 8, 13, 18, 23, 4, 9, 14, 19, 24, 7, 12, 17, 22, 10, 20, 6, 16, 26]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == [1000000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 500000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == [1000000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 500000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 5, 8, 3, 6, 9, 2, 1, 4]) == [7, 5, 3, 10, 8, 6, 9, 2, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 5, 8, 3, 6, 9, 2, 1, 4]) == [7, 5, 3, 10, 8, 6, 9, 2, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == [100, 102, 104, 106, 108, 101, 103, 105, 107, 109]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == [100, 102, 104, 106, 108, 101, 103, 105, 107, 109]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]) == [100, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 99]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]) == [100, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 99]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10, 11, 12, 13, 14, 15]) == [9, 8, 2, 7, 3, 6, 4, 5, 1, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10, 11, 12, 13, 14, 15]) == [9, 8, 2, 7, 3, 6, 4, 5, 1, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [10, 8, 7, 6, 5, 4, 3, 2, 1, 19, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [10, 8, 7, 6, 5, 4, 3, 2, 1, 19, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10]) == [5, 8, 6, 2, 7, 4, 1, 3, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10]) == [5, 8, 6, 2, 7, 4, 1, 3, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [5, 3, 2, 1, 9, 4, 6, 7, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [5, 3, 2, 1, 9, 4, 6, 7, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [25, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [25, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 7, 1, 8, 3, 6, 4, 9, 10, 1, 1, 1, 1, 1]) == [5, 7, 1, 3, 9, 2, 8, 6, 4, 10, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 7, 1, 8, 3, 6, 4, 9, 10, 1, 1, 1, 1, 1]) == [5, 7, 1, 3, 9, 2, 8, 6, 4, 10, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == [1, 5, 4, 9, 8, 13, 12, 3, 2, 7, 6, 11, 10, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == [1, 5, 4, 9, 8, 13, 12, 3, 2, 7, 6, 11, 10, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == [2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == [2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == [1, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == [1, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16, 10, 2, 9, 3, 8, 4, 7, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 8, 7, 6, 5, 4, 3, 2, 1, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 8, 7, 6, 5, 4, 3, 2, 1, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == [1, 3, 2, 1, 3, 2, 1, 3, 2, 3, 2, 1, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == [1, 3, 2, 1, 3, 2, 1, 3, 2, 3, 2, 1, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 45, 35, 25, 15]) == [10, 30, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 25, 15, 20, 40, 55, 45, 35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 45, 35, 25, 15]) == [10, 30, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 25, 15, 20, 40, 55, 45, 35]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 25, 30, 5, 2, 1, 3, 18, 19, 21, 22, 23, 24, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [10, 25, 30, 5, 2, 1, 3, 18, 19, 21, 22, 23, 24, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 25, 30, 5, 2, 1, 3, 18, 19, 21, 22, 23, 24, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [10, 25, 30, 5, 2, 1, 3, 18, 19, 21, 22, 23, 24, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == [1, 5, 4, 9, 8, 13, 12, 3, 2, 7, 6, 11, 10, 15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == [1, 5, 4, 9, 8, 13, 12, 3, 2, 7, 6, 11, 10, 15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 1, 2, 2, 3, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 1, 2, 2, 3, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 15, 10, 12, 1, 13, 5, 8, 2, 14, 9, 6, 11, 4]) == [7, 15, 10, 12, 1, 13, 5, 8, 2, 14, 9, 6, 11, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 15, 10, 12, 1, 13, 5, 8, 2, 14, 9, 6, 11, 4]) == [7, 15, 10, 12, 1, 13, 5, 8, 2, 14, 9, 6, 11, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == [5, 9, 2, 8, 3, 7, 4, 6, 1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == [5, 9, 2, 8, 3, 7, 4, 6, 1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4]) == [1, 3, 2, 10, 9, 8, 7, 6, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4]) == [1, 3, 2, 10, 9, 8, 7, 6, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 7, 6, 5, 4, 3, 2, 1, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 7, 6, 5, 4, 3, 2, 1, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 8, 2, 7, 3, 6, 4, 5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 8, 2, 7, 3, 6, 4, 5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 110, 120, 130, 140, 150, 5, 15, 25, 35, 45]) == [100, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 90, 110, 120, 130, 140, 150, 35, 45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 110, 120, 130, 140, 150, 5, 15, 25, 35, 45]) == [100, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 90, 110, 120, 130, 140, 150, 35, 45]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [1, 5, 9, 13, 17, 4, 8, 12, 16, 20, 3, 7, 11, 15, 19, 2, 6, 10, 14, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [1, 5, 9, 13, 17, 4, 8, 12, 16, 20, 3, 7, 11, 15, 19, 2, 6, 10, 14, 18]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == [1, 1, 2, 3, 3, 1, 2, 2, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == [1, 1, 2, 3, 3, 1, 2, 2, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [1, 3, 5, 2, 4, 1, 3, 5, 2, 4, 2, 4, 1, 3, 5, 2, 4, 1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [1, 3, 5, 2, 4, 1, 3, 5, 2, 4, 2, 4, 1, 3, 5, 2, 4, 1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 10, 5, 25, 30, 5, 15, 25]) == [10, 25, 30, 5, 15, 25, 20, 15, 10, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 10, 5, 25, 30, 5, 15, 25]) == [10, 25, 30, 5, 15, 25, 20, 15, 10, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == [1, 5, 4, 9, 8, 13, 12, 17, 16, 20, 3, 2, 7, 6, 11, 10, 15, 14, 19, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == [1, 5, 4, 9, 8, 13, 12, 17, 16, 20, 3, 2, 7, 6, 11, 10, 15, 14, 19, 18]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 10, 40, 1, 2, 3, 4, 5]) == [50, 30, 10, 40, 1, 2, 3, 4, 5, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 10, 40, 1, 2, 3, 4, 5]) == [50, 30, 10, 40, 1, 2, 3, 4, 5, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == [50, 30, 20, 10, 15, 25, 45, 105, 125, 145, 40, 35, 55, 65, 75, 85, 95, 115, 135, 155]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == [50, 30, 20, 10, 15, 25, 45, 105, 125, 145, 40, 35, 55, 65, 75, 85, 95, 115, 135, 155]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 25, 25, 25, 25, 50, 50, 50, 50, 50, 75, 75, 75, 75, 75, 100, 100, 100, 100, 100]) == [25, 25, 25, 50, 50, 75, 75, 75, 100, 100, 25, 25, 50, 50, 50, 75, 75, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 25, 25, 25, 25, 50, 50, 50, 50, 50, 75, 75, 75, 75, 75, 100, 100, 100, 100, 100]) == [25, 25, 25, 50, 50, 75, 75, 75, 100, 100, 25, 25, 50, 50, 50, 75, 75, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [3, 2, 1, 5, 4, 9, 8, 7, 6, 10]) == [3, 1, 9, 8, 7, 6, 2, 5, 4, 10]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [100, 80, 70, 60, 50, 40, 30, 20, 10, 90]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    assert candidate(nums = [7, 10, 4, 3, 20, 15]) == [7, 4, 3, 10, 20, 15]
    assert candidate(nums = [10, 5, 20, 15, 25, 30]) == [10, 20, 15, 5, 25, 30]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == [1000000000, 1000000000, 1, 1, 1000000000, 1, 1, 1000000000, 1000000000, 1]
    assert candidate(nums = [5, 14, 3, 1, 2]) == [5, 3, 1, 2, 14]
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10]) == [9, 8, 2, 7, 3, 6, 4, 5, 1, 10]
    assert candidate(nums = [2, 1, 3, 3]) == [2, 3, 1, 3]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 8, 7, 6, 5, 4, 3, 2, 1, 9]
    assert candidate(nums = [3, 3, 3, 3]) == [3, 3, 3, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    assert candidate(nums = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10, 13, 12, 11, 15, 14, 17, 16, 19, 18, 20, 21, 22, 23, 24, 25]) == [1, 6, 5, 4, 10, 13, 12, 11, 19, 18, 21, 23, 25, 3, 2, 9, 8, 7, 15, 14, 17, 16, 20, 22, 24]
    assert candidate(nums = [1000000000, 1, 1000000000, 2, 1000000000, 3, 1000000000, 4, 1000000000]) == [1000000000, 1000000000, 2, 3, 1000000000, 1, 1000000000, 1000000000, 4]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16]) == [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14, 20, 19, 18, 17, 16]
    assert candidate(nums = [50, 25, 75, 12, 37, 62, 88, 43, 59, 100, 20, 90, 30, 80, 40, 70, 60, 50, 10, 95]) == [50, 75, 12, 37, 62, 43, 59, 20, 30, 40, 10, 25, 88, 100, 90, 80, 70, 60, 50, 95]
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996, 6, 999999995, 7, 999999994, 8, 999999993, 9, 999999992, 10, 999999991]) == [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996, 6, 999999995, 7, 999999994, 8, 999999993, 9, 999999992, 10, 999999991]
    assert candidate(nums = [20, 10, 30, 5, 25, 15, 35, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 40]) == [20, 30, 5, 25, 15, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 10, 35, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 40]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 19]
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [5, 3, 2, 1, 9, 4, 6, 7, 8, 10, 1, 2, 3, 4, 5]
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 45, 50, 55, 5, 60, 65, 70]) == [10, 25, 30, 5, 45, 55, 60, 70, 20, 15, 35, 40, 50, 5, 65]
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == [1, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3]
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 2, 3, 3]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 14]
    assert candidate(nums = [5, 3, 8, 6, 7, 2, 4, 1, 9, 10]) == [5, 8, 6, 7, 2, 4, 1, 3, 9, 10]
    assert candidate(nums = [100, 99, 101, 98, 102, 97, 103, 96, 104, 95, 105, 94, 106, 93, 107]) == [100, 101, 98, 97, 96, 95, 94, 93, 99, 102, 103, 104, 105, 106, 107]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [25, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24]
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    assert candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == [5, 9, 2, 8, 3, 7, 4, 6, 1, 10]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24]) == [1, 5, 4, 9, 8, 13, 12, 17, 16, 21, 20, 25, 24, 3, 2, 7, 6, 11, 10, 15, 14, 19, 18, 23, 22]
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == [5, 7, 9, 1, 3, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 5, 7, 9, 1, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]
    assert candidate(nums = [109, 108, 107, 106, 105, 104, 103, 102, 101, 100]) == [109, 107, 106, 105, 104, 103, 102, 101, 100, 108]
    assert candidate(nums = [2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == [2, 1, 7, 6, 11, 10, 15, 14, 19, 18, 3, 5, 4, 9, 8, 13, 12, 17, 16, 20]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [3, 2, 1, 3, 1, 2, 1, 3, 2, 3]
    assert candidate(nums = [10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19, 20]) == [10, 11, 2, 3, 14, 5, 16, 7, 18, 9, 1, 12, 13, 4, 15, 6, 17, 8, 19, 20]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 30, 50, 70, 90, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 40, 60, 80, 100]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == [10, 20, 2, 3, 50, 5, 1, 30, 40, 4]
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == [1, 5, 9, 4, 8, 3, 7, 2, 6, 10]
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [1000000000, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999999]
    assert candidate(nums = [5, 10, 15, 20, 25, 1, 6, 11, 16, 21, 3, 8, 13, 18, 23, 4, 9, 14, 19, 24, 7, 12, 17, 22, 26]) == [5, 15, 25, 1, 11, 21, 3, 8, 13, 18, 23, 4, 9, 14, 19, 24, 7, 12, 17, 22, 10, 20, 6, 16, 26]
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == [1000000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 500000000]
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    assert candidate(nums = [7, 10, 5, 8, 3, 6, 9, 2, 1, 4]) == [7, 5, 3, 10, 8, 6, 9, 2, 1, 4]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == [100, 102, 104, 106, 108, 101, 103, 105, 107, 109]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]) == [100, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 99]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10, 11, 12, 13, 14, 15]) == [9, 8, 2, 7, 3, 6, 4, 5, 1, 10, 11, 12, 13, 14, 15]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [10, 8, 7, 6, 5, 4, 3, 2, 1, 19, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20]
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10]) == [5, 8, 6, 2, 7, 4, 1, 3, 9, 10]
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [5, 3, 2, 1, 9, 4, 6, 7, 8, 10]
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [25, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 24]
    assert candidate(nums = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]
    assert candidate(nums = [5, 2, 7, 1, 8, 3, 6, 4, 9, 10, 1, 1, 1, 1, 1]) == [5, 7, 1, 3, 9, 2, 8, 6, 4, 10, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == [1, 5, 4, 9, 8, 13, 12, 3, 2, 7, 6, 11, 10, 15, 14]
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == [2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == [1, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 8, 7, 6, 5, 4, 3, 2, 1, 9]
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == [1, 3, 2, 1, 3, 2, 1, 3, 2, 3, 2, 1, 3, 2, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 45, 35, 25, 15]) == [10, 30, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 25, 15, 20, 40, 55, 45, 35]
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 2, 1, 3, 18, 19, 21, 22, 23, 24, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [10, 25, 30, 5, 2, 1, 3, 18, 19, 21, 22, 23, 24, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 15]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == [1, 5, 4, 9, 8, 13, 12, 3, 2, 7, 6, 11, 10, 15, 14]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 1, 2, 2, 3, 4, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert candidate(nums = [7, 3, 15, 10, 12, 1, 13, 5, 8, 2, 14, 9, 6, 11, 4]) == [7, 15, 10, 12, 1, 13, 5, 8, 2, 14, 9, 6, 11, 4, 3]
    assert candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == [5, 9, 2, 8, 3, 7, 4, 6, 1, 10]
    assert candidate(nums = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4]) == [1, 3, 2, 10, 9, 8, 7, 6, 5, 4]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 7, 6, 5, 4, 3, 2, 1, 8]
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == [9, 8, 2, 7, 3, 6, 4, 5, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 110, 120, 130, 140, 150, 5, 15, 25, 35, 45]) == [100, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 90, 110, 120, 130, 140, 150, 35, 45]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [1, 5, 9, 13, 17, 4, 8, 12, 16, 20, 3, 7, 11, 15, 19, 2, 6, 10, 14, 18]
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == [1, 1, 2, 3, 3, 1, 2, 2, 3, 3]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [1, 3, 5, 2, 4, 1, 3, 5, 2, 4, 2, 4, 1, 3, 5, 2, 4, 1, 3, 5]
    assert candidate(nums = [10, 20, 15, 10, 5, 25, 30, 5, 15, 25]) == [10, 25, 30, 5, 15, 25, 20, 15, 10, 5]
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1000000000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == [1, 5, 4, 9, 8, 13, 12, 17, 16, 20, 3, 2, 7, 6, 11, 10, 15, 14, 19, 18]
    assert candidate(nums = [50, 20, 30, 10, 40, 1, 2, 3, 4, 5]) == [50, 30, 10, 40, 1, 2, 3, 4, 5, 20]
    assert candidate(nums = [50, 40, 30, 20, 10, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == [50, 30, 20, 10, 15, 25, 45, 105, 125, 145, 40, 35, 55, 65, 75, 85, 95, 115, 135, 155]
    assert candidate(nums = [25, 25, 25, 25, 25, 50, 50, 50, 50, 50, 75, 75, 75, 75, 75, 100, 100, 100, 100, 100]) == [25, 25, 25, 50, 50, 75, 75, 75, 100, 100, 25, 25, 50, 50, 50, 75, 75, 100, 100, 100]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]


