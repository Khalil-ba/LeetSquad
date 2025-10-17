def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 31) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 31) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 32) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32) == 31: {e}')
    
    total += 1
    try:
        result = candidate(num = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 1023) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1023) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num = 2147483647) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2147483647) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 8191) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8191) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 4294967295) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4294967295) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 33) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33) == 30: {e}')
    
    total += 1
    try:
        result = candidate(num = 4095) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4095) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1048575) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1048575) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 10760938
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 10760938: {e}')
    
    total += 1
    try:
        result = candidate(num = 65535) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65535) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 500) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500) == 11: {e}')
    
    total += 1
    try:
        result = candidate(num = 2097151) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2097151) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 131071) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 131071) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 16777215) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16777215) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 2147483646) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2147483646) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 134217728) == 134217727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 134217728) == 134217727: {e}')
    
    total += 1
    try:
        result = candidate(num = 4194303) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4194303) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 2047) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2047) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 86087502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 86087502: {e}')
    
    total += 1
    try:
        result = candidate(num = 89123456) == 45094271
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 89123456) == 45094271: {e}')
    
    total += 1
    try:
        result = candidate(num = 255) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 255) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 8388607) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8388607) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1024) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1024) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000) == 31071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000) == 31071: {e}')
    
    total += 1
    try:
        result = candidate(num = 1073741823) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1073741823) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 262143) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 262143) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 268435455) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 268435455) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456) == 7615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456) == 7615: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == 48575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == 48575: {e}')
    
    total += 1
    try:
        result = candidate(num = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 32767) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32767) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 524287) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 524287) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 134217727) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 134217727) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 4294967294) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4294967294) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 33554431) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33554431) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 536870911) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 536870911) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 67108863) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 67108863) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1073741824) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1073741824) == 1073741823: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 31) == 0
    assert candidate(num = 10) == 5
    assert candidate(num = 32) == 31
    assert candidate(num = 5) == 2
    assert candidate(num = 1023) == 0
    assert candidate(num = 1) == 0
    assert candidate(num = 100) == 27
    assert candidate(num = 2147483647) == 0
    assert candidate(num = 15) == 0
    assert candidate(num = 8191) == 0
    assert candidate(num = 4294967295) == 0
    assert candidate(num = 33) == 30
    assert candidate(num = 4095) == 0
    assert candidate(num = 1048575) == 0
    assert candidate(num = 123456789) == 10760938
    assert candidate(num = 65535) == 0
    assert candidate(num = 500) == 11
    assert candidate(num = 2097151) == 0
    assert candidate(num = 131071) == 0
    assert candidate(num = 16777215) == 0
    assert candidate(num = 2147483646) == 1
    assert candidate(num = 134217728) == 134217727
    assert candidate(num = 4194303) == 0
    assert candidate(num = 2047) == 0
    assert candidate(num = 987654321) == 86087502
    assert candidate(num = 89123456) == 45094271
    assert candidate(num = 255) == 0
    assert candidate(num = 8388607) == 0
    assert candidate(num = 1024) == 1023
    assert candidate(num = 100000) == 31071
    assert candidate(num = 1073741823) == 0
    assert candidate(num = 262143) == 0
    assert candidate(num = 268435455) == 0
    assert candidate(num = 123456) == 7615
    assert candidate(num = 1000000) == 48575
    assert candidate(num = 8) == 7
    assert candidate(num = 32767) == 0
    assert candidate(num = 524287) == 0
    assert candidate(num = 134217727) == 0
    assert candidate(num = 4294967294) == 1
    assert candidate(num = 33554431) == 0
    assert candidate(num = 536870911) == 0
    assert candidate(num = 67108863) == 0
    assert candidate(num = 1073741824) == 1073741823


