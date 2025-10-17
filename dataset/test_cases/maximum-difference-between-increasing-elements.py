def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [9, 4, 3, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 4, 3, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 999999999]) == 999999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 999999999]) == 999999998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 999999999, 2, 999999998]) == 999999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 999999999, 2, 999999998]) == 999999998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 20, 10, 30]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 20, 10, 30]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10, 1, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10, 1, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 7, 9, 14, 10]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 7, 9, 14, 10]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 11]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 11]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 1, 1000000000, 2, 999999998, 3, 1000000000, 4, 999999997]) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 1, 1000000000, 2, 999999998, 3, 1000000000, 4, 999999997]) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 101, 100, 100, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 101, 100, 100, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 10, 6, 4, 8, 1, 5, 7, 9]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 10, 6, 4, 8, 1, 5, 7, 9]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 2, 8, 1, 5, 6, 3, 9]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 2, 8, 1, 5, 6, 3, 9]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997]) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997]) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 100, 1, 2, 3, 4]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 100, 1, 2, 3, 4]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 31]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 31]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 5, 3, 4, 8, 7, 6, 9, 10, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 5, 3, 4, 8, 7, 6, 9, 10, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 11, 9, 8, 10, 12]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 11, 9, 8, 10, 12]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 10, 8, 9, 7, 8, 6, 7, 5, 6, 4, 5, 3, 4, 2, 3, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 10, 8, 9, 7, 8, 6, 7, 5, 6, 4, 5, 3, 4, 2, 3, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 150]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 150]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 10, 11, 12, 13]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 10, 11, 12, 13]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 1, 2, 2, 2, 5, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 1, 2, 2, 2, 5, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 100, 1, 2, 3, 101, 1, 2, 3, 102, 1, 2, 3, 103, 1, 2, 3, 104]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 100, 1, 2, 3, 101, 1, 2, 3, 102, 1, 2, 3, 103, 1, 2, 3, 104]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 1, 9, 4, 3, 7, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 1, 9, 4, 3, 7, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 25, 30, 5, 10, 40, 35, 45, 50]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 25, 30, 5, 10, 40, 35, 45, 50]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 7, 9, 2, 6, 8, 4, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 7, 9, 2, 6, 8, 4, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 6, 7, 2, 5, 4, 8, 9, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 6, 7, 2, 5, 4, 8, 9, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 1, 1, 1, 2, 2, 2, 5, 5, 5, 4, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 1, 1, 1, 2, 2, 2, 5, 5, 5, 4, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 11, 2, 14, 1, 3, 10, 6, 12, 4, 15, 8]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 11, 2, 14, 1, 3, 10, 6, 12, 4, 15, 8]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 101, 2, 102, 3, 103, 4, 104, 5, 105, 6, 106, 7, 107, 8, 108, 9, 109, 10]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 101, 2, 102, 3, 103, 4, 104, 5, 105, 6, 106, 7, 107, 8, 108, 9, 109, 10]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 6, 5, 0, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 6, 5, 0, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 10, 40, 60, 25, 35, 55, 45, 70, 65, 80, 75, 90, 85, 100, 95]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 10, 40, 60, 25, 35, 55, 45, 70, 65, 80, 75, 90, 85, 100, 95]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 100, 5, 6, 7, 8, 9, 10]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 100, 5, 6, 7, 8, 9, 10]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 1, 4, 7, 6, 8]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 1, 4, 7, 6, 8]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 101, 100, 100, 100, 100, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 101, 100, 100, 100, 100, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 75, 100, 200, 150, 175, 225, 275, 300, 250, 325, 350]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 75, 100, 200, 150, 175, 225, 275, 300, 250, 325, 350]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 1, 7, 3, 6, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 1, 7, 3, 6, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 1000000001]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 1000000001]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 101, 2, 102, 3, 103, 4, 104, 5]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 101, 2, 102, 3, 103, 4, 104, 5]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [9, 4, 3, 2]) == -1
    assert candidate(nums = [5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 2, 999999999]) == 999999998
    assert candidate(nums = [1, 100, 1, 100, 1]) == 99
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [1, 999999999, 2, 999999998]) == 999999998
    assert candidate(nums = [10, 20, 20, 10, 30]) == 20
    assert candidate(nums = [1, 5, 2, 10]) == 9
    assert candidate(nums = [1, 1, 1, 1]) == -1
    assert candidate(nums = [1, 3, 2, 4, 3, 5]) == 4
    assert candidate(nums = [10, 1, 10, 1, 10]) == 9
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [7, 1, 5, 4]) == 4
    assert candidate(nums = [1, 3, 6, 7, 9, 14, 10]) == 13
    assert candidate(nums = [1, 2, 1, 2, 1]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 10]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 11]) == 1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 8
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
    assert candidate(nums = [1000000000, 999999999, 999999998, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [1000000000, 999999999, 1, 1000000000, 2, 999999998, 3, 1000000000, 4, 999999997]) == 999999999
    assert candidate(nums = [100, 100, 100, 100, 101, 100, 100, 100]) == 1
    assert candidate(nums = [2, 3, 10, 6, 4, 8, 1, 5, 7, 9]) == 8
    assert candidate(nums = [10, 1, 2, 8, 1, 5, 6, 3, 9]) == 8
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 18
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997]) == 999999999
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 38
    assert candidate(nums = [3, 2, 1, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 6
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 29
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 1
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 9
    assert candidate(nums = [1, 3, 2, 3, 100, 1, 2, 3, 4]) == 99
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 9
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 31]) == 30
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
    assert candidate(nums = [2, 1, 5, 3, 4, 8, 7, 6, 9, 10, 1]) == 9
    assert candidate(nums = [8, 11, 9, 8, 10, 12]) == 4
    assert candidate(nums = [10, 9, 10, 8, 9, 7, 8, 6, 7, 5, 6, 4, 5, 3, 4, 2, 3, 1, 2]) == 1
    assert candidate(nums = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 9
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 150]) == 50
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 90
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 9
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15]) == 14
    assert candidate(nums = [5, 4, 3, 2, 1, 10, 11, 12, 13]) == 12
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == -1
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10
    assert candidate(nums = [999999999, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 99
    assert candidate(nums = [3, 3, 3, 1, 2, 2, 2, 5, 5, 5]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == -1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]) == 11
    assert candidate(nums = [1, 2, 3, 100, 1, 2, 3, 101, 1, 2, 3, 102, 1, 2, 3, 103, 1, 2, 3, 104]) == 103
    assert candidate(nums = [3, 3, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == 5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == 2
    assert candidate(nums = [5, 1, 4, 3, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == 20
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 18
    assert candidate(nums = [5, 2, 6, 1, 9, 4, 3, 7, 8]) == 8
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == -1
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 10, 40, 35, 45, 50]) == 45
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [1, 5, 3, 7, 9, 2, 6, 8, 4, 10]) == 9
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1]) == 90
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10
    assert candidate(nums = [5, 3, 6, 7, 2, 5, 4, 8, 9, 1]) == 7
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21]) == 20
    assert candidate(nums = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(nums = [5, 4, 3, 2, 1, 10]) == 9
    assert candidate(nums = [3, 3, 3, 1, 1, 1, 2, 2, 2, 5, 5, 5, 4, 4, 4]) == 4
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9
    assert candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 10
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 9
    assert candidate(nums = [5, 11, 2, 14, 1, 3, 10, 6, 12, 4, 15, 8]) == 14
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == -1
    assert candidate(nums = [100, 1, 101, 2, 102, 3, 103, 4, 104, 5, 105, 6, 106, 7, 107, 8, 108, 9, 109, 10]) == 108
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [3, 2, 6, 5, 0, 3]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(nums = [50, 20, 30, 10, 40, 60, 25, 35, 55, 45, 70, 65, 80, 75, 90, 85, 100, 95]) == 90
    assert candidate(nums = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 11
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11]) == 10
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996]) == 999999999
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 9
    assert candidate(nums = [1, 2, 3, 4, 100, 5, 6, 7, 8, 9, 10]) == 99
    assert candidate(nums = [5, 2, 3, 1, 4, 7, 6, 8]) == 7
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
    assert candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 9
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2]) == -1
    assert candidate(nums = [100, 100, 100, 100, 101, 100, 100, 100, 100, 100]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18]) == 99
    assert candidate(nums = [50, 25, 75, 100, 200, 150, 175, 225, 275, 300, 250, 325, 350]) == 325
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40]) == 40
    assert candidate(nums = [10, 5, 1, 7, 3, 6, 4]) == 6
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 1000000001]) == 5
    assert candidate(nums = [100, 1, 101, 2, 102, 3, 103, 4, 104, 5]) == 103
    assert candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]) == 4


