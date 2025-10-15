def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3],nums2 = [2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3],nums2 = [2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [5, 15, 25, 35]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [5, 15, 25, 35]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [1, 2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [1, 2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2],nums2 = [2, 2, 3, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2],nums2 = [2, 2, 3, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [5, 15, 25]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [5, 15, 25]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [2, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [2, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000],nums2 = [1000000000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000],nums2 = [1000000000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 9],nums2 = [3, 6, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 9],nums2 = [3, 6, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 9, 13, 17],nums2 = [2, 6, 10, 14, 18]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 9, 13, 17],nums2 = [2, 6, 10, 14, 18]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 9],nums2 = [3, 7, 11]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 9],nums2 = [3, 7, 11]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15],nums2 = [15, 20, 25]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15],nums2 = [15, 20, 25]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 6],nums2 = [2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 6],nums2 = [2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 20],nums2 = [5, 15, 25]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 20],nums2 = [5, 15, 25]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 7, 9],nums2 = [2, 6, 8, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 7, 9],nums2 = [2, 6, 8, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [11, 13, 15, 17, 19]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [11, 13, 15, 17, 19]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],nums2 = [2, 5, 8, 13, 21, 34, 55, 89]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],nums2 = [2, 5, 8, 13, 21, 34, 55, 89]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3, 4, 5],nums2 = [2, 2, 3, 4, 5, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3, 4, 5],nums2 = [2, 2, 3, 4, 5, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],nums2 = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],nums2 = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13],nums2 = [2, 5, 8, 11, 14]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13],nums2 = [2, 5, 8, 11, 14]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 10, 20, 30, 50],nums2 = [1, 2, 3, 10, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 10, 20, 30, 50],nums2 = [1, 2, 3, 10, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],nums2 = [5, 10, 16, 23, 31, 40, 50, 61, 73, 86]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],nums2 = [5, 10, 16, 23, 31, 40, 50, 61, 73, 86]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 101, 102, 103, 104],nums2 = [99, 100, 101, 102, 105]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 101, 102, 103, 104],nums2 = [99, 100, 101, 102, 105]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 8, 10, 12, 15, 18, 20],nums2 = [2, 4, 6, 8, 10, 14, 18]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 8, 10, 12, 15, 18, 20],nums2 = [2, 4, 6, 8, 10, 14, 18]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3, 4, 5],nums2 = [2, 3, 3, 4, 5, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3, 4, 5],nums2 = [2, 3, 3, 4, 5, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],nums2 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],nums2 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 6, 10, 20],nums2 = [3, 4, 15, 20, 25]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 6, 10, 20],nums2 = [3, 4, 15, 20, 25]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13],nums2 = [2, 5, 8, 11, 14]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13],nums2 = [2, 5, 8, 11, 14]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 2000000, 3000000, 4000000],nums2 = [500000, 1500000, 2500000, 3500000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 2000000, 3000000, 4000000],nums2 = [500000, 1500000, 2500000, 3500000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3, 4, 5, 5, 5, 6],nums2 = [2, 3, 3, 4, 5, 5, 6, 7, 8]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3, 4, 5, 5, 5, 6],nums2 = [2, 3, 3, 4, 5, 5, 6, 7, 8]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67],nums2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67],nums2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [6, 12, 18, 24, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [6, 12, 18, 24, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [5, 10, 15, 20, 25, 30, 35, 40]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [5, 10, 15, 20, 25, 30, 35, 40]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [150, 250, 350, 450, 550]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [150, 250, 350, 450, 550]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3, 4, 5],nums2 = [2, 2, 3, 4, 6, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3, 4, 5],nums2 = [2, 2, 3, 4, 6, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],nums2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],nums2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 6, 7, 8, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 6, 7, 8, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45, 55]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45, 55]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000],nums2 = [5, 50, 500, 5000, 50000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000],nums2 = [5, 50, 500, 5000, 50000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],nums2 = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],nums2 = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]) == 50: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [1, 2, 2, 3],nums2 = [2, 2]) == 2
    assert candidate(nums1 = [10, 20, 30],nums2 = [5, 15, 25, 35]) == -1
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 1
    assert candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == -1
    assert candidate(nums1 = [10, 20, 30],nums2 = [1, 2, 3]) == -1
    assert candidate(nums1 = [1, 1, 2, 2],nums2 = [2, 2, 3, 3]) == 2
    assert candidate(nums1 = [10, 20, 30],nums2 = [5, 15, 25]) == -1
    assert candidate(nums1 = [1, 2, 3],nums2 = [2, 4]) == 2
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == -1
    assert candidate(nums1 = [1000000000],nums2 = [1000000000]) == 1000000000
    assert candidate(nums1 = [1, 5, 9],nums2 = [3, 6, 9]) == 9
    assert candidate(nums1 = [1, 5, 9, 13, 17],nums2 = [2, 6, 10, 14, 18]) == -1
    assert candidate(nums1 = [1],nums2 = [2]) == -1
    assert candidate(nums1 = [1, 5, 9],nums2 = [3, 7, 11]) == -1
    assert candidate(nums1 = [5, 10, 15],nums2 = [15, 20, 25]) == 15
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == -1
    assert candidate(nums1 = [1, 2, 3, 6],nums2 = [2, 3, 4, 5]) == 2
    assert candidate(nums1 = [1, 10, 20],nums2 = [5, 15, 25]) == -1
    assert candidate(nums1 = [1],nums2 = [1]) == 1
    assert candidate(nums1 = [1, 5, 7, 9],nums2 = [2, 6, 8, 10]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 5
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [11, 13, 15, 17, 19]) == -1
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 2
    assert candidate(nums1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],nums2 = [2, 5, 8, 13, 21, 34, 55, 89]) == -1
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums1 = [1, 2, 2, 3, 4, 5],nums2 = [2, 2, 3, 4, 5, 6]) == 2
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == -1
    assert candidate(nums1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],nums2 = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]) == 1
    assert candidate(nums1 = [1, 4, 7, 10, 13],nums2 = [2, 5, 8, 11, 14]) == -1
    assert candidate(nums1 = [2, 10, 20, 30, 50],nums2 = [1, 2, 3, 10, 100]) == 2
    assert candidate(nums1 = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],nums2 = [5, 10, 16, 23, 31, 40, 50, 61, 73, 86]) == 10
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 10
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 5
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 3
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]) == -1
    assert candidate(nums1 = [100, 101, 102, 103, 104],nums2 = [99, 100, 101, 102, 105]) == 100
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums1 = [1, 4, 8, 10, 12, 15, 18, 20],nums2 = [2, 4, 6, 8, 10, 14, 18]) == 4
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == -1
    assert candidate(nums1 = [1, 2, 2, 3, 4, 5],nums2 = [2, 3, 3, 4, 5, 6]) == 2
    assert candidate(nums1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == -1
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == -1
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10]) == 10
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [16, 17, 18, 19, 20]) == -1
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9]) == -1
    assert candidate(nums1 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],nums2 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]) == 1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == -1
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 3
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums1 = [1, 4, 6, 10, 20],nums2 = [3, 4, 15, 20, 25]) == 4
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(nums1 = [1, 4, 7, 10, 13],nums2 = [2, 5, 8, 11, 14]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == -1
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 15
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 5
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 20
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == 1
    assert candidate(nums1 = [1000000, 2000000, 3000000, 4000000],nums2 = [500000, 1500000, 2500000, 3500000]) == -1
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 3
    assert candidate(nums1 = [1, 2, 2, 3, 4, 5, 5, 5, 6],nums2 = [2, 3, 3, 4, 5, 5, 6, 7, 8]) == 2
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums1 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67],nums2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 2
    assert candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [6, 12, 18, 24, 30]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15]) == -1
    assert candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [5, 10, 15, 20, 25, 30, 35, 40]) == 5
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 10
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [150, 250, 350, 450, 550]) == -1
    assert candidate(nums1 = [1, 2, 2, 3, 4, 5],nums2 = [2, 2, 3, 4, 6, 7]) == 2
    assert candidate(nums1 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],nums2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 1
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == -1
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 6, 7, 8, 9]) == 5
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45, 55]) == -1
    assert candidate(nums1 = [1, 10, 100, 1000, 10000],nums2 = [5, 50, 500, 5000, 50000]) == -1
    assert candidate(nums1 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],nums2 = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]) == 50


