def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]) == 258365767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]) == 258365767: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 2, 2]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 2, 2]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 896
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 896: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 3, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 3, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4]) == 3360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4]) == 3360: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 2, 2]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 2, 2]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12]) == 645120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12]) == 645120: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 203434154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 203434154: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]) == 37717233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]) == 37717233: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]) == 118354482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]) == 118354482: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 977384288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 977384288: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 1, 4, 2, 6, 5, 7, 5, 9, 8, 10, 9, 11, 12, 13, 14, 10]) == 245044800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 1, 4, 2, 6, 5, 7, 5, 9, 8, 10, 9, 11, 12, 13, 14, 10]) == 245044800: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]) == 645247453
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]) == 645247453: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 2, 2, 1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 466985999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 2, 2, 1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 466985999: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 0, 2, 3, 4, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 11, 12]) == 777509735
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 0, 2, 3, 4, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 11, 12]) == 777509735: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 960269310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 960269310: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12]) == 270200339
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12]) == 270200339: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 815328371
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 815328371: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39]) == 558903913
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39]) == 558903913: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 2, 1, 3, 4, 3, 5, 6, 7, 5, 8, 9, 10, 11, 12, 11, 13, 14, 15, 16, 17, 18]) == 574577861
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 2, 1, 3, 4, 3, 5, 6, 7, 5, 8, 9, 10, 11, 12, 11, 13, 14, 15, 16, 17, 18]) == 574577861: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == 594293086
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == 594293086: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 65279563
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 65279563: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 258365767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 258365767: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]) == 916824814
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]) == 916824814: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]) == 499858301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]) == 499858301: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 144195955
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 144195955: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17]) == 977718734
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17]) == 977718734: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 927211300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 927211300: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 214454105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 214454105: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 881663664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 881663664: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]) == 182996126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]) == 182996126: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 904828424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 904828424: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 19170323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 19170323: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 232266423
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 232266423: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]) == 281601700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]) == 281601700: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 134837072
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 134837072: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35]) == 151296514
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35]) == 151296514: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == 580542770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == 580542770: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 374254273
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 374254273: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 506880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 506880: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 4036032
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 4036032: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 457389881
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 457389881: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 862785756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 862785756: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 259495482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 259495482: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39]) == 104533170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39]) == 104533170: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29]) == 944857254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29]) == 944857254: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 185834123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 185834123: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 3, 0, 5, 6, 7, 8, 4, 11, 12, 13, 14, 10, 16, 17, 18, 19]) == 462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 3, 0, 5, 6, 7, 8, 4, 11, 12, 13, 14, 10, 16, 17, 18, 19]) == 462: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 686400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 686400: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12]) == 846964197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12]) == 846964197: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12]) == 839553459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12]) == 839553459: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]) == 864359005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]) == 864359005: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 0, 2, 3, 2, 4, 5, 6, 5, 7, 8, 9, 10, 11, 10, 11, 12, 13, 14, 15, 14, 15, 16, 17, 18, 19, 20]) == 696057029
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 0, 2, 3, 2, 4, 5, 6, 5, 7, 8, 9, 10, 11, 10, 11, 12, 13, 14, 15, 14, 15, 16, 17, 18, 19, 20]) == 696057029: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]) == 495153778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]) == 495153778: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 1, 4, 5, 6, 4, 8, 9, 5, 10, 11, 6, 12, 13, 7, 14, 15, 8, 16, 17, 9, 18, 19]) == 298444100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 1, 4, 5, 6, 4, 8, 9, 5, 10, 11, 6, 12, 13, 7, 14, 15, 8, 16, 17, 9, 18, 19]) == 298444100: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 980653881
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 980653881: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 185998261
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 185998261: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 820019200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 820019200: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 316920121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 316920121: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 645414306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 645414306: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]) == 989258543
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]) == 989258543: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 414301485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 414301485: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7]) == 452706138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7]) == 452706138: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == 37717233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == 37717233: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 185998261
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 185998261: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34]) == 764478009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34]) == 764478009: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]) == 874133999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]) == 874133999: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 838387635
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 838387635: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 544962428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 544962428: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 268444119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 268444119: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 435629637
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 435629637: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11]) == 59583424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11]) == 59583424: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29]) == 468972288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29]) == 468972288: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 0, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 930392109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 0, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 930392109: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 466985999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 466985999: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 17, 17, 17, 17]) == 715654985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 17, 17, 17, 17]) == 715654985: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]) == 199114634
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]) == 199114634: {e}')
    
    total += 1
    try:
        result = candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]) == 258365767
    assert candidate(prevRoom = [-1, 0, 1, 1, 2, 2]) == 8
    assert candidate(prevRoom = [-1, 0, 0, 1, 2]) == 6
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2]) == 80
    assert candidate(prevRoom = [-1, 0, 1]) == 1
    assert candidate(prevRoom = [-1, 0, 0, 0]) == 6
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 2, 2]) == 120
    assert candidate(prevRoom = [-1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 896
    assert candidate(prevRoom = [-1, 0, 1, 2, 3, 4]) == 1
    assert candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4]) == 3360
    assert candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == 1
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 2, 2]) == 560
    assert candidate(prevRoom = [-1, 0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12]) == 645120
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 203434154
    assert candidate(prevRoom = [-1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]) == 37717233
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]) == 118354482
    assert candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14]) == 2
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 977384288
    assert candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 1
    assert candidate(prevRoom = [-1, 0, 1, 2, 1, 4, 2, 6, 5, 7, 5, 9, 8, 10, 9, 11, 12, 13, 14, 10]) == 245044800
    assert candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]) == 645247453
    assert candidate(prevRoom = [-1, 0, 0, 2, 2, 1, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 466985999
    assert candidate(prevRoom = [-1, 0, 1, 2, 0, 2, 3, 4, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 11, 12]) == 777509735
    assert candidate(prevRoom = [-1, 0, 0, 1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 960269310
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12]) == 270200339
    assert candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 815328371
    assert candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39]) == 558903913
    assert candidate(prevRoom = [-1, 0, 0, 1, 2, 1, 3, 4, 3, 5, 6, 7, 5, 8, 9, 10, 11, 12, 11, 13, 14, 15, 16, 17, 18]) == 574577861
    assert candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 1
    assert candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == 594293086
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 65279563
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 258365767
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]) == 916824814
    assert candidate(prevRoom = [-1, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]) == 499858301
    assert candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 144195955
    assert candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17]) == 977718734
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 927211300
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 214454105
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 881663664
    assert candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]) == 182996126
    assert candidate(prevRoom = [-1, 0, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]) == 904828424
    assert candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == 19170323
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 232266423
    assert candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]) == 281601700
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 134837072
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35]) == 151296514
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == 580542770
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 374254273
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 506880
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 4036032
    assert candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 457389881
    assert candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 862785756
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 259495482
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39]) == 104533170
    assert candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29]) == 944857254
    assert candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 185834123
    assert candidate(prevRoom = [-1, 0, 1, 2, 3, 0, 5, 6, 7, 8, 4, 11, 12, 13, 14, 10, 16, 17, 18, 19]) == 462
    assert candidate(prevRoom = [-1, 0, 0, 1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 686400
    assert candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12]) == 846964197
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12]) == 839553459
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]) == 864359005
    assert candidate(prevRoom = [-1, 0, 1, 0, 2, 3, 2, 4, 5, 6, 5, 7, 8, 9, 10, 11, 10, 11, 12, 13, 14, 15, 14, 15, 16, 17, 18, 19, 20]) == 696057029
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]) == 495153778
    assert candidate(prevRoom = [-1, 0, 1, 2, 1, 4, 5, 6, 4, 8, 9, 5, 10, 11, 6, 12, 13, 7, 14, 15, 8, 16, 17, 9, 18, 19]) == 298444100
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 980653881
    assert candidate(prevRoom = [-1, 0, 1, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 185998261
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 820019200
    assert candidate(prevRoom = [-1, 0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 316920121
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 645414306
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]) == 989258543
    assert candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 414301485
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7]) == 452706138
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == 37717233
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 185998261
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34]) == 764478009
    assert candidate(prevRoom = [-1, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]) == 874133999
    assert candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 838387635
    assert candidate(prevRoom = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 544962428
    assert candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 268444119
    assert candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == 1
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 435629637
    assert candidate(prevRoom = [-1, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11]) == 59583424
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29]) == 468972288
    assert candidate(prevRoom = [-1, 0, 1, 0, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 930392109
    assert candidate(prevRoom = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 466985999
    assert candidate(prevRoom = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 17, 17, 17, 17]) == 715654985
    assert candidate(prevRoom = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]) == 199114634
    assert candidate(prevRoom = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 1


