def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 7, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 7, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, -10000000, 5000000, -5000000, 2500000, -2500000]) == 5000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, -10000000, 5000000, -5000000, 2500000, -2500000]) == 5000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, -10000000, 5000000, -5000000, 2500000, -2500000, 1250000, -1250000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, -10000000, 5000000, -5000000, 2500000, -2500000, 1250000, -1250000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -1, 0, 4, -2, -9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -1, 0, 4, -2, -9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, -10000000, 10000000, -10000000, 10000000, -10000000]) == 20000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, -10000000, 10000000, -10000000, 10000000, -10000000]) == 20000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-36, 36]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-36, 36]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 1000, -1500, 1500, -2000, 2000, -2500, 2500, -3000, 3000, -3500, 3500, -4000, 4000, -4500, 4500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 1000, -1500, 1500, -2000, 2000, -2500, 2500, -3000, 3000, -3500, 3500, -4000, 4000, -4500, 4500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, -987654, 876543, -876543, 765432, -765432, 654321, -654321, 543210, -543210, 432109, -432109, 321098, -321098, 210987, -210987]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, -987654, 876543, -876543, 765432, -765432, 654321, -654321, 543210, -543210, 432109, -432109, 321098, -321098, 210987, -210987]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 500000, -500000, 250000, -250000, 125000, -125000, 62500, -62500, 31250, -31250, 15625, -15625, 7812, -7812]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 500000, -500000, 250000, -250000, 125000, -125000, 62500, -62500, 31250, -31250, 15625, -15625, 7812, -7812]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 15, -15, 25, -25, 35, -35, 45, -45, 55, -55, 65, -65, 75, -75]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 15, -15, 25, -25, 35, -35, 45, -45, 55, -55, 65, -65, 75, -75]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234567, -7654321, 8901234, -4321098, 5678901, -1234567, 8765432, -2345678, 9876543, -3456789, 4567890, -5678901, 6789012, -6789012, 7890123, -7890123]) == 7307
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234567, -7654321, 8901234, -4321098, 5678901, -1234567, 8765432, -2345678, 9876543, -3456789, 4567890, -5678901, 6789012, -6789012, 7890123, -7890123]) == 7307: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 2000000, -2000000, 3000000, -3000000, 4000000, -4000000, 5000000, -5000000, 6000000, -6000000, 7000000, -7000000, 8000000, -8000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 2000000, -2000000, 3000000, -3000000, 4000000, -4000000, 5000000, -5000000, 6000000, -6000000, 7000000, -7000000, 8000000, -8000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, -10000000, -10000000, -10000000, -10000000, -10000000, -10000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, -10000000, -10000000, -10000000, -10000000, -10000000, -10000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000, -6000, 6000, -7000, 7000, -8000, 8000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000, -6000, 6000, -7000, 7000, -8000, 8000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, -12345, 67890, -67890, 11111, -11111, 22222, -22222, 33333, -33333, 44444, -44444, 55555, -55555, 66666, -66666]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, -12345, 67890, -67890, 11111, -11111, 22222, -22222, 33333, -33333, 44444, -44444, 55555, -55555, 66666, -66666]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, -123, -456, -789, 321, 654, 987, -321, -654, -987, 234, 567, 890, -234, -567, -890]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, -123, -456, -789, 321, 654, 987, -321, -654, -987, 234, 567, 890, -234, -567, -890]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, -10000000, 20000000, -20000000, 30000000, -30000000, 40000000, -40000000, 50000000, -50000000, 60000000, -60000000, 70000000, -70000000, 80000000, -80000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, -10000000, 20000000, -20000000, 30000000, -30000000, 40000000, -40000000, 50000000, -50000000, 60000000, -60000000, 70000000, -70000000, 80000000, -80000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, 10000, -20000, 20000, -30000, 30000, -40000, 40000, -50000, 50000, -60000, 60000, -70000, 70000, -80000, 80000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, 10000, -20000, 20000, -30000, 30000, -40000, 40000, -50000, 50000, -60000, 60000, -70000, 70000, -80000, 80000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 9, 11, 15, 18, 3, 7, 14, 6, 10, 4, 8, 13, 1, 12]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 9, 11, 15, 18, 3, 7, 14, 6, 10, 4, 8, 13, 1, 12]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, -100000, 200000, -200000, 300000, -300000, 400000, -400000, 500000, -500000, 600000, -600000, 700000, -700000, 800000, -800000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, -100000, 200000, -200000, 300000, -300000, 400000, -400000, 500000, -500000, 600000, -600000, 700000, -700000, 800000, -800000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999999, -9999999, 4999999, -4999999, 2499999, -2499999, 1249999, -1249999, 624999, -624999, 312499, -312499, 156249, -156249, 78124, -78124]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999999, -9999999, 4999999, -4999999, 2499999, -2499999, 1249999, -1249999, 624999, -624999, 312499, -312499, 156249, -156249, 78124, -78124]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -500, 2000, -1500, 3000, -2500, 4000, -3500, 5000, -4500, 6000, -5500, 7000, -6500, 8000, -7500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -500, 2000, -1500, 3000, -2500, 4000, -3500, 5000, -4500, 6000, -5500, 7000, -6500, 8000, -7500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500, -1600]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500, -1600]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 500000, -500000, 250000, -250000, 750000, -750000, 375000, -375000, 187500, -187500, 937500, -937500, 468750, -468750]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 500000, -500000, 250000, -250000, 750000, -750000, 375000, -375000, 187500, -187500, 937500, -937500, 468750, -468750]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, -500, 600, -700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500, 1600]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, -500, 600, -700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500, 1600]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 5, -10, 10, -15, 15, -20, 20, -25, 25, -30, 30, -35, 35, -40, 40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 5, -10, 10, -15, 15, -20, 20, -25, 25, -30, 30, -35, 35, -40, 40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 100, -200, 200, -300, 300, -400, 400, -500, 500, -600, 600, -700, 700, -800, 800]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 100, -200, 200, -300, 300, -400, 400, -500, 500, -600, 600, -700, 700, -800, 800]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50, -60, 60, -70, 70, -80, 80]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50, -60, 60, -70, 70, -80, 80]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 33, 55, 77, 99, 22, 44]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 33, 55, 77, 99, 22, 44]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000, 0, -1000000, -2000000, -3000000, -4000000, -5000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000, 0, -1000000, -2000000, -3000000, -4000000, -5000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000000, -9999999, 9999998, -9999997, 9999996, -9999995, 9999994, -9999993, 9999992, -9999991, 9999990, -9999989, 9999988, -9999987, 9999986, -9999985]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000000, -9999999, 9999998, -9999997, 9999996, -9999995, 9999994, -9999993, 9999992, -9999991, 9999990, -9999989, 9999988, -9999987, 9999986, -9999985]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 99999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 99999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999999, -9999999, 8888888, -8888888, 7777777, -7777777, 6666666, -6666666, 5555555, -5555555, 4444444, -4444444, 3333333, -3333333, 2222222, -2222222]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999999, -9999999, 8888888, -8888888, 7777777, -7777777, 6666666, -6666666, 5555555, -5555555, 4444444, -4444444, 3333333, -3333333, 2222222, -2222222]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 9, 2, 6, 4, 7, 0, 11, 13, 15, 17, 19, 21]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 9, 2, 6, 4, 7, 0, 11, 13, 15, 17, 19, 21]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000, 11000000, 12000000, 13000000, 14000000, 15000000, 16000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000, 11000000, 12000000, 13000000, 14000000, 15000000, 16000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [3, 9, 7, 3]) == 2
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0
    assert candidate(nums = [10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
    assert candidate(nums = [10000000, -10000000, 5000000, -5000000, 2500000, -2500000]) == 5000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30]) == 0
    assert candidate(nums = [10000000, -10000000, 5000000, -5000000, 2500000, -2500000, 1250000, -1250000]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [2, -1, 0, 4, -2, -9]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40]) == 0
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(nums = [10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000, 10000000, -10000000]) == 0
    assert candidate(nums = [10000000, -10000000, 10000000, -10000000, 10000000, -10000000]) == 20000000
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 0
    assert candidate(nums = [-36, 36]) == 72
    assert candidate(nums = [-1, -2, -3, -4, -5, -6]) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == 0
    assert candidate(nums = [-1000, 1000, -1500, 1500, -2000, 2000, -2500, 2500, -3000, 3000, -3500, 3500, -4000, 4000, -4500, 4500]) == 0
    assert candidate(nums = [987654, -987654, 876543, -876543, 765432, -765432, 654321, -654321, 543210, -543210, 432109, -432109, 321098, -321098, 210987, -210987]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
    assert candidate(nums = [1000000, -1000000, 500000, -500000, 250000, -250000, 125000, -125000, 62500, -62500, 31250, -31250, 15625, -15625, 7812, -7812]) == 0
    assert candidate(nums = [5, -5, 15, -15, 25, -25, 35, -35, 45, -45, 55, -55, 65, -65, 75, -75]) == 0
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800]) == 0
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(nums = [1234567, -7654321, 8901234, -4321098, 5678901, -1234567, 8765432, -2345678, 9876543, -3456789, 4567890, -5678901, 6789012, -6789012, 7890123, -7890123]) == 7307
    assert candidate(nums = [1000000, -1000000, 2000000, -2000000, 3000000, -3000000, 4000000, -4000000, 5000000, -5000000, 6000000, -6000000, 7000000, -7000000, 8000000, -8000000]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
    assert candidate(nums = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, -10000000, -10000000, -10000000, -10000000, -10000000, -10000000]) == 0
    assert candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 0
    assert candidate(nums = [-9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2]) == 0
    assert candidate(nums = [-1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000, -6000, 6000, -7000, 7000, -8000, 8000]) == 0
    assert candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 0
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [12345, -12345, 67890, -67890, 11111, -11111, 22222, -22222, 33333, -33333, 44444, -44444, 55555, -55555, 66666, -66666]) == 0
    assert candidate(nums = [123, 456, 789, -123, -456, -789, 321, 654, 987, -321, -654, -987, 234, 567, 890, -234, -567, -890]) == 4
    assert candidate(nums = [10000000, -10000000, 20000000, -20000000, 30000000, -30000000, 40000000, -40000000, 50000000, -50000000, 60000000, -60000000, 70000000, -70000000, 80000000, -80000000]) == 0
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 0
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == 0
    assert candidate(nums = [-10000, 10000, -20000, 20000, -30000, 30000, -40000, 40000, -50000, 50000, -60000, 60000, -70000, 70000, -80000, 80000]) == 0
    assert candidate(nums = [5, 2, 9, 11, 15, 18, 3, 7, 14, 6, 10, 4, 8, 13, 1, 12]) == 0
    assert candidate(nums = [100000, -100000, 200000, -200000, 300000, -300000, 400000, -400000, 500000, -500000, 600000, -600000, 700000, -700000, 800000, -800000]) == 0
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8]) == 0
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 0
    assert candidate(nums = [-100, -200, -300, -400, -500, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500]) == 100
    assert candidate(nums = [9999999, -9999999, 4999999, -4999999, 2499999, -2499999, 1249999, -1249999, 624999, -624999, 312499, -312499, 156249, -156249, 78124, -78124]) == 0
    assert candidate(nums = [1000, -500, 2000, -1500, 3000, -2500, 4000, -3500, 5000, -4500, 6000, -5500, 7000, -6500, 8000, -7500]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 0
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 0
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15]) == 0
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80]) == 0
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500, -1600]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == 0
    assert candidate(nums = [1000000, -1000000, 500000, -500000, 250000, -250000, 750000, -750000, 375000, -375000, 187500, -187500, 937500, -937500, 468750, -468750]) == 0
    assert candidate(nums = [-7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0
    assert candidate(nums = [100, 200, 300, 400, -500, 600, -700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500, 1600]) == 0
    assert candidate(nums = [-5, 5, -10, 10, -15, 15, -20, 20, -25, 25, -30, 30, -35, 35, -40, 40]) == 0
    assert candidate(nums = [-100, 100, -200, 200, -300, 300, -400, 400, -500, 500, -600, 600, -700, 700, -800, 800]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 0
    assert candidate(nums = [-5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50, -60, 60, -70, 70, -80, 80]) == 0
    assert candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 33, 55, 77, 99, 22, 44]) == 3
    assert candidate(nums = [10000000, 9000000, 8000000, 7000000, 6000000, 5000000, 4000000, 3000000, 2000000, 1000000, 0, -1000000, -2000000, -3000000, -4000000, -5000000]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000]) == 0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [10000000, -9999999, 9999998, -9999997, 9999996, -9999995, 9999994, -9999993, 9999992, -9999991, 9999990, -9999989, 9999988, -9999987, 9999986, -9999985]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 99999
    assert candidate(nums = [9999999, -9999999, 8888888, -8888888, 7777777, -7777777, 6666666, -6666666, 5555555, -5555555, 4444444, -4444444, 3333333, -3333333, 2222222, -2222222]) == 0
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]) == 0
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 0
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]) == 0
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums = [5, 3, 8, 1, 9, 2, 6, 4, 7, 0, 11, 13, 15, 17, 19, 21]) == 1
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 0
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000, 11000000, 12000000, 13000000, 14000000, 15000000, 16000000]) == 0
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16]) == 0


