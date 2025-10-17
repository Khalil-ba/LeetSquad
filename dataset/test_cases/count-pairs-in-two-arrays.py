def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 1, 1, 1],nums2 = [1, 100000, 100000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 1, 1, 1],nums2 = [1, 100000, 100000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 6, 2],nums2 = [1, 4, 1, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 6, 2],nums2 = [1, 4, 1, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 1, 2, 1],nums2 = [1, 2, 1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 1, 2, 1],nums2 = [1, 2, 1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [4, 4, 4, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [4, 4, 4, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [1, 10000, 20000, 30000, 40000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [1, 10000, 20000, 30000, 40000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [90000, 50000, 30000, 10000],nums2 = [10000, 20000, 30000, 40000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [90000, 50000, 30000, 10000],nums2 = [10000, 20000, 30000, 40000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],nums2 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],nums2 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 90000, 80000, 70000, 60000],nums2 = [1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 90000, 80000, 70000, 60000],nums2 = [1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 1000],nums2 = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 1000],nums2 = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [49999, 49999, 49999, 49999, 49999]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [49999, 49999, 49999, 49999, 49999]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50000, 40000, 30000, 20000, 10000],nums2 = [10000, 20000, 30000, 40000, 50000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50000, 40000, 30000, 20000, 10000],nums2 = [10000, 20000, 30000, 40000, 50000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50000, 40000, 30000, 20000, 10000, 10000, 20000, 30000, 40000, 50000],nums2 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50000, 40000, 30000, 20000, 10000, 10000, 20000, 30000, 40000, 50000],nums2 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99999, 50000, 10000, 5000, 1000],nums2 = [1, 10, 100, 1000, 10000]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99999, 50000, 10000, 5000, 1000],nums2 = [1, 10, 100, 1000, 10000]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],nums2 = [29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],nums2 = [29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000, 100000, 100000],nums2 = [99999, 99999, 99999, 99999, 99999]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000, 100000, 100000],nums2 = [99999, 99999, 99999, 99999, 99999]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],nums2 = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],nums2 = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 99999, 99998, 99997, 99996],nums2 = [1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 99999, 99998, 99997, 99996],nums2 = [1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7],nums2 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7],nums2 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 10000, 1000, 100, 10],nums2 = [100000, 10000, 1000, 100, 10, 1, 10, 100, 1000, 10000]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 10000, 1000, 100, 10],nums2 = [100000, 10000, 1000, 100, 10, 1, 10, 100, 1000, 10000]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99999, 1, 99999, 2, 99999],nums2 = [1, 99999, 1, 99999, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99999, 1, 99999, 2, 99999],nums2 = [1, 99999, 1, 99999, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45, 55],nums2 = [45, 35, 25, 15, 5, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45, 55],nums2 = [45, 35, 25, 15, 5, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100000],nums2 = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100000],nums2 = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],nums2 = [1, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],nums2 = [1, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1],nums2 = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1],nums2 = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 1, 100000, 1, 100000],nums2 = [1, 100000, 1, 100000, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 1, 100000, 1, 100000],nums2 = [1, 100000, 1, 100000, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99999, 1, 100000, 2, 3],nums2 = [1, 100000, 99999, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99999, 1, 100000, 2, 3],nums2 = [1, 100000, 99999, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],nums2 = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],nums2 = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 1]) == 25: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 3
    assert candidate(nums1 = [100000, 1, 1, 1],nums2 = [1, 100000, 100000, 100000]) == 0
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [1, 1, 1, 1]) == 6
    assert candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 3
    assert candidate(nums1 = [1, 10, 6, 2],nums2 = [1, 4, 1, 5]) == 5
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 4
    assert candidate(nums1 = [2, 1, 2, 1],nums2 = [1, 2, 1, 2]) == 1
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [4, 4, 4, 4]) == 6
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5]) == 0
    assert candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [1, 10000, 20000, 30000, 40000]) == 10
    assert candidate(nums1 = [90000, 50000, 30000, 10000],nums2 = [10000, 20000, 30000, 40000]) == 4
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
    assert candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 10
    assert candidate(nums1 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],nums2 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 20
    assert candidate(nums1 = [100000, 90000, 80000, 70000, 60000],nums2 = [1, 2, 3, 4, 5]) == 10
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 20
    assert candidate(nums1 = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 1000],nums2 = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]) == 20
    assert candidate(nums1 = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [49999, 49999, 49999, 49999, 49999]) == 10
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 49
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 105
    assert candidate(nums1 = [50000, 40000, 30000, 20000, 10000],nums2 = [10000, 20000, 30000, 40000, 50000]) == 4
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 105
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(nums1 = [50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50]) == 4
    assert candidate(nums1 = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(nums1 = [50000, 40000, 30000, 20000, 10000, 10000, 20000, 30000, 40000, 50000],nums2 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 45
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49
    assert candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 45
    assert candidate(nums1 = [99999, 50000, 10000, 5000, 1000],nums2 = [1, 10, 100, 1000, 10000]) == 9
    assert candidate(nums1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],nums2 = [29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == 20
    assert candidate(nums1 = [100000, 100000, 100000, 100000, 100000],nums2 = [99999, 99999, 99999, 99999, 99999]) == 10
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],nums2 = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 90
    assert candidate(nums1 = [100000, 99999, 99998, 99997, 99996],nums2 = [1, 2, 3, 4, 5]) == 10
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0
    assert candidate(nums1 = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7],nums2 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]) == 45
    assert candidate(nums1 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 20
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 10000, 1000, 100, 10],nums2 = [100000, 10000, 1000, 100, 10, 1, 10, 100, 1000, 10000]) == 18
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [99999, 1, 99999, 2, 99999],nums2 = [1, 99999, 1, 99999, 1]) == 6
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(nums1 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(nums1 = [5, 15, 25, 35, 45, 55],nums2 = [45, 35, 25, 15, 5, 1]) == 9
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 4
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 20
    assert candidate(nums1 = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]) == 9
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 45
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100000],nums2 = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(nums1 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],nums2 = [1, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 45
    assert candidate(nums1 = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1],nums2 = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 10
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums1 = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 190
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 4
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
    assert candidate(nums1 = [100000, 1, 100000, 1, 100000],nums2 = [1, 100000, 1, 100000, 1]) == 3
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 20
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums1 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45
    assert candidate(nums1 = [99999, 1, 100000, 2, 3],nums2 = [1, 100000, 99999, 1, 1]) == 6
    assert candidate(nums1 = [20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 45
    assert candidate(nums1 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],nums2 = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 1]) == 25


