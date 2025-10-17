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
        result = candidate(n = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 2499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 2499: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 249: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 625) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625) == 156: {e}')
    
    total += 1
    try:
        result = candidate(n = 15000) == 3748
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15000) == 3748: {e}')
    
    total += 1
    try:
        result = candidate(n = 1875) == 468
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1875) == 468: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000) == 999: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 2345) == 583
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2345) == 583: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 24994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 24994: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 62499) == 15618
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 62499) == 15618: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == 1021
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == 1021: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 499: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 1874
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 1874: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 12499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 12499: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 2304) == 573
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2304) == 573: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 31249) == 7806
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31249) == 7806: {e}')
    
    total += 1
    try:
        result = candidate(n = 15625) == 3906
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15625) == 3906: {e}')
    
    total += 1
    try:
        result = candidate(n = 31250) == 7812
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31250) == 7812: {e}')
    
    total += 1
    try:
        result = candidate(n = 2050) == 511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2050) == 511: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 253: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 62: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 24999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 24999: {e}')
    
    total += 1
    try:
        result = candidate(n = 15624) == 3900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15624) == 3900: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 4999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 4999: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == 509
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == 509: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == 2045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == 2045: {e}')
    
    total += 1
    try:
        result = candidate(n = 375) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 375) == 93: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 246: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(n = 62500) == 15624
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 62500) == 15624: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 1249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 1249: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 2495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 2495: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 149) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 149) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 249) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 249) == 59: {e}')
    
    total += 1
    try:
        result = candidate(n = 1250) == 312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1250) == 312: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7654) == 1911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7654) == 1911: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 8750) == 2186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8750) == 2186: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 624
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 624: {e}')
    
    total += 1
    try:
        result = candidate(n = 4999) == 1245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4999) == 1245: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 305: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3125) == 781
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3125) == 781: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876) == 2467
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876) == 2467: {e}')
    
    total += 1
    try:
        result = candidate(n = 7812) == 1950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7812) == 1950: {e}')
    
    total += 1
    try:
        result = candidate(n = 124) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 124) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 1249) == 308
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1249) == 308: {e}')
    
    total += 1
    try:
        result = candidate(n = 499) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499) == 121: {e}')
    
    total += 1
    try:
        result = candidate(n = 199) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199) == 47: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 124: {e}')
    
    total += 1
    try:
        result = candidate(n = 180) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180) == 44: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 3) == 0
    assert candidate(n = 10000) == 2499
    assert candidate(n = 25) == 6
    assert candidate(n = 100) == 24
    assert candidate(n = 1000) == 249
    assert candidate(n = 10) == 2
    assert candidate(n = 5) == 1
    assert candidate(n = 625) == 156
    assert candidate(n = 15000) == 3748
    assert candidate(n = 1875) == 468
    assert candidate(n = 4000) == 999
    assert candidate(n = 29) == 6
    assert candidate(n = 2345) == 583
    assert candidate(n = 99999) == 24994
    assert candidate(n = 49) == 10
    assert candidate(n = 125) == 31
    assert candidate(n = 62499) == 15618
    assert candidate(n = 4096) == 1021
    assert candidate(n = 2000) == 499
    assert candidate(n = 7500) == 1874
    assert candidate(n = 50000) == 12499
    assert candidate(n = 50) == 12
    assert candidate(n = 2304) == 573
    assert candidate(n = 30) == 7
    assert candidate(n = 4) == 0
    assert candidate(n = 99) == 22
    assert candidate(n = 31249) == 7806
    assert candidate(n = 15625) == 3906
    assert candidate(n = 31250) == 7812
    assert candidate(n = 2050) == 511
    assert candidate(n = 1024) == 253
    assert candidate(n = 250) == 62
    assert candidate(n = 100000) == 24999
    assert candidate(n = 15624) == 3900
    assert candidate(n = 20000) == 4999
    assert candidate(n = 2048) == 509
    assert candidate(n = 8192) == 2045
    assert candidate(n = 375) == 93
    assert candidate(n = 999) == 246
    assert candidate(n = 8000) == 1998
    assert candidate(n = 62500) == 15624
    assert candidate(n = 18) == 3
    assert candidate(n = 5000) == 1249
    assert candidate(n = 9999) == 2495
    assert candidate(n = 20) == 4
    assert candidate(n = 149) == 35
    assert candidate(n = 19) == 3
    assert candidate(n = 249) == 59
    assert candidate(n = 1250) == 312
    assert candidate(n = 24) == 4
    assert candidate(n = 7654) == 1911
    assert candidate(n = 150) == 37
    assert candidate(n = 8750) == 2186
    assert candidate(n = 15) == 3
    assert candidate(n = 2500) == 624
    assert candidate(n = 4999) == 1245
    assert candidate(n = 200) == 49
    assert candidate(n = 14) == 2
    assert candidate(n = 1234) == 305
    assert candidate(n = 9) == 1
    assert candidate(n = 3125) == 781
    assert candidate(n = 9876) == 2467
    assert candidate(n = 7812) == 1950
    assert candidate(n = 124) == 28
    assert candidate(n = 1249) == 308
    assert candidate(n = 499) == 121
    assert candidate(n = 199) == 47
    assert candidate(n = 1) == 0
    assert candidate(n = 500) == 124
    assert candidate(n = 180) == 44


