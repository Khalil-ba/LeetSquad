def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 2, 999, 3, 998]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 2, 999, 3, 998]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 1911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 1911: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500, 500]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500, 500]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1000]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1000]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 4, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 4, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 3, 8]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 3, 8]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 1, 1000]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 1, 1000]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 100, 101, 99]) == 9900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 100, 101, 99]) == 9900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 616
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 616: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 1, 1]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 1, 1]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 5, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 5, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 499, 499, 498, 498, 497, 497, 496, 496]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 499, 499, 498, 498, 497, 497, 496, 496]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]) == 14112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]) == 14112: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 898101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 898101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500, 499, 499, 499, 499, 498, 498]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500, 499, 499, 499, 499, 498, 498]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420]) == 157963
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420]) == 157963: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 250, 125, 625, 312, 156, 78, 39, 19, 9, 4, 2]) == 311376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 250, 125, 625, 312, 156, 78, 39, 19, 9, 4, 2]) == 311376: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 50, 40, 30, 20, 10]) == 199101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 50, 40, 30, 20, 10]) == 199101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1]) == 199101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1]) == 199101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [333, 666, 999, 334, 667, 998, 335, 668, 997]) == 995006
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [333, 666, 999, 334, 667, 998, 335, 668, 997]) == 995006: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 1000]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 1000]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309]) == 94556
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309]) == 94556: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 999, 999, 998, 998, 997, 997]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 999, 999, 998, 998, 997, 997]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 300, 300, 300, 300, 300, 299, 299, 299, 299]) == 89401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 300, 300, 300, 300, 300, 299, 299, 299, 299]) == 89401: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 754
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 754: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 450, 450, 400, 400, 350, 350, 300, 300]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 450, 450, 400, 400, 350, 350, 300, 300]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265]) == 69432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265]) == 69432: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 999, 999, 998, 998, 997, 997, 996, 996]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 999, 999, 998, 998, 997, 997, 996, 996]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1000, 1000, 1000, 1000, 1000]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1000, 1000, 1000, 1000, 1000]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1932
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1932: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50]) == 224051
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50]) == 224051: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491]) == 248502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491]) == 248502: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 17982
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 17982: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 4620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 4620: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 300, 300, 300, 300, 300, 300, 300, 300, 1]) == 89401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 300, 300, 300, 300, 300, 300, 300, 300, 1]) == 89401: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 9702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 9702: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78]) == 6776
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78]) == 6776: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 99]) == 9702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 99]) == 9702: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 1000]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 1000]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 8811
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 8811: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 995006
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 995006: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == 498501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == 498501: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 1, 2, 3, 4, 5]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 1, 2, 3, 4, 5]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 288: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1, 999, 2, 999, 3, 999, 4, 999, 5]) == 996004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1, 999, 2, 999, 3, 999, 4, 999, 5]) == 996004: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 182: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 616
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 616: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 37611
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 37611: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509]) == 257556
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509]) == 257556: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 323: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 12971
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 12971: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 501, 499, 502, 498, 503, 497, 504, 496, 505]) == 253512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 501, 499, 502, 498, 503, 497, 504, 496, 505]) == 253512: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 11556
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 11556: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 342: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100]) == 4851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100]) == 4851: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 1, 2, 3]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 1, 2, 3]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 995006
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 995006: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 100, 10, 1]) == 98901
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 100, 10, 1]) == 98901: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 1368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 1368: {e}')
    
    total += 1
    try:
        result = candidate(nums = [333, 666, 999, 222, 555, 888, 111, 444, 777, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 885226
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [333, 666, 999, 222, 555, 888, 111, 444, 777, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 885226: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4]) == 199101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4]) == 199101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 1000, 1000, 1000, 1000, 1000]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 1000, 1000, 1000, 1000, 1000]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1000, 4, 5, 6, 7, 8, 9]) == 7992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1000, 4, 5, 6, 7, 8, 9]) == 7992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 8811
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 8811: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 998, 998, 997, 997, 996, 996, 995, 995]) == 996004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 998, 998, 997, 997, 996, 996, 995, 995]) == 996004: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 1000]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 1000]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1000, 1, 2, 3, 4, 5, 6, 7, 8]) == 997002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1000, 1, 2, 3, 4, 5, 6, 7, 8]) == 997002: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1000]) == 8991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1000]) == 8991: {e}')
    
    total += 1
    try:
        result = candidate(nums = [250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269]) == 71556
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269]) == 71556: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1000, 1001, 1002, 1003, 1004]) == 1005006
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1000, 1001, 1002, 1003, 1004]) == 1005006: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 20711
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 20711: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 7992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 7992: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1000, 998, 1000, 997]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1000, 998, 1000, 997]) == 998001: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 10, 10, 10]) == 81
    assert candidate(nums = [2, 3, 5, 7, 11, 13]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
    assert candidate(nums = [1, 1000, 2, 999, 3, 998]) == 997002
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
    assert candidate(nums = [10, 20, 30, 40, 50]) == 1911
    assert candidate(nums = [5, 6, 7, 8, 9]) == 56
    assert candidate(nums = [5, 5, 5, 5]) == 16
    assert candidate(nums = [1, 2, 3, 4, 5]) == 12
    assert candidate(nums = [500, 500, 500, 500, 500]) == 249001
    assert candidate(nums = [999, 1000]) == 997002
    assert candidate(nums = [1, 5, 4, 5]) == 16
    assert candidate(nums = [10, 2, 3, 8]) == 63
    assert candidate(nums = [1, 1000, 1, 1000]) == 998001
    assert candidate(nums = [2, 3, 100, 101, 99]) == 9900
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 616
    assert candidate(nums = [100, 100]) == 9801
    assert candidate(nums = [500, 500, 1, 1]) == 249001
    assert candidate(nums = [3, 7]) == 12
    assert candidate(nums = [3, 4, 5, 2]) == 12
    assert candidate(nums = [500, 500, 499, 499, 498, 498, 497, 497, 496, 496]) == 249001
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]) == 14112
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 898101
    assert candidate(nums = [500, 500, 500, 500, 499, 499, 499, 499, 498, 498]) == 249001
    assert candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420]) == 157963
    assert candidate(nums = [500, 250, 125, 625, 312, 156, 78, 39, 19, 9, 4, 2]) == 311376
    assert candidate(nums = [500, 400, 300, 200, 100, 50, 40, 30, 20, 10]) == 199101
    assert candidate(nums = [100, 200, 300, 400, 500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1]) == 199101
    assert candidate(nums = [333, 666, 999, 334, 667, 998, 335, 668, 997]) == 995006
    assert candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8]) == 997002
    assert candidate(nums = [1000, 999, 998, 997, 996]) == 997002
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 1000]) == 997002
    assert candidate(nums = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309]) == 94556
    assert candidate(nums = [1000, 1000, 999, 999, 998, 998, 997, 997]) == 998001
    assert candidate(nums = [300, 300, 300, 300, 300, 300, 299, 299, 299, 299]) == 89401
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 754
    assert candidate(nums = [500, 500, 450, 450, 400, 400, 350, 350, 300, 300]) == 249001
    assert candidate(nums = [250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265]) == 69432
    assert candidate(nums = [1000, 1000, 999, 999, 998, 998, 997, 997, 996, 996]) == 998001
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1000, 1000, 1000, 1000, 1000]) == 998001
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 1932
    assert candidate(nums = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50]) == 224051
    assert candidate(nums = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491]) == 248502
    assert candidate(nums = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 17982
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 4620
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == 6
    assert candidate(nums = [300, 300, 300, 300, 300, 300, 300, 300, 300, 1]) == 89401
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 9702
    assert candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78]) == 6776
    assert candidate(nums = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 99]) == 9702
    assert candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 249001
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 997002
    assert candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 1000]) == 997002
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 8811
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 995006
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 0
    assert candidate(nums = [1, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == 498501
    assert candidate(nums = [500, 500, 500, 1, 2, 3, 4, 5]) == 249001
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 288
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0
    assert candidate(nums = [999, 1, 999, 2, 999, 3, 999, 4, 999, 5]) == 996004
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 182
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 616
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 37611
    assert candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509]) == 257556
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 323
    assert candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == 997002
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 12971
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 997002
    assert candidate(nums = [500, 501, 499, 502, 498, 503, 497, 504, 496, 505]) == 253512
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 11556
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 342
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100]) == 4851
    assert candidate(nums = [1000, 999, 998, 1, 2, 3]) == 997002
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 995006
    assert candidate(nums = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 998001
    assert candidate(nums = [1, 10, 100, 1000, 100, 10, 1]) == 98901
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 1368
    assert candidate(nums = [333, 666, 999, 222, 555, 888, 111, 444, 777, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 885226
    assert candidate(nums = [500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4]) == 199101
    assert candidate(nums = [3, 3, 3, 3, 3, 1000, 1000, 1000, 1000, 1000]) == 998001
    assert candidate(nums = [1, 2, 3, 1000, 4, 5, 6, 7, 8, 9]) == 7992
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 8811
    assert candidate(nums = [999, 999, 998, 998, 997, 997, 996, 996, 995, 995]) == 996004
    assert candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 1000]) == 997002
    assert candidate(nums = [999, 1000, 1, 2, 3, 4, 5, 6, 7, 8]) == 997002
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 81
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1000]) == 8991
    assert candidate(nums = [250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269]) == 71556
    assert candidate(nums = [1, 2, 3, 4, 5, 1000, 1001, 1002, 1003, 1004]) == 1005006
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 20711
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 25
    assert candidate(nums = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 7992
    assert candidate(nums = [999, 1000, 998, 1000, 997]) == 998001


