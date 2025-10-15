def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 891632373
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 891632373: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 50001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 50001: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 900000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 300: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 600001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 600001: {e}')
    
    total += 1
    try:
        result = candidate(n = 501) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 501) == 201: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 900000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 900000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 301: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000) == 45000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000) == 45000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(n = 210) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 210) == 142: {e}')
    
    total += 1
    try:
        result = candidate(n = 1010) == 313
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010) == 313: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000005) == 500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000005) == 500000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 8121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 8121: {e}')
    
    total += 1
    try:
        result = candidate(n = 50123) == 30057
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50123) == 30057: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 2971027783
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 2971027783: {e}')
    
    total += 1
    try:
        result = candidate(n = 909090909) == 826446281
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 909090909) == 826446281: {e}')
    
    total += 1
    try:
        result = candidate(n = 202020202) == 262218141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 202020202) == 262218141: {e}')
    
    total += 1
    try:
        result = candidate(n = 111) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 213456789) == 273589849
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 213456789) == 273589849: {e}')
    
    total += 1
    try:
        result = candidate(n = 111000111) == 99600372
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111000111) == 99600372: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000000) == 2800000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000000) == 2800000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 123000000) == 129800001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123000000) == 129800001: {e}')
    
    total += 1
    try:
        result = candidate(n = 56789) == 33059
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56789) == 33059: {e}')
    
    total += 1
    try:
        result = candidate(n = 110) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 110) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000000000) == 3700000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000000000) == 3700000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 807060504) == 745234201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 807060504) == 745234201: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 160: {e}')
    
    total += 1
    try:
        result = candidate(n = 10001) == 4003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10001) == 4003: {e}')
    
    total += 1
    try:
        result = candidate(n = 100100100) == 80150223
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100100100) == 80150223: {e}')
    
    total += 1
    try:
        result = candidate(n = 10999) == 5300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10999) == 5300: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 876543210) == 803978042
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876543210) == 803978042: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 303
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 303: {e}')
    
    total += 1
    try:
        result = candidate(n = 808080808) == 745842261
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 808080808) == 745842261: {e}')
    
    total += 1
    try:
        result = candidate(n = 5001) == 2501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5001) == 2501: {e}')
    
    total += 1
    try:
        result = candidate(n = 1101101101) == 1082954833
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1101101101) == 1082954833: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == 81624329
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == 81624329: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000) == 260000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000) == 260000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 303030303) == 342822161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 303030303) == 342822161: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000) == 740000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000) == 740000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == 7000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == 7000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000000) == 10000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000000) == 10000000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 432109876) == 453263855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 432109876) == 453263855: {e}')
    
    total += 1
    try:
        result = candidate(n = 2020) == 1612
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2020) == 1612: {e}')
    
    total += 1
    try:
        result = candidate(n = 10101) == 4125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10101) == 4125: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000000) == 580000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000000) == 580000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == 337
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == 337: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555555) == 549382716
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555555) == 549382716: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == 900000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == 900000003: {e}')
    
    total += 1
    try:
        result = candidate(n = 50001) == 30001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50001) == 30001: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == 100000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == 100000008: {e}')
    
    total += 1
    try:
        result = candidate(n = 1010101010) == 917253346
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010101010) == 917253346: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888) == 812345679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888) == 812345679: {e}')
    
    total += 1
    try:
        result = candidate(n = 50005) == 30001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50005) == 30001: {e}')
    
    total += 1
    try:
        result = candidate(n = 654321098) == 628668419
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 654321098) == 628668419: {e}')
    
    total += 1
    try:
        result = candidate(n = 700000000) == 660000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700000000) == 660000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 140: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765) == 49657
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765) == 49657: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 400000000) == 420000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400000000) == 420000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100100) == 50122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100100) == 50122: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 130589849
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 130589849: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999999) == 2800000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999999) == 2800000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100001) == 50003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100001) == 50003: {e}')
    
    total += 1
    try:
        result = candidate(n = 199) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199) == 140: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == 1111111120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == 1111111120: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000008) == 740000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000008) == 740000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 100010001) == 80014005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100010001) == 80014005: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == 80000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == 80000001: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 987654321) == 891632373
    assert candidate(n = 100000) == 50001
    assert candidate(n = 999999999) == 900000000
    assert candidate(n = 999) == 300
    assert candidate(n = 1000000) == 600001
    assert candidate(n = 501) == 201
    assert candidate(n = 9999) == 4000
    assert candidate(n = 100) == 21
    assert candidate(n = 1000000000) == 900000001
    assert candidate(n = 1000) == 301
    assert candidate(n = 55) == 16
    assert candidate(n = 50000000) == 45000000
    assert candidate(n = 13) == 6
    assert candidate(n = 99999) == 50000
    assert candidate(n = 210) == 142
    assert candidate(n = 1010) == 313
    assert candidate(n = 500000005) == 500000001
    assert candidate(n = 12345) == 8121
    assert candidate(n = 50123) == 30057
    assert candidate(n = 2147483647) == 2971027783
    assert candidate(n = 909090909) == 826446281
    assert candidate(n = 202020202) == 262218141
    assert candidate(n = 111) == 36
    assert candidate(n = 213456789) == 273589849
    assert candidate(n = 111000111) == 99600372
    assert candidate(n = 2000000000) == 2800000000
    assert candidate(n = 123000000) == 129800001
    assert candidate(n = 56789) == 33059
    assert candidate(n = 110) == 33
    assert candidate(n = 3000000000) == 3700000000
    assert candidate(n = 807060504) == 745234201
    assert candidate(n = 300) == 160
    assert candidate(n = 10001) == 4003
    assert candidate(n = 100100100) == 80150223
    assert candidate(n = 10999) == 5300
    assert candidate(n = 99) == 20
    assert candidate(n = 876543210) == 803978042
    assert candidate(n = 1001) == 303
    assert candidate(n = 808080808) == 745842261
    assert candidate(n = 5001) == 2501
    assert candidate(n = 1101101101) == 1082954833
    assert candidate(n = 101010101) == 81624329
    assert candidate(n = 200000000) == 260000000
    assert candidate(n = 303030303) == 342822161
    assert candidate(n = 800000000) == 740000000
    assert candidate(n = 101) == 23
    assert candidate(n = 10000000) == 7000001
    assert candidate(n = 10000000000) == 10000000001
    assert candidate(n = 432109876) == 453263855
    assert candidate(n = 2020) == 1612
    assert candidate(n = 10101) == 4125
    assert candidate(n = 600000000) == 580000000
    assert candidate(n = 1023) == 337
    assert candidate(n = 555555555) == 549382716
    assert candidate(n = 1000000001) == 900000003
    assert candidate(n = 50001) == 30001
    assert candidate(n = 111111111) == 100000008
    assert candidate(n = 1010101010) == 917253346
    assert candidate(n = 888888888) == 812345679
    assert candidate(n = 50005) == 30001
    assert candidate(n = 654321098) == 628668419
    assert candidate(n = 700000000) == 660000000
    assert candidate(n = 200) == 140
    assert candidate(n = 98765) == 49657
    assert candidate(n = 500000000) == 500000000
    assert candidate(n = 400000000) == 420000000
    assert candidate(n = 100100) == 50122
    assert candidate(n = 123456789) == 130589849
    assert candidate(n = 1999999999) == 2800000000
    assert candidate(n = 100001) == 50003
    assert candidate(n = 199) == 140
    assert candidate(n = 1111111111) == 1111111120
    assert candidate(n = 800000008) == 740000001
    assert candidate(n = 100010001) == 80014005
    assert candidate(n = 100000000) == 80000001


