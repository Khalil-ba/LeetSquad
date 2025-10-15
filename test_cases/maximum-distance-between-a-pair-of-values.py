def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [100],nums2 = [101]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100],nums2 = [101]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [30, 29, 19, 5],nums2 = [25, 25, 25, 25, 25]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [30, 29, 19, 5],nums2 = [25, 25, 25, 25, 25]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [10, 9, 8, 7, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [10, 9, 8, 7, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5],nums2 = [10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5],nums2 = [10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7],nums2 = [7, 7, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7],nums2 = [7, 7, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5],nums2 = [5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5],nums2 = [5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10],nums2 = [5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10],nums2 = [5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90],nums2 = [95, 85]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90],nums2 = [95, 85]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80],nums2 = [100, 90, 80, 70, 60]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80],nums2 = [100, 90, 80, 70, 60]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99999, 99998, 99997],nums2 = [100000, 99999, 99998]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99999, 99998, 99997],nums2 = [100000, 99999, 99998]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [5, 5, 5, 5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [5, 5, 5, 5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 2, 2],nums2 = [10, 10, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 2, 2],nums2 = [10, 10, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 50, 25, 10],nums2 = [100, 100, 100, 100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 50, 25, 10],nums2 = [100, 100, 100, 100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [55, 30, 5, 4, 2],nums2 = [100, 20, 10, 10, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [55, 30, 5, 4, 2],nums2 = [100, 20, 10, 10, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [15, 14, 13, 12, 11]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [15, 14, 13, 12, 11]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000],nums2 = [100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000],nums2 = [100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [100, 80, 60, 40, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [100, 80, 60, 40, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [30, 29, 19, 5],nums2 = [25, 25, 25, 25, 25, 20, 15, 10, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [30, 29, 19, 5],nums2 = [25, 25, 25, 25, 25, 20, 15, 10, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [95, 85, 75, 65, 55],nums2 = [95, 85, 75, 65, 55, 45, 35, 25, 15, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [95, 85, 75, 65, 55],nums2 = [95, 85, 75, 65, 55, 45, 35, 25, 15, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 100000, 100000, 100000, 100000],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 100000, 100000, 100000, 100000],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [99, 89, 79, 69, 59, 49, 39, 29, 19, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [99, 89, 79, 69, 59, 49, 39, 29, 19, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0],nums2 = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0],nums2 = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 25, 10, 1],nums2 = [50, 40, 30, 25, 20, 15, 10, 5, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 25, 10, 1],nums2 = [50, 40, 30, 25, 20, 15, 10, 5, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [90, 80, 70, 60, 50],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [90, 80, 70, 60, 50],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 5, 3, 2],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 5, 3, 2],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [20, 10, 5, 2, 1],nums2 = [50, 40, 30, 20, 10, 5, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [20, 10, 5, 2, 1],nums2 = [50, 40, 30, 20, 10, 5, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 30, 10],nums2 = [60, 50, 40, 30, 20, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 30, 10],nums2 = [60, 50, 40, 30, 20, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [10, 9, 8, 7, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [10, 9, 8, 7, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [90, 70, 50, 30, 10],nums2 = [100, 80, 60, 40, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [90, 70, 50, 30, 10],nums2 = [100, 80, 60, 40, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 50, 25],nums2 = [150, 120, 90, 70, 50, 30, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 50, 25],nums2 = [150, 120, 90, 70, 50, 30, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 900, 800, 700, 600],nums2 = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 900, 800, 700, 600],nums2 = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111, 1],nums2 = [100000, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111, 1],nums2 = [100000, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10, 10, 10, 10],nums2 = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10, 10, 10, 10],nums2 = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],nums2 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],nums2 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 50, 25, 10, 1],nums2 = [200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 25, 20, 15, 10, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 50, 25, 10, 1],nums2 = [200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 25, 20, 15, 10, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 5, 5, 5, 5],nums2 = [20, 15, 15, 10, 10, 10, 5, 5, 5, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 5, 5, 5, 5],nums2 = [20, 15, 15, 10, 10, 10, 5, 5, 5, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 4, 3, 3, 3, 2, 1],nums2 = [9, 8, 7, 6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 4, 3, 3, 3, 2, 1],nums2 = [9, 8, 7, 6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 50, 30, 20, 10],nums2 = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 50, 30, 20, 10],nums2 = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 50, 25, 10, 5],nums2 = [100, 75, 50, 25, 10, 5, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 50, 25, 10, 5],nums2 = [100, 75, 50, 25, 10, 5, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10, 10, 10],nums2 = [20, 20, 20, 20, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10, 10, 10],nums2 = [20, 20, 20, 20, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000],nums2 = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000],nums2 = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70, 60],nums2 = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70, 60],nums2 = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55]) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [100],nums2 = [101]) == 0
    assert candidate(nums1 = [30, 29, 19, 5],nums2 = [25, 25, 25, 25, 25]) == 2
    assert candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [10, 9, 8, 7, 6]) == 0
    assert candidate(nums1 = [5],nums2 = [10]) == 0
    assert candidate(nums1 = [10, 9, 8, 7],nums2 = [7, 7, 7, 7]) == 0
    assert candidate(nums1 = [5],nums2 = [5]) == 0
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 3
    assert candidate(nums1 = [10],nums2 = [5]) == 0
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [100, 90],nums2 = [95, 85]) == 0
    assert candidate(nums1 = [100, 90, 80],nums2 = [100, 90, 80, 70, 60]) == 0
    assert candidate(nums1 = [99999, 99998, 99997],nums2 = [100000, 99999, 99998]) == 1
    assert candidate(nums1 = [1],nums2 = [2]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [5, 5, 5, 5, 5]) == 4
    assert candidate(nums1 = [2, 2, 2],nums2 = [10, 10, 1]) == 1
    assert candidate(nums1 = [100, 50, 25, 10],nums2 = [100, 100, 100, 100]) == 3
    assert candidate(nums1 = [55, 30, 5, 4, 2],nums2 = [100, 20, 10, 10, 5]) == 2
    assert candidate(nums1 = [1],nums2 = [1]) == 0
    assert candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [15, 14, 13, 12, 11]) == 4
    assert candidate(nums1 = [100000],nums2 = [100000]) == 0
    assert candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [100, 80, 60, 40, 20]) == 2
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums1 = [30, 29, 19, 5],nums2 = [25, 25, 25, 25, 25, 20, 15, 10, 5]) == 5
    assert candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 9
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 9
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 9
    assert candidate(nums1 = [95, 85, 75, 65, 55],nums2 = [95, 85, 75, 65, 55, 45, 35, 25, 15, 5]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 9
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [100000, 100000, 100000, 100000, 100000],nums2 = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 9
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
    assert candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 9
    assert candidate(nums1 = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 5
    assert candidate(nums1 = [1],nums2 = [100000]) == 0
    assert candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 5
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [99, 89, 79, 69, 59, 49, 39, 29, 19, 9]) == 0
    assert candidate(nums1 = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0],nums2 = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0]) == 0
    assert candidate(nums1 = [50, 25, 10, 1],nums2 = [50, 40, 30, 25, 20, 15, 10, 5, 1]) == 5
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1]) == 10
    assert candidate(nums1 = [90, 80, 70, 60, 50],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1
    assert candidate(nums1 = [10, 5, 3, 2],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 4
    assert candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 4
    assert candidate(nums1 = [20, 10, 5, 2, 1],nums2 = [50, 40, 30, 20, 10, 5, 2, 1]) == 3
    assert candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 5
    assert candidate(nums1 = [100],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 9
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10
    assert candidate(nums1 = [50, 30, 10],nums2 = [60, 50, 40, 30, 20, 10]) == 3
    assert candidate(nums1 = [10, 9, 8, 7, 6],nums2 = [10, 9, 8, 7, 6]) == 0
    assert candidate(nums1 = [90, 70, 50, 30, 10],nums2 = [100, 80, 60, 40, 20]) == 0
    assert candidate(nums1 = [100, 50, 25],nums2 = [150, 120, 90, 70, 50, 30, 10]) == 3
    assert candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 9
    assert candidate(nums1 = [1000, 900, 800, 700, 600],nums2 = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500]) == 4
    assert candidate(nums1 = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111, 1],nums2 = [100000, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111]) == 1
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [10, 10, 10, 10, 10, 10],nums2 = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 14
    assert candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(nums1 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],nums2 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 9
    assert candidate(nums1 = [100, 50, 25, 10, 1],nums2 = [200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 25, 20, 15, 10, 5]) == 10
    assert candidate(nums1 = [10, 5, 5, 5, 5],nums2 = [20, 15, 15, 10, 10, 10, 5, 5, 5, 5]) == 8
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(nums1 = [5, 4, 4, 3, 3, 3, 2, 1],nums2 = [9, 8, 7, 6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 9
    assert candidate(nums1 = [100, 50, 30, 20, 10],nums2 = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 10
    assert candidate(nums1 = [100, 50, 25, 10, 5],nums2 = [100, 75, 50, 25, 10, 5, 2]) == 1
    assert candidate(nums1 = [10, 10, 10, 10, 10],nums2 = [20, 20, 20, 20, 20]) == 4
    assert candidate(nums1 = [100000],nums2 = [1]) == 0
    assert candidate(nums1 = [100, 90, 80, 70, 60],nums2 = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55]) == 4


