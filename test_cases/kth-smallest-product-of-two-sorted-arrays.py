def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [-100000, 100000],nums2 = [-100000, 100000],k = 1) == -10000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100000, 100000],nums2 = [-100000, 100000],k = 1) == -10000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100000, -50000, 0, 50000, 100000],nums2 = [-100000, -50000, 0, 50000, 100000],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100000, -50000, 0, 50000, 100000],nums2 = [-100000, -50000, 0, 50000, 100000],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -9, -8, -7, -6],nums2 = [-5, -4, -3, -2, -1],k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -9, -8, -7, -6],nums2 = [-5, -4, -3, -2, -1],k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 25) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 25) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 5],nums2 = [3, 4],k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 5],nums2 = [3, 4],k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-4, -2, 0, 3],nums2 = [2, 4],k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-4, -2, 0, 3],nums2 = [2, 4],k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100000, 100000],nums2 = [-100000, 100000],k = 2) == -10000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100000, 100000],nums2 = [-100000, 100000],k = 2) == -10000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -3, -1, 1, 3, 5],nums2 = [-5, -3, -1, 1, 3, 5],k = 18) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -3, -1, 1, 3, 5],nums2 = [-5, -3, -1, 1, 3, 5],k = 18) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-2, -1, 0, 1, 2],nums2 = [-3, -1, 2, 4, 5],k = 3) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-2, -1, 0, 1, 2],nums2 = [-3, -1, 2, 4, 5],k = 3) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5],k = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5],k = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, -1],nums2 = [1, 5, 10],k = 5) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, -1],nums2 = [1, 5, 10],k = 5) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100, -50, -10, -5, 0, 5, 10, 50, 100],nums2 = [-100, -50, -10, -5, 0, 5, 10, 50, 100],k = 200) == 10001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100, -50, -10, -5, 0, 5, 10, 50, 100],nums2 = [-100, -50, -10, -5, 0, 5, 10, 50, 100],k = 200) == 10001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [-5, -4, -3, -2, -1],k = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [-5, -4, -3, -2, -1],k = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-10000, 0, 10000],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-10000, 0, 10000],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-25, -15, -5, 5, 15, 25],nums2 = [-25, -15, -5, 0, 5, 15, 25],k = 30) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-25, -15, -5, 5, 15, 25],nums2 = [-25, -15, -5, 0, 5, 15, 25],k = 30) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-10000, -5000, 0, 5000, 10000],k = 7) == -125000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-10000, -5000, 0, 5000, 10000],k = 7) == -125000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-10000, -5000, 0, 5000, 10000],k = 125000) == 500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-10000, -5000, 0, 5000, 10000],k = 125000) == 500000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1],k = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1],k = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 20) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 20) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-9, -3, 0, 1, 5],nums2 = [-6, -2, 1, 4, 7],k = 9) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-9, -3, 0, 1, 5],nums2 = [-6, -2, 1, 4, 7],k = 9) == -3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 124999) == 2500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 124999) == 2500000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-100, -50, 0, 50, 100],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-100, -50, 0, 50, 100],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5],k = 49) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5],k = 49) == -2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 24) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 24) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-200, -100, 0, 100, 200],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-200, -100, 0, 100, 200],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, -1, 0, 1, 5, 10],nums2 = [-20, -15, -10, -5, 0, 5, 10, 15, 20],k = 20) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, -1, 0, 1, 5, 10],nums2 = [-20, -15, -10, -5, 0, 5, 10, 15, 20],k = 20) == -15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],nums2 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],k = 1000) == 1000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],nums2 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],k = 1000) == 1000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 1250000) == 2500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 1250000) == 2500000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50, -25, 0, 25, 50],nums2 = [-50, -25, 0, 25, 50],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50, -25, 0, 25, 50],nums2 = [-50, -25, 0, 25, 50],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000],nums2 = [-100000, 0, 100000],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000],nums2 = [-100000, 0, 100000],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100000, 100000],nums2 = [-1, 1],k = 1) == -100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100000, 100000],nums2 = [-1, 1],k = 1) == -100000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1000, -900, -800],nums2 = [800, 900, 1000],k = 8) == -720000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1000, -900, -800],nums2 = [800, 900, 1000],k = 8) == -720000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100000, -50000, -10000, -5000, -1000, -500, -100, -50, -10, -5, 0, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],nums2 = [-100000, -50000, -10000, -5000, -1000, -500, -100, -50, -10, -5, 0, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],k = 1000000) == 10000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100000, -50000, -10000, -5000, -1000, -500, -100, -50, -10, -5, 0, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],nums2 = [-100000, -50000, -10000, -5000, -1000, -500, -100, -50, -10, -5, 0, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],k = 1000000) == 10000000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [-9, -7, -5, -3, -1],k = 15) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [-9, -7, -5, -3, -1],k = 15) == -15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 45) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 45) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 2, 3, 4, 5],k = 20) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 2, 3, 4, 5],k = 20) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 20000, 30000, 40000, 50000],nums2 = [-10000, -20000, -30000, -40000, -50000],k = 12) == -900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 20000, 30000, 40000, 50000],nums2 = [-10000, -20000, -30000, -40000, -50000],k = 12) == -900000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-2, -1, 0, 1, 2],nums2 = [-2, -1, 0, 1, 2, 3, 4, 5],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-2, -1, 0, 1, 2],nums2 = [-2, -1, 0, 1, 2, 3, 4, 5],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12],k = 36) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12],k = 36) == 132: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-5, -10, -15, -20, -25],k = 10) == -600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-5, -10, -15, -20, -25],k = 10) == -600: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1000, -500, -100, 0, 100, 500, 1000],nums2 = [-1000, -500, -100, 0, 100, 500, 1000],k = 48) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1000, -500, -100, 0, 100, 500, 1000],nums2 = [-1000, -500, -100, 0, 100, 500, 1000],k = 48) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-2, 0, 2],nums2 = [-2, 0, 2],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-2, 0, 2],nums2 = [-2, 0, 2],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -1, 0, 1, 1],nums2 = [-1, -1, 0, 1, 1],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -1, 0, 1, 1],nums2 = [-1, -1, 0, 1, 1],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-200, -100, 0, 100, 200],k = 50) == 20001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-200, -100, 0, 100, 200],k = 50) == 20001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 100) == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 100) == 380: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 20000, 30000, 40000, 50000],nums2 = [-1, -2, -3, -4, -5],k = 15) == -90000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 20000, 30000, 40000, 50000],nums2 = [-1, -2, -3, -4, -5],k = 15) == -90000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-100, -50, 0, 50, 100],k = 1000) == 10001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-100, -50, 0, 50, 100],k = 1000) == 10001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 125000000) == 2500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 125000000) == 2500000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10000, -5000, -1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000],nums2 = [-10000, -5000, -1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000],k = 361) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10000, -5000, -1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000],nums2 = [-10000, -5000, -1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000],k = 361) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 1],nums2 = [-100000, 100000],k = 1) == -100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 1],nums2 = [-100000, 100000],k = 1) == -100000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 324) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 324) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-100000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000],k = 100) == 100001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-100000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000],k = 100) == 100001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -1, -1, -1, -1],nums2 = [-1, -1, -1, -1, -1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -1, -1, -1, -1],nums2 = [-1, -1, -1, -1, -1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-3, -2, -1, 0, 1, 2, 3],nums2 = [-3, -2, -1, 0, 1, 2, 3],k = 21) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-3, -2, -1, 0, 1, 2, 3],nums2 = [-3, -2, -1, 0, 1, 2, 3],k = 21) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],nums2 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],k = 22500) == 1000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],nums2 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],k = 22500) == 1000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -1, -1, -1, -1],nums2 = [-1, -1, -1, -1, -1],k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -1, -1, -1, -1],nums2 = [-1, -1, -1, -1, -1],k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-100000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000],k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-100000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000],k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 500000) == 2500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 500000) == 2500000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -3, -1, 1, 3, 5],nums2 = [-5, -3, -1, 1, 3, 5],k = 15) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -3, -1, 1, 3, 5],nums2 = [-5, -3, -1, 1, 3, 5],k = 15) == -3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000],nums2 = [-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000],k = 1000000) == 2500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000],nums2 = [-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000],k = 1000000) == 2500000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-9, -7, -5, -3, -1],nums2 = [-9, -7, -5, -3, -1],k = 24) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-9, -7, -5, -3, -1],nums2 = [-9, -7, -5, -3, -1],k = 24) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 24999) == 2500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 24999) == 2500000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -1, -1, -1],nums2 = [-1, -1, -1, -1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -1, -1, -1],nums2 = [-1, -1, -1, -1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 100) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 100) == -15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-2, -1, 0, 1, 2],k = 8) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-2, -1, 0, 1, 2],k = 8) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -1, -1, -1],nums2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -1, -1, -1],nums2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 12) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 12) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1000, -900, -800, -700, -600],nums2 = [-1000, -900, -800, -700, -600],k = 20) == 800000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1000, -900, -800, -700, -600],nums2 = [-1000, -900, -800, -700, -600],k = 20) == 800000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-100, -50, 0, 50, 100],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-100, -50, 0, 50, 100],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-100000, -50000, -10000, -5000, -1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],k = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-100000, -50000, -10000, -5000, -1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],k = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 25) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 25) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1],nums2 = [-100, 0, 100],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1],nums2 = [-100, 0, 100],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -3, -1, 0, 1, 3, 5],nums2 = [-6, -4, -2, 0, 2, 4, 6],k = 15) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -3, -1, 0, 1, 3, 5],nums2 = [-6, -4, -2, 0, 2, 4, 6],k = 15) == -4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 441) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 441) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1000, -500, 0, 500, 1000],nums2 = [-1000, -500, 0, 500, 1000],k = 1250) == 1000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1000, -500, 0, 500, 1000],nums2 = [-1000, -500, 0, 500, 1000],k = 1250) == 1000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -3, -1, 1, 3, 5],nums2 = [-6, -4, -2, 0, 2, 4, 6],k = 15) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -3, -1, 1, 3, 5],nums2 = [-6, -4, -2, 0, 2, 4, 6],k = 15) == -4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-9, -7, -5, -3, -1],nums2 = [1, 3, 5, 7, 9],k = 10) == -27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-9, -7, -5, -3, -1],nums2 = [1, 3, 5, 7, 9],k = 10) == -27: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-5, -4, -3, -2, -1],k = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-5, -4, -3, -2, -1],k = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 45) == -36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 45) == -36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-3, -2, -1, 0, 1, 2, 3],nums2 = [-3, -2, -1, 0, 1, 2, 3],k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-3, -2, -1, 0, 1, 2, 3],nums2 = [-3, -2, -1, 0, 1, 2, 3],k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -1, -1, -1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, 1, 1, 1, 1],k = 32) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -1, -1, -1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, 1, 1, 1, 1],k = 32) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [-9, -7, -5, -3, -1],k = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [-9, -7, -5, -3, -1],k = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-50000, -40000, -30000, 0, 30000, 40000, 50000],nums2 = [-50000, 0, 50000],k = 20) == 2500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-50000, -40000, -30000, 0, 30000, 40000, 50000],nums2 = [-50000, 0, 50000],k = 20) == 2500000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-5, -4, -3, -2, -1],k = 15) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-5, -4, -3, -2, -1],k = 15) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 20) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 20) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 1, -1, 1, -1],nums2 = [-1, 1, -1, 1, -1],k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 1, -1, 1, -1],nums2 = [-1, 1, -1, 1, -1],k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-9, -6, -3, 0, 3, 6, 9],nums2 = [-9, -6, -3, 0, 3, 6, 9],k = 49) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-9, -6, -3, 0, 3, 6, 9],nums2 = [-9, -6, -3, 0, 3, 6, 9],k = 49) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-20, -15, -10, -5, 0, 5, 10, 15, 20],k = 30) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-20, -15, -10, -5, 0, 5, 10, 15, 20],k = 30) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100, -50, -25, -10, -5, -1, 0, 1, 5, 10, 25, 50, 100],nums2 = [-100, -50, -25, -10, -5, -1, 0, 1, 5, 10, 25, 50, 100],k = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100, -50, -25, -10, -5, -1, 0, 1, 5, 10, 25, 50, 100],nums2 = [-100, -50, -25, -10, -5, -1, 0, 1, 5, 10, 25, 50, 100],k = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5],k = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5],k = 25) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [-100000, 100000],nums2 = [-100000, 100000],k = 1) == -10000000000
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 4) == 0
    assert candidate(nums1 = [-100000, -50000, 0, 50000, 100000],nums2 = [-100000, -50000, 0, 50000, 100000],k = 12) == 0
    assert candidate(nums1 = [-10, -9, -8, -7, -6],nums2 = [-5, -4, -3, -2, -1],k = 1) == 6
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 25) == 90
    assert candidate(nums1 = [2, 5],nums2 = [3, 4],k = 2) == 8
    assert candidate(nums1 = [-4, -2, 0, 3],nums2 = [2, 4],k = 6) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5],k = 10) == 5
    assert candidate(nums1 = [-100000, 100000],nums2 = [-100000, 100000],k = 2) == -10000000000
    assert candidate(nums1 = [-5, -3, -1, 1, 3, 5],nums2 = [-5, -3, -1, 1, 3, 5],k = 18) == -1
    assert candidate(nums1 = [-2, -1, 0, 1, 2],nums2 = [-3, -1, 2, 4, 5],k = 3) == -6
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5],k = 25) == 25
    assert candidate(nums1 = [-10, -5, -1],nums2 = [1, 5, 10],k = 5) == -10
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6],k = 5) == 10
    assert candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0],k = 5) == 0
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 12) == 0
    assert candidate(nums1 = [-100, -50, -10, -5, 0, 5, 10, 50, 100],nums2 = [-100, -50, -10, -5, 0, 5, 10, 50, 100],k = 200) == 10001
    assert candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [-5, -4, -3, -2, -1],k = 12) == 6
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-10000, 0, 10000],k = 7) == 0
    assert candidate(nums1 = [-25, -15, -5, 5, 15, 25],nums2 = [-25, -15, -5, 0, 5, 15, 25],k = 30) == 75
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 25) == 1
    assert candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-10000, -5000, 0, 5000, 10000],k = 7) == -125000000
    assert candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-10000, -5000, 0, 5000, 10000],k = 125000) == 500000001
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1],k = 25) == -1
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 50) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 20) == 50
    assert candidate(nums1 = [-9, -3, 0, 1, 5],nums2 = [-6, -2, 1, 4, 7],k = 9) == -3
    assert candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 124999) == 2500000001
    assert candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-100, -50, 0, 50, 100],k = 10) == 0
    assert candidate(nums1 = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5],k = 49) == -2
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 24) == 72
    assert candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-200, -100, 0, 100, 200],k = 10) == 0
    assert candidate(nums1 = [-10, -5, -1, 0, 1, 5, 10],nums2 = [-20, -15, -10, -5, 0, 5, 10, 15, 20],k = 20) == -15
    assert candidate(nums1 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],nums2 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],k = 1000) == 1000001
    assert candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 1250000) == 2500000001
    assert candidate(nums1 = [-50, -25, 0, 25, 50],nums2 = [-50, -25, 0, 25, 50],k = 12) == 0
    assert candidate(nums1 = [100000],nums2 = [-100000, 0, 100000],k = 2) == 0
    assert candidate(nums1 = [-100000, 100000],nums2 = [-1, 1],k = 1) == -100000
    assert candidate(nums1 = [-1000, -900, -800],nums2 = [800, 900, 1000],k = 8) == -720000
    assert candidate(nums1 = [-100000, -50000, -10000, -5000, -1000, -500, -100, -50, -10, -5, 0, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],nums2 = [-100000, -50000, -10000, -5000, -1000, -500, -100, -50, -10, -5, 0, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],k = 1000000) == 10000000001
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [-9, -7, -5, -3, -1],k = 15) == -15
    assert candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 15) == 0
    assert candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 13) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 45) == 20
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [1, 2, 3, 4, 5],k = 20) == 1500
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums1 = [10000, 20000, 30000, 40000, 50000],nums2 = [-10000, -20000, -30000, -40000, -50000],k = 12) == -900000000
    assert candidate(nums1 = [-2, -1, 0, 1, 2],nums2 = [-2, -1, 0, 1, 2, 3, 4, 5],k = 15) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12],k = 36) == 132
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-5, -10, -15, -20, -25],k = 10) == -600
    assert candidate(nums1 = [-1000, -500, -100, 0, 100, 500, 1000],nums2 = [-1000, -500, -100, 0, 100, 500, 1000],k = 48) == 1000000
    assert candidate(nums1 = [-2, 0, 2],nums2 = [-2, 0, 2],k = 3) == 0
    assert candidate(nums1 = [-1, -1, 0, 1, 1],nums2 = [-1, -1, 0, 1, 1],k = 12) == 0
    assert candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-200, -100, 0, 100, 200],k = 50) == 20001
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 100) == 380
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 3) == 0
    assert candidate(nums1 = [10000, 20000, 30000, 40000, 50000],nums2 = [-1, -2, -3, -4, -5],k = 15) == -90000
    assert candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-100, -50, 0, 50, 100],k = 1000) == 10001
    assert candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 125000000) == 2500000001
    assert candidate(nums1 = [-10000, -5000, -1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000],nums2 = [-10000, -5000, -1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000],k = 361) == 100000000
    assert candidate(nums1 = [-1, 1],nums2 = [-100000, 100000],k = 1) == -100000
    assert candidate(nums1 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 324) == 40
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-100000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000],k = 100) == 100001
    assert candidate(nums1 = [-1, -1, -1, -1, -1],nums2 = [-1, -1, -1, -1, -1],k = 1) == 1
    assert candidate(nums1 = [-3, -2, -1, 0, 1, 2, 3],nums2 = [-3, -2, -1, 0, 1, 2, 3],k = 21) == 0
    assert candidate(nums1 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],nums2 = [-1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000],k = 22500) == 1000001
    assert candidate(nums1 = [-1, -1, -1, -1, -1],nums2 = [-1, -1, -1, -1, -1],k = 20) == 1
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-100000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000],k = 13) == 0
    assert candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 500000) == 2500000001
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 5) == 0
    assert candidate(nums1 = [-5, -3, -1, 1, 3, 5],nums2 = [-5, -3, -1, 1, 3, 5],k = 15) == -3
    assert candidate(nums1 = [-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000],nums2 = [-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000],k = 1000000) == 2500000001
    assert candidate(nums1 = [-9, -7, -5, -3, -1],nums2 = [-9, -7, -5, -3, -1],k = 24) == 63
    assert candidate(nums1 = [-50000, -25000, 0, 25000, 50000],nums2 = [-50000, -25000, 0, 25000, 50000],k = 24999) == 2500000001
    assert candidate(nums1 = [-1, -1, -1, -1],nums2 = [-1, -1, -1, -1],k = 10) == 1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 240
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-1, 0, 1],k = 4) == 0
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums1 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 100) == -15
    assert candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-2, -1, 0, 1, 2],k = 8) == -5
    assert candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 10) == 0
    assert candidate(nums1 = [-1, -1, -1, -1],nums2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 5) == 1
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10],k = 12) == 20
    assert candidate(nums1 = [-1000, -900, -800, -700, -600],nums2 = [-1000, -900, -800, -700, -600],k = 20) == 800000
    assert candidate(nums1 = [-100, -50, 0, 50, 100],nums2 = [-100, -50, 0, 50, 100],k = 12) == 0
    assert candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 12) == 0
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-100000, -50000, -10000, -5000, -1000, -500, -100, -50, -10, -5, -1, 0, 1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000],k = 50) == 5
    assert candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 25) == 100
    assert candidate(nums1 = [-1, 0, 1],nums2 = [-100, 0, 100],k = 4) == 0
    assert candidate(nums1 = [-5, -3, -1, 0, 1, 3, 5],nums2 = [-6, -4, -2, 0, 2, 4, 6],k = 15) == -4
    assert candidate(nums1 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 441) == 100
    assert candidate(nums1 = [-1000, -500, 0, 500, 1000],nums2 = [-1000, -500, 0, 500, 1000],k = 1250) == 1000001
    assert candidate(nums1 = [-5, -3, -1, 1, 3, 5],nums2 = [-6, -4, -2, 0, 2, 4, 6],k = 15) == -4
    assert candidate(nums1 = [-9, -7, -5, -3, -1],nums2 = [1, 3, 5, 7, 9],k = 10) == -27
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-5, -4, -3, -2, -1],k = 25) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 24
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 45) == -36
    assert candidate(nums1 = [-3, -2, -1, 0, 1, 2, 3],nums2 = [-3, -2, -1, 0, 1, 2, 3],k = 20) == 0
    assert candidate(nums1 = [-1, -1, -1, -1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, 1, 1, 1, 1],k = 32) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [-9, -7, -5, -3, -1],k = 25) == -1
    assert candidate(nums1 = [-50000, -40000, -30000, 0, 30000, 40000, 50000],nums2 = [-50000, 0, 50000],k = 20) == 2500000000
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-5, -4, -3, -2, -1],k = 15) == -6
    assert candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-10, -5, 0, 5, 10],k = 20) == 50
    assert candidate(nums1 = [-1, 1, -1, 1, -1],nums2 = [-1, 1, -1, 1, -1],k = 10) == -1
    assert candidate(nums1 = [-9, -6, -3, 0, 3, 6, 9],nums2 = [-9, -6, -3, 0, 3, 6, 9],k = 49) == 81
    assert candidate(nums1 = [-10, -5, 0, 5, 10],nums2 = [-20, -15, -10, -5, 0, 5, 10, 15, 20],k = 30) == 25
    assert candidate(nums1 = [-100, -50, -25, -10, -5, -1, 0, 1, 5, 10, 25, 50, 100],nums2 = [-100, -50, -25, -10, -5, -1, 0, 1, 5, 10, 25, 50, 100],k = 100) == 5
    assert candidate(nums1 = [-5, -4, -3, -2, -1],nums2 = [1, 2, 3, 4, 5],k = 25) == -1


