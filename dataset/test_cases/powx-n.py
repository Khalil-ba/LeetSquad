def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(x = 3.0,n = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3.0,n = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 10.0,n = -3) == 0.001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10.0,n = -3) == 0.001: {e}')
    
    total += 1
    try:
        result = candidate(x = 5.0,n = 1) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5.0,n = 1) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.0,n = -2) == 0.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.0,n = -2) == 0.25: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.1,n = 2) == 0.010000000000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.1,n = 2) == 0.010000000000000002: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.5,n = 5) == 7.59375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.5,n = 5) == 7.59375: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.1,n = 3) == 9.261000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.1,n = 3) == 9.261000000000001: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.0,n = -1) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.0,n = -1) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.5,n = 4) == 0.0625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.5,n = 4) == 0.0625: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.0,n = 10) == 1024.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.0,n = 10) == 1024.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.99,n = 100) == 0.3660323412732289
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.99,n = 100) == 0.3660323412732289: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.0,n = -1000000) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.0,n = -1000000) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.5,n = -5) == 0.01024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.5,n = -5) == 0.01024: {e}')
    
    total += 1
    try:
        result = candidate(x = 10.0,n = 5) == 100000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10.0,n = 5) == 100000.0: {e}')
    
    total += 1
    try:
        result = candidate(x = -1.0,n = 2147483647) == -1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1.0,n = 2147483647) == -1.0: {e}')
    
    total += 1
    try:
        result = candidate(x = -2.0,n = 12) == 4096.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2.0,n = 12) == 4096.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.23456,n = 789) == 1.5963462056225718e+72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.23456,n = 789) == 1.5963462056225718e+72: {e}')
    
    total += 1
    try:
        result = candidate(x = 3.14,n = 7) == 3009.5913952479914
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3.14,n = 7) == 3009.5913952479914: {e}')
    
    total += 1
    try:
        result = candidate(x = -2.0,n = -3) == -0.125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2.0,n = -3) == -0.125: {e}')
    
    total += 1
    try:
        result = candidate(x = -1.0,n = 1000001) == -1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1.0,n = 1000001) == -1.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.1,n = 10) == 1.0000000000000011e-10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.1,n = 10) == 1.0000000000000011e-10: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.1,n = 20) == 1.0000000000000022e-20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.1,n = 20) == 1.0000000000000022e-20: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.99999,n = -10000) == 1.1051714706643663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.99999,n = -10000) == 1.1051714706643663: {e}')
    
    total += 1
    try:
        result = candidate(x = -1.5,n = 2) == 2.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1.5,n = 2) == 2.25: {e}')
    
    total += 1
    try:
        result = candidate(x = -0.5,n = 4) == 0.0625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -0.5,n = 4) == 0.0625: {e}')
    
    total += 1
    try:
        result = candidate(x = -0.5,n = 6) == 0.015625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -0.5,n = 6) == 0.015625: {e}')
    
    total += 1
    try:
        result = candidate(x = -1.0,n = -2147483648) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1.0,n = -2147483648) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 9.87654,n = -321) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9.87654,n = -321) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.5,n = 100) == 6.223015277861143e+39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.5,n = 100) == 6.223015277861143e+39: {e}')
    
    total += 1
    try:
        result = candidate(x = 10.0,n = 10) == 10000000000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10.0,n = 10) == 10000000000.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.0,n = 1000000) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.0,n = 1000000) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 5.0,n = -3) == 0.008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5.0,n = -3) == 0.008: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.0,n = -2147483648) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.0,n = -2147483648) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.0,n = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.0,n = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 10.0,n = 2147483647) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10.0,n = 2147483647) == inf: {e}')
    
    total += 1
    try:
        result = candidate(x = 99.99999,n = 10) == 9.999990000004497e+19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 99.99999,n = 10) == 9.999990000004497e+19: {e}')
    
    total += 1
    try:
        result = candidate(x = -0.5,n = 8) == 0.00390625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -0.5,n = 8) == 0.00390625: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.0,n = -1000) == 9.332636185032189e-302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.0,n = -1000) == 9.332636185032189e-302: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.0,n = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.0,n = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.5,n = -3) == 0.064
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.5,n = -3) == 0.064: {e}')
    
    total += 1
    try:
        result = candidate(x = 10.0,n = 1000) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10.0,n = 1000) == inf: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.99999,n = 1000) == 0.990049784246398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.99999,n = 1000) == 0.990049784246398: {e}')
    
    total += 1
    try:
        result = candidate(x = -3.0,n = 4) == 81.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -3.0,n = 4) == 81.0: {e}')
    
    total += 1
    try:
        result = candidate(x = -3.0,n = -3) == -0.037037037037037035
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -3.0,n = -3) == -0.037037037037037035: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.1,n = -5) == 99999.99999999994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.1,n = -5) == 99999.99999999994: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.5,n = 20) == 90949470.17729282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.5,n = 20) == 90949470.17729282: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.00001,n = -1000000) == 4.5402199796741926e-05
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.00001,n = -1000000) == 4.5402199796741926e-05: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.1,n = -3) == 999.9999999999998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.1,n = -3) == 999.9999999999998: {e}')
    
    total += 1
    try:
        result = candidate(x = -0.5,n = 3) == -0.125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -0.5,n = 3) == -0.125: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.73205,n = 12) == 728.9959212545092
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.73205,n = 12) == 728.9959212545092: {e}')
    
    total += 1
    try:
        result = candidate(x = 10.0,n = 1) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10.0,n = 1) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(x = -2.0,n = 4) == 16.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2.0,n = 4) == 16.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.1,n = 100) == 1.0000000000000108e-100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.1,n = 100) == 1.0000000000000108e-100: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.0,n = 2147483647) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.0,n = 2147483647) == inf: {e}')
    
    total += 1
    try:
        result = candidate(x = 1e-05,n = 10000) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1e-05,n = 10000) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.0,n = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.0,n = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.5,n = -5) == 32.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.5,n = -5) == 32.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 3.0,n = 20) == 3486784401.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3.0,n = 20) == 3486784401.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 3.0,n = 15) == 14348907.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3.0,n = 15) == 14348907.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.00001,n = 1000) == 1.0100501165820832
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.00001,n = 1000) == 1.0100501165820832: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.5,n = 2147483646) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.5,n = 2147483646) == inf: {e}')
    
    total += 1
    try:
        result = candidate(x = 10.0,n = 100) == 1.0000000000000002e+100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10.0,n = 100) == 1.0000000000000002e+100: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.0,n = -2147483648) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.0,n = -2147483648) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 1e-05,n = 1000000) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1e-05,n = 1000000) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(x = -1.0,n = 2147483646) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1.0,n = 2147483646) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.5,n = 20) == 3325.256730079651
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.5,n = 20) == 3325.256730079651: {e}')
    
    total += 1
    try:
        result = candidate(x = -2.0,n = 3) == -8.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2.0,n = 3) == -8.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.2,n = -5) == 0.4018775720164609
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.2,n = -5) == 0.4018775720164609: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.1,n = -10) == 9999999999.999989
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.1,n = -10) == 9999999999.999989: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.0,n = -1000) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.0,n = -1000) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.0,n = 100000000) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.0,n = 100000000) == inf: {e}')
    
    total += 1
    try:
        result = candidate(x = -2.0,n = 11) == -2048.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2.0,n = 11) == -2048.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 3.5,n = 15) == 144884079.28292847
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3.5,n = 15) == 144884079.28292847: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.5,n = -10) == 1024.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.5,n = -10) == 1024.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.41421,n = 50) == 33550206.11671562
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.41421,n = 50) == 33550206.11671562: {e}')
    
    total += 1
    try:
        result = candidate(x = 3.0,n = 13) == 1594323.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3.0,n = 13) == 1594323.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 0.99999,n = 1000000) == 4.539765980992338e-05
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0.99999,n = 1000000) == 4.539765980992338e-05: {e}')
    
    total += 1
    try:
        result = candidate(x = 5.0,n = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5.0,n = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 2.0,n = -10) == 0.0009765625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2.0,n = -10) == 0.0009765625: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.0,n = -5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.0,n = -5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.00001,n = -1000) == 0.9900498832512471
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.00001,n = -1000) == 0.9900498832512471: {e}')
    
    total += 1
    try:
        result = candidate(x = -1.5,n = 5) == -7.59375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1.5,n = 5) == -7.59375: {e}')
    
    total += 1
    try:
        result = candidate(x = 1.0,n = 2147483647) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1.0,n = 2147483647) == 1.0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(x = 3.0,n = 0) == 1
    assert candidate(x = 10.0,n = -3) == 0.001
    assert candidate(x = 5.0,n = 1) == 5.0
    assert candidate(x = 2.0,n = -2) == 0.25
    assert candidate(x = 0.1,n = 2) == 0.010000000000000002
    assert candidate(x = 1.5,n = 5) == 7.59375
    assert candidate(x = 2.1,n = 3) == 9.261000000000001
    assert candidate(x = 2.0,n = -1) == 0.5
    assert candidate(x = 0.5,n = 4) == 0.0625
    assert candidate(x = 2.0,n = 10) == 1024.0
    assert candidate(x = 0.99,n = 100) == 0.3660323412732289
    assert candidate(x = 1.0,n = -1000000) == 1.0
    assert candidate(x = 2.5,n = -5) == 0.01024
    assert candidate(x = 10.0,n = 5) == 100000.0
    assert candidate(x = -1.0,n = 2147483647) == -1.0
    assert candidate(x = -2.0,n = 12) == 4096.0
    assert candidate(x = 1.23456,n = 789) == 1.5963462056225718e+72
    assert candidate(x = 3.14,n = 7) == 3009.5913952479914
    assert candidate(x = -2.0,n = -3) == -0.125
    assert candidate(x = -1.0,n = 1000001) == -1.0
    assert candidate(x = 0.1,n = 10) == 1.0000000000000011e-10
    assert candidate(x = 0.1,n = 20) == 1.0000000000000022e-20
    assert candidate(x = 0.99999,n = -10000) == 1.1051714706643663
    assert candidate(x = -1.5,n = 2) == 2.25
    assert candidate(x = -0.5,n = 4) == 0.0625
    assert candidate(x = -0.5,n = 6) == 0.015625
    assert candidate(x = -1.0,n = -2147483648) == 1.0
    assert candidate(x = 9.87654,n = -321) == 0.0
    assert candidate(x = 2.5,n = 100) == 6.223015277861143e+39
    assert candidate(x = 10.0,n = 10) == 10000000000.0
    assert candidate(x = 1.0,n = 1000000) == 1.0
    assert candidate(x = 5.0,n = -3) == 0.008
    assert candidate(x = 1.0,n = -2147483648) == 1.0
    assert candidate(x = 1.0,n = 0) == 1
    assert candidate(x = 10.0,n = 2147483647) == inf
    assert candidate(x = 99.99999,n = 10) == 9.999990000004497e+19
    assert candidate(x = -0.5,n = 8) == 0.00390625
    assert candidate(x = 2.0,n = -1000) == 9.332636185032189e-302
    assert candidate(x = 2.0,n = 0) == 1
    assert candidate(x = 2.5,n = -3) == 0.064
    assert candidate(x = 10.0,n = 1000) == inf
    assert candidate(x = 0.99999,n = 1000) == 0.990049784246398
    assert candidate(x = -3.0,n = 4) == 81.0
    assert candidate(x = -3.0,n = -3) == -0.037037037037037035
    assert candidate(x = 0.1,n = -5) == 99999.99999999994
    assert candidate(x = 2.5,n = 20) == 90949470.17729282
    assert candidate(x = 1.00001,n = -1000000) == 4.5402199796741926e-05
    assert candidate(x = 0.1,n = -3) == 999.9999999999998
    assert candidate(x = -0.5,n = 3) == -0.125
    assert candidate(x = 1.73205,n = 12) == 728.9959212545092
    assert candidate(x = 10.0,n = 1) == 10.0
    assert candidate(x = -2.0,n = 4) == 16.0
    assert candidate(x = 0.1,n = 100) == 1.0000000000000108e-100
    assert candidate(x = 2.0,n = 2147483647) == inf
    assert candidate(x = 1e-05,n = 10000) == 0.0
    assert candidate(x = 0.0,n = 0) == 1
    assert candidate(x = 0.5,n = -5) == 32.0
    assert candidate(x = 3.0,n = 20) == 3486784401.0
    assert candidate(x = 3.0,n = 15) == 14348907.0
    assert candidate(x = 1.00001,n = 1000) == 1.0100501165820832
    assert candidate(x = 1.5,n = 2147483646) == inf
    assert candidate(x = 10.0,n = 100) == 1.0000000000000002e+100
    assert candidate(x = 2.0,n = -2147483648) == 0.0
    assert candidate(x = 1e-05,n = 1000000) == 0.0
    assert candidate(x = -1.0,n = 2147483646) == 1.0
    assert candidate(x = 1.5,n = 20) == 3325.256730079651
    assert candidate(x = -2.0,n = 3) == -8.0
    assert candidate(x = 1.2,n = -5) == 0.4018775720164609
    assert candidate(x = 0.1,n = -10) == 9999999999.999989
    assert candidate(x = 1.0,n = -1000) == 1.0
    assert candidate(x = 2.0,n = 100000000) == inf
    assert candidate(x = -2.0,n = 11) == -2048.0
    assert candidate(x = 3.5,n = 15) == 144884079.28292847
    assert candidate(x = 0.5,n = -10) == 1024.0
    assert candidate(x = 1.41421,n = 50) == 33550206.11671562
    assert candidate(x = 3.0,n = 13) == 1594323.0
    assert candidate(x = 0.99999,n = 1000000) == 4.539765980992338e-05
    assert candidate(x = 5.0,n = 0) == 1
    assert candidate(x = 2.0,n = -10) == 0.0009765625
    assert candidate(x = 1.0,n = -5) == 1.0
    assert candidate(x = 1.00001,n = -1000) == 0.9900498832512471
    assert candidate(x = -1.5,n = 5) == -7.59375
    assert candidate(x = 1.0,n = 2147483647) == 1.0


