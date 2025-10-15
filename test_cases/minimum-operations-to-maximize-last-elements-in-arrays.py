def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5],nums2 = [5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5],nums2 = [5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2],nums2 = [2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2],nums2 = [2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8],nums2 = [7, 6, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8],nums2 = [7, 6, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3],nums2 = [3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3],nums2 = [3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 1],nums2 = [2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 1],nums2 = [2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 1],nums2 = [4, 2, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 1],nums2 = [4, 2, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 4, 5, 9],nums2 = [8, 8, 4, 4, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 4, 5, 9],nums2 = [8, 8, 4, 4, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9],nums2 = [9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9],nums2 = [9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [15, 25, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [15, 25, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5],nums2 = [2, 4, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5],nums2 = [2, 4, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 4],nums2 = [2, 5, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 4],nums2 = [2, 5, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 7],nums2 = [4, 5, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 7],nums2 = [4, 5, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 4, 2],nums2 = [5, 3, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 4, 2],nums2 = [5, 3, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10],nums2 = [10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10],nums2 = [10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [10, 20, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [10, 20, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 1000000000],nums2 = [1000000000, 1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 1000000000],nums2 = [1000000000, 1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 9, 3, 7, 5],nums2 = [6, 2, 8, 4, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 9, 3, 7, 5],nums2 = [6, 2, 8, 4, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 5, 1, 4, 7, 3, 6, 8, 2, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 5, 1, 4, 7, 3, 6, 8, 2, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 999999999, 999999998],nums2 = [1, 2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 999999999, 999999998],nums2 = [1, 2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14],nums2 = [14, 12, 10, 8, 6, 4, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14],nums2 = [14, 12, 10, 8, 6, 4, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3],nums2 = [3, 3, 2, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3],nums2 = [3, 3, 2, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 20, 30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 20, 30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 3, 9, 5, 6, 4],nums2 = [2, 8, 4, 7, 10, 1, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 3, 9, 5, 6, 4],nums2 = [2, 8, 4, 7, 10, 1, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [60, 50, 40, 30, 20, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [60, 50, 40, 30, 20, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 1, 2],nums2 = [3, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 1, 2],nums2 = [3, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [45, 35, 25, 15, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [45, 35, 25, 15, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 1, 2],nums2 = [2, 1, 1, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 1, 2],nums2 = [2, 1, 1, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],nums2 = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],nums2 = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 8, 6, 7],nums2 = [4, 6, 2, 9, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 8, 6, 7],nums2 = [4, 6, 2, 9, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [8, 6, 4, 2, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [8, 6, 4, 2, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 1000000000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 1000000000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 6, 4, 3, 1],nums2 = [7, 5, 9, 2, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 6, 4, 3, 1],nums2 = [7, 5, 9, 2, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 9, 8, 7, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 9, 8, 7, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 100, 200, 300, 400]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 100, 200, 300, 400]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [2, 4, 6, 8, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [2, 4, 6, 8, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 8, 6, 2, 7, 4, 1, 9],nums2 = [9, 1, 4, 7, 2, 6, 8, 3, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 8, 6, 2, 7, 4, 1, 9],nums2 = [9, 1, 4, 7, 2, 6, 8, 3, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70, 60],nums2 = [60, 70, 80, 90, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70, 60],nums2 = [60, 70, 80, 90, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 9, 1, 3, 7],nums2 = [8, 4, 6, 2, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 9, 1, 3, 7],nums2 = [8, 4, 6, 2, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 1, 9, 3, 7, 2, 8, 4, 6, 10],nums2 = [1, 5, 3, 9, 2, 8, 4, 7, 10, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 1, 9, 3, 7, 2, 8, 4, 6, 10],nums2 = [1, 5, 3, 9, 2, 8, 4, 7, 10, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 2, 1, 4, 5, 6],nums2 = [6, 5, 4, 1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 2, 1, 4, 5, 6],nums2 = [6, 5, 4, 1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 2, 4, 5],nums2 = [5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 2, 4, 5],nums2 = [5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 1, 8, 2, 7],nums2 = [3, 6, 5, 4, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 1, 8, 2, 7],nums2 = [3, 6, 5, 4, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [2, 4, 6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [2, 4, 6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [10, 9, 8, 7, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [10, 9, 8, 7, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [10, 8, 6, 4, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [10, 8, 6, 4, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 1000000000],nums2 = [1000000000, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 1000000000],nums2 = [1000000000, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 2, 2, 2, 2],nums2 = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 2, 2, 2, 2],nums2 = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [3, 3, 2, 2, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [3, 3, 2, 2, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 8, 6, 7],nums2 = [4, 9, 2, 1, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 8, 6, 7],nums2 = [4, 9, 2, 1, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 1, 2],nums2 = [1, 2, 1000000000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 1, 2],nums2 = [1, 2, 1000000000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [6, 6, 6, 6, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [6, 6, 6, 6, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1000000000],nums2 = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1000000000],nums2 = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [49, 42, 35, 28, 21, 14, 7]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [49, 42, 35, 28, 21, 14, 7]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 1, 7, 9],nums2 = [8, 6, 4, 2, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 1, 7, 9],nums2 = [8, 6, 4, 2, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 7, 7, 7, 1],nums2 = [8, 8, 8, 8, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 7, 7, 7, 1],nums2 = [8, 8, 8, 8, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 6, 7, 5, 3, 0, 9],nums2 = [1, 4, 2, 8, 6, 7, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 6, 7, 5, 3, 0, 9],nums2 = [1, 4, 2, 8, 6, 7, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [11, 9, 7, 5, 3, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [11, 9, 7, 5, 3, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [1, 2, 3, 4, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [1, 2, 3, 4, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 1000000000],nums2 = [1000000000, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 1000000000],nums2 = [1000000000, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 1, 1, 1, 1],nums2 = [1, 1000000000, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 1, 1, 1, 1],nums2 = [1, 1000000000, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 3, 1, 2, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 3, 1, 2, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 2, 2],nums2 = [2, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 2, 2],nums2 = [2, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 2, 5, 4],nums2 = [4, 2, 3, 1, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 2, 5, 4],nums2 = [4, 2, 3, 1, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 2, 5, 7, 1],nums2 = [1, 8, 3, 4, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 2, 5, 7, 1],nums2 = [1, 8, 3, 4, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15],nums2 = [15, 12, 9, 6, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15],nums2 = [15, 12, 9, 6, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [10, 20, 30, 40, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [10, 20, 30, 40, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 7, 3, 9, 2],nums2 = [8, 1, 6, 4, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 7, 3, 9, 2],nums2 = [8, 1, 6, 4, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10, 10],nums2 = [10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10, 10],nums2 = [10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 1, 4, 2, 6, 8, 7, 10, 9],nums2 = [9, 7, 10, 8, 6, 4, 2, 5, 1, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 1, 4, 2, 6, 8, 7, 10, 9],nums2 = [9, 7, 10, 8, 6, 4, 2, 5, 1, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 8, 10, 2, 9],nums2 = [7, 6, 1, 10, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 8, 10, 2, 9],nums2 = [7, 6, 1, 10, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 3, 5, 8, 6],nums2 = [2, 4, 1, 9, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 3, 5, 8, 6],nums2 = [2, 4, 1, 9, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [9, 18, 27, 36, 45]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [9, 18, 27, 36, 45]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10, 10, 1],nums2 = [1, 10, 10, 10, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10, 10, 1],nums2 = [1, 10, 10, 10, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3],nums2 = [3, 3, 2, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3],nums2 = [3, 3, 2, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 1, 8, 3, 7, 6, 4],nums2 = [4, 9, 2, 6, 1, 8, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 1, 8, 3, 7, 6, 4],nums2 = [4, 9, 2, 6, 1, 8, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 9, 3, 7, 5, 2],nums2 = [6, 8, 4, 2, 9, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 9, 3, 7, 5, 2],nums2 = [6, 8, 4, 2, 9, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 1, 4, 8, 5, 3],nums2 = [2, 7, 6, 3, 10, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 1, 4, 8, 5, 3],nums2 = [2, 7, 6, 3, 10, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 2, 2, 2, 2],nums2 = [2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 2, 2, 2, 2],nums2 = [2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 9, 9, 9, 9, 9],nums2 = [9, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 9, 9, 9, 9, 9],nums2 = [9, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 6, 3, 4, 7],nums2 = [4, 5, 6, 7, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 6, 3, 4, 7],nums2 = [4, 5, 6, 7, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [3, 3, 3, 3, 3]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [5, 5, 5],nums2 = [5, 5, 5]) == 0
    assert candidate(nums1 = [1, 2],nums2 = [2, 1]) == 1
    assert candidate(nums1 = [10, 9, 8],nums2 = [7, 6, 5]) == -1
    assert candidate(nums1 = [3, 3, 3],nums2 = [3, 3, 3]) == 0
    assert candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 0
    assert candidate(nums1 = [3, 1],nums2 = [2, 2]) == -1
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [5, 3, 1],nums2 = [4, 2, 6]) == -1
    assert candidate(nums1 = [2, 3, 4, 5, 9],nums2 = [8, 8, 4, 4, 4]) == 2
    assert candidate(nums1 = [9],nums2 = [9]) == 0
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5]) == 0
    assert candidate(nums1 = [10, 20, 30],nums2 = [15, 25, 20]) == 1
    assert candidate(nums1 = [1],nums2 = [2]) == 0
    assert candidate(nums1 = [1, 3, 5],nums2 = [2, 4, 6]) == 0
    assert candidate(nums1 = [1, 5, 4],nums2 = [2, 5, 3]) == -1
    assert candidate(nums1 = [1, 2, 7],nums2 = [4, 5, 3]) == 1
    assert candidate(nums1 = [1],nums2 = [1]) == 0
    assert candidate(nums1 = [6, 4, 2],nums2 = [5, 3, 1]) == -1
    assert candidate(nums1 = [10, 10, 10],nums2 = [10, 10, 10]) == 0
    assert candidate(nums1 = [10, 20, 30],nums2 = [10, 20, 30]) == 0
    assert candidate(nums1 = [1000000000, 1000000000],nums2 = [1000000000, 1000000000]) == 0
    assert candidate(nums1 = [1, 9, 3, 7, 5],nums2 = [6, 2, 8, 4, 10]) == 2
    assert candidate(nums1 = [9, 5, 1, 4, 7, 3, 6, 8, 2, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [6, 7, 8, 9, 10]) == -1
    assert candidate(nums1 = [1000000000, 999999999, 999999998],nums2 = [1, 2, 3]) == -1
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14],nums2 = [14, 12, 10, 8, 6, 4, 2]) == -1
    assert candidate(nums1 = [1, 1, 2, 2, 3],nums2 = [3, 3, 2, 2, 1]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 20, 30, 40, 50]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 1]) == -1
    assert candidate(nums1 = [1, 10, 3, 9, 5, 6, 4],nums2 = [2, 8, 4, 7, 10, 1, 5]) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [60, 50, 40, 30, 20, 10]) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums1 = [3, 1, 2],nums2 = [3, 1, 2]) == -1
    assert candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [45, 35, 25, 15, 5]) == -1
    assert candidate(nums1 = [1, 2, 2, 1, 2],nums2 = [2, 1, 1, 2, 1]) == 2
    assert candidate(nums1 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],nums2 = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5
    assert candidate(nums1 = [5, 3, 8, 6, 7],nums2 = [4, 6, 2, 9, 1]) == -1
    assert candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [8, 6, 4, 2, 0]) == -1
    assert candidate(nums1 = [1000000000, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 1000000000]) == 1
    assert candidate(nums1 = [8, 6, 4, 3, 1],nums2 = [7, 5, 9, 2, 10]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 9, 8, 7, 6]) == -1
    assert candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [1, 2, 3, 4, 5]) == -1
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 100, 200, 300, 400]) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == 0
    assert candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [2, 4, 6, 8, 10]) == -1
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5]) == 0
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert candidate(nums1 = [5, 3, 8, 6, 2, 7, 4, 1, 9],nums2 = [9, 1, 4, 7, 2, 6, 8, 3, 5]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
    assert candidate(nums1 = [100, 90, 80, 70, 60],nums2 = [60, 70, 80, 90, 100]) == -1
    assert candidate(nums1 = [5, 9, 1, 3, 7],nums2 = [8, 4, 6, 2, 5]) == -1
    assert candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [3, 3, 3, 3, 3]) == 0
    assert candidate(nums1 = [5, 1, 9, 3, 7, 2, 8, 4, 6, 10],nums2 = [1, 5, 3, 9, 2, 8, 4, 7, 10, 6]) == 4
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [5, 5, 5, 5, 5]) == 0
    assert candidate(nums1 = [3, 2, 1, 4, 5, 6],nums2 = [6, 5, 4, 1, 2, 3]) == 3
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums1 = [1, 3, 2, 4, 5],nums2 = [5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [9, 1, 8, 2, 7],nums2 = [3, 6, 5, 4, 10]) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [2, 4, 6, 8, 10]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [10, 9, 8, 7, 6]) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == -1
    assert candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [10, 8, 6, 4, 2]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 1000000000],nums2 = [1000000000, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [2, 2, 2, 2, 2],nums2 = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [3, 3, 2, 2, 1, 1]) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [5, 3, 8, 6, 7],nums2 = [4, 9, 2, 1, 10]) == 1
    assert candidate(nums1 = [7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7]) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 0
    assert candidate(nums1 = [1000000000, 1, 2],nums2 = [1, 2, 1000000000]) == 1
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [6, 6, 6, 6, 6]) == 0
    assert candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1000000000],nums2 = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [49, 42, 35, 28, 21, 14, 7]) == -1
    assert candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums1 = [5, 3, 1, 7, 9],nums2 = [8, 6, 4, 2, 10]) == 0
    assert candidate(nums1 = [7, 7, 7, 7, 1],nums2 = [8, 8, 8, 8, 2]) == -1
    assert candidate(nums1 = [8, 6, 7, 5, 3, 0, 9],nums2 = [1, 4, 2, 8, 6, 7, 4]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [11, 9, 7, 5, 3, 1]) == -1
    assert candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [1, 2, 3, 4, 10]) == 1
    assert candidate(nums1 = [1, 2, 1000000000],nums2 = [1000000000, 1, 2]) == 1
    assert candidate(nums1 = [1000000000, 1, 1, 1, 1],nums2 = [1, 1000000000, 1, 1, 1]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 3, 1, 2, 4]) == 1
    assert candidate(nums1 = [1, 2, 2, 2, 2],nums2 = [2, 1, 1, 1, 1]) == 1
    assert candidate(nums1 = [1, 3, 2, 5, 4],nums2 = [4, 2, 3, 1, 5]) == 1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums1 = [9, 2, 5, 7, 1],nums2 = [1, 8, 3, 4, 6]) == -1
    assert candidate(nums1 = [3, 6, 9, 12, 15],nums2 = [15, 12, 9, 6, 3]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 0
    assert candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [10, 20, 30, 40, 50]) == -1
    assert candidate(nums1 = [5, 7, 3, 9, 2],nums2 = [8, 1, 6, 4, 10]) == -1
    assert candidate(nums1 = [10, 10, 10, 10],nums2 = [10, 10, 10, 10]) == 0
    assert candidate(nums1 = [3, 5, 1, 4, 2, 6, 8, 7, 10, 9],nums2 = [9, 7, 10, 8, 6, 4, 2, 5, 1, 3]) == -1
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == -1
    assert candidate(nums1 = [5, 8, 10, 2, 9],nums2 = [7, 6, 1, 10, 3]) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2]) == 0
    assert candidate(nums1 = [7, 3, 5, 8, 6],nums2 = [2, 4, 1, 9, 5]) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [9, 18, 27, 36, 45]) == 0
    assert candidate(nums1 = [10, 10, 10, 10, 1],nums2 = [1, 10, 10, 10, 10]) == -1
    assert candidate(nums1 = [1, 1, 2, 2, 3],nums2 = [3, 3, 2, 2, 1]) == -1
    assert candidate(nums1 = [5, 1, 8, 3, 7, 6, 4],nums2 = [4, 9, 2, 6, 1, 8, 5]) == -1
    assert candidate(nums1 = [1, 9, 3, 7, 5, 2],nums2 = [6, 8, 4, 2, 9, 1]) == -1
    assert candidate(nums1 = [9, 1, 4, 8, 5, 3],nums2 = [2, 7, 6, 3, 10, 9]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == -1
    assert candidate(nums1 = [2, 2, 2, 2, 2],nums2 = [2, 2, 2, 2, 2]) == 0
    assert candidate(nums1 = [1, 9, 9, 9, 9, 9],nums2 = [9, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2]) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == -1
    assert candidate(nums1 = [5, 6, 3, 4, 7],nums2 = [4, 5, 6, 7, 8]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == -1
    assert candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [3, 3, 3, 3, 3]) == 0


