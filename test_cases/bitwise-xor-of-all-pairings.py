def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32],nums2 = [4, 8, 12, 16, 20]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32],nums2 = [4, 8, 12, 16, 20]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 1, 3],nums2 = [10, 2, 5, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 1, 3],nums2 = [10, 2, 5, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9],nums2 = [10, 11, 12, 13]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9],nums2 = [10, 11, 12, 13]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [14, 15, 16],nums2 = [17, 18]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [14, 15, 16],nums2 = [17, 18]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5],nums2 = [5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5],nums2 = [5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000],nums2 = [1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000],nums2 = [1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7, 6],nums2 = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7, 6],nums2 = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [9, 8, 7],nums2 = [6, 5, 4, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [9, 8, 7],nums2 = [6, 5, 4, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2],nums2 = [3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2],nums2 = [3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3],nums2 = [6, 5, 4, 3, 2, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3],nums2 = [6, 5, 4, 3, 2, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5],nums2 = [5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5],nums2 = [5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21],nums2 = [3, 6, 9, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21],nums2 = [3, 6, 9, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 29, 37, 41, 53],nums2 = [67, 71, 73, 79, 83, 89, 97, 101]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 29, 37, 41, 53],nums2 = [67, 71, 73, 79, 83, 89, 97, 101]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 11, 13, 14],nums2 = [18, 19, 20, 21, 22]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 11, 13, 14],nums2 = [18, 19, 20, 21, 22]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 682
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 682: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 30, 45, 60, 75],nums2 = [1, 3, 5, 7, 9, 11, 13]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 30, 45, 60, 75],nums2 = [1, 3, 5, 7, 9, 11, 13]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [255, 127, 63, 31],nums2 = [1, 2, 4, 8, 16, 32]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [255, 127, 63, 31],nums2 = [1, 2, 4, 8, 16, 32]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195],nums2 = [199, 299, 399, 499, 599, 699]) == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195],nums2 = [199, 299, 399, 499, 599, 699]) == 380: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000],nums2 = [1000000000, 1000000000, 1000000000, 1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000],nums2 = [1000000000, 1000000000, 1000000000, 1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9, 10],nums2 = [3, 1, 4, 1, 5, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9, 10],nums2 = [3, 1, 4, 1, 5, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1431655765, 1431655765, 1431655765, 1431655765],nums2 = [1431655765]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1431655765, 1431655765, 1431655765, 1431655765],nums2 = [1431655765]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [1, 3, 5, 7, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [1, 3, 5, 7, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300],nums2 = [101, 202, 303, 404]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300],nums2 = [101, 202, 303, 404]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456789, 987654321, 1122334455],nums2 = [554433221, 987654321, 123456789, 1000000000]) == 655660385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456789, 987654321, 1122334455],nums2 = [554433221, 987654321, 123456789, 1000000000]) == 655660385: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000],nums2 = [500000000, 600000000, 700000000, 800000000, 900000000]) == 908472064
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000],nums2 = [500000000, 600000000, 700000000, 800000000, 900000000]) == 908472064: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300],nums2 = [101, 202, 303, 404, 505]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300],nums2 = [101, 202, 303, 404, 505]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90],nums2 = [96, 102, 108, 114, 120, 126]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90],nums2 = [96, 102, 108, 114, 120, 126]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [255, 254, 253, 252, 251],nums2 = [127, 63, 31, 15, 7]) == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [255, 254, 253, 252, 251],nums2 = [127, 63, 31, 15, 7]) == 172: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 255, 511, 1023, 2047],nums2 = [1, 128, 256, 512, 1024]) == 641
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 255, 511, 1023, 2047],nums2 = [1, 128, 256, 512, 1024]) == 641: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1000000000],nums2 = [1, 1000000000, 1000000000, 1000000000, 1000000000]) == 1000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1000000000],nums2 = [1, 1000000000, 1000000000, 1000000000, 1000000000]) == 1000000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 15, 21],nums2 = [9, 3, 12, 8]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 15, 21],nums2 = [9, 3, 12, 8]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [255, 128, 64, 32, 16],nums2 = [1, 2, 4, 8, 16, 32]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [255, 128, 64, 32, 16],nums2 = [1, 2, 4, 8, 16, 32]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999999, 888888888, 777777777],nums2 = [666666666, 555555555, 444444444, 333333333, 222222222]) == 587645496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999999, 888888888, 777777777],nums2 = [666666666, 555555555, 444444444, 333333333, 222222222]) == 587645496: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456789, 987654321, 456789123],nums2 = [321654987, 789123456, 654987321, 123456789]) == 477404263
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456789, 987654321, 456789123],nums2 = [321654987, 789123456, 654987321, 123456789]) == 477404263: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2046
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2046: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 17, 19, 23, 29, 31],nums2 = [37, 41, 43, 47, 53, 59, 61, 67, 71]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 17, 19, 23, 29, 31],nums2 = [37, 41, 43, 47, 53, 59, 61, 67, 71]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000],nums2 = [1000000000, 1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000],nums2 = [1000000000, 1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 29, 31, 47, 53, 59, 61, 67, 71, 73],nums2 = [79, 83, 89, 97, 101, 103, 107, 109, 113, 127]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 29, 31, 47, 53, 59, 61, 67, 71, 73],nums2 = [79, 83, 89, 97, 101, 103, 107, 109, 113, 127]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [255, 128, 64, 32, 16, 8, 4, 2, 1],nums2 = [1, 3, 7, 15, 31, 63, 127, 255]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [255, 128, 64, 32, 16, 8, 4, 2, 1],nums2 = [1, 3, 7, 15, 31, 63, 127, 255]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [255, 511, 765, 1023, 1279],nums2 = [15, 31, 47, 63, 79]) == 1202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [255, 511, 765, 1023, 1279],nums2 = [15, 31, 47, 63, 79]) == 1202: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [255, 128, 64, 32, 16, 8, 4, 2, 1],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [255, 128, 64, 32, 16, 8, 4, 2, 1],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456789],nums2 = [987654321, 1122334455, 6677889900]) == 8345112639
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456789],nums2 = [987654321, 1122334455, 6677889900]) == 8345112639: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [999999999, 888888888, 777777777, 666666666],nums2 = [555555555, 444444444, 333333333, 222222222]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [999999999, 888888888, 777777777, 666666666],nums2 = [555555555, 444444444, 333333333, 222222222]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000000, 2000000000, 3000000000],nums2 = [1, 1000000000, 2000000000]) == 3000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000000, 2000000000, 3000000000],nums2 = [1, 1000000000, 2000000000]) == 3000000001: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [666],nums2 = [666, 666, 666, 666, 666, 666]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [666],nums2 = [666, 666, 666, 666, 666, 666]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1024, 2048, 4096, 8192, 16384],nums2 = [1, 2, 4, 8, 16]) == 31775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1024, 2048, 4096, 8192, 16384],nums2 = [1, 2, 4, 8, 16]) == 31775: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [3, 6, 9, 12, 15]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [3, 6, 9, 12, 15]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [1024, 2048, 4096, 8192, 16384]) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [1024, 2048, 4096, 8192, 16384]) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456789, 987654321],nums2 = [1000000007, 1111111111]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456789, 987654321],nums2 = [1000000007, 1111111111]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [50, 60, 70]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [50, 60, 70]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [255, 128, 64, 32],nums2 = [16, 8, 4, 2, 1]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [255, 128, 64, 32],nums2 = [16, 8, 4, 2, 1]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [111, 222, 333, 444, 555, 666, 777, 888, 999],nums2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 707
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [111, 222, 333, 444, 555, 666, 777, 888, 999],nums2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 707: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [123456789, 987654321, 111111111, 222222222],nums2 = [333333333, 444444444, 555555555]) == 908335597
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [123456789, 987654321, 111111111, 222222222],nums2 = [333333333, 444444444, 555555555]) == 908335597: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6],nums2 = [7, 8, 9, 10, 11, 12, 13]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6],nums2 = [7, 8, 9, 10, 11, 12, 13]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000000, 2000000, 3000000, 4000000],nums2 = [500000, 600000, 700000]) == 67840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000000, 2000000, 3000000, 4000000],nums2 = [500000, 600000, 700000]) == 67840: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300],nums2 = [50, 150, 250, 350, 450]) == 322
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300],nums2 = [50, 150, 250, 350, 450]) == 322: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2147483647, 2147483646, 2147483645],nums2 = [1073741823, 1073741824, 1073741825]) == 1073741826
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2147483647, 2147483646, 2147483645],nums2 = [1073741823, 1073741824, 1073741825]) == 1073741826: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113],nums2 = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113],nums2 = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 14, 15, 16, 17, 18, 19, 20],nums2 = [21, 22, 23, 24, 25, 26, 27, 28]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 14, 15, 16, 17, 18, 19, 20],nums2 = [21, 22, 23, 24, 25, 26, 27, 28]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 23, 42, 8, 16],nums2 = [32, 19, 10, 7, 11]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 23, 42, 8, 16],nums2 = [32, 19, 10, 7, 11]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10, 12, 14]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10, 12, 14]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1024, 512, 256, 128],nums2 = [64, 32, 16, 8, 4, 2, 1]) == 1920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1024, 512, 256, 128],nums2 = [64, 32, 16, 8, 4, 2, 1]) == 1920: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [8, 16, 24, 32],nums2 = [4, 8, 12, 16, 20]) == 32
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1]) == 11
    assert candidate(nums1 = [2, 1, 3],nums2 = [10, 2, 5, 0]) == 13
    assert candidate(nums1 = [7, 8, 9],nums2 = [10, 11, 12, 13]) == 0
    assert candidate(nums1 = [14, 15, 16],nums2 = [17, 18]) == 3
    assert candidate(nums1 = [5],nums2 = [5]) == 0
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0
    assert candidate(nums1 = [1, 1, 1],nums2 = [1, 1, 1]) == 0
    assert candidate(nums1 = [1, 3, 5, 7],nums2 = [2, 4, 6, 8]) == 0
    assert candidate(nums1 = [1],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [1000000000],nums2 = [1000000000]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums1 = [9, 8, 7, 6],nums2 = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums1 = [9, 8, 7],nums2 = [6, 5, 4, 3, 2, 1]) == 7
    assert candidate(nums1 = [1, 2],nums2 = [3, 4]) == 0
    assert candidate(nums1 = [1],nums2 = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums1 = [1, 2, 3],nums2 = [6, 5, 4, 3, 2, 1]) == 7
    assert candidate(nums1 = [0, 0, 0],nums2 = [0, 0, 0]) == 0
    assert candidate(nums1 = [5],nums2 = [5, 5, 5, 5, 5]) == 0
    assert candidate(nums1 = [7, 14, 21],nums2 = [3, 6, 9, 12]) == 0
    assert candidate(nums1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],nums2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 0
    assert candidate(nums1 = [13, 29, 37, 41, 53],nums2 = [67, 71, 73, 79, 83, 89, 97, 101]) == 12
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [7, 11, 13, 14],nums2 = [18, 19, 20, 21, 22]) == 15
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums1 = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 682
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1]) == 0
    assert candidate(nums1 = [15, 30, 45, 60, 75],nums2 = [1, 3, 5, 7, 9, 11, 13]) == 68
    assert candidate(nums1 = [255, 127, 63, 31],nums2 = [1, 2, 4, 8, 16, 32]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums1 = [7, 8, 9, 10],nums2 = [11, 12, 13, 14, 15]) == 12
    assert candidate(nums1 = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195],nums2 = [199, 299, 399, 499, 599, 699]) == 380
    assert candidate(nums1 = [1000000000],nums2 = [1000000000, 1000000000, 1000000000, 1000000000]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 31
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(nums1 = [7, 8, 9, 10],nums2 = [3, 1, 4, 1, 5, 9]) == 0
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums1 = [1431655765, 1431655765, 1431655765, 1431655765],nums2 = [1431655765]) == 0
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [1, 3, 5, 7, 9]) == 1
    assert candidate(nums1 = [100, 200, 300],nums2 = [101, 202, 303, 404]) == 20
    assert candidate(nums1 = [123456789, 987654321, 1122334455],nums2 = [554433221, 987654321, 123456789, 1000000000]) == 655660385
    assert candidate(nums1 = [0, 0, 0, 0, 0],nums2 = [1, 2, 3, 4, 5]) == 1
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == 0
    assert candidate(nums1 = [1000000000],nums2 = [500000000, 600000000, 700000000, 800000000, 900000000]) == 908472064
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums1 = [100, 200, 300],nums2 = [101, 202, 303, 404, 505]) == 109
    assert candidate(nums1 = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90],nums2 = [96, 102, 108, 114, 120, 126]) == 30
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums1 = [255, 254, 253, 252, 251],nums2 = [127, 63, 31, 15, 7]) == 172
    assert candidate(nums1 = [0, 255, 511, 1023, 2047],nums2 = [1, 128, 256, 512, 1024]) == 641
    assert candidate(nums1 = [1, 1000000000],nums2 = [1, 1000000000, 1000000000, 1000000000, 1000000000]) == 1000000001
    assert candidate(nums1 = [7, 15, 21],nums2 = [9, 3, 12, 8]) == 14
    assert candidate(nums1 = [255, 128, 64, 32, 16],nums2 = [1, 2, 4, 8, 16, 32]) == 63
    assert candidate(nums1 = [999999999, 888888888, 777777777],nums2 = [666666666, 555555555, 444444444, 333333333, 222222222]) == 587645496
    assert candidate(nums1 = [123456789, 987654321, 456789123],nums2 = [321654987, 789123456, 654987321, 123456789]) == 477404263
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2046
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13],nums2 = [2, 4, 6, 8, 10, 12, 14, 16]) == 16
    assert candidate(nums1 = [13, 17, 19, 23, 29, 31],nums2 = [37, 41, 43, 47, 53, 59, 61, 67, 71]) == 26
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 0
    assert candidate(nums1 = [1000000000],nums2 = [1000000000, 1000000000]) == 0
    assert candidate(nums1 = [13, 29, 31, 47, 53, 59, 61, 67, 71, 73],nums2 = [79, 83, 89, 97, 101, 103, 107, 109, 113, 127]) == 0
    assert candidate(nums1 = [255, 128, 64, 32, 16, 8, 4, 2, 1],nums2 = [1, 3, 7, 15, 31, 63, 127, 255]) == 170
    assert candidate(nums1 = [255, 511, 765, 1023, 1279],nums2 = [15, 31, 47, 63, 79]) == 1202
    assert candidate(nums1 = [255, 128, 64, 32, 16, 8, 4, 2, 1],nums2 = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == 17
    assert candidate(nums1 = [7, 8, 9, 10],nums2 = [1, 2, 3, 4, 5, 6]) == 0
    assert candidate(nums1 = [123456789],nums2 = [987654321, 1122334455, 6677889900]) == 8345112639
    assert candidate(nums1 = [999999999, 888888888, 777777777, 666666666],nums2 = [555555555, 444444444, 333333333, 222222222]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10]) == 11
    assert candidate(nums1 = [1000000000, 2000000000, 3000000000],nums2 = [1, 1000000000, 2000000000]) == 3000000001
    assert candidate(nums1 = [1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [666],nums2 = [666, 666, 666, 666, 666, 666]) == 0
    assert candidate(nums1 = [1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [500, 400, 300, 200, 100]) == 0
    assert candidate(nums1 = [1024, 2048, 4096, 8192, 16384],nums2 = [1, 2, 4, 8, 16]) == 31775
    assert candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [3, 6, 9, 12, 15]) == 12
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [1024, 2048, 4096, 8192, 16384]) == 1023
    assert candidate(nums1 = [123456789, 987654321],nums2 = [1000000007, 1111111111]) == 0
    assert candidate(nums1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]) == 0
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [50, 60, 70]) == 16
    assert candidate(nums1 = [255, 128, 64, 32],nums2 = [16, 8, 4, 2, 1]) == 31
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [0, 0, 0, 0]) == 0
    assert candidate(nums1 = [111, 222, 333, 444, 555, 666, 777, 888, 999],nums2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 707
    assert candidate(nums1 = [123456789, 987654321, 111111111, 222222222],nums2 = [333333333, 444444444, 555555555]) == 908335597
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6],nums2 = [7, 8, 9, 10, 11, 12, 13]) == 1
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [2, 2, 2, 2, 2]) == 3
    assert candidate(nums1 = [1000000, 2000000, 3000000, 4000000],nums2 = [500000, 600000, 700000]) == 67840
    assert candidate(nums1 = [100, 200, 300],nums2 = [50, 150, 250, 350, 450]) == 322
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11],nums2 = [2, 4, 6, 8, 10]) == 2
    assert candidate(nums1 = [2147483647, 2147483646, 2147483645],nums2 = [1073741823, 1073741824, 1073741825]) == 1073741826
    assert candidate(nums1 = [13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113],nums2 = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111]) == 42
    assert candidate(nums1 = [0, 0, 0, 0],nums2 = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums1 = [13, 14, 15, 16, 17, 18, 19, 20],nums2 = [21, 22, 23, 24, 25, 26, 27, 28]) == 0
    assert candidate(nums1 = [15, 23, 42, 8, 16],nums2 = [32, 19, 10, 7, 11]) == 31
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [2, 4, 6, 8, 10, 12, 14]) == 9
    assert candidate(nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(nums1 = [1024, 512, 256, 128],nums2 = [64, 32, 16, 8, 4, 2, 1]) == 1920


