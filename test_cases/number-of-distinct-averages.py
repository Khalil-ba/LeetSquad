def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 100, 50, 50, 25, 75]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 100, 50, 50, 25, 75]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 4, 0, 3, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 4, 0, 3, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 98, 2, 97, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 98, 2, 97, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6, 6, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6, 6, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 6, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 6, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 50, 50, 25, 75, 20, 80]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 50, 50, 25, 75, 20, 80]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 100, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 100, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 75, 20, 80, 15, 85, 10, 90, 5, 95]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 75, 20, 80, 15, 85, 10, 90, 5, 95]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 33, 33, 67, 67, 67]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 33, 33, 67, 67, 67]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 34, 56, 78, 90, 24, 46, 68]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 34, 56, 78, 90, 24, 46, 68]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 13, 21, 34, 55, 89, 144]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 13, 21, 34, 55, 89, 144]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 99, 99, 99, 2, 2, 2, 98, 98, 98]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 99, 99, 99, 2, 2, 2, 98, 98, 98]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 105, 94, 84, 74, 64, 54, 44, 34]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 105, 94, 84, 74, 64, 54, 44, 34]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 99, 98, 97, 96, 95]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 99, 98, 97, 96, 95]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 100, 100, 100, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 100, 100, 100, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [88, 92, 77, 65, 99, 100, 42, 33, 21, 11, 55, 66, 78, 89, 90, 91]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [88, 92, 77, 65, 99, 100, 42, 33, 21, 11, 55, 66, 78, 89, 90, 91]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 2, 1, 4, 5, 5, 4, 6, 7, 7, 6, 8, 9, 9, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 2, 1, 4, 5, 5, 4, 6, 7, 7, 6, 8, 9, 9, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 25, 15, 35, 45, 55, 65, 75, 85, 95, 105, 115]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 25, 15, 35, 45, 55, 65, 75, 85, 95, 105, 115]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [40, 20, 60, 80, 100, 0, 50, 30, 90, 70]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [40, 20, 60, 80, 100, 0, 50, 30, 90, 70]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 15, 35, 55, 75]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 15, 35, 55, 75]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 50, 50, 25, 75, 20, 80]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 50, 50, 25, 75, 20, 80]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 12, 67, 89, 34, 56, 78, 90, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 12, 67, 89, 34, 56, 78, 90, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 1, 4, 6, 5, 8, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 1, 4, 6, 5, 8, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90, 11, 89, 12, 88, 13, 87, 14, 86]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90, 11, 89, 12, 88, 13, 87, 14, 86]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 100, 90, 80, 70, 60, 55]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 100, 90, 80, 70, 60, 55]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 50, 2, 50, 3, 50, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 50, 2, 50, 3, 50, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 2, 5, 7, 3, 8, 10, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 2, 5, 7, 3, 8, 10, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 100, 100, 100, 100, 50, 50, 50, 50]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 100, 100, 100, 100, 50, 50, 50, 50]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 51, 24, 76, 38, 62, 19, 81, 9, 90]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 51, 24, 76, 38, 62, 19, 81, 9, 90]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 100, 50, 51, 49, 52, 48, 53, 47, 54]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 100, 50, 51, 49, 52, 48, 53, 47, 54]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 4, 4, 6, 6, 8, 8, 10, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 4, 4, 6, 6, 8, 8, 10, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 10, 40, 60, 80, 70]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 10, 40, 60, 80, 70]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == 1
    assert candidate(nums = [50, 50, 50, 50]) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [1, 2, 3, 4]) == 1
    assert candidate(nums = [0, 100, 50, 50, 25, 75]) == 1
    assert candidate(nums = [1, 100]) == 1
    assert candidate(nums = [4, 1, 4, 0, 3, 5]) == 2
    assert candidate(nums = [5, 5, 5, 5]) == 1
    assert candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6]) == 1
    assert candidate(nums = [99, 1, 98, 2, 97, 3]) == 1
    assert candidate(nums = [0, 0, 0, 0]) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [6, 6, 6, 6, 6, 6]) == 1
    assert candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4]) == 1
    assert candidate(nums = [1, 3, 2, 4, 6, 5]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 1
    assert candidate(nums = [100, 0, 50, 50, 25, 75, 20, 80]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [0, 100, 50, 50]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 1
    assert candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == 1
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 1
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50]) == 1
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93]) == 1
    assert candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]) == 6
    assert candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97]) == 1
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == 1
    assert candidate(nums = [25, 75, 20, 80, 15, 85, 10, 90, 5, 95]) == 1
    assert candidate(nums = [33, 33, 33, 67, 67, 67]) == 1
    assert candidate(nums = [12, 34, 56, 78, 90, 24, 46, 68]) == 1
    assert candidate(nums = [0, 100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93]) == 1
    assert candidate(nums = [5, 8, 13, 21, 34, 55, 89, 144]) == 4
    assert candidate(nums = [1, 1, 1, 99, 99, 99, 2, 2, 2, 98, 98, 98]) == 1
    assert candidate(nums = [95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 105, 94, 84, 74, 64, 54, 44, 34]) == 2
    assert candidate(nums = [0, 1, 2, 99, 98, 97, 96, 95]) == 2
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1
    assert candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5]) == 1
    assert candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95]) == 1
    assert candidate(nums = [1, 1, 1, 1, 100, 100, 100, 100]) == 1
    assert candidate(nums = [23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
    assert candidate(nums = [88, 92, 77, 65, 99, 100, 42, 33, 21, 11, 55, 66, 78, 89, 90, 91]) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1
    assert candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 1
    assert candidate(nums = [1, 2, 3, 3, 2, 1, 4, 5, 5, 4, 6, 7, 7, 6, 8, 9, 9, 8]) == 1
    assert candidate(nums = [5, 25, 15, 35, 45, 55, 65, 75, 85, 95, 105, 115]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1
    assert candidate(nums = [40, 20, 60, 80, 100, 0, 50, 30, 90, 70]) == 2
    assert candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0]) == 1
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 1
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]) == 2
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 15, 35, 55, 75]) == 4
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 1
    assert candidate(nums = [100, 0, 50, 50, 25, 75, 20, 80]) == 1
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 1
    assert candidate(nums = [23, 45, 12, 67, 89, 34, 56, 78, 90, 10]) == 2
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1
    assert candidate(nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
    assert candidate(nums = [2, 3, 1, 4, 6, 5, 8, 7]) == 1
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [8, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90, 11, 89, 12, 88, 13, 87, 14, 86]) == 1
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 1
    assert candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90]) == 1
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 100, 90, 80, 70, 60, 55]) == 2
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92]) == 1
    assert candidate(nums = [50, 1, 50, 2, 50, 3, 50, 4]) == 4
    assert candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1
    assert candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96]) == 1
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 1
    assert candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4]) == 1
    assert candidate(nums = [9, 2, 5, 7, 3, 8, 10, 1]) == 2
    assert candidate(nums = [1, 1, 1, 1, 100, 100, 100, 100, 50, 50, 50, 50]) == 2
    assert candidate(nums = [49, 51, 24, 76, 38, 62, 19, 81, 9, 90]) == 2
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 1
    assert candidate(nums = [0, 100, 50, 51, 49, 52, 48, 53, 47, 54]) == 2
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 3
    assert candidate(nums = [25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(nums = [2, 2, 4, 4, 6, 6, 8, 8, 10, 10]) == 1
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]) == 2
    assert candidate(nums = [50, 20, 30, 10, 40, 60, 80, 70]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 1
    assert candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == 1
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1
    assert candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80]) == 1


