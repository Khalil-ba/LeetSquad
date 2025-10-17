def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [20, 40, 20, 70, 30],nums2 = [50, 20, 50, 40, 20]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [20, 40, 20, 70, 30],nums2 = [50, 20, 50, 40, 20]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300],nums2 = [300, 200, 100]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300],nums2 = [300, 200, 100]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5000, 5000, 5000],nums2 = [5000, 5000, 5000]) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5000, 5000, 5000],nums2 = [5000, 5000, 5000]) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5000, 5000, 5000, 5000, 5000],nums2 = [6000, 6000, 6000, 6000, 6000]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5000, 5000, 5000, 5000, 5000],nums2 = [6000, 6000, 6000, 6000, 6000]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 10000, 10000],nums2 = [1, 1, 1]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 10000, 10000],nums2 = [1, 1, 1]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [60, 60, 60],nums2 = [10, 90, 10]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [60, 60, 60],nums2 = [10, 90, 10]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1],nums2 = [10000, 10000, 10000]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1],nums2 = [10000, 10000, 10000]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 11, 13],nums2 = [1, 1, 1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 11, 13],nums2 = [1, 1, 1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7],nums2 = [1, 2, 3]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7],nums2 = [1, 2, 3]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 310: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 10000, 10000, 10000, 10000],nums2 = [5000, 5000, 5000, 5000, 5000]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 10000, 10000, 10000, 10000],nums2 = [5000, 5000, 5000, 5000, 5000]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 2, 30, 4, 50, 6, 70, 8, 90, 10]) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 2, 30, 4, 50, 6, 70, 8, 90, 10]) == 280: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 55000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 55000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 1, 10000, 1, 10000],nums2 = [1, 10000, 1, 10000, 1]) == 40001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 1, 10000, 1, 10000],nums2 = [1, 10000, 1, 10000, 1]) == 40001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 1, 3, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 1, 3, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5000, 3000, 1000, 500, 250],nums2 = [250, 500, 1000, 3000, 5000]) == 17000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5000, 3000, 1000, 500, 250],nums2 = [250, 500, 1000, 3000, 5000]) == 17000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 176: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [1, 6, 11, 16, 21]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [1, 6, 11, 16, 21]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 10000, 10000, 10000, 10000],nums2 = [9999, 9999, 9999, 9999, 9999]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 10000, 10000, 10000, 10000],nums2 = [9999, 9999, 9999, 9999, 9999]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9999, 9999, 9999, 9999, 9999],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9999, 9999, 9999, 9999, 9999],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50005: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],nums2 = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 3100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],nums2 = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 3100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]) == 99990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]) == 99990: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 150000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 150000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1],nums2 = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000]) == 60004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1],nums2 = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000]) == 60004: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 9000, 8000, 7000, 6000],nums2 = [100, 200, 300, 400, 500]) == 40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 9000, 8000, 7000, 6000],nums2 = [100, 200, 300, 400, 500]) == 40000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5000, 2000, 3000, 4000, 1000],nums2 = [1000, 4000, 3000, 2000, 5000]) == 19000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5000, 2000, 3000, 4000, 1000],nums2 = [1000, 4000, 3000, 2000, 5000]) == 19000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9999, 9998, 9997, 9996, 9995],nums2 = [1, 2, 3, 4, 5]) == 49985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9999, 9998, 9997, 9996, 9995],nums2 = [1, 2, 3, 4, 5]) == 49985: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5000, 5000, 5000, 5000, 5000],nums2 = [10000, 10000, 10000, 10000, 10000]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5000, 5000, 5000, 5000, 5000],nums2 = [10000, 10000, 10000, 10000, 10000]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],nums2 = [9000, 9000, 9000, 9000, 9000, 9000, 9000, 9000, 9000, 9000]) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],nums2 = [9000, 9000, 9000, 9000, 9000, 9000, 9000, 9000, 9000, 9000]) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 100, 100, 100, 100],nums2 = [200, 200, 200, 200, 200]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 100, 100, 100, 100],nums2 = [200, 200, 200, 200, 200]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [5000, 4000, 3000, 2000, 1000]) == 21000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [5000, 4000, 3000, 2000, 1000]) == 21000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5000, 5000, 5000, 5000, 5000],nums2 = [5000, 5000, 5000, 5000, 5000]) == 25000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5000, 5000, 5000, 5000, 5000],nums2 = [5000, 5000, 5000, 5000, 5000]) == 25000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],nums2 = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],nums2 = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 604: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100, 5, 4, 3, 2, 1]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100, 5, 4, 3, 2, 1]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000],nums2 = [10000, 1000, 100, 10, 1]) == 22100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000],nums2 = [10000, 1000, 100, 10, 1]) == 22100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 50, 30, 20, 10],nums2 = [10, 20, 30, 50, 100]) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 50, 30, 20, 10],nums2 = [10, 20, 30, 50, 100]) == 330: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [100, 90, 80, 70, 60]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [100, 90, 80, 70, 60]) == 400: {e}')
    
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
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 8000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],nums2 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 80000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],nums2 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 80000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [10, 8, 6, 4, 2]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [10, 8, 6, 4, 2]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 1, 1, 1, 10000],nums2 = [1, 10000, 10000, 1, 1]) == 40001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 1, 1, 1, 10000],nums2 = [1, 10000, 10000, 1, 1]) == 40001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1760: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 10000, 10000, 10000, 10000],nums2 = [1, 1, 1, 1, 1]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 10000, 10000, 10000, 10000],nums2 = [1, 1, 1, 1, 1]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [1, 2, 3, 4, 5]) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [1, 2, 3, 4, 5]) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 10000],nums2 = [10000, 1, 1, 1, 1, 1]) == 20004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 10000],nums2 = [10000, 1, 1, 1, 1, 1]) == 20004: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [20, 40, 20, 70, 30],nums2 = [50, 20, 50, 40, 20]) == 220
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [5, 15, 25, 35, 45]) == 150
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000]) == 50000
    assert candidate(nums1 = [100, 200, 300],nums2 = [300, 200, 100]) == 800
    assert candidate(nums1 = [1, 2, 3],nums2 = [4, 5, 6]) == 15
    assert candidate(nums1 = [5000, 5000, 5000],nums2 = [5000, 5000, 5000]) == 15000
    assert candidate(nums1 = [1, 2, 3],nums2 = [3, 2, 1]) == 8
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 30
    assert candidate(nums1 = [5000, 5000, 5000, 5000, 5000],nums2 = [6000, 6000, 6000, 6000, 6000]) == 30000
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 21
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5]) == 25
    assert candidate(nums1 = [10000, 10000, 10000],nums2 = [1, 1, 1]) == 30000
    assert candidate(nums1 = [60, 60, 60],nums2 = [10, 90, 10]) == 210
    assert candidate(nums1 = [1, 1, 1],nums2 = [10000, 10000, 10000]) == 30000
    assert candidate(nums1 = [7, 11, 13],nums2 = [1, 1, 1]) == 31
    assert candidate(nums1 = [9, 8, 7],nums2 = [1, 2, 3]) == 24
    assert candidate(nums1 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 120
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [1, 2, 3, 4, 5]) == 25
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 310
    assert candidate(nums1 = [10000, 10000, 10000, 10000, 10000],nums2 = [5000, 5000, 5000, 5000, 5000]) == 50000
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 2, 30, 4, 50, 6, 70, 8, 90, 10]) == 280
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 5500
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5]) == 15
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 800
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 55000
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 30
    assert candidate(nums1 = [10000, 1, 10000, 1, 10000],nums2 = [1, 10000, 1, 10000, 1]) == 40001
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 200000
    assert candidate(nums1 = [5, 1, 3, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 104
    assert candidate(nums1 = [5000, 3000, 1000, 500, 250],nums2 = [250, 500, 1000, 3000, 5000]) == 17000
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 176
    assert candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [1, 6, 11, 16, 21]) == 75
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],nums2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 42
    assert candidate(nums1 = [10000, 10000, 10000, 10000, 10000],nums2 = [9999, 9999, 9999, 9999, 9999]) == 50000
    assert candidate(nums1 = [9999, 9999, 9999, 9999, 9999],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50005
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 45
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],nums2 = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 3100
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]) == 99990
    assert candidate(nums1 = [5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5]) == 41
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 150000
    assert candidate(nums1 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 58
    assert candidate(nums1 = [10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1],nums2 = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000]) == 60004
    assert candidate(nums1 = [10000, 9000, 8000, 7000, 6000],nums2 = [100, 200, 300, 400, 500]) == 40000
    assert candidate(nums1 = [5000, 2000, 3000, 4000, 1000],nums2 = [1000, 4000, 3000, 2000, 5000]) == 19000
    assert candidate(nums1 = [9999, 9998, 9997, 9996, 9995],nums2 = [1, 2, 3, 4, 5]) == 49985
    assert candidate(nums1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 36
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 80
    assert candidate(nums1 = [5000, 5000, 5000, 5000, 5000],nums2 = [10000, 10000, 10000, 10000, 10000]) == 50000
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(nums1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],nums2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(nums1 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],nums2 = [9000, 9000, 9000, 9000, 9000, 9000, 9000, 9000, 9000, 9000]) == 100000
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 400
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 100000
    assert candidate(nums1 = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50000
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 550
    assert candidate(nums1 = [100, 100, 100, 100, 100],nums2 = [200, 200, 200, 200, 200]) == 1000
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [5000, 4000, 3000, 2000, 1000]) == 21000
    assert candidate(nums1 = [5000, 5000, 5000, 5000, 5000],nums2 = [5000, 5000, 5000, 5000, 5000]) == 25000
    assert candidate(nums1 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1000
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 40
    assert candidate(nums1 = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],nums2 = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 604
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 100
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == 26
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 20
    assert candidate(nums1 = [1, 2, 3, 4, 5, 100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100, 5, 4, 3, 2, 1]) == 3000
    assert candidate(nums1 = [1, 10, 100, 1000, 10000],nums2 = [10000, 1000, 100, 10, 1]) == 22100
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5500
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert candidate(nums1 = [100, 50, 30, 20, 10],nums2 = [10, 20, 30, 50, 100]) == 330
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 110
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [100, 90, 80, 70, 60]) == 400
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 8000
    assert candidate(nums1 = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],nums2 = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 80000
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [10, 8, 6, 4, 2]) == 40
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 60
    assert candidate(nums1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5]) == 120
    assert candidate(nums1 = [10000, 1, 1, 1, 10000],nums2 = [1, 10000, 10000, 1, 1]) == 40001
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == 2100
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],nums2 = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1760
    assert candidate(nums1 = [10000, 10000, 10000, 10000, 10000],nums2 = [1, 1, 1, 1, 1]) == 50000
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [1, 2, 3, 4, 5]) == 15000
    assert candidate(nums1 = [1, 1, 1, 1, 1, 10000],nums2 = [10000, 1, 1, 1, 1, 1]) == 20004


