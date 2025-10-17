def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10, -10, 20, -20, 30, -30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10, -10, 20, -20, 30, -30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(stones = [100, 200, -300, 400, -500, 600, -700, 800]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [100, 200, -300, 400, -500, 600, -700, 800]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(stones = [100, -100, 100, -100, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [100, -100, 100, -100, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10, -10, 20, -20, 30, -30, 40, -40]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10, -10, 20, -20, 30, -30, 40, -40]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, -2, -3, -4, -5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, -2, -3, -4, -5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-10, -12]) == -22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-10, -12]) == -22: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-5, -4, -3, -2, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-5, -4, -3, -2, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [7, -6, 5, 10, 5, -2, -6]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [7, -6, 5, 10, 5, -2, -6]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, 2, -3, 4, -5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, 2, -3, 4, -5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(stones = [100, -50, 25, -12, 6, -3, 1, -1, 3, -2, 5, -4, 7, -6, 9]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [100, -50, 25, -12, 6, -3, 1, -1, 3, -2, 5, -4, 7, -6, 9]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-10000, 0, 10000, 0, -10000, 0, 10000, 0, -10000, 0, 10000, 0, -10000, 0, 10000, 0, -10000, 0, 10000, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-10000, 0, 10000, 0, -10000, 0, 10000, 0, -10000, 0, 10000, 0, -10000, 0, 10000, 0, -10000, 0, 10000, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, -10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, -10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 11055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 11055: {e}')
    
    total += 1
    try:
        result = candidate(stones = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(stones = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(stones = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(stones = [5, 10, -5, 20, -10, 25, -15, 30, -20, 35, -25, 40, -30, 45, -35, 50, -40, 55, -45, 60]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [5, 10, -5, 20, -10, 25, -15, 30, -20, 35, -25, 40, -30, 45, -35, 50, -40, 55, -45, 60]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-5, 15, -25, 35, -45, 55, -65, 75, -85, 95, -105]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-5, 15, -25, 35, -45, 55, -65, 75, -85, 95, -105]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stones = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0, -1, -3, -7, -15, -31]) == 1937
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0, -1, -3, -7, -15, -31]) == 1937: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10000, -10000, 9999, -9999, 9998, -9998, 9997, -9997, 9996, -9996]) == 9996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10000, -10000, 9999, -9999, 9998, -9998, 9997, -9997, 9996, -9996]) == 9996: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-10000, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-10000, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1000, -900, -800, -700, -600]) == 3100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1000, -900, -800, -700, -600]) == 3100: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10000, -5000, 2000, -1000, 500, -200, 100, -50, 20, -10]) == 6360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10000, -5000, 2000, -1000, 500, -200, 100, -50, 20, -10]) == 6360: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, -2, -4, -8, -16, -32, -64, -128, -256, -512, -1024, -2048, -4096, -8192, -16384, -32768, -65536, -131072, -262144, -524288]) == 524288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, -2, -4, -8, -16, -32, -64, -128, -256, -512, -1024, -2048, -4096, -8192, -16384, -32768, -65536, -131072, -262144, -524288]) == 524288: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10000, -5000, 5000, -2500, 2500, -1250, 1250, -625, 625, -312, 312, -156, 156, -78, 78, -39, 39, -19, 19, -9, 9]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10000, -5000, 5000, -2500, 2500, -1250, 1250, -625, 625, -312, 312, -156, 156, -78, 78, -39, 39, -19, 19, -9, 9]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(stones = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 550000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 550000: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10000, -9999, 9998, -9997, 9996, -9995, 9994, -9993, 9992, -9991, 9990]) == 9995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10000, -9999, 9998, -9997, 9996, -9995, 9994, -9993, 9992, -9991, 9990]) == 9995: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(stones = [5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30, 35, -35, 40, -40, 45, -45, 50, -50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30, 35, -35, 40, -40, 45, -45, 50, -50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(stones = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000, 1100, -1100, 1200, -1200]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000, 1100, -1100, 1200, -1200]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -10, 100, -1000, 10000, -100000, 1000000, -10000000, 100000000, -1000000000]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -10, 100, -1000, 10000, -100000, 1000000, -10000000, 100000000, -1000000000]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10000, -9999, 9998, -9997, 9996, -9995, 9994, -9993, 9992, -9991]) == 9991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10000, -9999, 9998, -9997, 9996, -9995, 9994, -9993, 9992, -9991]) == 9991: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(stones = [100, 200, -300, 400, -500, 600, -700, 800, -900, 1000]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [100, 200, -300, 400, -500, 600, -700, 800, -900, 1000]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048575: {e}')
    
    total += 1
    try:
        result = candidate(stones = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(stones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10000]) == 10014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10000]) == 10014: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(stones = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stones = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(stones = [10, -10, 20, -20, 30, -30]) == 30
    assert candidate(stones = [100, 200, -300, 400, -500, 600, -700, 800]) == 600
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 50
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(stones = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000]) == 0
    assert candidate(stones = [1, 2, 3, 4, 5]) == 15
    assert candidate(stones = [100, -100, 100, -100, 100]) == 100
    assert candidate(stones = [10, -10, 20, -20, 30, -30, 40, -40]) == 40
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(stones = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(stones = [-1, -2, -3, -4, -5]) == 5
    assert candidate(stones = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50
    assert candidate(stones = [-10, -12]) == -22
    assert candidate(stones = [-5, -4, -3, -2, -1]) == 1
    assert candidate(stones = [7, -6, 5, 10, 5, -2, -6]) == 13
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(stones = [-1, 2, -3, 4, -5]) == 5
    assert candidate(stones = [100, -50, 25, -12, 6, -3, 1, -1, 3, -2, 5, -4, 7, -6, 9]) == 78
    assert candidate(stones = [-10000, 0, 10000, 0, -10000, 0, 10000, 0, -10000, 0, 10000, 0, -10000, 0, 10000, 0, -10000, 0, 10000, 0]) == 0
    assert candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(stones = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1100, -1200, 1300, -1400, 1500]) == 800
    assert candidate(stones = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, -10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000]) == 30000
    assert candidate(stones = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 11055
    assert candidate(stones = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000]) == 1000
    assert candidate(stones = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 250
    assert candidate(stones = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000]) == 1000
    assert candidate(stones = [5, 10, -5, 20, -10, 25, -15, 30, -20, 35, -25, 40, -30, 45, -35, 50, -40, 55, -45, 60]) == 150
    assert candidate(stones = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(stones = [-5, 15, -25, 35, -45, 55, -65, 75, -85, 95, -105]) == 105
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 325
    assert candidate(stones = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 10
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(stones = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
    assert candidate(stones = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]) == 16
    assert candidate(stones = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]) == 10
    assert candidate(stones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(stones = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 10
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 1000
    assert candidate(stones = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0, -1, -3, -7, -15, -31]) == 1937
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(stones = [10000, -10000, 9999, -9999, 9998, -9998, 9997, -9997, 9996, -9996]) == 9996
    assert candidate(stones = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11]) == 11
    assert candidate(stones = [-10000, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1]) == -1
    assert candidate(stones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1000, -900, -800, -700, -600]) == 3100
    assert candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(stones = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 20
    assert candidate(stones = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 15
    assert candidate(stones = [10000, -5000, 2000, -1000, 500, -200, 100, -50, 20, -10]) == 6360
    assert candidate(stones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 28
    assert candidate(stones = [-1, -2, -4, -8, -16, -32, -64, -128, -256, -512, -1024, -2048, -4096, -8192, -16384, -32768, -65536, -131072, -262144, -524288]) == 524288
    assert candidate(stones = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 9
    assert candidate(stones = [10000, -5000, 5000, -2500, 2500, -1250, 1250, -625, 625, -312, 312, -156, 156, -78, 78, -39, 39, -19, 19, -9, 9]) == 10000
    assert candidate(stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(stones = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, 5]) == 10
    assert candidate(stones = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 550000
    assert candidate(stones = [10000, -9999, 9998, -9997, 9996, -9995, 9994, -9993, 9992, -9991, 9990]) == 9995
    assert candidate(stones = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 8
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1200
    assert candidate(stones = [5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30, 35, -35, 40, -40, 45, -45, 50, -50]) == 50
    assert candidate(stones = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000, 1100, -1100, 1200, -1200]) == 1200
    assert candidate(stones = [1, -10, 100, -1000, 10000, -100000, 1000000, -10000000, 100000000, -1000000000]) == 1000000000
    assert candidate(stones = [-150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 10
    assert candidate(stones = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10]) == 10
    assert candidate(stones = [10000, -9999, 9998, -9997, 9996, -9995, 9994, -9993, 9992, -9991]) == 9991
    assert candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(stones = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 0
    assert candidate(stones = [100, 200, -300, 400, -500, 600, -700, 800, -900, 1000]) == 700
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 300
    assert candidate(stones = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048575
    assert candidate(stones = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000]) == 10000
    assert candidate(stones = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1
    assert candidate(stones = [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1]) == 1
    assert candidate(stones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10000]) == 10014
    assert candidate(stones = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 20
    assert candidate(stones = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == 5


