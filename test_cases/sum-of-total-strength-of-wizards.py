def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(strength = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1, 1, 1, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1, 1, 1, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 9, 8, 7, 6]) == 1988
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 9, 8, 7, 6]) == 1988: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4576: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1000000000, 1000000000, 1000000000]) == 490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1000000000, 1000000000, 1000000000]) == 490: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 3, 1, 2, 4]) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 3, 1, 2, 4]) == 156: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5]) == 238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5]) == 238: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 6, 7, 8, 9, 10]) == 2688
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 6, 7, 8, 9, 10]) == 2688: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 4, 6]) == 213
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 4, 6]) == 213: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 10, 1, 10, 1, 10]) == 578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 10, 1, 10, 1, 10]) == 578: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 731
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 731: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 9, 8, 7, 6, 5]) == 2688
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 9, 8, 7, 6, 5]) == 2688: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4576: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 3, 1, 2]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 3, 1, 2]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1000000000, 1000000000]) == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1000000000, 1000000000]) == 196: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 2577
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 2577: {e}')
    
    total += 1
    try:
        result = candidate(strength = [100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100]) == 2600000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100]) == 2600000: {e}')
    
    total += 1
    try:
        result = candidate(strength = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 21824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 21824: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2330: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 4144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 4144: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 315315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 315315: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 22000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 22000: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 108290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 108290: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 760: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1540: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 4820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 4820: {e}')
    
    total += 1
    try:
        result = candidate(strength = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8712
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8712: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 5, 2, 5, 3, 5, 4, 5, 5, 5]) == 2232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 5, 2, 5, 3, 5, 4, 5, 5, 5]) == 2232: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 13042
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 13042: {e}')
    
    total += 1
    try:
        result = candidate(strength = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 457600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 457600: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 370373883
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 370373883: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 109802
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 109802: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 98736
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 98736: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2871
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2871: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2871
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2871: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 1660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 1660: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 20, 30, 40, 50]) == 23800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 20, 30, 40, 50]) == 23800: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38768: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000]) == 980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000]) == 980: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4576: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 370373883
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 370373883: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 3, 8, 6, 2, 7, 4, 9, 1]) == 1914
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 3, 8, 6, 2, 7, 4, 9, 1]) == 1914: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 14312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 14312: {e}')
    
    total += 1
    try:
        result = candidate(strength = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == 2684
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == 2684: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 2439
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 2439: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == 4200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == 4200: {e}')
    
    total += 1
    try:
        result = candidate(strength = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109802
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109802: {e}')
    
    total += 1
    try:
        result = candidate(strength = [2, 1, 3, 4, 2, 1, 3, 4, 2, 1]) == 638
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [2, 1, 3, 4, 2, 1, 3, 4, 2, 1]) == 638: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 268328687
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 268328687: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 457600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 457600: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 13552
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 13552: {e}')
    
    total += 1
    try:
        result = candidate(strength = [2, 1, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2]) == 3672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [2, 1, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2]) == 3672: {e}')
    
    total += 1
    try:
        result = candidate(strength = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 3193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 3193: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 1590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 1590: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2767600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2767600: {e}')
    
    total += 1
    try:
        result = candidate(strength = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 619372
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 619372: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 30778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 30778: {e}')
    
    total += 1
    try:
        result = candidate(strength = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1]) == 64317
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1]) == 64317: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10]) == 3448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10]) == 3448: {e}')
    
    total += 1
    try:
        result = candidate(strength = [2, 1, 2, 1, 2, 1, 2, 1, 2]) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [2, 1, 2, 1, 2, 1, 2, 1, 2]) == 260: {e}')
    
    total += 1
    try:
        result = candidate(strength = [35, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 35]) == 72275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [35, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 35]) == 72275: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 3178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 3178: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 268328687
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 268328687: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1715
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1715: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000]) == 980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000]) == 980: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1414
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1414: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2767600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2767600: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 15, 10, 20, 15, 25, 20, 30, 25, 35]) == 61475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 15, 10, 20, 15, 25, 20, 30, 25, 35]) == 61475: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]) == 301120400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]) == 301120400: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 457600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 457600: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 1013
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 1013: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1540: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 3150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 3150: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 20, 30, 20, 10, 10, 20, 30, 20, 10]) == 46200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 20, 30, 20, 10, 10, 20, 30, 20, 10]) == 46200: {e}')
    
    total += 1
    try:
        result = candidate(strength = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2871
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2871: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4576: {e}')
    
    total += 1
    try:
        result = candidate(strength = [3, 1, 2, 5, 4]) == 186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [3, 1, 2, 5, 4]) == 186: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 1, 3, 2, 4, 6, 8, 7, 9]) == 2155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 1, 3, 2, 4, 6, 8, 7, 9]) == 2155: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10780
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10780: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2876356
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2876356: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1000000000, 1, 1000000000, 1, 1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1000000000, 1, 1000000000, 1, 1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3676
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3676: {e}')
    
    total += 1
    try:
        result = candidate(strength = [100, 1, 200, 2, 300, 3, 400, 4, 500]) == 596592
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [100, 1, 200, 2, 300, 3, 400, 4, 500]) == 596592: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 109802
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 109802: {e}')
    
    total += 1
    try:
        result = candidate(strength = [50, 20, 30, 10, 40, 60, 70, 5, 80, 90]) == 115850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [50, 20, 30, 10, 40, 60, 70, 5, 80, 90]) == 115850: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 30778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 30778: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 28764
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 28764: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 926
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 926: {e}')
    
    total += 1
    try:
        result = candidate(strength = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28764
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28764: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 826
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 826: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 369
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 369: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 340: {e}')
    
    total += 1
    try:
        result = candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 6, 7, 8, 9, 10]) == 3083588
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 6, 7, 8, 9, 10]) == 3083588: {e}')
    
    total += 1
    try:
        result = candidate(strength = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2871
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2871: {e}')
    
    total += 1
    try:
        result = candidate(strength = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 3, 2, 4, 1, 5, 2, 6, 1, 7, 2, 8, 1, 9, 2, 10]) == 3648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 3, 2, 4, 1, 5, 2, 6, 1, 7, 2, 8, 1, 9, 2, 10]) == 3648: {e}')
    
    total += 1
    try:
        result = candidate(strength = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 1864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 1864: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 639
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 639: {e}')
    
    total += 1
    try:
        result = candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(strength = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strength = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1980: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(strength = [1]) == 1
    assert candidate(strength = [1, 1, 1, 1, 1]) == 35
    assert candidate(strength = [10, 9, 8, 7, 6]) == 1988
    assert candidate(strength = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4576
    assert candidate(strength = [5]) == 25
    assert candidate(strength = [1000000000, 1000000000, 1000000000]) == 490
    assert candidate(strength = [5, 3, 1, 2, 4]) == 156
    assert candidate(strength = [1, 2, 3, 4, 5]) == 238
    assert candidate(strength = [5, 6, 7, 8, 9, 10]) == 2688
    assert candidate(strength = [5, 4, 6]) == 213
    assert candidate(strength = [1, 10, 1, 10, 1, 10]) == 578
    assert candidate(strength = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 731
    assert candidate(strength = [10, 9, 8, 7, 6, 5]) == 2688
    assert candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4576
    assert candidate(strength = [1, 3, 1, 2]) == 44
    assert candidate(strength = [1000000000, 1000000000]) == 196
    assert candidate(strength = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 2577
    assert candidate(strength = [100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100]) == 2600000
    assert candidate(strength = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 21824
    assert candidate(strength = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2330
    assert candidate(strength = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 4144
    assert candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 315315
    assert candidate(strength = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 22000
    assert candidate(strength = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 108290
    assert candidate(strength = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 760
    assert candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1540
    assert candidate(strength = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 4820
    assert candidate(strength = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8712
    assert candidate(strength = [1, 5, 2, 5, 3, 5, 4, 5, 5, 5]) == 2232
    assert candidate(strength = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 13042
    assert candidate(strength = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 457600
    assert candidate(strength = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 370373883
    assert candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 109802
    assert candidate(strength = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 98736
    assert candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2871
    assert candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2871
    assert candidate(strength = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 1660
    assert candidate(strength = [10, 20, 30, 40, 50]) == 23800
    assert candidate(strength = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38768
    assert candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000]) == 980
    assert candidate(strength = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4576
    assert candidate(strength = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111]) == 370373883
    assert candidate(strength = [5, 3, 8, 6, 2, 7, 4, 9, 1]) == 1914
    assert candidate(strength = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 14312
    assert candidate(strength = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == 2684
    assert candidate(strength = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 2439
    assert candidate(strength = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == 4200
    assert candidate(strength = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109802
    assert candidate(strength = [2, 1, 3, 4, 2, 1, 3, 4, 2, 1]) == 638
    assert candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 165
    assert candidate(strength = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 268328687
    assert candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 457600
    assert candidate(strength = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 13552
    assert candidate(strength = [2, 1, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2]) == 3672
    assert candidate(strength = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 3193
    assert candidate(strength = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 1590
    assert candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2767600
    assert candidate(strength = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == 619372
    assert candidate(strength = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 30778
    assert candidate(strength = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1]) == 64317
    assert candidate(strength = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10]) == 3448
    assert candidate(strength = [2, 1, 2, 1, 2, 1, 2, 1, 2]) == 260
    assert candidate(strength = [35, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 35]) == 72275
    assert candidate(strength = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 3178
    assert candidate(strength = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 268328687
    assert candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1715
    assert candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000]) == 980
    assert candidate(strength = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1414
    assert candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2767600
    assert candidate(strength = [10, 15, 10, 20, 15, 25, 20, 30, 25, 35]) == 61475
    assert candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]) == 301120400
    assert candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 457600
    assert candidate(strength = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 1013
    assert candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1540
    assert candidate(strength = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 3150
    assert candidate(strength = [10, 20, 30, 20, 10, 10, 20, 30, 20, 10]) == 46200
    assert candidate(strength = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2871
    assert candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4576
    assert candidate(strength = [3, 1, 2, 5, 4]) == 186
    assert candidate(strength = [5, 1, 3, 2, 4, 6, 8, 7, 9]) == 2155
    assert candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 220
    assert candidate(strength = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 10780
    assert candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2876356
    assert candidate(strength = [1, 1000000000, 1, 1000000000, 1, 1000000000]) == 0
    assert candidate(strength = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 3676
    assert candidate(strength = [100, 1, 200, 2, 300, 3, 400, 4, 500]) == 596592
    assert candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 109802
    assert candidate(strength = [50, 20, 30, 10, 40, 60, 70, 5, 80, 90]) == 115850
    assert candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 220
    assert candidate(strength = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 30778
    assert candidate(strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 28764
    assert candidate(strength = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 926
    assert candidate(strength = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28764
    assert candidate(strength = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 826
    assert candidate(strength = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 369
    assert candidate(strength = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 340
    assert candidate(strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 6, 7, 8, 9, 10]) == 3083588
    assert candidate(strength = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2871
    assert candidate(strength = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5500
    assert candidate(strength = [1, 3, 2, 4, 1, 5, 2, 6, 1, 7, 2, 8, 1, 9, 2, 10]) == 3648
    assert candidate(strength = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 1864
    assert candidate(strength = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 639
    assert candidate(strength = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 165
    assert candidate(strength = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1980


