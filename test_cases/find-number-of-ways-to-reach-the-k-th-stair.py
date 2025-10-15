def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 10000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 10000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 100000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 127) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 127) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 8388608) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8388608) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 63) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 63) == 7: {e}')
    
    total += 1
    try:
        result = candidate(k = 65536) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 65536) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 16384) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 16384) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 5000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 60000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 60000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 4194304) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4194304) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 8191) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8191) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 30000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 30000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 750000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 750000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 4096) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4096) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 65535) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 65535) == 17: {e}')
    
    total += 1
    try:
        result = candidate(k = 536870912) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 536870912) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 2048) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2048) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000001) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000001) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 8192) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8192) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 20000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 5000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 32767) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 32767) == 16: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 524288) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 524288) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000010) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000010) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 32768) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 32768) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 23) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 23) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 500000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 1073741824) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1073741824) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 131072) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 131072) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 268435456) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 268435456) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 4095) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4095) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 33554432) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 33554432) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 999999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 64) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 64) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 70000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 70000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 31) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 31) == 6: {e}')
    
    total += 1
    try:
        result = candidate(k = 1100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 50000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 16) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 16) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 2097152) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2097152) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 999999999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 256) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 256) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 262144) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 262144) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 134217728) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 134217728) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1001000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1001000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 90000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 90000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 2047) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2047) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(k = 1024) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1024) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 67108864) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 67108864) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 1048576) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1048576) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 255) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 255) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 512) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 512) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 80000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 80000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 1023) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1023) == 11: {e}')
    
    total += 1
    try:
        result = candidate(k = 16777216) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 16777216) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 40000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 40000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 511) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 511) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 1010000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1010000) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(k = 1000) == 0
    assert candidate(k = 100) == 0
    assert candidate(k = 20) == 0
    assert candidate(k = 1000000000) == 0
    assert candidate(k = 1) == 4
    assert candidate(k = 10) == 0
    assert candidate(k = 10000) == 0
    assert candidate(k = 500) == 0
    assert candidate(k = 1000000) == 0
    assert candidate(k = 10000000) == 0
    assert candidate(k = 3) == 3
    assert candidate(k = 100000000) == 0
    assert candidate(k = 0) == 2
    assert candidate(k = 2) == 4
    assert candidate(k = 100000) == 0
    assert candidate(k = 5) == 4
    assert candidate(k = 4) == 2
    assert candidate(k = 50) == 0
    assert candidate(k = 127) == 8
    assert candidate(k = 8388608) == 1
    assert candidate(k = 63) == 7
    assert candidate(k = 65536) == 1
    assert candidate(k = 16384) == 1
    assert candidate(k = 5000) == 0
    assert candidate(k = 60000000) == 0
    assert candidate(k = 4194304) == 1
    assert candidate(k = 8191) == 14
    assert candidate(k = 30000000) == 0
    assert candidate(k = 750000) == 0
    assert candidate(k = 4096) == 1
    assert candidate(k = 65535) == 17
    assert candidate(k = 536870912) == 1
    assert candidate(k = 2048) == 1
    assert candidate(k = 1000001) == 0
    assert candidate(k = 8192) == 1
    assert candidate(k = 20000000) == 0
    assert candidate(k = 5000000) == 0
    assert candidate(k = 32767) == 16
    assert candidate(k = 1000100) == 0
    assert candidate(k = 524288) == 1
    assert candidate(k = 1000010) == 0
    assert candidate(k = 9) == 0
    assert candidate(k = 32768) == 1
    assert candidate(k = 23) == 0
    assert candidate(k = 500000) == 0
    assert candidate(k = 1073741824) == 1
    assert candidate(k = 131072) == 1
    assert candidate(k = 268435456) == 1
    assert candidate(k = 4095) == 13
    assert candidate(k = 15) == 5
    assert candidate(k = 33554432) == 1
    assert candidate(k = 999999) == 0
    assert candidate(k = 64) == 1
    assert candidate(k = 70000000) == 0
    assert candidate(k = 31) == 6
    assert candidate(k = 1100000) == 0
    assert candidate(k = 50000000) == 0
    assert candidate(k = 16) == 1
    assert candidate(k = 2097152) == 1
    assert candidate(k = 999999999) == 0
    assert candidate(k = 256) == 1
    assert candidate(k = 262144) == 1
    assert candidate(k = 134217728) == 1
    assert candidate(k = 1001000) == 0
    assert candidate(k = 90000000) == 0
    assert candidate(k = 2047) == 12
    assert candidate(k = 30) == 15
    assert candidate(k = 1024) == 1
    assert candidate(k = 67108864) == 1
    assert candidate(k = 7) == 4
    assert candidate(k = 1048576) == 1
    assert candidate(k = 255) == 9
    assert candidate(k = 512) == 1
    assert candidate(k = 80000000) == 0
    assert candidate(k = 1023) == 11
    assert candidate(k = 16777216) == 1
    assert candidate(k = 40000000) == 0
    assert candidate(k = 511) == 10
    assert candidate(k = 1010000) == 0


