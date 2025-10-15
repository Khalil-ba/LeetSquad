def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(satisfaction = [1, -1, 2, -2, 3, -3]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, -1, 2, -2, 3, -3]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-500, -500, -500, -500, -500]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-500, -500, -500, -500, -500]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1000, 1000, -500, 500]) == 3500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1000, 1000, -500, 500]) == 3500: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1000, -1000, 1000, -1000, 1000]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1000, -1000, 1000, -1000, 1000]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -8, 0, 5, -9]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -8, 0, 5, -9]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-10, -20, -30, 10, 20, 30]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-10, -20, -30, 10, 20, 30]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, 2, 3, 4, 5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, 2, 3, 4, 5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [100, 200, 300, 400, 500]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [100, 200, 300, 400, 500]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-10, -20, -30, -40, -50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-10, -20, -30, -40, -50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [4, 3, 2]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [4, 3, 2]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [500, 500, 500, 500, 500]) == 7500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [500, 500, 500, 500, 500]) == 7500: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1000, 1000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1000, 1000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -4, -5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -4, -5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-5, -4, -3, -2, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-5, -4, -3, -2, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-500, -400, -300, -200, -100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-500, -400, -300, -200, -100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1000, -1000, 1000, -1000, 1000]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1000, -1000, 1000, -1000, 1000]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, 1, -2, 2, -3, 3]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, 1, -2, 2, -3, 3]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1000, -1000, 1000, -1000]) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1000, -1000, 1000, -1000]) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [5, -1, 3, 2, -2, 1]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [5, -1, 3, 2, -2, 1]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [10, 9, 8, 7, 6, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 415
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [10, 9, 8, 7, 6, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 415: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [100, -90, 50, -40, 30, -20, 10, -5, 0]) == 1320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [100, -90, 50, -40, 30, -20, 10, -5, 0]) == 1320: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 13600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 13600: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 715
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 715: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-500, -499, -498, -497, -496, -495, -494, -493, -492, -491, -490, -489, -488, -487, -486]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-500, -499, -498, -497, -496, -495, -494, -493, -492, -491, -490, -489, -488, -487, -486]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [999, -999, 998, -998, 997, -997, 996, -996, 995, -995]) == 24945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [999, -999, 998, -998, 997, -997, 996, -996, 995, -995]) == 24945: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [999, 1000, 998, -1000, 500, 499, 501, -499, -501, 0, 1, -1, 2, -2, 3, -3]) == 59488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [999, 1000, 998, -1000, 500, 499, 501, -499, -501, 0, 1, -1, 2, -2, 3, -3]) == 59488: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == 525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == 525: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -2, -3, 4, 5, 6, 7, 8]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -2, -3, 4, 5, 6, 7, 8]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 1, 2, 3, 4, 5]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 1, 2, 3, 4, 5]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 625: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 625: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-500, -400, -300, -200, -100, 100, 200, 300, 400, 500]) == 9500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-500, -400, -300, -200, -100, 100, 200, 300, 400, 500]) == 9500: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-10, 0, 10, -20, 0, 20, -30, 0, 30, -40]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-10, 0, 10, -20, 0, 20, -30, 0, 30, -40]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50, 60, 70, 80, 90, 100]) == 6250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50, 60, 70, 80, 90, 100]) == 6250: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-500, 500, -250, 250, 0, 100, -100, 150]) == 5850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-500, 500, -250, 250, 0, 100, -100, 150]) == 5850: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 570: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 950: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 229460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 229460: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-100, -200, -300, 50, 100, 150, 200, 250]) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-100, -200, -300, 50, 100, 150, 200, 250]) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [50, 20, -10, 0, -30, 100, -200, 300, -400, 500]) == 8040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [50, 20, -10, 0, -30, 100, -200, 300, -400, 500]) == 8040: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-100, -200, -300, -400, 100, 200, 300, 400, 500]) == 9500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-100, -200, -300, -400, 100, 200, 300, 400, 500]) == 9500: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486]) == 59440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486]) == 59440: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [500, -1, -2, -3, 0, 1, 2, 3, 4, 5]) == 5105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [500, -1, -2, -3, 0, 1, 2, 3, 4, 5]) == 5105: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-999, -998, -997, -996, 999, 998, 997, 996]) == 15970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-999, -998, -997, -996, 999, 998, 997, 996]) == 15970: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [5, -5, 15, -15, 25, -25, 35, -35]) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [5, -5, 15, -15, 25, -25, 35, -35]) == 420: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [5, -1, 3, -2, 4, -3, 2]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [5, -1, 3, -2, 4, -3, 2]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-100, 0, 100, -200, 200, -300, 300, -400, 400, -500, 500]) == 11000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-100, 0, 100, -200, 200, -300, 300, -400, 400, -500, 500]) == 11000: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [999, 1000, -999, -1000, 998, 997, -998, -997, 996, -996]) == 24970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [999, 1000, -999, -1000, 998, 997, -998, -997, 996, -996]) == 24970: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [10, -1, 2, 5, -7, 8, -2]) == 137
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [10, -1, 2, 5, -7, 8, -2]) == 137: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-5, -2, 0, 1, 3, 6]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-5, -2, 0, 1, 3, 6]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, -1, -2, -3, -4, -5]) == 6565
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, -1, -2, -3, -4, -5]) == 6565: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-500, 500, -499, 499, -498, 498, -497, 497, -496, 496]) == 12470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-500, 500, -499, 499, -498, 498, -497, 497, -496, 496]) == 12470: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [9, -1, -2, 3, -4, 5, -6, 7, -8, 9]) == 235
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [9, -1, -2, 3, -4, 5, -6, 7, -8, 9]) == 235: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 950: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 625: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-5, -3, -2, 1, 4, 6]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-5, -3, -2, 1, 4, 6]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 3850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 3850: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [900, 100, 200, -900, 50, -50, 300, -300, 400, -400]) == 14450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [900, 100, 200, -900, 50, -50, 300, -300, 400, -400]) == 14450: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 950: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-100, -200, -300, -400, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-100, -200, -300, -400, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 161: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-999, -998, -997, -996, -995, 995, 996, 997, 998, 999]) == 24945
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-999, -998, -997, -996, -995, 995, 996, 997, 998, 999]) == 24945: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, 0, 1, -2, 0, 2, -3, 0, 3]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, 0, 1, -2, 0, 2, -3, 0, 3]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-5, -3, -1, 1, 3, 5]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-5, -3, -1, 1, 3, 5]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-50, -50, 50, 50, -25, -25, 25, 25, -75, 75]) == 1375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-50, -50, 50, 50, -25, -25, 25, 25, -75, 75]) == 1375: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-10, -20, -30, -40, -50, 5, 15, 25, 35, 45]) == 775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-10, -20, -30, -40, -50, 5, 15, 25, 35, 45]) == 775: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-9, -8, -7, -6, -5, 1, 2, 3, 4, 5]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-9, -8, -7, -6, -5, 1, 2, 3, 4, 5]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-100, -200, -300, 100, 200, 300, 400, 500]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-100, -200, -300, 100, 200, 300, 400, 500]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 295: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-100, -90, -80, 70, 80, 90, 100]) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-100, -90, -80, 70, 80, 90, 100]) == 1400: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [50, 100, 150, 200, -10, -20, -30, -40, -50, -60]) == 3940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [50, 100, 150, 200, -10, -20, -30, -40, -50, -60]) == 3940: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 715
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 715: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [100, 100, 100, -1, -1, -1, -1, -1, -1, -1]) == 2672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [100, 100, 100, -1, -1, -1, -1, -1, -1, -1]) == 2672: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1000, 1000, -999, 999, -998, 998, -997, 997, -996, 996, -995, 995, -994, 994]) == 48909
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1000, 1000, -999, 999, -998, 998, -997, 997, -996, 996, -995, 995, -994, 994]) == 48909: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, -2, -3, 4, 5, 6]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, -2, -3, 4, 5, 6]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 780
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 780: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-500, 500, -400, 400, -300, 300, -200, 200, -100, 100]) == 9500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-500, 500, -400, 400, -300, 300, -200, 200, -100, 100]) == 9500: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [500, -500, 250, -250, 125, -125, 62, -62, 31, -31]) == 7092
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [500, -500, 250, -250, 125, -125, 62, -62, 31, -31]) == 7092: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-1000, -500, 0, 500, 1000, 1500, 2000]) == 28000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-1000, -500, 0, 500, 1000, 1500, 2000]) == 28000: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [5, 1, 3, 7, -5, -3, 2, 6, -2, 4]) == 207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [5, 1, 3, 7, -5, -3, 2, 6, -2, 4]) == 207: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-999, -998, -997, -996, 996, 997, 998, 999]) == 15970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-999, -998, -997, -996, 996, 997, 998, 999]) == 15970: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-999, 999, -998, 998, -997, 997, -996, 996, -995, 995, -994, 994, -993, 993, -992, 992]) == 63796
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-999, 999, -998, 998, -997, 997, -996, 996, -995, 995, -994, 994, -993, 993, -992, 992]) == 63796: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [500, -500, 400, -400, 300, -300, 200, -200, 100, -100, 0]) == 11000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [500, -500, 400, -400, 300, -300, 200, -200, 100, -100, 0]) == 11000: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-5, -3, -1, 2, 4, 6]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-5, -3, -1, 2, 4, 6]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [-999, -1000, 1000, 999, -998, 998, 0, 0, 0, 0, 0]) == 23980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [-999, -1000, 1000, 999, -998, 998, 0, 0, 0, 0, 0]) == 23980: {e}')
    
    total += 1
    try:
        result = candidate(satisfaction = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(satisfaction = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1240: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(satisfaction = [1, -1, 2, -2, 3, -3]) == 22
    assert candidate(satisfaction = [0]) == 0
    assert candidate(satisfaction = [-1]) == 0
    assert candidate(satisfaction = [-500, -500, -500, -500, -500]) == 0
    assert candidate(satisfaction = [0, 0, 0, 0, 0]) == 0
    assert candidate(satisfaction = [-1000, 1000, -500, 500]) == 3500
    assert candidate(satisfaction = [0, 0, 0, 0]) == 0
    assert candidate(satisfaction = [1000, -1000, 1000, -1000, 1000]) == 9000
    assert candidate(satisfaction = [-1, -8, 0, 5, -9]) == 14
    assert candidate(satisfaction = [-10, -20, -30, 10, 20, 30]) == 220
    assert candidate(satisfaction = [1, 2, 3, 4, 5]) == 55
    assert candidate(satisfaction = [100, 200, 300, 400, 500]) == 5500
    assert candidate(satisfaction = [-10, -20, -30, -40, -50]) == 0
    assert candidate(satisfaction = [4, 3, 2]) == 20
    assert candidate(satisfaction = [500, 500, 500, 500, 500]) == 7500
    assert candidate(satisfaction = [-1000, 1000]) == 1000
    assert candidate(satisfaction = [-1, -4, -5]) == 0
    assert candidate(satisfaction = [-5, -4, -3, -2, -1]) == 0
    assert candidate(satisfaction = [-500, -400, -300, -200, -100]) == 0
    assert candidate(satisfaction = [1000, -1000, 1000, -1000, 1000]) == 9000
    assert candidate(satisfaction = [1]) == 1
    assert candidate(satisfaction = [-1, 1, -2, 2, -3, 3]) == 22
    assert candidate(satisfaction = [1000, -1000, 1000, -1000]) == 4000
    assert candidate(satisfaction = [5, -1, 3, 2, -2, 1]) == 52
    assert candidate(satisfaction = [10, 9, 8, 7, 6, 5, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 415
    assert candidate(satisfaction = [100, -90, 50, -40, 30, -20, 10, -5, 0]) == 1320
    assert candidate(satisfaction = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 13600
    assert candidate(satisfaction = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 715
    assert candidate(satisfaction = [-500, -499, -498, -497, -496, -495, -494, -493, -492, -491, -490, -489, -488, -487, -486]) == 0
    assert candidate(satisfaction = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 155
    assert candidate(satisfaction = [999, -999, 998, -998, 997, -997, 996, -996, 995, -995]) == 24945
    assert candidate(satisfaction = [999, 1000, 998, -1000, 500, 499, 501, -499, -501, 0, 1, -1, 2, -2, 3, -3]) == 59488
    assert candidate(satisfaction = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == 525
    assert candidate(satisfaction = [-1, -2, -3, 4, 5, 6, 7, 8]) == 180
    assert candidate(satisfaction = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 110
    assert candidate(satisfaction = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 1, 2, 3, 4, 5]) == 60
    assert candidate(satisfaction = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 625
    assert candidate(satisfaction = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 625
    assert candidate(satisfaction = [-500, -400, -300, -200, -100, 100, 200, 300, 400, 500]) == 9500
    assert candidate(satisfaction = [-10, 0, 10, -20, 0, 20, -30, 0, 30, -40]) == 400
    assert candidate(satisfaction = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50, 60, 70, 80, 90, 100]) == 6250
    assert candidate(satisfaction = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(satisfaction = [-500, 500, -250, 250, 0, 100, -100, 150]) == 5850
    assert candidate(satisfaction = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 95
    assert candidate(satisfaction = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 570
    assert candidate(satisfaction = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 950
    assert candidate(satisfaction = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 229460
    assert candidate(satisfaction = [-100, -200, -300, 50, 100, 150, 200, 250]) == 4000
    assert candidate(satisfaction = [50, 20, -10, 0, -30, 100, -200, 300, -400, 500]) == 8040
    assert candidate(satisfaction = [-100, -200, -300, -400, 100, 200, 300, 400, 500]) == 9500
    assert candidate(satisfaction = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]) == 110
    assert candidate(satisfaction = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486]) == 59440
    assert candidate(satisfaction = [500, -1, -2, -3, 0, 1, 2, 3, 4, 5]) == 5105
    assert candidate(satisfaction = [-999, -998, -997, -996, 999, 998, 997, 996]) == 15970
    assert candidate(satisfaction = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 95
    assert candidate(satisfaction = [5, -5, 15, -15, 25, -25, 35, -35]) == 420
    assert candidate(satisfaction = [5, -1, 3, -2, 4, -3, 2]) == 72
    assert candidate(satisfaction = [-100, 0, 100, -200, 200, -300, 300, -400, 400, -500, 500]) == 11000
    assert candidate(satisfaction = [999, 1000, -999, -1000, 998, 997, -998, -997, 996, -996]) == 24970
    assert candidate(satisfaction = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10]) == 0
    assert candidate(satisfaction = [10, -1, 2, 5, -7, 8, -2]) == 137
    assert candidate(satisfaction = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 100
    assert candidate(satisfaction = [-5, -2, 0, 1, 3, 6]) == 46
    assert candidate(satisfaction = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, -1, -2, -3, -4, -5]) == 6565
    assert candidate(satisfaction = [-1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1]) == 36
    assert candidate(satisfaction = [-500, 500, -499, 499, -498, 498, -497, 497, -496, 496]) == 12470
    assert candidate(satisfaction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 100
    assert candidate(satisfaction = [9, -1, -2, 3, -4, 5, -6, 7, -8, 9]) == 235
    assert candidate(satisfaction = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 950
    assert candidate(satisfaction = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 625
    assert candidate(satisfaction = [-5, -3, -2, 1, 4, 6]) == 43
    assert candidate(satisfaction = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
    assert candidate(satisfaction = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 3850
    assert candidate(satisfaction = [900, 100, 200, -900, 50, -50, 300, -300, 400, -400]) == 14450
    assert candidate(satisfaction = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]) == 950
    assert candidate(satisfaction = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 95
    assert candidate(satisfaction = [-100, -200, -300, -400, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385
    assert candidate(satisfaction = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 161
    assert candidate(satisfaction = [-999, -998, -997, -996, -995, 995, 996, 997, 998, 999]) == 24945
    assert candidate(satisfaction = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) == 40
    assert candidate(satisfaction = [-1, 0, 1, -2, 0, 2, -3, 0, 3]) == 40
    assert candidate(satisfaction = [-5, -3, -1, 1, 3, 5]) == 35
    assert candidate(satisfaction = [-50, -50, 50, 50, -25, -25, 25, 25, -75, 75]) == 1375
    assert candidate(satisfaction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 465
    assert candidate(satisfaction = [-10, -20, -30, -40, -50, 5, 15, 25, 35, 45]) == 775
    assert candidate(satisfaction = [-9, -8, -7, -6, -5, 1, 2, 3, 4, 5]) == 69
    assert candidate(satisfaction = [-100, -200, -300, 100, 200, 300, 400, 500]) == 9000
    assert candidate(satisfaction = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]) == 295
    assert candidate(satisfaction = [-100, -90, -80, 70, 80, 90, 100]) == 1400
    assert candidate(satisfaction = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(satisfaction = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 110
    assert candidate(satisfaction = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385
    assert candidate(satisfaction = [50, 100, 150, 200, -10, -20, -30, -40, -50, -60]) == 3940
    assert candidate(satisfaction = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 715
    assert candidate(satisfaction = [100, 100, 100, -1, -1, -1, -1, -1, -1, -1]) == 2672
    assert candidate(satisfaction = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(satisfaction = [-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985, -984, -983, -982, -981, -980]) == 0
    assert candidate(satisfaction = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(satisfaction = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 0
    assert candidate(satisfaction = [-1000, 1000, -999, 999, -998, 998, -997, 997, -996, 996, -995, 995, -994, 994]) == 48909
    assert candidate(satisfaction = [-1, -2, -3, 4, 5, 6]) == 67
    assert candidate(satisfaction = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]) == 780
    assert candidate(satisfaction = [-500, 500, -400, 400, -300, 300, -200, 200, -100, 100]) == 9500
    assert candidate(satisfaction = [500, -500, 250, -250, 125, -125, 62, -62, 31, -31]) == 7092
    assert candidate(satisfaction = [-1000, -500, 0, 500, 1000, 1500, 2000]) == 28000
    assert candidate(satisfaction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
    assert candidate(satisfaction = [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100]) == 0
    assert candidate(satisfaction = [5, 1, 3, 7, -5, -3, 2, 6, -2, 4]) == 207
    assert candidate(satisfaction = [-999, -998, -997, -996, 996, 997, 998, 999]) == 15970
    assert candidate(satisfaction = [-999, 999, -998, 998, -997, 997, -996, 996, -995, 995, -994, 994, -993, 993, -992, 992]) == 63796
    assert candidate(satisfaction = [500, -500, 400, -400, 300, -300, 200, -200, 100, -100, 0]) == 11000
    assert candidate(satisfaction = [-5, -3, -1, 2, 4, 6]) == 50
    assert candidate(satisfaction = [-999, -1000, 1000, 999, -998, 998, 0, 0, 0, 0, 0]) == 23980
    assert candidate(satisfaction = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1240


