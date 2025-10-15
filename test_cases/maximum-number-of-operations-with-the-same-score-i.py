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
        result = candidate(nums = [1, 100, 1, 100, 1, 100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1, 999, 2, 998, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1, 999, 2, 998, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 3, 4, 1, 3, 2, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 3, 4, 1, 3, 2, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1, 1000, 1, 1000, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1, 1000, 1, 1000, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 100, 200, 100, 200]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 100, 200, 100, 200]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 100, 200, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 100, 200, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 98, 2, 97, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 98, 2, 97, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 30, 40]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 30, 40]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 13, 13, 7, 10, 10, 10, 10, 15, 15]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 13, 13, 7, 10, 10, 10, 10, 15, 15]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 84, 0, 84, 0, 168, -42, 42, 84, 168, -84, 84, 168, -168, 42]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 84, 0, 84, 0, 168, -42, 42, 84, 168, -84, 84, 168, -168, 42]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 10, 10, 20, 20, 10, 10, 20, 20, 10, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 10, 10, 20, 20, 10, 10, 20, 20, 10, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 25, 75, 25, 75, 100, 0, 0, 100, 10, 90, 20, 80, 30, 70]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 25, 75, 25, 75, 100, 0, 0, 100, 10, 90, 20, 80, 30, 70]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 10, 20, 20, 40, 40, 80, 80, 160, 160, 320, 320, 640, 640, 1280, 1280, 2560, 2560]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 10, 20, 20, 40, 40, 80, 80, 160, 160, 320, 320, 640, 640, 1280, 1280, 2560, 2560]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 1, 1, 100, 100, 2, 2, 100, 100, 3, 3, 100, 100, 4, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 1, 1, 100, 100, 2, 2, 100, 100, 3, 3, 100, 100, 4, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 12, 12, 18, 18, 24, 24, 30, 30, 36, 36, 42, 42, 48, 48, 54, 54, 60, 60]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 12, 12, 18, 18, 24, 24, 30, 30, 36, 36, 42, 42, 48, 48, 54, 54, 60, 60]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, 7, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, 7, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 5, 5, 2, 8, 6, 4, 3, 7, 1, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 5, 5, 2, 8, 6, 4, 3, 7, 1, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 250, 250, 125, 125, 625, 625, 312, 312]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 250, 250, 125, 125, 625, 625, 312, 312]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 3, 7, 5, 5, 2, 2, 8, 8, 1, 1, 9, 9, 4, 4, 6, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 3, 7, 5, 5, 2, 2, 8, 8, 1, 1, 9, 9, 4, 4, 6, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 3, 2, 1, 4, 5, 5, 4, 6, 7, 7, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 3, 2, 1, 4, 5, 5, 4, 6, 7, 7, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 3, 7, 7, 3, 3, 7, 7, 3, 3, 7, 7, 3, 3, 7]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 3, 7, 7, 3, 3, 7, 7, 3, 3, 7, 7, 3, 3, 7]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15, 1, 16, 1, 17, 1, 18, 1, 19, 1, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15, 1, 16, 1, 17, 1, 18, 1, 19, 1, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 84, 0, 42, 42, 84, 0, 42, 42]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 84, 0, 42, 42, 84, 0, 42, 42]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 49, 49, 50, 49, 50, 49, 48, 48, 48]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 49, 49, 50, 49, 50, 49, 48, 48, 48]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 30, 30, 40, 40, 50, 50]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 30, 30, 40, 40, 50, 50]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 5, 5, 10, 10, 5, 5, 10, 10, 5, 5, 10, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 5, 5, 10, 10, 5, 5, 10, 10, 5, 5, 10, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 250, 250, 750, 250, 500, 250, 500, 250, 750, 250, 500, 250, 750, 250, 500, 250]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 250, 250, 750, 250, 500, 250, 500, 250, 750, 250, 500, 250, 750, 250, 500, 250]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 25, 25, 75, 75, 25, 25, 75, 75]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 25, 25, 75, 75, 25, 25, 75, 75]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 1, 8, 2, 7, 3, 6, 4, 5, 1, 8, 1, 8, 2, 7, 3, 6, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 1, 8, 2, 7, 3, 6, 4, 5, 1, 8, 1, 8, 2, 7, 3, 6, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6, 93, 7, 92, 8, 91, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6, 93, 7, 92, 8, 91, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 999, 998, 1, 499, 500, 249, 751, 374, 626, 187, 813, 93, 907, 46, 954]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 999, 998, 1, 499, 500, 249, 751, 374, 626, 187, 813, 93, 907, 46, 954]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 14, 0, 14, 0, 21, -7, 7, 14, 28, -14, 14, 28, -21, 7]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 14, 0, 14, 0, 21, -7, 7, 14, 28, -14, 14, 28, -21, 7]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 15, 5, 20, 0, 15, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 15, 5, 20, 0, 15, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 30, 30, 40, 40, 50, 50, 60, 60]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 30, 30, 40, 40, 50, 50, 60, 60]) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == 1
    assert candidate(nums = [1, 100, 1, 100, 1, 100]) == 3
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == 4
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 5
    assert candidate(nums = [1000, 1, 999, 2, 998, 3]) == 3
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [1, 5, 3, 3, 4, 1, 3, 2, 2, 3]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 5
    assert candidate(nums = [1000, 1, 1000, 1, 1000, 1]) == 3
    assert candidate(nums = [100, 200, 100, 200, 100, 200]) == 3
    assert candidate(nums = [3, 2, 1, 4, 5]) == 2
    assert candidate(nums = [100, 200, 100, 200, 100]) == 2
    assert candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [5, 3]) == 1
    assert candidate(nums = [99, 1, 98, 2, 97, 3]) == 3
    assert candidate(nums = [10, 10, 10, 10, 10, 10]) == 3
    assert candidate(nums = [10, 10, 20, 20, 30, 30]) == 1
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3]) == 4
    assert candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5]) == 1
    assert candidate(nums = [10, 20, 10, 20, 30, 40]) == 2
    assert candidate(nums = [7, 13, 13, 7, 10, 10, 10, 10, 15, 15]) == 4
    assert candidate(nums = [42, 42, 84, 0, 84, 0, 168, -42, 42, 84, 168, -84, 84, 168, -168, 42]) == 3
    assert candidate(nums = [10, 10, 20, 20, 10, 10, 20, 20, 10, 10, 20, 20, 10, 10]) == 1
    assert candidate(nums = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]) == 11
    assert candidate(nums = [50, 50, 25, 75, 25, 75, 100, 0, 0, 100, 10, 90, 20, 80, 30, 70]) == 8
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 7
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10
    assert candidate(nums = [5, 5, 10, 10, 20, 20, 40, 40, 80, 80, 160, 160, 320, 320, 640, 640, 1280, 1280, 2560, 2560]) == 1
    assert candidate(nums = [33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67, 33, 67]) == 11
    assert candidate(nums = [45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55, 45, 55]) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [100, 100, 1, 1, 100, 100, 2, 2, 100, 100, 3, 3, 100, 100, 4, 4]) == 1
    assert candidate(nums = [6, 6, 12, 12, 18, 18, 24, 24, 30, 30, 36, 36, 42, 42, 48, 48, 54, 54, 60, 60]) == 1
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60]) == 1
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 6
    assert candidate(nums = [1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, 7, 8]) == 1
    assert candidate(nums = [10, 10, 5, 5, 2, 8, 6, 4, 3, 7, 1, 9]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 8
    assert candidate(nums = [500, 500, 250, 250, 125, 125, 625, 625, 312, 312]) == 1
    assert candidate(nums = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 16
    assert candidate(nums = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1]) == 8
    assert candidate(nums = [3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2]) == 1
    assert candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100]) == 5
    assert candidate(nums = [7, 3, 3, 7, 5, 5, 2, 2, 8, 8, 1, 1, 9, 9, 4, 4, 6, 6]) == 3
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 9
    assert candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40]) == 1
    assert candidate(nums = [1, 2, 3, 3, 2, 1, 4, 5, 5, 4, 6, 7, 7, 6]) == 1
    assert candidate(nums = [7, 3, 3, 7, 7, 3, 3, 7, 7, 3, 3, 7, 7, 3, 3, 7]) == 8
    assert candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15, 1, 16, 1, 17, 1, 18, 1, 19, 1, 20]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 1
    assert candidate(nums = [42, 42, 84, 0, 42, 42, 84, 0, 42, 42]) == 5
    assert candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 1
    assert candidate(nums = [50, 50, 50, 49, 49, 50, 49, 50, 49, 48, 48, 48]) == 1
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 5
    assert candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9]) == 9
    assert candidate(nums = [10, 20, 10, 20, 30, 30, 40, 40, 50, 50]) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 10
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 19
    assert candidate(nums = [5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10]) == 1
    assert candidate(nums = [10, 10, 5, 5, 10, 10, 5, 5, 10, 10, 5, 5, 10, 10]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11
    assert candidate(nums = [500, 500, 250, 250, 750, 250, 500, 250, 500, 250, 750, 250, 500, 250, 750, 250, 500, 250]) == 1
    assert candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5]) == 5
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 6
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 1
    assert candidate(nums = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 6
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3]) == 12
    assert candidate(nums = [50, 50, 25, 25, 75, 75, 25, 25, 75, 75]) == 1
    assert candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50]) == 1
    assert candidate(nums = [100, 1, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93]) == 1
    assert candidate(nums = [8, 1, 1, 8, 2, 7, 3, 6, 4, 5, 1, 8, 1, 8, 2, 7, 3, 6, 4, 5]) == 10
    assert candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6, 93, 7, 92, 8, 91, 9]) == 9
    assert candidate(nums = [7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3]) == 15
    assert candidate(nums = [8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1]) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200, 100, 200]) == 6
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 8
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 13
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 5
    assert candidate(nums = [1, 999, 998, 1, 499, 500, 249, 751, 374, 626, 187, 813, 93, 907, 46, 954]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 9
    assert candidate(nums = [7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3]) == 10
    assert candidate(nums = [7, 7, 14, 0, 14, 0, 21, -7, 7, 14, 28, -14, 14, 28, -21, 7]) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [10, 10, 15, 5, 20, 0, 15, 5]) == 4
    assert candidate(nums = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92]) == 8
    assert candidate(nums = [1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 1
    assert candidate(nums = [10, 20, 10, 20, 30, 30, 40, 40, 50, 50, 60, 60]) == 2


