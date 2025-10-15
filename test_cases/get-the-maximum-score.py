def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [10000000],nums2 = [10000000]) == 10000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000000],nums2 = [10000000]) == 10000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 5, 8, 10],nums2 = [4, 6, 8, 9]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 5, 8, 10],nums2 = [4, 6, 8, 9]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6, 7, 8, 9, 10]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6, 7, 8, 9, 10]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 6, 8, 10],nums2 = [2, 4, 6, 8, 12]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 6, 8, 10],nums2 = [2, 4, 6, 8, 12]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [3, 5, 100]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [3, 5, 100]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45, 55]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45, 55]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [3, 4, 5, 6, 7, 8]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [3, 4, 5, 6, 7, 8]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [5, 15, 25, 35, 45]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [5, 15, 25, 35, 45]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10000000],nums2 = [2, 9999999]) == 10000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10000000],nums2 = [2, 9999999]) == 10000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 6, 8],nums2 = [2, 3, 5, 7]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 6, 8],nums2 = [2, 3, 5, 7]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 4095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 4095: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 605: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9999991, 9999992, 9999993, 9999994, 9999995, 9999996, 9999997, 9999998, 9999999, 10000000],nums2 = [10000001, 10000002, 10000003, 10000004, 10000005, 10000006, 10000007, 10000008, 10000009, 10000010]) == 100000055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9999991, 9999992, 9999993, 9999994, 9999995, 9999996, 9999997, 9999998, 9999999, 10000000],nums2 = [10000001, 10000002, 10000003, 10000004, 10000005, 10000006, 10000007, 10000008, 10000009, 10000010]) == 100000055: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 551: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [5, 15, 25, 35, 45]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [5, 15, 25, 35, 45]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1300: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 195: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 6, 7, 10, 20, 30],nums2 = [2, 4, 5, 7, 11, 12, 15, 20]) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 6, 7, 10, 20, 30],nums2 = [2, 4, 5, 7, 11, 12, 15, 20]) == 107: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 6, 7, 8, 10, 15, 20],nums2 = [2, 4, 5, 7, 9, 10, 13, 18]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 6, 7, 8, 10, 15, 20],nums2 = [2, 4, 5, 7, 9, 10, 13, 18]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 6, 7, 11, 15],nums2 = [1, 2, 3, 8, 12, 16, 20]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 6, 7, 11, 15],nums2 = [1, 2, 3, 8, 12, 16, 20]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17],nums2 = [4, 6, 8, 10, 12, 14, 16, 18, 20]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17],nums2 = [4, 6, 8, 10, 12, 14, 16, 18, 20]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000],nums2 = [1500000, 2500000, 3500000, 4500000, 5500000]) == 17500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000],nums2 = [1500000, 2500000, 3500000, 4500000, 5500000]) == 17500000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000000, 20000000, 30000000, 40000000, 50000000],nums2 = [15000000, 20000000, 25000000, 35000000, 40000000, 45000000, 55000000]) == 235000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000000, 20000000, 30000000, 40000000, 50000000],nums2 = [15000000, 20000000, 25000000, 35000000, 40000000, 45000000, 55000000]) == 235000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],nums2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],nums2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 5, 6, 10, 15, 20, 25],nums2 = [2, 4, 7, 10, 12, 15, 22]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 5, 6, 10, 15, 20, 25],nums2 = [2, 4, 7, 10, 12, 15, 22]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == 3069
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == 3069: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10000000],nums2 = [5000000, 10000000]) == 15000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10000000],nums2 = [5000000, 10000000]) == 15000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 3, 5, 8, 9, 10, 12, 15, 18, 20]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 3, 5, 8, 9, 10, 12, 15, 18, 20]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 208: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],nums2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],nums2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == 1250: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45, 55]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45, 55]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10000000],nums2 = [2, 9999999]) == 10000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10000000],nums2 = [2, 9999999]) == 10000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 100, 1000, 10000, 100000],nums2 = [10, 100, 1000, 10000, 100000, 1000000]) == 1111110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 100, 1000, 10000, 100000],nums2 = [10, 100, 1000, 10000, 100000, 1000000]) == 1111110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],nums2 = [2, 20, 200, 2000, 20000, 200000, 2000000, 20000000]) == 22222222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],nums2 = [2, 20, 200, 2000, 20000, 200000, 2000000, 20000000]) == 22222222: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 20, 25, 35, 40, 45, 55, 65, 70, 75, 85, 95]) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 20, 25, 35, 40, 45, 55, 65, 70, 75, 85, 95]) == 640: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],nums2 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 11111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],nums2 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 11111111: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 5, 7, 8, 10, 12],nums2 = [3, 4, 6, 7, 9, 10, 11, 13]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 5, 7, 8, 10, 12],nums2 = [3, 4, 6, 7, 9, 10, 11, 13]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 3, 5, 7, 11, 13, 17, 18, 19]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 3, 5, 7, 11, 13, 17, 18, 19]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 365: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 306: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000000],nums2 = [9999999, 10000000, 10000001]) == 30000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000000],nums2 = [9999999, 10000000, 10000001]) == 30000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 6, 10, 14, 18],nums2 = [3, 6, 9, 12, 15, 18, 21]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 6, 10, 14, 18],nums2 = [3, 6, 9, 12, 15, 18, 21]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40],nums2 = [10, 20, 30, 40, 50, 60, 70]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40],nums2 = [10, 20, 30, 40, 50, 60, 70]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 435: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9, 10, 12]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9, 10, 12]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [2, 5, 8, 11, 14, 17, 20]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [2, 5, 8, 11, 14, 17, 20]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 730: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],nums2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],nums2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1300: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000000],nums2 = [5000000, 10000000, 15000000]) == 30000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000000],nums2 = [5000000, 10000000, 15000000]) == 30000000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [2, 4, 6, 8, 10, 12, 14]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [2, 4, 6, 8, 10, 12, 14]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 490: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]) == 345: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 365: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 10, 15, 20, 25]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 10, 15, 20, 25]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],nums2 = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456]) == 536870911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],nums2 = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456]) == 536870911: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 605: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 435: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 1290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 1290: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 10, 20, 30, 40, 50],nums2 = [3, 10, 15, 25, 35, 45, 55]) == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 10, 20, 30, 40, 50],nums2 = [3, 10, 15, 25, 35, 45, 55]) == 191: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],nums2 = [250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500]) == 33750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],nums2 = [250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500]) == 33750: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000],nums2 = [500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000]) == 27500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000],nums2 = [500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000]) == 27500000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 20, 30, 40],nums2 = [5, 15, 25, 35, 45]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 20, 30, 40],nums2 = [5, 15, 25, 35, 45]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [3, 4, 9, 10, 15, 16, 20]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [3, 4, 9, 10, 15, 16, 20]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [1, 5, 9, 13, 17, 21]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [1, 5, 9, 13, 17, 21]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 335: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],nums2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],nums2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == 1250: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [10000000],nums2 = [10000000]) == 10000000
    assert candidate(nums1 = [2, 4, 5, 8, 10],nums2 = [4, 6, 8, 9]) == 30
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6, 7, 8, 9, 10]) == 49
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 155
    assert candidate(nums1 = [1, 4, 6, 8, 10],nums2 = [2, 4, 6, 8, 12]) == 32
    assert candidate(nums1 = [5, 10, 15, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [3, 5, 100]) == 109
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10]) == 40
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 4, 5]) == 15
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45, 55]) == 180
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6],nums2 = [3, 4, 5, 6, 7, 8]) == 36
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [5, 15, 25, 35, 45]) == 125
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 15
    assert candidate(nums1 = [1, 10000000],nums2 = [2, 9999999]) == 10000001
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 150
    assert candidate(nums1 = [1],nums2 = [1]) == 1
    assert candidate(nums1 = [1, 4, 6, 8],nums2 = [2, 3, 5, 7]) == 19
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 4095
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 605
    assert candidate(nums1 = [9999991, 9999992, 9999993, 9999994, 9999995, 9999996, 9999997, 9999998, 9999999, 10000000],nums2 = [10000001, 10000002, 10000003, 10000004, 10000005, 10000006, 10000007, 10000008, 10000009, 10000010]) == 100000055
    assert candidate(nums1 = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 551
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [5, 15, 25, 35, 45]) == 275
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 135
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 240
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 550
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1300
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 195
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums1 = [1, 4, 6, 7, 10, 20, 30],nums2 = [2, 4, 5, 7, 11, 12, 15, 20]) == 107
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 100
    assert candidate(nums1 = [1, 4, 6, 7, 8, 10, 15, 20],nums2 = [2, 4, 5, 7, 9, 10, 13, 18]) == 73
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(nums1 = [2, 3, 6, 7, 11, 15],nums2 = [1, 2, 3, 8, 12, 16, 20]) == 62
    assert candidate(nums1 = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17],nums2 = [4, 6, 8, 10, 12, 14, 16, 18, 20]) == 108
    assert candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000],nums2 = [1500000, 2500000, 3500000, 4500000, 5500000]) == 17500000
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(nums1 = [5, 15, 25, 35, 45],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 225
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5]) == 55
    assert candidate(nums1 = [10000000, 20000000, 30000000, 40000000, 50000000],nums2 = [15000000, 20000000, 25000000, 35000000, 40000000, 45000000, 55000000]) == 235000000
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 110
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],nums2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]) == 990
    assert candidate(nums1 = [1, 4, 5, 6, 10, 15, 20, 25],nums2 = [2, 4, 7, 10, 12, 15, 22]) == 99
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == 3069
    assert candidate(nums1 = [1, 10000000],nums2 = [5000000, 10000000]) == 15000000
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 3, 5, 8, 9, 10, 12, 15, 18, 20]) == 104
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 120
    assert candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 208
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 6000
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 240
    assert candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],nums2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == 1250
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 240
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 550
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 420
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 420
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45, 55]) == 180
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 121
    assert candidate(nums1 = [1, 10000000],nums2 = [2, 9999999]) == 10000001
    assert candidate(nums1 = [1, 100, 1000, 10000, 100000],nums2 = [10, 100, 1000, 10000, 100000, 1000000]) == 1111110
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],nums2 = [2, 20, 200, 2000, 20000, 200000, 2000000, 20000000]) == 22222222
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 20, 25, 35, 40, 45, 55, 65, 70, 75, 85, 95]) == 640
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],nums2 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]) == 11111111
    assert candidate(nums1 = [1, 2, 4, 5, 7, 8, 10, 12],nums2 = [3, 4, 6, 7, 9, 10, 11, 13]) == 63
    assert candidate(nums1 = [1, 3, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 3, 5, 7, 11, 13, 17, 18, 19]) == 119
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 365
    assert candidate(nums1 = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 306
    assert candidate(nums1 = [10000000],nums2 = [9999999, 10000000, 10000001]) == 30000000
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 145
    assert candidate(nums1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]) == 155
    assert candidate(nums1 = [2, 6, 10, 14, 18],nums2 = [3, 6, 9, 12, 15, 18, 21]) == 84
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40],nums2 = [10, 20, 30, 40, 50, 60, 70]) == 360
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 435
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 300
    assert candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26]) == 126
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [1, 3, 5, 7, 9, 10, 12]) == 47
    assert candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [2, 5, 8, 11, 14, 17, 20]) == 77
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 730
    assert candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],nums2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58]) == 450
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1300
    assert candidate(nums1 = [10000000],nums2 = [5000000, 10000000, 15000000]) == 30000000
    assert candidate(nums1 = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 500
    assert candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [2, 4, 6, 8, 10, 12, 14]) == 78
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 490
    assert candidate(nums1 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],nums2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]) == 345
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 365
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 10, 15, 20, 25]) == 115
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],nums2 = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456]) == 536870911
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 605
    assert candidate(nums1 = [1, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 435
    assert candidate(nums1 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 2500
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 105
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],nums2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 1290
    assert candidate(nums1 = [1, 5, 10, 20, 30, 40, 50],nums2 = [3, 10, 15, 25, 35, 45, 55]) == 191
    assert candidate(nums1 = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],nums2 = [250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500]) == 33750
    assert candidate(nums1 = [1000000, 2000000, 3000000, 4000000, 5000000],nums2 = [500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000]) == 27500000
    assert candidate(nums1 = [1, 10, 20, 30, 40],nums2 = [5, 15, 25, 35, 45]) == 125
    assert candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [3, 4, 9, 10, 15, 16, 20]) == 77
    assert candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [1, 5, 9, 13, 17, 21]) == 73
    assert candidate(nums1 = [1, 4, 7, 10, 13, 16, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 91
    assert candidate(nums1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],nums2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 335
    assert candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],nums2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == 1250


