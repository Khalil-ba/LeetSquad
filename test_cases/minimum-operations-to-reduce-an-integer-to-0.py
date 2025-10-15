def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 54) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 39) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 39) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 32768) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32768) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 65534) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65534) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 33333) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33333) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 8765) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8765) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 7456) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7456) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 77777) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77777) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 67890) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67890) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 65537) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65537) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 65533) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65533) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 86420) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 86420) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 19683) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19683) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 16383) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16383) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 24680) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24680) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 16384) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16384) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10001) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10001) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 81920) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81920) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1365) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1365) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 32769) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32769) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4095) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4095) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 7890) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7890) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 11001) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11001) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 39321) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 39321) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 13579) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13579) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 43210) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43210) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 531441) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 531441) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1536) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1536) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 2
    assert candidate(n = 63) == 2
    assert candidate(n = 100) == 3
    assert candidate(n = 50000) == 6
    assert candidate(n = 4) == 1
    assert candidate(n = 64) == 1
    assert candidate(n = 16) == 1
    assert candidate(n = 10000) == 4
    assert candidate(n = 2) == 1
    assert candidate(n = 1024) == 1
    assert candidate(n = 54) == 3
    assert candidate(n = 100000) == 6
    assert candidate(n = 1048576) == 1
    assert candidate(n = 65536) == 1
    assert candidate(n = 32) == 1
    assert candidate(n = 1023) == 2
    assert candidate(n = 39) == 3
    assert candidate(n = 65535) == 2
    assert candidate(n = 15) == 2
    assert candidate(n = 32768) == 1
    assert candidate(n = 1048575) == 2
    assert candidate(n = 31) == 2
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 2
    assert candidate(n = 65534) == 2
    assert candidate(n = 33333) == 6
    assert candidate(n = 99999) == 7
    assert candidate(n = 8765) == 5
    assert candidate(n = 131071) == 2
    assert candidate(n = 12345) == 5
    assert candidate(n = 7456) == 4
    assert candidate(n = 77777) == 6
    assert candidate(n = 67890) == 6
    assert candidate(n = 65537) == 2
    assert candidate(n = 111111) == 6
    assert candidate(n = 32767) == 2
    assert candidate(n = 65533) == 3
    assert candidate(n = 86420) == 7
    assert candidate(n = 19683) == 7
    assert candidate(n = 16383) == 2
    assert candidate(n = 24680) == 5
    assert candidate(n = 16384) == 1
    assert candidate(n = 123) == 3
    assert candidate(n = 10001) == 5
    assert candidate(n = 81920) == 2
    assert candidate(n = 1365) == 6
    assert candidate(n = 32769) == 2
    assert candidate(n = 4095) == 2
    assert candidate(n = 8192) == 1
    assert candidate(n = 999) == 4
    assert candidate(n = 8191) == 2
    assert candidate(n = 7890) == 5
    assert candidate(n = 11001) == 6
    assert candidate(n = 39321) == 8
    assert candidate(n = 13579) == 7
    assert candidate(n = 98765) == 7
    assert candidate(n = 43210) == 7
    assert candidate(n = 54321) == 7
    assert candidate(n = 531441) == 5
    assert candidate(n = 1536) == 2


