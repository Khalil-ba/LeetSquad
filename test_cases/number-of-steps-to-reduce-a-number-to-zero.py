def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 14) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 14) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == 26: {e}')
    
    total += 1
    try:
        result = candidate(num = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 65535) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65535) == 31: {e}')
    
    total += 1
    try:
        result = candidate(num = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 123) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123) == 12: {e}')
    
    total += 1
    try:
        result = candidate(num = 8191) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8191) == 25: {e}')
    
    total += 1
    try:
        result = candidate(num = 750000) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 750000) == 29: {e}')
    
    total += 1
    try:
        result = candidate(num = 500000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567) == 31: {e}')
    
    total += 1
    try:
        result = candidate(num = 131072) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 131072) == 18: {e}')
    
    total += 1
    try:
        result = candidate(num = 1023) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1023) == 19: {e}')
    
    total += 1
    try:
        result = candidate(num = 777777) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777777) == 31: {e}')
    
    total += 1
    try:
        result = candidate(num = 127) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 127) == 13: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num = 16384) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16384) == 15: {e}')
    
    total += 1
    try:
        result = candidate(num = 31) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 31) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 100001) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100001) == 23: {e}')
    
    total += 1
    try:
        result = candidate(num = 1048575) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1048575) == 39: {e}')
    
    total += 1
    try:
        result = candidate(num = 8192) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8192) == 14: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 42: {e}')
    
    total += 1
    try:
        result = candidate(num = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 135792468) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 135792468) == 36: {e}')
    
    total += 1
    try:
        result = candidate(num = 32768) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32768) == 16: {e}')
    
    total += 1
    try:
        result = candidate(num = 63) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 63) == 11: {e}')
    
    total += 1
    try:
        result = candidate(num = 3125) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3125) == 17: {e}')
    
    total += 1
    try:
        result = candidate(num = 5318008) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5318008) == 32: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000002) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000002) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num = 2097151) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2097151) == 41: {e}')
    
    total += 1
    try:
        result = candidate(num = 131071) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 131071) == 33: {e}')
    
    total += 1
    try:
        result = candidate(num = 16383) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16383) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num = 665772) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 665772) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 46: {e}')
    
    total += 1
    try:
        result = candidate(num = 4096) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4096) == 13: {e}')
    
    total += 1
    try:
        result = candidate(num = 511) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 511) == 17: {e}')
    
    total += 1
    try:
        result = candidate(num = 524288) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 524288) == 20: {e}')
    
    total += 1
    try:
        result = candidate(num = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 543210) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 543210) == 28: {e}')
    
    total += 1
    try:
        result = candidate(num = 1048576) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1048576) == 21: {e}')
    
    total += 1
    try:
        result = candidate(num = 567890) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 567890) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num = 255) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 255) == 15: {e}')
    
    total += 1
    try:
        result = candidate(num = 8675309) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8675309) == 37: {e}')
    
    total += 1
    try:
        result = candidate(num = 1024) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1024) == 11: {e}')
    
    total += 1
    try:
        result = candidate(num = 246813579) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 246813579) == 42: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000) == 22: {e}')
    
    total += 1
    try:
        result = candidate(num = 54321) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 54321) == 22: {e}')
    
    total += 1
    try:
        result = candidate(num = 262143) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 262143) == 35: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456) == 22: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999) == 31: {e}')
    
    total += 1
    try:
        result = candidate(num = 32767) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32767) == 29: {e}')
    
    total += 1
    try:
        result = candidate(num = 65536) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65536) == 17: {e}')
    
    total += 1
    try:
        result = candidate(num = 2048) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2048) == 12: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000001) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000001) == 27: {e}')
    
    total += 1
    try:
        result = candidate(num = 536870911) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 536870911) == 57: {e}')
    
    total += 1
    try:
        result = candidate(num = 2147483647) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2147483647) == 61: {e}')
    
    total += 1
    try:
        result = candidate(num = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654) == 27: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 14) == 6
    assert candidate(num = 1000000) == 26
    assert candidate(num = 8) == 4
    assert candidate(num = 65535) == 31
    assert candidate(num = 0) == 0
    assert candidate(num = 2) == 2
    assert candidate(num = 1) == 1
    assert candidate(num = 123) == 12
    assert candidate(num = 8191) == 25
    assert candidate(num = 750000) == 29
    assert candidate(num = 500000) == 25
    assert candidate(num = 1234567) == 31
    assert candidate(num = 131072) == 18
    assert candidate(num = 1023) == 19
    assert candidate(num = 777777) == 31
    assert candidate(num = 127) == 13
    assert candidate(num = 888888) == 27
    assert candidate(num = 16384) == 15
    assert candidate(num = 31) == 9
    assert candidate(num = 100001) == 23
    assert candidate(num = 1048575) == 39
    assert candidate(num = 8192) == 14
    assert candidate(num = 123456789) == 42
    assert candidate(num = 15) == 7
    assert candidate(num = 135792468) == 36
    assert candidate(num = 32768) == 16
    assert candidate(num = 63) == 11
    assert candidate(num = 3125) == 17
    assert candidate(num = 5318008) == 32
    assert candidate(num = 1000002) == 27
    assert candidate(num = 2097151) == 41
    assert candidate(num = 131071) == 33
    assert candidate(num = 16383) == 27
    assert candidate(num = 665772) == 27
    assert candidate(num = 987654321) == 46
    assert candidate(num = 4096) == 13
    assert candidate(num = 511) == 17
    assert candidate(num = 524288) == 20
    assert candidate(num = 7) == 5
    assert candidate(num = 543210) == 28
    assert candidate(num = 1048576) == 21
    assert candidate(num = 567890) == 27
    assert candidate(num = 255) == 15
    assert candidate(num = 8675309) == 37
    assert candidate(num = 1024) == 11
    assert candidate(num = 246813579) == 42
    assert candidate(num = 100000) == 22
    assert candidate(num = 54321) == 22
    assert candidate(num = 262143) == 35
    assert candidate(num = 123456) == 22
    assert candidate(num = 999999) == 31
    assert candidate(num = 32767) == 29
    assert candidate(num = 65536) == 17
    assert candidate(num = 2048) == 12
    assert candidate(num = 1000001) == 27
    assert candidate(num = 536870911) == 57
    assert candidate(num = 2147483647) == 61
    assert candidate(num = 3) == 3
    assert candidate(num = 987654) == 27


