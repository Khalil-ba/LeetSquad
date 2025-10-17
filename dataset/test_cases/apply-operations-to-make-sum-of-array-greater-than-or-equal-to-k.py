def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(k = 100) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100) == 18: {e}')
    
    total += 1
    try:
        result = candidate(k = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(k = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(k = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 100000) == 631
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000) == 631: {e}')
    
    total += 1
    try:
        result = candidate(k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 29) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 29) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 30) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 30) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 101) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 101) == 19: {e}')
    
    total += 1
    try:
        result = candidate(k = 2048) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2048) == 89: {e}')
    
    total += 1
    try:
        result = candidate(k = 1024) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1024) == 62: {e}')
    
    total += 1
    try:
        result = candidate(k = 9999) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9999) == 198: {e}')
    
    total += 1
    try:
        result = candidate(k = 999) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999) == 62: {e}')
    
    total += 1
    try:
        result = candidate(k = 500) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500) == 43: {e}')
    
    total += 1
    try:
        result = candidate(k = 49) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 49) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 8192) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8192) == 180: {e}')
    
    total += 1
    try:
        result = candidate(k = 50) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 127) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 127) == 21: {e}')
    
    total += 1
    try:
        result = candidate(k = 64) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 64) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 17) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 17) == 7: {e}')
    
    total += 1
    try:
        result = candidate(k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 63) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 63) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 99) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99) == 18: {e}')
    
    total += 1
    try:
        result = candidate(k = 31) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 31) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 13) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 13) == 6: {e}')
    
    total += 1
    try:
        result = candidate(k = 65536) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 65536) == 510: {e}')
    
    total += 1
    try:
        result = candidate(k = 16384) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 16384) == 254: {e}')
    
    total += 1
    try:
        result = candidate(k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 12345) == 221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 12345) == 221: {e}')
    
    total += 1
    try:
        result = candidate(k = 42) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 42) == 11: {e}')
    
    total += 1
    try:
        result = candidate(k = 67890) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 67890) == 520: {e}')
    
    total += 1
    try:
        result = candidate(k = 200) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 200) == 27: {e}')
    
    total += 1
    try:
        result = candidate(k = 99999) == 631
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99999) == 631: {e}')
    
    total += 1
    try:
        result = candidate(k = 250) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 250) == 30: {e}')
    
    total += 1
    try:
        result = candidate(k = 87500) == 590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 87500) == 590: {e}')
    
    total += 1
    try:
        result = candidate(k = 37) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 37) == 11: {e}')
    
    total += 1
    try:
        result = candidate(k = 255) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 255) == 30: {e}')
    
    total += 1
    try:
        result = candidate(k = 256) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 256) == 30: {e}')
    
    total += 1
    try:
        result = candidate(k = 512) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 512) == 44: {e}')
    
    total += 1
    try:
        result = candidate(k = 85) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 85) == 17: {e}')
    
    total += 1
    try:
        result = candidate(k = 32768) == 361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 32768) == 361: {e}')
    
    total += 1
    try:
        result = candidate(k = 62500) == 498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 62500) == 498: {e}')
    
    total += 1
    try:
        result = candidate(k = 1023) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1023) == 62: {e}')
    
    total += 1
    try:
        result = candidate(k = 75000) == 546
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75000) == 546: {e}')
    
    total += 1
    try:
        result = candidate(k = 23) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 23) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 4096) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4096) == 126: {e}')
    
    total += 1
    try:
        result = candidate(k = 10000) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10000) == 198: {e}')
    
    total += 1
    try:
        result = candidate(k = 511) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 511) == 44: {e}')
    
    total += 1
    try:
        result = candidate(k = 28) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 28) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000) == 62: {e}')
    
    total += 1
    try:
        result = candidate(k = 19) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 19) == 7: {e}')
    
    total += 1
    try:
        result = candidate(k = 32) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 32) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 128) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 128) == 21: {e}')
    
    total += 1
    try:
        result = candidate(k = 50000) == 446
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50000) == 446: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(k = 100) == 18
    assert candidate(k = 20) == 7
    assert candidate(k = 1) == 0
    assert candidate(k = 15) == 6
    assert candidate(k = 11) == 5
    assert candidate(k = 3) == 2
    assert candidate(k = 100000) == 631
    assert candidate(k = 5) == 3
    assert candidate(k = 10) == 5
    assert candidate(k = 29) == 9
    assert candidate(k = 30) == 9
    assert candidate(k = 101) == 19
    assert candidate(k = 2048) == 89
    assert candidate(k = 1024) == 62
    assert candidate(k = 9999) == 198
    assert candidate(k = 999) == 62
    assert candidate(k = 500) == 43
    assert candidate(k = 49) == 12
    assert candidate(k = 8192) == 180
    assert candidate(k = 50) == 13
    assert candidate(k = 127) == 21
    assert candidate(k = 64) == 14
    assert candidate(k = 17) == 7
    assert candidate(k = 6) == 3
    assert candidate(k = 63) == 14
    assert candidate(k = 7) == 4
    assert candidate(k = 99) == 18
    assert candidate(k = 31) == 10
    assert candidate(k = 13) == 6
    assert candidate(k = 65536) == 510
    assert candidate(k = 16384) == 254
    assert candidate(k = 2) == 1
    assert candidate(k = 12345) == 221
    assert candidate(k = 42) == 11
    assert candidate(k = 67890) == 520
    assert candidate(k = 200) == 27
    assert candidate(k = 99999) == 631
    assert candidate(k = 250) == 30
    assert candidate(k = 87500) == 590
    assert candidate(k = 37) == 11
    assert candidate(k = 255) == 30
    assert candidate(k = 256) == 30
    assert candidate(k = 512) == 44
    assert candidate(k = 85) == 17
    assert candidate(k = 32768) == 361
    assert candidate(k = 62500) == 498
    assert candidate(k = 1023) == 62
    assert candidate(k = 75000) == 546
    assert candidate(k = 23) == 8
    assert candidate(k = 4096) == 126
    assert candidate(k = 10000) == 198
    assert candidate(k = 511) == 44
    assert candidate(k = 28) == 9
    assert candidate(k = 1000) == 62
    assert candidate(k = 19) == 7
    assert candidate(k = 32) == 10
    assert candidate(k = 128) == 21
    assert candidate(k = 50000) == 446


