def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [10, 11, 12, 13, 14, 15]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 11, 12, 13, 14, 15]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 4, 5, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 4, 5, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [500, 501, 502, 503, 504]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [500, 501, 502, 503, 504]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 999, 998, 997, 996]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 999, 998, 997, 996]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 11, 12, 13, 14]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 11, 12, 13, 14]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [500, 501, 502, 503, 504, 505]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [500, 501, 502, 503, 504, 505]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 3, 3, 5, 5, 7, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 3, 3, 5, 5, 7, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 3, 5, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 3, 5, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 1000, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 1000, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [500, 500, 501, 502, 503, 503, 503, 504, 505, 505, 506, 507, 508]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [500, 500, 501, 502, 503, 503, 503, 504, 505, 505, 506, 507, 508]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 1000, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 1000, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 13, 14, 15]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 13, 14, 15]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 9]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 9]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 101, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 101, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 1000, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 1000, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(arr = [400, 401, 401, 402, 402, 403, 403, 404, 404, 405, 405, 406, 406, 407, 407, 408, 408, 409, 409]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [400, 401, 401, 402, 402, 403, 403, 404, 404, 405, 405, 406, 406, 407, 407, 408, 408, 409, 409]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [500, 501, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [500, 501, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [333, 334, 334, 335, 336, 337, 337, 338, 339, 340, 341, 342, 343, 344, 345]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [333, 334, 334, 335, 336, 337, 337, 338, 339, 340, 341, 342, 343, 344, 345]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 10]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 10]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 11, 12, 12, 12, 12, 12, 13, 14, 15, 15, 15, 15, 15, 16, 17, 18, 19, 20, 21, 21, 21, 21, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 11, 12, 12, 12, 12, 12, 13, 14, 15, 15, 15, 15, 15, 16, 17, 18, 19, 20, 21, 21, 21, 21, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 100, 101, 101, 102, 102, 103, 103, 104, 104, 105, 105, 106, 106, 107, 107, 108, 108, 109, 109, 110, 110]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 100, 101, 101, 102, 102, 103, 103, 104, 104, 105, 105, 106, 106, 107, 107, 108, 108, 109, 109, 110, 110]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [300, 301, 301, 302, 302, 302, 303, 303, 303, 303]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [300, 301, 301, 302, 302, 302, 303, 303, 303, 303]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 200, 201, 202, 203, 204, 205]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 200, 201, 202, 203, 204, 205]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [450, 451, 451, 451, 452, 452, 452, 452, 452, 453, 454, 455]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [450, 451, 451, 451, 452, 452, 452, 452, 452, 453, 454, 455]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [200, 201, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [200, 201, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 10]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 10]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 30, 30, 30]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 30, 30, 30]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(arr = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [998, 999, 1000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [998, 999, 1000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1001, 1002, 1003, 1004, 1005]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1001, 1002, 1003, 1004, 1005]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 6, 7, 8, 8, 8, 9, 9, 10, 11, 11, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 6, 7, 8, 8, 8, 9, 9, 10, 11, 11, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [500, 501, 502, 502, 503, 504, 504, 505, 506, 506, 507, 508, 508, 509, 509, 510, 511, 511, 512, 512]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [500, 501, 502, 502, 503, 504, 504, 505, 506, 506, 507, 508, 508, 509, 509, 510, 511, 511, 512, 512]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 14: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [10, 11, 12, 13, 14, 15]) == 5
    assert candidate(arr = [5, 4, 3, 2, 1]) == 4
    assert candidate(arr = [1, 2, 3]) == 2
    assert candidate(arr = [1, 2]) == 1
    assert candidate(arr = [0]) == 0
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(arr = [1, 2, 2, 3, 4, 5, 6]) == 6
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 4]) == 6
    assert candidate(arr = [500, 501, 502, 503, 504]) == 4
    assert candidate(arr = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 8
    assert candidate(arr = [5, 6, 7, 8, 9, 10]) == 5
    assert candidate(arr = [1]) == 0
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]) == 8
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(arr = [1000, 999, 998, 997, 996]) == 4
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == 7
    assert candidate(arr = [10, 11, 12, 13, 14]) == 4
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(arr = [500, 501, 502, 503, 504, 505]) == 5
    assert candidate(arr = [0, 0, 0, 0, 0]) == 0
    assert candidate(arr = [0, 0, 0, 0]) == 0
    assert candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5]) == 7
    assert candidate(arr = [1, 1, 3, 3, 5, 5, 7, 7]) == 0
    assert candidate(arr = [0, 1, 2, 3, 4, 5]) == 5
    assert candidate(arr = [1000]) == 0
    assert candidate(arr = [0, 1000]) == 0
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4]) == 6
    assert candidate(arr = [1, 3, 2, 3, 5, 0]) == 3
    assert candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10
    assert candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 20
    assert candidate(arr = [999, 1000, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 12
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106]) == 0
    assert candidate(arr = [750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780]) == 30
    assert candidate(arr = [500, 500, 501, 502, 503, 503, 503, 504, 505, 505, 506, 507, 508]) == 12
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 0
    assert candidate(arr = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325]) == 25
    assert candidate(arr = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]) == 32
    assert candidate(arr = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]) == 10
    assert candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 10
    assert candidate(arr = [999, 1000, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 24
    assert candidate(arr = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]) == 11
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
    assert candidate(arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 12
    assert candidate(arr = [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]) == 20
    assert candidate(arr = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 14
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 0
    assert candidate(arr = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == 19
    assert candidate(arr = [299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313]) == 14
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 0
    assert candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 15
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 13, 14, 15]) == 12
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 29
    assert candidate(arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 9]) == 19
    assert candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530]) == 30
    assert candidate(arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 23
    assert candidate(arr = [100, 101, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]) == 16
    assert candidate(arr = [999, 1000, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 19
    assert candidate(arr = [0, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12
    assert candidate(arr = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 17
    assert candidate(arr = [400, 401, 401, 402, 402, 403, 403, 404, 404, 405, 405, 406, 406, 407, 407, 408, 408, 409, 409]) == 17
    assert candidate(arr = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 14
    assert candidate(arr = [500, 501, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510]) == 11
    assert candidate(arr = [333, 334, 334, 335, 336, 337, 337, 338, 339, 340, 341, 342, 343, 344, 345]) == 14
    assert candidate(arr = [5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]) == 19
    assert candidate(arr = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315]) == 15
    assert candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515]) == 15
    assert candidate(arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 0
    assert candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519]) == 19
    assert candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30]) == 57
    assert candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 10
    assert candidate(arr = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315]) == 15
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 14
    assert candidate(arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 10]) == 16
    assert candidate(arr = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 10
    assert candidate(arr = [998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006]) == 8
    assert candidate(arr = [10, 10, 10, 10, 10, 11, 12, 12, 12, 12, 12, 13, 14, 15, 15, 15, 15, 15, 16, 17, 18, 19, 20, 21, 21, 21, 21, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 36
    assert candidate(arr = [100, 100, 101, 101, 102, 102, 103, 103, 104, 104, 105, 105, 106, 106, 107, 107, 108, 108, 109, 109, 110, 110]) == 20
    assert candidate(arr = [300, 301, 301, 302, 302, 302, 303, 303, 303, 303]) == 6
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0
    assert candidate(arr = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105]) == 0
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == 20
    assert candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 200, 201, 202, 203, 204, 205]) == 14
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == 15
    assert candidate(arr = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12]) == 21
    assert candidate(arr = [450, 451, 451, 451, 452, 452, 452, 452, 452, 453, 454, 455]) == 11
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 0
    assert candidate(arr = [200, 201, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219]) == 20
    assert candidate(arr = [0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 12
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 28
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == 10
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == 22
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8]) == 28
    assert candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]) == 19
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
    assert candidate(arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9, 10]) == 21
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(arr = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100, 100]) == 0
    assert candidate(arr = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 14
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 15
    assert candidate(arr = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 30, 30, 30]) == 40
    assert candidate(arr = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213]) == 13
    assert candidate(arr = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509]) == 9
    assert candidate(arr = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430]) == 30
    assert candidate(arr = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 50
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 10
    assert candidate(arr = [998, 999, 1000]) == 2
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1001, 1002, 1003, 1004, 1005]) == 5
    assert candidate(arr = [3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 23
    assert candidate(arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 19
    assert candidate(arr = [200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185]) == 15
    assert candidate(arr = [5, 6, 6, 7, 8, 8, 8, 9, 9, 10, 11, 11, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20]) == 21
    assert candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]) == 19
    assert candidate(arr = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 24
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]) == 21
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0
    assert candidate(arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 15
    assert candidate(arr = [500, 501, 502, 502, 503, 504, 504, 505, 506, 506, 507, 508, 508, 509, 509, 510, 511, 511, 512, 512]) == 18
    assert candidate(arr = [999, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 14


