def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [3, 4, 2],nums2 = [4, 2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 4, 2],nums2 = [4, 2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2],nums2 = [2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2],nums2 = [2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 4, 5],nums2 = [5, 4, 3, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 4, 5],nums2 = [5, 4, 3, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 6, 2],nums2 = [9, 3, 5]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 6, 2],nums2 = [9, 3, 5]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15],nums2 = [15, 10, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15],nums2 = [15, 10, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 3, 4],nums2 = [1, 0, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 3, 4],nums2 = [1, 0, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [14, 15, 16],nums2 = [13, 14, 15]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [14, 15, 16],nums2 = [13, 14, 15]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9],nums2 = [9, 8, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9],nums2 = [9, 8, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [2, 2, 2, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [2, 2, 2, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9],nums2 = [10, 11, 12]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9],nums2 = [10, 11, 12]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000000, 10000000, 10000000],nums2 = [10000000, 10000000, 10000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000000, 10000000, 10000000],nums2 = [10000000, 10000000, 10000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 7, 9],nums2 = [9, 7, 5, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 7, 9],nums2 = [9, 7, 5, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2],nums2 = [3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2],nums2 = [3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [14, 28, 19],nums2 = [28, 14, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [14, 28, 19],nums2 = [28, 14, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 0, 3],nums2 = [5, 3, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 0, 3],nums2 = [5, 3, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 14, 16, 18, 20, 22],nums2 = [21, 19, 17, 15, 13, 11]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 14, 16, 18, 20, 22],nums2 = [21, 19, 17, 15, 13, 11]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 1, 3, 2],nums2 = [7, 6, 5, 8]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 1, 3, 2],nums2 = [7, 6, 5, 8]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9999999, 8888888, 7777777, 6666666, 5555555],nums2 = [4444444, 3333333, 2222222, 1111111, 0]) == 28302135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9999999, 8888888, 7777777, 6666666, 5555555],nums2 = [4444444, 3333333, 2222222, 1111111, 0]) == 28302135: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128],nums2 = [128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128],nums2 = [128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 23, 15, 4, 8],nums2 = [17, 9, 3, 20, 12]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 23, 15, 4, 8],nums2 = [17, 9, 3, 20, 12]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8],nums2 = [8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8],nums2 = [8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000000, 10000001, 10000002, 10000003, 10000004],nums2 = [10000005, 10000006, 10000007, 10000008, 10000009]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000000, 10000001, 10000002, 10000003, 10000004],nums2 = [10000005, 10000006, 10000007, 10000008, 10000009]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [15, 13, 11, 9, 7, 5, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [15, 13, 11, 9, 7, 5, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 9999999, 999999, 99999, 9999, 999, 99],nums2 = [99, 999, 9999, 99999, 999999, 9999999, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 9999999, 999999, 99999, 9999, 999, 99],nums2 = [99, 999, 9999, 99999, 999999, 9999999, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9, 10, 11, 12],nums2 = [12, 11, 10, 9, 8, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9, 10, 11, 12],nums2 = [12, 11, 10, 9, 8, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 13, 21, 31],nums2 = [3, 8, 15, 28]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 13, 21, 31],nums2 = [3, 8, 15, 28]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],nums2 = [70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],nums2 = [70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],nums2 = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 32769
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],nums2 = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 32769: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],nums2 = [43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71]) == 546
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],nums2 = [43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71]) == 546: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9, 10, 11],nums2 = [12, 13, 14, 15, 16]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9, 10, 11],nums2 = [12, 13, 14, 15, 16]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 17, 19, 23, 29, 31],nums2 = [31, 29, 23, 19, 17, 13]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 17, 19, 23, 29, 31],nums2 = [31, 29, 23, 19, 17, 13]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [101, 202, 303, 404, 505, 606, 707, 808, 909],nums2 = [909, 808, 707, 606, 505, 404, 303, 202, 101]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [101, 202, 303, 404, 505, 606, 707, 808, 909],nums2 = [909, 808, 707, 606, 505, 404, 303, 202, 101]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800],nums2 = [800, 700, 600, 500, 400, 300, 200, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800],nums2 = [800, 700, 600, 500, 400, 300, 200, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 8, 12, 7, 3],nums2 = [10, 6, 4, 15, 9]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 8, 12, 7, 3],nums2 = [10, 6, 4, 15, 9]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],nums2 = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],nums2 = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],nums2 = [140000, 130000, 120000, 110000, 100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],nums2 = [140000, 130000, 120000, 110000, 100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],nums2 = [140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],nums2 = [140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 0, 0, 0],nums2 = [0, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 0, 0, 0],nums2 = [0, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [21, 17, 34, 19, 28, 42],nums2 = [45, 39, 27, 51, 18, 32]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [21, 17, 34, 19, 28, 42],nums2 = [45, 39, 27, 51, 18, 32]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 6, 4, 2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18],nums2 = [18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 2, 4, 6, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 6, 4, 2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18],nums2 = [18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 2, 4, 6, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 6, 7, 8, 9, 10, 11, 12, 13],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 6, 7, 8, 9, 10, 11, 12, 13],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192],nums2 = [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192],nums2 = [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 11, 7, 13, 17, 19, 23],nums2 = [29, 25, 21, 15, 13, 11, 7]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 11, 7, 13, 17, 19, 23],nums2 = [29, 25, 21, 15, 13, 11, 7]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7],nums2 = [7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7],nums2 = [7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 23, 45, 6, 78],nums2 = [89, 12, 34, 56, 78]) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 23, 45, 6, 78],nums2 = [89, 12, 34, 56, 78]) == 146: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64],nums2 = [64, 56, 48, 40, 32, 24, 16, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64],nums2 = [64, 56, 48, 40, 32, 24, 16, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000],nums2 = [10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000],nums2 = [10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9876543, 8765432, 7654321, 6543210, 5432109],nums2 = [4321098, 3210987, 2109876, 1098765, 987654]) == 28067535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9876543, 8765432, 7654321, 6543210, 5432109],nums2 = [4321098, 3210987, 2109876, 1098765, 987654]) == 28067535: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 32, 64, 128, 256],nums2 = [256, 128, 64, 32, 16, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 32, 64, 128, 256],nums2 = [256, 128, 64, 32, 16, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1234567, 7654321, 111222333, 444555666, 777888999],nums2 = [999888777, 666555444, 333222111, 210987654, 123456789]) == 1307758981
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1234567, 7654321, 111222333, 444555666, 777888999],nums2 = [999888777, 666555444, 333222111, 210987654, 123456789]) == 1307758981: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10000, 20000, 30000, 40000, 50000],nums2 = [50000, 40000, 30000, 20000, 10000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10000, 20000, 30000, 40000, 50000],nums2 = [50000, 40000, 30000, 20000, 10000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456, 789012, 345678, 901234, 567890, 678901, 789012, 890123, 901234, 123456, 234567, 345678, 456789, 567890],nums2 = [567890, 456789, 345678, 234567, 123456, 901234, 890123, 789012, 678901, 567890, 456789, 345678, 234567, 123456]) == 1656438
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456, 789012, 345678, 901234, 567890, 678901, 789012, 890123, 901234, 123456, 234567, 345678, 456789, 567890],nums2 = [567890, 456789, 345678, 234567, 123456, 901234, 890123, 789012, 678901, 567890, 456789, 345678, 234567, 123456]) == 1656438: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53],nums2 = [53, 49, 45, 41, 37, 33, 29, 25, 21, 17, 13, 9, 5, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53],nums2 = [53, 49, 45, 41, 37, 33, 29, 25, 21, 17, 13, 9, 5, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70],nums2 = [70, 60, 50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70],nums2 = [70, 60, 50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9, 10, 11],nums2 = [11, 10, 9, 8, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9, 10, 11],nums2 = [11, 10, 9, 8, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 5, 7, 11, 13, 17, 19],nums2 = [19, 17, 13, 11, 7, 5, 3, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 5, 7, 11, 13, 17, 19],nums2 = [19, 17, 13, 11, 7, 5, 3, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [10, 8, 6, 4, 2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [10, 8, 6, 4, 2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [256, 512, 1024, 2048, 4096],nums2 = [8192, 4096, 2048, 1024, 512]) == 8448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [256, 512, 1024, 2048, 4096],nums2 = [8192, 4096, 2048, 1024, 512]) == 8448: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],nums2 = [1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],nums2 = [1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],nums2 = [98, 91, 84, 77, 70, 63, 56, 49, 42, 35, 28, 21, 14, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],nums2 = [98, 91, 84, 77, 70, 63, 56, 49, 42, 35, 28, 21, 14, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 10000000, 2, 9999999, 3, 9999998, 4, 9999997, 5, 9999996, 6, 9999995, 7, 9999994, 8],nums2 = [8, 7, 9999994, 9, 6, 9999995, 10, 9999996, 5, 9999997, 4, 9999998, 3, 9999999, 2]) == 10000018
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 10000000, 2, 9999999, 3, 9999998, 4, 9999997, 5, 9999996, 6, 9999995, 7, 9999994, 8],nums2 = [8, 7, 9999994, 9, 6, 9999995, 10, 9999996, 5, 9999997, 4, 9999998, 3, 9999999, 2]) == 10000018: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [23, 34, 45, 56, 67],nums2 = [67, 56, 45, 34, 23]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [23, 34, 45, 56, 67],nums2 = [67, 56, 45, 34, 23]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [13, 11, 9, 7, 5, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [13, 11, 9, 7, 5, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700],nums2 = [700, 600, 500, 400, 300, 200, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700],nums2 = [700, 600, 500, 400, 300, 200, 100]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [3, 4, 2],nums2 = [4, 2, 2]) == 1
    assert candidate(nums1 = [1, 2],nums2 = [2, 3]) == 2
    assert candidate(nums1 = [2, 3, 4, 5],nums2 = [5, 4, 3, 2]) == 0
    assert candidate(nums1 = [4, 6, 2],nums2 = [9, 3, 5]) == 17
    assert candidate(nums1 = [5, 10, 15],nums2 = [15, 10, 5]) == 0
    assert candidate(nums1 = [10, 20, 30],nums2 = [30, 20, 10]) == 0
    assert candidate(nums1 = [1, 2, 3, 4],nums2 = [4, 3, 2, 1]) == 0
    assert candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 0
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0
    assert candidate(nums1 = [5, 3, 4],nums2 = [1, 0, 3]) == 8
    assert candidate(nums1 = [14, 15, 16],nums2 = [13, 14, 15]) == 29
    assert candidate(nums1 = [7, 8, 9],nums2 = [9, 8, 7]) == 0
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [2, 2, 2, 2]) == 12
    assert candidate(nums1 = [7, 8, 9],nums2 = [10, 11, 12]) == 15
    assert candidate(nums1 = [10000000, 10000000, 10000000],nums2 = [10000000, 10000000, 10000000]) == 0
    assert candidate(nums1 = [3, 5, 7, 9],nums2 = [9, 7, 5, 3]) == 0
    assert candidate(nums1 = [0, 1, 2],nums2 = [3, 4, 5]) == 9
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [14, 28, 19],nums2 = [28, 14, 19]) == 0
    assert candidate(nums1 = [1],nums2 = [1]) == 0
    assert candidate(nums1 = [1, 0, 3],nums2 = [5, 3, 4]) == 8
    assert candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 14
    assert candidate(nums1 = [12, 14, 16, 18, 20, 22],nums2 = [21, 19, 17, 15, 13, 11]) == 34
    assert candidate(nums1 = [4, 1, 3, 2],nums2 = [7, 6, 5, 8]) == 18
    assert candidate(nums1 = [9999999, 8888888, 7777777, 6666666, 5555555],nums2 = [4444444, 3333333, 2222222, 1111111, 0]) == 28302135
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128],nums2 = [128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums1 = [7, 23, 15, 4, 8],nums2 = [17, 9, 3, 20, 12]) == 30
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8],nums2 = [8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]) == 115
    assert candidate(nums1 = [10000000, 10000001, 10000002, 10000003, 10000004],nums2 = [10000005, 10000006, 10000007, 10000008, 10000009]) == 25
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 36
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [15, 13, 11, 9, 7, 5, 3, 1]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 119
    assert candidate(nums1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 9999999, 999999, 99999, 9999, 999, 99],nums2 = [99, 999, 9999, 99999, 999999, 9999999, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 45
    assert candidate(nums1 = [7, 8, 9, 10, 11, 12],nums2 = [12, 11, 10, 9, 8, 7]) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 220
    assert candidate(nums1 = [7, 13, 21, 31],nums2 = [3, 8, 15, 28]) == 34
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],nums2 = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],nums2 = [70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],nums2 = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == 32769
    assert candidate(nums1 = [13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],nums2 = [43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71]) == 546
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 15
    assert candidate(nums1 = [7, 8, 9, 10, 11],nums2 = [12, 13, 14, 15, 16]) == 39
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums1 = [10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],nums2 = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10000000]) == 0
    assert candidate(nums1 = [13, 17, 19, 23, 29, 31],nums2 = [31, 29, 23, 19, 17, 13]) == 0
    assert candidate(nums1 = [101, 202, 303, 404, 505, 606, 707, 808, 909],nums2 = [909, 808, 707, 606, 505, 404, 303, 202, 101]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == 24
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 42
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800],nums2 = [800, 700, 600, 500, 400, 300, 200, 100]) == 0
    assert candidate(nums1 = [5, 8, 12, 7, 3],nums2 = [10, 6, 4, 15, 9]) == 15
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],nums2 = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums1 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],nums2 = [140000, 130000, 120000, 110000, 100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 14
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],nums2 = [140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(nums1 = [1, 0, 0, 0],nums2 = [0, 1, 1, 1]) == 2
    assert candidate(nums1 = [21, 17, 34, 19, 28, 42],nums2 = [45, 39, 27, 51, 18, 32]) == 101
    assert candidate(nums1 = [8, 6, 4, 2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18],nums2 = [18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 2, 4, 6, 8]) == 0
    assert candidate(nums1 = [5, 6, 7, 8, 9, 10, 11, 12, 13],nums2 = [13, 12, 11, 10, 9, 8, 7, 6, 5]) == 0
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192],nums2 = [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums1 = [9, 11, 7, 13, 17, 19, 23],nums2 = [29, 25, 21, 15, 13, 11, 7]) == 30
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7],nums2 = [7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums1 = [7, 23, 45, 6, 78],nums2 = [89, 12, 34, 56, 78]) == 146
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 0
    assert candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64],nums2 = [64, 56, 48, 40, 32, 24, 16, 8]) == 0
    assert candidate(nums1 = [10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000],nums2 = [10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000, 0, 10000000]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 15
    assert candidate(nums1 = [9876543, 8765432, 7654321, 6543210, 5432109],nums2 = [4321098, 3210987, 2109876, 1098765, 987654]) == 28067535
    assert candidate(nums1 = [8, 16, 32, 64, 128, 256],nums2 = [256, 128, 64, 32, 16, 8]) == 0
    assert candidate(nums1 = [1234567, 7654321, 111222333, 444555666, 777888999],nums2 = [999888777, 666555444, 333222111, 210987654, 123456789]) == 1307758981
    assert candidate(nums1 = [10000, 20000, 30000, 40000, 50000],nums2 = [50000, 40000, 30000, 20000, 10000]) == 0
    assert candidate(nums1 = [123456, 789012, 345678, 901234, 567890, 678901, 789012, 890123, 901234, 123456, 234567, 345678, 456789, 567890],nums2 = [567890, 456789, 345678, 234567, 123456, 901234, 890123, 789012, 678901, 567890, 456789, 345678, 234567, 123456]) == 1656438
    assert candidate(nums1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53],nums2 = [53, 49, 45, 41, 37, 33, 29, 25, 21, 17, 13, 9, 5, 1]) == 0
    assert candidate(nums1 = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70],nums2 = [70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [50, 40, 30, 20, 10]) == 0
    assert candidate(nums1 = [7, 8, 9, 10, 11],nums2 = [11, 10, 9, 8, 7]) == 0
    assert candidate(nums1 = [2, 3, 5, 7, 11, 13, 17, 19],nums2 = [19, 17, 13, 11, 7, 5, 3, 2]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [10, 8, 6, 4, 2]) == 15
    assert candidate(nums1 = [256, 512, 1024, 2048, 4096],nums2 = [8192, 4096, 2048, 1024, 512]) == 8448
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],nums2 = [1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 0
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],nums2 = [98, 91, 84, 77, 70, 63, 56, 49, 42, 35, 28, 21, 14, 7]) == 0
    assert candidate(nums1 = [1, 10000000, 2, 9999999, 3, 9999998, 4, 9999997, 5, 9999996, 6, 9999995, 7, 9999994, 8],nums2 = [8, 7, 9999994, 9, 6, 9999995, 10, 9999996, 5, 9999997, 4, 9999998, 3, 9999999, 2]) == 10000018
    assert candidate(nums1 = [23, 34, 45, 56, 67],nums2 = [67, 56, 45, 34, 23]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [13, 11, 9, 7, 5, 3, 1]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700],nums2 = [700, 600, 500, 400, 300, 200, 100]) == 0


