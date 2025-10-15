def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 18, 24, 30]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 18, 24, 30]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 16, 20, 24, 28]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 16, 20, 24, 28]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 60, 90, 120, 150, 180]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 60, 90, 120, 150, 180]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 7, 11, 13, 17]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 7, 11, 13, 17]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 12, 15]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 12, 15]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 12, 18, 24, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 12, 18, 24, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [36, 72, 108, 144, 180]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [36, 72, 108, 144, 180]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 7, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 7, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 7, 11, 13, 17, 19]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 7, 11, 13, 17, 19]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3000, 3003, 3006, 3009, 3012, 3015, 3018, 3021, 3024, 3027]) == 3012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3000, 3003, 3006, 3009, 3012, 3015, 3018, 3021, 3024, 3027]) == 3012: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970, 969, 968, 967, 966, 965, 964, 963, 962, 961, 960, 959, 958, 957, 956, 955, 954, 953, 952, 951, 950, 949, 948, 947, 946, 945, 944, 943, 942, 941, 940, 939, 938, 937, 936, 935, 934, 933, 932, 931, 930]) == 963
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970, 969, 968, 967, 966, 965, 964, 963, 962, 961, 960, 959, 958, 957, 956, 955, 954, 953, 952, 951, 950, 949, 948, 947, 946, 945, 944, 943, 942, 941, 940, 939, 938, 937, 936, 935, 934, 933, 932, 931, 930]) == 963: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360, 366, 372, 378, 384, 390]) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360, 366, 372, 378, 384, 390]) == 345: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 102, 104, 105, 106, 108, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 102, 104, 105, 106, 108, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]) == 114: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 396, 432, 468, 504]) == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 396, 432, 468, 504]) == 252: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [150, 162, 174, 186, 198, 210, 222, 234, 246, 258, 270, 282, 294, 306, 318, 330, 342, 354, 366, 378]) == 264
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [150, 162, 174, 186, 198, 210, 222, 234, 246, 258, 270, 282, 294, 306, 318, 330, 342, 354, 366, 378]) == 264: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252]) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252]) == 138: {e}')
    
    total += 1
    try:
        result = candidate(nums = [150, 210, 270, 330, 390, 450, 510, 570, 630, 690, 750, 810, 870, 930, 990]) == 570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [150, 210, 270, 330, 390, 450, 510, 570, 630, 690, 750, 810, 870, 930, 990]) == 570: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 14, 18, 20, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 14, 18, 20, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 6, 9, 10, 12, 15, 18, 21, 24, 27, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 6, 9, 10, 12, 15, 18, 21, 24, 27, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960]) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960]) == 510: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 525: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 102, 104, 105, 108, 110, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180]) == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 102, 104, 105, 108, 110, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180]) == 141: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240]) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240]) == 171: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 303, 306, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 354, 357]) == 327
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 303, 306, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 354, 357]) == 327: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020]) == 1011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020]) == 1011: {e}')
    
    total += 1
    try:
        result = candidate(nums = [102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147, 153, 159, 165, 171, 177, 183, 189, 195, 201, 207, 213, 219, 225, 231, 237, 243, 249, 255, 261, 267, 273, 279, 285, 291, 297, 303, 309, 315, 321, 327, 333, 339, 345, 351, 357, 363, 369, 375, 381, 387, 393, 399]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147, 153, 159, 165, 171, 177, 183, 189, 195, 201, 207, 213, 219, 225, 231, 237, 243, 249, 255, 261, 267, 273, 279, 285, 291, 297, 303, 309, 315, 321, 327, 333, 339, 345, 351, 357, 363, 369, 375, 381, 387, 393, 399]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [102, 204, 306, 408, 510, 612, 714, 816, 918, 1020, 1122, 1224, 1326, 1428, 1530, 1632, 1734, 1836, 1938, 2040]) == 1071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [102, 204, 306, 408, 510, 612, 714, 816, 918, 1020, 1122, 1224, 1326, 1428, 1530, 1632, 1734, 1836, 1938, 2040]) == 1071: {e}')
    
    total += 1
    try:
        result = candidate(nums = [600, 600, 600, 600, 600, 600, 600, 600, 600, 600]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [600, 600, 600, 600, 600, 600, 600, 600, 600, 600]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270, 288, 306, 324, 342, 360]) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270, 288, 306, 324, 342, 360]) == 189: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 303, 306, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 354, 357, 360, 363, 366, 369, 372]) == 336
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 303, 306, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 354, 357, 360, 363, 366, 369, 372]) == 336: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270, 288, 306, 324, 342, 360, 378, 396, 414, 432, 450, 468, 486, 504, 522, 540, 558, 576, 594, 612, 630, 648, 666, 684, 702, 720, 738, 756, 774, 792, 810, 828, 846, 864, 882, 900, 918, 936, 954, 972, 990, 1008]) == 513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270, 288, 306, 324, 342, 360, 378, 396, 414, 432, 450, 468, 486, 504, 522, 540, 558, 576, 594, 612, 630, 648, 666, 684, 702, 720, 738, 756, 774, 792, 810, 828, 846, 864, 882, 900, 918, 936, 954, 972, 990, 1008]) == 513: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210]) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210]) == 117: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970]) == 984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970]) == 984: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [600, 602, 604, 606, 608, 610, 612, 614, 616, 618, 620, 622, 624, 626, 628, 630, 632, 634, 636, 638]) == 618
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [600, 602, 604, 606, 608, 610, 612, 614, 616, 618, 620, 622, 624, 626, 628, 630, 632, 634, 636, 638]) == 618: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180]) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180]) == 153: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240]) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240]) == 132: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180]) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180]) == 93: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 600, 900, 1200, 1500]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 600, 900, 1200, 1500]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 90, 135, 180, 225, 270, 315, 360, 405, 450, 495, 540, 585, 630, 675, 720, 765, 810, 855, 900]) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 90, 135, 180, 225, 270, 315, 360, 405, 450, 495, 540, 585, 630, 675, 720, 765, 810, 855, 900]) == 495: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338]) == 318
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338]) == 318: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126, 138, 150, 162, 174, 186, 198, 210, 222, 234, 246, 258, 270]) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126, 138, 150, 162, 174, 186, 198, 210, 222, 234, 246, 258, 270]) == 138: {e}')
    
    total += 1
    try:
        result = candidate(nums = [600, 1200, 1800, 2400, 3000, 3600, 4200, 4800, 5400, 6000, 6600, 7200, 7800, 8400, 9000, 9600, 10000]) == 5100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [600, 1200, 1800, 2400, 3000, 3600, 4200, 4800, 5400, 6000, 6600, 7200, 7800, 8400, 9000, 9600, 10000]) == 5100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330, 363, 396, 429, 462, 495, 528, 561, 594, 627, 660]) == 363
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330, 363, 396, 429, 462, 495, 528, 561, 594, 627, 660]) == 363: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200, 4500]) == 2400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200, 4500]) == 2400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195, 198, 201, 204, 207, 210]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195, 198, 201, 204, 207, 210]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 100]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 100]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [27, 54, 81, 108, 135, 162, 189, 216, 243, 270, 297, 324, 351, 378, 405, 432, 459, 486, 513, 540]) == 297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [27, 54, 81, 108, 135, 162, 189, 216, 243, 270, 297, 324, 351, 378, 405, 432, 459, 486, 513, 540]) == 297: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 1023, 1356, 1689, 2013, 2346, 2679, 3003]) == 1386
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 1023, 1356, 1689, 2013, 2346, 2679, 3003]) == 1386: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [102, 204, 306, 408, 510, 612, 714, 816, 918, 1020]) == 561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [102, 204, 306, 408, 510, 612, 714, 816, 918, 1020]) == 561: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [996, 998, 1000, 999, 993, 990, 987, 984, 981, 978, 975, 972, 969, 966, 963, 960, 957, 954, 951, 948]) == 972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [996, 998, 1000, 999, 993, 990, 987, 984, 981, 978, 975, 972, 969, 966, 963, 960, 957, 954, 951, 948]) == 972: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]) == 315: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 276, 288, 300, 312, 324, 336, 348, 360, 372, 384, 396, 408, 420, 432, 444, 456, 468, 480, 492, 504, 516, 528, 540, 552, 564, 576, 588, 600, 612, 624, 636, 648, 660, 672, 684, 696, 708, 720, 732, 744, 756, 768, 780, 792, 804, 816, 828, 840, 852, 864, 876, 888, 900, 912, 924, 936, 948, 960, 972, 984, 996]) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 276, 288, 300, 312, 324, 336, 348, 360, 372, 384, 396, 408, 420, 432, 444, 456, 468, 480, 492, 504, 516, 528, 540, 552, 564, 576, 588, 600, 612, 624, 636, 648, 660, 672, 684, 696, 708, 720, 732, 744, 756, 768, 780, 792, 804, 816, 828, 840, 852, 864, 876, 888, 900, 912, 924, 936, 948, 960, 972, 984, 996]) == 504: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 102, 104, 105, 108, 110, 112, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 102, 104, 105, 108, 110, 112, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126, 138, 150, 162, 174, 186, 198, 210, 222, 234, 246, 258, 270, 282, 294, 300, 306, 312, 318, 324, 330]) == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126, 138, 150, 162, 174, 186, 198, 210, 222, 234, 246, 258, 270, 282, 294, 300, 306, 312, 318, 324, 330]) == 181: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238]) == 219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238]) == 219: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 996, 993, 990, 987, 984, 981, 978, 975, 972, 969, 966, 963, 960, 957, 954, 951, 948, 945, 942, 939, 936, 933, 930, 927, 924, 921, 918, 915, 912, 909, 906, 903, 900, 897, 894, 891, 888, 885, 882, 879, 876, 873, 870, 867, 864, 861, 858, 855, 852, 849, 846, 843, 840, 837, 834, 831, 828, 825, 822, 819, 816, 813, 810, 807, 804, 801, 798, 795, 792, 789, 786, 783, 780, 777, 774, 771, 768, 765, 762, 759, 756, 753, 750, 747, 744, 741, 738, 735, 732, 729, 726, 723, 720, 717, 714, 711, 708, 705, 702, 699, 696, 693, 690, 687, 684, 681, 678, 675, 672, 669, 666, 663, 660, 657, 654, 651, 648, 645, 642, 639, 636, 633, 630, 627, 624, 621, 618, 615, 612, 609, 606, 603, 600]) == 798
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 996, 993, 990, 987, 984, 981, 978, 975, 972, 969, 966, 963, 960, 957, 954, 951, 948, 945, 942, 939, 936, 933, 930, 927, 924, 921, 918, 915, 912, 909, 906, 903, 900, 897, 894, 891, 888, 885, 882, 879, 876, 873, 870, 867, 864, 861, 858, 855, 852, 849, 846, 843, 840, 837, 834, 831, 828, 825, 822, 819, 816, 813, 810, 807, 804, 801, 798, 795, 792, 789, 786, 783, 780, 777, 774, 771, 768, 765, 762, 759, 756, 753, 750, 747, 744, 741, 738, 735, 732, 729, 726, 723, 720, 717, 714, 711, 708, 705, 702, 699, 696, 693, 690, 687, 684, 681, 678, 675, 672, 669, 666, 663, 660, 657, 654, 651, 648, 645, 642, 639, 636, 633, 630, 627, 624, 621, 618, 615, 612, 609, 606, 603, 600]) == 798: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]) == 1008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]) == 1008: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 996, 994, 992, 990, 988, 986, 984, 982, 980, 978, 976, 974, 972, 970, 968, 966, 964, 962, 960, 958, 956, 954, 952, 950, 948, 946, 944, 942, 940, 938, 936, 934, 932, 930, 928, 926, 924, 922, 920, 918, 916, 914, 912, 910, 908, 906, 904, 902, 900, 898, 896, 894, 892, 890, 888, 886, 884, 882, 880, 878, 876, 874, 872, 870, 868, 866, 864, 862, 860]) == 930
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 996, 994, 992, 990, 988, 986, 984, 982, 980, 978, 976, 974, 972, 970, 968, 966, 964, 962, 960, 958, 956, 954, 952, 950, 948, 946, 944, 942, 940, 938, 936, 934, 932, 930, 928, 926, 924, 922, 920, 918, 916, 914, 912, 910, 908, 906, 904, 902, 900, 898, 896, 894, 892, 890, 888, 886, 884, 882, 880, 878, 876, 874, 872, 870, 868, 866, 864, 862, 860]) == 930: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]) == 1005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]) == 1005: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 18
    assert candidate(nums = [3, 9, 15, 21, 27, 33]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12]) == 9
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80]) == 42
    assert candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]) == 165
    assert candidate(nums = [2, 6, 18, 24, 30]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(nums = [4, 8, 16, 20, 24, 28]) == 24
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 18
    assert candidate(nums = [30, 60, 90, 120, 150, 180]) == 105
    assert candidate(nums = [1, 5, 7, 11, 13, 17]) == 0
    assert candidate(nums = [1, 3, 6, 10, 12, 15]) == 9
    assert candidate(nums = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 54
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 12
    assert candidate(nums = [3, 9, 15, 21, 27]) == 0
    assert candidate(nums = [2, 6, 12, 18, 24, 30]) == 18
    assert candidate(nums = [36, 72, 108, 144, 180]) == 108
    assert candidate(nums = [2, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114]) == 60
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 990
    assert candidate(nums = [1, 2, 4, 7, 10]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 0
    assert candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330]) == 198
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 33
    assert candidate(nums = [1, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 0
    assert candidate(nums = [1, 5, 7, 11, 13, 17, 19]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 12
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]) == 24
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]) == 0
    assert candidate(nums = [3000, 3003, 3006, 3009, 3012, 3015, 3018, 3021, 3024, 3027]) == 3012
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970, 969, 968, 967, 966, 965, 964, 963, 962, 961, 960, 959, 958, 957, 956, 955, 954, 953, 952, 951, 950, 949, 948, 947, 946, 945, 944, 943, 942, 941, 940, 939, 938, 937, 936, 935, 934, 933, 932, 931, 930]) == 963
    assert candidate(nums = [300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360, 366, 372, 378, 384, 390]) == 345
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 600
    assert candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114]) == 60
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]) == 300
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 51
    assert candidate(nums = [100, 102, 104, 105, 106, 108, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]) == 114
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 18
    assert candidate(nums = [6, 36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 396, 432, 468, 504]) == 252
    assert candidate(nums = [2, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 33
    assert candidate(nums = [150, 162, 174, 186, 198, 210, 222, 234, 246, 258, 270, 282, 294, 306, 318, 330, 342, 354, 366, 378]) == 264
    assert candidate(nums = [18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150]) == 84
    assert candidate(nums = [24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252]) == 138
    assert candidate(nums = [150, 210, 270, 330, 390, 450, 510, 570, 630, 690, 750, 810, 870, 930, 990]) == 570
    assert candidate(nums = [8, 14, 18, 20, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 54
    assert candidate(nums = [2, 3, 5, 6, 9, 10, 12, 15, 18, 21, 24, 27, 30]) == 18
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120]) == 63
    assert candidate(nums = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960]) == 510
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 18
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]) == 525
    assert candidate(nums = [100, 102, 104, 105, 108, 110, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180]) == 141
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 0
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 33
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 18
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 27
    assert candidate(nums = [102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240]) == 171
    assert candidate(nums = [300, 303, 306, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 354, 357]) == 327
    assert candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020]) == 1011
    assert candidate(nums = [102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198]) == 150
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147, 153, 159, 165, 171, 177, 183, 189, 195, 201, 207, 213, 219, 225, 231, 237, 243, 249, 255, 261, 267, 273, 279, 285, 291, 297, 303, 309, 315, 321, 327, 333, 339, 345, 351, 357, 363, 369, 375, 381, 387, 393, 399]) == 0
    assert candidate(nums = [102, 204, 306, 408, 510, 612, 714, 816, 918, 1020, 1122, 1224, 1326, 1428, 1530, 1632, 1734, 1836, 1938, 2040]) == 1071
    assert candidate(nums = [600, 600, 600, 600, 600, 600, 600, 600, 600, 600]) == 600
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]) == 48
    assert candidate(nums = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270, 288, 306, 324, 342, 360]) == 189
    assert candidate(nums = [300, 303, 306, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 354, 357, 360, 363, 366, 369, 372]) == 336
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150]) == 78
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 990
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]) == 0
    assert candidate(nums = [18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198, 216, 234, 252, 270, 288, 306, 324, 342, 360, 378, 396, 414, 432, 450, 468, 486, 504, 522, 540, 558, 576, 594, 612, 630, 648, 666, 684, 702, 720, 738, 756, 774, 792, 810, 828, 846, 864, 882, 900, 918, 936, 954, 972, 990, 1008]) == 513
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == 51
    assert candidate(nums = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360]) == 198
    assert candidate(nums = [101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159]) == 0
    assert candidate(nums = [24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210]) == 117
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 21
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 21
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975, 974, 973, 972, 971, 970]) == 984
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 33
    assert candidate(nums = [600, 602, 604, 606, 608, 610, 612, 614, 616, 618, 620, 622, 624, 626, 628, 630, 632, 634, 636, 638]) == 618
    assert candidate(nums = [123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180]) == 153
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 990
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 33
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 18
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240]) == 132
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150]) == 78
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180]) == 93
    assert candidate(nums = [300, 600, 900, 1200, 1500]) == 900
    assert candidate(nums = [36, 72, 108, 144, 180, 216, 252, 288, 324, 360]) == 198
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]) == 51
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == 51
    assert candidate(nums = [45, 90, 135, 180, 225, 270, 315, 360, 405, 450, 495, 540, 585, 630, 675, 720, 765, 810, 855, 900]) == 495
    assert candidate(nums = [300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338]) == 318
    assert candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126, 138, 150, 162, 174, 186, 198, 210, 222, 234, 246, 258, 270]) == 138
    assert candidate(nums = [600, 1200, 1800, 2400, 3000, 3600, 4200, 4800, 5400, 6000, 6600, 7200, 7800, 8400, 9000, 9600, 10000]) == 5100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 12
    assert candidate(nums = [33, 66, 99, 132, 165, 198, 231, 264, 297, 330, 363, 396, 429, 462, 495, 528, 561, 594, 627, 660]) == 363
    assert candidate(nums = [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200, 4500]) == 2400
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195, 198, 201, 204, 207, 210]) == 108
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == 27
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 51
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120]) == 63
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 48
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 100]) == 48
    assert candidate(nums = [27, 54, 81, 108, 135, 162, 189, 216, 243, 270, 297, 324, 351, 378, 405, 432, 459, 486, 513, 540]) == 297
    assert candidate(nums = [3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 0
    assert candidate(nums = [123, 456, 789, 1023, 1356, 1689, 2013, 2346, 2679, 3003]) == 1386
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 60
    assert candidate(nums = [102, 204, 306, 408, 510, 612, 714, 816, 918, 1020]) == 561
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 0
    assert candidate(nums = [996, 998, 1000, 999, 993, 990, 987, 984, 981, 978, 975, 972, 969, 966, 963, 960, 957, 954, 951, 948]) == 972
    assert candidate(nums = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]) == 315
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 0
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147]) == 0
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 276, 288, 300, 312, 324, 336, 348, 360, 372, 384, 396, 408, 420, 432, 444, 456, 468, 480, 492, 504, 516, 528, 540, 552, 564, 576, 588, 600, 612, 624, 636, 648, 660, 672, 684, 696, 708, 720, 732, 744, 756, 768, 780, 792, 804, 816, 828, 840, 852, 864, 876, 888, 900, 912, 924, 936, 948, 960, 972, 984, 996]) == 504
    assert candidate(nums = [100, 102, 104, 105, 108, 110, 112, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150]) == 126
    assert candidate(nums = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126, 138, 150, 162, 174, 186, 198, 210, 222, 234, 246, 258, 270, 282, 294, 300, 306, 312, 318, 324, 330]) == 181
    assert candidate(nums = [200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238]) == 219
    assert candidate(nums = [999, 996, 993, 990, 987, 984, 981, 978, 975, 972, 969, 966, 963, 960, 957, 954, 951, 948, 945, 942, 939, 936, 933, 930, 927, 924, 921, 918, 915, 912, 909, 906, 903, 900, 897, 894, 891, 888, 885, 882, 879, 876, 873, 870, 867, 864, 861, 858, 855, 852, 849, 846, 843, 840, 837, 834, 831, 828, 825, 822, 819, 816, 813, 810, 807, 804, 801, 798, 795, 792, 789, 786, 783, 780, 777, 774, 771, 768, 765, 762, 759, 756, 753, 750, 747, 744, 741, 738, 735, 732, 729, 726, 723, 720, 717, 714, 711, 708, 705, 702, 699, 696, 693, 690, 687, 684, 681, 678, 675, 672, 669, 666, 663, 660, 657, 654, 651, 648, 645, 642, 639, 636, 633, 630, 627, 624, 621, 618, 615, 612, 609, 606, 603, 600]) == 798
    assert candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015]) == 1008
    assert candidate(nums = [999, 998, 996, 994, 992, 990, 988, 986, 984, 982, 980, 978, 976, 974, 972, 970, 968, 966, 964, 962, 960, 958, 956, 954, 952, 950, 948, 946, 944, 942, 940, 938, 936, 934, 932, 930, 928, 926, 924, 922, 920, 918, 916, 914, 912, 910, 908, 906, 904, 902, 900, 898, 896, 894, 892, 890, 888, 886, 884, 882, 880, 878, 876, 874, 872, 870, 868, 866, 864, 862, 860]) == 930
    assert candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]) == 1005


