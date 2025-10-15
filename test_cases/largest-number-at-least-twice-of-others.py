def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 3, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 3, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 3, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 3, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 16]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 16]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 0, 3, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 0, 3, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 3, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 3, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 7, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 7, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 12, 6, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 12, 6, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 20, 3, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 20, 3, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 20, 3, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 20, 3, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 0, 3, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 0, 3, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [81, 27, 9, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [81, 27, 9, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 25, 50, 75, 0, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 25, 50, 75, 0, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == 79: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 50, 500, 5000, 50000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 50, 500, 5000, 50000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 15, 7, 4, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 15, 7, 4, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 10, 5, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 10, 5, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 21, 7, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 21, 7, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 10, 5, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 10, 5, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 30, 10, 5, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 30, 10, 5, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 15, 9, 4, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 15, 9, 4, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [36, 18, 9, 4, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [36, 18, 9, 4, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 60]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 60]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 21, 10, 5, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 21, 10, 5, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 24, 12, 6, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 24, 12, 6, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [85, 84, 83, 82, 81, 80]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [85, 84, 83, 82, 81, 80]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 49, 33, 24, 19, 16, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 49, 33, 24, 19, 16, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 5, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 5, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [55, 27, 13, 6, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [55, 27, 13, 6, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [80, 40, 20, 10, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [80, 40, 20, 10, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 33, 22, 11, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 33, 22, 11, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 5, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 5, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98, 49, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98, 49, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [48, 24, 12, 6, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [48, 24, 12, 6, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 10, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 10, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 12, 6, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 12, 6, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 24, 12, 6, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 24, 12, 6, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 3, 6, 12, 24, 48]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 3, 6, 12, 24, 48]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 15, 5, 30, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 15, 5, 30, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 25, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 25, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 40]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 40]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 45, 30, 15, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 45, 30, 15, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 78]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 78]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 18, 36]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 18, 36]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 80, 20, 40, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 80, 20, 40, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 17, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 17, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 21, 10, 5, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 21, 10, 5, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [77, 38, 19, 9, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [77, 38, 19, 9, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [70, 69, 35, 20, 10, 5, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [70, 69, 35, 20, 10, 5, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98, 49, 24, 12, 6, 3, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98, 49, 24, 12, 6, 3, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [150, 75, 37, 18, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [150, 75, 37, 18, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 45, 30, 20, 10, 5, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 45, 30, 20, 10, 5, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 21, 10, 9, 8, 7, 6, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 21, 10, 9, 8, 7, 6, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 15, 14, 13, 12, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 15, 14, 13, 12, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 33, 11, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 33, 11, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 5, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 5, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 3, 1, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 3, 1, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 9, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 9, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 5, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 5, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 3, 4, 5, 6, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 21, 10, 5, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 21, 10, 5, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 21, 10, 5, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 21, 10, 5, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 10, 5, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 10, 5, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 49, 48, 47, 46, 45]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 49, 48, 47, 46, 45]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 50, 25, 100, 75]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 50, 25, 100, 75]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 4, 4, 4, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 4, 4, 4, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [120, 60, 30, 15, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [120, 60, 30, 15, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 4, 2, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 4, 2, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 2, 4, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 2, 4, 6]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 6]) == 3
    assert candidate(nums = [3, 6, 1, 0]) == 1
    assert candidate(nums = [7, 1, 3, 2]) == 0
    assert candidate(nums = [10, 1, 2, 3]) == 0
    assert candidate(nums = [100, 1, 2, 3]) == 0
    assert candidate(nums = [7, 1, 3, 5]) == -1
    assert candidate(nums = [1, 100, 2, 3]) == 1
    assert candidate(nums = [8, 8, 8, 8, 8, 16]) == 5
    assert candidate(nums = [5, 0, 3, 2]) == -1
    assert candidate(nums = [1, 2, 3, 4]) == -1
    assert candidate(nums = [5, 8, 3, 4]) == -1
    assert candidate(nums = [1, 1, 1, 7, 1, 1, 1]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 7]) == 6
    assert candidate(nums = [5, 3, 1, 4]) == -1
    assert candidate(nums = [50, 25, 12, 6, 3, 1]) == 0
    assert candidate(nums = [1, 20, 3, 4]) == 1
    assert candidate(nums = [1, 1, 1, 100]) == 3
    assert candidate(nums = [10, 20]) == 1
    assert candidate(nums = [10, 5, 3, 1]) == 0
    assert candidate(nums = [1, 20, 3, 1]) == 1
    assert candidate(nums = [1, 0, 0, 0, 0]) == 0
    assert candidate(nums = [0, 0, 0, 1]) == 3
    assert candidate(nums = [8, 16, 32, 4]) == 2
    assert candidate(nums = [1, 2, 0, 4]) == 3
    assert candidate(nums = [2, 1, 3, 6]) == 3
    assert candidate(nums = [10, 5, 2]) == 0
    assert candidate(nums = [7, 0, 3, 10]) == -1
    assert candidate(nums = [7, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 10, 2, 3]) == 1
    assert candidate(nums = [8, 1, 3, 4]) == 0
    assert candidate(nums = [1, 2, 0]) == 1
    assert candidate(nums = [81, 27, 9, 3, 1]) == 0
    assert candidate(nums = [100, 25, 50, 75, 0, 100]) == -1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]) == 19
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == -1
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == 79
    assert candidate(nums = [5, 50, 500, 5000, 50000]) == 4
    assert candidate(nums = [30, 15, 7, 4, 2]) == 0
    assert candidate(nums = [8, 4, 4, 2, 1]) == 0
    assert candidate(nums = [50, 25, 10, 5, 1]) == 0
    assert candidate(nums = [42, 21, 7, 3, 1]) == 0
    assert candidate(nums = [50, 25, 10, 5, 1, 0]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50]) == -1
    assert candidate(nums = [60, 30, 10, 5, 2]) == 0
    assert candidate(nums = [30, 15, 9, 4, 2]) == 0
    assert candidate(nums = [36, 18, 9, 4, 2]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 60]) == 10
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [42, 21, 10, 5, 2]) == 0
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60]) == -1
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 6
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == -1
    assert candidate(nums = [100, 99, 98, 97, 96, 95]) == -1
    assert candidate(nums = [49, 24, 12, 6, 3, 1]) == 0
    assert candidate(nums = [85, 84, 83, 82, 81, 80]) == -1
    assert candidate(nums = [10, 10, 10, 10, 20]) == 4
    assert candidate(nums = [25, 24, 23, 22, 21]) == -1
    assert candidate(nums = [99, 49, 33, 24, 19, 16, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == -1
    assert candidate(nums = [20, 10, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [30, 20, 10, 5, 2, 1]) == -1
    assert candidate(nums = [55, 27, 13, 6, 3]) == 0
    assert candidate(nums = [80, 40, 20, 10, 5]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == -1
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == 44
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == -1
    assert candidate(nums = [99, 33, 22, 11, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [20, 10, 5, 1]) == 0
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [98, 49, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [48, 24, 12, 6, 3]) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256]) == 7
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == -1
    assert candidate(nums = [100, 50, 25, 10, 5]) == 0
    assert candidate(nums = [50, 25, 12, 6, 3, 1]) == 0
    assert candidate(nums = [49, 24, 12, 6, 3, 1]) == 0
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == 0
    assert candidate(nums = [9, 18, 3, 6, 12, 24, 48]) == 6
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0]) == 0
    assert candidate(nums = [25, 15, 5, 30, 10]) == -1
    assert candidate(nums = [49, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]) == -1
    assert candidate(nums = [50, 49, 25, 10]) == -1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 40]) == 10
    assert candidate(nums = [100, 99, 98, 97, 96]) == -1
    assert candidate(nums = [90, 45, 30, 15, 7]) == 0
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == -1
    assert candidate(nums = [9, 7, 5, 3, 1]) == -1
    assert candidate(nums = [50, 49, 48, 47, 46]) == -1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 78]) == 20
    assert candidate(nums = [3, 6, 9, 18, 36]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(nums = [8, 80, 20, 40, 10]) == 1
    assert candidate(nums = [100, 99, 98, 97, 96]) == -1
    assert candidate(nums = [34, 17, 8, 4, 2, 1]) == 0
    assert candidate(nums = [42, 21, 10, 5, 3]) == 0
    assert candidate(nums = [60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == -1
    assert candidate(nums = [77, 38, 19, 9, 4, 2, 1]) == 0
    assert candidate(nums = [70, 69, 35, 20, 10, 5, 1]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50]) == -1
    assert candidate(nums = [98, 49, 24, 12, 6, 3, 1, 0]) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128]) == 6
    assert candidate(nums = [3, 3, 3, 3, 3, 6]) == 5
    assert candidate(nums = [150, 75, 37, 18, 9]) == 0
    assert candidate(nums = [8, 16, 32, 64, 128]) == 4
    assert candidate(nums = [90, 45, 30, 20, 10, 5, 1]) == 0
    assert candidate(nums = [42, 21, 10, 9, 8, 7, 6, 5]) == 0
    assert candidate(nums = [30, 15, 14, 13, 12, 11]) == 0
    assert candidate(nums = [99, 33, 11, 3, 1]) == 0
    assert candidate(nums = [20, 10, 5, 1, 0]) == 0
    assert candidate(nums = [100, 99, 98, 97, 96, 95]) == -1
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == -1
    assert candidate(nums = [64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums = [9, 3, 1, 0, 0]) == 0
    assert candidate(nums = [18, 9, 4, 2, 1]) == 0
    assert candidate(nums = [20, 10, 5, 2, 1]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == -1
    assert candidate(nums = [10, 9, 8, 7, 6]) == -1
    assert candidate(nums = [100, 50, 25, 12, 6]) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 10
    assert candidate(nums = [1, 100, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(nums = [42, 21, 10, 5, 3, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]) == 19
    assert candidate(nums = [42, 21, 10, 5, 3, 2, 1]) == 0
    assert candidate(nums = [25, 10, 5, 3, 1]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(nums = [100, 49, 48, 47, 46, 45]) == 0
    assert candidate(nums = [5, 50, 25, 100, 75]) == -1
    assert candidate(nums = [8, 16, 32, 64, 128]) == 4
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21]) == -1
    assert candidate(nums = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 50]) == -1
    assert candidate(nums = [1, 10, 100, 1000, 10000]) == 4
    assert candidate(nums = [4, 4, 4, 4, 8]) == 4
    assert candidate(nums = [120, 60, 30, 15, 7]) == 0
    assert candidate(nums = [8, 4, 2, 1, 1, 1, 1]) == 0
    assert candidate(nums = [8, 16, 2, 4, 6]) == 1


