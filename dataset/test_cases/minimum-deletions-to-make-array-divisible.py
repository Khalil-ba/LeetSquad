def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],numsDivide = [10, 20, 30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],numsDivide = [10, 20, 30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20],numsDivide = [5, 15, 25, 35]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20],numsDivide = [5, 15, 25, 35]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7],numsDivide = [2, 4, 6, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7],numsDivide = [2, 4, 6, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],numsDivide = [5, 10, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],numsDivide = [5, 10, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],numsDivide = [5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],numsDivide = [5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9],numsDivide = [15, 30, 45, 60]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9],numsDivide = [15, 30, 45, 60]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8],numsDivide = [2, 4, 6, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8],numsDivide = [2, 4, 6, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20],numsDivide = [10, 20, 30, 40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20],numsDivide = [10, 20, 30, 40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 10],numsDivide = [14, 35, 70]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 10],numsDivide = [14, 35, 70]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16],numsDivide = [1, 2, 3, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16],numsDivide = [1, 2, 3, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 6, 8, 9],numsDivide = [30, 45, 60]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 6, 8, 9],numsDivide = [30, 45, 60]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4],numsDivide = [2, 4, 6, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4],numsDivide = [2, 4, 6, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 6],numsDivide = [8, 2, 6, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 6],numsDivide = [8, 2, 6, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 7, 3],numsDivide = [9, 18, 90, 72]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 7, 3],numsDivide = [9, 18, 90, 72]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 4, 3],numsDivide = [9, 6, 9, 3, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 4, 3],numsDivide = [9, 6, 9, 3, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],numsDivide = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],numsDivide = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12],numsDivide = [3, 6, 9, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12],numsDivide = [3, 6, 9, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15],numsDivide = [27, 54, 81, 108]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15],numsDivide = [27, 54, 81, 108]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],numsDivide = [20, 40, 60, 80, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],numsDivide = [20, 40, 60, 80, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81],numsDivide = [162, 324, 486, 648]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81],numsDivide = [162, 324, 486, 648]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],numsDivide = [84, 168, 252]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],numsDivide = [84, 168, 252]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],numsDivide = [100, 200, 300]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],numsDivide = [100, 200, 300]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68],numsDivide = [34, 68, 102, 136, 170]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68],numsDivide = [34, 68, 102, 136, 170]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],numsDivide = [15, 30, 45, 60, 75]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],numsDivide = [15, 30, 45, 60, 75]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128],numsDivide = [256, 512, 1024, 2048]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128],numsDivide = [256, 512, 1024, 2048]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35],numsDivide = [49, 98, 147, 196]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35],numsDivide = [49, 98, 147, 196]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20],numsDivide = [8, 16, 24, 32, 40, 48, 56]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20],numsDivide = [8, 16, 24, 32, 40, 48, 56]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45],numsDivide = [18, 36, 54, 72]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45],numsDivide = [18, 36, 54, 72]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],numsDivide = [18, 36, 54, 72, 90]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],numsDivide = [18, 36, 54, 72, 90]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 42, 63, 84],numsDivide = [42, 84, 126, 168, 210]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 42, 63, 84],numsDivide = [42, 84, 126, 168, 210]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128],numsDivide = [256, 512, 1024, 2048]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128],numsDivide = [256, 512, 1024, 2048]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 27, 81, 243],numsDivide = [81, 243, 729, 2187]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 27, 81, 243],numsDivide = [81, 243, 729, 2187]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],numsDivide = [4, 8, 12, 16, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],numsDivide = [4, 8, 12, 16, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12],numsDivide = [24, 48, 72, 96]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12],numsDivide = [24, 48, 72, 96]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12],numsDivide = [18, 24, 30, 36, 42]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12],numsDivide = [18, 24, 30, 36, 42]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52],numsDivide = [260, 390, 520]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52],numsDivide = [260, 390, 520]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],numsDivide = [30, 45, 60, 75]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],numsDivide = [30, 45, 60, 75]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64],numsDivide = [192, 384, 576, 768]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64],numsDivide = [192, 384, 576, 768]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 21],numsDivide = [36, 54, 72, 90]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 21],numsDivide = [36, 54, 72, 90]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 11, 13, 17],numsDivide = [14, 22, 26, 34]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 11, 13, 17],numsDivide = [14, 22, 26, 34]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 7, 11, 13],numsDivide = [2, 3, 5, 7, 11, 13]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 7, 11, 13],numsDivide = [2, 3, 5, 7, 11, 13]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65],numsDivide = [260, 390, 520, 650]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65],numsDivide = [260, 390, 520, 650]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 37, 41, 43, 47],numsDivide = [93, 121, 143, 187]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 37, 41, 43, 47],numsDivide = [93, 121, 143, 187]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],numsDivide = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],numsDivide = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35],numsDivide = [14, 28, 42, 56]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35],numsDivide = [14, 28, 42, 56]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55],numsDivide = [66, 132, 198, 264]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55],numsDivide = [66, 132, 198, 264]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 7, 10, 14],numsDivide = [4, 10, 14, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 7, 10, 14],numsDivide = [4, 10, 14, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65],numsDivide = [78, 156, 234, 312]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65],numsDivide = [78, 156, 234, 312]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],numsDivide = [100, 50, 25, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],numsDivide = [100, 50, 25, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 93, 124, 155],numsDivide = [186, 372, 558, 744]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 93, 124, 155],numsDivide = [186, 372, 558, 744]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404],numsDivide = [202, 404, 606, 808, 1010]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404],numsDivide = [202, 404, 606, 808, 1010]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],numsDivide = [100, 200, 300, 400]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],numsDivide = [100, 200, 300, 400]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55],numsDivide = [220, 330, 440, 550]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55],numsDivide = [220, 330, 440, 550]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [47, 94, 141, 188, 235],numsDivide = [282, 564, 846, 1128]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [47, 94, 141, 188, 235],numsDivide = [282, 564, 846, 1128]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 58, 87, 116, 145],numsDivide = [174, 348, 522, 696]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 58, 87, 116, 145],numsDivide = [174, 348, 522, 696]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],numsDivide = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],numsDivide = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36],numsDivide = [27, 54, 81, 108, 135]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36],numsDivide = [27, 54, 81, 108, 135]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15],numsDivide = [27, 54, 81, 108]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15],numsDivide = [27, 54, 81, 108]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55],numsDivide = [22, 44, 66, 88]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55],numsDivide = [22, 44, 66, 88]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65],numsDivide = [78, 156, 234, 312]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65],numsDivide = [78, 156, 234, 312]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13],numsDivide = [15, 21, 35, 77]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13],numsDivide = [15, 21, 35, 77]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 27, 36, 45, 54],numsDivide = [54, 108, 162, 216]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 27, 36, 45, 54],numsDivide = [54, 108, 162, 216]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15],numsDivide = [18, 36, 54, 72]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15],numsDivide = [18, 36, 54, 72]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],numsDivide = [60, 105, 140, 231]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],numsDivide = [60, 105, 140, 231]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],numsDivide = [1000, 2000, 3000, 4000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],numsDivide = [1000, 2000, 3000, 4000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 35],numsDivide = [28, 56, 84, 112]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 35],numsDivide = [28, 56, 84, 112]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000],numsDivide = [1000000000, 500000000, 250000000, 125000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000],numsDivide = [1000000000, 500000000, 250000000, 125000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 2000000000, 3000000000],numsDivide = [5000000000, 10000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2000000000, 3000000000],numsDivide = [5000000000, 10000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],numsDivide = [12, 18, 24, 30, 36]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],numsDivide = [12, 18, 24, 30, 36]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909],numsDivide = [1010, 2020, 3030]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909],numsDivide = [1010, 2020, 3030]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85],numsDivide = [102, 204, 306, 408]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85],numsDivide = [102, 204, 306, 408]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 75, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 75, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numsDivide = [100, 200, 300, 400, 500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numsDivide = [100, 200, 300, 400, 500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],numsDivide = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],numsDivide = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104],numsDivide = [104, 208, 312]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104],numsDivide = [104, 208, 312]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],numsDivide = [12, 18, 24, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],numsDivide = [12, 18, 24, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11],numsDivide = [2310, 4620, 6930, 9240]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11],numsDivide = [2310, 4620, 6930, 9240]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28],numsDivide = [42, 56, 70, 84]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28],numsDivide = [42, 56, 70, 84]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 40, 50, 60, 70],numsDivide = [300, 600, 900, 1200]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 40, 50, 60, 70],numsDivide = [300, 600, 900, 1200]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 27, 36, 45],numsDivide = [162, 243, 324]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 27, 36, 45],numsDivide = [162, 243, 324]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66],numsDivide = [132, 264, 396]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66],numsDivide = [132, 264, 396]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30],numsDivide = [100, 150, 200]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30],numsDivide = [100, 150, 200]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],numsDivide = [50, 100, 150, 200]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],numsDivide = [50, 100, 150, 200]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 20, 25, 30],numsDivide = [60, 90, 120, 150]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 20, 25, 30],numsDivide = [60, 90, 120, 150]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42],numsDivide = [420, 840, 1260, 1680]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42],numsDivide = [420, 840, 1260, 1680]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 35, 42],numsDivide = [84, 168, 252, 336]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 35, 42],numsDivide = [84, 168, 252, 336]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],numsDivide = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],numsDivide = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 46, 69, 92, 115],numsDivide = [138, 207, 276, 345, 414]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 46, 69, 92, 115],numsDivide = [138, 207, 276, 345, 414]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],numsDivide = [25, 50, 75, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],numsDivide = [25, 50, 75, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13],numsDivide = [30030, 60060, 90090, 120120]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13],numsDivide = [30030, 60060, 90090, 120120]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 24, 36, 48],numsDivide = [60, 120, 180]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 24, 36, 48],numsDivide = [60, 120, 180]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [43, 86, 129, 172, 215],numsDivide = [258, 387, 516, 645, 774]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [43, 86, 129, 172, 215],numsDivide = [258, 387, 516, 645, 774]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35],numsDivide = [42, 56, 70, 84]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35],numsDivide = [42, 56, 70, 84]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55],numsDivide = [220, 330, 440, 550, 660]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55],numsDivide = [220, 330, 440, 550, 660]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],numsDivide = [3, 5, 7, 9, 11]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],numsDivide = [3, 5, 7, 9, 11]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2],numsDivide = [4, 6, 8, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2],numsDivide = [4, 6, 8, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40],numsDivide = [40, 80, 120, 160]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40],numsDivide = [40, 80, 120, 160]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65],numsDivide = [165, 330, 495]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65],numsDivide = [165, 330, 495]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [43, 86, 129, 172, 215],numsDivide = [258, 516, 774, 1032]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [43, 86, 129, 172, 215],numsDivide = [258, 516, 774, 1032]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30],numsDivide = [150, 300, 450, 600, 750]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30],numsDivide = [150, 300, 450, 600, 750]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18],numsDivide = [180, 360, 540, 720, 900]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18],numsDivide = [180, 360, 540, 720, 900]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],numsDivide = [100, 200, 300, 400, 500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],numsDivide = [100, 200, 300, 400, 500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],numsDivide = [13, 17, 19, 29, 31]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],numsDivide = [13, 17, 19, 29, 31]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 2002, 3003, 4004],numsDivide = [2002, 4004, 6006, 8008, 10010]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 2002, 3003, 4004],numsDivide = [2002, 4004, 6006, 8008, 10010]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45],numsDivide = [108, 162, 216, 270, 324]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45],numsDivide = [108, 162, 216, 270, 324]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],numsDivide = [20, 40, 60, 80, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],numsDivide = [20, 40, 60, 80, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65],numsDivide = [78, 130, 195, 260, 325]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65],numsDivide = [78, 130, 195, 260, 325]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12],numsDivide = [36, 72, 108]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12],numsDivide = [36, 72, 108]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23],numsDivide = [2310, 4620, 6930, 9240]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23],numsDivide = [2310, 4620, 6930, 9240]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 12, 18],numsDivide = [27, 54, 81, 108]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 12, 18],numsDivide = [27, 54, 81, 108]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45],numsDivide = [75, 150, 225, 300]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45],numsDivide = [75, 150, 225, 300]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 100, 150, 200]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 100, 150, 200]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55],numsDivide = [110, 220, 330, 440, 550]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55],numsDivide = [110, 220, 330, 440, 550]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [37, 74, 111, 148, 185],numsDivide = [238, 357, 476, 595, 714]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [37, 74, 111, 148, 185],numsDivide = [238, 357, 476, 595, 714]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 62, 93, 124, 155],numsDivide = [186, 279, 372, 465, 558]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 62, 93, 124, 155],numsDivide = [186, 279, 372, 465, 558]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [41, 82, 123, 164, 205],numsDivide = [246, 369, 492, 615, 738]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [41, 82, 123, 164, 205],numsDivide = [246, 369, 492, 615, 738]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78],numsDivide = [156, 195, 260, 390]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78],numsDivide = [156, 195, 260, 390]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35],numsDivide = [49, 98, 147, 196]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35],numsDivide = [49, 98, 147, 196]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28],numsDivide = [42, 56, 70]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28],numsDivide = [42, 56, 70]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 60, 90, 120, 150, 180],numsDivide = [300, 600, 900, 1200]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 60, 90, 120, 150, 180],numsDivide = [300, 600, 900, 1200]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35],numsDivide = [25, 50, 75, 100, 125]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35],numsDivide = [25, 50, 75, 100, 125]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],numsDivide = [150, 300, 450, 600]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],numsDivide = [150, 300, 450, 600]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],numsDivide = [14, 28, 42, 56, 70]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],numsDivide = [14, 28, 42, 56, 70]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52],numsDivide = [26, 52, 78, 104, 130]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52],numsDivide = [26, 52, 78, 104, 130]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 34, 51, 68, 85],numsDivide = [340, 680, 1020, 1360]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 34, 51, 68, 85],numsDivide = [340, 680, 1020, 1360]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 100, 150, 200]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 100, 150, 200]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42],numsDivide = [14, 28, 42, 56, 70]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42],numsDivide = [14, 28, 42, 56, 70]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999],numsDivide = [1110, 2220, 3330]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999],numsDivide = [1110, 2220, 3330]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 7, 11],numsDivide = [105, 165, 231]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 7, 11],numsDivide = [105, 165, 231]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63],numsDivide = [108, 162, 216, 270]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63],numsDivide = [108, 162, 216, 270]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65],numsDivide = [26, 52, 78, 104]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65],numsDivide = [26, 52, 78, 104]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55],numsDivide = [66, 77, 88, 99]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55],numsDivide = [66, 77, 88, 99]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30],numsDivide = [60, 120, 180, 240]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30],numsDivide = [60, 120, 180, 240]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 100, 150, 200, 250]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 100, 150, 200, 250]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400],numsDivide = [500, 1000, 1500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400],numsDivide = [500, 1000, 1500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [37, 74, 111, 148, 185],numsDivide = [222, 444, 666, 888]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [37, 74, 111, 148, 185],numsDivide = [222, 444, 666, 888]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 58, 87, 116, 145],numsDivide = [174, 261, 348, 435, 522]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 58, 87, 116, 145],numsDivide = [174, 261, 348, 435, 522]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],numsDivide = [10, 20, 30, 40, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],numsDivide = [10, 20, 30, 40, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40],numsDivide = [100, 200, 300, 400]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40],numsDivide = [100, 200, 300, 400]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 46, 69, 92, 115],numsDivide = [138, 276, 414, 552]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 46, 69, 92, 115],numsDivide = [138, 276, 414, 552]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 38, 57, 76, 95],numsDivide = [114, 190, 285, 380, 475]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 38, 57, 76, 95],numsDivide = [114, 190, 285, 380, 475]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],numsDivide = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],numsDivide = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 38, 57, 76, 95],numsDivide = [114, 228, 342, 456]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 38, 57, 76, 95],numsDivide = [114, 228, 342, 456]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25],numsDivide = [100, 200, 300]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25],numsDivide = [100, 200, 300]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],numsDivide = [12, 24, 36, 48, 60]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],numsDivide = [12, 24, 36, 48, 60]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44],numsDivide = [22, 44, 66, 88, 110]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44],numsDivide = [22, 44, 66, 88, 110]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],numsDivide = [24, 36, 48, 60]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],numsDivide = [24, 36, 48, 60]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 23, 31, 37, 41, 43],numsDivide = [51, 68, 85]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 23, 31, 37, 41, 43],numsDivide = [51, 68, 85]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40],numsDivide = [16, 32, 48, 64, 80, 96]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40],numsDivide = [16, 32, 48, 64, 80, 96]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 38, 57, 76],numsDivide = [38, 76, 114, 152, 190]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 38, 57, 76],numsDivide = [38, 76, 114, 152, 190]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [41, 82, 123, 164, 205],numsDivide = [246, 492, 738, 984]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [41, 82, 123, 164, 205],numsDivide = [246, 492, 738, 984]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],numsDivide = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],numsDivide = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35],numsDivide = [42, 56, 84, 98, 140]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35],numsDivide = [42, 56, 84, 98, 140]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30],numsDivide = [12, 24, 36, 48, 60, 72]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30],numsDivide = [12, 24, 36, 48, 60, 72]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5],numsDivide = [10, 20, 30, 40, 50]) == 0
    assert candidate(nums = [5, 10, 15, 20],numsDivide = [5, 15, 25, 35]) == 0
    assert candidate(nums = [1, 3, 5, 7],numsDivide = [2, 4, 6, 8]) == 0
    assert candidate(nums = [10, 20, 30],numsDivide = [5, 10, 15]) == -1
    assert candidate(nums = [5, 5, 5, 5],numsDivide = [5, 5, 5, 5]) == 0
    assert candidate(nums = [3, 5, 7, 9],numsDivide = [15, 30, 45, 60]) == 0
    assert candidate(nums = [2, 4, 6, 8],numsDivide = [2, 4, 6, 8]) == 0
    assert candidate(nums = [5, 10, 15, 20],numsDivide = [10, 20, 30, 40]) == 0
    assert candidate(nums = [5, 7, 10],numsDivide = [14, 35, 70]) == 1
    assert candidate(nums = [2, 4, 8, 16],numsDivide = [1, 2, 3, 4]) == -1
    assert candidate(nums = [3, 5, 6, 8, 9],numsDivide = [30, 45, 60]) == 0
    assert candidate(nums = [1, 2, 3, 4],numsDivide = [2, 4, 6, 8]) == 0
    assert candidate(nums = [4, 3, 6],numsDivide = [8, 2, 6, 10]) == -1
    assert candidate(nums = [3, 9, 7, 3],numsDivide = [9, 18, 90, 72]) == 0
    assert candidate(nums = [2, 3, 2, 4, 3],numsDivide = [9, 6, 9, 3, 15]) == 2
    assert candidate(nums = [1],numsDivide = [1]) == 0
    assert candidate(nums = [3, 6, 9, 12],numsDivide = [3, 6, 9, 12]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15],numsDivide = [27, 54, 81, 108]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10],numsDivide = [20, 40, 60, 80, 100]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81],numsDivide = [162, 324, 486, 648]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],numsDivide = [84, 168, 252]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25],numsDivide = [100, 200, 300]) == 0
    assert candidate(nums = [17, 34, 51, 68],numsDivide = [34, 68, 102, 136, 170]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],numsDivide = [15, 30, 45, 60, 75]) == 0
    assert candidate(nums = [8, 16, 32, 64, 128],numsDivide = [256, 512, 1024, 2048]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35],numsDivide = [49, 98, 147, 196]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == -1
    assert candidate(nums = [4, 8, 12, 16, 20],numsDivide = [8, 16, 24, 32, 40, 48, 56]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45],numsDivide = [18, 36, 54, 72]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],numsDivide = [18, 36, 54, 72, 90]) == 0
    assert candidate(nums = [21, 42, 63, 84],numsDivide = [42, 84, 126, 168, 210]) == 0
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128],numsDivide = [256, 512, 1024, 2048]) == 0
    assert candidate(nums = [3, 9, 27, 81, 243],numsDivide = [81, 243, 729, 2187]) == 0
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],numsDivide = [4, 8, 12, 16, 20]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12],numsDivide = [24, 48, 72, 96]) == 0
    assert candidate(nums = [3, 6, 9, 12],numsDivide = [18, 24, 30, 36, 42]) == 0
    assert candidate(nums = [13, 26, 39, 52],numsDivide = [260, 390, 520]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],numsDivide = [30, 45, 60, 75]) == -1
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64],numsDivide = [192, 384, 576, 768]) == 0
    assert candidate(nums = [12, 15, 18, 21],numsDivide = [36, 54, 72, 90]) == 2
    assert candidate(nums = [7, 11, 13, 17],numsDivide = [14, 22, 26, 34]) == -1
    assert candidate(nums = [1, 2, 3, 5, 7, 11, 13],numsDivide = [2, 3, 5, 7, 11, 13]) == 0
    assert candidate(nums = [13, 26, 39, 52, 65],numsDivide = [260, 390, 520, 650]) == 0
    assert candidate(nums = [31, 37, 41, 43, 47],numsDivide = [93, 121, 143, 187]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],numsDivide = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35],numsDivide = [14, 28, 42, 56]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55],numsDivide = [66, 132, 198, 264]) == 0
    assert candidate(nums = [2, 5, 7, 10, 14],numsDivide = [4, 10, 14, 20]) == 0
    assert candidate(nums = [13, 26, 39, 52, 65],numsDivide = [78, 156, 234, 312]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25],numsDivide = [100, 50, 25, 20]) == 0
    assert candidate(nums = [31, 62, 93, 124, 155],numsDivide = [186, 372, 558, 744]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
    assert candidate(nums = [101, 202, 303, 404],numsDivide = [202, 404, 606, 808, 1010]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25],numsDivide = [100, 200, 300, 400]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55],numsDivide = [220, 330, 440, 550]) == 0
    assert candidate(nums = [47, 94, 141, 188, 235],numsDivide = [282, 564, 846, 1128]) == 0
    assert candidate(nums = [29, 58, 87, 116, 145],numsDivide = [174, 348, 522, 696]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],numsDivide = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0
    assert candidate(nums = [9, 18, 27, 36],numsDivide = [27, 54, 81, 108, 135]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15],numsDivide = [27, 54, 81, 108]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55],numsDivide = [22, 44, 66, 88]) == 0
    assert candidate(nums = [13, 26, 39, 52, 65],numsDivide = [78, 156, 234, 312]) == 0
    assert candidate(nums = [3, 5, 7, 11, 13],numsDivide = [15, 21, 35, 77]) == -1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [18, 27, 36, 45, 54],numsDivide = [54, 108, 162, 216]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15],numsDivide = [18, 36, 54, 72]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],numsDivide = [60, 105, 140, 231]) == -1
    assert candidate(nums = [100, 200, 300, 400, 500],numsDivide = [1000, 2000, 3000, 4000]) == 0
    assert candidate(nums = [7, 14, 28, 35],numsDivide = [28, 56, 84, 112]) == 0
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000],numsDivide = [1000000000, 500000000, 250000000, 125000000]) == 0
    assert candidate(nums = [1000000000, 2000000000, 3000000000],numsDivide = [5000000000, 10000000000]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10],numsDivide = [12, 18, 24, 30, 36]) == 0
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909],numsDivide = [1010, 2020, 3030]) == 0
    assert candidate(nums = [17, 34, 51, 68, 85],numsDivide = [102, 204, 306, 408]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 75, 100]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],numsDivide = [100, 200, 300, 400, 500]) == 0
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],numsDivide = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104],numsDivide = [104, 208, 312]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10],numsDivide = [12, 18, 24, 30]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11],numsDivide = [2310, 4620, 6930, 9240]) == 0
    assert candidate(nums = [7, 14, 21, 28],numsDivide = [42, 56, 70, 84]) == 0
    assert candidate(nums = [30, 40, 50, 60, 70],numsDivide = [300, 600, 900, 1200]) == 0
    assert candidate(nums = [18, 27, 36, 45],numsDivide = [162, 243, 324]) == 1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],numsDivide = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums = [11, 22, 33, 44, 55, 66],numsDivide = [132, 264, 396]) == 0
    assert candidate(nums = [10, 15, 20, 25, 30],numsDivide = [100, 150, 200]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],numsDivide = [50, 100, 150, 200]) == 0
    assert candidate(nums = [12, 15, 20, 25, 30],numsDivide = [60, 90, 120, 150]) == 1
    assert candidate(nums = [7, 14, 21, 28, 35, 42],numsDivide = [420, 840, 1260, 1680]) == 0
    assert candidate(nums = [7, 14, 28, 35, 42],numsDivide = [84, 168, 252, 336]) == 0
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],numsDivide = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == -1
    assert candidate(nums = [23, 46, 69, 92, 115],numsDivide = [138, 207, 276, 345, 414]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50],numsDivide = [25, 50, 75, 100]) == -1
    assert candidate(nums = [2, 3, 5, 7, 11, 13],numsDivide = [30030, 60060, 90090, 120120]) == 0
    assert candidate(nums = [12, 24, 36, 48],numsDivide = [60, 120, 180]) == 0
    assert candidate(nums = [43, 86, 129, 172, 215],numsDivide = [258, 387, 516, 645, 774]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35],numsDivide = [42, 56, 70, 84]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55],numsDivide = [220, 330, 440, 550, 660]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10],numsDivide = [3, 5, 7, 9, 11]) == -1
    assert candidate(nums = [2, 2, 2, 2, 2],numsDivide = [4, 6, 8, 10]) == 0
    assert candidate(nums = [8, 16, 24, 32, 40],numsDivide = [40, 80, 120, 160]) == 0
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65],numsDivide = [165, 330, 495]) == 0
    assert candidate(nums = [43, 86, 129, 172, 215],numsDivide = [258, 516, 774, 1032]) == 0
    assert candidate(nums = [10, 15, 20, 25, 30],numsDivide = [150, 300, 450, 600, 750]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18],numsDivide = [180, 360, 540, 720, 900]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50],numsDivide = [100, 200, 300, 400, 500]) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],numsDivide = [13, 17, 19, 29, 31]) == -1
    assert candidate(nums = [1001, 2002, 3003, 4004],numsDivide = [2002, 4004, 6006, 8008, 10010]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45],numsDivide = [108, 162, 216, 270, 324]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],numsDivide = [20, 40, 60, 80, 100]) == 0
    assert candidate(nums = [13, 26, 39, 52, 65],numsDivide = [78, 130, 195, 260, 325]) == 0
    assert candidate(nums = [3, 6, 9, 12],numsDivide = [36, 72, 108]) == 0
    assert candidate(nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23],numsDivide = [2310, 4620, 6930, 9240]) == 0
    assert candidate(nums = [3, 9, 12, 18],numsDivide = [27, 54, 81, 108]) == 0
    assert candidate(nums = [5, 15, 25, 35, 45],numsDivide = [75, 150, 225, 300]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 100, 150, 200]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55],numsDivide = [110, 220, 330, 440, 550]) == 0
    assert candidate(nums = [37, 74, 111, 148, 185],numsDivide = [238, 357, 476, 595, 714]) == -1
    assert candidate(nums = [31, 62, 93, 124, 155],numsDivide = [186, 279, 372, 465, 558]) == 0
    assert candidate(nums = [41, 82, 123, 164, 205],numsDivide = [246, 369, 492, 615, 738]) == 0
    assert candidate(nums = [13, 26, 39, 52, 65, 78],numsDivide = [156, 195, 260, 390]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35],numsDivide = [49, 98, 147, 196]) == 0
    assert candidate(nums = [7, 14, 21, 28],numsDivide = [42, 56, 70]) == 0
    assert candidate(nums = [30, 60, 90, 120, 150, 180],numsDivide = [300, 600, 900, 1200]) == 0
    assert candidate(nums = [5, 15, 25, 35],numsDivide = [25, 50, 75, 100, 125]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500],numsDivide = [150, 300, 450, 600]) == -1
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],numsDivide = [14, 28, 42, 56, 70]) == 0
    assert candidate(nums = [13, 26, 39, 52],numsDivide = [26, 52, 78, 104, 130]) == 0
    assert candidate(nums = [17, 34, 51, 68, 85],numsDivide = [340, 680, 1020, 1360]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 100, 150, 200]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42],numsDivide = [14, 28, 42, 56, 70]) == 0
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999],numsDivide = [1110, 2220, 3330]) == 0
    assert candidate(nums = [1, 2, 3, 5, 7, 11],numsDivide = [105, 165, 231]) == 0
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63],numsDivide = [108, 162, 216, 270]) == 0
    assert candidate(nums = [13, 26, 39, 52, 65],numsDivide = [26, 52, 78, 104]) == 0
    assert candidate(nums = [11, 22, 33, 44, 55],numsDivide = [66, 77, 88, 99]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30],numsDivide = [60, 120, 180, 240]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25],numsDivide = [50, 100, 150, 200, 250]) == 0
    assert candidate(nums = [100, 200, 300, 400],numsDivide = [500, 1000, 1500]) == 0
    assert candidate(nums = [37, 74, 111, 148, 185],numsDivide = [222, 444, 666, 888]) == 0
    assert candidate(nums = [29, 58, 87, 116, 145],numsDivide = [174, 261, 348, 435, 522]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50],numsDivide = [10, 20, 30, 40, 50]) == 0
    assert candidate(nums = [8, 16, 24, 32, 40],numsDivide = [100, 200, 300, 400]) == -1
    assert candidate(nums = [23, 46, 69, 92, 115],numsDivide = [138, 276, 414, 552]) == 0
    assert candidate(nums = [19, 38, 57, 76, 95],numsDivide = [114, 190, 285, 380, 475]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],numsDivide = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == -1
    assert candidate(nums = [19, 38, 57, 76, 95],numsDivide = [114, 228, 342, 456]) == 0
    assert candidate(nums = [10, 15, 20, 25],numsDivide = [100, 200, 300]) == 0
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],numsDivide = [12, 24, 36, 48, 60]) == 0
    assert candidate(nums = [11, 22, 33, 44],numsDivide = [22, 44, 66, 88, 110]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10],numsDivide = [24, 36, 48, 60]) == 0
    assert candidate(nums = [17, 23, 31, 37, 41, 43],numsDivide = [51, 68, 85]) == 0
    assert candidate(nums = [8, 16, 24, 32, 40],numsDivide = [16, 32, 48, 64, 80, 96]) == 0
    assert candidate(nums = [19, 38, 57, 76],numsDivide = [38, 76, 114, 152, 190]) == 0
    assert candidate(nums = [41, 82, 123, 164, 205],numsDivide = [246, 492, 738, 984]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1],numsDivide = [1]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35],numsDivide = [42, 56, 84, 98, 140]) == 0
    assert candidate(nums = [6, 12, 18, 24, 30],numsDivide = [12, 24, 36, 48, 60, 72]) == 0


