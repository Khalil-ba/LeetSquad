def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1],nums2 = [100, 100, 100]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1],nums2 = [100, 100, 100]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 100, 100],nums2 = [100, 100, 100]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 100, 100],nums2 = [100, 100, 100]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 1, 4, 5, 7],nums2 = [3, 2, 4, 8, 6]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 1, 4, 5, 7],nums2 = [3, 2, 4, 8, 6]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [100, 100, 100, 100]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [100, 100, 100, 100]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 100, 100],nums2 = [1, 1, 1]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 100, 100],nums2 = [1, 1, 1]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 4, 2],nums2 = [4, 2, 2, 5]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 4, 2],nums2 = [4, 2, 2, 5]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [6, 5, 4]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [6, 5, 4]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [100, 100, 100, 100, 100]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [100, 100, 100, 100, 100]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [5, 0, 2, 3]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [5, 0, 2, 3]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 20, 30],nums2 = [10, 60, 40]) == 2900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 20, 30],nums2 = [10, 60, 40]) == 2900: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [5, 6, 7, 8]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [5, 6, 7, 8]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [88, 77, 66, 55, 44, 33, 22, 11],nums2 = [11, 22, 33, 44, 55, 66, 77, 88]) == 14520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [88, 77, 66, 55, 44, 33, 22, 11],nums2 = [11, 22, 33, 44, 55, 66, 77, 88]) == 14520: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 3300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 3300: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99, 98, 97, 96],nums2 = [1, 2, 3, 4]) == 970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99, 98, 97, 96],nums2 = [1, 2, 3, 4]) == 970: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99, 98, 97, 96, 95],nums2 = [1, 2, 3, 4, 5]) == 1445
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99, 98, 97, 96, 95],nums2 = [1, 2, 3, 4, 5]) == 1445: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 1, 100, 1, 100],nums2 = [1, 100, 1, 100, 1]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 1, 100, 1, 100],nums2 = [1, 100, 1, 100, 1]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 20, 30, 40, 10],nums2 = [10, 20, 30, 40, 50]) == 3500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 20, 30, 40, 10],nums2 = [10, 20, 30, 40, 50]) == 3500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 25, 75, 100, 125],nums2 = [200, 150, 100, 50, 1]) == 25125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 25, 75, 100, 125],nums2 = [200, 150, 100, 50, 1]) == 25125: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [2, 4, 6, 8, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [2, 4, 6, 8, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 99, 2, 98, 3, 97],nums2 = [100, 1, 99, 2, 98, 3]) == 1178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 99, 2, 98, 3, 97],nums2 = [100, 1, 99, 2, 98, 3]) == 1178: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 25, 75, 100],nums2 = [200, 100, 50, 25]) == 16250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 25, 75, 100],nums2 = [200, 100, 50, 25]) == 16250: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 22100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 22100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 6, 4, 2, 1],nums2 = [1, 2, 4, 6, 8]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 6, 4, 2, 1],nums2 = [1, 2, 4, 6, 8]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 50, 75, 25, 125, 75, 150, 25, 100],nums2 = [50, 100, 75, 150, 25, 125, 25, 75, 100]) == 44375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 50, 75, 25, 125, 75, 150, 25, 100],nums2 = [50, 100, 75, 150, 25, 125, 25, 75, 100]) == 44375: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 5, 3, 1, 9],nums2 = [2, 8, 6, 4, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 5, 3, 1, 9],nums2 = [2, 8, 6, 4, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 2750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 2750: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1540: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 770: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 68000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 68000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 7, 3, 5, 1],nums2 = [2, 8, 6, 4, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 7, 3, 5, 1],nums2 = [2, 8, 6, 4, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99, 1, 23, 78, 56, 34],nums2 = [45, 67, 89, 12, 34, 56]) == 9894
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99, 1, 23, 78, 56, 34],nums2 = [45, 67, 89, 12, 34, 56]) == 9894: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 4, 2, 1],nums2 = [4, 2, 2, 5, 3]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 4, 2, 1],nums2 = [4, 2, 2, 5, 3]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 20, 30, 10, 40],nums2 = [1, 5, 3, 9, 7]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 20, 30, 10, 40],nums2 = [1, 5, 3, 9, 7]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 770: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 5, 9, 2, 6],nums2 = [1, 3, 8, 4, 10]) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 5, 9, 2, 6],nums2 = [1, 3, 8, 4, 10]) == 114: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1925: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 5, 7, 11, 13],nums2 = [13, 11, 7, 5, 3, 2]) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 5, 7, 11, 13],nums2 = [13, 11, 7, 5, 3, 2]) == 188: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [1, 2, 3, 4, 5]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [1, 2, 3, 4, 5]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [6, 5, 4, 3, 2, 1]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [6, 5, 4, 3, 2, 1]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18130: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10, 10, 10],nums2 = [1, 2, 3, 4, 5]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10, 10, 10],nums2 = [1, 2, 3, 4, 5]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 22000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 22000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 100, 2, 99, 3, 98],nums2 = [100, 1, 99, 2, 98, 3]) == 1184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 100, 2, 99, 3, 98],nums2 = [100, 1, 99, 2, 98, 3]) == 1184: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 27500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 27500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 770: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],nums2 = [120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 36400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],nums2 = [120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 36400: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [1, 2, 3, 4, 5]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [1, 2, 3, 4, 5]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [90, 30, 50, 60],nums2 = [20, 40, 70, 80]) == 10100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [90, 30, 50, 60],nums2 = [20, 40, 70, 80]) == 10100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1540: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 770: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 2750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 2750: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12]) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12]) == 182: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 22000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 22000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5115: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [15, 13, 11, 9, 7, 5, 3, 1]) == 344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [15, 13, 11, 9, 7, 5, 3, 1]) == 344: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 2, 7, 8, 3, 9, 1, 4, 6, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 2, 7, 8, 3, 9, 1, 4, 6, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 100]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 100]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 2, 7, 8, 3, 9, 1, 4, 6],nums2 = [9, 4, 1, 8, 5, 2, 7, 3, 6]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 2, 7, 8, 3, 9, 1, 4, 6],nums2 = [9, 4, 1, 8, 5, 2, 7, 3, 6]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [98, 86, 74, 62, 50, 38, 26, 14, 2, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [98, 86, 74, 62, 50, 38, 26, 14, 2, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2080: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2750: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 35, 55, 25, 45, 65, 75, 85, 95, 105],nums2 = [105, 95, 85, 75, 65, 55, 45, 35, 25, 15]) == 27750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 35, 55, 25, 45, 65, 75, 85, 95, 105],nums2 = [105, 95, 85, 75, 65, 55, 45, 35, 25, 15]) == 27750: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 40, 30, 20, 10, 1],nums2 = [1, 10, 20, 30, 40, 50]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 40, 30, 20, 10, 1],nums2 = [1, 10, 20, 30, 40, 50]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],nums2 = [101, 1, 102, 2, 103, 3, 104, 4, 105, 5]) == 2995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],nums2 = [101, 1, 102, 2, 103, 3, 104, 4, 105, 5]) == 2995: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [99, 98, 97, 96, 95],nums2 = [1, 2, 3, 4, 5]) == 1445
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [99, 98, 97, 96, 95],nums2 = [1, 2, 3, 4, 5]) == 1445: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],nums2 = [9, 7, 9, 3, 7, 9, 3, 7, 9, 3, 7]) == 242
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],nums2 = [9, 7, 9, 3, 7, 9, 3, 7, 9, 3, 7]) == 242: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 20, 30, 40, 10],nums2 = [1, 2, 3, 4, 5]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 20, 30, 40, 10],nums2 = [1, 2, 3, 4, 5]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 20, 80, 40, 60],nums2 = [5, 10, 3, 9, 7]) == 1450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 20, 80, 40, 60],nums2 = [5, 10, 3, 9, 7]) == 1450: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 50, 50, 50, 50],nums2 = [1, 2, 3, 4, 5]) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 50, 50, 50, 50],nums2 = [1, 2, 3, 4, 5]) == 750: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 6, 4, 2, 0],nums2 = [1, 3, 5, 7, 9]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 6, 4, 2, 0],nums2 = [1, 3, 5, 7, 9]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [55, 45, 35, 25, 15, 5, 1, 2, 3, 4],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [55, 45, 35, 25, 15, 5, 1, 2, 3, 4],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5350: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 8, 8, 8, 8, 8, 8, 8],nums2 = [9, 7, 5, 3, 1, 6, 4, 2]) == 296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 8, 8, 8, 8, 8, 8, 8],nums2 = [9, 7, 5, 3, 1, 6, 4, 2]) == 296: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]) == 2565
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]) == 2565: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 100]) == 244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 100]) == 244: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 22000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 22000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],nums2 = [9, 7, 9, 3, 7, 9, 3, 2, 3, 8, 4]) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],nums2 = [9, 7, 9, 3, 7, 9, 3, 2, 3, 8, 4]) == 195: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 3500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 3500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 390: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [30, 20, 10, 40, 50],nums2 = [5, 4, 3, 2, 1]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [30, 20, 10, 40, 50],nums2 = [5, 4, 3, 2, 1]) == 350: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [1, 1, 1],nums2 = [100, 100, 100]) == 300
    assert candidate(nums1 = [100, 100, 100],nums2 = [100, 100, 100]) == 30000
    assert candidate(nums1 = [2, 1, 4, 5, 7],nums2 = [3, 2, 4, 8, 6]) == 65
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [100, 100, 100, 100]) == 400
    assert candidate(nums1 = [100, 100, 100],nums2 = [1, 1, 1]) == 300
    assert candidate(nums1 = [5, 3, 4, 2],nums2 = [4, 2, 2, 5]) == 40
    assert candidate(nums1 = [1, 2, 3],nums2 = [6, 5, 4]) == 28
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [100, 100, 100, 100, 100]) == 500
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == 20
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [5, 0, 2, 3]) == 17
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 4
    assert candidate(nums1 = [50, 20, 30],nums2 = [10, 60, 40]) == 2900
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [5, 6, 7, 8]) == 60
    assert candidate(nums1 = [88, 77, 66, 55, 44, 33, 22, 11],nums2 = [11, 22, 33, 44, 55, 66, 77, 88]) == 14520
    assert candidate(nums1 = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 3300
    assert candidate(nums1 = [99, 98, 97, 96],nums2 = [1, 2, 3, 4]) == 970
    assert candidate(nums1 = [99, 98, 97, 96, 95],nums2 = [1, 2, 3, 4, 5]) == 1445
    assert candidate(nums1 = [100, 1, 100, 1, 100],nums2 = [1, 100, 1, 100, 1]) == 500
    assert candidate(nums1 = [50, 20, 30, 40, 10],nums2 = [10, 20, 30, 40, 50]) == 3500
    assert candidate(nums1 = [50, 25, 75, 100, 125],nums2 = [200, 150, 100, 50, 1]) == 25125
    assert candidate(nums1 = [9, 7, 5, 3, 1],nums2 = [2, 4, 6, 8, 10]) == 110
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680
    assert candidate(nums1 = [1, 99, 2, 98, 3, 97],nums2 = [100, 1, 99, 2, 98, 3]) == 1178
    assert candidate(nums1 = [50, 25, 75, 100],nums2 = [200, 100, 50, 25]) == 16250
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1050
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 22100
    assert candidate(nums1 = [8, 6, 4, 2, 1],nums2 = [1, 2, 4, 6, 8]) == 56
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 220
    assert candidate(nums1 = [100, 50, 75, 25, 125, 75, 150, 25, 100],nums2 = [50, 100, 75, 150, 25, 125, 25, 75, 100]) == 44375
    assert candidate(nums1 = [7, 5, 3, 1, 9],nums2 = [2, 8, 6, 4, 10]) == 110
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 2750
    assert candidate(nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1540
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 770
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 68000
    assert candidate(nums1 = [9, 7, 3, 5, 1],nums2 = [2, 8, 6, 4, 10]) == 110
    assert candidate(nums1 = [99, 1, 23, 78, 56, 34],nums2 = [45, 67, 89, 12, 34, 56]) == 9894
    assert candidate(nums1 = [5, 3, 4, 2, 1],nums2 = [4, 2, 2, 5, 3]) == 40
    assert candidate(nums1 = [50, 20, 30, 10, 40],nums2 = [1, 5, 3, 9, 7]) == 550
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 770
    assert candidate(nums1 = [7, 5, 9, 2, 6],nums2 = [1, 3, 8, 4, 10]) == 114
    assert candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1925
    assert candidate(nums1 = [2, 3, 5, 7, 11, 13],nums2 = [13, 11, 7, 5, 3, 2]) == 188
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 250
    assert candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [1, 2, 3, 4, 5]) == 350
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60],nums2 = [6, 5, 4, 3, 2, 1]) == 560
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680
    assert candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18130
    assert candidate(nums1 = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
    assert candidate(nums1 = [10, 10, 10, 10, 10],nums2 = [1, 2, 3, 4, 5]) == 150
    assert candidate(nums1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 22000
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == 85
    assert candidate(nums1 = [1, 100, 2, 99, 3, 98],nums2 = [100, 1, 99, 2, 98, 3]) == 1184
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 220
    assert candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 27500
    assert candidate(nums1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 770
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],nums2 = [120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 36400
    assert candidate(nums1 = [50, 40, 30, 20, 10],nums2 = [1, 2, 3, 4, 5]) == 350
    assert candidate(nums1 = [90, 30, 50, 60],nums2 = [20, 40, 70, 80]) == 10100
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1540
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 770
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 2750
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10, 12]) == 182
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 22000
    assert candidate(nums1 = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5115
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [15, 13, 11, 9, 7, 5, 3, 1]) == 344
    assert candidate(nums1 = [5, 2, 7, 8, 3, 9, 1, 4, 6, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 680
    assert candidate(nums1 = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 100]) == 400
    assert candidate(nums1 = [5, 2, 7, 8, 3, 9, 1, 4, 6],nums2 = [9, 4, 1, 8, 5, 2, 7, 3, 6]) == 165
    assert candidate(nums1 = [98, 86, 74, 62, 50, 38, 26, 14, 2, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2080
    assert candidate(nums1 = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2750
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2200
    assert candidate(nums1 = [15, 35, 55, 25, 45, 65, 75, 85, 95, 105],nums2 = [105, 95, 85, 75, 65, 55, 45, 35, 25, 15]) == 27750
    assert candidate(nums1 = [50, 40, 30, 20, 10, 1],nums2 = [1, 10, 20, 30, 40, 50]) == 2100
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 275
    assert candidate(nums1 = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],nums2 = [101, 1, 102, 2, 103, 3, 104, 4, 105, 5]) == 2995
    assert candidate(nums1 = [99, 98, 97, 96, 95],nums2 = [1, 2, 3, 4, 5]) == 1445
    assert candidate(nums1 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 70
    assert candidate(nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],nums2 = [9, 7, 9, 3, 7, 9, 3, 7, 9, 3, 7]) == 242
    assert candidate(nums1 = [50, 20, 30, 40, 10],nums2 = [1, 2, 3, 4, 5]) == 350
    assert candidate(nums1 = [50, 20, 80, 40, 60],nums2 = [5, 10, 3, 9, 7]) == 1450
    assert candidate(nums1 = [50, 50, 50, 50, 50],nums2 = [1, 2, 3, 4, 5]) == 750
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 1000
    assert candidate(nums1 = [8, 6, 4, 2, 0],nums2 = [1, 3, 5, 7, 9]) == 60
    assert candidate(nums1 = [55, 45, 35, 25, 15, 5, 1, 2, 3, 4],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 5350
    assert candidate(nums1 = [8, 8, 8, 8, 8, 8, 8, 8],nums2 = [9, 7, 5, 3, 1, 6, 4, 2]) == 296
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]) == 2565
    assert candidate(nums1 = [100, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 100]) == 244
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [9, 7, 5, 3, 1]) == 85
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [1, 2, 3, 4, 5]) == 350
    assert candidate(nums1 = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 22000
    assert candidate(nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],nums2 = [9, 7, 9, 3, 7, 9, 3, 2, 3, 8, 4]) == 195
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 3500
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 390
    assert candidate(nums1 = [30, 20, 10, 40, 50],nums2 = [5, 4, 3, 2, 1]) == 350


