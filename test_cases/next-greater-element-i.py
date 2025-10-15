def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 5, 6],nums2 = [5, 6, 2, 3, 8, 9]) == [3, 8, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 5, 6],nums2 = [5, 6, 2, 3, 8, 9]) == [3, 8, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2],nums2 = [2, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2],nums2 = [2, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == [-1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == [-1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5],nums2 = [5]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5],nums2 = [5]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 6, 4, 8],nums2 = [4, 5, 1, 8, 6, 7, 9]) == [8, 7, 5, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 6, 4, 8],nums2 = [4, 5, 1, 8, 6, 7, 9]) == [8, 7, 5, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 2, 6],nums2 = [4, 1, 5, 2, 3, 6]) == [6, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 2, 6],nums2 = [4, 1, 5, 2, 3, 6]) == [6, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4],nums2 = [1, 2, 3, 4]) == [3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4],nums2 = [1, 2, 3, 4]) == [3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 1, 2],nums2 = [1, 3, 4, 2]) == [-1, 3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 1, 2],nums2 = [1, 3, 4, 2]) == [-1, 3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 5, 6],nums2 = [3, 4, 2, 1, 5, 7, 8, 9, 10, 6]) == [-1, 7, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 5, 6],nums2 = [3, 4, 2, 1, 5, 7, 8, 9, 10, 6]) == [-1, 7, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2],nums2 = [1, 2]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2],nums2 = [1, 2]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7],nums2 = [1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7],nums2 = [1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 8],nums2 = [2, 3, 4, 5, 7, 8, 10]) == [4, 7, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 8],nums2 = [2, 3, 4, 5, 7, 8, 10]) == [4, 7, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [3, 2, 1]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [3, 2, 1]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7],nums2 = [8, 9, 7, 6, 5, 4, 3, 2, 1]) == [-1, 9, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7],nums2 = [8, 9, 7, 6, 5, 4, 3, 2, 1]) == [-1, 9, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 8],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [4, 6, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 8],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [4, 6, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 10, 7],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, -1, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 10, 7],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, -1, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7],nums2 = [7, 5, 3, 1, 9, 11, 13]) == [9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7],nums2 = [7, 5, 3, 1, 9, 11, 13]) == [9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3],nums2 = [2, 1, 3, 4]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3],nums2 = [2, 1, 3, 4]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 8, 6],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [11, 9, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 8, 6],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [11, 9, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 7, 3],nums2 = [3, 6, 9, 12, 15, 7]) == [12, -1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 7, 3],nums2 = [3, 6, 9, 12, 15, 7]) == [12, -1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8],nums2 = [8, 9, 10, 5, 7]) == [-1, 10, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8],nums2 = [8, 9, 10, 5, 7]) == [-1, 10, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70],nums2 = [70, 80, 90, 100, 110, 120, 130, 140, 150]) == [110, 100, 90, 80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70],nums2 = [70, 80, 90, 100, 110, 120, 130, 140, 150]) == [110, 100, 90, 80]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == [3, 5, 7, 9, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == [3, 5, 7, 9, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [33, 22, 11],nums2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == [44, 33, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [33, 22, 11],nums2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == [44, 33, 22]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 99, 98, 97],nums2 = [98, 100, 97, 99, 96, 95, 94, 93, 92]) == [-1, -1, 100, 99]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 99, 98, 97],nums2 = [98, 100, 97, 99, 96, 95, 94, 93, 92]) == [-1, -1, 100, 99]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 2, 1],nums2 = [1, 2, 3, 5, 4]) == [5, -1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 2, 1],nums2 = [1, 2, 3, 5, 4]) == [5, -1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 2, 4, 9],nums2 = [8, 5, 3, 9, 2, 4, 7, 6]) == [9, 9, 4, 7, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 2, 4, 9],nums2 = [8, 5, 3, 9, 2, 4, 7, 6]) == [9, 9, 4, 7, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [8, 9, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [8, 9, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 8, 9],nums2 = [10, 11, 7, 8, 6, 5, 3, 4, 9, 2, 1]) == [4, 9, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 8, 9],nums2 = [10, 11, 7, 8, 6, 5, 3, 4, 9, 2, 1]) == [4, 9, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 7, 3, 9, 1],nums2 = [11, 14, 8, 15, 13, 2, 11, 5, 12, 7, 9, 3, 6, 10, 4, 1]) == [12, 9, 6, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 7, 3, 9, 1],nums2 = [11, 14, 8, 15, 13, 2, 11, 5, 12, 7, 9, 3, 6, 10, 4, 1]) == [12, 9, 6, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 2, 8, 9],nums2 = [6, 5, 4, 3, 2, 1, 10, 11, 8, 9, 7]) == [10, 10, 9, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 2, 8, 9],nums2 = [6, 5, 4, 3, 2, 1, 10, 11, 8, 9, 7]) == [10, 10, 9, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 13, 15, 17],nums2 = [17, 15, 13, 11, 19, 21, 23]) == [19, 19, 19, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 13, 15, 17],nums2 = [17, 15, 13, 11, 19, 21, 23]) == [19, 19, 19, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [5, 6, 7, 8, 9]) == [-1, 9, 8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [5, 6, 7, 8, 9]) == [-1, 9, 8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 6, 7]) == [6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 6, 7]) == [6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7],nums2 = [7, 5, 3, 1, 2, 4, 6, 8, 10]) == [2, 4, 6, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7],nums2 = [7, 5, 3, 1, 2, 4, 6, 8, 10]) == [2, 4, 6, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [4, 7, 10, 13, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [4, 7, 10, 13, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 25, 35],nums2 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == [20, 30, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 25, 35],nums2 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == [20, 30, 40]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70],nums2 = [70, 80, 90, 100, 110]) == [110, 100, 90, 80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70],nums2 = [70, 80, 90, 100, 110]) == [110, 100, 90, 80]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 10, 20, 30, 50, 60, 70]) == [20, 30, 50, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 10, 20, 30, 50, 60, 70]) == [20, 30, 50, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6]) == [-1, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6]) == [-1, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 2, 1],nums2 = [5, 3, 2, 1, 6, 4]) == [6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 2, 1],nums2 = [5, 3, 2, 1, 6, 4]) == [6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [23, 56, 78, 90],nums2 = [90, 78, 56, 23, 12, 34, 45, 67, 89, 100]) == [34, 67, 89, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [23, 56, 78, 90],nums2 = [90, 78, 56, 23, 12, 34, 45, 67, 89, 100]) == [34, 67, 89, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [42, 55, 66, 77],nums2 = [42, 77, 55, 88, 66, 99, 100]) == [77, 88, 99, 88]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [42, 55, 66, 77],nums2 = [42, 77, 55, 88, 66, 99, 100]) == [77, 88, 99, 88]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 6, 4, 2],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 7, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 6, 4, 2],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 7, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80],nums2 = [70, 80, 90, 100, 60, 50, 40, 30, 20, 10]) == [-1, 100, 90]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80],nums2 = [70, 80, 90, 100, 60, 50, 40, 30, 20, 10]) == [-1, 100, 90]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [10, 20, 30, 25, 15, 5, 40, 35, 33, 31]) == [20, 30, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [10, 20, 30, 25, 15, 5, 40, 35, 33, 31]) == [20, 30, 40]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [7, 8, 9, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [7, 8, 9, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 3, 2],nums2 = [5, 7, 3, 2, 1, 8]) == [8, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 3, 2],nums2 = [5, 7, 3, 2, 1, 8]) == [8, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 14, 13, 11, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [13, 15, 14, 12, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 14, 13, 11, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [13, 15, 14, 12, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 10, 4, 3],nums2 = [1, 11, 10, 4, 8, 3, 7]) == [-1, -1, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 10, 4, 3],nums2 = [1, 11, 10, 4, 8, 3, 7]) == [-1, -1, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 6, 5, 4, 3, 2, 1],nums2 = [2, 1, 3, 6, 5, 4, 7]) == [-1, 7, 7, 7, 6, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 6, 5, 4, 3, 2, 1],nums2 = [2, 1, 3, 6, 5, 4, 7]) == [-1, 7, 7, 7, 6, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 6, 4, 5, 3],nums2 = [3, 1, 2, 5, 4, 7, 6]) == [5, -1, 7, 7, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 6, 4, 5, 3],nums2 = [3, 1, 2, 5, 4, 7, 6]) == [5, -1, 7, 7, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 9, 10, 11],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 9, 10, 11],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [4, 7, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [4, 7, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 7, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [4, 6, 8, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 7, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [4, 6, 8, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 5, 3, 1],nums2 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [8, 6, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 5, 3, 1],nums2 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [8, 6, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70],nums2 = [70, 80, 90, 100, 110, 120, 130]) == [110, 100, 90, 80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70],nums2 = [70, 80, 90, 100, 110, 120, 130]) == [110, 100, 90, 80]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 2, 4, 9],nums2 = [9, 1, 2, 5, 3, 7, 8, 4, 6]) == [7, 7, 5, 6, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 2, 4, 9],nums2 = [9, 1, 2, 5, 3, 7, 8, 4, 6]) == [7, 7, 5, 6, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [42, 23, 14, 5, 1],nums2 = [1, 5, 14, 23, 42, 3, 7, 11, 13, 19, 21, 27]) == [-1, 42, 23, 14, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [42, 23, 14, 5, 1],nums2 = [1, 5, 14, 23, 42, 3, 7, 11, 13, 19, 21, 27]) == [-1, 42, 23, 14, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17],nums2 = [15, 13, 11, 9, 7, 5, 3, 1, 17, 19]) == [17, 17, 17, 17, 17, 17, 17, 17, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17],nums2 = [15, 13, 11, 9, 7, 5, 3, 1, 17, 19]) == [17, 17, 17, 17, 17, 17, 17, 17, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20],nums2 = [20, 15, 10, 5, 25, 30, 35, 40]) == [25, 25, 25, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20],nums2 = [20, 15, 10, 5, 25, 30, 35, 40]) == [25, 25, 25, 25]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 3, 9, 1],nums2 = [1, 3, 5, 7, 9]) == [9, 5, -1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 3, 9, 1],nums2 = [1, 3, 5, 7, 9]) == [9, 5, -1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 10, 5],nums2 = [1, 2, 3, 4, 5, 10, 15, 20, 25]) == [20, 15, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 10, 5],nums2 = [1, 2, 3, 4, 5, 10, 15, 20, 25]) == [20, 15, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 11, 12, 13],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 11, 12, 13],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7]) == [-1, 7, 6, 5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7]) == [-1, 7, 6, 5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 7, 8],nums2 = [1, 2, 3, 6, 7, 8, 5, 4]) == [7, 8, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 7, 8],nums2 = [1, 2, 3, 6, 7, 8, 5, 4]) == [7, 8, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 6]) == [6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 6]) == [6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000],nums2 = [100, 1, 1000, 10, 200, 300, 400, 500]) == [1000, 200, 1000, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000],nums2 = [100, 1, 1000, 10, 200, 300, 400, 500]) == [1000, 200, 1000, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 1, 4],nums2 = [9, 3, 8, 1, 7, 6, 5, 4, 2]) == [8, -1, 7, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 1, 4],nums2 = [9, 3, 8, 1, 7, 6, 5, 4, 2]) == [8, -1, 7, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 12, 11, 13],nums2 = [15, 12, 11, 14, 10, 9, 8, 13, 16]) == [16, 14, 14, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 12, 11, 13],nums2 = [15, 12, 11, 14, 10, 9, 8, 13, 16]) == [16, 14, 14, 16]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 99, 98, 97, 96],nums2 = [96, 97, 98, 99, 100, 101, 102, 103]) == [101, 100, 99, 98, 97]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 99, 98, 97, 96],nums2 = [96, 97, 98, 99, 100, 101, 102, 103]) == [101, 100, 99, 98, 97]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [11, 9, 7, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [11, 9, 7, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 7, 4, 2, 10],nums2 = [2, 1, 10, 7, 4, 5, 3]) == [10, -1, 5, 10, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 7, 4, 2, 10],nums2 = [2, 1, 10, 7, 4, 5, 3]) == [10, -1, 5, 10, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 13, 7, 5, 3, 1],nums2 = [1, 3, 5, 7, 9, 11, 13, 15]) == [13, 15, 9, 7, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 13, 7, 5, 3, 1],nums2 = [1, 3, 5, 7, 9, 11, 13, 15]) == [13, 15, 9, 7, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15]) == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15]) == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10, 40, 50, 60]) == [40, 40, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10, 40, 50, 60]) == [40, 40, 40]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [10, 15, 20, 25, 30]) == [15, 25, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [10, 15, 20, 25, 30]) == [15, 25, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 4, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [7, 5, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 4, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [7, 5, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 5, 9],nums2 = [9, 4, 7, 3, 5, 1, 8, 6, 2]) == [8, 8, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 5, 9],nums2 = [9, 4, 7, 3, 5, 1, 8, 6, 2]) == [8, 8, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 6, 5],nums2 = [5, 1, 2, 3, 4, 6, 7]) == [-1, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 6, 5],nums2 = [5, 1, 2, 3, 4, 6, 7]) == [-1, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 11, 17, 19],nums2 = [3, 19, 23, 11, 17, 29, 21, 25]) == [19, 17, 29, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 11, 17, 19],nums2 = [3, 19, 23, 11, 17, 29, 21, 25]) == [19, 17, 29, 23]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 7, 3, 4, 5, 6],nums2 = [3, 4, 1, 6, 8, 9, 5, 2, 7]) == [6, -1, 4, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 7, 3, 4, 5, 6],nums2 = [3, 4, 1, 6, 8, 9, 5, 2, 7]) == [6, -1, 4, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 5, 10, 15, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [-1, 7, -1, 17, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 5, 10, 15, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [-1, 7, -1, 17, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 10, 18, 23, 5],nums2 = [18, 10, 15, 5, 23, 2, 11, 17, 3, 12]) == [23, 15, 23, -1, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 10, 18, 23, 5],nums2 = [18, 10, 15, 5, 23, 2, 11, 17, 3, 12]) == [23, 15, 23, -1, 23]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 12, 13],nums2 = [5, 11, 9, 12, 13, 8, 7, 6, 10]) == [12, 13, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 12, 13],nums2 = [5, 11, 9, 12, 13, 8, 7, 6, 10]) == [12, 13, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50, 40, 30, 20, 10]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50, 40, 30, 20, 10]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [400, 300, 200, 100, 50, 150, 250, 350, 450]) == [150, 250, 350, 450]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [400, 300, 200, 100, 50, 150, 250, 350, 450]) == [150, 250, 350, 450]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 6, 11, 13],nums2 = [1, 3, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 12, 14]) == [3, 8, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 6, 11, 13],nums2 = [1, 3, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 12, 14]) == [3, 8, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 25, 35],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 25, 35]) == [25, 35, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 25, 35],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 25, 35]) == [25, 35, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 5, 3, 1],nums2 = [1, 3, 5, 7, 9]) == [9, 7, 5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 5, 3, 1],nums2 = [1, 3, 5, 7, 9]) == [9, 7, 5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 8, 12, 15],nums2 = [15, 12, 5, 8, 20, 25, 30, 35]) == [8, 20, 20, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 8, 12, 15],nums2 = [15, 12, 5, 8, 20, 25, 30, 35]) == [8, 20, 20, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 1, 4],nums2 = [2, 6, 4, 5, 1, 9]) == [9, 9, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 1, 4],nums2 = [2, 6, 4, 5, 1, 9]) == [9, 9, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 10, 11],nums2 = [3, 4, 5, 1, 6, 9, 7, 8, 11, 10, 2]) == [11, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 10, 11],nums2 = [3, 4, 5, 1, 6, 9, 7, 8, 11, 10, 2]) == [11, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [-1, 9, 8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [-1, 9, 8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 3, 2, 1],nums2 = [1, 2, 3, 4]) == [-1, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 3, 2, 1],nums2 = [1, 2, 3, 4]) == [-1, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 6, 4, 2],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == [10, 8, 6, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 6, 4, 2],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == [10, 8, 6, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 6, 4, 5, 7, 3],nums2 = [3, 5, 4, 6, 2, 1, 7, 9, 8]) == [7, 7, 6, 6, 9, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 6, 4, 5, 7, 3],nums2 = [3, 5, 4, 6, 2, 1, 7, 9, 8]) == [7, 7, 6, 6, 9, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8, 1, 3, 5, 7]) == [3, 5, 7, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8, 1, 3, 5, 7]) == [3, 5, 7, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 22, 33],nums2 = [33, 22, 11, 44, 55, 66, 77]) == [44, 44, 44]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 22, 33],nums2 = [33, 22, 11, 44, 55, 66, 77]) == [44, 44, 44]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10, 60, 70, 80, 90]) == [60, 60, 60, 60, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10, 60, 70, 80, 90]) == [60, 60, 60, 60, 60]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 1, 3, 7, 6, 2, 5],nums2 = [7, 8, 2, 3, 4, 1, 6, 5, 9]) == [6, 6, 4, 8, 9, 3, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 1, 3, 7, 6, 2, 5],nums2 = [7, 8, 2, 3, 4, 1, 6, 5, 9]) == [6, 6, 4, 8, 9, 3, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12]) == [11, 11, 11, 11, 11, 11, 11, 11, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12]) == [11, 11, 11, 11, 11, 11, 11, 11, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [3, 4, 5, 1, 2]) == [2, -1, 4, 5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [3, 4, 5, 1, 2]) == [2, -1, 4, 5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 5, 3],nums2 = [3, 1, 10, 5, 9, 7, 4, 6, 8]) == [10, -1, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 5, 3],nums2 = [3, 1, 10, 5, 9, 7, 4, 6, 8]) == [10, -1, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 20],nums2 = [20, 10, 5, 25, 15, 30]) == [25, 25, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 20],nums2 = [20, 10, 5, 25, 15, 30]) == [25, 25, 25]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 5, 3, 2],nums2 = [3, 2, 7, 5, 4]) == [-1, -1, 7, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 5, 3, 2],nums2 = [3, 2, 7, 5, 4]) == [-1, -1, 7, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 7, 4, 3],nums2 = [3, 4, 1, 5, 7, 8, 9]) == [5, 8, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 7, 4, 3],nums2 = [3, 4, 1, 5, 7, 8, 9]) == [5, 8, 5, 4]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [2, 3, 5, 6],nums2 = [5, 6, 2, 3, 8, 9]) == [3, 8, 6, 8]
    assert candidate(nums1 = [1, 2],nums2 = [2, 1]) == [-1, -1]
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == [-1, -1, -1, -1]
    assert candidate(nums1 = [5],nums2 = [5]) == [-1]
    assert candidate(nums1 = [1, 6, 4, 8],nums2 = [4, 5, 1, 8, 6, 7, 9]) == [8, 7, 5, 9]
    assert candidate(nums1 = [5, 2, 6],nums2 = [4, 1, 5, 2, 3, 6]) == [6, 3, -1]
    assert candidate(nums1 = [2, 4],nums2 = [1, 2, 3, 4]) == [3, -1]
    assert candidate(nums1 = [4, 1, 2],nums2 = [1, 3, 4, 2]) == [-1, 3, -1]
    assert candidate(nums1 = [10, 5, 6],nums2 = [3, 4, 2, 1, 5, 7, 8, 9, 10, 6]) == [-1, 7, -1]
    assert candidate(nums1 = [2],nums2 = [1, 2]) == [-1]
    assert candidate(nums1 = [1, 3, 5, 7],nums2 = [1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]
    assert candidate(nums1 = [3, 5, 8],nums2 = [2, 3, 4, 5, 7, 8, 10]) == [4, 7, 10]
    assert candidate(nums1 = [1],nums2 = [3, 2, 1]) == [-1]
    assert candidate(nums1 = [9, 8, 7],nums2 = [8, 9, 7, 6, 5, 4, 3, 2, 1]) == [-1, 9, -1]
    assert candidate(nums1 = [3, 5, 8],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [4, 6, 9]
    assert candidate(nums1 = [9, 10, 7],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, -1, 8]
    assert candidate(nums1 = [1, 3, 5, 7],nums2 = [7, 5, 3, 1, 9, 11, 13]) == [9, 9, 9, 9]
    assert candidate(nums1 = [1],nums2 = [1]) == [-1]
    assert candidate(nums1 = [1, 3],nums2 = [2, 1, 3, 4]) == [3, 4]
    assert candidate(nums1 = [10, 8, 6],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [11, 9, 7]
    assert candidate(nums1 = [9, 7, 3],nums2 = [3, 6, 9, 12, 15, 7]) == [12, -1, 6]
    assert candidate(nums1 = [10, 9, 8],nums2 = [8, 9, 10, 5, 7]) == [-1, 10, 9]
    assert candidate(nums1 = [100, 90, 80, 70],nums2 = [70, 80, 90, 100, 110, 120, 130, 140, 150]) == [110, 100, 90, 80]
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == [3, 5, 7, 9, -1]
    assert candidate(nums1 = [33, 22, 11],nums2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == [44, 33, 22]
    assert candidate(nums1 = [100, 99, 98, 97],nums2 = [98, 100, 97, 99, 96, 95, 94, 93, 92]) == [-1, -1, 100, 99]
    assert candidate(nums1 = [3, 5, 2, 1],nums2 = [1, 2, 3, 5, 4]) == [5, -1, 3, 2]
    assert candidate(nums1 = [3, 5, 2, 4, 9],nums2 = [8, 5, 3, 9, 2, 4, 7, 6]) == [9, 9, 4, 7, -1]
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
    assert candidate(nums1 = [7, 8, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [8, 9, -1]
    assert candidate(nums1 = [3, 8, 9],nums2 = [10, 11, 7, 8, 6, 5, 3, 4, 9, 2, 1]) == [4, 9, -1]
    assert candidate(nums1 = [5, 7, 3, 9, 1],nums2 = [11, 14, 8, 15, 13, 2, 11, 5, 12, 7, 9, 3, 6, 10, 4, 1]) == [12, 9, 6, 10, -1]
    assert candidate(nums1 = [6, 2, 8, 9],nums2 = [6, 5, 4, 3, 2, 1, 10, 11, 8, 9, 7]) == [10, 10, 9, -1]
    assert candidate(nums1 = [11, 13, 15, 17],nums2 = [17, 15, 13, 11, 19, 21, 23]) == [19, 19, 19, 19]
    assert candidate(nums1 = [9, 8, 7, 6, 5],nums2 = [5, 6, 7, 8, 9]) == [-1, 9, 8, 7, 6]
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 6, 7]) == [6, 6, 6, 6, 6]
    assert candidate(nums1 = [1, 3, 5, 7],nums2 = [7, 5, 3, 1, 2, 4, 6, 8, 10]) == [2, 4, 6, 8]
    assert candidate(nums1 = [3, 6, 9, 12, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [4, 7, 10, 13, -1]
    assert candidate(nums1 = [3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [4, 6, 8, 10]
    assert candidate(nums1 = [15, 25, 35],nums2 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == [20, 30, 40]
    assert candidate(nums1 = [6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [7, 6, 5, 4, 3, 2]
    assert candidate(nums1 = [100, 90, 80, 70],nums2 = [70, 80, 90, 100, 110]) == [110, 100, 90, 80]
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 10, 20, 30, 50, 60, 70]) == [20, 30, 50, 50]
    assert candidate(nums1 = [6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6]) == [-1, 6, 5, 4, 3, 2]
    assert candidate(nums1 = [3, 2, 1],nums2 = [5, 3, 2, 1, 6, 4]) == [6, 6, 6]
    assert candidate(nums1 = [23, 56, 78, 90],nums2 = [90, 78, 56, 23, 12, 34, 45, 67, 89, 100]) == [34, 67, 89, 100]
    assert candidate(nums1 = [42, 55, 66, 77],nums2 = [42, 77, 55, 88, 66, 99, 100]) == [77, 88, 99, 88]
    assert candidate(nums1 = [8, 6, 4, 2],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 7, 5, 3]
    assert candidate(nums1 = [100, 90, 80],nums2 = [70, 80, 90, 100, 60, 50, 40, 30, 20, 10]) == [-1, 100, 90]
    assert candidate(nums1 = [10, 20, 30],nums2 = [10, 20, 30, 25, 15, 5, 40, 35, 33, 31]) == [20, 30, 40]
    assert candidate(nums1 = [6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [7, 8, 9, 10, -1]
    assert candidate(nums1 = [7, 3, 2],nums2 = [5, 7, 3, 2, 1, 8]) == [8, 8, 8]
    assert candidate(nums1 = [12, 14, 13, 11, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [13, 15, 14, 12, -1]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
    assert candidate(nums1 = [8, 10, 4, 3],nums2 = [1, 11, 10, 4, 8, 3, 7]) == [-1, -1, 8, 7]
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
    assert candidate(nums1 = [7, 6, 5, 4, 3, 2, 1],nums2 = [2, 1, 3, 6, 5, 4, 7]) == [-1, 7, 7, 7, 6, 3, 3]
    assert candidate(nums1 = [2, 6, 4, 5, 3],nums2 = [3, 1, 2, 5, 4, 7, 6]) == [5, -1, 7, 7, 5]
    assert candidate(nums1 = [8, 9, 10, 11],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [9, 10, 11, 12]
    assert candidate(nums1 = [3, 6, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [4, 7, 10]
    assert candidate(nums1 = [3, 5, 7, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [4, 6, 8, -1]
    assert candidate(nums1 = [7, 5, 3, 1],nums2 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [8, 6, 4, 2]
    assert candidate(nums1 = [100, 90, 80, 70],nums2 = [70, 80, 90, 100, 110, 120, 130]) == [110, 100, 90, 80]
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert candidate(nums1 = [3, 5, 2, 4, 9],nums2 = [9, 1, 2, 5, 3, 7, 8, 4, 6]) == [7, 7, 5, 6, -1]
    assert candidate(nums1 = [42, 23, 14, 5, 1],nums2 = [1, 5, 14, 23, 42, 3, 7, 11, 13, 19, 21, 27]) == [-1, 42, 23, 14, 5]
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17],nums2 = [15, 13, 11, 9, 7, 5, 3, 1, 17, 19]) == [17, 17, 17, 17, 17, 17, 17, 17, 19]
    assert candidate(nums1 = [5, 10, 15, 20],nums2 = [20, 15, 10, 5, 25, 30, 35, 40]) == [25, 25, 25, 25]
    assert candidate(nums1 = [7, 3, 9, 1],nums2 = [1, 3, 5, 7, 9]) == [9, 5, -1, 3]
    assert candidate(nums1 = [15, 10, 5],nums2 = [1, 2, 3, 4, 5, 10, 15, 20, 25]) == [20, 15, 10]
    assert candidate(nums1 = [10, 11, 12, 13],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1]
    assert candidate(nums1 = [7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7]) == [-1, 7, 6, 5, 4, 3, 2]
    assert candidate(nums1 = [6, 7, 8],nums2 = [1, 2, 3, 6, 7, 8, 5, 4]) == [7, 8, -1]
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 6]) == [6, 6, 6, 6, 6]
    assert candidate(nums1 = [7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1]
    assert candidate(nums1 = [1, 10, 100, 1000],nums2 = [100, 1, 1000, 10, 200, 300, 400, 500]) == [1000, 200, 1000, -1]
    assert candidate(nums1 = [3, 6, 1, 4],nums2 = [9, 3, 8, 1, 7, 6, 5, 4, 2]) == [8, -1, 7, -1]
    assert candidate(nums1 = [15, 12, 11, 13],nums2 = [15, 12, 11, 14, 10, 9, 8, 13, 16]) == [16, 14, 14, 16]
    assert candidate(nums1 = [100, 99, 98, 97, 96],nums2 = [96, 97, 98, 99, 100, 101, 102, 103]) == [101, 100, 99, 98, 97]
    assert candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [11, 9, 7, 5, 3]
    assert candidate(nums1 = [1, 7, 4, 2, 10],nums2 = [2, 1, 10, 7, 4, 5, 3]) == [10, -1, 5, 10, -1]
    assert candidate(nums1 = [11, 13, 7, 5, 3, 1],nums2 = [1, 3, 5, 7, 9, 11, 13, 15]) == [13, 15, 9, 7, 5, 3]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15]) == [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
    assert candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10, 40, 50, 60]) == [40, 40, 40]
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums1 = [10, 20, 30],nums2 = [10, 15, 20, 25, 30]) == [15, 25, -1]
    assert candidate(nums1 = [6, 4, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [7, 5, 2]
    assert candidate(nums1 = [7, 5, 9],nums2 = [9, 4, 7, 3, 5, 1, 8, 6, 2]) == [8, 8, -1]
    assert candidate(nums1 = [7, 6, 5],nums2 = [5, 1, 2, 3, 4, 6, 7]) == [-1, 7, 6]
    assert candidate(nums1 = [3, 11, 17, 19],nums2 = [3, 19, 23, 11, 17, 29, 21, 25]) == [19, 17, 29, 23]
    assert candidate(nums1 = [1, 7, 3, 4, 5, 6],nums2 = [3, 4, 1, 6, 8, 9, 5, 2, 7]) == [6, -1, 4, 6, 7, 8]
    assert candidate(nums1 = [2, 5, 10, 15, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [-1, 7, -1, 17, -1]
    assert candidate(nums1 = [15, 10, 18, 23, 5],nums2 = [18, 10, 15, 5, 23, 2, 11, 17, 3, 12]) == [23, 15, 23, -1, 23]
    assert candidate(nums1 = [11, 12, 13],nums2 = [5, 11, 9, 12, 13, 8, 7, 6, 10]) == [12, 13, -1]
    assert candidate(nums1 = [50, 60, 70, 80, 90],nums2 = [90, 80, 70, 60, 50, 40, 30, 20, 10]) == [-1, -1, -1, -1, -1]
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [400, 300, 200, 100, 50, 150, 250, 350, 450]) == [150, 250, 350, 450]
    assert candidate(nums1 = [1, 6, 11, 13],nums2 = [1, 3, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 12, 14]) == [3, 8, 13, 14]
    assert candidate(nums1 = [15, 25, 35],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 25, 35]) == [25, 35, -1]
    assert candidate(nums1 = [7, 5, 3, 1],nums2 = [1, 3, 5, 7, 9]) == [9, 7, 5, 3]
    assert candidate(nums1 = [5, 8, 12, 15],nums2 = [15, 12, 5, 8, 20, 25, 30, 35]) == [8, 20, 20, 20]
    assert candidate(nums1 = [5, 1, 4],nums2 = [2, 6, 4, 5, 1, 9]) == [9, 9, 5]
    assert candidate(nums1 = [9, 10, 11],nums2 = [3, 4, 5, 1, 6, 9, 7, 8, 11, 10, 2]) == [11, -1, -1]
    assert candidate(nums1 = [9, 8, 7, 6],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [-1, 9, 8, 7]
    assert candidate(nums1 = [4, 3, 2, 1],nums2 = [1, 2, 3, 4]) == [-1, 4, 3, 2]
    assert candidate(nums1 = [4, 3, 2, 1, 0],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [5, 4, 3, 2, 1]
    assert candidate(nums1 = [8, 6, 4, 2],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == [10, 8, 6, 4]
    assert candidate(nums1 = [2, 6, 4, 5, 7, 3],nums2 = [3, 5, 4, 6, 2, 1, 7, 9, 8]) == [7, 7, 6, 6, 9, 5]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8, 1, 3, 5, 7]) == [3, 5, 7, -1]
    assert candidate(nums1 = [11, 22, 33],nums2 = [33, 22, 11, 44, 55, 66, 77]) == [44, 44, 44]
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10, 60, 70, 80, 90]) == [60, 60, 60, 60, 60]
    assert candidate(nums1 = [4, 1, 3, 7, 6, 2, 5],nums2 = [7, 8, 2, 3, 4, 1, 6, 5, 9]) == [6, 6, 4, 8, 9, 3, 9]
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12]) == [11, 11, 11, 11, 11, 11, 11, 11, 11]
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [3, 4, 5, 1, 2]) == [2, -1, 4, 5, -1]
    assert candidate(nums1 = [1, 10, 5, 3],nums2 = [3, 1, 10, 5, 9, 7, 4, 6, 8]) == [10, -1, 9, 10]
    assert candidate(nums1 = [5, 10, 20],nums2 = [20, 10, 5, 25, 15, 30]) == [25, 25, 25]
    assert candidate(nums1 = [7, 5, 3, 2],nums2 = [3, 2, 7, 5, 4]) == [-1, -1, 7, 7]
    assert candidate(nums1 = [1, 7, 4, 3],nums2 = [3, 4, 1, 5, 7, 8, 9]) == [5, 8, 5, 4]


