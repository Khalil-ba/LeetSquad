def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5],k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5],k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],k = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],k = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100],k = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100],k = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100],k = 100) == 14950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100],k = 100) == 14950: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],k = 4) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],k = 4) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100],k = 100) == 14950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100],k = 100) == 14950: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],k = 5) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],k = 5) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],k = 60) == 7530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],k = 60) == 7530: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 6225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 6225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 42, 42, 42],k = 7) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 42, 42, 42],k = 7) == 315: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 15) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 15) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50],k = 10) == 545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50],k = 10) == 545: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 15) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 15) == 390: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],k = 100) == 5050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],k = 100) == 5050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 1035
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 1035: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],k = 5) == 710
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],k = 5) == 710: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 20) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 20) == 290: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 100) == 6950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 100) == 6950: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 7) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 7) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 75, 100],k = 15) == 1605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 75, 100],k = 15) == 1605: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 7) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 7) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],k = 30) == 1935
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],k = 30) == 1935: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 405: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 3725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 3725: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 16) == 760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 16) == 760: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95],k = 10) == 1035
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95],k = 10) == 1035: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 50) == 1575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 50) == 1575: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 75) == 10275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 75) == 10275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 145: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 1045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 1045: {e}')
    
    total += 1
    try:
        result = candidate(nums = [55, 55, 55, 55, 55, 55, 55, 55, 55, 55],k = 100) == 10450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [55, 55, 55, 55, 55, 55, 55, 55, 55, 55],k = 100) == 10450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 15) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 15) == 180: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 30) == 1035
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 30) == 1035: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 91: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 6225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 6225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 12) == 306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 12) == 306: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 100) == 14950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 100) == 14950: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50],k = 100) == 9950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50],k = 100) == 9950: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 50) == 6125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 50) == 6125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 50) == 6475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 50) == 6475: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 20) == 590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 20) == 590: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 100) == 5750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 100) == 5750: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 40) == 1980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 40) == 1980: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 50) == 6225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 50) == 6225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 75) == 6525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 75) == 6525: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95],k = 20) == 2170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95],k = 20) == 2170: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11],k = 10) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11],k = 10) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 52, 53, 54],k = 8) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 52, 53, 54],k = 8) == 460: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 25) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 25) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 11) == 1155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 11) == 1155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 75) == 4200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 75) == 4200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 1275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 1275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 10) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 10) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 100) == 14950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 100) == 14950: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 2190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 2190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == 460: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 100) == 19950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 100) == 19950: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500],k = 25) == 12800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500],k = 25) == 12800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 15) == 1605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 15) == 1605: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42],k = 100) == 9150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42],k = 100) == 9150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60],k = 10) == 645
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60],k = 10) == 645: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 15) == 1590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 15) == 1590: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 50) == 1325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 50) == 1325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 100) == 5450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 100) == 5450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],k = 30) == 1545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],k = 30) == 1545: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 100) == 14850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 100) == 14850: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 50) == 2225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 50) == 2225: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30],k = 9) == 306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30],k = 9) == 306: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == 325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 75) == 10275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 75) == 10275: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99],k = 100) == 14850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99],k = 100) == 14850: {e}')
    
    total += 1
    try:
        result = candidate(nums = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],k = 75) == 10200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],k = 75) == 10200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],k = 15) == 855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],k = 15) == 855: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12],k = 15) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12],k = 15) == 285: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 1725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 1725: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 590: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],k = 100) == 7450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],k = 100) == 7450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 20) == 2190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 20) == 2190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50],k = 7) == 371
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50],k = 7) == 371: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 2800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 2800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 30) == 3405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 30) == 3405: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95],k = 25) == 2775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95],k = 25) == 2775: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 15) == 1605
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 15) == 1605: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 25) == 2800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 25) == 2800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 145: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 3725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 3725: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 18
    assert candidate(nums = [5, 5, 5],k = 2) == 11
    assert candidate(nums = [1, 1, 1, 1],k = 4) == 10
    assert candidate(nums = [10, 20, 30],k = 1) == 30
    assert candidate(nums = [100],k = 1) == 100
    assert candidate(nums = [1, 1, 1, 1, 1],k = 10) == 55
    assert candidate(nums = [100],k = 100) == 14950
    assert candidate(nums = [10, 20, 30],k = 4) == 126
    assert candidate(nums = [1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [1, 1, 1, 1],k = 5) == 15
    assert candidate(nums = [100, 100, 100, 100],k = 100) == 14950
    assert candidate(nums = [10, 20, 30],k = 5) == 160
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],k = 60) == 7530
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 6225
    assert candidate(nums = [42, 42, 42, 42, 42, 42, 42],k = 7) == 315
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 15) == 165
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50],k = 10) == 545
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 15) == 390
    assert candidate(nums = [1],k = 100) == 5050
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 1035
    assert candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],k = 5) == 710
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 20) == 290
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 100) == 6950
    assert candidate(nums = [1, 3, 5, 7, 9],k = 7) == 84
    assert candidate(nums = [25, 50, 75, 100],k = 15) == 1605
    assert candidate(nums = [1, 3, 5, 7, 9],k = 7) == 84
    assert candidate(nums = [50, 40, 30, 20, 10],k = 30) == 1935
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 405
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 3725
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 16) == 760
    assert candidate(nums = [99, 98, 97, 96, 95],k = 10) == 1035
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 50) == 1575
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 75) == 10275
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 145
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 1045
    assert candidate(nums = [55, 55, 55, 55, 55, 55, 55, 55, 55, 55],k = 100) == 10450
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 15) == 180
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 30) == 1035
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 91
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 6225
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 210
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 12) == 306
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 100) == 14950
    assert candidate(nums = [50],k = 100) == 9950
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],k = 50) == 6125
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 50) == 6475
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 20) == 590
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 100) == 5750
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 245
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 40) == 1980
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 50) == 6225
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 75) == 6525
    assert candidate(nums = [99, 98, 97, 96, 95],k = 20) == 2170
    assert candidate(nums = [1, 3, 5, 7, 9, 11],k = 10) == 155
    assert candidate(nums = [50, 51, 52, 53, 54],k = 8) == 460
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 25) == 550
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 210
    assert candidate(nums = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 11) == 1155
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 75) == 4200
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 1275
    assert candidate(nums = [1, 3, 5, 7, 9],k = 10) == 135
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 100) == 14950
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 2190
    assert candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == 460
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 100) == 19950
    assert candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500],k = 25) == 12800
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 15) == 1605
    assert candidate(nums = [42],k = 100) == 9150
    assert candidate(nums = [10, 20, 30, 40, 50, 60],k = 10) == 645
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 15) == 1590
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 50) == 1325
    assert candidate(nums = [1, 2, 3, 4, 5],k = 100) == 5450
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],k = 30) == 1545
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 100) == 14850
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 50) == 2225
    assert candidate(nums = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30],k = 9) == 306
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 100
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 25) == 325
    assert candidate(nums = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 75) == 10275
    assert candidate(nums = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99],k = 100) == 14850
    assert candidate(nums = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],k = 75) == 10200
    assert candidate(nums = [50, 40, 30, 20, 10],k = 15) == 855
    assert candidate(nums = [2, 4, 6, 8, 10, 12],k = 15) == 285
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 1725
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 590
    assert candidate(nums = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],k = 100) == 7450
    assert candidate(nums = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],k = 20) == 2190
    assert candidate(nums = [1, 3, 5, 7, 9],k = 5) == 55
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50],k = 7) == 371
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 25) == 2800
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 30) == 3405
    assert candidate(nums = [99, 98, 97, 96, 95],k = 25) == 2775
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 15) == 1605
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 25) == 2800
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 145
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 50) == 3725


