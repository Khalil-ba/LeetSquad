def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13],diff = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13],diff = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30],diff = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30],diff = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],diff = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],diff = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 6, 7, 8, 9],diff = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 6, 7, 8, 9],diff = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],diff = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],diff = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 6, 9, 12],diff = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 6, 9, 12],diff = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 4, 6, 7, 10],diff = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 4, 6, 7, 10],diff = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],diff = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],diff = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],diff = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],diff = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10],diff = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10],diff = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],diff = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],diff = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 8, 11, 14, 17, 20],diff = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 8, 11, 14, 17, 20],diff = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],diff = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],diff = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35],diff = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35],diff = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],diff = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],diff = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],diff = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],diff = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98, 106, 114, 122],diff = 8) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98, 106, 114, 122],diff = 8) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],diff = 4) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],diff = 4) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109],diff = 6) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109],diff = 6) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98, 104, 110, 116, 122],diff = 6) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98, 104, 110, 116, 122],diff = 6) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85],diff = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85],diff = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93],diff = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93],diff = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72],diff = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72],diff = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],diff = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],diff = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160],diff = 8) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160],diff = 8) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],diff = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],diff = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 12, 19, 26, 33, 40, 47, 54, 61, 68],diff = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 12, 19, 26, 33, 40, 47, 54, 61, 68],diff = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68],diff = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68],diff = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133],diff = 7) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133],diff = 7) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113, 120, 127, 134, 141, 148, 155, 162, 169, 176, 183, 190, 197],diff = 7) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113, 120, 127, 134, 141, 148, 155, 162, 169, 176, 183, 190, 197],diff = 7) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],diff = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],diff = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80],diff = 4) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80],diff = 4) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 14, 19, 24, 29, 34, 39, 44, 49],diff = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 14, 19, 24, 29, 34, 39, 44, 49],diff = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72],diff = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72],diff = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 6, 8, 10, 14, 18, 20, 24, 28, 32, 34, 38, 40],diff = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 6, 8, 10, 14, 18, 20, 24, 28, 32, 34, 38, 40],diff = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191],diff = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191],diff = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115],diff = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115],diff = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99],diff = 7) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99],diff = 7) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 9, 11, 15, 18, 21, 24, 27, 30],diff = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 9, 11, 15, 18, 21, 24, 27, 30],diff = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198],diff = 11) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198],diff = 11) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147, 153, 159, 165, 171, 177, 183, 189, 195],diff = 6) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147, 153, 159, 165, 171, 177, 183, 189, 195],diff = 6) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93],diff = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93],diff = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38],diff = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38],diff = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99, 107, 115, 123, 131, 139, 147, 155, 163, 171, 179],diff = 8) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99, 107, 115, 123, 131, 139, 147, 155, 163, 171, 179],diff = 8) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62],diff = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62],diff = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123],diff = 6) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123],diff = 6) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111],diff = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111],diff = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40],diff = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40],diff = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95, 101, 107, 113, 119, 125, 131, 137, 143, 149, 155, 161, 167, 173, 179, 185, 191, 197],diff = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95, 101, 107, 113, 119, 125, 131, 137, 143, 149, 155, 161, 167, 173, 179, 185, 191, 197],diff = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45],diff = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45],diff = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51],diff = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51],diff = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39],diff = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39],diff = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],diff = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],diff = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97, 102],diff = 5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97, 102],diff = 5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],diff = 1) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],diff = 1) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41],diff = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41],diff = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71],diff = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71],diff = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97],diff = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97],diff = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97],diff = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97],diff = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98],diff = 4) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98],diff = 4) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],diff = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],diff = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98],diff = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98],diff = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 5, 11, 16, 22, 27, 33, 38, 44, 49],diff = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 5, 11, 16, 22, 27, 33, 38, 44, 49],diff = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 7, 12, 15, 19, 24, 27, 31, 36, 39, 43, 48, 51, 55, 60, 63, 67, 72],diff = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 7, 12, 15, 19, 24, 27, 31, 36, 39, 43, 48, 51, 55, 60, 63, 67, 72],diff = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59],diff = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59],diff = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 12, 19, 26, 33, 40, 47, 54, 61, 68, 75, 82, 89],diff = 7) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 12, 19, 26, 33, 40, 47, 54, 61, 68, 75, 82, 89],diff = 7) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48],diff = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48],diff = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 20, 35, 50, 65, 80, 95, 110, 125, 140, 155, 170, 185],diff = 15) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 20, 35, 50, 65, 80, 95, 110, 125, 140, 155, 170, 185],diff = 15) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],diff = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],diff = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],diff = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],diff = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93, 102, 111, 120, 129, 138, 147, 156, 165, 174],diff = 9) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93, 102, 111, 120, 129, 138, 147, 156, 165, 174],diff = 9) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25],diff = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25],diff = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81],diff = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81],diff = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95],diff = 6) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95],diff = 6) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],diff = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],diff = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],diff = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],diff = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20],diff = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20],diff = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 8, 11, 14, 17, 20, 23, 26],diff = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 8, 11, 14, 17, 20, 23, 26],diff = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],diff = 1) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],diff = 1) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40],diff = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40],diff = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43],diff = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43],diff = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],diff = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],diff = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61],diff = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61],diff = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 48, 50, 51, 53, 54, 56, 57, 59, 60, 62, 63, 65, 66, 68, 69, 71, 72, 74, 75, 77, 78, 80, 81, 83, 84, 86, 87, 89, 90, 92, 93, 95, 96, 98, 99, 101, 102, 104, 105, 107, 108, 110, 111, 113, 114, 116, 117, 119, 120, 122, 123, 125, 126, 128, 129, 131, 132, 134, 135, 137, 138, 140, 141, 143, 144, 146, 147, 149, 150, 152, 153, 155, 156, 158, 159, 161, 162, 164, 165, 167, 168, 170, 171, 173, 174, 176, 177, 179, 180, 182, 183, 185, 186, 188, 189, 191, 192, 194, 195, 197, 198],diff = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 48, 50, 51, 53, 54, 56, 57, 59, 60, 62, 63, 65, 66, 68, 69, 71, 72, 74, 75, 77, 78, 80, 81, 83, 84, 86, 87, 89, 90, 92, 93, 95, 96, 98, 99, 101, 102, 104, 105, 107, 108, 110, 111, 113, 114, 116, 117, 119, 120, 122, 123, 125, 126, 128, 129, 131, 132, 134, 135, 137, 138, 140, 141, 143, 144, 146, 147, 149, 150, 152, 153, 155, 156, 158, 159, 161, 162, 164, 165, 167, 168, 170, 171, 173, 174, 176, 177, 179, 180, 182, 183, 185, 186, 188, 189, 191, 192, 194, 195, 197, 198],diff = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22],diff = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22],diff = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111, 116, 121, 126, 131, 136, 141, 146, 151, 156, 161, 166, 171, 176, 181, 186, 191, 196, 200],diff = 5) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111, 116, 121, 126, 131, 136, 141, 146, 151, 156, 161, 166, 171, 176, 181, 186, 191, 196, 200],diff = 5) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61],diff = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61],diff = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93, 100],diff = 7) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93, 100],diff = 7) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],diff = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],diff = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],diff = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],diff = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101],diff = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101],diff = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97],diff = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97],diff = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100],diff = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100],diff = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67],diff = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67],diff = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73, 78, 83, 88, 93, 98],diff = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73, 78, 83, 88, 93, 98],diff = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109, 118, 127],diff = 9) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109, 118, 127],diff = 9) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44],diff = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44],diff = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98, 106, 114],diff = 8) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98, 106, 114],diff = 8) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97, 107, 117, 127, 137, 147, 157, 167, 177, 187, 197],diff = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97, 107, 117, 127, 137, 147, 157, 167, 177, 187, 197],diff = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53],diff = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53],diff = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],diff = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],diff = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],diff = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],diff = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],diff = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],diff = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73],diff = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73],diff = 5) == 13: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13],diff = 2) == 5
    assert candidate(nums = [5, 10, 15, 20, 25, 30],diff = 5) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],diff = 4) == 6
    assert candidate(nums = [4, 5, 6, 7, 8, 9],diff = 2) == 2
    assert candidate(nums = [1, 3, 5, 7, 9],diff = 2) == 3
    assert candidate(nums = [0, 3, 6, 9, 12],diff = 3) == 3
    assert candidate(nums = [0, 1, 4, 6, 7, 10],diff = 3) == 2
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41],diff = 4) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],diff = 1) == 8
    assert candidate(nums = [0, 2, 4, 6, 8, 10],diff = 2) == 4
    assert candidate(nums = [10, 20, 30, 40, 50],diff = 10) == 3
    assert candidate(nums = [2, 5, 8, 11, 14, 17, 20],diff = 3) == 5
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],diff = 3) == 8
    assert candidate(nums = [10, 15, 20, 25, 30, 35],diff = 5) == 4
    assert candidate(nums = [5, 10, 15, 20, 25],diff = 5) == 3
    assert candidate(nums = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],diff = 3) == 13
    assert candidate(nums = [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98, 106, 114, 122],diff = 8) == 13
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],diff = 4) == 23
    assert candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109],diff = 6) == 17
    assert candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98, 104, 110, 116, 122],diff = 6) == 19
    assert candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85],diff = 6) == 13
    assert candidate(nums = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93],diff = 9) == 9
    assert candidate(nums = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72],diff = 6) == 11
    assert candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],diff = 5) == 9
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160],diff = 8) == 18
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],diff = 5) == 18
    assert candidate(nums = [5, 12, 19, 26, 33, 40, 47, 54, 61, 68],diff = 7) == 8
    assert candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68],diff = 6) == 10
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133],diff = 7) == 17
    assert candidate(nums = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113, 120, 127, 134, 141, 148, 155, 162, 169, 176, 183, 190, 197],diff = 7) == 27
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],diff = 10) == 14
    assert candidate(nums = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80],diff = 4) == 19
    assert candidate(nums = [1, 5, 9, 14, 19, 24, 29, 34, 39, 44, 49],diff = 4) == 1
    assert candidate(nums = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72],diff = 7) == 9
    assert candidate(nums = [0, 2, 6, 8, 10, 14, 18, 20, 24, 28, 32, 34, 38, 40],diff = 2) == 1
    assert candidate(nums = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191],diff = 10) == 18
    assert candidate(nums = [3, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115],diff = 4) == 0
    assert candidate(nums = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99],diff = 7) == 13
    assert candidate(nums = [1, 6, 9, 11, 15, 18, 21, 24, 27, 30],diff = 3) == 4
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198],diff = 11) == 16
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123, 129, 135, 141, 147, 153, 159, 165, 171, 177, 183, 189, 195],diff = 6) == 31
    assert candidate(nums = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93],diff = 7) == 12
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38],diff = 4) == 8
    assert candidate(nums = [3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99, 107, 115, 123, 131, 139, 147, 155, 163, 171, 179],diff = 8) == 21
    assert candidate(nums = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62],diff = 5) == 11
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123],diff = 6) == 19
    assert candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111],diff = 5) == 21
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40],diff = 3) == 12
    assert candidate(nums = [0, 5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95, 101, 107, 113, 119, 125, 131, 137, 143, 149, 155, 161, 167, 173, 179, 185, 191, 197],diff = 7) == 0
    assert candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45],diff = 5) == 8
    assert candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51],diff = 5) == 9
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39],diff = 3) == 11
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],diff = 3) == 8
    assert candidate(nums = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97, 102],diff = 5) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],diff = 1) == 18
    assert candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41],diff = 5) == 7
    assert candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71],diff = 6) == 10
    assert candidate(nums = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97],diff = 10) == 8
    assert candidate(nums = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97],diff = 5) == 18
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98],diff = 4) == 23
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],diff = 10) == 8
    assert candidate(nums = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98],diff = 6) == 15
    assert candidate(nums = [0, 5, 11, 16, 22, 27, 33, 38, 44, 49],diff = 7) == 0
    assert candidate(nums = [0, 3, 7, 12, 15, 19, 24, 27, 31, 36, 39, 43, 48, 51, 55, 60, 63, 67, 72],diff = 3) == 0
    assert candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59],diff = 6) == 8
    assert candidate(nums = [5, 12, 19, 26, 33, 40, 47, 54, 61, 68, 75, 82, 89],diff = 7) == 11
    assert candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48],diff = 5) == 8
    assert candidate(nums = [5, 20, 35, 50, 65, 80, 95, 110, 125, 140, 155, 170, 185],diff = 15) == 11
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],diff = 3) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],diff = 10) == 18
    assert candidate(nums = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93, 102, 111, 120, 129, 138, 147, 156, 165, 174],diff = 9) == 18
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25],diff = 3) == 7
    assert candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81],diff = 5) == 15
    assert candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95],diff = 6) == 14
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],diff = 6) == 15
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],diff = 2) == 9
    assert candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20],diff = 1) == 0
    assert candidate(nums = [1, 5, 8, 11, 14, 17, 20, 23, 26],diff = 3) == 6
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],diff = 1) == 19
    assert candidate(nums = [0, 5, 10, 15, 20, 25, 30, 35, 40],diff = 5) == 7
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43],diff = 4) == 9
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],diff = 10) == 18
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61],diff = 3) == 19
    assert candidate(nums = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 48, 50, 51, 53, 54, 56, 57, 59, 60, 62, 63, 65, 66, 68, 69, 71, 72, 74, 75, 77, 78, 80, 81, 83, 84, 86, 87, 89, 90, 92, 93, 95, 96, 98, 99, 101, 102, 104, 105, 107, 108, 110, 111, 113, 114, 116, 117, 119, 120, 122, 123, 125, 126, 128, 129, 131, 132, 134, 135, 137, 138, 140, 141, 143, 144, 146, 147, 149, 150, 152, 153, 155, 156, 158, 159, 161, 162, 164, 165, 167, 168, 170, 171, 173, 174, 176, 177, 179, 180, 182, 183, 185, 186, 188, 189, 191, 192, 194, 195, 197, 198],diff = 2) == 1
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22],diff = 3) == 6
    assert candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111, 116, 121, 126, 131, 136, 141, 146, 151, 156, 161, 166, 171, 176, 181, 186, 191, 196, 200],diff = 5) == 38
    assert candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61],diff = 5) == 11
    assert candidate(nums = [2, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93, 100],diff = 7) == 13
    assert candidate(nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],diff = 2) == 2
    assert candidate(nums = [3, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],diff = 3) == 8
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101],diff = 4) == 24
    assert candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97],diff = 6) == 15
    assert candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100],diff = 15) == 0
    assert candidate(nums = [7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67],diff = 5) == 11
    assert candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73, 78, 83, 88, 93, 98],diff = 5) == 18
    assert candidate(nums = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109, 118, 127],diff = 9) == 13
    assert candidate(nums = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44],diff = 4) == 10
    assert candidate(nums = [2, 10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98, 106, 114],diff = 8) == 13
    assert candidate(nums = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97, 107, 117, 127, 137, 147, 157, 167, 177, 187, 197],diff = 10) == 18
    assert candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53],diff = 5) == 9
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],diff = 4) == 11
    assert candidate(nums = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],diff = 6) == 15
    assert candidate(nums = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],diff = 9) == 10
    assert candidate(nums = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73],diff = 5) == 13


