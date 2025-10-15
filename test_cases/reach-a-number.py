def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = -20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = -5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = -10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 5000) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5000) == 100: {e}')
    
    total += 1
    try:
        result = candidate(target = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 123456789) == 15713
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 123456789) == 15713: {e}')
    
    total += 1
    try:
        result = candidate(target = -21) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -21) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = -123456) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -123456) == 499: {e}')
    
    total += 1
    try:
        result = candidate(target = 25) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 25) == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = -987654) == 1407
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -987654) == 1407: {e}')
    
    total += 1
    try:
        result = candidate(target = 65535) == 362
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 65535) == 362: {e}')
    
    total += 1
    try:
        result = candidate(target = -17) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -17) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 999999999) == 44721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 999999999) == 44721: {e}')
    
    total += 1
    try:
        result = candidate(target = 60) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 60) == 11: {e}')
    
    total += 1
    try:
        result = candidate(target = 45) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 45) == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = 500000001) == 31625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500000001) == 31625: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000) == 47: {e}')
    
    total += 1
    try:
        result = candidate(target = 987654321) == 44445
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 987654321) == 44445: {e}')
    
    total += 1
    try:
        result = candidate(target = 500000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(target = -987654321) == 44445
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -987654321) == 44445: {e}')
    
    total += 1
    try:
        result = candidate(target = -101) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -101) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 55) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 55) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 12345) == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 12345) == 157: {e}')
    
    total += 1
    try:
        result = candidate(target = 17) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 17) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = -500000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -500000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000000) == 1415
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000000) == 1415: {e}')
    
    total += 1
    try:
        result = candidate(target = -501) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -501) == 33: {e}')
    
    total += 1
    try:
        result = candidate(target = -2147483647) == 65537
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -2147483647) == 65537: {e}')
    
    total += 1
    try:
        result = candidate(target = -15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = -100) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -100) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 13) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 13) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 81) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 81) == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = 500) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500) == 32: {e}')
    
    total += 1
    try:
        result = candidate(target = -5000) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -5000) == 100: {e}')
    
    total += 1
    try:
        result = candidate(target = -1024) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -1024) == 47: {e}')
    
    total += 1
    try:
        result = candidate(target = 101) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 101) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = -75) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -75) == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = -123456789) == 15713
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -123456789) == 15713: {e}')
    
    total += 1
    try:
        result = candidate(target = 1023) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1023) == 45: {e}')
    
    total += 1
    try:
        result = candidate(target = 100) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 2048) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2048) == 64: {e}')
    
    total += 1
    try:
        result = candidate(target = 1024) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1024) == 47: {e}')
    
    total += 1
    try:
        result = candidate(target = -25) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -25) == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = -1000000000) == 44723
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -1000000000) == 44723: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000000000) == 44723
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000000000) == 44723: {e}')
    
    total += 1
    try:
        result = candidate(target = 50) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 50) == 11: {e}')
    
    total += 1
    try:
        result = candidate(target = 499999999) == 31625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 499999999) == 31625: {e}')
    
    total += 1
    try:
        result = candidate(target = -500) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -500) == 32: {e}')
    
    total += 1
    try:
        result = candidate(target = -1023) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -1023) == 45: {e}')
    
    total += 1
    try:
        result = candidate(target = -999999999) == 44721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -999999999) == 44721: {e}')
    
    total += 1
    try:
        result = candidate(target = 14) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 14) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 4096) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4096) == 91: {e}')
    
    total += 1
    try:
        result = candidate(target = 501) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 501) == 33: {e}')
    
    total += 1
    try:
        result = candidate(target = -1000) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -1000) == 47: {e}')
    
    total += 1
    try:
        result = candidate(target = 123456) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 123456) == 499: {e}')
    
    total += 1
    try:
        result = candidate(target = 100000000) == 14143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100000000) == 14143: {e}')
    
    total += 1
    try:
        result = candidate(target = -100000000) == 14143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -100000000) == 14143: {e}')
    
    total += 1
    try:
        result = candidate(target = -65535) == 362
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -65535) == 362: {e}')
    
    total += 1
    try:
        result = candidate(target = -12) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -12) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = -999999) == 1414
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = -999999) == 1414: {e}')
    
    total += 1
    try:
        result = candidate(target = 200) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 200) == 20: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = 2) == 3
    assert candidate(target = -20) == 7
    assert candidate(target = 15) == 5
    assert candidate(target = 10) == 4
    assert candidate(target = -5) == 5
    assert candidate(target = 1) == 1
    assert candidate(target = -1) == 1
    assert candidate(target = 3) == 2
    assert candidate(target = 20) == 7
    assert candidate(target = -10) == 4
    assert candidate(target = 5000) == 100
    assert candidate(target = 8) == 4
    assert candidate(target = 123456789) == 15713
    assert candidate(target = -21) == 6
    assert candidate(target = -123456) == 499
    assert candidate(target = 25) == 9
    assert candidate(target = -987654) == 1407
    assert candidate(target = 65535) == 362
    assert candidate(target = -17) == 6
    assert candidate(target = 999999999) == 44721
    assert candidate(target = 60) == 11
    assert candidate(target = 45) == 9
    assert candidate(target = 500000001) == 31625
    assert candidate(target = 1000) == 47
    assert candidate(target = 987654321) == 44445
    assert candidate(target = 500000) == 1000
    assert candidate(target = -987654321) == 44445
    assert candidate(target = -101) == 14
    assert candidate(target = 5) == 5
    assert candidate(target = 55) == 10
    assert candidate(target = 12345) == 157
    assert candidate(target = 17) == 6
    assert candidate(target = -500000) == 1000
    assert candidate(target = 1000000) == 1415
    assert candidate(target = -501) == 33
    assert candidate(target = -2147483647) == 65537
    assert candidate(target = -15) == 5
    assert candidate(target = -100) == 15
    assert candidate(target = 13) == 5
    assert candidate(target = 81) == 13
    assert candidate(target = 500) == 32
    assert candidate(target = -5000) == 100
    assert candidate(target = -1024) == 47
    assert candidate(target = 101) == 14
    assert candidate(target = -75) == 13
    assert candidate(target = 7) == 5
    assert candidate(target = -123456789) == 15713
    assert candidate(target = 1023) == 45
    assert candidate(target = 100) == 15
    assert candidate(target = 2048) == 64
    assert candidate(target = 1024) == 47
    assert candidate(target = -25) == 9
    assert candidate(target = -1000000000) == 44723
    assert candidate(target = 1000000000) == 44723
    assert candidate(target = 50) == 11
    assert candidate(target = 499999999) == 31625
    assert candidate(target = -500) == 32
    assert candidate(target = -1023) == 45
    assert candidate(target = -999999999) == 44721
    assert candidate(target = 14) == 7
    assert candidate(target = 4096) == 91
    assert candidate(target = 501) == 33
    assert candidate(target = -1000) == 47
    assert candidate(target = 123456) == 499
    assert candidate(target = 100000000) == 14143
    assert candidate(target = -100000000) == 14143
    assert candidate(target = -65535) == 362
    assert candidate(target = -12) == 7
    assert candidate(target = -999999) == 1414
    assert candidate(target = 200) == 20


