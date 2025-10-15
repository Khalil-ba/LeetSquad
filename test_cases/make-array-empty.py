def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -1, -2, -4]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -1, -2, -4]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, -10, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, -10, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 10, -10, 5, -5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 10, -10, 5, -5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -1, 0, 2, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -1, 0, 2, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 2, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 2, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -1, 0, 2, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -1, 0, 2, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 4, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 4, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 1, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 1, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -1, -3, -2, -4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -1, -3, -2, -4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 125, 200]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 125, 200]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 5, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 5, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 150, 250, 350, 450, 650, 750, 850, 950, 550]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 150, 250, 350, 450, 650, 750, 850, 950, 550]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 9]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 9]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 0]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 0]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2, 3, 4, 5, 6, 7, 8, 9]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2, 3, 4, 5, 6, 7, 8, 9]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 5, 15, 25, 30]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 5, 15, 25, 30]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -50, -25, -125, -62, -31, -156, -78, -39]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -50, -25, -125, -62, -31, -156, -78, -39]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 3, 6, 12, 24, 48, 96]) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 3, 6, 12, 24, 48, 96]) == 132: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -10, -100, -1000, -10000, -100000, -1000000, -10000000, -100000000, -1000000000]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -10, -100, -1000, -10000, -100000, -1000000, -10000000, -100000000, -1000000000]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0, 11, 13, 15, 17, 19, 12, 14, 16, 18, 20]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0, 11, 13, 15, 17, 19, 12, 14, 16, 18, 20]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 20, 15, 30, 25, 40, 35, 50, 45, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 20, 15, 30, 25, 40, 35, 50, 45, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 4, 6, 8, 1, 3, 5, 7, 9]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 4, 6, 8, 1, 3, 5, 7, 9]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 100, -20, 200, -30, 300, -40, 400, -50, 500]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 100, -20, 200, -30, 300, -40, 400, -50, 500]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 4, 2, 6, 8, 7]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 4, 2, 6, 8, 7]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000, -250000000]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000, -250000000]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 4, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 4, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 20, 15, 30, 25, 40, 35, 50, 45]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 20, 15, 30, 25, 40, 35, 50, 45]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 4, 3, 20, 15]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 4, 3, 20, 15]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 125, 62, 31, 156, 78, 39]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 125, 62, 31, 156, 78, 39]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -999999999, -1000000001, -999999998, -1000000002]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -999999999, -1000000001, -999999998, -1000000002]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -1000, -10000, -100000, -1000000, -10000000, -100000000, -1000000000, -10000000000, 1]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -1000, -10000, -100000, -1000000, -10000000, -100000000, -1000000000, -10000000000, 1]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 5, 4, 6, 8, 7, 9]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 5, 4, 6, 8, 7, 9]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1000000000, 2, -999999999, 3, -999999998, 4, -999999997]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1000000000, 2, -999999999, 3, -999999998, 4, -999999997]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 1, -1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 1, -1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1000000000, 1, -1000000000, 2, -999999999, 3, -999999998, 4, -999999997]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1000000000, 1, -1000000000, 2, -999999999, 3, -999999998, 4, -999999997]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, 10]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, 10]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, -500000000, -1000000000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, -500000000, -1000000000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, -999999999, 999999998, -999999998, 999999997, -999999997]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, -999999999, 999999998, -999999998, 999999997, -999999997]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 1, 4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 1, 4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 1, 3, 4]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 1, 3, 4]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 0]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 0]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 2, 4, 6]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 2, 4, 6]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, 0, 250000000]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, 0, 250000000]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 100, 50, 20, -20]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 100, 50, 20, -20]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, 0, 5, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, 0, 5, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50, 25, -25]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50, 25, -25]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000000000, -1000000000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000000000, -1000000000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 5, 15, 25]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 5, 15, 25]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 3, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 3, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 4, 1, 3]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 4, 1, 3]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -5, -15, -25]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -5, -15, -25]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 1, 2, 0, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 1, 2, 0, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 3, 8, 2]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 3, 8, 2]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 100, 5, 2, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 100, 5, 2, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 100, 0, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 100, 0, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -1, -2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -1, -2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 5, 2, 4, 6, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 5, 2, 4, 6, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 1, 2, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 1, 2, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 10, 0, 7, -3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 10, 0, 7, -3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -1, -4, -2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -1, -4, -2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 100, 0, 5, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 100, 0, 5, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 1, 2, 0, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 1, 2, 0, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -1, -2, -4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -1, -2, -4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 3, 8, 2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 3, 8, 2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 2, 1, 4]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 2, 1, 4]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -1, -4, -2]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -1, -4, -2]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -2, 2]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -2, 2]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -1, -4, -2, -3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -1, -4, -2, -3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -1, 2, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -1, 2, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 5, 1, 9, 2, 4, 6, 8]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 5, 1, 9, 2, 4, 6, 8]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -1, 1, 3, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -1, 1, 3, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 3, 7]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 3, 7]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -2, -4, -1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -2, -4, -1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 3, -2, 1, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 3, -2, 1, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 5, 6, 3, 4, 1, 2]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 5, 6, 3, 4, 1, 2]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 100, 0, 5, -5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 100, 0, 5, -5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 55
    assert candidate(nums = [-3, -1, -2, -4]) == 8
    assert candidate(nums = [10, 20, -10, 0]) == 6
    assert candidate(nums = [0, 10, -10, 5, -5]) == 9
    assert candidate(nums = [-3, -1, 0, 2, 4]) == 5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [1, 3, 2]) == 4
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 28
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 15
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000]) == 7
    assert candidate(nums = [10, 20, 30, 40, 50]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums = [-3, -2, -1]) == 3
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 22
    assert candidate(nums = [0, 1, -1, 2, -2]) == 12
    assert candidate(nums = [5, 1, 3, 2, 4]) == 9
    assert candidate(nums = [1, 3, 2]) == 4
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000]) == 7
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 55
    assert candidate(nums = [-3, -1, 0, 2, 5]) == 5
    assert candidate(nums = [5, 1, 2, 4, 3]) == 8
    assert candidate(nums = [100, 200, 300, 400, 500]) == 5
    assert candidate(nums = [1, 2, 4, 3]) == 5
    assert candidate(nums = [5, 2, 6, 1, 4]) == 11
    assert candidate(nums = [1, 2, 3]) == 3
    assert candidate(nums = [3, 4, -1]) == 5
    assert candidate(nums = [-100, -200, -300, -400, -500]) == 15
    assert candidate(nums = [5, 3, 1, 2, 4]) == 9
    assert candidate(nums = [-5, -1, -3, -2, -4]) == 9
    assert candidate(nums = [50, 40, 30, 20, 10]) == 15
    assert candidate(nums = [100, 50, 25, 125, 200]) == 12
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 20
    assert candidate(nums = [50, 40, 30, 20, 10, 5, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]) == 57
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 150, 250, 350, 450, 650, 750, 850, 950, 550]) == 120
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 10
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 10
    assert candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 9]) == 30
    assert candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40]) == 55
    assert candidate(nums = [1, -10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 51
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 0]) == 35
    assert candidate(nums = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2, 3, 4, 5, 6, 7, 8, 9]) == 31
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 45
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 50
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 15
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997]) == 14
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [10, 20, 5, 15, 25, 30]) == 14
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4]) == 26
    assert candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50]) == 55
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1]) == 26
    assert candidate(nums = [-100, -200, -300, -50, -25, -125, -62, -31, -156, -78, -39]) == 48
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 465
    assert candidate(nums = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == 41
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 165
    assert candidate(nums = [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 3, 6, 12, 24, 48, 96]) == 132
    assert candidate(nums = [-1, -10, -100, -1000, -10000, -100000, -1000000, -10000000, -100000000, -1000000000]) == 55
    assert candidate(nums = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0, 11, 13, 15, 17, 19, 12, 14, 16, 18, 20]) == 115
    assert candidate(nums = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15]) == 15
    assert candidate(nums = [10, 5, 20, 15, 30, 25, 40, 35, 50, 45, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(nums = [10, 2, 4, 6, 8, 1, 3, 5, 7, 9]) == 35
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1]) == 19
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 55
    assert candidate(nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]) == 75
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 15
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 55
    assert candidate(nums = [-10, 100, -20, 200, -30, 300, -40, 400, -50, 500]) == 40
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 55
    assert candidate(nums = [5, 3, 1, 4, 2, 6, 8, 7]) == 19
    assert candidate(nums = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]) == 10
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000, -250000000]) == 12
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 55
    assert candidate(nums = [5, 3, 1, 4, 2]) == 9
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 55
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 30
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 10]) == 30
    assert candidate(nums = [10, 5, 20, 15, 30, 25, 40, 35, 50, 45]) == 35
    assert candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40]) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 165
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 10
    assert candidate(nums = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 10
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 25
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 30
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 144
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 22
    assert candidate(nums = [7, 10, 4, 3, 20, 15]) == 16
    assert candidate(nums = [100, 50, 25, 125, 62, 31, 156, 78, 39]) == 18
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 20
    assert candidate(nums = [-1000000000, -999999999, -1000000001, -999999998, -1000000002]) == 12
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110]) == 110
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1001]) == 110
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 41
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == 21
    assert candidate(nums = [-100, -1000, -10000, -100000, -1000000, -10000000, -100000000, -1000000000, -10000000000, 1]) == 54
    assert candidate(nums = [3, 1, 2, 5, 4, 6, 8, 7, 9]) == 23
    assert candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002]) == 12
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000]) == 8
    assert candidate(nums = [1, -1000000000, 2, -999999999, 3, -999999998, 4, -999999997]) == 12
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]) == 98
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 190
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 20
    assert candidate(nums = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 15
    assert candidate(nums = [1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == 55
    assert candidate(nums = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90]) == 27
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 55
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 165
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 45
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 1, -1]) == 12
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums = [-1, 1000000000, 1, -1000000000, 2, -999999999, 3, -999999998, 4, -999999997]) == 17
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6]) == 25
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 120
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5]) == 40
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, 10]) == 54
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 55
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 15
    assert candidate(nums = [1000000000, 500000000, -500000000, -1000000000]) == 10
    assert candidate(nums = [999999999, -999999999, 999999998, -999999998, 999999997, -999999997]) == 12
    assert candidate(nums = [5, 1, 4, 2, 3]) == 8
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 7
    assert candidate(nums = [5, 2, 3, 1, 4]) == 10
    assert candidate(nums = [5, 2, 6, 1, 3, 4]) == 13
    assert candidate(nums = [1000000000, -1000000000, 0]) == 4
    assert candidate(nums = [1, 2, 4, 3]) == 5
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 0]) == 8
    assert candidate(nums = [10, 20, 30, 40, 50]) == 5
    assert candidate(nums = [-1, -2, -3, -4]) == 10
    assert candidate(nums = [1, 3, 5, 2, 4, 6]) == 12
    assert candidate(nums = [1000000000, -1000000000, 500000000, 0, 250000000]) == 8
    assert candidate(nums = [1, 3, 2, 5, 4]) == 9
    assert candidate(nums = [-10, 100, 50, 20, -20]) == 12
    assert candidate(nums = [-10, 10, 0, 5, 3]) == 8
    assert candidate(nums = [1, -1, 2, -2, 3, -3]) == 18
    assert candidate(nums = [100, -100, 50, -50, 25, -25]) == 12
    assert candidate(nums = [1, 1000000000, -1000000000]) == 5
    assert candidate(nums = [10, 20, 30, 5, 15, 25]) == 15
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 55
    assert candidate(nums = [5, 1, 2, 3, 4]) == 6
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3]) == 7
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
    assert candidate(nums = [50, 40, 30, 20, 10]) == 15
    assert candidate(nums = [5, 3, 8, 6, 2]) == 13
    assert candidate(nums = [5, 1, 4, 2, 3]) == 8
    assert candidate(nums = [1, -2, 3, -4, 5]) == 12
    assert candidate(nums = [5]) == 1
    assert candidate(nums = [5, 2, 4, 1, 3]) == 12
    assert candidate(nums = [1000000000, -1000000000, 500000000]) == 4
    assert candidate(nums = [-10, -20, -30, -5, -15, -25]) == 12
    assert candidate(nums = [0, 1, -1, 2, -2]) == 12
    assert candidate(nums = [-5, 1, 2, 0, 3]) == 8
    assert candidate(nums = [10, 5, 3, 8, 2]) == 13
    assert candidate(nums = [-10, 100, 5, 2, 0]) == 11
    assert candidate(nums = [-10, 100, 0, 5]) == 5
    assert candidate(nums = [1000000000, -1000000000]) == 3
    assert candidate(nums = [-3, -1, -2]) == 4
    assert candidate(nums = [10, -10, 20, -20, 30, -30]) == 18
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
    assert candidate(nums = [7, 3, 5, 2, 4, 6, 1]) == 22
    assert candidate(nums = [5, 3, 8, 1, 4]) == 11
    assert candidate(nums = [-5, 1, 2, 0]) == 6
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997]) == 10
    assert candidate(nums = [5, 4, 3, 2, 1]) == 15
    assert candidate(nums = [5, 3, 1, 2, 4]) == 9
    assert candidate(nums = [-5, 10, 0, 7, -3]) == 9
    assert candidate(nums = [-3, -1, -4, -2]) == 8
    assert candidate(nums = [10, -10, 0]) == 4
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 10
    assert candidate(nums = [0]) == 1
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 51
    assert candidate(nums = [3, 4, -1]) == 5
    assert candidate(nums = [-10, 100, 0, 5, 3]) == 8
    assert candidate(nums = [-5, 1, 2, 0, -1]) == 10
    assert candidate(nums = [-5, -3, -1, -2, -4]) == 9
    assert candidate(nums = [10, -5, 3, 8, 2]) == 9
    assert candidate(nums = [0, -1, 1]) == 5
    assert candidate(nums = [5, 3, 2, 1, 4]) == 13
    assert candidate(nums = [-5, -3, -1, -4, -2]) == 9
    assert candidate(nums = [0, -1, 1, -2, 2]) == 12
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 28
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2]) == 55
    assert candidate(nums = [1000000000, -1000000000, 500000000]) == 4
    assert candidate(nums = [-5, -1, -4, -2, -3]) == 8
    assert candidate(nums = [-10, -20, -30, -40, -50]) == 15
    assert candidate(nums = [1, 2, 3]) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 55
    assert candidate(nums = [-5, -3, -1, 2, 4]) == 5
    assert candidate(nums = [1, -1, 2, -2, 3, -3]) == 18
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
    assert candidate(nums = [7, 3, 5, 1, 9, 2, 4, 6, 8]) == 25
    assert candidate(nums = [-10, -20, -30, -40, -50]) == 15
    assert candidate(nums = [-5, -3, -1, 1, 3, 5]) == 6
    assert candidate(nums = [5, 1, 9, 3, 7]) == 9
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(nums = [9, 7, 5, 3, 1]) == 15
    assert candidate(nums = [42]) == 1
    assert candidate(nums = [-5, -3, -2, -4, -1]) == 8
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 35
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 22
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 120
    assert candidate(nums = [-5, 3, -2, 1, 4]) == 7
    assert candidate(nums = [1, 2]) == 2
    assert candidate(nums = [7, 5, 6, 3, 4, 1, 2]) == 16
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30
    assert candidate(nums = [-10, 100, 0, 5, -5]) == 9
    assert candidate(nums = [5, 4, 3, 2, 1]) == 15


