def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [3, 8, 5, 2],nums2 = [2, 4, 1, 6],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 8, 5, 2],nums2 = [2, 4, 1, 6],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [10, 10, 10, 10],k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [10, 10, 10, 10],k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [1, 2, 3, 4],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [1, 2, 3, 4],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [20, 30, 40],k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [20, 30, 40],k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [10, 10, 0, 0],k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [10, 10, 0, 0],k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1],nums2 = [2, 2, 2],k = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1],nums2 = [2, 2, 2],k = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [1, 2, 3],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [1, 2, 3],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10],k = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10],k = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [1, 1, 1, 1],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [1, 1, 1, 1],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [10, 20, 30],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [10, 20, 30],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 3, 1, 4],nums2 = [1, 3, 7, 1],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 3, 1, 4],nums2 = [1, 3, 7, 1],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100],k = 50) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100],k = 50) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 0, 0, 0],nums2 = [0, 0, 0, 1000000000],k = 250000000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 0, 0, 0],nums2 = [0, 0, 0, 1000000000],k = 250000000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [9, 9, 9, 9, 9, 9, 9, 9],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [9, 9, 9, 9, 9, 9, 9, 9],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 3],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 3],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 1000000000, 1000000000],nums2 = [500000000, 500000000, 500000000],k = 500000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 1000000000, 1000000000],nums2 = [500000000, 500000000, 500000000],k = 500000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [20, 30, 40, 50, 60],k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [20, 30, 40, 50, 60],k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 150, 250, 350, 451],k = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 150, 250, 350, 451],k = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [10, 8, 6, 4, 2],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [10, 8, 6, 4, 2],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 0, 0, 1000000000],nums2 = [500000000, 500000000, 500000000, 500000000],k = 500000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 0, 0, 1000000000],nums2 = [500000000, 500000000, 500000000, 500000000],k = 500000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [400, 300, 200, 100],k = 50) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [400, 300, 200, 100],k = 50) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 200000, 300000],nums2 = [300000, 200000, 100000],k = 100000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 200000, 300000],nums2 = [300000, 200000, 100000],k = 100000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [6, 5, 4, 3, 2, 1],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [6, 5, 4, 3, 2, 1],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0],k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0],k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [10, -10, 20, -20],k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [10, -10, 20, -20],k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 150, 200, 250, 300],nums2 = [300, 250, 200, 150, 100],k = 50) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 150, 200, 250, 300],nums2 = [300, 250, 200, 150, 100],k = 50) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [400, 300, 200, 100],k = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [400, 300, 200, 100],k = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [7, 7, 7, 7, 7, 7, 7, 7],k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [7, 7, 7, 7, 7, 7, 7, 7],k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [13, 11, 9, 7, 5, 3, 1],k = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [13, 11, 9, 7, 5, 3, 1],k = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [600, 500, 400, 300, 200, 100],k = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [600, 500, 400, 300, 200, 100],k = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 500000000, 250000000, 125000000],nums2 = [0, 0, 0, 0],k = 125000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 500000000, 250000000, 125000000],nums2 = [0, 0, 0, 0],k = 125000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 100, 150, 200, 250],k = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 100, 150, 200, 250],k = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [10, 8, 6, 4, 2],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [10, 8, 6, 4, 2],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [10, 8, 6, 4, 2],k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [10, 8, 6, 4, 2],k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100],k = 10) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100],k = 10) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [60, 50, 40, 30, 20, 10],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [60, 50, 40, 30, 20, 10],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 15, 20, 25, 30, 35],nums2 = [35, 30, 25, 20, 15, 10],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 15, 20, 25, 30, 35],nums2 = [35, 30, 25, 20, 15, 10],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100],k = 50) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100],k = 50) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45, 55, 65],nums2 = [15, 25, 35, 45, 55, 65, 75],k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45, 55, 65],nums2 = [15, 25, 35, 45, 55, 65, 75],k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [10, 20, 30, 40, 50],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [10, 20, 30, 40, 50],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 1000000, 1000000],nums2 = [500000, 500000, 500000],k = 500000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 1000000, 1000000],nums2 = [500000, 500000, 500000],k = 500000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 7, 7, 7],nums2 = [1, 13, 1, 13],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 7, 7, 7],nums2 = [1, 13, 1, 13],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45],k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45],k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 9],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 9],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 6, 7, 8, 9, 10],nums2 = [15, 14, 13, 12, 11, 10],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 6, 7, 8, 9, 10],nums2 = [15, 14, 13, 12, 11, 10],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45, 55, 65],nums2 = [65, 55, 45, 35, 25, 15, 5],k = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45, 55, 65],nums2 = [65, 55, 45, 35, 25, 15, 5],k = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 0, 500000000, 500000000],nums2 = [500000000, 500000000, 0, 1000000000],k = 500000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 0, 500000000, 500000000],nums2 = [500000000, 500000000, 0, 1000000000],k = 500000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2],k = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2],k = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [5, 5, 5, 5, 5, 5],k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [5, 5, 5, 5, 5, 5],k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [6, 5, 4, 3, 2, 1],k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [6, 5, 4, 3, 2, 1],k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 1000000000, 1000000000],nums2 = [999999998, 1000000002, 1000000000],k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 1000000000, 1000000000],nums2 = [999999998, 1000000002, 1000000000],k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 3],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 3],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [6, 6, 6, 6, 6, 6],k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [6, 6, 6, 6, 6, 6],k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [10, 20, 30, 40, 50],k = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [10, 20, 30, 40, 50],k = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [6, 6, 6, 6, 6, 6],k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [6, 6, 6, 6, 6, 6],k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 150, 250, 350, 450],k = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 150, 250, 350, 450],k = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 10) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 10) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45],nums2 = [45, 36, 27, 18, 9],k = 9) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45],nums2 = [45, 36, 27, 18, 9],k = 9) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16],nums2 = [16, 14, 12, 10, 8, 6, 4, 2],k = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16],nums2 = [16, 14, 12, 10, 8, 6, 4, 2],k = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [3, 8, 5, 2],nums2 = [2, 4, 1, 6],k = 1) == -1
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [10, 10, 10, 10],k = 5) == -1
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [1, 2, 3, 4],k = 2) == 0
    assert candidate(nums1 = [10, 20, 30],nums2 = [20, 30, 40],k = 10) == -1
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1],k = 2) == 1
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0],k = 0) == 0
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [10, 10, 0, 0],k = 5) == 2
    assert candidate(nums1 = [1, 1, 1],nums2 = [2, 2, 2],k = 0) == -1
    assert candidate(nums1 = [1, 2, 3],nums2 = [1, 2, 3],k = 0) == 0
    assert candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0],k = 0) == 0
    assert candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10],k = 10) == 2
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [1, 1, 1, 1],k = 2) == -1
    assert candidate(nums1 = [10, 20, 30],nums2 = [10, 20, 30],k = 5) == 0
    assert candidate(nums1 = [4, 3, 1, 4],nums2 = [1, 3, 7, 1],k = 3) == 2
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 100
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100],k = 50) == 12
    assert candidate(nums1 = [1000000000, 0, 0, 0],nums2 = [0, 0, 0, 1000000000],k = 250000000) == 4
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [9, 9, 9, 9, 9, 9, 9, 9],k = 2) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 3],k = 1) == -1
    assert candidate(nums1 = [1000000000, 1000000000, 1000000000],nums2 = [500000000, 500000000, 500000000],k = 500000000) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [20, 30, 40, 50, 60],k = 10) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1],k = 2) == 6
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 10) == 4
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 150, 250, 350, 451],k = 50) == -1
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == -1
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [10, 8, 6, 4, 2],k = 2) == 6
    assert candidate(nums1 = [1000000000, 0, 0, 1000000000],nums2 = [500000000, 500000000, 500000000, 500000000],k = 500000000) == 2
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [400, 300, 200, 100],k = 50) == 8
    assert candidate(nums1 = [100000, 200000, 300000],nums2 = [300000, 200000, 100000],k = 100000) == 2
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 0) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [6, 5, 4, 3, 2, 1],k = 1) == 9
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],k = 1) == 9
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0],k = 5) == 5
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [10, -10, 20, -20],k = 10) == 3
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 10) == 4
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11],k = 1) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9],k = 1) == 1
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 10) == 6
    assert candidate(nums1 = [100, 150, 200, 250, 300],nums2 = [300, 250, 200, 150, 100],k = 50) == 6
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2],k = 1) == -1
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0],k = 100000) == 0
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [400, 300, 200, 100],k = 100) == 4
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [7, 7, 7, 7, 7, 7, 7, 7],k = 3) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [13, 11, 9, 7, 5, 3, 1],k = 2) == 12
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 15) == -1
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [600, 500, 400, 300, 200, 100],k = 100) == 9
    assert candidate(nums1 = [1000000000, 500000000, 250000000, 125000000],nums2 = [0, 0, 0, 0],k = 125000000) == -1
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 100, 150, 200, 250],k = 50) == -1
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [10, 8, 6, 4, 2],k = 2) == 6
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9],k = 1) == -1
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [10, 8, 6, 4, 2],k = 3) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 10
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100],k = 10) == 60
    assert candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 0) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [60, 50, 40, 30, 20, 10],k = 10) == 9
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],k = 0) == 0
    assert candidate(nums1 = [10, 15, 20, 25, 30, 35],nums2 = [35, 30, 25, 20, 15, 10],k = 5) == 9
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100],k = 50) == 12
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 0
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1) == 25
    assert candidate(nums1 = [5, 15, 25, 35, 45, 55, 65],nums2 = [15, 25, 35, 45, 55, 65, 75],k = 10) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2],k = 1) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1],k = 100) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 10) == 6
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [10, 20, 30, 40, 50],k = 5) == 0
    assert candidate(nums1 = [1000000, 1000000, 1000000],nums2 = [500000, 500000, 500000],k = 500000) == -1
    assert candidate(nums1 = [7, 7, 7, 7],nums2 = [1, 13, 1, 13],k = 3) == 4
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45],k = 5) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 9],k = 2) == -1
    assert candidate(nums1 = [5, 6, 7, 8, 9, 10],nums2 = [15, 14, 13, 12, 11, 10],k = 2) == -1
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],k = 5) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums1 = [5, 15, 25, 35, 45, 55, 65],nums2 = [65, 55, 45, 35, 25, 15, 5],k = 10) == 12
    assert candidate(nums1 = [1000000000, 0, 500000000, 500000000],nums2 = [500000000, 500000000, 0, 1000000000],k = 500000000) == 2
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 1) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 25
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 25
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2],k = 0) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [5, 5, 5, 5, 5, 5],k = 4) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [6, 5, 4, 3, 2, 1],k = 1) == 9
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000) == 0
    assert candidate(nums1 = [1000000000, 1000000000, 1000000000],nums2 = [999999998, 1000000002, 1000000000],k = 1) == 2
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 5) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 1) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1],k = 2) == 6
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 3],k = 2) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [6, 6, 6, 6, 6, 6],k = 1) == -1
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [10, 20, 30, 40, 50],k = 0) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [6, 6, 6, 6, 6, 6],k = 5) == -1
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 2) == 10
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [50, 150, 250, 350, 450],k = 50) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 10) == 25
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 5) == 8
    assert candidate(nums1 = [9, 18, 27, 36, 45],nums2 = [45, 36, 27, 18, 9],k = 9) == 6
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16],nums2 = [16, 14, 12, 10, 8, 6, 4, 2],k = 2) == 16
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5],k = 0) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 56
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10],k = 5) == 12
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [40, 30, 20, 10],k = 5) == 8
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == -1


