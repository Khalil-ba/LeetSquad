def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 10760938
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 10760938: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 894567890) == 179173933
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 894567890) == 179173933: {e}')
    
    total += 1
    try:
        result = candidate(n = 890123456) == 183618367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 890123456) == 183618367: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 897543210) == 176198613
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 897543210) == 176198613: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108863) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108863) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 67890) == 63181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67890) == 63181: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967295) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967295) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 891011121) == 182730702
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 891011121) == 182730702: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == 2047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == 2047: {e}')
    
    total += 1
    try:
        result = candidate(n = 255) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 73741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 73741823: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 86087502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 86087502: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 36870911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 36870911: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 543210987) == 530530836
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543210987) == 530530836: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == 11214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == 11214: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 1
    assert candidate(n = 8) == 7
    assert candidate(n = 100) == 27
    assert candidate(n = 15) == 0
    assert candidate(n = 31) == 0
    assert candidate(n = 123456789) == 10760938
    assert candidate(n = 1) == 0
    assert candidate(n = 7) == 0
    assert candidate(n = 10) == 5
    assert candidate(n = 5) == 2
    assert candidate(n = 123) == 4
    assert candidate(n = 894567890) == 179173933
    assert candidate(n = 890123456) == 183618367
    assert candidate(n = 131071) == 0
    assert candidate(n = 897543210) == 176198613
    assert candidate(n = 67108863) == 0
    assert candidate(n = 2147483647) == 0
    assert candidate(n = 67890) == 63181
    assert candidate(n = 32767) == 0
    assert candidate(n = 4294967295) == 0
    assert candidate(n = 134217727) == 0
    assert candidate(n = 891011121) == 182730702
    assert candidate(n = 1073741823) == 0
    assert candidate(n = 1024) == 1023
    assert candidate(n = 16777215) == 0
    assert candidate(n = 2048) == 2047
    assert candidate(n = 255) == 0
    assert candidate(n = 1023) == 0
    assert candidate(n = 65535) == 0
    assert candidate(n = 1000000000) == 73741823
    assert candidate(n = 987654321) == 86087502
    assert candidate(n = 1048575) == 0
    assert candidate(n = 500000000) == 36870911
    assert candidate(n = 536870911) == 0
    assert candidate(n = 543210987) == 530530836
    assert candidate(n = 33554431) == 0
    assert candidate(n = 54321) == 11214


