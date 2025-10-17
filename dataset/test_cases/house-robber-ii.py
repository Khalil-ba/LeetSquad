def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 4, 7, 8]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 4, 7, 8]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 3, 140, 20, 10, 5, 5, 200]) == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 3, 140, 20, 10, 5, 5, 200]) == 455: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 7, 9, 3, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 7, 9, 3, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 4, 2, 5, 7, 8]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 4, 2, 5, 7, 8]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 3, 140, 20, 10]) == 340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 3, 140, 20, 10]) == 340: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 100, 10, 5, 5]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 100, 10, 5, 5]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 3, 100, 4]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 3, 100, 4]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 1, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 1, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 3, 4, 5, 6]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 3, 4, 5, 6]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 300, 150, 100, 250, 300, 200, 100, 50, 400, 350, 250]) == 1450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 300, 150, 100, 250, 300, 200, 100, 50, 400, 350, 250]) == 1450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 150, 200, 250, 300]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 150, 200, 250, 300]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 0, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500]) == 3300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 0, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500]) == 3300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 100, 50, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 50, 150, 200, 300, 400, 500]) == 4050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 100, 50, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 50, 150, 200, 300, 400, 500]) == 4050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 10, 1]) == 3020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 10, 1]) == 3020: {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 200, 200, 100, 400, 90, 200, 200, 100, 400, 90, 200, 200, 100, 400]) == 1800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 200, 200, 100, 400, 90, 200, 200, 100, 400, 90, 200, 200, 100, 400]) == 1800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 3, 12, 8, 6, 11, 7, 14, 9]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 3, 12, 8, 6, 11, 7, 14, 9]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 2, 5, 2, 6, 2, 5, 2, 6, 2, 5, 2, 6]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 2, 5, 2, 6, 2, 5, 2, 6, 2, 5, 2, 6]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100, 100]) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100, 100]) == 208: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 100, 500, 100, 500, 100, 500, 100, 500, 100, 500, 100, 500]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 100, 500, 100, 500, 100, 500, 100, 500, 100, 500, 100, 500]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909]) == 3213
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909]) == 3213: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 1, 100, 1, 100, 1, 200, 1, 100, 1, 100, 1]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 1, 100, 1, 100, 1, 200, 1, 100, 1, 100, 1]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 0, 0, 0, 0, 0, 0, 0, 0, 1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 0, 0, 0, 0, 0, 0, 0, 0, 1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [800, 200, 100, 300, 600, 400, 500, 700, 50, 90]) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [800, 200, 100, 300, 600, 400, 500, 700, 50, 90]) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 4995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 4995: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 1, 50, 1, 1, 50, 1, 1, 50, 1, 1]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 1, 50, 1, 1, 50, 1, 1, 50, 1, 1]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 100, 5, 100, 5, 100, 5, 100, 5, 100, 5, 100, 5, 100, 5, 100]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 100, 5, 100, 5, 100, 5, 100, 5, 100, 5, 100, 5, 100, 5, 100]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 100]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 100]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 3, 140, 20, 10, 5, 5, 200, 150, 250, 350, 450]) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 3, 140, 20, 10, 5, 5, 200, 150, 250, 350, 450]) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 5, 10, 5, 10, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 5, 10, 5, 10, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 9, 1, 5, 1, 2, 9, 1, 5, 1, 2, 9, 1, 5, 1, 2, 9, 1]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 9, 1, 5, 1, 2, 9, 1, 5, 1, 2, 9, 1, 5, 1, 2, 9, 1]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 3, 4, 1, 5, 6, 7, 8, 9, 10]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 3, 4, 1, 5, 6, 7, 8, 9, 10]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 4, 1, 7, 3, 2, 5, 6, 8, 0, 12, 15]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 4, 1, 7, 3, 2, 5, 6, 8, 0, 12, 15]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 6, 7, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 6, 7, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 1, 1, 10, 1, 1, 1, 10, 1, 1, 1, 10, 1, 1, 1]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 1, 1, 10, 1, 1, 1, 10, 1, 1, 1, 10, 1, 1, 1]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 6951
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 6951: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 100, 0, 100, 0, 100]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 100, 0, 100, 0, 100]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 1, 50, 1, 1, 50, 1, 1, 50]) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 1, 50, 1, 1, 50, 1, 1, 50]) == 151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 640: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 100, 1, 3, 1, 3, 1, 3, 100]) == 209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 100, 1, 3, 1, 3, 1, 3, 100]) == 209: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 5, 3, 7, 9, 8, 10, 2, 5]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 5, 3, 7, 9, 8, 10, 2, 5]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 50, 100, 50, 100, 50]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 50, 100, 50, 100, 50]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 0, 100, 0, 100, 0, 100, 0, 100]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 0, 100, 0, 100, 0, 100, 0, 100]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50]) == 5050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50]) == 5050: {e}')
    
    total += 1
    try:
        result = candidate(nums = [250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250, 0, 250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250]) == 1650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250, 0, 250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250]) == 1650: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0]) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0]) == 8000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 630: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 50, 1, 50, 1, 50, 1, 50, 1]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 50, 1, 50, 1, 50, 1, 50, 1]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 3, 5, 7, 1, 3, 5, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 3, 5, 7, 1, 3, 5, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 650: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 200, 300, 100, 50]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 200, 300, 100, 50]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 1680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 1680: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975]) == 11856
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975]) == 11856: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, 0, 100, 0, 0, 100, 0, 0, 100]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, 0, 100, 0, 0, 100, 0, 0, 100]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1, 999, 1, 999, 1, 999, 1]) == 3996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1, 999, 1, 999, 1, 999, 1]) == 3996: {e}')
    
    total += 1
    try:
        result = candidate(nums = [200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 9990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 9990: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 100: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 3, 1]) == 4
    assert candidate(nums = [1, 0, 1, 0, 1]) == 2
    assert candidate(nums = [5, 1, 2, 4, 7, 8]) == 14
    assert candidate(nums = [5, 3, 1, 1, 1]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
    assert candidate(nums = [10, 20, 30, 40, 50]) == 80
    assert candidate(nums = [300, 3, 140, 20, 10, 5, 5, 200]) == 455
    assert candidate(nums = [5, 5, 5, 5, 5]) == 10
    assert candidate(nums = [4, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25
    assert candidate(nums = [1, 2, 3, 4, 5]) == 8
    assert candidate(nums = [2, 7, 9, 3, 1]) == 11
    assert candidate(nums = [1000]) == 1000
    assert candidate(nums = [2, 3, 2]) == 3
    assert candidate(nums = [2, 1, 1, 2]) == 3
    assert candidate(nums = [3, 6, 4, 2, 5, 7, 8]) == 19
    assert candidate(nums = [1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [200, 3, 140, 20, 10]) == 340
    assert candidate(nums = [5, 5, 10, 100, 10, 5, 5]) == 110
    assert candidate(nums = [300, 3, 100, 4]) == 400
    assert candidate(nums = [5, 1, 1, 5]) == 6
    assert candidate(nums = [1, 2]) == 2
    assert candidate(nums = [1, 2, 3]) == 3
    assert candidate(nums = [10, 2, 3, 4, 5, 6]) == 18
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 7000
    assert candidate(nums = [200, 300, 150, 100, 250, 300, 200, 100, 50, 400, 350, 250]) == 1450
    assert candidate(nums = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0]) == 500
    assert candidate(nums = [50, 100, 150, 200, 250, 300]) == 600
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
    assert candidate(nums = [500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 0, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500]) == 3300
    assert candidate(nums = [200, 100, 50, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 50, 150, 200, 300, 400, 500]) == 4050
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2550
    assert candidate(nums = [10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1]) == 70
    assert candidate(nums = [1, 10, 100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 10, 1]) == 3020
    assert candidate(nums = [90, 200, 200, 100, 400, 90, 200, 200, 100, 400, 90, 200, 200, 100, 400]) == 1800
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 24
    assert candidate(nums = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 5000
    assert candidate(nums = [5, 10, 3, 12, 8, 6, 11, 7, 14, 9]) == 47
    assert candidate(nums = [5, 2, 6, 2, 5, 2, 6, 2, 5, 2, 6, 2, 5, 2, 6]) == 39
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 63
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12
    assert candidate(nums = [100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100, 100]) == 208
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3000
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 168
    assert candidate(nums = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 109
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 240
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 35
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 84
    assert candidate(nums = [100, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 200
    assert candidate(nums = [500, 100, 500, 100, 500, 100, 500, 100, 500, 100, 500, 100, 500]) == 3000
    assert candidate(nums = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909]) == 3213
    assert candidate(nums = [200, 1, 100, 1, 100, 1, 200, 1, 100, 1, 100, 1]) == 800
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 500
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 63
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1000, 0, 0, 0, 0, 0, 0, 0, 0, 1000]) == 1000
    assert candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 19
    assert candidate(nums = [800, 200, 100, 300, 600, 400, 500, 700, 50, 90]) == 2200
    assert candidate(nums = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 4995
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 50
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 200
    assert candidate(nums = [50, 1, 1, 50, 1, 1, 50, 1, 1, 50, 1, 1]) == 200
    assert candidate(nums = [5, 100, 5, 100, 5, 100, 5, 100, 5, 100, 5, 100, 5, 100, 5, 100]) == 800
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 100]) == 2500
    assert candidate(nums = [200, 3, 140, 20, 10, 5, 5, 200, 150, 250, 350, 450]) == 1050
    assert candidate(nums = [1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0]) == 10000
    assert candidate(nums = [5, 10, 5, 10, 5, 10, 5]) == 30
    assert candidate(nums = [5, 1, 2, 9, 1, 5, 1, 2, 9, 1, 5, 1, 2, 9, 1, 5, 1, 2, 9, 1]) == 56
    assert candidate(nums = [10, 2, 3, 4, 1, 5, 6, 7, 8, 9, 10]) == 35
    assert candidate(nums = [9, 4, 1, 7, 3, 2, 5, 6, 8, 0, 12, 15]) == 41
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110
    assert candidate(nums = [2, 3, 5, 6, 7, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 44
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 1000
    assert candidate(nums = [10, 1, 1, 1, 10, 1, 1, 1, 10, 1, 1, 1, 10, 1, 1, 1]) == 44
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985]) == 6951
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 140
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
    assert candidate(nums = [100, 0, 100, 0, 100, 0, 100]) == 300
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 190
    assert candidate(nums = [50, 1, 1, 50, 1, 1, 50, 1, 1, 50]) == 151
    assert candidate(nums = [50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1]) == 500
    assert candidate(nums = [50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 640
    assert candidate(nums = [1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 168
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300
    assert candidate(nums = [1, 3, 1, 3, 100, 1, 3, 1, 3, 1, 3, 100]) == 209
    assert candidate(nums = [10, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 24
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 30
    assert candidate(nums = [10, 2, 5, 3, 7, 9, 8, 10, 2, 5]) == 34
    assert candidate(nums = [200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300, 200, 300]) == 3000
    assert candidate(nums = [50, 100, 50, 100, 50, 100, 50]) == 300
    assert candidate(nums = [100, 100, 0, 100, 0, 100, 0, 100, 0, 100]) == 500
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50]) == 5050
    assert candidate(nums = [250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250, 0, 250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250]) == 1650
    assert candidate(nums = [1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0, 1000, 0]) == 8000
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 110
    assert candidate(nums = [20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20]) == 200
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 630
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 500
    assert candidate(nums = [50, 1, 50, 1, 50, 1, 50, 1, 50, 1]) == 250
    assert candidate(nums = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 10000
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 300
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 800
    assert candidate(nums = [9, 3, 5, 7, 1, 3, 5, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 47
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 60
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 650
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [50, 100, 200, 300, 100, 50]) == 450
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 1680
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980, 979, 978, 977, 976, 975]) == 11856
    assert candidate(nums = [100, 0, 0, 100, 0, 0, 100, 0, 0, 100]) == 300
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 30
    assert candidate(nums = [5, 2, 3, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 52
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 300
    assert candidate(nums = [999, 1, 999, 1, 999, 1, 999, 1]) == 3996
    assert candidate(nums = [200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1, 200, 1]) == 2000
    assert candidate(nums = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 9990
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 90
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 3000
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 100


