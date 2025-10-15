def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 299997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 299997: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 7, 5],nums2 = [2, 3, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 7, 5],nums2 = [2, 3, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [1, 1, 1, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [1, 1, 1, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 299997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 299997: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 4, 4, 2, 7],nums2 = [9, 3, 5, 1, 7, 4]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 4, 4, 2, 7],nums2 = [9, 3, 5, 1, 7, 4]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [2, 4, 6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [2, 4, 6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [6, 5, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [6, 5, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 1, 100000],nums2 = [1, 100000, 1]) == 199998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 1, 100000],nums2 = [1, 100000, 1]) == 199998: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000],nums2 = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 899991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000],nums2 = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 899991: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 99999, 99998, 99997],nums2 = [1, 2, 3, 4]) == 399981
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 99999, 99998, 99997],nums2 = [1, 2, 3, 4]) == 399981: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 999881
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 999881: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 999945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 999945: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 945: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 99999, 99998, 99997, 99996],nums2 = [1, 2, 3, 4, 5]) == 499971
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 99999, 99998, 99997, 99996],nums2 = [1, 2, 3, 4, 5]) == 499971: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000, 100000],nums2 = [1, 100000, 100000, 1]) == 199998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000, 100000],nums2 = [1, 100000, 100000, 1]) == 199998: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [1, 2, 3, 4, 5]) == 249985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [1, 2, 3, 4, 5]) == 249985: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996],nums2 = [100000, 1, 99999, 2, 99998, 3, 99997, 4, 99996, 5]) == 899951
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996],nums2 = [100000, 1, 99999, 2, 99998, 3, 99997, 4, 99996, 5]) == 899951: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 1, 50000, 75000],nums2 = [50000, 99999, 1, 100000]) == 125000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 1, 50000, 75000],nums2 = [50000, 99999, 1, 100000]) == 125000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50, 40, 30, 20, 10, 1]) == 409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50, 40, 30, 20, 10, 1]) == 409: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996],nums2 = [100000, 1, 99999, 2, 99998, 3, 99997, 4, 99996, 5]) == 899951
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996],nums2 = [100000, 1, 99999, 2, 99998, 3, 99997, 4, 99996, 5]) == 899951: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 204
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 204: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [1, 1, 1, 1, 1]) == 249995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [1, 1, 1, 1, 1]) == 249995: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 3, 6, 8, 11, 13, 16, 18, 21, 23]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 3, 6, 8, 11, 13, 16, 18, 21, 23]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]) == 999980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]) == 999980: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 499936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 499936: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000],nums2 = [90000, 90000, 90000]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000],nums2 = [90000, 90000, 90000]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 181: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 82: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000, 100000],nums2 = [100000, 10000, 1000, 100, 10, 1]) == 121779
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000, 100000],nums2 = [100000, 10000, 1000, 100, 10, 1]) == 121779: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 486
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 486: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 410: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 100, 100, 100, 100],nums2 = [10, 90, 110, 10, 90]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 100, 100, 100, 100],nums2 = [10, 90, 110, 10, 90]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 999990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 999990: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000, 100000],nums2 = [1, 1, 1, 1]) == 399996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000, 100000],nums2 = [1, 1, 1, 1]) == 399996: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000],nums2 = [2, 11, 101, 1001, 10001]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000],nums2 = [2, 11, 101, 1001, 10001]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 405: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 549990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 549990: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 999891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 999891: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 200000, 300000, 400000, 500000],nums2 = [1, 2, 3, 4, 5]) == 1099985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 200000, 300000, 400000, 500000],nums2 = [1, 2, 3, 4, 5]) == 1099985: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99999, 99998, 99997, 99996, 99995],nums2 = [1, 100, 200, 300, 400]) == 498980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99999, 99998, 99997, 99996, 99995],nums2 = [1, 100, 200, 300, 400]) == 498980: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50000, 40000, 30000, 20000, 10000],nums2 = [1, 2, 3, 4, 5]) == 109985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50000, 40000, 30000, 20000, 10000],nums2 = [1, 2, 3, 4, 5]) == 109985: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 171: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 90000, 80000, 70000, 60000],nums2 = [50000, 40000, 30000, 20000, 10000]) == 210000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 90000, 80000, 70000, 60000],nums2 = [50000, 40000, 30000, 20000, 10000]) == 210000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 99943
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 99943: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [101, 201, 301, 401, 501]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [101, 201, 301, 401, 501]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 25, 45, 65, 85],nums2 = [10, 30, 50, 70, 90]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 25, 45, 65, 85],nums2 = [10, 30, 50, 70, 90]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 82: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 891: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000, 100000, 100000],nums2 = [1, 1, 1, 1, 1]) == 499995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000, 100000, 100000],nums2 = [1, 1, 1, 1, 1]) == 499995: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 540: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [15, 25, 35, 45, 55]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [15, 25, 35, 45, 55]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 999882
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 999882: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 50000, 25000, 12500, 6250],nums2 = [99999, 49999, 24999, 12499, 6249]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 50000, 25000, 12500, 6250],nums2 = [99999, 49999, 24999, 12499, 6249]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 100000, 200000, 300000],nums2 = [50000, 250000, 150000, 350000]) == 199999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 100000, 200000, 300000],nums2 = [50000, 250000, 150000, 350000]) == 199999: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 55: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 299997
    assert candidate(nums1 = [1, 7, 5],nums2 = [2, 3, 5]) == 3
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [1, 1, 1, 1]) == 16
    assert candidate(nums1 = [100000, 100000, 100000],nums2 = [1, 1, 1]) == 299997
    assert candidate(nums1 = [1, 10, 4, 4, 2, 7],nums2 = [9, 3, 5, 1, 7, 4]) == 20
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [2, 4, 6, 8, 10]) == 0
    assert candidate(nums1 = [1, 2, 3],nums2 = [6, 5, 4]) == 7
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 8
    assert candidate(nums1 = [100000, 1, 100000],nums2 = [1, 100000, 1]) == 199998
    assert candidate(nums1 = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000],nums2 = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 899991
    assert candidate(nums1 = [100000, 99999, 99998, 99997],nums2 = [1, 2, 3, 4]) == 399981
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]) == 15
    assert candidate(nums1 = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 999881
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 999945
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 90
    assert candidate(nums1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 945
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 5
    assert candidate(nums1 = [100000, 99999, 99998, 99997, 99996],nums2 = [1, 2, 3, 4, 5]) == 499971
    assert candidate(nums1 = [100000, 100000, 100000, 100000],nums2 = [1, 100000, 100000, 1]) == 199998
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 41
    assert candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [1, 2, 3, 4, 5]) == 249985
    assert candidate(nums1 = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996],nums2 = [100000, 1, 99999, 2, 99998, 3, 99997, 4, 99996, 5]) == 899951
    assert candidate(nums1 = [100000, 1, 50000, 75000],nums2 = [50000, 99999, 1, 100000]) == 125000
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
    assert candidate(nums1 = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50, 40, 30, 20, 10, 1]) == 409
    assert candidate(nums1 = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996],nums2 = [100000, 1, 99999, 2, 99998, 3, 99997, 4, 99996, 5]) == 899951
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [45, 40, 35, 30, 25, 20, 15, 10, 5, 1]) == 204
    assert candidate(nums1 = [50000, 50000, 50000, 50000, 50000],nums2 = [1, 1, 1, 1, 1]) == 249995
    assert candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 10
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 3, 6, 8, 11, 13, 16, 18, 21, 23]) == 130
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 98
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]) == 999980
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 499936
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5]) == 95
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 36
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 16
    assert candidate(nums1 = [100000, 100000, 100000],nums2 = [90000, 90000, 90000]) == 30000
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 210
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 500
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 41
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 50
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 41
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 181
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 82
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 25
    assert candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == 8
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000],nums2 = [100000, 10000, 1000, 100, 10, 1]) == 121779
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 486
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 410
    assert candidate(nums1 = [100, 100, 100, 100, 100],nums2 = [10, 90, 110, 10, 90]) == 210
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 999990
    assert candidate(nums1 = [100000, 100000, 100000, 100000],nums2 = [1, 1, 1, 1]) == 399996
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 50
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 67
    assert candidate(nums1 = [1, 10, 100, 1000, 10000],nums2 = [2, 11, 101, 1001, 10001]) == 5
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 405
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 5
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 549990
    assert candidate(nums1 = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 999891
    assert candidate(nums1 = [100000, 200000, 300000, 400000, 500000],nums2 = [1, 2, 3, 4, 5]) == 1099985
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 20
    assert candidate(nums1 = [99999, 99998, 99997, 99996, 99995],nums2 = [1, 100, 200, 300, 400]) == 498980
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 9
    assert candidate(nums1 = [50000, 40000, 30000, 20000, 10000],nums2 = [1, 2, 3, 4, 5]) == 109985
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 171
    assert candidate(nums1 = [100000, 90000, 80000, 70000, 60000],nums2 = [50000, 40000, 30000, 20000, 10000]) == 210000
    assert candidate(nums1 = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 99943
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [101, 201, 301, 401, 501]) == 5
    assert candidate(nums1 = [5, 25, 45, 65, 85],nums2 = [10, 30, 50, 70, 90]) == 25
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 82
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 891
    assert candidate(nums1 = [100000, 100000, 100000, 100000, 100000],nums2 = [1, 1, 1, 1, 1]) == 499995
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 540
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [15, 25, 35, 45, 55]) == 25
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 20
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 999882
    assert candidate(nums1 = [100000, 50000, 25000, 12500, 6250],nums2 = [99999, 49999, 24999, 12499, 6249]) == 5
    assert candidate(nums1 = [1, 100000, 200000, 300000],nums2 = [50000, 250000, 150000, 350000]) == 199999
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 55


