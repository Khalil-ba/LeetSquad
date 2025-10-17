def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097152) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097152) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -16) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -16) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108864) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108864) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870912) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870912) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 524288) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524288) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435456) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435456) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16384) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16384) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777216) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777216) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -1) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217728) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217728) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194304) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194304) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554432) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554432) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741824) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741824) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483648) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483648) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 262144) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262144) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 131072) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131072) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 32768) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32768) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388608) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388608) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 262143) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262143) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2047) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2047) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -2147483648) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -2147483648) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9223372036854775808) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9223372036854775808) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -4) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967296) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967296) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -128) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -128) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -2) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435455) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435455) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483649) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483649) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -8) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108863) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108863) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 511) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 511) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1152921504606846976) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1152921504606846976) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 255) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4611686018427387904) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4611686018427387904) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 26) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18446744073709551616) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18446744073709551616) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16383) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16383) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2305843009213693952) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2305843009213693952) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097151) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097151) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18014398509481984) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18014398509481984) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4095) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4095) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18014398509481983) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18014398509481983) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -32) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -32) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -64) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -64) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == False
    assert candidate(n = 2097152) == True
    assert candidate(n = -16) == False
    assert candidate(n = 67108864) == True
    assert candidate(n = 4096) == True
    assert candidate(n = 2147483647) == False
    assert candidate(n = 536870912) == True
    assert candidate(n = 524288) == True
    assert candidate(n = 268435456) == True
    assert candidate(n = 16384) == True
    assert candidate(n = 16777216) == True
    assert candidate(n = -1) == False
    assert candidate(n = 4) == True
    assert candidate(n = 64) == True
    assert candidate(n = 16) == True
    assert candidate(n = 134217728) == True
    assert candidate(n = 4194304) == True
    assert candidate(n = 2) == True
    assert candidate(n = 33554432) == True
    assert candidate(n = 1024) == True
    assert candidate(n = 128) == True
    assert candidate(n = 0) == False
    assert candidate(n = 1073741824) == True
    assert candidate(n = 8) == True
    assert candidate(n = 1048576) == True
    assert candidate(n = 8192) == True
    assert candidate(n = 2048) == True
    assert candidate(n = 2147483648) == True
    assert candidate(n = 65536) == True
    assert candidate(n = 256) == True
    assert candidate(n = 32) == True
    assert candidate(n = 262144) == True
    assert candidate(n = 131072) == True
    assert candidate(n = 32768) == True
    assert candidate(n = 512) == True
    assert candidate(n = 1) == True
    assert candidate(n = 8388608) == True
    assert candidate(n = 262143) == False
    assert candidate(n = 2047) == False
    assert candidate(n = 5) == False
    assert candidate(n = 23) == False
    assert candidate(n = -2147483648) == False
    assert candidate(n = 9223372036854775808) == True
    assert candidate(n = 8191) == False
    assert candidate(n = 27) == False
    assert candidate(n = 1000000000) == False
    assert candidate(n = 24) == False
    assert candidate(n = -4) == False
    assert candidate(n = 11) == False
    assert candidate(n = 4294967296) == True
    assert candidate(n = 1048575) == False
    assert candidate(n = 29) == False
    assert candidate(n = 131071) == False
    assert candidate(n = -128) == False
    assert candidate(n = 21) == False
    assert candidate(n = -2) == False
    assert candidate(n = 524287) == False
    assert candidate(n = 268435455) == False
    assert candidate(n = 28) == False
    assert candidate(n = 2147483649) == False
    assert candidate(n = 17) == False
    assert candidate(n = 1073741823) == False
    assert candidate(n = 16777215) == False
    assert candidate(n = 9) == False
    assert candidate(n = -8) == False
    assert candidate(n = 6) == False
    assert candidate(n = 10) == False
    assert candidate(n = 63) == False
    assert candidate(n = 67108863) == False
    assert candidate(n = 32767) == False
    assert candidate(n = 511) == False
    assert candidate(n = 4194303) == False
    assert candidate(n = 30) == False
    assert candidate(n = 1152921504606846976) == True
    assert candidate(n = 255) == False
    assert candidate(n = 18) == False
    assert candidate(n = 4611686018427387904) == True
    assert candidate(n = 1023) == False
    assert candidate(n = 127) == False
    assert candidate(n = 15) == False
    assert candidate(n = 14) == False
    assert candidate(n = 26) == False
    assert candidate(n = 536870911) == False
    assert candidate(n = 1000000) == False
    assert candidate(n = 33554431) == False
    assert candidate(n = 18446744073709551616) == True
    assert candidate(n = 12) == False
    assert candidate(n = 16383) == False
    assert candidate(n = 2305843009213693952) == True
    assert candidate(n = 134217727) == False
    assert candidate(n = 8388607) == False
    assert candidate(n = 2097151) == False
    assert candidate(n = 18014398509481984) == True
    assert candidate(n = 4095) == False
    assert candidate(n = 18014398509481983) == False
    assert candidate(n = 22) == False
    assert candidate(n = -32) == False
    assert candidate(n = -64) == False
    assert candidate(n = 19) == False
    assert candidate(n = 65535) == False
    assert candidate(n = 31) == False
    assert candidate(n = 7) == False
    assert candidate(n = 25) == False


