def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 7],nums2 = [9, 25, 49]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 7],nums2 = [9, 25, 49]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [25, 25, 25, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [25, 25, 25, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 5, 2],nums2 = [100, 25, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 5, 2],nums2 = [100, 25, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 5],nums2 = [2, 5, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 5],nums2 = [2, 5, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 2, 2, 2],nums2 = [4, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 2, 2, 2],nums2 = [4, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 4],nums2 = [5, 2, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 4],nums2 = [5, 2, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3],nums2 = [3, 3, 3, 3]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3],nums2 = [3, 3, 3, 3]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 4, 9, 16, 25]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 4, 9, 16, 25]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 10, 15],nums2 = [36, 100, 225]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 10, 15],nums2 = [36, 100, 225]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10],nums2 = [10, 10, 10, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10],nums2 = [10, 10, 10, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5],nums2 = [5, 5, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5],nums2 = [5, 5, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 7, 8, 3],nums2 = [1, 2, 9, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 7, 8, 3],nums2 = [1, 2, 9, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3],nums2 = [9, 9, 9, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3],nums2 = [9, 9, 9, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000],nums2 = [1, 10, 100, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000],nums2 = [1, 10, 100, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 5],nums2 = [4, 9, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 5],nums2 = [4, 9, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 15, 9],nums2 = [9, 25, 36]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 15, 9],nums2 = [9, 25, 36]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 4],nums2 = [1, 5, 6, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 4],nums2 = [1, 5, 6, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10],nums2 = [10, 10, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10],nums2 = [10, 10, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1],nums2 = [1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1],nums2 = [1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 5, 3],nums2 = [2, 4, 8, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 5, 3],nums2 = [2, 4, 8, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1],nums2 = [1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1],nums2 = [1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 9, 27, 81],nums2 = [9, 81, 243, 729, 2187, 6561]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 9, 27, 81],nums2 = [9, 81, 243, 729, 2187, 6561]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 22, 33, 44],nums2 = [121, 484, 726, 1936, 2904]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 22, 33, 44],nums2 = [121, 484, 726, 1936, 2904]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25, 25, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25, 25, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 10, 12, 15],nums2 = [36, 100, 144, 225, 150]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 10, 12, 15],nums2 = [36, 100, 144, 225, 150]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [10000, 40000, 90000, 160000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [10000, 40000, 90000, 160000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3, 3, 3],nums2 = [9, 9, 9, 9, 9, 9, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3, 3, 3],nums2 = [9, 9, 9, 9, 9, 9, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3, 3, 3],nums2 = [1, 4, 4, 9, 9, 9, 9]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3, 3, 3],nums2 = [1, 4, 4, 9, 9, 9, 9]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 9, 27, 81, 243, 729],nums2 = [9, 27, 81, 243, 729, 2187]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 9, 27, 81, 243, 729],nums2 = [9, 27, 81, 243, 729, 2187]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [10000, 40000, 90000, 160000, 250000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [10000, 40000, 90000, 160000, 250000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],nums2 = [49, 196, 441, 784, 1225, 1764, 2401, 3136, 3969, 4900, 5929, 7056, 8281, 9604, 11025]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],nums2 = [49, 196, 441, 784, 1225, 1764, 2401, 3136, 3969, 4900, 5929, 7056, 8281, 9604, 11025]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],nums2 = [169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],nums2 = [169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [4, 8, 12, 16, 20],nums2 = [16, 64, 144, 256, 400, 625, 1024]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [4, 8, 12, 16, 20],nums2 = [16, 64, 144, 256, 400, 625, 1024]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [4, 16, 36, 64, 100, 144, 196]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [4, 16, 36, 64, 100, 144, 196]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 10, 15],nums2 = [36, 100, 150, 225]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 10, 15],nums2 = [36, 100, 150, 225]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [13, 169, 2197, 28561, 371293, 4826809, 62748517, 815730721, 10604499373],nums2 = [169, 2197, 28561, 371293, 4826809, 62748517, 815730721, 10604499373, 13841287201]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [13, 169, 2197, 28561, 371293, 4826809, 62748517, 815730721, 10604499373],nums2 = [169, 2197, 28561, 371293, 4826809, 62748517, 815730721, 10604499373, 13841287201]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 12, 18, 24],nums2 = [36, 144, 324, 576, 864, 1152, 1440]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 12, 18, 24],nums2 = [36, 144, 324, 576, 864, 1152, 1440]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15, 18],nums2 = [9, 36, 81, 144, 225, 324, 441]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15, 18],nums2 = [9, 36, 81, 144, 225, 324, 441]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 9, 12, 15, 18],nums2 = [64, 81, 144, 225, 324]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 9, 12, 15, 18],nums2 = [64, 81, 144, 225, 324]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [25, 100, 225, 400, 625]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [25, 100, 225, 400, 625]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [25, 100, 225, 400, 625, 900]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [25, 100, 225, 400, 625, 900]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [1, 9, 25, 49, 81]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [1, 9, 25, 49, 81]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4],nums2 = [1, 1, 4, 4, 9, 9, 16, 16]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4],nums2 = [1, 1, 4, 4, 9, 9, 16, 16]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12],nums2 = [4, 16, 36, 64, 100, 144, 256]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12],nums2 = [4, 16, 36, 64, 100, 144, 256]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 100, 1000, 10000, 100000],nums2 = [100, 10000, 1000000, 100000000, 10000000000]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 100, 1000, 10000, 100000],nums2 = [100, 10000, 1000000, 100000000, 10000000000]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [12, 15, 20, 25, 30],nums2 = [144, 225, 400, 625, 900]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [12, 15, 20, 25, 30],nums2 = [144, 225, 400, 625, 900]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 11, 121, 1331, 14641],nums2 = [121, 1331, 14641, 161051, 1771561]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 11, 121, 1331, 14641],nums2 = [121, 1331, 14641, 161051, 1771561]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 3, 3, 3, 3, 3],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 3, 3, 3, 3, 3],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249],nums2 = [49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249, 2004761894]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249],nums2 = [49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249, 2004761894]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 6, 9, 12, 15, 18],nums2 = [9, 36, 81, 144, 225, 324]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 6, 9, 12, 15, 18],nums2 = [9, 36, 81, 144, 225, 324]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],nums2 = [36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],nums2 = [36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],nums2 = [1, 1, 1, 4, 4, 4, 9, 9, 9, 16, 16, 16, 1]) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],nums2 = [1, 1, 1, 4, 4, 4, 9, 9, 9, 16, 16, 16, 1]) == 156: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [1000000, 4000000, 9000000, 16000000, 25000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [1000000, 4000000, 9000000, 16000000, 25000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 12100, 14400, 16900, 19600, 22500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 12100, 14400, 16900, 19600, 22500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 4, 8, 16, 32],nums2 = [1, 1, 4, 4, 16, 16, 64]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 4, 8, 16, 32],nums2 = [1, 1, 4, 4, 16, 16, 64]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [100, 400, 900, 1600, 2500, 50, 250, 1250, 6250]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [100, 400, 900, 1600, 2500, 50, 250, 1250, 6250]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400],nums2 = [10000, 40000, 90000, 160000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400],nums2 = [10000, 40000, 90000, 160000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],nums2 = [4, 9, 25, 49, 121, 169, 289, 361, 529, 841]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],nums2 = [4, 9, 25, 49, 121, 169, 289, 361, 529, 841]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 49, 343, 2401],nums2 = [49, 343, 2401, 16807]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 49, 343, 2401],nums2 = [49, 343, 2401, 16807]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [25, 50, 75, 100, 125, 150]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [25, 50, 75, 100, 125, 150]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 15, 17, 20],nums2 = [64, 225, 289, 400, 676, 841]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 15, 17, 20],nums2 = [64, 225, 289, 400, 676, 841]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 6, 6, 6, 6],nums2 = [36, 36, 36, 36, 36]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 6, 6, 6, 6],nums2 = [36, 36, 36, 36, 36]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11550: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 11, 13, 17, 19, 23, 29, 31, 37],nums2 = [49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 11, 13, 17, 19, 23, 29, 31, 37],nums2 = [49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 8, 16, 32, 64],nums2 = [4, 16, 64, 256, 1024, 4096, 16384]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 8, 16, 32, 64],nums2 = [4, 16, 64, 256, 1024, 4096, 16384]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [100, 225, 400, 625, 900, 1225, 1600, 2025, 2500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [100, 225, 400, 625, 900, 1225, 1600, 2025, 2500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 24, 25, 30],nums2 = [49, 576, 625, 900, 1440, 1800]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 24, 25, 30],nums2 = [49, 576, 625, 900, 1440, 1800]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 5, 7, 11, 13, 17],nums2 = [4, 9, 25, 49, 121, 169, 289]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 5, 7, 11, 13, 17],nums2 = [4, 9, 25, 49, 121, 169, 289]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [49, 121, 169, 289, 361, 529]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [49, 121, 169, 289, 361, 529]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 3, 3, 3, 1],nums2 = [1, 9, 9, 1, 1, 9]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 3, 3, 3, 1],nums2 = [1, 9, 9, 1, 1, 9]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [10000, 40000, 90000, 160000, 250000, 360000, 490000, 640000, 810000, 1000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [10000, 40000, 90000, 160000, 250000, 360000, 490000, 640000, 810000, 1000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3, 3, 3],nums2 = [1, 1, 2, 2, 3, 3]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3, 3, 3],nums2 = [1, 1, 2, 2, 3, 3]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],nums2 = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 563
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],nums2 = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 563: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [1, 1, 1, 4, 4, 9]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [1, 1, 1, 4, 4, 9]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 9, 27, 81, 243],nums2 = [27, 81, 243, 729, 2187]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 9, 27, 81, 243],nums2 = [27, 81, 243, 729, 2187]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [31, 37, 41, 43, 47, 53, 59],nums2 = [961, 1369, 1681, 1849, 2209, 2809, 3481]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [31, 37, 41, 43, 47, 53, 59],nums2 = [961, 1369, 1681, 1849, 2209, 2809, 3481]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 8, 16, 32, 64, 128, 256],nums2 = [4, 16, 64, 256, 1024, 4096]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 8, 16, 32, 64, 128, 256],nums2 = [4, 16, 64, 256, 1024, 4096]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 2, 2, 2],nums2 = [4, 4, 4, 4, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 2, 2, 2],nums2 = [4, 4, 4, 4, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 8, 16, 32, 64],nums2 = [4, 16, 64, 256, 1024, 4096]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 8, 16, 32, 64],nums2 = [4, 16, 64, 256, 1024, 4096]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 6, 6, 6, 6, 6],nums2 = [36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 6, 6, 6, 6, 6],nums2 = [36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [25, 100, 225, 400, 625, 900, 1225, 1600, 2025, 2500]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [25, 100, 225, 400, 625, 900, 1225, 1600, 2025, 2500]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 8, 12, 15, 17, 20],nums2 = [9, 25, 64, 144, 225, 289, 400]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 8, 12, 15, 17, 20],nums2 = [9, 25, 64, 144, 225, 289, 400]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 20, 25, 30],nums2 = [225, 400, 625, 900, 1200, 1800]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 20, 25, 30],nums2 = [225, 400, 625, 900, 1200, 1800]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 10, 10],nums2 = [100, 100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 10, 10],nums2 = [100, 100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [49, 121, 169, 289, 361]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [49, 121, 169, 289, 361]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 7, 8],nums2 = [36, 49, 64, 84, 112]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 7, 8],nums2 = [36, 49, 64, 84, 112]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 3, 5, 7, 11],nums2 = [4, 6, 9, 10, 14, 15, 21, 22, 30, 33, 35, 55, 77, 105]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 3, 5, 7, 11],nums2 = [4, 6, 9, 10, 14, 15, 21, 22, 30, 33, 35, 55, 77, 105]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [100, 400, 900, 1600, 2500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [100, 400, 900, 1600, 2500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],nums2 = [121, 484, 1089, 1936, 3025, 4356, 5929, 7744, 9801, 12100, 14641, 17424, 20736, 24336, 28081]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],nums2 = [121, 484, 1089, 1936, 3025, 4356, 5929, 7744, 9801, 12100, 14641, 17424, 20736, 24336, 28081]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [10, 20, 30, 40],nums2 = [100, 400, 900, 1600, 2500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [10, 20, 30, 40],nums2 = [100, 400, 900, 1600, 2500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 8, 10, 12, 14],nums2 = [36, 64, 100, 144, 196, 256]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 8, 10, 12, 14],nums2 = [36, 64, 100, 144, 196, 256]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [15, 25, 35, 45, 55],nums2 = [225, 625, 1225, 2025, 3025, 450, 750, 1050, 1350, 1650]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [15, 25, 35, 45, 55],nums2 = [225, 625, 1225, 2025, 3025, 450, 750, 1050, 1350, 1650]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [100000, 99999, 99998, 99997, 99996],nums2 = [10000000000, 9999800001, 9999600004, 9999400009, 9999200016]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [100000, 99999, 99998, 99997, 99996],nums2 = [10000000000, 9999800001, 9999600004, 9999400009, 9999200016]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 8, 10, 12, 14],nums2 = [36, 64, 100, 144, 196, 48, 72, 96, 112, 120]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 8, 10, 12, 14],nums2 = [36, 64, 100, 144, 196, 48, 72, 96, 112, 120]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],nums2 = [64, 256, 576, 1024, 1600, 2304, 3136, 4096, 5184, 6400]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],nums2 = [64, 256, 576, 1024, 1600, 2304, 3136, 4096, 5184, 6400]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [6, 10, 14, 18, 22, 26, 30],nums2 = [36, 100, 196, 324, 484, 676, 900]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [6, 10, 14, 18, 22, 26, 30],nums2 = [36, 100, 196, 324, 484, 676, 900]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [3, 5, 7, 11, 13],nums2 = [9, 25, 49, 121, 169, 289]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [3, 5, 7, 11, 13],nums2 = [9, 25, 49, 121, 169, 289]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 11, 13, 17, 19, 23, 29],nums2 = [49, 121, 169, 289, 361, 529, 841]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 11, 13, 17, 19, 23, 29],nums2 = [49, 121, 169, 289, 361, 529, 841]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [5, 12, 13, 15],nums2 = [25, 144, 169, 225, 441]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [5, 12, 13, 15],nums2 = [25, 144, 169, 225, 441]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [11, 13, 17, 19],nums2 = [121, 169, 289, 361, 441, 529]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [11, 13, 17, 19],nums2 = [121, 169, 289, 361, 441, 529]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [1, 2, 2, 3, 3, 3, 4],nums2 = [1, 4, 4, 9, 9, 16]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [1, 2, 2, 3, 3, 3, 4],nums2 = [1, 4, 4, 9, 9, 16]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [49, 121, 169, 289, 361, 441]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [49, 121, 169, 289, 361, 441]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums1 = [3, 5, 7],nums2 = [9, 25, 49]) == 0
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [25, 25, 25, 25]) == 0
    assert candidate(nums1 = [10, 5, 2],nums2 = [100, 25, 4]) == 1
    assert candidate(nums1 = [2, 3, 5],nums2 = [2, 5, 10]) == 0
    assert candidate(nums1 = [2, 2, 2, 2],nums2 = [4, 4, 4]) == 0
    assert candidate(nums1 = [7, 4],nums2 = [5, 2, 8, 9]) == 1
    assert candidate(nums1 = [3, 3, 3],nums2 = [3, 3, 3, 3]) == 30
    assert candidate(nums1 = [1, 2, 3, 4, 5],nums2 = [1, 4, 9, 16, 25]) == 4
    assert candidate(nums1 = [6, 10, 15],nums2 = [36, 100, 225]) == 0
    assert candidate(nums1 = [10, 10, 10],nums2 = [10, 10, 10, 10]) == 30
    assert candidate(nums1 = [5],nums2 = [5, 5, 5]) == 3
    assert candidate(nums1 = [7, 7, 8, 3],nums2 = [1, 2, 9, 7]) == 2
    assert candidate(nums1 = [3, 3, 3, 3],nums2 = [9, 9, 9, 9]) == 0
    assert candidate(nums1 = [1000],nums2 = [1, 10, 100, 1000]) == 0
    assert candidate(nums1 = [2, 3, 5],nums2 = [4, 9, 25]) == 0
    assert candidate(nums1 = [3, 15, 9],nums2 = [9, 25, 36]) == 1
    assert candidate(nums1 = [2, 3, 4],nums2 = [1, 5, 6, 10]) == 0
    assert candidate(nums1 = [10, 10, 10],nums2 = [10, 10, 10]) == 18
    assert candidate(nums1 = [1],nums2 = [1, 1, 1, 1, 1]) == 10
    assert candidate(nums1 = [10, 5, 3],nums2 = [2, 4, 8, 16]) == 0
    assert candidate(nums1 = [1, 1],nums2 = [1, 1, 1]) == 9
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]) == 10
    assert candidate(nums1 = [3, 9, 27, 81],nums2 = [9, 81, 243, 729, 2187, 6561]) == 3
    assert candidate(nums1 = [11, 22, 33, 44],nums2 = [121, 484, 726, 1936, 2904]) == 0
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25, 25, 25]) == 0
    assert candidate(nums1 = [6, 10, 12, 15],nums2 = [36, 100, 144, 225, 150]) == 0
    assert candidate(nums1 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) == 0
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [10000, 40000, 90000, 160000]) == 0
    assert candidate(nums1 = [3, 3, 3, 3, 3, 3],nums2 = [9, 9, 9, 9, 9, 9, 9]) == 0
    assert candidate(nums1 = [1, 2, 2, 3, 3, 3],nums2 = [1, 4, 4, 9, 9, 9, 9]) == 16
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 900
    assert candidate(nums1 = [3, 9, 27, 81, 243, 729],nums2 = [9, 27, 81, 243, 729, 2187]) == 12
    assert candidate(nums1 = [100, 200, 300, 400, 500],nums2 = [10000, 40000, 90000, 160000, 250000]) == 0
    assert candidate(nums1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],nums2 = [49, 196, 441, 784, 1225, 1764, 2401, 3136, 3969, 4900, 5929, 7056, 8281, 9604, 11025]) == 1
    assert candidate(nums1 = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],nums2 = [169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169]) == 0
    assert candidate(nums1 = [4, 8, 12, 16, 20],nums2 = [16, 64, 144, 256, 400, 625, 1024]) == 0
    assert candidate(nums1 = [2, 4, 6, 8, 10],nums2 = [4, 16, 36, 64, 100, 144, 196]) == 2
    assert candidate(nums1 = [5, 5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25, 25]) == 0
    assert candidate(nums1 = [6, 10, 15],nums2 = [36, 100, 150, 225]) == 0
    assert candidate(nums1 = [13, 169, 2197, 28561, 371293, 4826809, 62748517, 815730721, 10604499373],nums2 = [169, 2197, 28561, 371293, 4826809, 62748517, 815730721, 10604499373, 13841287201]) == 28
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 13
    assert candidate(nums1 = [6, 12, 18, 24],nums2 = [36, 144, 324, 576, 864, 1152, 1440]) == 0
    assert candidate(nums1 = [3, 6, 9, 12, 15, 18],nums2 = [9, 36, 81, 144, 225, 324, 441]) == 1
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1]) == 220
    assert candidate(nums1 = [8, 9, 12, 15, 18],nums2 = [64, 81, 144, 225, 324]) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [25, 100, 225, 400, 625]) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30],nums2 = [25, 100, 225, 400, 625, 900]) == 0
    assert candidate(nums1 = [1, 3, 5, 7, 9],nums2 = [1, 9, 25, 49, 81]) == 4
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3, 4, 4],nums2 = [1, 1, 4, 4, 9, 9, 16, 16]) == 32
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12],nums2 = [4, 16, 36, 64, 100, 144, 256]) == 3
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],nums2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]) == 13
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]) == 5
    assert candidate(nums1 = [10, 100, 1000, 10000, 100000],nums2 = [100, 10000, 1000000, 100000000, 10000000000]) == 6
    assert candidate(nums1 = [12, 15, 20, 25, 30],nums2 = [144, 225, 400, 625, 900]) == 0
    assert candidate(nums1 = [5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25]) == 0
    assert candidate(nums1 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 0
    assert candidate(nums1 = [11, 11, 121, 1331, 14641],nums2 = [121, 1331, 14641, 161051, 1771561]) == 6
    assert candidate(nums1 = [3, 3, 3, 3, 3, 3],nums2 = [9, 9, 9, 9, 9, 9, 9, 9, 9]) == 0
    assert candidate(nums1 = [7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249],nums2 = [49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249, 2004761894]) == 36
    assert candidate(nums1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],nums2 = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]) == 10
    assert candidate(nums1 = [3, 6, 9, 12, 15, 18],nums2 = [9, 36, 81, 144, 225, 324]) == 1
    assert candidate(nums1 = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],nums2 = [36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36]) == 0
    assert candidate(nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],nums2 = [1, 1, 1, 4, 4, 4, 9, 9, 9, 16, 16, 16, 1]) == 156
    assert candidate(nums1 = [1000, 2000, 3000, 4000, 5000],nums2 = [1000000, 4000000, 9000000, 16000000, 25000000]) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],nums2 = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 12100, 14400, 16900, 19600, 22500]) == 0
    assert candidate(nums1 = [1, 2, 2, 4, 8, 16, 32],nums2 = [1, 1, 4, 4, 16, 16, 64]) == 33
    assert candidate(nums1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],nums2 = [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]) == 5
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [100, 400, 900, 1600, 2500, 50, 250, 1250, 6250]) == 0
    assert candidate(nums1 = [100, 200, 300, 400],nums2 = [10000, 40000, 90000, 160000]) == 0
    assert candidate(nums1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],nums2 = [4, 9, 25, 49, 121, 169, 289, 361, 529, 841]) == 0
    assert candidate(nums1 = [7, 49, 343, 2401],nums2 = [49, 343, 2401, 16807]) == 4
    assert candidate(nums1 = [1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 325
    assert candidate(nums1 = [5, 10, 15, 20, 25],nums2 = [25, 50, 75, 100, 125, 150]) == 0
    assert candidate(nums1 = [8, 15, 17, 20],nums2 = [64, 225, 289, 400, 676, 841]) == 0
    assert candidate(nums1 = [2, 4, 8, 16, 32, 64, 128, 256, 512],nums2 = [4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576]) == 24
    assert candidate(nums1 = [6, 6, 6, 6, 6],nums2 = [36, 36, 36, 36, 36]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11550
    assert candidate(nums1 = [7, 11, 13, 17, 19, 23, 29, 31, 37],nums2 = [49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681]) == 0
    assert candidate(nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],nums2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) == 22
    assert candidate(nums1 = [2, 4, 8, 16, 32, 64],nums2 = [4, 16, 64, 256, 1024, 4096, 16384]) == 9
    assert candidate(nums1 = [10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [100, 225, 400, 625, 900, 1225, 1600, 2025, 2500]) == 0
    assert candidate(nums1 = [7, 24, 25, 30],nums2 = [49, 576, 625, 900, 1440, 1800]) == 0
    assert candidate(nums1 = [2, 3, 5, 7, 11, 13, 17],nums2 = [4, 9, 25, 49, 121, 169, 289]) == 0
    assert candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [49, 121, 169, 289, 361, 529]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 900
    assert candidate(nums1 = [1, 3, 3, 3, 1],nums2 = [1, 9, 9, 1, 1, 9]) == 36
    assert candidate(nums1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],nums2 = [10000, 40000, 90000, 160000, 250000, 360000, 490000, 640000, 810000, 1000000]) == 0
    assert candidate(nums1 = [5, 5, 5, 5, 5, 5, 5, 5, 5],nums2 = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == 0
    assert candidate(nums1 = [1, 2, 2, 3, 3, 3],nums2 = [1, 1, 2, 2, 3, 3]) == 14
    assert candidate(nums1 = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],nums2 = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 563
    assert candidate(nums1 = [1, 1, 2, 2, 3, 3],nums2 = [1, 1, 1, 4, 4, 9]) == 27
    assert candidate(nums1 = [3, 9, 27, 81, 243],nums2 = [27, 81, 243, 729, 2187]) == 6
    assert candidate(nums1 = [31, 37, 41, 43, 47, 53, 59],nums2 = [961, 1369, 1681, 1849, 2209, 2809, 3481]) == 0
    assert candidate(nums1 = [2, 4, 8, 16, 32, 64, 128, 256],nums2 = [4, 16, 64, 256, 1024, 4096]) == 17
    assert candidate(nums1 = [2, 2, 2, 2],nums2 = [4, 4, 4, 4, 4]) == 0
    assert candidate(nums1 = [2, 4, 8, 16, 32, 64],nums2 = [4, 16, 64, 256, 1024, 4096]) == 9
    assert candidate(nums1 = [6, 6, 6, 6, 6, 6],nums2 = [36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36]) == 0
    assert candidate(nums1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],nums2 = [25, 100, 225, 400, 625, 900, 1225, 1600, 2025, 2500]) == 1
    assert candidate(nums1 = [3, 5, 8, 12, 15, 17, 20],nums2 = [9, 25, 64, 144, 225, 289, 400]) == 1
    assert candidate(nums1 = [15, 20, 25, 30],nums2 = [225, 400, 625, 900, 1200, 1800]) == 0
    assert candidate(nums1 = [10, 10, 10],nums2 = [100, 100, 100, 100]) == 0
    assert candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [49, 121, 169, 289, 361]) == 0
    assert candidate(nums1 = [6, 7, 8],nums2 = [36, 49, 64, 84, 112]) == 0
    assert candidate(nums1 = [2, 3, 5, 7, 11],nums2 = [4, 6, 9, 10, 14, 15, 21, 22, 30, 33, 35, 55, 77, 105]) == 0
    assert candidate(nums1 = [10, 20, 30, 40, 50],nums2 = [100, 400, 900, 1600, 2500]) == 0
    assert candidate(nums1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],nums2 = [121, 484, 1089, 1936, 3025, 4356, 5929, 7744, 9801, 12100, 14641, 17424, 20736, 24336, 28081]) == 0
    assert candidate(nums1 = [10, 20, 30, 40],nums2 = [100, 400, 900, 1600, 2500]) == 0
    assert candidate(nums1 = [6, 8, 10, 12, 14],nums2 = [36, 64, 100, 144, 196, 256]) == 0
    assert candidate(nums1 = [15, 25, 35, 45, 55],nums2 = [225, 625, 1225, 2025, 3025, 450, 750, 1050, 1350, 1650]) == 0
    assert candidate(nums1 = [100000, 99999, 99998, 99997, 99996],nums2 = [10000000000, 9999800001, 9999600004, 9999400009, 9999200016]) == 0
    assert candidate(nums1 = [1, 1, 1, 1, 1, 1],nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 351
    assert candidate(nums1 = [6, 8, 10, 12, 14],nums2 = [36, 64, 100, 144, 196, 48, 72, 96, 112, 120]) == 0
    assert candidate(nums1 = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],nums2 = [64, 256, 576, 1024, 1600, 2304, 3136, 4096, 5184, 6400]) == 0
    assert candidate(nums1 = [6, 10, 14, 18, 22, 26, 30],nums2 = [36, 100, 196, 324, 484, 676, 900]) == 0
    assert candidate(nums1 = [3, 5, 7, 11, 13],nums2 = [9, 25, 49, 121, 169, 289]) == 0
    assert candidate(nums1 = [7, 11, 13, 17, 19, 23, 29],nums2 = [49, 121, 169, 289, 361, 529, 841]) == 0
    assert candidate(nums1 = [5, 12, 13, 15],nums2 = [25, 144, 169, 225, 441]) == 0
    assert candidate(nums1 = [11, 13, 17, 19],nums2 = [121, 169, 289, 361, 441, 529]) == 0
    assert candidate(nums1 = [1, 2, 2, 3, 3, 3, 4],nums2 = [1, 4, 4, 9, 9, 16]) == 12
    assert candidate(nums1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],nums2 = [4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576]) == 30
    assert candidate(nums1 = [7, 11, 13, 17, 19],nums2 = [49, 121, 169, 289, 361, 441]) == 0


