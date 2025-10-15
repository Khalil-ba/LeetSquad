def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 6,k = 31) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 31) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 11) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 11) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 511) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 511) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 545) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 545) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 65536) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 65536) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 131071) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 131071) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 127) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 127) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 262144) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 262144) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 289) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 289) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 2047) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 2047) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 40) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 40) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 11,k = 148) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,k = 148) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 511) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 511) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 524287) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 524287) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 1023) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 1023) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 11,k = 1024) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,k = 1024) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 85) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 85) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 8191) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 8191) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 16384) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 16384) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 32767) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 32767) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 4095) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 4095) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 1048575) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 1048575) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 255) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 255) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 16) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 16) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 63) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 63) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 1057) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 1057) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 1) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 1) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 127) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 127) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 256) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 256) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 4096) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 4096) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 2081) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 2081) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 2047) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 2047) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 64) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 64) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 262143) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 262143) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 128) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 128) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 32767) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 32767) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1023) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1023) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 4096) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 4096) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 262144) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 262144) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 8192) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 8192) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 4096) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 4096) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 2048) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 2048) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 8191) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 8191) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 11,k = 1023) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,k = 1023) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 131071) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 131071) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 65535) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 65535) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 65536) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 65536) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 4096) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 4096) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 524288) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 524288) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 255) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 255) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 524288) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 524288) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 131072) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 131072) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 11,k = 2048) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,k = 2048) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 16383) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 16383) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 32767) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 32767) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 524287) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 524287) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 4095) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 4095) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 32) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 32) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 512) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 512) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 5) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 5) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 256) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 256) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 65536) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 65536) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 32768) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 32768) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 64) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 64) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 16385) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 16385) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 11,k = 2047) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,k = 2047) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 511) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 511) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 255) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 255) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 128) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 128) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 7) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 7) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 128) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 128) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 327679) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 327679) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 8192) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 8192) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 262143) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 262143) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 32768) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 32768) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 512) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 512) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 16384) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 16384) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 511999) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 511999) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 2) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 2) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 65535) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 65535) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 4095) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 4095) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 64) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 64) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 1) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 1) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 256) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 256) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1024) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1024) == "1": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 6,k = 31) == "1"
    assert candidate(n = 4,k = 11) == "1"
    assert candidate(n = 14,k = 511) == "1"
    assert candidate(n = 15,k = 545) == "0"
    assert candidate(n = 17,k = 65536) == "1"
    assert candidate(n = 18,k = 131071) == "1"
    assert candidate(n = 10,k = 127) == "1"
    assert candidate(n = 19,k = 262144) == "1"
    assert candidate(n = 13,k = 289) == "0"
    assert candidate(n = 12,k = 2047) == "1"
    assert candidate(n = 7,k = 40) == "1"
    assert candidate(n = 11,k = 148) == "1"
    assert candidate(n = 10,k = 511) == "1"
    assert candidate(n = 20,k = 524287) == "1"
    assert candidate(n = 16,k = 1023) == "1"
    assert candidate(n = 11,k = 1024) == "1"
    assert candidate(n = 9,k = 85) == "0"
    assert candidate(n = 14,k = 8191) == "1"
    assert candidate(n = 15,k = 16384) == "1"
    assert candidate(n = 16,k = 32767) == "1"
    assert candidate(n = 20,k = 4095) == "1"
    assert candidate(n = 20,k = 1048575) == "1"
    assert candidate(n = 12,k = 255) == "1"
    assert candidate(n = 5,k = 16) == "1"
    assert candidate(n = 8,k = 63) == "1"
    assert candidate(n = 17,k = 1057) == "0"
    assert candidate(n = 3,k = 1) == "0"
    assert candidate(n = 8,k = 127) == "1"
    assert candidate(n = 9,k = 256) == "1"
    assert candidate(n = 13,k = 4096) == "1"
    assert candidate(n = 19,k = 2081) == "0"
    assert candidate(n = 18,k = 2047) == "1"
    assert candidate(n = 7,k = 64) == "1"
    assert candidate(n = 19,k = 262143) == "1"
    assert candidate(n = 9,k = 128) == "1"
    assert candidate(n = 17,k = 32767) == "1"
    assert candidate(n = 10,k = 1023) == "1"
    assert candidate(n = 12,k = 4096) == "1"
    assert candidate(n = 18,k = 262144) == "1"
    assert candidate(n = 14,k = 8192) == "1"
    assert candidate(n = 14,k = 4096) == "1"
    assert candidate(n = 13,k = 2048) == "1"
    assert candidate(n = 13,k = 8191) == "1"
    assert candidate(n = 11,k = 1023) == "1"
    assert candidate(n = 17,k = 131071) == "1"
    assert candidate(n = 16,k = 65535) == "1"
    assert candidate(n = 18,k = 65536) == "1"
    assert candidate(n = 19,k = 4096) == "1"
    assert candidate(n = 19,k = 524288) == "1"
    assert candidate(n = 9,k = 255) == "1"
    assert candidate(n = 20,k = 524288) == "1"
    assert candidate(n = 17,k = 131072) == "1"
    assert candidate(n = 11,k = 2048) == "1"
    assert candidate(n = 14,k = 16383) == "1"
    assert candidate(n = 15,k = 32767) == "1"
    assert candidate(n = 19,k = 524287) == "1"
    assert candidate(n = 19,k = 4095) == "1"
    assert candidate(n = 5,k = 32) == "1"
    assert candidate(n = 10,k = 512) == "1"
    assert candidate(n = 3,k = 5) == "0"
    assert candidate(n = 8,k = 256) == "1"
    assert candidate(n = 16,k = 65536) == "1"
    assert candidate(n = 15,k = 32768) == "1"
    assert candidate(n = 6,k = 64) == "1"
    assert candidate(n = 17,k = 16385) == "0"
    assert candidate(n = 11,k = 2047) == "1"
    assert candidate(n = 9,k = 511) == "1"
    assert candidate(n = 8,k = 255) == "1"
    assert candidate(n = 7,k = 128) == "1"
    assert candidate(n = 3,k = 7) == "1"
    assert candidate(n = 8,k = 128) == "1"
    assert candidate(n = 19,k = 327679) == "1"
    assert candidate(n = 13,k = 8192) == "1"
    assert candidate(n = 18,k = 262143) == "1"
    assert candidate(n = 16,k = 32768) == "1"
    assert candidate(n = 9,k = 512) == "1"
    assert candidate(n = 14,k = 16384) == "1"
    assert candidate(n = 19,k = 511999) == "1"
    assert candidate(n = 2,k = 2) == "1"
    assert candidate(n = 17,k = 65535) == "1"
    assert candidate(n = 13,k = 4095) == "1"
    assert candidate(n = 8,k = 64) == "1"
    assert candidate(n = 20,k = 1) == "0"
    assert candidate(n = 10,k = 256) == "1"
    assert candidate(n = 10,k = 1024) == "1"


