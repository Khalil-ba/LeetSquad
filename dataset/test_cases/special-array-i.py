def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 7, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 7, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 30, 40, 50, 60]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 30, 40, 50, 60]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 8, 3, 8, 3, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 8, 3, 8, 3, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 3, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 3, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 10, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 10, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 1, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 1, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 50, 51, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 50, 51, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 7, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 7, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 50, 51]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 50, 51]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98, 99]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98, 99]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 100, 99]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 100, 99]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 2, 9, 4, 11, 6, 13, 8, 15, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 2, 9, 4, 11, 6, 13, 8, 15, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [89, 90, 89, 90, 89, 90, 89, 90, 89, 90]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [89, 90, 89, 90, 89, 90, 89, 90, 89, 90]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 25, 50, 25, 50, 25, 50, 25]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 25, 50, 25, 50, 25, 50, 25]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 2, 97, 4, 95, 6, 93, 8, 91, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 2, 97, 4, 95, 6, 93, 8, 91, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 20, 3, 40, 5, 60, 7, 80, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 20, 3, 40, 5, 60, 7, 80, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 51, 52, 53, 54, 55]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 51, 52, 53, 54, 55]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 3, 8, 5, 12, 7, 16, 9, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 3, 8, 5, 12, 7, 16, 9, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 24, 35, 46, 57, 68, 79, 80, 91, 102]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 24, 35, 46, 57, 68, 79, 80, 91, 102]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 100, 101, 102, 103, 104, 105]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 100, 101, 102, 103, 104, 105]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 46, 47, 48, 49, 50, 51]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 46, 47, 48, 49, 50, 51]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [61, 62, 63, 64, 65, 66, 67, 68, 69]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [61, 62, 63, 64, 65, 66, 67, 68, 69]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [83, 84, 85, 86, 87, 88, 89, 90, 91, 92]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [83, 84, 85, 86, 87, 88, 89, 90, 91, 92]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 27, 28, 29, 30]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 27, 28, 29, 30]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 100, 99, 98, 97, 96, 95, 94, 93, 92]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 100, 99, 98, 97, 96, 95, 94, 93, 92]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 100, 99, 100, 99]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 100, 99, 100, 99]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 22, 25, 24, 27, 26, 29, 28, 31, 30]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 22, 25, 24, 27, 26, 29, 28, 31, 30]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 22, 33, 24, 35, 26, 37, 28, 39, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 22, 33, 24, 35, 26, 37, 28, 39, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [47, 48, 49, 50, 51, 52, 53, 54, 55, 56]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [47, 48, 49, 50, 51, 52, 53, 54, 55, 56]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [97, 98, 95, 96, 93, 94]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [97, 98, 95, 96, 93, 94]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 100, 99, 100, 99, 100, 99, 100, 99, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 100, 99, 100, 99, 100, 99, 100, 99, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 50, 49, 50, 49, 50, 49, 50, 49, 50]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 50, 49, 50, 49, 50, 49, 50, 49, 50]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 2, 99, 2, 99, 2, 99, 2, 99, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 2, 99, 2, 99, 2, 99, 2, 99, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [51, 52, 51, 52, 51, 52, 51, 52, 51, 52, 51, 52]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [51, 52, 51, 52, 51, 52, 51, 52, 51, 52, 51, 52]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 3, 12, 7, 14, 9, 16, 11, 18]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 3, 12, 7, 14, 9, 16, 11, 18]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 7, 8, 7, 8, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 7, 8, 7, 8, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [97, 98, 99, 100, 1, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [97, 98, 99, 100, 1, 2, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [82, 81, 82, 83, 82, 81, 82, 83, 82, 81]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [82, 81, 82, 83, 82, 81, 82, 83, 82, 81]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51]) == True: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [100, 99, 100]) == True
    assert candidate(nums = [5, 2, 7, 8]) == True
    assert candidate(nums = [20, 30, 40, 50, 60]) == False
    assert candidate(nums = [3, 8, 3, 8, 3, 8]) == True
    assert candidate(nums = [2, 3, 4, 5]) == True
    assert candidate(nums = [10, 11, 12, 13]) == True
    assert candidate(nums = [3, 6, 3, 6]) == True
    assert candidate(nums = [2, 4, 6, 8, 10]) == False
    assert candidate(nums = [1, 3, 5, 7, 9]) == False
    assert candidate(nums = [1]) == True
    assert candidate(nums = [2, 3]) == True
    assert candidate(nums = [100]) == True
    assert candidate(nums = [10, 11, 10, 11]) == True
    assert candidate(nums = [1, 2, 3, 4, 5]) == True
    assert candidate(nums = [4, 3, 1, 6]) == False
    assert candidate(nums = [50, 51, 50, 51, 50]) == True
    assert candidate(nums = [15, 14, 13, 12, 11]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == True
    assert candidate(nums = [2, 1, 4]) == True
    assert candidate(nums = [20, 19, 18, 17, 16]) == True
    assert candidate(nums = [5, 8, 7, 2]) == True
    assert candidate(nums = [15]) == True
    assert candidate(nums = [50, 51, 50, 51]) == True
    assert candidate(nums = [2, 3, 2, 3]) == True
    assert candidate(nums = [1, 2]) == True
    assert candidate(nums = [1, 3, 5, 7]) == False
    assert candidate(nums = [98, 99]) == True
    assert candidate(nums = [100, 99, 100, 99]) == True
    assert candidate(nums = [5]) == True
    assert candidate(nums = [2, 4, 6, 8]) == False
    assert candidate(nums = [7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2]) == True
    assert candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == True
    assert candidate(nums = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]) == True
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == True
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [7, 2, 9, 4, 11, 6, 13, 8, 15, 10]) == True
    assert candidate(nums = [60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == True
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == False
    assert candidate(nums = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98]) == True
    assert candidate(nums = [89, 90, 89, 90, 89, 90, 89, 90, 89, 90]) == True
    assert candidate(nums = [25, 50, 25, 50, 25, 50, 25, 50, 25]) == True
    assert candidate(nums = [99, 2, 97, 4, 95, 6, 93, 8, 91, 10]) == True
    assert candidate(nums = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]) == True
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6]) == False
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == True
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]) == True
    assert candidate(nums = [10, 1, 20, 3, 40, 5, 60, 7, 80, 9]) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == False
    assert candidate(nums = [10, 20, 30, 40, 50, 51, 52, 53, 54, 55]) == False
    assert candidate(nums = [1, 4, 3, 8, 5, 12, 7, 16, 9, 20]) == True
    assert candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]) == False
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == True
    assert candidate(nums = [13, 24, 35, 46, 57, 68, 79, 80, 91, 102]) == True
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]) == True
    assert candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == False
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == False
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False
    assert candidate(nums = [99, 100, 101, 102, 103, 104, 105]) == True
    assert candidate(nums = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106]) == True
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == True
    assert candidate(nums = [45, 46, 47, 48, 49, 50, 51]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == False
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == False
    assert candidate(nums = [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == True
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == True
    assert candidate(nums = [61, 62, 63, 64, 65, 66, 67, 68, 69]) == True
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11]) == True
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16]) == False
    assert candidate(nums = [83, 84, 85, 86, 87, 88, 89, 90, 91, 92]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010]) == True
    assert candidate(nums = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]) == True
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == True
    assert candidate(nums = [25, 26, 27, 28, 29, 30]) == True
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == True
    assert candidate(nums = [101, 100, 99, 98, 97, 96, 95, 94, 93, 92]) == True
    assert candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == True
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == False
    assert candidate(nums = [100, 99, 100, 99, 100, 99]) == True
    assert candidate(nums = [23, 22, 25, 24, 27, 26, 29, 28, 31, 30]) == True
    assert candidate(nums = [31, 22, 33, 24, 35, 26, 37, 28, 39, 20]) == True
    assert candidate(nums = [100, 99, 98, 97, 96]) == True
    assert candidate(nums = [47, 48, 49, 50, 51, 52, 53, 54, 55, 56]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [5, 4, 3, 2, 1]) == True
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True
    assert candidate(nums = [97, 98, 95, 96, 93, 94]) == True
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == False
    assert candidate(nums = [99, 100, 99, 100, 99, 100, 99, 100, 99, 100]) == True
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]) == True
    assert candidate(nums = [100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99, 100, 99]) == True
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14]) == False
    assert candidate(nums = [49, 50, 49, 50, 49, 50, 49, 50, 49, 50]) == True
    assert candidate(nums = [42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30]) == True
    assert candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == True
    assert candidate(nums = [99, 2, 99, 2, 99, 2, 99, 2, 99, 2]) == True
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13]) == False
    assert candidate(nums = [97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == True
    assert candidate(nums = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == True
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
    assert candidate(nums = [51, 52, 51, 52, 51, 52, 51, 52, 51, 52, 51, 52]) == True
    assert candidate(nums = [5, 8, 3, 12, 7, 14, 9, 16, 11, 18]) == True
    assert candidate(nums = [7, 8, 7, 8, 7, 8, 7]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == False
    assert candidate(nums = [97, 98, 99, 100, 1, 2, 3, 4]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == True
    assert candidate(nums = [82, 81, 82, 83, 82, 81, 82, 83, 82, 81]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == False
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == True
    assert candidate(nums = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == True
    assert candidate(nums = [50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51, 50, 51]) == True
    assert candidate(nums = [5, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True


