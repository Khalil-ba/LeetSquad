def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(values = [10, 1, 1, 10]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 1, 10]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 328
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 328: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 1, 2, 4, 5, 6]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 1, 2, 4, 5, 6]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 1, 20, 2, 30, 3, 40, 4]) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 20, 2, 30, 3, 40, 4]) == 510: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 5, 11, 7, 10, 2, 12, 8]) == 342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 5, 11, 7, 10, 2, 12, 8]) == 342: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 3, 1, 4, 1, 5]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 3, 1, 4, 1, 5]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 328000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 328000: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 5, 10, 7, 2]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 5, 10, 7, 2]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(values = [6, 6, 6, 6, 6, 6]) == 864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [6, 6, 6, 6, 6, 6]) == 864: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 2, 1, 4, 3]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 2, 1, 4, 3]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50]) == 38000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50]) == 38000: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 875: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 5, 5, 5, 5, 5, 5]) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 5, 5, 5, 5, 5, 5]) == 625: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 864: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 5, 5, 5]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 5, 5, 5]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 3, 3, 3, 3, 3]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 3, 3, 3, 3, 3]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(values = [8, 3, 5, 1]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [8, 3, 5, 1]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 7, 4, 5]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 7, 4, 5]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 328
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 328: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 5, 2, 1, 4, 3]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 5, 2, 1, 4, 3]) == 102: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 50, 24, 30]) == 9600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 50, 24, 30]) == 9600: {e}')
    
    total += 1
    try:
        result = candidate(values = [6, 10, 5, 2, 1, 4, 3]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [6, 10, 5, 2, 1, 4, 3]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 8, 7, 3, 2, 9, 4]) == 346
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 8, 7, 3, 2, 9, 4]) == 346: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 3, 2, 6, 1, 4, 7]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 3, 2, 6, 1, 4, 7]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 1, 3, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 1, 3, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(values = [8, 6, 7, 5, 3, 0, 9, 2, 4, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [8, 6, 7, 5, 3, 0, 9, 2, 4, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2658
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2658: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 41736
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 41736: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 5, 1, 9, 3, 7, 2, 6]) == 184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 5, 1, 9, 3, 7, 2, 6]) == 184: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 328000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 328000: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(values = [15, 25, 35, 45, 55, 65, 75]) == 200625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [15, 25, 35, 45, 55, 65, 75]) == 200625: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 10, 3, 8, 4, 1, 9, 7]) == 183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 10, 3, 8, 4, 1, 9, 7]) == 183: {e}')
    
    total += 1
    try:
        result = candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 323398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 323398: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 70000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 70000: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 3, 4, 5, 6, 7, 8, 9]) == 464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 3, 4, 5, 6, 7, 8, 9]) == 464: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 328000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 328000000: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 486
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 486: {e}')
    
    total += 1
    try:
        result = candidate(values = [30, 20, 10, 5, 15, 25, 40, 35]) == 23125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [30, 20, 10, 5, 15, 25, 40, 35]) == 23125: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 328
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 328: {e}')
    
    total += 1
    try:
        result = candidate(values = [30, 20, 10, 40, 50, 60, 70]) == 119000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [30, 20, 10, 40, 50, 60, 70]) == 119000: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(values = [50, 40, 30, 20, 10, 90, 80, 70, 60, 50, 40, 30, 20, 10, 90, 80, 70, 60, 50, 40, 30]) == 527000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [50, 40, 30, 20, 10, 90, 80, 70, 60, 50, 40, 30, 20, 10, 90, 80, 70, 60, 50, 40, 30]) == 527000: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]) == 368064
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]) == 368064: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50, 60, 70]) == 110000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50, 60, 70]) == 110000: {e}')
    
    total += 1
    try:
        result = candidate(values = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]) == 963750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]) == 963750: {e}')
    
    total += 1
    try:
        result = candidate(values = [8, 3, 7, 1, 2, 9, 4]) == 131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [8, 3, 7, 1, 2, 9, 4]) == 131: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 1, 100, 1, 100, 1, 100]) == 10301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 1, 100, 1, 100, 1, 100]) == 10301: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2658000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2658000: {e}')
    
    total += 1
    try:
        result = candidate(values = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110]) == 459000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110]) == 459000: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 570: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 29750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 29750: {e}')
    
    total += 1
    try:
        result = candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54]) == 14469840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54]) == 14469840: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 238: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 328000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 328000: {e}')
    
    total += 1
    try:
        result = candidate(values = [12, 21, 34, 43, 55, 67, 78, 89, 90, 101, 112, 123, 134, 145, 156]) == 1453368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [12, 21, 34, 43, 55, 67, 78, 89, 90, 101, 112, 123, 134, 145, 156]) == 1453368: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 6, 7, 8, 9, 10, 11]) == 1850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 6, 7, 8, 9, 10, 11]) == 1850: {e}')
    
    total += 1
    try:
        result = candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 11702400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 11702400: {e}')
    
    total += 1
    try:
        result = candidate(values = [8, 2, 3, 4, 1, 5, 7]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [8, 2, 3, 4, 1, 5, 7]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 328
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 328: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 100, 2, 99, 3, 98, 4, 97, 5]) == 2254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 100, 2, 99, 3, 98, 4, 97, 5]) == 2254: {e}')
    
    total += 1
    try:
        result = candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89]) == 7158270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89]) == 7158270: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 2, 1, 4, 6, 5, 9, 7, 8]) == 248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 2, 1, 4, 6, 5, 9, 7, 8]) == 248: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 5634
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 5634: {e}')
    
    total += 1
    try:
        result = candidate(values = [7, 6, 8, 5, 3, 4, 9, 2]) == 386
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [7, 6, 8, 5, 3, 4, 9, 2]) == 386: {e}')
    
    total += 1
    try:
        result = candidate(values = [7, 3, 8, 6, 2, 9, 1, 4, 10, 5]) == 248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [7, 3, 8, 6, 2, 9, 1, 4, 10, 5]) == 248: {e}')
    
    total += 1
    try:
        result = candidate(values = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1118000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1118000: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == 726000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == 726000000: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(values = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10, 11, 12, 13, 14, 15]) == 1088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10, 11, 12, 13, 14, 15]) == 1088: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1128: {e}')
    
    total += 1
    try:
        result = candidate(values = [40, 10, 30, 20, 50, 60, 70, 80, 90]) == 252000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [40, 10, 30, 20, 50, 60, 70, 80, 90]) == 252000: {e}')
    
    total += 1
    try:
        result = candidate(values = [25, 15, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135]) == 1254375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [25, 15, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135]) == 1254375: {e}')
    
    total += 1
    try:
        result = candidate(values = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2, 1, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 66691
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2, 1, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 66691: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(values = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 238: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 101010101000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 101010101000: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 71978
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 71978: {e}')
    
    total += 1
    try:
        result = candidate(values = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1151000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1151000: {e}')
    
    total += 1
    try:
        result = candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1118: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 864: {e}')
    
    total += 1
    try:
        result = candidate(values = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 291840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 291840: {e}')
    
    total += 1
    try:
        result = candidate(values = [7, 8, 9, 10, 11, 12, 13, 14]) == 5194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [7, 8, 9, 10, 11, 12, 13, 14]) == 5194: {e}')
    
    total += 1
    try:
        result = candidate(values = [12, 8, 6, 3, 7, 11, 9, 5, 4]) == 1299
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [12, 8, 6, 3, 7, 11, 9, 5, 4]) == 1299: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 1, 100, 10, 1, 100, 10, 1, 100]) == 3031
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 1, 100, 10, 1, 100, 10, 1, 100]) == 3031: {e}')
    
    total += 1
    try:
        result = candidate(values = [9, 1, 8, 1, 7, 2, 6, 3, 5, 4]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [9, 1, 8, 1, 7, 2, 6, 3, 5, 4]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(values = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6]) == 3836
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6]) == 3836: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 6, 3, 2, 7, 8, 4, 1, 9]) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 6, 3, 2, 7, 8, 4, 1, 9]) == 201: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 32000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 32000000: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 7, 4, 5, 6, 8, 2, 9, 1]) == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 7, 4, 5, 6, 8, 2, 9, 1]) == 181: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 5, 1, 100, 10, 5, 1]) == 1110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 5, 1, 100, 10, 5, 1]) == 1110: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 41788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 41788: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50, 60, 70, 80]) == 166000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50, 60, 70, 80]) == 166000: {e}')
    
    total += 1
    try:
        result = candidate(values = [99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 56498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 56498: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 25, 15, 10, 40, 50]) == 14625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 25, 15, 10, 40, 50]) == 14625: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50]) == 38000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50]) == 38000: {e}')
    
    total += 1
    try:
        result = candidate(values = [3, 5, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [3, 5, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 568: {e}')
    
    total += 1
    try:
        result = candidate(values = [2, 5, 8, 13, 21, 34, 55, 89]) == 15792
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [2, 5, 8, 13, 21, 34, 55, 89]) == 15792: {e}')
    
    total += 1
    try:
        result = candidate(values = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 10503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 10503: {e}')
    
    total += 1
    try:
        result = candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1625: {e}')
    
    total += 1
    try:
        result = candidate(values = [12, 34, 56, 78, 90, 11, 22, 33, 44, 55]) == 208538
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [12, 34, 56, 78, 90, 11, 22, 33, 44, 55]) == 208538: {e}')
    
    total += 1
    try:
        result = candidate(values = [50, 20, 10, 30, 40, 60, 80, 70, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2733000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [50, 20, 10, 30, 40, 60, 80, 70, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2733000: {e}')
    
    total += 1
    try:
        result = candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 238000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 238000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(values = [10, 1, 1, 10]) == 110
    assert candidate(values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 328
    assert candidate(values = [3, 1, 2, 4, 5, 6]) == 76
    assert candidate(values = [10, 1, 20, 2, 30, 3, 40, 4]) == 510
    assert candidate(values = [1, 5, 11, 7, 10, 2, 12, 8]) == 342
    assert candidate(values = [1, 3, 1, 4, 1, 5]) == 13
    assert candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 328000
    assert candidate(values = [3, 5, 10, 7, 2]) == 270
    assert candidate(values = [6, 6, 6, 6, 6, 6]) == 864
    assert candidate(values = [5, 2, 1, 4, 3]) == 37
    assert candidate(values = [10, 20, 30, 40, 50]) == 38000
    assert candidate(values = [1, 1, 1, 1, 1, 1]) == 4
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 875
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 44
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5]) == 625
    assert candidate(values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 864
    assert candidate(values = [5, 5, 5, 5]) == 250
    assert candidate(values = [3, 3, 3, 3, 3, 3]) == 108
    assert candidate(values = [8, 3, 5, 1]) == 39
    assert candidate(values = [3, 7, 4, 5]) == 144
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 328
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(values = [1, 2, 3]) == 6
    assert candidate(values = [10, 5, 2, 1, 4, 3]) == 102
    assert candidate(values = [5, 50, 24, 30]) == 9600
    assert candidate(values = [6, 10, 5, 2, 1, 4, 3]) == 150
    assert candidate(values = [1, 2, 3, 4, 5]) == 38
    assert candidate(values = [5, 8, 7, 3, 2, 9, 4]) == 346
    assert candidate(values = [5, 3, 2, 6, 1, 4, 7]) == 96
    assert candidate(values = [2, 1, 3, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == 77
    assert candidate(values = [8, 6, 7, 5, 3, 0, 9, 2, 4, 1]) == 0
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2658
    assert candidate(values = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 41736
    assert candidate(values = [10, 5, 1, 9, 3, 7, 2, 6]) == 184
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 328000
    assert candidate(values = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6]) == 0
    assert candidate(values = [15, 25, 35, 45, 55, 65, 75]) == 200625
    assert candidate(values = [2, 10, 3, 8, 4, 1, 9, 7]) == 183
    assert candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 323398
    assert candidate(values = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 70000
    assert candidate(values = [2, 3, 4, 5, 6, 7, 8, 9]) == 464
    assert candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 328000000
    assert candidate(values = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 486
    assert candidate(values = [30, 20, 10, 5, 15, 25, 40, 35]) == 23125
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 328
    assert candidate(values = [30, 20, 10, 40, 50, 60, 70]) == 119000
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 48
    assert candidate(values = [50, 40, 30, 20, 10, 90, 80, 70, 60, 50, 40, 30, 20, 10, 90, 80, 70, 60, 50, 40, 30]) == 527000
    assert candidate(values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]) == 368064
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1000
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70]) == 110000
    assert candidate(values = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]) == 963750
    assert candidate(values = [8, 3, 7, 1, 2, 9, 4]) == 131
    assert candidate(values = [100, 1, 100, 1, 100, 1, 100]) == 10301
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2658000
    assert candidate(values = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110]) == 459000
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 570
    assert candidate(values = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 29750
    assert candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54]) == 14469840
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 238
    assert candidate(values = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 328000
    assert candidate(values = [12, 21, 34, 43, 55, 67, 78, 89, 90, 101, 112, 123, 134, 145, 156]) == 1453368
    assert candidate(values = [5, 6, 7, 8, 9, 10, 11]) == 1850
    assert candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 11702400
    assert candidate(values = [8, 2, 3, 4, 1, 5, 7]) == 125
    assert candidate(values = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 328
    assert candidate(values = [1, 100, 2, 99, 3, 98, 4, 97, 5]) == 2254
    assert candidate(values = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89]) == 7158270
    assert candidate(values = [3, 2, 1, 4, 6, 5, 9, 7, 8]) == 248
    assert candidate(values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 5634
    assert candidate(values = [7, 6, 8, 5, 3, 4, 9, 2]) == 386
    assert candidate(values = [7, 3, 8, 6, 2, 9, 1, 4, 10, 5]) == 248
    assert candidate(values = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1118000
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 54
    assert candidate(values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == 726000000
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 51
    assert candidate(values = [9, 1, 8, 2, 7, 3, 6, 4, 5, 10, 11, 12, 13, 14, 15]) == 1088
    assert candidate(values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1128
    assert candidate(values = [40, 10, 30, 20, 50, 60, 70, 80, 90]) == 252000
    assert candidate(values = [25, 15, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135]) == 1254375
    assert candidate(values = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2, 1, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 66691
    assert candidate(values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 47
    assert candidate(values = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 238
    assert candidate(values = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 101010101000
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 71978
    assert candidate(values = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1151000
    assert candidate(values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1118
    assert candidate(values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 864
    assert candidate(values = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 291840
    assert candidate(values = [7, 8, 9, 10, 11, 12, 13, 14]) == 5194
    assert candidate(values = [12, 8, 6, 3, 7, 11, 9, 5, 4]) == 1299
    assert candidate(values = [10, 1, 100, 10, 1, 100, 10, 1, 100]) == 3031
    assert candidate(values = [9, 1, 8, 1, 7, 2, 6, 3, 5, 4]) == 125
    assert candidate(values = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5, 94, 6]) == 3836
    assert candidate(values = [5, 6, 3, 2, 7, 8, 4, 1, 9]) == 201
    assert candidate(values = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 32000000
    assert candidate(values = [3, 7, 4, 5, 6, 8, 2, 9, 1]) == 181
    assert candidate(values = [10, 5, 1, 100, 10, 5, 1]) == 1110
    assert candidate(values = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 41788
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80]) == 166000
    assert candidate(values = [99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 56498
    assert candidate(values = [5, 25, 15, 10, 40, 50]) == 14625
    assert candidate(values = [10, 20, 30, 40, 50]) == 38000
    assert candidate(values = [3, 5, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 568
    assert candidate(values = [2, 5, 8, 13, 21, 34, 55, 89]) == 15792
    assert candidate(values = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 10503
    assert candidate(values = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1625
    assert candidate(values = [12, 34, 56, 78, 90, 11, 22, 33, 44, 55]) == 208538
    assert candidate(values = [50, 20, 10, 30, 40, 60, 80, 70, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2733000
    assert candidate(values = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 238000


