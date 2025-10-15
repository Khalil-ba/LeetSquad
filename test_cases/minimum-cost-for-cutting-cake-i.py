def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(m = 5,n = 4,horizontalCut = [1, 2, 3, 4],verticalCut = [2, 4, 6]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 4,horizontalCut = [1, 2, 3, 4],verticalCut = [2, 4, 6]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,horizontalCut = [2, 5, 7],verticalCut = [3, 8]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,horizontalCut = [2, 5, 7],verticalCut = [3, 8]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2,horizontalCut = [7],verticalCut = [4]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2,horizontalCut = [7],verticalCut = [4]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,horizontalCut = [1, 2, 3],verticalCut = [1, 2]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,horizontalCut = [1, 2, 3],verticalCut = [1, 2]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 4,horizontalCut = [1, 4, 6, 8],verticalCut = [2, 3, 5]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 4,horizontalCut = [1, 4, 6, 8],verticalCut = [2, 3, 5]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 5,horizontalCut = [1, 3, 5, 7, 9],verticalCut = [2, 4, 6, 8]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 5,horizontalCut = [1, 3, 5, 7, 9],verticalCut = [2, 4, 6, 8]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,horizontalCut = [1, 2],verticalCut = [1, 2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,horizontalCut = [1, 2],verticalCut = [1, 2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 4,horizontalCut = [1, 2, 3, 4],verticalCut = [1, 2, 3]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 4,horizontalCut = [1, 2, 3, 4],verticalCut = [1, 2, 3]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 4,horizontalCut = [1, 3, 6, 9],verticalCut = [2, 4, 7]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 4,horizontalCut = [1, 3, 6, 9],verticalCut = [2, 4, 7]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 2,horizontalCut = [1, 3],verticalCut = [5]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 2,horizontalCut = [1, 3],verticalCut = [5]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,horizontalCut = [2, 5, 7],verticalCut = [1, 6]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,horizontalCut = [2, 5, 7],verticalCut = [1, 6]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,horizontalCut = [2, 4, 6],verticalCut = [1, 3]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,horizontalCut = [2, 4, 6],verticalCut = [1, 3]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(m = 18,n = 16,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2598
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 18,n = 16,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2598: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 12,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 3763
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 12,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 3763: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27],verticalCut = [2, 5, 8, 11, 14, 17, 20, 23, 26]) == 1071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27],verticalCut = [2, 5, 8, 11, 14, 17, 20, 23, 26]) == 1071: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 6,horizontalCut = [1, 3, 5, 7, 9, 11],verticalCut = [2, 4, 6, 8, 10]) == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 6,horizontalCut = [1, 3, 5, 7, 9, 11],verticalCut = [2, 4, 6, 8, 10]) == 191: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 8,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27],verticalCut = [2, 5, 8, 11, 14, 17, 20, 23]) == 891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 8,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27],verticalCut = [2, 5, 8, 11, 14, 17, 20, 23]) == 891: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15],verticalCut = [1, 3, 5, 7, 9, 11, 13, 15]) == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15],verticalCut = [1, 3, 5, 7, 9, 11, 13, 15]) == 455: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 5,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCut = [5, 15, 25, 35, 45]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 5,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCut = [5, 15, 25, 35, 45]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(m = 18,n = 16,horizontalCut = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == 5983
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 18,n = 16,horizontalCut = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == 5983: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 8,horizontalCut = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72],verticalCut = [4, 8, 12, 16, 20, 24, 28, 32]) == 2036
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 8,horizontalCut = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72],verticalCut = [4, 8, 12, 16, 20, 24, 28, 32]) == 2036: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 10,horizontalCut = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48],verticalCut = [2, 6, 10, 14, 18, 20, 24, 28, 32, 36]) == 2216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 10,horizontalCut = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48],verticalCut = [2, 6, 10, 14, 18, 20, 24, 28, 32, 36]) == 2216: {e}')
    
    total += 1
    try:
        result = candidate(m = 18,n = 12,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 3045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 18,n = 12,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 3045: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 10,horizontalCut = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1523
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 10,horizontalCut = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1523: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 12,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 1199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 12,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 1199: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 10,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 2874
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 10,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 2874: {e}')
    
    total += 1
    try:
        result = candidate(m = 16,n = 20,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 4240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 16,n = 20,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 4240: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 6289
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 6289: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 8,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCut = [5, 15, 25, 35, 45, 55, 65, 75]) == 2900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 8,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCut = [5, 15, 25, 35, 45, 55, 65, 75]) == 2900: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 6,horizontalCut = [2, 4, 6, 8, 10, 12],verticalCut = [1, 3, 5, 7, 9, 11]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 6,horizontalCut = [2, 4, 6, 8, 10, 12],verticalCut = [1, 3, 5, 7, 9, 11]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 7,horizontalCut = [2, 4, 6, 8, 10, 12, 14],verticalCut = [1, 3, 5, 7, 9, 11]) == 289
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 7,horizontalCut = [2, 4, 6, 8, 10, 12, 14],verticalCut = [1, 3, 5, 7, 9, 11]) == 289: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 8,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16]) == 733
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 8,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16]) == 733: {e}')
    
    total += 1
    try:
        result = candidate(m = 19,n = 14,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 19,n = 14,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1536: {e}')
    
    total += 1
    try:
        result = candidate(m = 11,n = 12,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 1652
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 11,n = 12,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 1652: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 7,horizontalCut = [2, 4, 6, 8, 10, 12, 14, 16],verticalCut = [1, 3, 5, 7, 9, 11, 13]) == 413
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 7,horizontalCut = [2, 4, 6, 8, 10, 12, 14, 16],verticalCut = [1, 3, 5, 7, 9, 11, 13]) == 413: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,horizontalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,horizontalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 888: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 7,horizontalCut = [7, 14, 21, 28, 35, 42, 49, 56],verticalCut = [5, 10, 15, 20, 25, 30, 35]) == 1234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 7,horizontalCut = [7, 14, 21, 28, 35, 42, 49, 56],verticalCut = [5, 10, 15, 20, 25, 30, 35]) == 1234: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 2850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 2850: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 10,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 865
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 10,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 865: {e}')
    
    total += 1
    try:
        result = candidate(m = 18,n = 15,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 6621
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 18,n = 15,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 6621: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],verticalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 2674
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],verticalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 2674: {e}')
    
    total += 1
    try:
        result = candidate(m = 16,n = 14,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]) == 7675
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 16,n = 14,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]) == 7675: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],verticalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 6099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],verticalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 6099: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 10,horizontalCut = [3, 6, 9, 12, 15, 18, 21],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 10,horizontalCut = [3, 6, 9, 12, 15, 18, 21],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 714: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 15,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == 16810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 15,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == 16810: {e}')
    
    total += 1
    try:
        result = candidate(m = 16,n = 14,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 16,n = 14,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1212: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 15,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1835
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 15,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1835: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == 6125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == 6125: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 10,horizontalCut = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],verticalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 6850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 10,horizontalCut = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],verticalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 6850: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 12,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 2267
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 12,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 2267: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 5,horizontalCut = [7, 14, 21, 28, 35],verticalCut = [4, 8, 12, 16, 20]) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 5,horizontalCut = [7, 14, 21, 28, 35],verticalCut = [4, 8, 12, 16, 20]) == 405: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 12,horizontalCut = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]) == 4578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 12,horizontalCut = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]) == 4578: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 9,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8]) == 414
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 9,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8]) == 414: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 9,horizontalCut = [3, 6, 9, 12, 15, 18],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 9,horizontalCut = [3, 6, 9, 12, 15, 18],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(m = 16,n = 16,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48],verticalCut = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47]) == 5070
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 16,n = 16,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48],verticalCut = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47]) == 5070: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(m = 5,n = 4,horizontalCut = [1, 2, 3, 4],verticalCut = [2, 4, 6]) == 49
    assert candidate(m = 4,n = 3,horizontalCut = [2, 5, 7],verticalCut = [3, 8]) == 47
    assert candidate(m = 2,n = 2,horizontalCut = [7],verticalCut = [4]) == 15
    assert candidate(m = 4,n = 3,horizontalCut = [1, 2, 3],verticalCut = [1, 2]) == 17
    assert candidate(m = 5,n = 4,horizontalCut = [1, 4, 6, 8],verticalCut = [2, 3, 5]) == 61
    assert candidate(m = 6,n = 5,horizontalCut = [1, 3, 5, 7, 9],verticalCut = [2, 4, 6, 8]) == 115
    assert candidate(m = 3,n = 3,horizontalCut = [1, 2],verticalCut = [1, 2]) == 11
    assert candidate(m = 5,n = 4,horizontalCut = [1, 2, 3, 4],verticalCut = [1, 2, 3]) == 36
    assert candidate(m = 5,n = 4,horizontalCut = [1, 3, 6, 9],verticalCut = [2, 4, 7]) == 68
    assert candidate(m = 3,n = 2,horizontalCut = [1, 3],verticalCut = [5]) == 13
    assert candidate(m = 4,n = 3,horizontalCut = [2, 5, 7],verticalCut = [1, 6]) == 37
    assert candidate(m = 4,n = 3,horizontalCut = [2, 4, 6],verticalCut = [1, 3]) == 27
    assert candidate(m = 18,n = 16,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 2598
    assert candidate(m = 15,n = 12,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 3763
    assert candidate(m = 10,n = 10,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27],verticalCut = [2, 5, 8, 11, 14, 17, 20, 23, 26]) == 1071
    assert candidate(m = 7,n = 6,horizontalCut = [1, 3, 5, 7, 9, 11],verticalCut = [2, 4, 6, 8, 10]) == 191
    assert candidate(m = 10,n = 8,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27],verticalCut = [2, 5, 8, 11, 14, 17, 20, 23]) == 891
    assert candidate(m = 8,n = 8,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15],verticalCut = [1, 3, 5, 7, 9, 11, 13, 15]) == 455
    assert candidate(m = 10,n = 5,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCut = [5, 15, 25, 35, 45]) == 1500
    assert candidate(m = 18,n = 16,horizontalCut = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == 5983
    assert candidate(m = 12,n = 8,horizontalCut = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72],verticalCut = [4, 8, 12, 16, 20, 24, 28, 32]) == 2036
    assert candidate(m = 12,n = 10,horizontalCut = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48],verticalCut = [2, 6, 10, 14, 18, 20, 24, 28, 32, 36]) == 2216
    assert candidate(m = 18,n = 12,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 3045
    assert candidate(m = 12,n = 10,horizontalCut = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1523
    assert candidate(m = 12,n = 12,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 1199
    assert candidate(m = 15,n = 10,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 2874
    assert candidate(m = 16,n = 20,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 4240
    assert candidate(m = 20,n = 20,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 6289
    assert candidate(m = 10,n = 8,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCut = [5, 15, 25, 35, 45, 55, 65, 75]) == 2900
    assert candidate(m = 6,n = 6,horizontalCut = [2, 4, 6, 8, 10, 12],verticalCut = [1, 3, 5, 7, 9, 11]) == 220
    assert candidate(m = 8,n = 7,horizontalCut = [2, 4, 6, 8, 10, 12, 14],verticalCut = [1, 3, 5, 7, 9, 11]) == 289
    assert candidate(m = 10,n = 8,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16]) == 733
    assert candidate(m = 19,n = 14,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1536
    assert candidate(m = 11,n = 12,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 1652
    assert candidate(m = 9,n = 7,horizontalCut = [2, 4, 6, 8, 10, 12, 14, 16],verticalCut = [1, 3, 5, 7, 9, 11, 13]) == 413
    assert candidate(m = 10,n = 10,horizontalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 888
    assert candidate(m = 8,n = 7,horizontalCut = [7, 14, 21, 28, 35, 42, 49, 56],verticalCut = [5, 10, 15, 20, 25, 30, 35]) == 1234
    assert candidate(m = 20,n = 20,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 2850
    assert candidate(m = 15,n = 10,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 865
    assert candidate(m = 18,n = 15,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 6621
    assert candidate(m = 15,n = 15,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],verticalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 2674
    assert candidate(m = 16,n = 14,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]) == 7675
    assert candidate(m = 20,n = 20,horizontalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],verticalCut = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 6099
    assert candidate(m = 7,n = 10,horizontalCut = [3, 6, 9, 12, 15, 18, 21],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 714
    assert candidate(m = 20,n = 15,horizontalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == 16810
    assert candidate(m = 16,n = 14,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 1212
    assert candidate(m = 20,n = 15,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1835
    assert candidate(m = 15,n = 15,horizontalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],verticalCut = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == 6125
    assert candidate(m = 15,n = 10,horizontalCut = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],verticalCut = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 6850
    assert candidate(m = 15,n = 12,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 2267
    assert candidate(m = 6,n = 5,horizontalCut = [7, 14, 21, 28, 35],verticalCut = [4, 8, 12, 16, 20]) == 405
    assert candidate(m = 15,n = 12,horizontalCut = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135],verticalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]) == 4578
    assert candidate(m = 12,n = 9,horizontalCut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],verticalCut = [1, 2, 3, 4, 5, 6, 7, 8]) == 414
    assert candidate(m = 7,n = 9,horizontalCut = [3, 6, 9, 12, 15, 18],verticalCut = [2, 4, 6, 8, 10, 12, 14, 16]) == 465
    assert candidate(m = 16,n = 16,horizontalCut = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48],verticalCut = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47]) == 5070


