def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 100) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100) == 19: {e}')
    
    total += 1
    try:
        result = candidate(target = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000) == 23: {e}')
    
    total += 1
    try:
        result = candidate(target = 999) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 999) == 20: {e}')
    
    total += 1
    try:
        result = candidate(target = 16383) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16383) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = 5000) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5000) == 41: {e}')
    
    total += 1
    try:
        result = candidate(target = 8) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 6553) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 6553) == 53: {e}')
    
    total += 1
    try:
        result = candidate(target = 65535) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 65535) == 16: {e}')
    
    total += 1
    try:
        result = candidate(target = 25) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 25) == 11: {e}')
    
    total += 1
    try:
        result = candidate(target = 5120) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5120) == 29: {e}')
    
    total += 1
    try:
        result = candidate(target = 200) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 200) == 22: {e}')
    
    total += 1
    try:
        result = candidate(target = 32767) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 32767) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 29) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 29) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 2047) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2047) == 11: {e}')
    
    total += 1
    try:
        result = candidate(target = 31) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 31) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 3000) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 3000) == 33: {e}')
    
    total += 1
    try:
        result = candidate(target = 2000) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2000) == 26: {e}')
    
    total += 1
    try:
        result = candidate(target = 123) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 123) == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = 8192) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8192) == 16: {e}')
    
    total += 1
    try:
        result = candidate(target = 40) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 40) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 8191) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 8191) == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = 17) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 17) == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = 20) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20) == 12: {e}')
    
    total += 1
    try:
        result = candidate(target = 10000) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10000) == 45: {e}')
    
    total += 1
    try:
        result = candidate(target = 500) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500) == 20: {e}')
    
    total += 1
    try:
        result = candidate(target = 750) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 750) == 25: {e}')
    
    total += 1
    try:
        result = candidate(target = 9999) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 9999) == 43: {e}')
    
    total += 1
    try:
        result = candidate(target = 250) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 250) == 16: {e}')
    
    total += 1
    try:
        result = candidate(target = 63) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 63) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 65536) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 65536) == 19: {e}')
    
    total += 1
    try:
        result = candidate(target = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 32768) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 32768) == 18: {e}')
    
    total += 1
    try:
        result = candidate(target = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = 42) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 42) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 1024) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1024) == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = 50) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 50) == 16: {e}')
    
    total += 1
    try:
        result = candidate(target = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 4096) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4096) == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = 4095) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 4095) == 12: {e}')
    
    total += 1
    try:
        result = candidate(target = 16) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 16) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 99) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 99) == 16: {e}')
    
    total += 1
    try:
        result = candidate(target = 2048) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 2048) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = 5432) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5432) == 45: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = 3) == 2
    assert candidate(target = 6) == 5
    assert candidate(target = 4) == 5
    assert candidate(target = 10) == 7
    assert candidate(target = 1) == 1
    assert candidate(target = 100) == 19
    assert candidate(target = 15) == 4
    assert candidate(target = 1000) == 23
    assert candidate(target = 999) == 20
    assert candidate(target = 16383) == 14
    assert candidate(target = 5000) == 41
    assert candidate(target = 8) == 6
    assert candidate(target = 6553) == 53
    assert candidate(target = 65535) == 16
    assert candidate(target = 25) == 11
    assert candidate(target = 5120) == 29
    assert candidate(target = 200) == 22
    assert candidate(target = 32767) == 15
    assert candidate(target = 29) == 10
    assert candidate(target = 2047) == 11
    assert candidate(target = 31) == 5
    assert candidate(target = 3000) == 33
    assert candidate(target = 2000) == 26
    assert candidate(target = 123) == 13
    assert candidate(target = 8192) == 16
    assert candidate(target = 40) == 15
    assert candidate(target = 8191) == 13
    assert candidate(target = 17) == 9
    assert candidate(target = 20) == 12
    assert candidate(target = 10000) == 45
    assert candidate(target = 500) == 20
    assert candidate(target = 750) == 25
    assert candidate(target = 9999) == 43
    assert candidate(target = 250) == 16
    assert candidate(target = 63) == 6
    assert candidate(target = 65536) == 19
    assert candidate(target = 7) == 3
    assert candidate(target = 32768) == 18
    assert candidate(target = 1023) == 10
    assert candidate(target = 42) == 15
    assert candidate(target = 1024) == 13
    assert candidate(target = 50) == 16
    assert candidate(target = 30) == 7
    assert candidate(target = 4096) == 15
    assert candidate(target = 4095) == 12
    assert candidate(target = 16) == 7
    assert candidate(target = 99) == 16
    assert candidate(target = 2048) == 14
    assert candidate(target = 5432) == 45


