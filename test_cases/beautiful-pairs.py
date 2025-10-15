def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 1, 2, 4],nums2 = [4, 2, 3, 1, 5]) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 1, 2, 4],nums2 = [4, 2, 3, 1, 5]) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 2, 4],nums2 = [2, 3, 1, 2, 3]) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 2, 4],nums2 = [2, 3, 1, 2, 3]) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 3, 2, 5],nums2 = [1, 4, 2, 3, 5, 1]) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 3, 2, 5],nums2 = [1, 4, 2, 3, 5, 1]) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4],nums2 = [4, 3, 2, 1, 0]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4],nums2 = [4, 3, 2, 1, 0]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 8, 6, 2],nums2 = [4, 9, 1, 7, 3]) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 8, 6, 2],nums2 = [4, 9, 1, 7, 3]) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 8, 9, 1],nums2 = [2, 5, 3, 7, 4]) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 8, 9, 1],nums2 = [2, 5, 3, 7, 4]) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 7, 7, 7, 7],nums2 = [7, 7, 7, 7, 7]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 7, 7, 7, 7],nums2 = [7, 7, 7, 7, 7]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],nums2 = [6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],nums2 = [6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 150, 250, 300, 350],nums2 = [350, 300, 250, 150, 200, 100]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 150, 250, 300, 350],nums2 = [350, 300, 250, 150, 200, 100]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],nums2 = [1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],nums2 = [1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [15, 13, 11, 9, 7, 5, 3, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [15, 13, 11, 9, 7, 5, 3, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 1, 6, 2, 7, 3, 8, 4, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 1, 6, 2, 7, 3, 8, 4, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 0, 1, 0, 1],nums2 = [1, 0, 1, 0, 1, 0]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 0, 1, 0, 1],nums2 = [1, 0, 1, 0, 1, 0]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 99999, 99998, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 100000, 99999, 99998, 1, 2]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 99999, 99998, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 100000, 99999, 99998, 1, 2]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 5, 7, 3, 8, 6],nums2 = [6, 8, 4, 5, 7, 9]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 5, 7, 3, 8, 6],nums2 = [6, 8, 4, 5, 7, 9]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [1, 2, 1, 2, 1, 2]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [1, 2, 1, 2, 1, 2]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],nums2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],nums2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 5, 3, 8, 2, 7, 6, 4, 9, 1],nums2 = [2, 9, 5, 4, 8, 3, 7, 6, 1, 10]) == [0, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 5, 3, 8, 2, 7, 6, 4, 9, 1],nums2 = [2, 9, 5, 4, 8, 3, 7, 6, 1, 10]) == [0, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [3, 3, 3, 3, 3]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [3, 3, 3, 3, 3]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 3],nums2 = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 3],nums2 = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 0, 50000, 75000, 25000],nums2 = [0, 100000, 25000, 50000, 75000]) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 0, 50000, 75000, 25000],nums2 = [0, 100000, 25000, 50000, 75000]) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],nums2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],nums2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 5, 3, 7, 8, 1, 9, 2],nums2 = [4, 10, 1, 8, 7, 3, 5, 2]) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 5, 3, 7, 8, 1, 9, 2],nums2 = [4, 10, 1, 8, 7, 3, 5, 2]) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 5, 8, 3, 7, 6, 9],nums2 = [3, 8, 4, 9, 5, 7, 2]) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 5, 8, 3, 7, 6, 9],nums2 = [3, 8, 4, 9, 5, 7, 2]) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 100000, 50000, 25000, 75000, 10000],nums2 = [10000, 0, 25000, 75000, 50000, 100000]) == [3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 100000, 50000, 25000, 75000, 10000],nums2 = [10000, 0, 25000, 75000, 50000, 100000]) == [3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989],nums2 = [99989, 99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989],nums2 = [99989, 99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],nums2 = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],nums2 = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 15, 20, 25, 30, 35, 40],nums2 = [40, 35, 30, 25, 20, 15, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 15, 20, 25, 30, 35, 40],nums2 = [40, 35, 30, 25, 20, 15, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [20, 10, 30, 5, 15, 25, 35],nums2 = [35, 25, 5, 15, 30, 10, 20]) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [20, 10, 30, 5, 15, 25, 35],nums2 = [35, 25, 5, 15, 30, 10, 20]) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [2, 4, 6, 8, 10, 12, 14]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [2, 4, 6, 8, 10, 12, 14]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],nums2 = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],nums2 = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 5, 1, 7, 3, 8, 6],nums2 = [4, 9, 6, 1, 7, 3, 8]) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 5, 1, 7, 3, 8, 6],nums2 = [4, 9, 6, 1, 7, 3, 8]) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == [0, 1]
    assert candidate(nums1 = [5, 3, 1, 2, 4],nums2 = [4, 2, 3, 1, 5]) == [0, 4]
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5]) == [0, 1]
    assert candidate(nums1 = [1, 2, 3, 2, 4],nums2 = [2, 3, 1, 2, 3]) == [0, 3]
    assert candidate(nums1 = [1, 2, 4, 3, 2, 5],nums2 = [1, 4, 2, 3, 5, 1]) == [1, 4]
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0]) == [0, 1]
    assert candidate(nums1 = [0, 1, 2, 3, 4],nums2 = [4, 3, 2, 1, 0]) == [0, 1]
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == [0, 1]
    assert candidate(nums1 = [5, 3, 8, 6, 2],nums2 = [4, 9, 1, 7, 3]) == [0, 3]
    assert candidate(nums1 = [5, 3, 8, 9, 1],nums2 = [2, 5, 3, 7, 4]) == [1, 4]
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == [0, 1]
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == [0, 1]
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5]) == [0, 1]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [0, 1]
    assert candidate(nums1 = [7, 7, 7, 7, 7],nums2 = [7, 7, 7, 7, 7]) == [0, 1]
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == [0, 1]
    assert candidate(nums1 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],nums2 = [6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == [0, 2]
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [0, 1]
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 1]
    assert candidate(nums1 = [100, 200, 150, 250, 300, 350],nums2 = [350, 300, 250, 150, 200, 100]) == [1, 2]
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [0, 1]
    assert candidate(nums1 = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],nums2 = [1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]) == [4, 5]
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [0, 1]
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [15, 13, 11, 9, 7, 5, 3, 1]) == [0, 1]
    assert candidate(nums1 = [5, 1, 6, 2, 7, 3, 8, 4, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, 9]
    assert candidate(nums1 = [0, 1, 0, 1, 0, 1],nums2 = [1, 0, 1, 0, 1, 0]) == [0, 2]
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
    assert candidate(nums1 = [100000, 99999, 99998, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 100000, 99999, 99998, 1, 2]) == [0, 1]
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 1]
    assert candidate(nums1 = [10, 5, 7, 3, 8, 6],nums2 = [6, 8, 4, 5, 7, 9]) == [1, 5]
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [1, 2, 1, 2, 1, 2]) == [0, 1]
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 1]
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
    assert candidate(nums1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],nums2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == [0, 1]
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1]
    assert candidate(nums1 = [10, 5, 3, 8, 2, 7, 6, 4, 9, 1],nums2 = [2, 9, 5, 4, 8, 3, 7, 6, 1, 10]) == [0, 8]
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [0, 1]
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
    assert candidate(nums1 = [3, 3, 3, 3, 3],nums2 = [3, 3, 3, 3, 3]) == [0, 1]
    assert candidate(nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 3],nums2 = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [0, 1]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 1]
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1]
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [0, 1]
    assert candidate(nums1 = [100000, 0, 50000, 75000, 25000],nums2 = [0, 100000, 25000, 50000, 75000]) == [1, 4]
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1]
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],nums2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [0, 1]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == [0, 1]
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [0, 1]
    assert candidate(nums1 = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
    assert candidate(nums1 = [10, 5, 3, 7, 8, 1, 9, 2],nums2 = [4, 10, 1, 8, 7, 3, 5, 2]) == [0, 6]
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0]) == [0, 1]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1]
    assert candidate(nums1 = [10, 5, 8, 3, 7, 6, 9],nums2 = [3, 8, 4, 9, 5, 7, 2]) == [0, 6]
    assert candidate(nums1 = [0, 100000, 50000, 25000, 75000, 10000],nums2 = [10000, 0, 25000, 75000, 50000, 100000]) == [3, 5]
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 1]
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
    assert candidate(nums1 = [99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989],nums2 = [99989, 99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998]) == [0, 1]
    assert candidate(nums1 = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == [8, 9]
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
    assert candidate(nums1 = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],nums2 = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == [0, 10]
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1]
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [0, 1]
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1]
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
    assert candidate(nums1 = [10, 15, 20, 25, 30, 35, 40],nums2 = [40, 35, 30, 25, 20, 15, 10]) == [0, 1]
    assert candidate(nums1 = [20, 10, 30, 5, 15, 25, 35],nums2 = [35, 25, 5, 15, 30, 10, 20]) == [0, 4]
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == [0, 1]
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == [0, 1]
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 1]
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [0, 1]
    assert candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1]
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [2, 4, 6, 8, 10, 12, 14]) == [0, 1]
    assert candidate(nums1 = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],nums2 = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [0, 2]
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1]
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == [0, 1]
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1]
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 1]
    assert candidate(nums1 = [9, 5, 1, 7, 3, 8, 6],nums2 = [4, 9, 6, 1, 7, 3, 8]) == [0, 5]
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1]
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1]


