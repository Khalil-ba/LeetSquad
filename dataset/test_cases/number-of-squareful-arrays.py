def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [9, 0, 16, 25, 36]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 0, 16, 25, 36]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 17, 8]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 17, 8]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 0, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 0, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 15, 33, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 15, 33, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 9, 4, 0, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 9, 4, 0, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 15, 33]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 15, 33]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 0, 4, 10, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 0, 4, 10, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 10, 5, 15, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 10, 5, 15, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 4, 1, 4, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 4, 1, 4, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 8, 10, 18, 26]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 8, 10, 18, 26]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 10, 17, 26, 37, 50, 65, 82]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 10, 17, 26, 37, 50, 65, 82]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 4, 9, 16, 25, 36, 49]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 4, 9, 16, 25, 36, 49]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 7, 8, 18, 20, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 7, 8, 18, 20, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 9, 11, 14, 16, 19, 21, 25, 27, 30, 32]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 9, 11, 14, 16, 19, 21, 25, 27, 30, 32]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 21, 26, 30, 35, 40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 21, 26, 30, 35, 40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 9, 0, 4, 25, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 9, 0, 4, 25, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 36, 49, 64, 81, 100, 121]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 36, 49, 64, 81, 100, 121]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 9, 10, 15, 21, 30, 36, 45, 55]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 9, 10, 15, 21, 30, 36, 45, 55]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 20, 22, 24, 26, 28, 30, 32, 34, 36]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 20, 22, 24, 26, 28, 30, 32, 34, 36]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 18, 28, 38, 48, 58, 68, 78, 88, 98]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 18, 28, 38, 48, 58, 68, 78, 88, 98]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 13, 29, 34, 37, 41, 50, 53, 61, 65, 72, 74]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 13, 29, 34, 37, 41, 50, 53, 61, 65, 72, 74]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 6, 11, 15, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 6, 11, 15, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 8, 18, 32, 50, 72, 98, 128, 162, 200, 242]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 8, 18, 32, 50, 72, 98, 128, 162, 200, 242]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 3, 0, 9, 16, 25, 36, 49]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 3, 0, 9, 16, 25, 36, 49]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 7, 11, 15, 20, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 7, 11, 15, 20, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [81, 180, 144, 121, 100, 25, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [81, 180, 144, 121, 100, 25, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6, 10, 15, 21]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6, 10, 15, 21]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 121]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 121]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 17, 28, 39, 50, 61, 72, 83]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 17, 28, 39, 50, 61, 72, 83]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 6, 7, 8, 15, 21, 30, 35, 42, 48, 55]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 6, 7, 8, 15, 21, 30, 35, 42, 48, 55]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 8, 12, 13, 16, 17, 24, 25, 28, 32, 33]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 8, 12, 13, 16, 17, 24, 25, 28, 32, 33]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 16, 81, 144, 121, 100, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 16, 81, 144, 121, 100, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 16, 9, 4, 0, 36, 25, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 16, 9, 4, 0, 36, 25, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 9, 10, 15, 21, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 9, 10, 15, 21, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 4, 4, 9, 9, 16, 16, 25, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 4, 4, 9, 9, 16, 16, 25, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 9, 13, 15, 17, 21, 25, 27, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 9, 13, 15, 17, 21, 25, 27, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 18, 23, 26, 32, 35, 38, 41]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 18, 23, 26, 32, 35, 38, 41]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 6, 5, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 6, 5, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 15, 1, 28, 25, 24]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 15, 1, 28, 25, 24]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 6, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 6, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [144, 169, 196, 225, 256, 289, 324, 361]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [144, 169, 196, 225, 256, 289, 324, 361]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 108, 118]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 108, 118]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 3, 12, 5, 13, 25, 16, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 3, 12, 5, 13, 25, 16, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [16, 9, 4, 1, 0, 25, 36, 49, 64, 81]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [16, 9, 4, 1, 0, 25, 36, 49, 64, 81]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [36, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [36, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 120]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 120]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 6, 9, 10, 13, 15, 16, 18, 19, 20, 25, 28]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 6, 9, 10, 13, 15, 16, 18, 19, 20, 25, 28]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 12, 27, 48, 75, 108, 147, 192, 243, 300, 363, 432]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 12, 27, 48, 75, 108, 147, 192, 243, 300, 363, 432]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 36, 25, 16, 9, 4, 1, 0, 81, 64, 49, 36]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 36, 25, 16, 9, 4, 1, 0, 81, 64, 49, 36]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 21, 35, 51, 70, 92, 117, 144, 173, 204, 237]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 21, 35, 51, 70, 92, 117, 144, 173, 204, 237]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 6, 11, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 6, 11, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 24, 35, 46, 57, 68, 79, 90, 101, 112, 123]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 24, 35, 46, 57, 68, 79, 90, 101, 112, 123]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 17, 8, 2, 18, 20, 32, 50, 33, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 17, 8, 2, 18, 20, 32, 50, 33, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 21, 26, 35, 40, 51, 56, 65, 70, 85, 90]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 21, 26, 35, 40, 51, 56, 65, 70, 85, 90]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]) == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [9, 0, 16, 25, 36]) == 0
    assert candidate(nums = [2, 2, 2]) == 1
    assert candidate(nums = [1, 17, 8]) == 2
    assert candidate(nums = [9, 0, 9]) == 1
    assert candidate(nums = [0, 0, 0]) == 1
    assert candidate(nums = [4, 6, 15, 33, 50]) == 0
    assert candidate(nums = [0, 1, 1, 0]) == 3
    assert candidate(nums = [16, 9, 4, 0, 25]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0
    assert candidate(nums = [1, 1, 1, 1]) == 0
    assert candidate(nums = [4, 6, 15, 33]) == 0
    assert candidate(nums = [9, 0, 4, 10, 9]) == 0
    assert candidate(nums = [0, 0, 0, 0]) == 1
    assert candidate(nums = [1, 2, 3, 6, 10]) == 0
    assert candidate(nums = [25, 10, 5, 15, 20]) == 0
    assert candidate(nums = [9, 4, 1, 4, 9]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9]) == 0
    assert candidate(nums = [2, 8, 10, 18, 26]) == 0
    assert candidate(nums = [1, 2, 5, 10, 17, 26, 37, 50, 65, 82]) == 0
    assert candidate(nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]) == 12
    assert candidate(nums = [0, 4, 9, 16, 25, 36, 49]) == 0
    assert candidate(nums = [2, 7, 8, 18, 20, 25]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45]) == 4
    assert candidate(nums = [4, 6, 9, 11, 14, 16, 19, 21, 25, 27, 30, 32]) == 0
    assert candidate(nums = [100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441]) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0
    assert candidate(nums = [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156]) == 0
    assert candidate(nums = [10, 15, 21, 26, 30, 35, 40]) == 0
    assert candidate(nums = [16, 9, 0, 4, 25, 1]) == 0
    assert candidate(nums = [25, 36, 49, 64, 81, 100, 121]) == 0
    assert candidate(nums = [4, 6, 9, 10, 15, 21, 30, 36, 45, 55]) == 0
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 0
    assert candidate(nums = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0
    assert candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]) == 0
    assert candidate(nums = [18, 20, 22, 24, 26, 28, 30, 32, 34, 36]) == 0
    assert candidate(nums = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]) == 0
    assert candidate(nums = [1, 2, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]) == 0
    assert candidate(nums = [8, 18, 28, 38, 48, 58, 68, 78, 88, 98]) == 0
    assert candidate(nums = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 0
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 0
    assert candidate(nums = [5, 13, 29, 34, 37, 41, 50, 53, 61, 65, 72, 74]) == 0
    assert candidate(nums = [2, 3, 6, 11, 15, 20]) == 0
    assert candidate(nums = [0, 2, 8, 18, 32, 50, 72, 98, 128, 162, 200, 242]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 0
    assert candidate(nums = [4, 1, 3, 0, 9, 16, 25, 36, 49]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0
    assert candidate(nums = [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256]) == 0
    assert candidate(nums = [2, 7, 11, 15, 20, 25]) == 0
    assert candidate(nums = [81, 180, 144, 121, 100, 25, 0]) == 0
    assert candidate(nums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]) == 12
    assert candidate(nums = [1, 2, 3, 6, 10, 15, 21]) == 0
    assert candidate(nums = [81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 121]) == 0
    assert candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68]) == 0
    assert candidate(nums = [8, 17, 28, 39, 50, 61, 72, 83]) == 0
    assert candidate(nums = [2, 3, 6, 7, 8, 15, 21, 30, 35, 42, 48, 55]) == 0
    assert candidate(nums = [5, 7, 8, 12, 13, 16, 17, 24, 25, 28, 32, 33]) == 0
    assert candidate(nums = [1, 16, 81, 144, 121, 100, 25]) == 0
    assert candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]) == 0
    assert candidate(nums = [1, 16, 9, 4, 0, 36, 25, 10]) == 0
    assert candidate(nums = [49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82]) == 0
    assert candidate(nums = [4, 6, 9, 10, 15, 21, 25]) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 0
    assert candidate(nums = [0, 0, 1, 1, 4, 4, 9, 9, 16, 16, 25, 25]) == 0
    assert candidate(nums = [4, 6, 9, 13, 15, 17, 21, 25, 27, 31]) == 0
    assert candidate(nums = [5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265]) == 0
    assert candidate(nums = [8, 15, 18, 23, 26, 32, 35, 38, 41]) == 0
    assert candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]) == 0
    assert candidate(nums = [2, 3, 6, 5, 9, 10]) == 0
    assert candidate(nums = [8, 7, 15, 1, 28, 25, 24]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21]) == 0
    assert candidate(nums = [1, 2, 2, 3, 6, 10]) == 0
    assert candidate(nums = [144, 169, 196, 225, 256, 289, 324, 361]) == 0
    assert candidate(nums = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 0
    assert candidate(nums = [8, 18, 28, 38, 48, 58, 68, 78, 88, 98, 108, 118]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 0
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]) == 12
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49]) == 0
    assert candidate(nums = [8, 7, 3, 12, 5, 13, 25, 16, 9]) == 0
    assert candidate(nums = [16, 9, 4, 1, 0, 25, 36, 49, 64, 81]) == 0
    assert candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49]) == 0
    assert candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]) == 0
    assert candidate(nums = [36, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 120]) == 0
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 0
    assert candidate(nums = [4, 6, 9, 10, 13, 15, 16, 18, 19, 20, 25, 28]) == 0
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 0
    assert candidate(nums = [3, 12, 27, 48, 75, 108, 147, 192, 243, 300, 363, 432]) == 0
    assert candidate(nums = [49, 36, 25, 16, 9, 4, 1, 0, 81, 64, 49, 36]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 0
    assert candidate(nums = [10, 21, 35, 51, 70, 92, 117, 144, 173, 204, 237]) == 0
    assert candidate(nums = [2, 3, 6, 11, 19, 20]) == 0
    assert candidate(nums = [8, 15, 24, 35, 46, 57, 68, 79, 90, 101, 112, 123]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 0
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 0
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81]) == 0
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 0
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [1, 17, 8, 2, 18, 20, 32, 50, 33, 6]) == 0
    assert candidate(nums = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100]) == 0
    assert candidate(nums = [50, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]) == 0
    assert candidate(nums = [10, 15, 21, 26, 35, 40, 51, 56, 65, 70, 85, 90]) == 0
    assert candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49]) == 0
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]) == 12


