def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 38: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 317) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 317) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 2047) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2047) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 16383) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16383) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 51) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 51) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 513) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 513) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 24: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 3
    assert candidate(n = 15) == 5
    assert candidate(n = 4) == 2
    assert candidate(n = 2147483647) == 32
    assert candidate(n = 1) == 0
    assert candidate(n = 1000000000) == 38
    assert candidate(n = 7) == 4
    assert candidate(n = 317) == 11
    assert candidate(n = 63) == 7
    assert candidate(n = 21) == 6
    assert candidate(n = 32767) == 16
    assert candidate(n = 50000) == 20
    assert candidate(n = 2047) == 12
    assert candidate(n = 16383) == 15
    assert candidate(n = 5) == 3
    assert candidate(n = 123) == 9
    assert candidate(n = 134217727) == 28
    assert candidate(n = 64) == 6
    assert candidate(n = 99) == 9
    assert candidate(n = 1073741823) == 31
    assert candidate(n = 23) == 6
    assert candidate(n = 51) == 8
    assert candidate(n = 16777215) == 25
    assert candidate(n = 101) == 9
    assert candidate(n = 99999999) == 32
    assert candidate(n = 2048) == 11
    assert candidate(n = 999) == 13
    assert candidate(n = 27) == 7
    assert candidate(n = 8191) == 14
    assert candidate(n = 1023) == 11
    assert candidate(n = 19) == 6
    assert candidate(n = 65535) == 17
    assert candidate(n = 513) == 10
    assert candidate(n = 127) == 8
    assert candidate(n = 1048575) == 21
    assert candidate(n = 31) == 6
    assert candidate(n = 1000000) == 24


