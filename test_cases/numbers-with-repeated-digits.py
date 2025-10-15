def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 99999) == 67509
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 67509: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 994388229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 994388229: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999999) == 9287109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999999) == 9287109: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 56789) == 37493
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56789) == 37493: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 262
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 262: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 4726
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 4726: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 67510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 67510: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 261
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 261: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 4725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 4725: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 994388230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 994388230: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 982042551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 982042551: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 431
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 431: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 831430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 831430: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 121064705
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 121064705: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 222222222) == 219432852
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222222) == 219432852: {e}')
    
    total += 1
    try:
        result = candidate(n = 567890) == 465294
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567890) == 465294: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123456789) == 1234567890114579099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123456789) == 1234567890114579099: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111) == 76941
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111) == 76941: {e}')
    
    total += 1
    try:
        result = candidate(n = 746384741) == 741672419
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 746384741) == 741672419: {e}')
    
    total += 1
    try:
        result = candidate(n = 23456) == 14387
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23456) == 14387: {e}')
    
    total += 1
    try:
        result = candidate(n = 100100100) == 97754250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100100100) == 97754250: {e}')
    
    total += 1
    try:
        result = candidate(n = 234567890) == 231766695
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 234567890) == 231766695: {e}')
    
    total += 1
    try:
        result = candidate(n = 23456789) == 22516226
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23456789) == 22516226: {e}')
    
    total += 1
    try:
        result = candidate(n = 876543210) == 871340553
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876543210) == 871340553: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == 98664251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == 98664251: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000) == 197291270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000) == 197291270: {e}')
    
    total += 1
    try:
        result = candidate(n = 900000000) == 894751110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900000000) == 894751110: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == 9287110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == 9287110: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654319) == 982042551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654319) == 982042551: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999) == 97654149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999) == 97654149: {e}')
    
    total += 1
    try:
        result = candidate(n = 314159265) == 311036535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 314159265) == 311036535: {e}')
    
    total += 1
    try:
        result = candidate(n = 543210987) == 539235633
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543210987) == 539235633: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000010) == 994388240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000010) == 994388240: {e}')
    
    total += 1
    try:
        result = candidate(n = 899899) == 746449
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 899899) == 746449: {e}')
    
    total += 1
    try:
        result = candidate(n = 1122334455) == 1116682365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1122334455) == 1116682365: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555555) == 551556585
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555555) == 551556585: {e}')
    
    total += 1
    try:
        result = candidate(n = 271828182) == 268868772
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 271828182) == 268868772: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == 108724941
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == 108724941: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890) == 1228909886
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890) == 1228909886: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888) == 883680318
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888) == 883680318: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111) == 5501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111) == 5501: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654320) == 982042551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654320) == 982042551: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 407030
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 407030: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765) == 66275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765) == 66275: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 496202630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 496202630: {e}')
    
    total += 1
    try:
        result = candidate(n = 88888888) == 86744638
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88888888) == 86744638: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == 1058291
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == 1058291: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 831429
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 831429: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 89039
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 89039: {e}')
    
    total += 1
    try:
        result = candidate(n = 87654321) == 85513027
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87654321) == 85513027: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == 35467
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == 35467: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == 97654150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == 97654150: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 99999) == 67509
    assert candidate(n = 999999999) == 994388229
    assert candidate(n = 9999999) == 9287109
    assert candidate(n = 100) == 10
    assert candidate(n = 56789) == 37493
    assert candidate(n = 1000) == 262
    assert candidate(n = 50) == 4
    assert candidate(n = 300) == 66
    assert candidate(n = 10000) == 4726
    assert candidate(n = 101) == 11
    assert candidate(n = 100000) == 67510
    assert candidate(n = 999) == 261
    assert candidate(n = 9999) == 4725
    assert candidate(n = 20) == 1
    assert candidate(n = 1000000000) == 994388230
    assert candidate(n = 987654321) == 982042551
    assert candidate(n = 1234) == 431
    assert candidate(n = 1000000) == 831430
    assert candidate(n = 123456789) == 121064705
    assert candidate(n = 1) == 0
    assert candidate(n = 10) == 0
    assert candidate(n = 222222222) == 219432852
    assert candidate(n = 567890) == 465294
    assert candidate(n = 1234567890123456789) == 1234567890114579099
    assert candidate(n = 111111) == 76941
    assert candidate(n = 746384741) == 741672419
    assert candidate(n = 23456) == 14387
    assert candidate(n = 100100100) == 97754250
    assert candidate(n = 234567890) == 231766695
    assert candidate(n = 23456789) == 22516226
    assert candidate(n = 876543210) == 871340553
    assert candidate(n = 101010101) == 98664251
    assert candidate(n = 200000000) == 197291270
    assert candidate(n = 900000000) == 894751110
    assert candidate(n = 10000000) == 9287110
    assert candidate(n = 987654319) == 982042551
    assert candidate(n = 99999999) == 97654149
    assert candidate(n = 314159265) == 311036535
    assert candidate(n = 543210987) == 539235633
    assert candidate(n = 1000000010) == 994388240
    assert candidate(n = 899899) == 746449
    assert candidate(n = 1122334455) == 1116682365
    assert candidate(n = 555555555) == 551556585
    assert candidate(n = 271828182) == 268868772
    assert candidate(n = 111111111) == 108724941
    assert candidate(n = 1234567890) == 1228909886
    assert candidate(n = 888888888) == 883680318
    assert candidate(n = 11111) == 5501
    assert candidate(n = 987654320) == 982042551
    assert candidate(n = 500000) == 407030
    assert candidate(n = 98765) == 66275
    assert candidate(n = 500000000) == 496202630
    assert candidate(n = 88888888) == 86744638
    assert candidate(n = 1234567) == 1058291
    assert candidate(n = 999999) == 831429
    assert candidate(n = 123456) == 89039
    assert candidate(n = 87654321) == 85513027
    assert candidate(n = 54321) == 35467
    assert candidate(n = 100000000) == 97654150


