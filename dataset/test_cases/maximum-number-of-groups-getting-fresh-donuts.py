def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 2,groups = [2, 2, 2, 2, 2, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 2,groups = [2, 2, 2, 2, 2, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [4, 8, 12, 16, 20]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [4, 8, 12, 16, 20]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [1, 2, 3, 4, 5, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [1, 2, 3, 4, 5, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [1, 3, 2, 5, 2, 2, 1, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [1, 3, 2, 5, 2, 2, 1, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [3, 6, 9, 12, 15]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [3, 6, 9, 12, 15]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [5, 10, 15, 20, 25]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [5, 10, 15, 20, 25]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 1,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 1,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [1, 2, 3, 4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [1, 2, 3, 4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [5, 5, 5, 5, 5, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [5, 5, 5, 5, 5, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 2,groups = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 2,groups = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [4, 7, 9, 12, 14, 15, 18, 20, 22, 23, 25, 26, 27, 29, 31, 32]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [4, 7, 9, 12, 14, 15, 18, 20, 22, 23, 25, 26, 27, 29, 31, 32]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 2,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 2,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 276, 288, 300, 312, 324, 336, 348, 360]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 276, 288, 300, 312, 324, 336, 348, 360]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [8, 9, 10, 11, 12, 13, 14, 15]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [8, 9, 10, 11, 12, 13, 14, 15]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234, 243, 252, 261, 270]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234, 243, 252, 261, 270]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [5, 8, 10, 11, 13, 16, 17, 19, 21, 22, 25, 28, 30]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [5, 8, 10, 11, 13, 16, 17, 19, 21, 22, 25, 28, 30]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 2,groups = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 2,groups = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [2, 3, 7, 8, 10, 12, 15, 17]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [2, 3, 7, 8, 10, 12, 15, 17]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [9, 15, 2, 7, 8, 11, 13, 4, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [9, 15, 2, 7, 8, 11, 13, 4, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [2, 4, 6, 8, 10, 12, 14, 16]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [2, 4, 6, 8, 10, 12, 14, 16]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [8, 7, 6, 5, 4, 3, 2, 1, 9, 18, 27, 36, 45, 54, 63, 72, 81]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [8, 7, 6, 5, 4, 3, 2, 1, 9, 18, 27, 36, 45, 54, 63, 72, 81]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [13, 19, 22, 29, 31, 37, 41, 43, 47, 53, 59]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [13, 19, 22, 29, 31, 37, 41, 43, 47, 53, 59]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [15, 22, 33, 44, 55, 66, 77, 88, 99]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [15, 22, 33, 44, 55, 66, 77, 88, 99]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [2, 3, 4, 1, 5, 6, 7, 8, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [2, 3, 4, 1, 5, 6, 7, 8, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [12, 24, 36, 48, 60, 72, 84, 96, 108]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [12, 24, 36, 48, 60, 72, 84, 96, 108]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [9, 13, 17, 21, 25, 29, 33, 37, 41, 45]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [9, 13, 17, 21, 25, 29, 33, 37, 41, 45]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 4,groups = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 4,groups = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [8, 17, 26, 35, 44, 53, 62, 71, 80, 89, 98, 107, 116, 125, 134, 143, 152]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [8, 17, 26, 35, 44, 53, 62, 71, 80, 89, 98, 107, 116, 125, 134, 143, 152]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(batchSize = 5,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batchSize = 5,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49]) == 7
    assert candidate(batchSize = 2,groups = [2, 2, 2, 2, 2, 2]) == 6
    assert candidate(batchSize = 7,groups = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 12
    assert candidate(batchSize = 4,groups = [4, 8, 12, 16, 20]) == 5
    assert candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
    assert candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42]) == 6
    assert candidate(batchSize = 3,groups = [1, 2, 3, 4, 5, 6]) == 4
    assert candidate(batchSize = 4,groups = [1, 3, 2, 5, 2, 2, 1, 6]) == 4
    assert candidate(batchSize = 3,groups = [3, 6, 9, 12, 15]) == 5
    assert candidate(batchSize = 5,groups = [5, 10, 15, 20, 25]) == 5
    assert candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72]) == 9
    assert candidate(batchSize = 1,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(batchSize = 5,groups = [1, 2, 3, 4, 5]) == 3
    assert candidate(batchSize = 5,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81]) == 9
    assert candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 10
    assert candidate(batchSize = 8,groups = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 15
    assert candidate(batchSize = 5,groups = [5, 5, 5, 5, 5, 5]) == 6
    assert candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56]) == 8
    assert candidate(batchSize = 9,groups = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(batchSize = 9,groups = [9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9
    assert candidate(batchSize = 2,groups = [1, 2, 3, 4, 5]) == 4
    assert candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54]) == 9
    assert candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64]) == 8
    assert candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 30
    assert candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 11
    assert candidate(batchSize = 8,groups = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 8
    assert candidate(batchSize = 3,groups = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000]) == 3
    assert candidate(batchSize = 7,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 11
    assert candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == 10
    assert candidate(batchSize = 5,groups = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 30
    assert candidate(batchSize = 4,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 19
    assert candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == 10
    assert candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147]) == 21
    assert candidate(batchSize = 8,groups = [4, 7, 9, 12, 14, 15, 18, 20, 22, 23, 25, 26, 27, 29, 31, 32]) == 8
    assert candidate(batchSize = 2,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(batchSize = 5,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(batchSize = 7,groups = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182]) == 13
    assert candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126]) == 14
    assert candidate(batchSize = 6,groups = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 276, 288, 300, 312, 324, 336, 348, 360]) == 30
    assert candidate(batchSize = 5,groups = [8, 9, 10, 11, 12, 13, 14, 15]) == 5
    assert candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40]) == 8
    assert candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234, 243, 252, 261, 270]) == 30
    assert candidate(batchSize = 5,groups = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 6
    assert candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]) == 15
    assert candidate(batchSize = 4,groups = [5, 8, 10, 11, 13, 16, 17, 19, 21, 22, 25, 28, 30]) == 8
    assert candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 10
    assert candidate(batchSize = 2,groups = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 21
    assert candidate(batchSize = 5,groups = [2, 3, 7, 8, 10, 12, 15, 17]) == 5
    assert candidate(batchSize = 3,groups = [9, 15, 2, 7, 8, 11, 13, 4, 1]) == 6
    assert candidate(batchSize = 4,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 13
    assert candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 20
    assert candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 7
    assert candidate(batchSize = 5,groups = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 9
    assert candidate(batchSize = 8,groups = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 3
    assert candidate(batchSize = 9,groups = [1, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112]) == 8
    assert candidate(batchSize = 5,groups = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 6
    assert candidate(batchSize = 5,groups = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10
    assert candidate(batchSize = 7,groups = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92]) == 2
    assert candidate(batchSize = 9,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 20
    assert candidate(batchSize = 5,groups = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 6
    assert candidate(batchSize = 5,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 30
    assert candidate(batchSize = 3,groups = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40]) == 5
    assert candidate(batchSize = 7,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(batchSize = 4,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 8
    assert candidate(batchSize = 8,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119]) == 10
    assert candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(batchSize = 4,groups = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 6
    assert candidate(batchSize = 5,groups = [2, 4, 6, 8, 10, 12, 14, 16]) == 5
    assert candidate(batchSize = 9,groups = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 6
    assert candidate(batchSize = 9,groups = [8, 7, 6, 5, 4, 3, 2, 1, 9, 18, 27, 36, 45, 54, 63, 72, 81]) == 13
    assert candidate(batchSize = 4,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9
    assert candidate(batchSize = 4,groups = [13, 19, 22, 29, 31, 37, 41, 43, 47, 53, 59]) == 6
    assert candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 8
    assert candidate(batchSize = 3,groups = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 10
    assert candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 14
    assert candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104]) == 13
    assert candidate(batchSize = 8,groups = [15, 22, 33, 44, 55, 66, 77, 88, 99]) == 5
    assert candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 12
    assert candidate(batchSize = 6,groups = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 30
    assert candidate(batchSize = 4,groups = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == 10
    assert candidate(batchSize = 6,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]) == 8
    assert candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]) == 15
    assert candidate(batchSize = 5,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9
    assert candidate(batchSize = 6,groups = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72]) == 12
    assert candidate(batchSize = 9,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == 7
    assert candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210]) == 30
    assert candidate(batchSize = 9,groups = [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]) == 7
    assert candidate(batchSize = 5,groups = [2, 3, 4, 1, 5, 6, 7, 8, 9]) == 5
    assert candidate(batchSize = 8,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(batchSize = 3,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(batchSize = 9,groups = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 8
    assert candidate(batchSize = 5,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9
    assert candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 18
    assert candidate(batchSize = 8,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112]) == 9
    assert candidate(batchSize = 6,groups = [12, 24, 36, 48, 60, 72, 84, 96, 108]) == 9
    assert candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]) == 13
    assert candidate(batchSize = 7,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]) == 14
    assert candidate(batchSize = 9,groups = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]) == 2
    assert candidate(batchSize = 8,groups = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240]) == 30
    assert candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
    assert candidate(batchSize = 6,groups = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51]) == 7
    assert candidate(batchSize = 6,groups = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 6
    assert candidate(batchSize = 3,groups = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 7
    assert candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 30
    assert candidate(batchSize = 4,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 10
    assert candidate(batchSize = 3,groups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 16
    assert candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 17
    assert candidate(batchSize = 6,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 7
    assert candidate(batchSize = 7,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9
    assert candidate(batchSize = 7,groups = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]) == 10
    assert candidate(batchSize = 3,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 20
    assert candidate(batchSize = 7,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 9
    assert candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 15
    assert candidate(batchSize = 3,groups = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 8
    assert candidate(batchSize = 4,groups = [9, 13, 17, 21, 25, 29, 33, 37, 41, 45]) == 3
    assert candidate(batchSize = 4,groups = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 8
    assert candidate(batchSize = 7,groups = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112]) == 16
    assert candidate(batchSize = 9,groups = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180]) == 20
    assert candidate(batchSize = 9,groups = [8, 17, 26, 35, 44, 53, 62, 71, 80, 89, 98, 107, 116, 125, 134, 143, 152]) == 2
    assert candidate(batchSize = 9,groups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 11
    assert candidate(batchSize = 5,groups = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 20
    assert candidate(batchSize = 3,groups = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 12
    assert candidate(batchSize = 5,groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10


