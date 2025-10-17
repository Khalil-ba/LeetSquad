def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 26) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 26) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 21) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 21) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 536870912) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 536870912) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 536870911) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 536870911) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 23) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 23) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 22) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 22) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 29) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 29) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 17) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 17) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 27) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 27) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 31) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 31) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 16) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 16) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 1073741823) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 1073741823) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 18) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 18) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 28) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 28) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 24) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 24) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 63) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 63) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 128) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 128) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 262144) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 262144) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1023) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1023) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 131071) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 131071) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 126) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 126) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 262144) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 262144) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 2047) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 2047) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 1048575) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 1048575) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 8192) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 8192) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 45) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 45) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 511) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 511) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 4194304) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 4194304) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 524287) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 524287) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 65536) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 65536) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 350) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 350) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 29,k = 536870911) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29,k = 536870911) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 255) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 255) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 524288) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 524288) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 16383) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 16383) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 16382) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 16382) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 16384) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 16384) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 32767) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 32767) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 33554432) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 33554432) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 512) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 512) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 2097151) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 2097151) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 1048575) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 1048575) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 262145) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 262145) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 129) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 129) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 67108863) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 67108863) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 65536) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 65536) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 2048) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 2048) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 23,k = 8388607) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23,k = 8388607) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 131072) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 131072) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 33554431) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 33554431) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 255) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 255) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 128) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 128) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 1073741824) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 1073741824) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 16777215) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 16777215) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 24,k = 8388608) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24,k = 8388608) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 4096) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 4096) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 127) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 127) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 256) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 256) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 268435455) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 268435455) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 262144) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 262144) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 8192) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 8192) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 33) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 33) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 256) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 256) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 64) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 64) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,k = 8) == 1
    assert candidate(n = 5,k = 26) == 0
    assert candidate(n = 5,k = 21) == 0
    assert candidate(n = 5,k = 19) == 0
    assert candidate(n = 30,k = 536870912) == 1
    assert candidate(n = 3,k = 2) == 1
    assert candidate(n = 1,k = 1) == 0
    assert candidate(n = 30,k = 536870911) == 0
    assert candidate(n = 4,k = 5) == 1
    assert candidate(n = 5,k = 23) == 0
    assert candidate(n = 5,k = 20) == 0
    assert candidate(n = 5,k = 25) == 0
    assert candidate(n = 4,k = 1) == 0
    assert candidate(n = 5,k = 22) == 0
    assert candidate(n = 5,k = 29) == 0
    assert candidate(n = 5,k = 10) == 0
    assert candidate(n = 2,k = 1) == 0
    assert candidate(n = 3,k = 3) == 1
    assert candidate(n = 3,k = 4) == 0
    assert candidate(n = 5,k = 15) == 1
    assert candidate(n = 5,k = 17) == 0
    assert candidate(n = 5,k = 27) == 0
    assert candidate(n = 5,k = 30) == 0
    assert candidate(n = 4,k = 2) == 1
    assert candidate(n = 5,k = 31) == 0
    assert candidate(n = 5,k = 16) == 0
    assert candidate(n = 30,k = 1073741823) == 1
    assert candidate(n = 4,k = 3) == 1
    assert candidate(n = 5,k = 18) == 0
    assert candidate(n = 3,k = 1) == 0
    assert candidate(n = 5,k = 28) == 0
    assert candidate(n = 5,k = 24) == 0
    assert candidate(n = 4,k = 6) == 0
    assert candidate(n = 2,k = 2) == 1
    assert candidate(n = 4,k = 7) == 0
    assert candidate(n = 4,k = 4) == 0
    assert candidate(n = 7,k = 63) == 1
    assert candidate(n = 9,k = 128) == 1
    assert candidate(n = 19,k = 262144) == 0
    assert candidate(n = 10,k = 1023) == 1
    assert candidate(n = 18,k = 131071) == 0
    assert candidate(n = 7,k = 126) == 0
    assert candidate(n = 18,k = 262144) == 1
    assert candidate(n = 12,k = 2047) == 0
    assert candidate(n = 25,k = 1048575) == 1
    assert candidate(n = 14,k = 8192) == 1
    assert candidate(n = 6,k = 45) == 1
    assert candidate(n = 10,k = 511) == 0
    assert candidate(n = 22,k = 4194304) == 1
    assert candidate(n = 20,k = 524287) == 0
    assert candidate(n = 18,k = 65536) == 0
    assert candidate(n = 10,k = 350) == 0
    assert candidate(n = 29,k = 536870911) == 0
    assert candidate(n = 9,k = 255) == 1
    assert candidate(n = 20,k = 524288) == 1
    assert candidate(n = 15,k = 16383) == 1
    assert candidate(n = 15,k = 16382) == 1
    assert candidate(n = 15,k = 16384) == 0
    assert candidate(n = 15,k = 32767) == 0
    assert candidate(n = 7,k = 100) == 0
    assert candidate(n = 25,k = 33554432) == 0
    assert candidate(n = 10,k = 512) == 1
    assert candidate(n = 22,k = 2097151) == 0
    assert candidate(n = 20,k = 1048575) == 1
    assert candidate(n = 18,k = 262145) == 1
    assert candidate(n = 8,k = 129) == 1
    assert candidate(n = 25,k = 67108863) == 0
    assert candidate(n = 16,k = 65536) == 1
    assert candidate(n = 12,k = 2048) == 1
    assert candidate(n = 23,k = 8388607) == 0
    assert candidate(n = 18,k = 131072) == 1
    assert candidate(n = 25,k = 33554431) == 0
    assert candidate(n = 8,k = 255) == 1
    assert candidate(n = 8,k = 128) == 1
    assert candidate(n = 30,k = 1073741824) == 1
    assert candidate(n = 25,k = 16777215) == 1
    assert candidate(n = 24,k = 8388608) == 1
    assert candidate(n = 13,k = 4096) == 0
    assert candidate(n = 8,k = 127) == 0
    assert candidate(n = 9,k = 256) == 0
    assert candidate(n = 28,k = 268435455) == 1
    assert candidate(n = 20,k = 262144) == 0
    assert candidate(n = 15,k = 8192) == 1
    assert candidate(n = 6,k = 33) == 1
    assert candidate(n = 10,k = 256) == 0
    assert candidate(n = 7,k = 64) == 0


