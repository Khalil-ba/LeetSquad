def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [100000000, 200000000],nums2 = [-300000000, -400000000],nums3 = [500000000, 600000000],nums4 = [-700000000, -800000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000000, 200000000],nums2 = [-300000000, -400000000],nums3 = [500000000, 600000000],nums4 = [-700000000, -800000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3],nums3 = [1, -1, 0],nums4 = [0, 2, -2]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3],nums3 = [1, -1, 0],nums4 = [0, 2, -2]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3],nums3 = [1, 2, 3],nums4 = [-1, -2, -3]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3],nums3 = [1, 2, 3],nums4 = [-1, -2, -3]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -2, -3],nums2 = [3, 2, 1],nums3 = [1, -2, 3],nums4 = [-3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -2, -3],nums2 = [3, 2, 1],nums3 = [1, -2, 3],nums4 = [-3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 1, 0],nums2 = [-1, 1, 0],nums3 = [-1, 1, 0],nums4 = [-1, 1, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 1, 0],nums2 = [-1, 1, 0],nums3 = [-1, 1, 0],nums4 = [-1, 1, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0],nums2 = [0],nums3 = [0],nums4 = [0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0],nums2 = [0],nums3 = [0],nums4 = [0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -1, -1, -1],nums2 = [1, 1, 1, 1],nums3 = [-1, -1, -1, -1],nums4 = [1, 1, 1, 1]) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -1, -1, -1],nums2 = [1, 1, 1, 1],nums3 = [-1, -1, -1, -1],nums4 = [1, 1, 1, 1]) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3],nums3 = [0, 1, -1],nums4 = [0, -1, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3],nums3 = [0, 1, -1],nums4 = [0, -1, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 0, -1],nums2 = [1, 0, -1],nums3 = [1, 0, -1],nums4 = [1, 0, -1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 0, -1],nums2 = [1, 0, -1],nums3 = [1, 0, -1],nums4 = [1, 0, -1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1],nums2 = [1, -1],nums3 = [1, -1],nums4 = [1, -1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1],nums2 = [1, -1],nums3 = [1, -1],nums4 = [1, -1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000000, -100000000],nums2 = [100000000, -100000000],nums3 = [100000000, -100000000],nums4 = [100000000, -100000000]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000000, -100000000],nums2 = [100000000, -100000000],nums3 = [100000000, -100000000],nums4 = [100000000, -100000000]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [-3, -2, -1],nums3 = [-1, 2, 1],nums4 = [0, 2, -2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [-3, -2, -1],nums3 = [-1, 2, 1],nums4 = [0, 2, -2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200],nums2 = [-100, -200],nums3 = [100, 200],nums4 = [-100, -200]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200],nums2 = [-100, -200],nums3 = [100, 200],nums4 = [-100, -200]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2],nums2 = [-2, -1],nums3 = [-1, 2],nums4 = [0, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2],nums2 = [-2, -1],nums3 = [-1, 2],nums4 = [0, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -1, -1],nums2 = [-1, -1, -1],nums3 = [-1, -1, -1],nums4 = [-1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -1, -1],nums2 = [-1, -1, -1],nums3 = [-1, -1, -1],nums4 = [-1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, -1],nums2 = [-1, 1, 0],nums3 = [0, -1, 1],nums4 = [1, 0, -1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, -1],nums2 = [-1, 1, 0],nums3 = [0, -1, 1],nums4 = [1, 0, -1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [-100, -200, -300, -400, -500],nums3 = [500, -500, 500, -500, 500],nums4 = [-500, 500, -500, 500, -500]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [-100, -200, -300, -400, -500],nums3 = [500, -500, 500, -500, 500],nums4 = [-500, 500, -500, 500, -500]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [1, 2, 3, 4],nums3 = [-1, -2, -3, -4],nums4 = [-1, -2, -3, -4]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [1, 2, 3, 4],nums3 = [-1, -2, -3, -4],nums4 = [-1, -2, -3, -4]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 1, -1],nums2 = [1, -1, 1, -1],nums3 = [1, -1, 1, -1],nums4 = [1, -1, 1, -1]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 1, -1],nums2 = [1, -1, 1, -1],nums3 = [1, -1, 1, -1],nums4 = [1, -1, 1, -1]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1],nums3 = [0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0]) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1],nums3 = [0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0]) == 625: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [5, 10, 15, 20],nums4 = [-5, -10, -15, -20]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [5, 10, 15, 20],nums4 = [-5, -10, -15, -20]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5],nums3 = [0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5],nums3 = [0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, 10, -10, 10],nums2 = [10, -10, 10, -10],nums3 = [5, -5, 5, -5],nums4 = [-5, 5, -5, 5]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, 10, -10, 10],nums2 = [10, -10, 10, -10],nums3 = [5, -5, 5, -5],nums4 = [-5, 5, -5, 5]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80],nums3 = [1, 2, 3, 4, 5, 6, 7, 8],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80],nums3 = [1, 2, 3, 4, 5, 6, 7, 8],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 0, 1, 2],nums2 = [1, -1, 2, -2],nums3 = [2, 1, -1, -2],nums4 = [-2, 2, -1, 1]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 0, 1, 2],nums2 = [1, -1, 2, -2],nums3 = [2, 1, -1, -2],nums4 = [-2, 2, -1, 1]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0],nums3 = [0, 0, 0, 0],nums4 = [0, 0, 0, 0]) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0],nums3 = [0, 0, 0, 0],nums4 = [0, 0, 0, 0]) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [-100, -200, -300, -400],nums3 = [1, 2, 3, 4],nums4 = [-1, -2, -3, -4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [-100, -200, -300, -400],nums3 = [1, 2, 3, 4],nums4 = [-1, -2, -3, -4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [-1, -1, -1, -1],nums3 = [1, 1, 1, 1],nums4 = [-1, -1, -1, -1]) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [-1, -1, -1, -1],nums3 = [1, 1, 1, 1],nums4 = [-1, -1, -1, -1]) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],nums3 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums4 = [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],nums3 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums4 = [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [-100, -200, -300, -400],nums3 = [50, 100, 150, 200],nums4 = [-50, -100, -150, -200]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [-100, -200, -300, -400],nums3 = [50, 100, 150, 200],nums4 = [-50, -100, -150, -200]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [-100, -200, -300, -400],nums3 = [50, 150, 250, 350],nums4 = [-50, -150, -250, -350]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [-100, -200, -300, -400],nums3 = [50, 150, 250, 350],nums4 = [-50, -150, -250, -350]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [-400, -300, -200, -100],nums3 = [50, 150, 250, 350],nums4 = [-350, -250, -150, -50]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [-400, -300, -200, -100],nums3 = [50, 150, 250, 350],nums4 = [-350, -250, -150, -50]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 0, -1, -2],nums2 = [2, -2, 1, 0],nums3 = [-1, 0, 1, 2],nums4 = [1, -1, -2, 2]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 0, -1, -2],nums2 = [2, -2, 1, 0],nums3 = [-1, 0, 1, 2],nums4 = [1, -1, -2, 2]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [-10, -20, -30, -40],nums3 = [10, 20, 30, 40],nums4 = [5, 15, 25, 35]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [-10, -20, -30, -40],nums3 = [10, 20, 30, 40],nums4 = [5, 15, 25, 35]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],nums3 = [0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0]) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],nums3 = [0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0]) == 625: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5],nums3 = [1, 2, 3, 4, 5],nums4 = [-1, -2, -3, -4, -5]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5],nums3 = [1, 2, 3, 4, 5],nums4 = [-1, -2, -3, -4, -5]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1],nums3 = [-1, -2, -3, -4, -5],nums4 = [-5, -4, -3, -2, -1]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1],nums3 = [-1, -2, -3, -4, -5],nums4 = [-5, -4, -3, -2, -1]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [-1, -2, -3, -4],nums3 = [0, 0, 0, 0],nums4 = [0, 0, 0, 0]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [-1, -2, -3, -4],nums3 = [0, 0, 0, 0],nums4 = [0, 0, 0, 0]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [10, -10, 20, -20],nums4 = [-10, 10, -20, 20]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [10, -10, 20, -20],nums4 = [-10, 10, -20, 20]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [-1, -2, -3, -4],nums3 = [1, -1, 1, -1],nums4 = [2, -2, 2, -2]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [-1, -2, -3, -4],nums3 = [1, -1, 1, -1],nums4 = [2, -2, 2, -2]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [25, -25, 50, -50],nums2 = [30, -30, 60, -60],nums3 = [10, -10, 20, -20],nums4 = [15, -15, 30, -30]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [25, -25, 50, -50],nums2 = [30, -30, 60, -60],nums3 = [10, -10, 20, -20],nums4 = [15, -15, 30, -30]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -2, 3, -4],nums2 = [4, -3, 2, -1],nums3 = [-1, 2, -3, 4],nums4 = [1, -2, 3, -4]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -2, 3, -4],nums2 = [4, -3, 2, -1],nums3 = [-1, 2, -3, 4],nums4 = [1, -2, 3, -4]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000000, -100000000, 200000000, -200000000],nums2 = [50000000, -50000000, 150000000, -150000000],nums3 = [25000000, -25000000, 75000000, -75000000],nums4 = [12500000, -12500000, 37500000, -37500000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000000, -100000000, 200000000, -200000000],nums2 = [50000000, -50000000, 150000000, -150000000],nums3 = [25000000, -25000000, 75000000, -75000000],nums4 = [12500000, -12500000, 37500000, -37500000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [2, 2, 2, 2],nums3 = [-3, -3, -3, -3],nums4 = [4, 4, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [2, 2, 2, 2],nums3 = [-3, -3, -3, -3],nums4 = [4, 4, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 2, -2, 3, -3],nums2 = [-3, 3, -2, 2, -1, 1],nums3 = [2, -2, 1, -1, 3, -3],nums4 = [-3, 3, 2, -2, 1, -1]) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 2, -2, 3, -3],nums2 = [-3, 3, -2, 2, -1, 1],nums3 = [2, -2, 1, -1, 3, -3],nums4 = [-3, 3, 2, -2, 1, -1]) == 122: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, -10, 20, -20],nums2 = [1, -1, 2, -2],nums3 = [3, -3, 4, -4],nums4 = [-4, 4, -3, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, -10, 20, -20],nums2 = [1, -1, 2, -2],nums3 = [3, -3, 4, -4],nums4 = [-4, 4, -3, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123, -123, 246, -246],nums2 = [369, -369, 738, -738],nums3 = [456, -456, 912, -912],nums4 = [-912, -456, 456, 912]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123, -123, 246, -246],nums2 = [369, -369, 738, -738],nums3 = [456, -456, 912, -912],nums4 = [-912, -456, 456, 912]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, -100, 200, -200],nums2 = [150, -150, 250, -250],nums3 = [200, -200, 300, -300],nums4 = [250, -250, 350, -350]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, -100, 200, -200],nums2 = [150, -150, 250, -250],nums3 = [200, -200, 300, -300],nums4 = [250, -250, 350, -350]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [-1, -2, -3, -4, -5, -6],nums3 = [1, -1, 2, -2, 3, -3],nums4 = [-1, 1, -2, 2, -3, 3]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [-1, -2, -3, -4, -5, -6],nums3 = [1, -1, 2, -2, 3, -3],nums4 = [-1, 1, -2, 2, -3, 3]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-5, -4, -3, -2, -1],nums3 = [1, 1, 1, 1, 1],nums4 = [-1, -1, -1, -1, -1]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-5, -4, -3, -2, -1],nums3 = [1, 1, 1, 1, 1],nums4 = [-1, -1, -1, -1, -1]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5],nums3 = [5, -5, 5, -5, 5],nums4 = [-5, 5, -5, 5, -5]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5],nums3 = [5, -5, 5, -5, 5],nums4 = [-5, 5, -5, 5, -5]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 2, -2],nums2 = [1, -1, 2, -2],nums3 = [1, -1, 2, -2],nums4 = [1, -1, 2, -2]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 2, -2],nums2 = [1, -1, 2, -2],nums3 = [1, -1, 2, -2],nums4 = [1, -1, 2, -2]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [5, 15, 25, 35],nums4 = [-5, -15, -25, -35]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [5, 15, 25, 35],nums4 = [-5, -15, -25, -35]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [-500, -400, -300, -200, -100],nums3 = [50, 150, 250, 350, 450],nums4 = [-450, -350, -250, -150, -50]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [-500, -400, -300, -200, -100],nums3 = [50, 150, 250, 350, 450],nums4 = [-450, -350, -250, -150, -50]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, -7, 14, -14],nums2 = [21, -21, 42, -42],nums3 = [6, -6, 12, -12],nums4 = [28, -28, 56, -56]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, -7, 14, -14],nums2 = [21, -21, 42, -42],nums3 = [6, -6, 12, -12],nums4 = [28, -28, 56, -56]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, -10, 20, -20],nums2 = [5, -5, 15, -15],nums3 = [3, -3, 12, -12],nums4 = [8, -8, 17, -17]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, -10, 20, -20],nums2 = [5, -5, 15, -15],nums3 = [3, -3, 12, -12],nums4 = [8, -8, 17, -17]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],nums3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums4 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],nums3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums4 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 1, -1],nums2 = [2, -2, 2, -2],nums3 = [3, -3, 3, -3],nums4 = [4, -4, 4, -4]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 1, -1],nums2 = [2, -2, 2, -2],nums3 = [3, -3, 3, -3],nums4 = [4, -4, 4, -4]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 1, -1, 1, -1, 1, -1],nums2 = [1, -1, 1, -1, 1, -1, 1, -1],nums3 = [1, -1, 1, -1, 1, -1, 1, -1],nums4 = [1, -1, 1, -1, 1, -1, 1, -1]) == 1536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 1, -1, 1, -1, 1, -1],nums2 = [1, -1, 1, -1, 1, -1, 1, -1],nums3 = [1, -1, 1, -1, 1, -1, 1, -1],nums4 = [1, -1, 1, -1, 1, -1, 1, -1]) == 1536: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0],nums3 = [0, 0, 0, 0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0, 0, 0, 0]) == 4096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0],nums3 = [0, 0, 0, 0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0, 0, 0, 0]) == 4096: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [5, 6, 7, 8],nums3 = [-1, -2, -3, -4],nums4 = [-5, -6, -7, -8]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [5, 6, 7, 8],nums3 = [-1, -2, -3, -4],nums4 = [-5, -6, -7, -8]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -9, -8, -7],nums2 = [7, 8, 9, 10],nums3 = [-5, 5, -5, 5],nums4 = [5, -5, 5, -5]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -9, -8, -7],nums2 = [7, 8, 9, 10],nums3 = [-5, 5, -5, 5],nums4 = [5, -5, 5, -5]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [-4, -3, -2, -1],nums3 = [1, 2, 3, 4],nums4 = [-4, -3, -2, -1]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [-4, -3, -2, -1],nums3 = [1, 2, 3, 4],nums4 = [-4, -3, -2, -1]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, -2, -3, -4],nums2 = [1, 2, 3, 4],nums3 = [-1, -2, -3, -4],nums4 = [1, 2, 3, 4]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, -2, -3, -4],nums2 = [1, 2, 3, 4],nums3 = [-1, -2, -3, -4],nums4 = [1, 2, 3, 4]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],nums3 = [-2, -2, -2, -2],nums4 = [-2, -2, -2, -2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],nums3 = [-2, -2, -2, -2],nums4 = [-2, -2, -2, -2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000000, 100000000, 100000000, 100000000],nums2 = [-250000000, 0, 250000000, 0],nums3 = [125000000, -125000000, 125000000, -125000000],nums4 = [-125000000, 125000000, -125000000, 125000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000000, 100000000, 100000000, 100000000],nums2 = [-250000000, 0, 250000000, 0],nums3 = [125000000, -125000000, 125000000, -125000000],nums4 = [-125000000, 125000000, -125000000, 125000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -1, 2, -2],nums2 = [2, -2, 1, -1],nums3 = [3, -3, 4, -4],nums4 = [-4, 4, -3, 3]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -1, 2, -2],nums2 = [2, -2, 1, -1],nums3 = [3, -3, 4, -4],nums4 = [-4, 4, -3, 3]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20],nums2 = [-20, -15, -10, -5],nums3 = [25, 30, 35, 40],nums4 = [-40, -35, -30, -25]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20],nums2 = [-20, -15, -10, -5],nums3 = [25, 30, 35, 40],nums4 = [-40, -35, -30, -25]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-10, -20, -30, -40, -50],nums3 = [5, 10, 15, 20, 25],nums4 = [-5, -10, -15, -20, -25]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-10, -20, -30, -40, -50],nums3 = [5, 10, 15, 20, 25],nums4 = [-5, -10, -15, -20, -25]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0],nums3 = [0, 0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0, 0]) == 1296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0],nums3 = [0, 0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0, 0]) == 1296: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, -6],nums2 = [-2, -3, 4, 1],nums3 = [0, 0, 0, 0],nums4 = [5, -5, 5, -5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, -6],nums2 = [-2, -3, 4, 1],nums3 = [0, 0, 0, 0],nums4 = [5, -5, 5, -5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [-1, -2, -3, -4],nums3 = [1, -1, 1, -1],nums4 = [-1, 1, -1, 1]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [-1, -2, -3, -4],nums3 = [1, -1, 1, -1],nums4 = [-1, 1, -1, 1]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-10, -20, -30, -40],nums2 = [10, 20, 30, 40],nums3 = [5, 15, 25, 35],nums4 = [-5, -15, -25, -35]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-10, -20, -30, -40],nums2 = [10, 20, 30, 40],nums3 = [5, 15, 25, 35],nums4 = [-5, -15, -25, -35]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],nums3 = [-2, -2, -2, -2],nums4 = [2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],nums3 = [-2, -2, -2, -2],nums4 = [2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, -2, 3, 4],nums2 = [-3, 2, 1, -1],nums3 = [2, -1, -3, 4],nums4 = [-4, 1, 2, 3]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, -2, 3, 4],nums2 = [-3, 2, 1, -1],nums3 = [2, -1, -3, 4],nums4 = [-4, 1, 2, 3]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-1, 1, -2, 2],nums2 = [-1, 1, -2, 2],nums3 = [-1, 1, -2, 2],nums4 = [-1, 1, -2, 2]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-1, 1, -2, 2],nums2 = [-1, 1, -2, 2],nums3 = [-1, 1, -2, 2],nums4 = [-1, 1, -2, 2]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-100000000, 100000000, -200000000, 200000000],nums2 = [200000000, -200000000, 100000000, -100000000],nums3 = [-50000000, 50000000, -50000000, 50000000],nums4 = [50000000, -50000000, 50000000, -50000000]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-100000000, 100000000, -200000000, 200000000],nums2 = [200000000, -200000000, 100000000, -100000000],nums3 = [-50000000, 50000000, -50000000, 50000000],nums4 = [50000000, -50000000, 50000000, -50000000]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [-23456789, 23456789, -98765432, 98765432],nums2 = [-45678912, 45678912, -87654321, 87654321],nums3 = [56789123, -56789123, 43210987, -43210987],nums4 = [-67891234, 67891234, -32109876, 32109876]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [-23456789, 23456789, -98765432, 98765432],nums2 = [-45678912, 45678912, -87654321, 87654321],nums3 = [56789123, -56789123, 43210987, -43210987],nums4 = [-67891234, 67891234, -32109876, 32109876]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7],nums2 = [-7, -6, -5, -4, -3, -2, -1],nums3 = [1, 2, 3, 4, 5, 6, 7],nums4 = [-7, -6, -5, -4, -3, -2, -1]) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7],nums2 = [-7, -6, -5, -4, -3, -2, -1],nums3 = [1, 2, 3, 4, 5, 6, 7],nums4 = [-7, -6, -5, -4, -3, -2, -1]) == 231: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, -100, 200, -200],nums2 = [300, -300, 600, -600],nums3 = [100, -100, 200, -200],nums4 = [200, -200, 400, -400]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, -100, 200, -200],nums2 = [300, -300, 600, -600],nums3 = [100, -100, 200, -200],nums4 = [200, -200, 400, -400]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [1, 2, 3, 4],nums3 = [1, 2, 3, 4],nums4 = [-8, 8, -8, 8]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [1, 2, 3, 4],nums3 = [1, 2, 3, 4],nums4 = [-8, 8, -8, 8]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, -4, 3, 2],nums2 = [-2, 6, -1, 0],nums3 = [1, -3, 4, -5],nums4 = [0, 1, -1, 2]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, -4, 3, 2],nums2 = [-2, 6, -1, 0],nums3 = [1, -3, 4, -5],nums4 = [0, 1, -1, 2]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [150, 100, 50, 0],nums2 = [-50, -100, -150, -200],nums3 = [250, 200, 150, 100],nums4 = [-100, -150, -200, -250]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [150, 100, 50, 0],nums2 = [-50, -100, -150, -200],nums3 = [250, 200, 150, 100],nums4 = [-100, -150, -200, -250]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000000, -100000000, 50000000, -50000000],nums2 = [100000000, -100000000, 50000000, -50000000],nums3 = [100000000, -100000000, 50000000, -50000000],nums4 = [100000000, -100000000, 50000000, -50000000]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000000, -100000000, 50000000, -50000000],nums2 = [100000000, -100000000, 50000000, -50000000],nums3 = [100000000, -100000000, 50000000, -50000000],nums4 = [100000000, -100000000, 50000000, -50000000]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],nums3 = [-1, -1, -1, -1],nums4 = [-1, -1, -1, -1]) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],nums3 = [-1, -1, -1, -1],nums4 = [-1, -1, -1, -1]) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [1, 2, 3, 4],nums4 = [-1, -2, -3, -4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [1, 2, 3, 4],nums4 = [-1, -2, -3, -4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [-5, -5, -5, -5],nums3 = [10, 10, 10, 10],nums4 = [-10, -10, -10, -10]) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [-5, -5, -5, -5],nums3 = [10, 10, 10, 10],nums4 = [-10, -10, -10, -10]) == 256: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8],nums2 = [-1, -2, -3, -4, -5, -6, -7, -8],nums3 = [1, 2, 3, 4, 5, 6, 7, 8],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8]) == 344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8],nums2 = [-1, -2, -3, -4, -5, -6, -7, -8],nums3 = [1, 2, 3, 4, 5, 6, 7, 8],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8]) == 344: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, -10, 20, -20],nums2 = [-10, 10, -20, 20],nums3 = [30, -30, 40, -40],nums4 = [-40, 40, -30, 30]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, -10, 20, -20],nums2 = [-10, 10, -20, 20],nums3 = [30, -30, 40, -40],nums4 = [-40, 40, -30, 30]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [-4, -3, -2, -1],nums3 = [0, 0, 0, 0],nums4 = [1, 1, 1, 1]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [-4, -3, -2, -1],nums3 = [0, 0, 0, 0],nums4 = [1, 1, 1, 1]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, -5, 5, -5],nums2 = [5, -5, 5, -5],nums3 = [5, -5, 5, -5],nums4 = [5, -5, 5, -5]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, -5, 5, -5],nums2 = [5, -5, 5, -5],nums3 = [5, -5, 5, -5],nums4 = [5, -5, 5, -5]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [-6, -5, -4, -3, -2, -1],nums3 = [0, 0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0, 0]) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [-6, -5, -4, -3, -2, -1],nums3 = [0, 0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0, 0]) == 216: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [-40, -30, -20, -10],nums3 = [5, 15, 25, 35],nums4 = [-35, -25, -15, -5]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [-40, -30, -20, -10],nums3 = [5, 15, 25, 35],nums4 = [-35, -25, -15, -5]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8],nums2 = [-8, -7, -6, -5, -4, -3, -2, -1],nums3 = [8, 7, 6, 5, 4, 3, 2, 1],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8]) == 344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8],nums2 = [-8, -7, -6, -5, -4, -3, -2, -1],nums3 = [8, 7, 6, 5, 4, 3, 2, 1],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8]) == 344: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, -4, 1],nums2 = [-1, 4, -2, 6],nums3 = [-3, 5, 2, -7],nums4 = [1, 2, -4, -3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, -4, 1],nums2 = [-1, 4, -2, 6],nums3 = [-3, 5, 2, -7],nums4 = [1, 2, -4, -3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, -5, 10, -10],nums2 = [5, -5, 10, -10],nums3 = [5, -5, 10, -10],nums4 = [5, -5, 10, -10]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, -5, 10, -10],nums2 = [5, -5, 10, -10],nums3 = [5, -5, 10, -10],nums4 = [5, -5, 10, -10]) == 36: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [100000000, 200000000],nums2 = [-300000000, -400000000],nums3 = [500000000, 600000000],nums4 = [-700000000, -800000000]) == 0
    assert candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3],nums3 = [1, -1, 0],nums4 = [0, 2, -2]) == 13
    assert candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3],nums3 = [1, 2, 3],nums4 = [-1, -2, -3]) == 19
    assert candidate(nums1 = [-1, -2, -3],nums2 = [3, 2, 1],nums3 = [1, -2, 3],nums4 = [-3, 2, 1]) == 10
    assert candidate(nums1 = [-1, 1, 0],nums2 = [-1, 1, 0],nums3 = [-1, 1, 0],nums4 = [-1, 1, 0]) == 19
    assert candidate(nums1 = [0],nums2 = [0],nums3 = [0],nums4 = [0]) == 1
    assert candidate(nums1 = [-1, -1, -1, -1],nums2 = [1, 1, 1, 1],nums3 = [-1, -1, -1, -1],nums4 = [1, 1, 1, 1]) == 256
    assert candidate(nums1 = [1, 2, 3],nums2 = [-1, -2, -3],nums3 = [0, 1, -1],nums4 = [0, -1, 1]) == 19
    assert candidate(nums1 = [1, 0, -1],nums2 = [1, 0, -1],nums3 = [1, 0, -1],nums4 = [1, 0, -1]) == 19
    assert candidate(nums1 = [1, -1],nums2 = [1, -1],nums3 = [1, -1],nums4 = [1, -1]) == 6
    assert candidate(nums1 = [100000000, -100000000],nums2 = [100000000, -100000000],nums3 = [100000000, -100000000],nums4 = [100000000, -100000000]) == 6
    assert candidate(nums1 = [1, 2, 3],nums2 = [-3, -2, -1],nums3 = [-1, 2, 1],nums4 = [0, 2, -2]) == 12
    assert candidate(nums1 = [100, 200],nums2 = [-100, -200],nums3 = [100, 200],nums4 = [-100, -200]) == 6
    assert candidate(nums1 = [1, 2],nums2 = [-2, -1],nums3 = [-1, 2],nums4 = [0, 2]) == 2
    assert candidate(nums1 = [-1, -1, -1],nums2 = [-1, -1, -1],nums3 = [-1, -1, -1],nums4 = [-1, -1, -1]) == 0
    assert candidate(nums1 = [0, 1, -1],nums2 = [-1, 1, 0],nums3 = [0, -1, 1],nums4 = [1, 0, -1]) == 19
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [-100, -200, -300, -400, -500],nums3 = [500, -500, 500, -500, 500],nums4 = [-500, 500, -500, 500, -500]) == 65
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [1, 2, 3, 4],nums3 = [-1, -2, -3, -4],nums4 = [-1, -2, -3, -4]) == 44
    assert candidate(nums1 = [1, -1, 1, -1],nums2 = [1, -1, 1, -1],nums3 = [1, -1, 1, -1],nums4 = [1, -1, 1, -1]) == 96
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1],nums3 = [0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0]) == 625
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [5, 10, 15, 20],nums4 = [-5, -10, -15, -20]) == 28
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5],nums3 = [0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0]) == 125
    assert candidate(nums1 = [-10, 10, -10, 10],nums2 = [10, -10, 10, -10],nums3 = [5, -5, 5, -5],nums4 = [-5, 5, -5, 5]) == 64
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80],nums3 = [1, 2, 3, 4, 5, 6, 7, 8],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8]) == 64
    assert candidate(nums1 = [-1, 0, 1, 2],nums2 = [1, -1, 2, -2],nums3 = [2, 1, -1, -2],nums4 = [-2, 2, -1, 1]) == 33
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0],nums3 = [0, 0, 0, 0],nums4 = [0, 0, 0, 0]) == 256
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [-100, -200, -300, -400],nums3 = [1, 2, 3, 4],nums4 = [-1, -2, -3, -4]) == 16
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [-1, -1, -1, -1],nums3 = [1, 1, 1, 1],nums4 = [-1, -1, -1, -1]) == 256
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],nums3 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums4 = [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2]) == 10000
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [-100, -200, -300, -400],nums3 = [50, 100, 150, 200],nums4 = [-50, -100, -150, -200]) == 28
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [-100, -200, -300, -400],nums3 = [50, 150, 250, 350],nums4 = [-50, -150, -250, -350]) == 44
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [-400, -300, -200, -100],nums3 = [50, 150, 250, 350],nums4 = [-350, -250, -150, -50]) == 44
    assert candidate(nums1 = [1, 0, -1, -2],nums2 = [2, -2, 1, 0],nums3 = [-1, 0, 1, 2],nums4 = [1, -1, -2, 2]) == 36
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [-10, -20, -30, -40],nums3 = [10, 20, 30, 40],nums4 = [5, 15, 25, 35]) == 0
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0],nums3 = [0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0]) == 625
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5],nums3 = [1, 2, 3, 4, 5],nums4 = [-1, -2, -3, -4, -5]) == 85
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1],nums3 = [-1, -2, -3, -4, -5],nums4 = [-5, -4, -3, -2, -1]) == 85
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [-1, -2, -3, -4],nums3 = [0, 0, 0, 0],nums4 = [0, 0, 0, 0]) == 64
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [10, -10, 20, -20],nums4 = [-10, 10, -20, 20]) == 36
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [-1, -2, -3, -4],nums3 = [1, -1, 1, -1],nums4 = [2, -2, 2, -2]) == 32
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 100
    assert candidate(nums1 = [25, -25, 50, -50],nums2 = [30, -30, 60, -60],nums3 = [10, -10, 20, -20],nums4 = [15, -15, 30, -30]) == 10
    assert candidate(nums1 = [1, -2, 3, -4],nums2 = [4, -3, 2, -1],nums3 = [-1, 2, -3, 4],nums4 = [1, -2, 3, -4]) == 36
    assert candidate(nums1 = [100000000, -100000000, 200000000, -200000000],nums2 = [50000000, -50000000, 150000000, -150000000],nums3 = [25000000, -25000000, 75000000, -75000000],nums4 = [12500000, -12500000, 37500000, -37500000]) == 0
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [2, 2, 2, 2],nums3 = [-3, -3, -3, -3],nums4 = [4, 4, 4, 4]) == 0
    assert candidate(nums1 = [1, -1, 2, -2, 3, -3],nums2 = [-3, 3, -2, 2, -1, 1],nums3 = [2, -2, 1, -1, 3, -3],nums4 = [-3, 3, 2, -2, 1, -1]) == 122
    assert candidate(nums1 = [10, -10, 20, -20],nums2 = [1, -1, 2, -2],nums3 = [3, -3, 4, -4],nums4 = [-4, 4, -3, 3]) == 2
    assert candidate(nums1 = [123, -123, 246, -246],nums2 = [369, -369, 738, -738],nums3 = [456, -456, 912, -912],nums4 = [-912, -456, 456, 912]) == 0
    assert candidate(nums1 = [100, -100, 200, -200],nums2 = [150, -150, 250, -250],nums3 = [200, -200, 300, -300],nums4 = [250, -250, 350, -350]) == 22
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [-1, -2, -3, -4, -5, -6],nums3 = [1, -1, 2, -2, 3, -3],nums4 = [-1, 1, -2, 2, -3, 3]) == 128
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-5, -4, -3, -2, -1],nums3 = [1, 1, 1, 1, 1],nums4 = [-1, -1, -1, -1, -1]) == 125
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [-1, -2, -3, -4, -5],nums3 = [5, -5, 5, -5, 5],nums4 = [-5, 5, -5, 5, -5]) == 65
    assert candidate(nums1 = [1, -1, 2, -2],nums2 = [1, -1, 2, -2],nums3 = [1, -1, 2, -2],nums4 = [1, -1, 2, -2]) == 36
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [5, 15, 25, 35],nums4 = [-5, -15, -25, -35]) == 44
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [-500, -400, -300, -200, -100],nums3 = [50, 150, 250, 350, 450],nums4 = [-450, -350, -250, -150, -50]) == 85
    assert candidate(nums1 = [7, -7, 14, -14],nums2 = [21, -21, 42, -42],nums3 = [6, -6, 12, -12],nums4 = [28, -28, 56, -56]) == 0
    assert candidate(nums1 = [10, -10, 20, -20],nums2 = [5, -5, 15, -15],nums3 = [3, -3, 12, -12],nums4 = [8, -8, 17, -17]) == 12
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],nums3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums4 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1000
    assert candidate(nums1 = [1, -1, 1, -1],nums2 = [2, -2, 2, -2],nums3 = [3, -3, 3, -3],nums4 = [4, -4, 4, -4]) == 32
    assert candidate(nums1 = [1, -1, 1, -1, 1, -1, 1, -1],nums2 = [1, -1, 1, -1, 1, -1, 1, -1],nums3 = [1, -1, 1, -1, 1, -1, 1, -1],nums4 = [1, -1, 1, -1, 1, -1, 1, -1]) == 1536
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0, 0, 0],nums3 = [0, 0, 0, 0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0, 0, 0, 0]) == 4096
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [5, 6, 7, 8],nums3 = [-1, -2, -3, -4],nums4 = [-5, -6, -7, -8]) == 44
    assert candidate(nums1 = [-10, -9, -8, -7],nums2 = [7, 8, 9, 10],nums3 = [-5, 5, -5, 5],nums4 = [5, -5, 5, -5]) == 32
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [-4, -3, -2, -1],nums3 = [1, 2, 3, 4],nums4 = [-4, -3, -2, -1]) == 44
    assert candidate(nums1 = [-1, -2, -3, -4],nums2 = [1, 2, 3, 4],nums3 = [-1, -2, -3, -4],nums4 = [1, 2, 3, 4]) == 44
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],nums3 = [-2, -2, -2, -2],nums4 = [-2, -2, -2, -2]) == 0
    assert candidate(nums1 = [100000000, 100000000, 100000000, 100000000],nums2 = [-250000000, 0, 250000000, 0],nums3 = [125000000, -125000000, 125000000, -125000000],nums4 = [-125000000, 125000000, -125000000, 125000000]) == 0
    assert candidate(nums1 = [1, -1, 2, -2],nums2 = [2, -2, 1, -1],nums3 = [3, -3, 4, -4],nums4 = [-4, 4, -3, 3]) == 24
    assert candidate(nums1 = [5, 10, 15, 20],nums2 = [-20, -15, -10, -5],nums3 = [25, 30, 35, 40],nums4 = [-40, -35, -30, -25]) == 44
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [-10, -20, -30, -40, -50],nums3 = [5, 10, 15, 20, 25],nums4 = [-5, -10, -15, -20, -25]) == 55
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0, 0, 0, 0],nums3 = [0, 0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0, 0]) == 1296
    assert candidate(nums1 = [1, 2, 3, -6],nums2 = [-2, -3, 4, 1],nums3 = [0, 0, 0, 0],nums4 = [5, -5, 5, -5]) == 16
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [-1, -2, -3, -4],nums3 = [1, -1, 1, -1],nums4 = [-1, 1, -1, 1]) == 48
    assert candidate(nums1 = [-10, -20, -30, -40],nums2 = [10, 20, 30, 40],nums3 = [5, 15, 25, 35],nums4 = [-5, -15, -25, -35]) == 44
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],nums3 = [-2, -2, -2, -2],nums4 = [2, 2, 2, 2]) == 0
    assert candidate(nums1 = [1, -2, 3, 4],nums2 = [-3, 2, 1, -1],nums3 = [2, -1, -3, 4],nums4 = [-4, 1, 2, 3]) == 21
    assert candidate(nums1 = [-1, 1, -2, 2],nums2 = [-1, 1, -2, 2],nums3 = [-1, 1, -2, 2],nums4 = [-1, 1, -2, 2]) == 36
    assert candidate(nums1 = [-100000000, 100000000, -200000000, 200000000],nums2 = [200000000, -200000000, 100000000, -100000000],nums3 = [-50000000, 50000000, -50000000, 50000000],nums4 = [50000000, -50000000, 50000000, -50000000]) == 48
    assert candidate(nums1 = [-23456789, 23456789, -98765432, 98765432],nums2 = [-45678912, 45678912, -87654321, 87654321],nums3 = [56789123, -56789123, 43210987, -43210987],nums4 = [-67891234, 67891234, -32109876, 32109876]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7],nums2 = [-7, -6, -5, -4, -3, -2, -1],nums3 = [1, 2, 3, 4, 5, 6, 7],nums4 = [-7, -6, -5, -4, -3, -2, -1]) == 231
    assert candidate(nums1 = [100, -100, 200, -200],nums2 = [300, -300, 600, -600],nums3 = [100, -100, 200, -200],nums4 = [200, -200, 400, -400]) == 12
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [1, 2, 3, 4],nums3 = [1, 2, 3, 4],nums4 = [-8, 8, -8, 8]) == 24
    assert candidate(nums1 = [5, -4, 3, 2],nums2 = [-2, 6, -1, 0],nums3 = [1, -3, 4, -5],nums4 = [0, 1, -1, 2]) == 16
    assert candidate(nums1 = [150, 100, 50, 0],nums2 = [-50, -100, -150, -200],nums3 = [250, 200, 150, 100],nums4 = [-100, -150, -200, -250]) == 40
    assert candidate(nums1 = [100000000, -100000000, 50000000, -50000000],nums2 = [100000000, -100000000, 50000000, -50000000],nums3 = [100000000, -100000000, 50000000, -50000000],nums4 = [100000000, -100000000, 50000000, -50000000]) == 36
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1],nums3 = [-1, -1, -1, -1],nums4 = [-1, -1, -1, -1]) == 256
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [-10, -20, -30, -40],nums3 = [1, 2, 3, 4],nums4 = [-1, -2, -3, -4]) == 16
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [-5, -5, -5, -5],nums3 = [10, 10, 10, 10],nums4 = [-10, -10, -10, -10]) == 256
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8],nums2 = [-1, -2, -3, -4, -5, -6, -7, -8],nums3 = [1, 2, 3, 4, 5, 6, 7, 8],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8]) == 344
    assert candidate(nums1 = [10, -10, 20, -20],nums2 = [-10, 10, -20, 20],nums3 = [30, -30, 40, -40],nums4 = [-40, 40, -30, 30]) == 24
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [-4, -3, -2, -1],nums3 = [0, 0, 0, 0],nums4 = [1, 1, 1, 1]) == 48
    assert candidate(nums1 = [5, -5, 5, -5],nums2 = [5, -5, 5, -5],nums3 = [5, -5, 5, -5],nums4 = [5, -5, 5, -5]) == 96
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [-6, -5, -4, -3, -2, -1],nums3 = [0, 0, 0, 0, 0, 0],nums4 = [0, 0, 0, 0, 0, 0]) == 216
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [-40, -30, -20, -10],nums3 = [5, 15, 25, 35],nums4 = [-35, -25, -15, -5]) == 44
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8],nums2 = [-8, -7, -6, -5, -4, -3, -2, -1],nums3 = [8, 7, 6, 5, 4, 3, 2, 1],nums4 = [-1, -2, -3, -4, -5, -6, -7, -8]) == 344
    assert candidate(nums1 = [5, 3, -4, 1],nums2 = [-1, 4, -2, 6],nums3 = [-3, 5, 2, -7],nums4 = [1, 2, -4, -3]) == 12
    assert candidate(nums1 = [5, -5, 10, -10],nums2 = [5, -5, 10, -10],nums3 = [5, -5, 10, -10],nums4 = [5, -5, 10, -10]) == 36


