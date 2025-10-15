def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [20, 30, 40]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [20, 30, 40]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [12, 22, 32]) == -18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [12, 22, 32]) == -18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [7, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [7, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 20, 20, 30],nums2 = [15, 25]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 20, 20, 30],nums2 = [15, 25]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 20, 16, 12, 8],nums2 = [14, 18, 10]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 20, 16, 12, 8],nums2 = [14, 18, 10]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40],nums2 = [10, 18]) == -14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40],nums2 = [10, 18]) == -14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [10, 20]) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [10, 20]) == -15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [15, 25]) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [15, 25]) == -15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5],nums2 = [7, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5],nums2 = [7, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [4, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [4, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [150, 250, 350]) == -150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [150, 250, 350]) == -150: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 5, 3],nums2 = [7, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 5, 3],nums2 = [7, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [150, 250]) == -150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [150, 250]) == -150: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 7, 5, 3, 1, -1, -3, -5, -7, -9],nums2 = [5, 3, 1, -1, -3, -5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 7, 5, 3, 1, -1, -3, -5, -7, -9],nums2 = [5, 3, 1, -1, -3, -5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12],nums2 = [6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12],nums2 = [6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4],nums2 = [2, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4],nums2 = [2, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],nums2 = [150, 200, 250]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],nums2 = [150, 200, 250]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],nums2 = [12, 14, 16, 18, 20, 22, 24, 26]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],nums2 = [12, 14, 16, 18, 20, 22, 24, 26]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 25, 35, 45, 55, 65, 75],nums2 = [25, 35, 45, 55, 65]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 25, 35, 45, 55, 65, 75],nums2 = [25, 35, 45, 55, 65]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45, 54],nums2 = [12, 21, 30]) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45, 54],nums2 = [12, 21, 30]) == -15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [10, 15, 20]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [10, 15, 20]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 8, 12, 16, 20, 24],nums2 = [8, 16, 24]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 8, 12, 16, 20, 24],nums2 = [8, 16, 24]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [3, 4, 5, 6, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [3, 4, 5, 6, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35],nums2 = [10, 15, 20]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35],nums2 = [10, 15, 20]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [110, 210, 310, 410]) == -190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [110, 210, 310, 410]) == -190: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],nums2 = [6, 7, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],nums2 = [6, 7, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [7, 7, 7, 7, 7, 7, 7, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [7, 7, 7, 7, 7, 7, 7, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [200, 300, 400]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [200, 300, 400]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15, 18],nums2 = [6, 12, 18]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15, 18],nums2 = [6, 12, 18]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [2, 3, 4, 5, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [2, 3, 4, 5, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 24, 36, 48, 60, 72],nums2 = [24, 48, 72]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 24, 36, 48, 60, 72],nums2 = [24, 48, 72]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [200, 300, 400]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [200, 300, 400]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],nums2 = [25, 30, 35]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],nums2 = [25, 30, 35]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 100, 100, 100, 100, 100, 100],nums2 = [100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 100, 100, 100, 100, 100, 100],nums2 = [100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 26, 39, 52, 65, 78],nums2 = [26, 52, 78]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 26, 39, 52, 65, 78],nums2 = [26, 52, 78]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],nums2 = [14, 14, 14, 14, 14, 14, 14, 14, 14, 14]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],nums2 = [14, 14, 14, 14, 14, 14, 14, 14, 14, 14]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15, 18, 21],nums2 = [6, 9, 12, 15, 18]) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15, 18, 21],nums2 = [6, 9, 12, 15, 18]) == -3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 5, 8, 11, 14, 17],nums2 = [8, 11, 14]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 5, 8, 11, 14, 17],nums2 = [8, 11, 14]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [30, 45, 60]) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [30, 45, 60]) == -15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 100, 2, 99, 3, 98],nums2 = [3, 100, 98]) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 100, 2, 99, 3, 98],nums2 = [3, 100, 98]) == inf: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [10, 15, 20, 25, 30]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [10, 15, 20, 25, 30]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [21, 42, 63, 84, 105, 126],nums2 = [42, 84, 126]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [21, 42, 63, 84, 105, 126],nums2 = [42, 84, 126]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [150, 250, 350, 450]) == -150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [150, 250, 350, 450]) == -150: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [14, 21, 28]) == -7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [14, 21, 28]) == -7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45],nums2 = [10, 15, 20]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45],nums2 = [10, 15, 20]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4],nums2 = [8, 7, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4],nums2 = [8, 7, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [300, 400, 500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [300, 400, 500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [4, 6, 8]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [4, 6, 8]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 70, 90, 110, 130, 150],nums2 = [90, 110, 130, 150]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 70, 90, 110, 130, 150],nums2 = [90, 110, 130, 150]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],nums2 = [7, 9, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],nums2 = [7, 9, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5],nums2 = [2, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5],nums2 = [2, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000],nums2 = [3000, 4000, 5000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000],nums2 = [3000, 4000, 5000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [200, 300, 400]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [200, 300, 400]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 12, 18, 24, 30, 36],nums2 = [12, 24, 36]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 12, 18, 24, 30, 36],nums2 = [12, 24, 36]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [5, 7, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [5, 7, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6],nums2 = [2, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6],nums2 = [2, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45, 54],nums2 = [18, 36, 54]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45, 54],nums2 = [18, 36, 54]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123, 246, 369, 492, 615, 738],nums2 = [246, 369, 492]) == -123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123, 246, 369, 492, 615, 738],nums2 = [246, 369, 492]) == -123: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18],nums2 = [6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18],nums2 = [6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5],nums2 = [7, 7, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5],nums2 = [7, 7, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42],nums2 = [14, 28, 42]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42],nums2 = [14, 28, 42]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],nums2 = [18, 27, 36, 45, 54]) == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],nums2 = [18, 27, 36, 45, 54]) == -9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9],nums2 = [5, 6, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9],nums2 = [5, 6, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80],nums2 = [30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80],nums2 = [30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7],nums2 = [5, 6, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7],nums2 = [5, 6, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],nums2 = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],nums2 = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [20, 30, 40]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [20, 30, 40]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [30, 29, 28, 27, 26, 25],nums2 = [28, 27, 26]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [30, 29, 28, 27, 26, 25],nums2 = [28, 27, 26]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75],nums2 = [25, 35, 45]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75],nums2 = [25, 35, 45]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [10, 20, 30, 40, 50, 60, 70, 80]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [10, 20, 30, 40, 50, 60, 70, 80]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 55, 60, 65, 70],nums2 = [55, 60, 65]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 55, 60, 65, 70],nums2 = [55, 60, 65]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 22, 33, 44, 55, 66],nums2 = [22, 33, 44]) == -11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 22, 33, 44, 55, 66],nums2 = [22, 33, 44]) == -11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 6, 7, 8, 9, 10, 11, 12],nums2 = [7, 8, 9, 10, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 6, 7, 8, 9, 10, 11, 12],nums2 = [7, 8, 9, 10, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4],nums2 = [2, 2, 3, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4],nums2 = [2, 2, 3, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],nums2 = [500, 400, 300, 200, 100]) == -200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],nums2 = [500, 400, 300, 200, 100]) == -200: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 15, 10, 20, 25],nums2 = [13, 18, 23]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 15, 10, 20, 25],nums2 = [13, 18, 23]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [3, 5, 7]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [3, 5, 7]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [15, 20, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [15, 20, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],nums2 = [18, 20, 22, 24, 26, 28]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],nums2 = [18, 20, 22, 24, 26, 28]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40, 48],nums2 = [16, 24, 32]) == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40, 48],nums2 = [16, 24, 32]) == -8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [5, 7, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [5, 7, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 15, 20, 25, 30, 35],nums2 = [15, 20, 25]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 15, 20, 25, 30, 35],nums2 = [15, 20, 25]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [3, 3, 3, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [3, 3, 3, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [25, 24, 23, 22, 21, 20],nums2 = [23, 22, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [25, 24, 23, 22, 21, 20],nums2 = [23, 22, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],nums2 = [18, 27, 36, 45, 54, 63, 72, 81, 90]) == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],nums2 = [18, 27, 36, 45, 54, 63, 72, 81, 90]) == -9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],nums2 = [30, 35, 40]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],nums2 = [30, 35, 40]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14],nums2 = [8, 10, 12]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14],nums2 = [8, 10, 12]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [8, 7, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [8, 7, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [150, 250, 350, 450, 550]) == -150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [150, 250, 350, 450, 550]) == -150: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [150, 250, 350]) == -150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [150, 250, 350]) == -150: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 100, 150, 200, 250, 300],nums2 = [75, 125, 175]) == -75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 100, 150, 200, 250, 300],nums2 = [75, 125, 175]) == -75: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [35, 34, 33, 32, 31, 30],nums2 = [33, 32, 31]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [35, 34, 33, 32, 31, 30],nums2 = [33, 32, 31]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [3, 3, 3]) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [3, 3, 3]) == inf: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [20, 25, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [20, 25, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [10, 15, 20, 25]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [10, 15, 20, 25]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],nums2 = [20, 30, 40]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],nums2 = [20, 30, 40]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 18, 24, 30, 36],nums2 = [18, 24, 30]) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 18, 24, 30, 36],nums2 = [18, 24, 30]) == -6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [30, 40, 50, 60, 70]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [30, 40, 50, 60, 70]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [3, 4, 5, 6, 7, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [3, 4, 5, 6, 7, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 20, 25, 30, 35, 40],nums2 = [20, 25, 30]) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 20, 25, 30, 35, 40],nums2 = [20, 25, 30]) == -5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42],nums2 = [14, 21, 28]) == -7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42],nums2 = [14, 21, 28]) == -7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4],nums2 = [3, 3, 4, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4],nums2 = [3, 3, 4, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64],nums2 = [10, 18, 26, 34, 42, 50, 58]) == -14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64],nums2 = [10, 18, 26, 34, 42, 50, 58]) == -14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [4, 5, 6, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [4, 5, 6, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],nums2 = [510, 510, 510, 510, 510, 510, 510, 510]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],nums2 = [510, 510, 510, 510, 510, 510, 510, 510]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129, 139, 149, 159, 169, 179, 189, 199],nums2 = [39, 49, 59]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129, 139, 149, 159, 169, 179, 189, 199],nums2 = [39, 49, 59]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70],nums2 = [15, 25, 35, 45, 55]) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70],nums2 = [15, 25, 35, 45, 55]) == -15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [998, 999, 1000, 1001, 1002],nums2 = [999, 1000, 1001]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [998, 999, 1000, 1001, 1002],nums2 = [999, 1000, 1001]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40, 48],nums2 = [24, 32, 40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40, 48],nums2 = [24, 32, 40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [20, 19, 18, 17, 16, 15],nums2 = [18, 17, 16]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [20, 19, 18, 17, 16, 15],nums2 = [18, 17, 16]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [120, 220, 320, 420, 520, 620]) == -180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [120, 220, 320, 420, 520, 620]) == -180: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8],nums2 = [2, 3, 4, 4, 5, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8],nums2 = [2, 3, 4, 4, 5, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [4, 5, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [4, 5, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],nums2 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],nums2 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 20, 20, 30, 30, 40, 40],nums2 = [20, 20, 30, 30, 40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 20, 20, 30, 30, 40, 40],nums2 = [20, 20, 30, 30, 40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],nums2 = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],nums2 = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45, 55],nums2 = [15, 25, 35]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45, 55],nums2 = [15, 25, 35]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70],nums2 = [30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70],nums2 = [30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [9, 16, 23]) == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [9, 16, 23]) == -12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [20, 30, 40]) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [20, 30, 40]) == -10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [3, 3, 4, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [3, 3, 4, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 22, 33, 44, 55, 66],nums2 = [22, 33, 44]) == -11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 22, 33, 44, 55, 66],nums2 = [22, 33, 44]) == -11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],nums2 = [16, 18, 20, 22, 24]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],nums2 = [16, 18, 20, 22, 24]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [5, 6, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [5, 6, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [2, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [2, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],nums2 = [7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],nums2 = [7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [5, 6, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [5, 6, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [14, 28, 42, 56, 70, 84],nums2 = [28, 56, 84]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [14, 28, 42, 56, 70, 84],nums2 = [28, 56, 84]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 18, 21, 24, 27, 30],nums2 = [12, 15, 18, 21]) == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 18, 21, 24, 27, 30],nums2 = [12, 15, 18, 21]) == -9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 14, 13, 12, 11, 10],nums2 = [13, 12, 11]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 14, 13, 12, 11, 10],nums2 = [13, 12, 11]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4],nums2 = [3, 3, 4, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4],nums2 = [3, 3, 4, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],nums2 = [5, 6, 7]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],nums2 = [5, 6, 7]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 18, 27, 36, 45, 54],nums2 = [18, 27, 36]) == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 18, 27, 36, 45, 54],nums2 = [18, 27, 36]) == -9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [2, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [2, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3, 4, 5, 6],nums2 = [3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3, 4, 5, 6],nums2 = [3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15],nums2 = [6, 9, 12]) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15],nums2 = [6, 9, 12]) == -3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [2, 3, 4, 5, 6, 7, 8]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [2, 3, 4, 5, 6, 7, 8]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 100, 150, 200, 250, 300],nums2 = [150, 200, 250]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 100, 150, 200, 250, 300],nums2 = [150, 200, 250]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700],nums2 = [200, 300, 400]) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700],nums2 = [200, 300, 400]) == -100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 1000, 1000, 1000, 1000, 1000],nums2 = [1002, 1002, 1002]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 1000, 1000, 1000, 1000, 1000],nums2 = [1002, 1002, 1002]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],nums2 = [25, 30, 35, 40, 45, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],nums2 = [25, 30, 35, 40, 45, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9, 10, 11, 12, 13],nums2 = [9, 10, 11, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9, 10, 11, 12, 13],nums2 = [9, 10, 11, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [45, 47, 49, 51, 53, 55, 57],nums2 = [46, 48, 50, 52, 54]) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [45, 47, 49, 51, 53, 55, 57],nums2 = [46, 48, 50, 52, 54]) == -3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],nums2 = [3, 3, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],nums2 = [3, 3, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999, 1000, 1001, 1002, 1003, 1004],nums2 = [1000, 1001, 1002, 1003]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999, 1000, 1001, 1002, 1003, 1004],nums2 = [1000, 1001, 1002, 1003]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5],nums2 = [8, 7, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5],nums2 = [8, 7, 6]) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [20, 30, 40]) == -10
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [2, 2]) == 1
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [12, 22, 32]) == -18
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [7, 7]) == 2
    assert candidate(nums1 = [10, 10, 20, 20, 30],nums2 = [15, 25]) == 5
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [3, 4, 5]) == 0
    assert candidate(nums1 = [4, 20, 16, 12, 8],nums2 = [14, 18, 10]) == -2
    assert candidate(nums1 = [8, 16, 24, 32, 40],nums2 = [10, 18]) == -14
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 1]) == 1
    assert candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [10, 20]) == -15
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [2, 3]) == -1
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [2, 2]) == 2
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [15, 25]) == -15
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5],nums2 = [7, 7]) == 2
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [4, 8]) == 1
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [150, 250, 350]) == -150
    assert candidate(nums1 = [3, 5, 5, 3],nums2 = [7, 7]) == 2
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [3, 4]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [150, 250]) == -150
    assert candidate(nums1 = [9, 7, 5, 3, 1, -1, -3, -5, -7, -9],nums2 = [5, 3, 1, -1, -3, -5]) == 0
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12],nums2 = [6, 8, 10]) == 0
    assert candidate(nums1 = [0, 1, 2, 3, 4],nums2 = [2, 3, 4]) == 0
    assert candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],nums2 = [150, 200, 250]) == 0
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],nums2 = [12, 14, 16, 18, 20, 22, 24, 26]) == 6
    assert candidate(nums1 = [15, 25, 35, 45, 55, 65, 75],nums2 = [25, 35, 45, 55, 65]) == -10
    assert candidate(nums1 = [9, 18, 27, 36, 45, 54],nums2 = [12, 21, 30]) == -15
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [10, 15, 20]) == -5
    assert candidate(nums1 = [4, 8, 12, 16, 20, 24],nums2 = [8, 16, 24]) == 4
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [3, 4, 5, 6, 7]) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35],nums2 = [10, 15, 20]) == -5
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [110, 210, 310, 410]) == -190
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],nums2 = [6, 7, 8]) == 3
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [7, 7, 7, 7, 7, 7, 7, 7]) == 2
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [200, 300, 400]) == -100
    assert candidate(nums1 = [3, 6, 9, 12, 15, 18],nums2 = [6, 12, 18]) == 3
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [2, 3, 4, 5, 6]) == 0
    assert candidate(nums1 = [12, 24, 36, 48, 60, 72],nums2 = [24, 48, 72]) == 12
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [200, 300, 400]) == -100
    assert candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],nums2 = [25, 30, 35]) == 5
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 3
    assert candidate(nums1 = [100, 100, 100, 100, 100, 100, 100],nums2 = [100, 100, 100]) == 0
    assert candidate(nums1 = [13, 26, 39, 52, 65, 78],nums2 = [26, 52, 78]) == 13
    assert candidate(nums1 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],nums2 = [14, 14, 14, 14, 14, 14, 14, 14, 14, 14]) == 2
    assert candidate(nums1 = [3, 6, 9, 12, 15, 18, 21],nums2 = [6, 9, 12, 15, 18]) == -3
    assert candidate(nums1 = [2, 5, 8, 11, 14, 17],nums2 = [8, 11, 14]) == 0
    assert candidate(nums1 = [15, 30, 45, 60, 75, 90],nums2 = [30, 45, 60]) == -15
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [3, 4, 5]) == 0
    assert candidate(nums1 = [1, 100, 2, 99, 3, 98],nums2 = [3, 100, 98]) == inf
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [10, 15, 20, 25, 30]) == -5
    assert candidate(nums1 = [21, 42, 63, 84, 105, 126],nums2 = [42, 84, 126]) == 21
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [150, 250, 350, 450]) == -150
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42, 49],nums2 = [14, 21, 28]) == -7
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45],nums2 = [10, 15, 20]) == -5
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4],nums2 = [8, 7, 6]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [300, 400, 500]) == 0
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [4, 6, 8]) == -2
    assert candidate(nums1 = [50, 70, 90, 110, 130, 150],nums2 = [90, 110, 130, 150]) == 0
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0, 0]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],nums2 = [7, 9, 11]) == 2
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5],nums2 = [2, 3, 4]) == 0
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000],nums2 = [3000, 4000, 5000]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [200, 300, 400]) == -100
    assert candidate(nums1 = [6, 12, 18, 24, 30, 36],nums2 = [12, 24, 36]) == 6
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [5, 7, 9]) == 0
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6],nums2 = [2, 3, 4]) == 0
    assert candidate(nums1 = [9, 18, 27, 36, 45, 54],nums2 = [18, 36, 54]) == 9
    assert candidate(nums1 = [123, 246, 369, 492, 615, 738],nums2 = [246, 369, 492]) == -123
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18],nums2 = [6, 8, 10]) == 0
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5],nums2 = [7, 7, 7]) == 2
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42],nums2 = [14, 28, 42]) == 7
    assert candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],nums2 = [18, 27, 36, 45, 54]) == -9
    assert candidate(nums1 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9],nums2 = [5, 6, 7]) == 3
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80],nums2 = [30, 40, 50]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7],nums2 = [5, 6, 7]) == 2
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],nums2 = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == -2
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [20, 30, 40]) == -10
    assert candidate(nums1 = [30, 29, 28, 27, 26, 25],nums2 = [28, 27, 26]) == -1
    assert candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75],nums2 = [25, 35, 45]) == 0
    assert candidate(nums1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [10, 20, 30, 40, 50, 60, 70, 80]) == -10
    assert candidate(nums1 = [50, 55, 60, 65, 70],nums2 = [55, 60, 65]) == -5
    assert candidate(nums1 = [11, 22, 33, 44, 55, 66],nums2 = [22, 33, 44]) == -11
    assert candidate(nums1 = [5, 6, 7, 8, 9, 10, 11, 12],nums2 = [7, 8, 9, 10, 11]) == 0
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4],nums2 = [2, 2, 3, 3, 4]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0
    assert candidate(nums1 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],nums2 = [500, 400, 300, 200, 100]) == -200
    assert candidate(nums1 = [8, 15, 10, 20, 25],nums2 = [13, 18, 23]) == -2
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [3, 5, 7]) == -2
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [15, 20, 25]) == 0
    assert candidate(nums1 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],nums2 = [18, 20, 22, 24, 26, 28]) == 2
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [3, 4, 5]) == 0
    assert candidate(nums1 = [8, 16, 24, 32, 40, 48],nums2 = [16, 24, 32]) == -8
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [5, 7, 9]) == 0
    assert candidate(nums1 = [10, 15, 20, 25, 30, 35],nums2 = [15, 20, 25]) == -5
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [3, 3, 3, 3]) == 2
    assert candidate(nums1 = [25, 24, 23, 22, 21, 20],nums2 = [23, 22, 21]) == -1
    assert candidate(nums1 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],nums2 = [18, 27, 36, 45, 54, 63, 72, 81, 90]) == -9
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],nums2 = [30, 35, 40]) == 15
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14],nums2 = [8, 10, 12]) == 2
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [8, 7, 6]) == 3
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [150, 250, 350, 450, 550]) == -150
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600],nums2 = [150, 250, 350]) == -150
    assert candidate(nums1 = [50, 100, 150, 200, 250, 300],nums2 = [75, 125, 175]) == -75
    assert candidate(nums1 = [35, 34, 33, 32, 31, 30],nums2 = [33, 32, 31]) == -1
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [3, 3, 3]) == inf
    assert candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [20, 25, 30]) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [10, 15, 20, 25]) == -5
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],nums2 = [20, 30, 40]) == -10
    assert candidate(nums1 = [12, 18, 24, 30, 36],nums2 = [18, 24, 30]) == -6
    assert candidate(nums1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],nums2 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]) == 2
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [30, 40, 50, 60, 70]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [3, 4, 5, 6, 7, 8]) == 0
    assert candidate(nums1 = [15, 20, 25, 30, 35, 40],nums2 = [20, 25, 30]) == -5
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42],nums2 = [14, 21, 28]) == -7
    assert candidate(nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4],nums2 = [3, 3, 4, 4]) == 2
    assert candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64],nums2 = [10, 18, 26, 34, 42, 50, 58]) == -14
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [4, 5, 6, 7, 8, 9]) == 1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums1 = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],nums2 = [510, 510, 510, 510, 510, 510, 510, 510]) == 10
    assert candidate(nums1 = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129, 139, 149, 159, 169, 179, 189, 199],nums2 = [39, 49, 59]) == 10
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70],nums2 = [15, 25, 35, 45, 55]) == -15
    assert candidate(nums1 = [998, 999, 1000, 1001, 1002],nums2 = [999, 1000, 1001]) == -1
    assert candidate(nums1 = [8, 16, 24, 32, 40, 48],nums2 = [24, 32, 40]) == 0
    assert candidate(nums1 = [20, 19, 18, 17, 16, 15],nums2 = [18, 17, 16]) == -1
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [120, 220, 320, 420, 520, 620]) == -180
    assert candidate(nums1 = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8],nums2 = [2, 3, 4, 4, 5, 6]) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [4, 5, 6]) == 1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],nums2 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -2
    assert candidate(nums1 = [10, 10, 20, 20, 30, 30, 40, 40],nums2 = [20, 20, 30, 30, 40]) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],nums2 = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == -10
    assert candidate(nums1 = [5, 15, 25, 35, 45, 55],nums2 = [15, 25, 35]) == -10
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70],nums2 = [30, 40, 50]) == 0
    assert candidate(nums1 = [7, 14, 21, 28, 35],nums2 = [9, 16, 23]) == -12
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],nums2 = [20, 30, 40]) == -10
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [3, 3, 4, 4]) == 1
    assert candidate(nums1 = [11, 22, 33, 44, 55, 66],nums2 = [22, 33, 44]) == -11
    assert candidate(nums1 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],nums2 = [16, 18, 20, 22, 24]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [5, 6, 7]) == 2
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [2, 3, 4]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],nums2 = [7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 2
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7]) == 2
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [5, 6, 7]) == 2
    assert candidate(nums1 = [14, 28, 42, 56, 70, 84],nums2 = [28, 56, 84]) == 14
    assert candidate(nums1 = [15, 18, 21, 24, 27, 30],nums2 = [12, 15, 18, 21]) == -9
    assert candidate(nums1 = [15, 14, 13, 12, 11, 10],nums2 = [13, 12, 11]) == -1
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4],nums2 = [3, 3, 4, 4]) == 1
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],nums2 = [5, 6, 7]) == 4
    assert candidate(nums1 = [9, 18, 27, 36, 45, 54],nums2 = [18, 27, 36]) == -9
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [2, 2, 3]) == 0
    assert candidate(nums1 = [1, 2, 2, 3, 4, 5, 6],nums2 = [3, 4, 5]) == 1
    assert candidate(nums1 = [3, 6, 9, 12, 15],nums2 = [6, 9, 12]) == -3
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [2, 3, 4, 5, 6, 7, 8]) == -1
    assert candidate(nums1 = [50, 100, 150, 200, 250, 300],nums2 = [150, 200, 250]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700],nums2 = [200, 300, 400]) == -100
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [30, 40, 50]) == 0
    assert candidate(nums1 = [1000, 1000, 1000, 1000, 1000, 1000],nums2 = [1002, 1002, 1002]) == 2
    assert candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],nums2 = [25, 30, 35, 40, 45, 50]) == 5
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0
    assert candidate(nums1 = [7, 8, 9, 10, 11, 12, 13],nums2 = [9, 10, 11, 12]) == 0
    assert candidate(nums1 = [45, 47, 49, 51, 53, 55, 57],nums2 = [46, 48, 50, 52, 54]) == -3
    assert candidate(nums1 = [0, 0, 0, 0, 0, 0],nums2 = [0, 0]) == 0
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],nums2 = [3, 3, 4]) == 1
    assert candidate(nums1 = [999, 1000, 1001, 1002, 1003, 1004],nums2 = [1000, 1001, 1002, 1003]) == -1
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5],nums2 = [8, 7, 6]) == -1


