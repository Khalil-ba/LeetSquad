def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 2020) == 2002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2020) == 2002: {e}')
    
    total += 1
    try:
        result = candidate(num = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = -10000000000) == -10000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -10000000000) == -10000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 10000000000) == 10000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000000000) == 10000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 10001) == 10001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10001) == 10001: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 123456789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 123456789: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543210) == 1023456789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543210) == 1023456789: {e}')
    
    total += 1
    try:
        result = candidate(num = 310) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 310) == 103: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(num = -10001) == -11000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -10001) == -11000: {e}')
    
    total += 1
    try:
        result = candidate(num = -9876543210) == -9876543210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -9876543210) == -9876543210: {e}')
    
    total += 1
    try:
        result = candidate(num = 1001) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1001) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 123456789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 123456789: {e}')
    
    total += 1
    try:
        result = candidate(num = -100) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -100) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = -7605) == -7650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -7605) == -7650: {e}')
    
    total += 1
    try:
        result = candidate(num = -1001) == -1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1001) == -1100: {e}')
    
    total += 1
    try:
        result = candidate(num = -123456789) == -987654321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -123456789) == -987654321: {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num = -12345) == -54321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -12345) == -54321: {e}')
    
    total += 1
    try:
        result = candidate(num = 54321) == 12345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 54321) == 12345: {e}')
    
    total += 1
    try:
        result = candidate(num = -10) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -10) == -10: {e}')
    
    total += 1
    try:
        result = candidate(num = -900) == -900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -900) == -900: {e}')
    
    total += 1
    try:
        result = candidate(num = 20001002003004005) == 10000000000022345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 20001002003004005) == 10000000000022345: {e}')
    
    total += 1
    try:
        result = candidate(num = -600500400300201) == -654321000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -600500400300201) == -654321000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 3000000000000000000) == 3000000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3000000000000000000) == 3000000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -999999999) == -999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -999999999) == -999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101010101) == 100000001111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101010101) == 100000001111111: {e}')
    
    total += 1
    try:
        result = candidate(num = 505050505050505) == 500000005555555
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 505050505050505) == 500000005555555: {e}')
    
    total += 1
    try:
        result = candidate(num = -123456789012345) == -987655443322110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -123456789012345) == -987655443322110: {e}')
    
    total += 1
    try:
        result = candidate(num = -1230456) == -6543210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1230456) == -6543210: {e}')
    
    total += 1
    try:
        result = candidate(num = 2100000000000000) == 1000000000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2100000000000000) == 1000000000000002: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -202020202020202) == -222222220000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -202020202020202) == -222222220000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 213004005) == 100002345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 213004005) == 100002345: {e}')
    
    total += 1
    try:
        result = candidate(num = -999999999999999) == -999999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -999999999999999) == -999999999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = -987654321012345) == -987655443322110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -987654321012345) == -987655443322110: {e}')
    
    total += 1
    try:
        result = candidate(num = -543210000) == -543210000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -543210000) == -543210000: {e}')
    
    total += 1
    try:
        result = candidate(num = -12000210) == -22110000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -12000210) == -22110000: {e}')
    
    total += 1
    try:
        result = candidate(num = -99999999999999) == -99999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -99999999999999) == -99999999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101) == 100001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101) == 100001111: {e}')
    
    total += 1
    try:
        result = candidate(num = 303030303030303) == 300000003333333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 303030303030303) == 300000003333333: {e}')
    
    total += 1
    try:
        result = candidate(num = 56789) == 56789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 56789) == 56789: {e}')
    
    total += 1
    try:
        result = candidate(num = 1230000000) == 1000000023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1230000000) == 1000000023: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000000000001) == 100000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000000000001) == 100000000000001: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890987654) == 1023445566778899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890987654) == 1023445566778899: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333444555666777888999) == 111222333444555666777888999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333444555666777888999) == 111222333444555666777888999: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000100) == 1000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000100) == 1000001: {e}')
    
    total += 1
    try:
        result = candidate(num = 120030400500600) == 100000000023456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 120030400500600) == 100000000023456: {e}')
    
    total += 1
    try:
        result = candidate(num = 20000000000000) == 20000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 20000000000000) == 20000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000000) == 1000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000000) == 1000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -111111111111111) == -111111111111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -111111111111111) == -111111111111111: {e}')
    
    total += 1
    try:
        result = candidate(num = -300000000000000) == -300000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -300000000000000) == -300000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000001) == 1000000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000001) == 1000000000000001: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000000000000) == 100000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000000000000) == 100000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 2000000000000000001) == 1000000000000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2000000000000000001) == 1000000000000000002: {e}')
    
    total += 1
    try:
        result = candidate(num = 202020202020202) == 200000002222222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 202020202020202) == 200000002222222: {e}')
    
    total += 1
    try:
        result = candidate(num = 1002003004) == 1000000234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1002003004) == 1000000234: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000001) == 1000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000001) == 1000000001: {e}')
    
    total += 1
    try:
        result = candidate(num = -123456789098765) == -998877665543210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -123456789098765) == -998877665543210: {e}')
    
    total += 1
    try:
        result = candidate(num = -200100000000000) == -210000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -200100000000000) == -210000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -111222333) == -333222111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -111222333) == -333222111: {e}')
    
    total += 1
    try:
        result = candidate(num = -9999999999999) == -9999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -9999999999999) == -9999999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 12003004005) == 10000002345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12003004005) == 10000002345: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = -50000000000000) == -50000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -50000000000000) == -50000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111111111) == 1111111111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111111111) == 1111111111111: {e}')
    
    total += 1
    try:
        result = candidate(num = -2000000000000000000) == -2000000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -2000000000000000000) == -2000000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -2000000000000000001) == -2100000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -2000000000000000001) == -2100000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -1000000000000000000) == -1000000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1000000000000000000) == -1000000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1010101010) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1010101010) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(num = 10000000000000000) == 10000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000000000000000) == 10000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -111000000) == -111000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -111000000) == -111000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 10000000000000001) == 10000000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000000000000001) == 10000000000000001: {e}')
    
    total += 1
    try:
        result = candidate(num = -1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = -543210987654321) == -987655443322110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -543210987654321) == -987655443322110: {e}')
    
    total += 1
    try:
        result = candidate(num = 2003005006) == 2000000356
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2003005006) == 2000000356: {e}')
    
    total += 1
    try:
        result = candidate(num = 30000123) == 10000233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 30000123) == 10000233: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000002) == 1000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000002) == 1000002: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999999999) == 999999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999999999) == 999999999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = -999888777666) == -999888777666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -999888777666) == -999888777666: {e}')
    
    total += 1
    try:
        result = candidate(num = 100001000010000) == 100000000000011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100001000010000) == 100000000000011: {e}')
    
    total += 1
    try:
        result = candidate(num = 500000000000000) == 500000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500000000000000) == 500000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -222222222) == -222222222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -222222222) == -222222222: {e}')
    
    total += 1
    try:
        result = candidate(num = -1000000000000000001) == -1100000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1000000000000000001) == -1100000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -200000000000001) == -210000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -200000000000001) == -210000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 2000000001) == 1000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2000000001) == 1000000002: {e}')
    
    total += 1
    try:
        result = candidate(num = -100000000000001) == -110000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -100000000000001) == -110000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 111000222333) == 100011222333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111000222333) == 100011222333: {e}')
    
    total += 1
    try:
        result = candidate(num = -900000000000001) == -910000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -900000000000001) == -910000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 5000000000000000000) == 5000000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5000000000000000000) == 5000000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 5000000000000000001) == 1000000000000000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5000000000000000001) == 1000000000000000005: {e}')
    
    total += 1
    try:
        result = candidate(num = -1000000000000000) == -1000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1000000000000000) == -1000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111111111111) == 111111111111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111111111111) == 111111111111111: {e}')
    
    total += 1
    try:
        result = candidate(num = -303030303030303) == -333333330000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -303030303030303) == -333333330000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 503020104) == 100002345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 503020104) == 100002345: {e}')
    
    total += 1
    try:
        result = candidate(num = 900000000000000) == 900000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 900000000000000) == 900000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 200000000000001) == 100000000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 200000000000001) == 100000000000002: {e}')
    
    total += 1
    try:
        result = candidate(num = -50006007008) == -87650000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -50006007008) == -87650000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 100020003000) == 100000000023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100020003000) == 100000000023: {e}')
    
    total += 1
    try:
        result = candidate(num = 99999999999999) == 99999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99999999999999) == 99999999999999: {e}')
    
    total += 1
    try:
        result = candidate(num = 3003003) == 3000033
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3003003) == 3000033: {e}')
    
    total += 1
    try:
        result = candidate(num = -10000100001000) == -11100000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -10000100001000) == -11100000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -100000000000000) == -100000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -100000000000000) == -100000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000000000000000) == 100000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000000000000000) == 100000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890) == 1023456789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890) == 1023456789: {e}')
    
    total += 1
    try:
        result = candidate(num = 10000000000000) == 10000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000000000000) == 10000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000000002) == 1000000000000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000000002) == 1000000000000000002: {e}')
    
    total += 1
    try:
        result = candidate(num = -2100300) == -3210000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -2100300) == -3210000: {e}')
    
    total += 1
    try:
        result = candidate(num = 2000000000000000000) == 2000000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2000000000000000000) == 2000000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000000000) == 1000000000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000000000) == 1000000000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789012345) == 101223344556789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789012345) == 101223344556789: {e}')
    
    total += 1
    try:
        result = candidate(num = 123000456) == 100023456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123000456) == 100023456: {e}')
    
    total += 1
    try:
        result = candidate(num = -987000000000000) == -987000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -987000000000000) == -987000000000000: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000000001) == 1000000000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000000001) == 1000000000000000001: {e}')
    
    total += 1
    try:
        result = candidate(num = -202020202) == -222220000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -202020202) == -222220000: {e}')
    
    total += 1
    try:
        result = candidate(num = 2003004005) == 2000000345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2003004005) == 2000000345: {e}')
    
    total += 1
    try:
        result = candidate(num = -1234567890) == -9876543210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1234567890) == -9876543210: {e}')
    
    total += 1
    try:
        result = candidate(num = -5000000) == -5000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -5000000) == -5000000: {e}')
    
    total += 1
    try:
        result = candidate(num = -56789) == -98765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -56789) == -98765: {e}')
    
    total += 1
    try:
        result = candidate(num = -1000000000000001) == -1100000000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = -1000000000000001) == -1100000000000000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 2020) == 2002
    assert candidate(num = 10) == 10
    assert candidate(num = -10000000000) == -10000000000
    assert candidate(num = 10000000000) == 10000000000
    assert candidate(num = 10001) == 10001
    assert candidate(num = 123456789) == 123456789
    assert candidate(num = 9876543210) == 1023456789
    assert candidate(num = 310) == 103
    assert candidate(num = 1000) == 1000
    assert candidate(num = -10001) == -11000
    assert candidate(num = -9876543210) == -9876543210
    assert candidate(num = 1001) == 1001
    assert candidate(num = 987654321) == 123456789
    assert candidate(num = -100) == -100
    assert candidate(num = 0) == 0
    assert candidate(num = -7605) == -7650
    assert candidate(num = -1001) == -1100
    assert candidate(num = -123456789) == -987654321
    assert candidate(num = 100) == 100
    assert candidate(num = -12345) == -54321
    assert candidate(num = 54321) == 12345
    assert candidate(num = -10) == -10
    assert candidate(num = -900) == -900
    assert candidate(num = 20001002003004005) == 10000000000022345
    assert candidate(num = -600500400300201) == -654321000000000
    assert candidate(num = 3000000000000000000) == 3000000000000000000
    assert candidate(num = -999999999) == -999999999
    assert candidate(num = 101010101010101) == 100000001111111
    assert candidate(num = 505050505050505) == 500000005555555
    assert candidate(num = -123456789012345) == -987655443322110
    assert candidate(num = -1230456) == -6543210
    assert candidate(num = 2100000000000000) == 1000000000000002
    assert candidate(num = 1000000000) == 1000000000
    assert candidate(num = -202020202020202) == -222222220000000
    assert candidate(num = 213004005) == 100002345
    assert candidate(num = -999999999999999) == -999999999999999
    assert candidate(num = -987654321012345) == -987655443322110
    assert candidate(num = -543210000) == -543210000
    assert candidate(num = -12000210) == -22110000
    assert candidate(num = -99999999999999) == -99999999999999
    assert candidate(num = 101010101) == 100001111
    assert candidate(num = 303030303030303) == 300000003333333
    assert candidate(num = 56789) == 56789
    assert candidate(num = 1230000000) == 1000000023
    assert candidate(num = 100000000000001) == 100000000000001
    assert candidate(num = 1234567890987654) == 1023445566778899
    assert candidate(num = 111222333444555666777888999) == 111222333444555666777888999
    assert candidate(num = 1000100) == 1000001
    assert candidate(num = 120030400500600) == 100000000023456
    assert candidate(num = 20000000000000) == 20000000000000
    assert candidate(num = 1000000000000000) == 1000000000000000
    assert candidate(num = -111111111111111) == -111111111111111
    assert candidate(num = -300000000000000) == -300000000000000
    assert candidate(num = 1000000000000001) == 1000000000000001
    assert candidate(num = 100000000000000) == 100000000000000
    assert candidate(num = 2000000000000000001) == 1000000000000000002
    assert candidate(num = 202020202020202) == 200000002222222
    assert candidate(num = 1002003004) == 1000000234
    assert candidate(num = 1000000001) == 1000000001
    assert candidate(num = -123456789098765) == -998877665543210
    assert candidate(num = -200100000000000) == -210000000000000
    assert candidate(num = -111222333) == -333222111
    assert candidate(num = -9999999999999) == -9999999999999
    assert candidate(num = 12003004005) == 10000002345
    assert candidate(num = 999999999) == 999999999
    assert candidate(num = -50000000000000) == -50000000000000
    assert candidate(num = 1111111111111) == 1111111111111
    assert candidate(num = -2000000000000000000) == -2000000000000000000
    assert candidate(num = -2000000000000000001) == -2100000000000000000
    assert candidate(num = -1000000000000000000) == -1000000000000000000
    assert candidate(num = 1010101010) == 1000001111
    assert candidate(num = 10000000000000000) == 10000000000000000
    assert candidate(num = -111000000) == -111000000
    assert candidate(num = 10000000000000001) == 10000000000000001
    assert candidate(num = -1) == -1
    assert candidate(num = -543210987654321) == -987655443322110
    assert candidate(num = 2003005006) == 2000000356
    assert candidate(num = 30000123) == 10000233
    assert candidate(num = 1000002) == 1000002
    assert candidate(num = 999999999999999) == 999999999999999
    assert candidate(num = -999888777666) == -999888777666
    assert candidate(num = 100001000010000) == 100000000000011
    assert candidate(num = 500000000000000) == 500000000000000
    assert candidate(num = -222222222) == -222222222
    assert candidate(num = -1000000000000000001) == -1100000000000000000
    assert candidate(num = -200000000000001) == -210000000000000
    assert candidate(num = 2000000001) == 1000000002
    assert candidate(num = -100000000000001) == -110000000000000
    assert candidate(num = 111000222333) == 100011222333
    assert candidate(num = -900000000000001) == -910000000000000
    assert candidate(num = 5000000000000000000) == 5000000000000000000
    assert candidate(num = 5000000000000000001) == 1000000000000000005
    assert candidate(num = -1000000000000000) == -1000000000000000
    assert candidate(num = 111111111111111) == 111111111111111
    assert candidate(num = -303030303030303) == -333333330000000
    assert candidate(num = 503020104) == 100002345
    assert candidate(num = 900000000000000) == 900000000000000
    assert candidate(num = 200000000000001) == 100000000000002
    assert candidate(num = -50006007008) == -87650000000
    assert candidate(num = 100020003000) == 100000000023
    assert candidate(num = 99999999999999) == 99999999999999
    assert candidate(num = 3003003) == 3000033
    assert candidate(num = -10000100001000) == -11100000000000
    assert candidate(num = -100000000000000) == -100000000000000
    assert candidate(num = 100000000000000000) == 100000000000000000
    assert candidate(num = 1234567890) == 1023456789
    assert candidate(num = 10000000000000) == 10000000000000
    assert candidate(num = 1000000000000000002) == 1000000000000000002
    assert candidate(num = -2100300) == -3210000
    assert candidate(num = 2000000000000000000) == 2000000000000000000
    assert candidate(num = 1000000000000000000) == 1000000000000000000
    assert candidate(num = 123456789012345) == 101223344556789
    assert candidate(num = 123000456) == 100023456
    assert candidate(num = -987000000000000) == -987000000000000
    assert candidate(num = 1000000000000000001) == 1000000000000000001
    assert candidate(num = -202020202) == -222220000
    assert candidate(num = 2003004005) == 2000000345
    assert candidate(num = -1234567890) == -9876543210
    assert candidate(num = -5000000) == -5000000
    assert candidate(num = -56789) == -98765
    assert candidate(num = -1000000000000001) == -1100000000000000


