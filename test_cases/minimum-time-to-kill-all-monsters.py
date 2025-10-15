def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(power = [17]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [17]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 721695391
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 721695391: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 4, 8, 16, 32, 64, 128]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 4, 8, 16, 32, 64, 128]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(power = [3, 1, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [3, 1, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 9, 3, 1, 7]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 9, 3, 1, 7]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(power = [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 6, 10, 15]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 6, 10, 15]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 5, 5, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 5, 5, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 4, 9]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 4, 9]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 30, 40]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 30, 40]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1000000000]) == 500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1000000000]) == 500000001: {e}')
    
    total += 1
    try:
        result = candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 5, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 5, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(power = [16, 8, 4, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [16, 8, 4, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 3, 6, 1, 5, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 17]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 3, 6, 1, 5, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 17]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [7, 3, 9, 2, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [7, 3, 9, 2, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 3439552527
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 3439552527: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 2439552528
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 2439552528: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(power = [8, 6, 7, 5, 3, 0, 9, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [8, 6, 7, 5, 3, 0, 9, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(power = [3, 6, 10, 15, 21]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [3, 6, 10, 15, 21]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(power = [256, 128, 64, 32, 16, 8, 4, 2, 1, 1, 2, 4, 8, 16, 32, 64, 128]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [256, 128, 64, 32, 16, 8, 4, 2, 1, 1, 2, 4, 8, 16, 32, 64, 128]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]) == 457
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]) == 457: {e}')
    
    total += 1
    try:
        result = candidate(power = [15, 20, 10, 30, 5, 40, 25, 35, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [15, 20, 10, 30, 5, 40, 25, 35, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(power = [17, 9, 5, 3, 2, 1, 10, 6, 4, 7, 11, 13, 15, 12, 14, 16, 8]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [17, 9, 5, 3, 2, 1, 10, 6, 4, 7, 11, 13, 15, 12, 14, 16, 8]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 16563
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 16563: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1, 500000000, 2, 750000000, 3, 250000000, 4]) == 365476196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1, 500000000, 2, 750000000, 3, 250000000, 4]) == 365476196: {e}')
    
    total += 1
    try:
        result = candidate(power = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 15, 10, 5, 20, 25, 30, 5, 10, 15, 20, 25, 30, 5, 10, 15, 20]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 15, 10, 5, 20, 25, 30, 5, 10, 15, 20, 25, 30, 5, 10, 15, 20]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 15, 25, 30, 5, 40, 35, 2, 8, 12, 18, 24, 3, 6, 9, 11]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 15, 25, 30, 5, 40, 35, 2, 8, 12, 18, 24, 3, 6, 9, 11]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 3, 8, 6, 11, 9, 14, 12, 17, 15, 20, 18, 23, 21, 26, 24, 29]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 3, 8, 6, 11, 9, 14, 12, 17, 15, 20, 18, 23, 21, 26, 24, 29]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 3, 5, 7, 11, 13, 17, 19]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 3, 5, 7, 11, 13, 17, 19]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(power = [8, 6, 7, 5, 3, 0, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [8, 6, 7, 5, 3, 0, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(power = [17, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [17, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 3, 8, 2, 7, 4, 6]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 3, 8, 2, 7, 4, 6]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 759523813
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 759523813: {e}')
    
    total += 1
    try:
        result = candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16, 15, 14, 13, 12, 11, 10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16, 15, 14, 13, 12, 11, 10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1, 64, 32, 16, 8, 4]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1, 64, 32, 16, 8, 4]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 4, 8, 16, 32, 64, 128]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 4, 8, 16, 32, 64, 128]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 8287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 8287: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 10, 100, 1000, 10000]) == 2290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 10, 100, 1000, 10000]) == 2290: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000]) == 65908401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000]) == 65908401: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84]) == 306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84]) == 306: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 9, 2, 7, 3]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 9, 2, 7, 3]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1, 1000000000, 1, 1000000000]) == 783333336
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1, 1000000000, 1, 1000000000]) == 783333336: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 500000000, 100000000, 50000000, 10000000, 5000000, 1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10]) == 101658453
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 500000000, 100000000, 50000000, 10000000, 5000000, 1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10]) == 101658453: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [50, 25, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425]) == 425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [50, 25, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425]) == 425: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 999999999, 99999999, 9999999, 999999, 99999, 9999, 999]) == 136953726
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 999999999, 99999999, 9999999, 999999, 99999, 9999, 999]) == 136953726: {e}')
    
    total += 1
    try:
        result = candidate(power = [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(power = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]) == 153: {e}')
    
    total += 1
    try:
        result = candidate(power = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153]) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153]) == 153: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]) == 1700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]) == 1700: {e}')
    
    total += 1
    try:
        result = candidate(power = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(power = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(power = [15, 10, 5, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [15, 10, 5, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(power = [17, 3, 7, 16, 15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [17, 3, 7, 16, 15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 50, 25, 12, 6, 3, 1]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 50, 25, 12, 6, 3, 1]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(power = [9, 7, 5, 3, 2, 1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [9, 7, 5, 3, 2, 1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(power = [7, 3, 8, 4, 2, 6, 5, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [7, 3, 8, 4, 2, 6, 5, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(power = [7, 3, 10, 1, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [7, 3, 10, 1, 5]) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(power = [17]) == 17
    assert candidate(power = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 17
    assert candidate(power = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 721695391
    assert candidate(power = [10, 20, 30]) == 30
    assert candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 17
    assert candidate(power = [1, 1, 4]) == 4
    assert candidate(power = [2, 4, 8, 16, 32, 64, 128]) == 48
    assert candidate(power = [3, 1, 4]) == 4
    assert candidate(power = [5, 9, 3, 1, 7]) == 9
    assert candidate(power = [1, 2, 3, 4, 5]) == 5
    assert candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 16
    assert candidate(power = [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17
    assert candidate(power = [1]) == 1
    assert candidate(power = [1, 3, 6, 10, 15]) == 11
    assert candidate(power = [5, 5, 5, 5]) == 12
    assert candidate(power = [1, 2, 4, 9]) == 6
    assert candidate(power = [10, 20, 30, 40]) == 40
    assert candidate(power = [1, 1000000000]) == 500000001
    assert candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(power = [10, 5, 1]) == 8
    assert candidate(power = [1, 1, 1, 1]) == 4
    assert candidate(power = [16, 8, 4, 2, 1]) == 10
    assert candidate(power = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 17
    assert candidate(power = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153]) == 89
    assert candidate(power = [2, 3, 6, 1, 5, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 17]) == 17
    assert candidate(power = [7, 3, 9, 2, 5]) == 10
    assert candidate(power = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 48
    assert candidate(power = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 3439552527
    assert candidate(power = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == 2439552528
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1]) == 17
    assert candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 18
    assert candidate(power = [8, 6, 7, 5, 3, 0, 9, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 17
    assert candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 85
    assert candidate(power = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90]) == 43
    assert candidate(power = [3, 6, 10, 15, 21]) == 19
    assert candidate(power = [256, 128, 64, 32, 16, 8, 4, 2, 1, 1, 2, 4, 8, 16, 32, 64, 128]) == 62
    assert candidate(power = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]) == 457
    assert candidate(power = [15, 20, 10, 30, 5, 40, 25, 35, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 24
    assert candidate(power = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256]) == 62
    assert candidate(power = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 100
    assert candidate(power = [17, 9, 5, 3, 2, 1, 10, 6, 4, 7, 11, 13, 15, 12, 14, 16, 8]) == 17
    assert candidate(power = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]) == 16563
    assert candidate(power = [1000000000, 1, 500000000, 2, 750000000, 3, 250000000, 4]) == 365476196
    assert candidate(power = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]) == 51
    assert candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]) == 17
    assert candidate(power = [10, 15, 10, 5, 20, 25, 30, 5, 10, 15, 20, 25, 30, 5, 10, 15, 20]) == 38
    assert candidate(power = [10, 20, 15, 25, 30, 5, 40, 35, 2, 8, 12, 18, 24, 3, 6, 9, 11]) == 33
    assert candidate(power = [5, 3, 8, 6, 11, 9, 14, 12, 17, 15, 20, 18, 23, 21, 26, 24, 29]) == 34
    assert candidate(power = [2, 3, 5, 7, 11, 13, 17, 19]) == 19
    assert candidate(power = [8, 6, 7, 5, 3, 0, 9]) == 10
    assert candidate(power = [17, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 17
    assert candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]) == 34
    assert candidate(power = [5, 3, 8, 2, 7, 4, 6]) == 10
    assert candidate(power = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000]) == 759523813
    assert candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16, 15, 14, 13, 12, 11, 10]) == 17
    assert candidate(power = [16, 8, 4, 2, 1, 32, 16, 8, 4, 2, 1, 64, 32, 16, 8, 4]) == 26
    assert candidate(power = [2, 4, 8, 16, 32, 64, 128]) == 48
    assert candidate(power = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2]) == 17
    assert candidate(power = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 15, 14, 13, 12, 11, 10]) == 17
    assert candidate(power = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 8287
    assert candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 25
    assert candidate(power = [1, 10, 100, 1000, 10000]) == 2290
    assert candidate(power = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000]) == 65908401
    assert candidate(power = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84]) == 306
    assert candidate(power = [5, 9, 2, 7, 3]) == 10
    assert candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == 33
    assert candidate(power = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 48
    assert candidate(power = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 1]) == 17
    assert candidate(power = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 31
    assert candidate(power = [1000000000, 1, 1000000000, 1, 1000000000]) == 783333336
    assert candidate(power = [1000000000, 500000000, 100000000, 50000000, 10000000, 5000000, 1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10]) == 101658453
    assert candidate(power = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 17
    assert candidate(power = [50, 25, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425]) == 425
    assert candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]) == 170
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 19
    assert candidate(power = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 999999999, 99999999, 9999999, 999999, 99999, 9999, 999]) == 136953726
    assert candidate(power = [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17
    assert candidate(power = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]) == 19
    assert candidate(power = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119]) == 119
    assert candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 17
    assert candidate(power = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]) == 153
    assert candidate(power = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153]) == 153
    assert candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]) == 1700
    assert candidate(power = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3]) == 17
    assert candidate(power = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8]) == 19
    assert candidate(power = [15, 10, 5, 1]) == 12
    assert candidate(power = [17, 3, 7, 16, 15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == 19
    assert candidate(power = [100, 50, 25, 12, 6, 3, 1]) == 37
    assert candidate(power = [9, 7, 5, 3, 2, 1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 21
    assert candidate(power = [7, 3, 8, 4, 2, 6, 5, 1]) == 8
    assert candidate(power = [7, 3, 10, 1, 5]) == 9


