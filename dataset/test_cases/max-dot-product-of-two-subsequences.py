def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 1, -2, 5],nums2 = [3, 0, -6]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 1, -2, 5],nums2 = [3, 0, -6]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, -5, 4],nums2 = [-2, -4, 0, 3]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, -5, 4],nums2 = [-2, -4, 0, 3]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -1],nums2 = [1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -1],nums2 = [1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, -1000],nums2 = [-1000, 1000]) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, -1000],nums2 = [-1000, 1000]) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1000, 1000],nums2 = [-1000, 1000]) == 2000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1000, 1000],nums2 = [-1000, 1000]) == 2000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, -3],nums2 = [4, -1, -2]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, -3],nums2 = [4, -1, -2]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000],nums2 = [-1000]) == -1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000],nums2 = [-1000]) == -1000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4],nums2 = [5, 6, 7, 8, 9]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4],nums2 = [5, 6, 7, 8, 9]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1000],nums2 = [1000]) == -1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1000],nums2 = [1000]) == -1000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, -2],nums2 = [2, -6, 7]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, -2],nums2 = [2, -6, 7]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [-3, -2, -1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [-3, -2, -1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [-5, -4, -3]) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [-5, -4, -3]) == -3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3],nums2 = [1, 2, 3]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3],nums2 = [1, 2, 3]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 2, 1, 5],nums2 = [1, 2, 4, 2, 5]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 2, 1, 5],nums2 = [1, 2, 4, 2, 5]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [-1, -2, -3, -4, -5]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [-1, -2, -3, -4, -5]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999, -999, 999, -999, 999],nums2 = [-999, 999, -999, 999, -999]) == 3992004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999, -999, 999, -999, 999],nums2 = [-999, 999, -999, 999, -999]) == 3992004: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 2, -4, 7, -8],nums2 = [3, -1, 6, -3, 2]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 2, -4, 7, -8],nums2 = [3, -1, 6, -3, 2]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 2, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 2, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 1, -1, 1, -1],nums2 = [-1, 1, -1, 1, -1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 1, -1, 1, -1],nums2 = [-1, 1, -1, 1, -1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 1, -1, 1],nums2 = [1, -1, 1, -1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 1, -1, 1],nums2 = [1, -1, 1, -1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, -4, 2, 1],nums2 = [-2, 6, 3, -5, 4]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, -4, 2, 1],nums2 = [-2, 6, 3, -5, 4]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, -2, 4],nums2 = [1, 2, 3, 4, 5]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, -2, 4],nums2 = [1, 2, 3, 4, 5]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, -100, 200, -200, 300],nums2 = [1, -1, 2, -2, 3]) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, -100, 200, -200, 300],nums2 = [1, -1, 2, -2, 3]) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],nums2 = [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],nums2 = [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, -100, 200, -200],nums2 = [-100, 100, -200, 200]) == 70000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, -100, 200, -200],nums2 = [-100, 100, -200, 200]) == 70000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-1, -2, -3, -4, -5]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-1, -2, -3, -4, -5]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -20, -30, -40, -50],nums2 = [1, 2, 3, 4, 5]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -20, -30, -40, -50],nums2 = [1, 2, 3, 4, 5]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999, 1000, -999, -1000],nums2 = [-999, 999, -1000, 1000]) == 1999000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999, 1000, -999, -1000],nums2 = [-999, 999, -1000, 1000]) == 1999000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-10, -20, -30, -40, -50]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-10, -20, -30, -40, -50]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 320: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],nums2 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],nums2 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, -10, 15, -20, 25],nums2 = [-5, 10, -15, 20]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, -10, 15, -20, 25],nums2 = [-5, 10, -15, 20]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, -100, 200, -200, 300, -300],nums2 = [10, -10, 20, -20, 30, -30]) == 28000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, -100, 200, -200, 300, -300],nums2 = [10, -10, 20, -20, 30, -30]) == 28000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, -1, 2, -2, 3, -3],nums2 = [3, -3, 2, -2, 1, -1, 0]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, -1, 2, -2, 3, -3],nums2 = [3, -3, 2, -2, 1, -1, 0]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, -3, 10, 2, -7],nums2 = [8, 4, -2, 6, 1]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, -3, 10, 2, -7],nums2 = [8, 4, -2, 6, 1]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-500, -400, -300, -200, -100],nums2 = [100, 200, 300, 400, 500]) == -10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-500, -400, -300, -200, -100],nums2 = [100, 200, 300, 400, 500]) == -10000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -3, -2, -4],nums2 = [-1, -2, -3, -4, -5]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -3, -2, -4],nums2 = [-1, -2, -3, -4, -5]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1029
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1029: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 0, 200, 0, 300, 0, 400, 0, 500, 0],nums2 = [0, 500, 0, 400, 0, 300, 0, 200, 0, 100]) == 460000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 0, 200, 0, 300, 0, 400, 0, 500, 0],nums2 = [0, 500, 0, 400, 0, 300, 0, 200, 0, 100]) == 460000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, -10, 20, -20, 30],nums2 = [30, -30, 20, -20, 10]) == 1800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, -10, 20, -20, 30],nums2 = [30, -30, 20, -20, 10]) == 1800: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1, 0, -1],nums2 = [-1, 0, 1, 0, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1, 0, -1],nums2 = [-1, 0, 1, 0, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [-1, -2, -3, -4, -5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [-1, -2, -3, -4, -5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, -3, 8, -1, 7],nums2 = [-2, 4, 1, -5, 3]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, -3, 8, -1, 7],nums2 = [-2, 4, 1, -5, 3]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -2, -3, -4, -5],nums2 = [5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -2, -3, -4, -5],nums2 = [5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [-100, -200, -300, -400, -500]) == -10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [-100, -200, -300, -400, -500]) == -10000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 900, 800, 700, 600],nums2 = [10, 20, 30, 40, 50]) == 114000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 900, 800, 700, 600],nums2 = [10, 20, 30, 40, 50]) == 114000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, -3, 2, 1, 6],nums2 = [-1, 2, -3, 4, 5]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, -3, 2, 1, 6],nums2 = [-1, 2, -3, 4, 5]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [100, 200, 300, 400, 500]) == 2600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [100, 200, 300, 400, 500]) == 2600: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -2, -3, -4, -5],nums2 = [-5, -4, -3, -2, -1]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -2, -3, -4, -5],nums2 = [-5, -4, -3, -2, -1]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -2, 3, -4, 5],nums2 = [-5, 4, -3, 2, -1]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -2, 3, -4, 5],nums2 = [-5, 4, -3, 2, -1]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 2, 3]) == 2600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 2, 3]) == 2600: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 38500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 38500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999, -999, 888, -888, 777, -777],nums2 = [-666, 666, -555, 555, -444, 444, -333, 333]) == 2710620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999, -999, 888, -888, 777, -777],nums2 = [-666, 666, -555, 555, -444, 444, -333, 333]) == 2710620: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 1, -1, 1],nums2 = [-1, 1, -1, 1, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 1, -1, 1],nums2 = [-1, 1, -1, 1, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 4750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 4750: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 999, 998, 997, 996],nums2 = [1, 2, 3, 4, 5]) == 14960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 999, 998, 997, 996],nums2 = [1, 2, 3, 4, 5]) == 14960: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [100, 200, 300]) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [100, 200, 300]) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, -100, 200, -200],nums2 = [300, -300, 400, -400]) == 220000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, -100, 200, -200],nums2 = [300, -300, 400, -400]) == 220000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6, 7, 8, 9, 10, 11, 12]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6, 7, 8, 9, 10, 11, 12]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3, 4, 5]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3, 4, 5]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, -3, 8, 1],nums2 = [-7, 4, 6, -2]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, -3, 8, 1],nums2 = [-7, 4, 6, -2]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, -5, 7, -9],nums2 = [-9, 7, -5, 3, 1]) == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, -5, 7, -9],nums2 = [-9, 7, -5, 3, 1]) == 139: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, -5, 7, -9, 11],nums2 = [11, -9, 7, -5, 3, -1]) == 235
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, -5, 7, -9, 11],nums2 = [11, -9, 7, -5, 3, -1]) == 235: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, -5, 7, -9],nums2 = [-2, 4, -6, 8, -10]) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, -5, 7, -9],nums2 = [-2, 4, -6, 8, -10]) == 188: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3850: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -5, -5, -5, -5],nums2 = [-5, -5, -5, -5, -5]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -5, -5, -5, -5],nums2 = [-5, -5, -5, -5, -5]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 0, -1, 0, 1],nums2 = [0, 1, 0, -1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 0, -1, 0, 1],nums2 = [0, 1, 0, -1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == 460000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == 460000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -2, -3, -4, -5],nums2 = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -2, -3, -4, -5],nums2 = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50, -40, -30, -20, -10],nums2 = [-10, -20, -30, -40, -50]) == 4600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50, -40, -30, -20, -10],nums2 = [-10, -20, -30, -40, -50]) == 4600: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 2, -2, 3, -3],nums2 = [-1, 1, -2, 2, -3, 3]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 2, -2, 3, -3],nums2 = [-1, 1, -2, 2, -3, 3]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300],nums2 = [1, 2, 3, 4, 5]) == 2600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300],nums2 = [1, 2, 3, 4, 5]) == 2600: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -1, -1, -1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -1, -1, -1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 2, -2, 3, -3],nums2 = [3, -3, 2, -2, 1, -1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 2, -2, 3, -3],nums2 = [3, -3, 2, -2, 1, -1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [10]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [10]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-50, -40, -30, -20, -10]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-50, -40, -30, -20, -10]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -20, -30, -40, -50],nums2 = [10, 20, 30, 40, 50]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -20, -30, -40, -50],nums2 = [10, 20, 30, 40, 50]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 4600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 4600: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 0, -1, 0, 1],nums2 = [1, 0, -1, 0, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 0, -1, 0, 1],nums2 = [1, 0, -1, 0, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [2, 4, 6, 8, 10, 12, 14]) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [2, 4, 6, 8, 10, 12, 14]) == 504: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1, -2, 0, 2],nums2 = [2, 0, -2, 0, 1, -1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1, -2, 0, 2],nums2 = [2, 0, -2, 0, 1, -1]) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1]) == 2
    assert candidate(nums1 = [2, 1, -2, 5],nums2 = [3, 0, -6]) == 18
    assert candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == 46
    assert candidate(nums1 = [1, 3, -5, 4],nums2 = [-2, -4, 0, 3]) == 32
    assert candidate(nums1 = [-1, -1],nums2 = [1, 1]) == -1
    assert candidate(nums1 = [1000, -1000],nums2 = [-1000, 1000]) == 1000000
    assert candidate(nums1 = [-1000, 1000],nums2 = [-1000, 1000]) == 2000000
    assert candidate(nums1 = [5, 4, -3],nums2 = [4, -1, -2]) == 26
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 46
    assert candidate(nums1 = [1000],nums2 = [-1000]) == -1000000
    assert candidate(nums1 = [0, 1, 2, 3, 4],nums2 = [5, 6, 7, 8, 9]) == 80
    assert candidate(nums1 = [-1000],nums2 = [1000]) == -1000000
    assert candidate(nums1 = [3, -2],nums2 = [2, -6, 7]) == 21
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [-3, -2, -1, 0]) == 0
    assert candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5]) == 46
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 46
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == 12
    assert candidate(nums1 = [1, 2, 3],nums2 = [-5, -4, -3]) == -3
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 32
    assert candidate(nums1 = [5, 4, 3],nums2 = [1, 2, 3]) == 22
    assert candidate(nums1 = [5, 5, 2, 1, 5],nums2 = [1, 2, 4, 2, 5]) == 59
    assert candidate(nums1 = [1],nums2 = [1]) == 1
    assert candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [-1, -2, -3, -4, -5]) == 46
    assert candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 0
    assert candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5]) == -1
    assert candidate(nums1 = [999, -999, 999, -999, 999],nums2 = [-999, 999, -999, 999, -999]) == 3992004
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums1 = [5, 2, -4, 7, -8],nums2 = [3, -1, 6, -3, 2]) == 85
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 2, 3, 4]) == 0
    assert candidate(nums1 = [1, -1, 1, -1, 1, -1],nums2 = [-1, 1, -1, 1, -1, 1]) == 5
    assert candidate(nums1 = [1, -1, 1, -1, 1],nums2 = [1, -1, 1, -1, 1]) == 5
    assert candidate(nums1 = [5, 3, -4, 2, 1],nums2 = [-2, 6, 3, -5, 4]) == 67
    assert candidate(nums1 = [5, 3, -2, 4],nums2 = [1, 2, 3, 4, 5]) == 47
    assert candidate(nums1 = [100, -100, 200, -200, 300],nums2 = [1, -1, 2, -2, 3]) == 1900
    assert candidate(nums1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],nums2 = [-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == 90
    assert candidate(nums1 = [100, -100, 200, -200],nums2 = [-100, 100, -200, 200]) == 70000
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-1, -2, -3, -4, -5]) == -10
    assert candidate(nums1 = [-10, -20, -30, -40, -50],nums2 = [1, 2, 3, 4, 5]) == -10
    assert candidate(nums1 = [999, 1000, -999, -1000],nums2 = [-999, 999, -1000, 1000]) == 1999000
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == -100
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-10, -20, -30, -40, -50]) == -100
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 320
    assert candidate(nums1 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],nums2 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 81
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5]) == 125
    assert candidate(nums1 = [5, -10, 15, -20, 25],nums2 = [-5, 10, -15, 20]) == 1000
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 46
    assert candidate(nums1 = [100, -100, 200, -200, 300, -300],nums2 = [10, -10, 20, -20, 30, -30]) == 28000
    assert candidate(nums1 = [0, 1, -1, 2, -2, 3, -3],nums2 = [3, -3, 2, -2, 1, -1, 0]) == 24
    assert candidate(nums1 = [5, -3, 10, 2, -7],nums2 = [8, 4, -2, 6, 1]) == 108
    assert candidate(nums1 = [-500, -400, -300, -200, -100],nums2 = [100, 200, 300, 400, 500]) == -10000
    assert candidate(nums1 = [-5, -3, -2, -4],nums2 = [-1, -2, -3, -4, -5]) == 47
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1029
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 74
    assert candidate(nums1 = [100, 0, 200, 0, 300, 0, 400, 0, 500, 0],nums2 = [0, 500, 0, 400, 0, 300, 0, 200, 0, 100]) == 460000
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9]) == 190
    assert candidate(nums1 = [10, -10, 20, -20, 30],nums2 = [30, -30, 20, -20, 10]) == 1800
    assert candidate(nums1 = [-1, 0, 1, 0, -1],nums2 = [-1, 0, 1, 0, -1]) == 3
    assert candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [-1, -2, -3, -4, -5]) == -1
    assert candidate(nums1 = [5, -3, 8, -1, 7],nums2 = [-2, 4, 1, -5, 3]) == 64
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3]) == 56
    assert candidate(nums1 = [-1, -2, -3, -4, -5],nums2 = [5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [-100, -200, -300, -400, -500]) == -10000
    assert candidate(nums1 = [1000, 900, 800, 700, 600],nums2 = [10, 20, 30, 40, 50]) == 114000
    assert candidate(nums1 = [5, -3, 2, 1, 6],nums2 = [-1, 2, -3, 4, 5]) == 57
    assert candidate(nums1 = [1, 2, 3],nums2 = [100, 200, 300, 400, 500]) == 2600
    assert candidate(nums1 = [-1, -2, -3, -4, -5],nums2 = [-5, -4, -3, -2, -1]) == 46
    assert candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
    assert candidate(nums1 = [1, -2, 3, -4, 5],nums2 = [-5, 4, -3, 2, -1]) == 44
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 2, 3]) == 2600
    assert candidate(nums1 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 38500
    assert candidate(nums1 = [999, -999, 888, -888, 777, -777],nums2 = [-666, 666, -555, 555, -444, 444, -333, 333]) == 2710620
    assert candidate(nums1 = [1, -1, 1, -1, 1],nums2 = [-1, 1, -1, 1, -1]) == 4
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 4750
    assert candidate(nums1 = [1000, 999, 998, 997, 996],nums2 = [1, 2, 3, 4, 5]) == 14960
    assert candidate(nums1 = [5, 4, 3, 2, 1],nums2 = [100, 200, 300]) == 2200
    assert candidate(nums1 = [100, -100, 200, -200],nums2 = [300, -300, 400, -400]) == 220000
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6, 7, 8, 9, 10, 11, 12]) == 68
    assert candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3, 4, 5]) == 23
    assert candidate(nums1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums1 = [5, -3, 8, 1],nums2 = [-7, 4, 6, -2]) == 69
    assert candidate(nums1 = [1, 3, -5, 7, -9],nums2 = [-9, 7, -5, 3, 1]) == 139
    assert candidate(nums1 = [1, 3, -5, 7, -9, 11],nums2 = [11, -9, 7, -5, 3, -1]) == 235
    assert candidate(nums1 = [1, 3, -5, 7, -9],nums2 = [-2, 4, -6, 8, -10]) == 188
    assert candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10]) == 1200
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3850
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 190
    assert candidate(nums1 = [-5, -5, -5, -5, -5],nums2 = [-5, -5, -5, -5, -5]) == 125
    assert candidate(nums1 = [1, 0, -1, 0, 1],nums2 = [0, 1, 0, -1, 0]) == 2
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == 460000
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5]) == 55
    assert candidate(nums1 = [-1, -2, -3, -4, -5],nums2 = [1, 2, 3, 4, 5]) == -1
    assert candidate(nums1 = [-50, -40, -30, -20, -10],nums2 = [-10, -20, -30, -40, -50]) == 4600
    assert candidate(nums1 = [1, -1, 2, -2, 3, -3],nums2 = [-1, 1, -2, 2, -3, 3]) == 22
    assert candidate(nums1 = [100, 200, 300],nums2 = [1, 2, 3, 4, 5]) == 2600
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -1, -1, -1, -1]) == -1
    assert candidate(nums1 = [1, -1, 2, -2, 3, -3],nums2 = [3, -3, 2, -2, 1, -1]) == 24
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5]) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [10]) == 1000
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-50, -40, -30, -20, -10]) == -100
    assert candidate(nums1 = [-10, -20, -30, -40, -50],nums2 = [10, 20, 30, 40, 50]) == -100
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 4600
    assert candidate(nums1 = [1, 0, -1, 0, 1],nums2 = [1, 0, -1, 0, 1]) == 3
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [2, 4, 6, 8, 10, 12, 14]) == 504
    assert candidate(nums1 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1]) == -1
    assert candidate(nums1 = [-1, 0, 1, -2, 0, 2],nums2 = [2, 0, -2, 0, 1, -1]) == 8


