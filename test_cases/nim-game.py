def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 104) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483646) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483646) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870912) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870912) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 262143) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262143) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435456) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435456) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483643) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483643) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554432) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554432) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 333333333) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333333) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 32768) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32768) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108864) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108864) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 524288) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524288) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435455) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435455) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217728) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217728) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 131072) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131072) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388608) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388608) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 130) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 130) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108863) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108863) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 34) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16384) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16384) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777216) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777216) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 345) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 345) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483644) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483644) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483641) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483641) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 26) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1337) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1337) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097152) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097152) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097151) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097151) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194304) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194304) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483645) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483645) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741824) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741824) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 262144) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262144) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 39) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 39) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483640) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483640) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483642) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483642) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 38) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 38) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == True
    assert candidate(n = 21) == True
    assert candidate(n = 2147483647) == True
    assert candidate(n = 104) == False
    assert candidate(n = 100) == False
    assert candidate(n = 10) == True
    assert candidate(n = 5) == True
    assert candidate(n = 28) == False
    assert candidate(n = 40) == False
    assert candidate(n = 4) == False
    assert candidate(n = 16) == False
    assert candidate(n = 33) == True
    assert candidate(n = 17) == True
    assert candidate(n = 37) == True
    assert candidate(n = 2) == True
    assert candidate(n = 23) == True
    assert candidate(n = 1024) == False
    assert candidate(n = 8) == False
    assert candidate(n = 27) == True
    assert candidate(n = 35) == True
    assert candidate(n = 32) == False
    assert candidate(n = 20) == False
    assert candidate(n = 19) == True
    assert candidate(n = 24) == False
    assert candidate(n = 15) == True
    assert candidate(n = 31) == True
    assert candidate(n = 1) == True
    assert candidate(n = 7) == True
    assert candidate(n = 13) == True
    assert candidate(n = 25) == True
    assert candidate(n = 2147483646) == True
    assert candidate(n = 536870912) == False
    assert candidate(n = 1000) == False
    assert candidate(n = 262143) == True
    assert candidate(n = 268435456) == False
    assert candidate(n = 300) == False
    assert candidate(n = 2147483643) == True
    assert candidate(n = 33554432) == False
    assert candidate(n = 333333333) == True
    assert candidate(n = 2048) == False
    assert candidate(n = 1048576) == False
    assert candidate(n = 999) == True
    assert candidate(n = 8191) == True
    assert candidate(n = 36) == False
    assert candidate(n = 1000000000) == False
    assert candidate(n = 11) == True
    assert candidate(n = 32768) == False
    assert candidate(n = 200) == False
    assert candidate(n = 1048575) == True
    assert candidate(n = 500) == False
    assert candidate(n = 29) == True
    assert candidate(n = 131071) == True
    assert candidate(n = 67108864) == False
    assert candidate(n = 524288) == False
    assert candidate(n = 524287) == True
    assert candidate(n = 268435455) == True
    assert candidate(n = 134217728) == False
    assert candidate(n = 1073741823) == True
    assert candidate(n = 80) == False
    assert candidate(n = 16777215) == True
    assert candidate(n = 256) == False
    assert candidate(n = 131072) == False
    assert candidate(n = 81) == True
    assert candidate(n = 9) == True
    assert candidate(n = 6) == True
    assert candidate(n = 123456789) == True
    assert candidate(n = 8388608) == False
    assert candidate(n = 63) == True
    assert candidate(n = 999999999) == True
    assert candidate(n = 130) == True
    assert candidate(n = 47) == True
    assert candidate(n = 4096) == False
    assert candidate(n = 67108863) == True
    assert candidate(n = 32767) == True
    assert candidate(n = 34) == True
    assert candidate(n = 16384) == False
    assert candidate(n = 123) == True
    assert candidate(n = 16777216) == False
    assert candidate(n = 4194303) == True
    assert candidate(n = 30) == True
    assert candidate(n = 345) == True
    assert candidate(n = 2147483644) == False
    assert candidate(n = 8192) == False
    assert candidate(n = 65536) == False
    assert candidate(n = 18) == True
    assert candidate(n = 1023) == True
    assert candidate(n = 127) == True
    assert candidate(n = 2147483641) == True
    assert candidate(n = 14) == True
    assert candidate(n = 26) == True
    assert candidate(n = 536870911) == True
    assert candidate(n = 1000000) == False
    assert candidate(n = 33554431) == True
    assert candidate(n = 1337) == True
    assert candidate(n = 2097152) == False
    assert candidate(n = 12) == False
    assert candidate(n = 50) == True
    assert candidate(n = 134217727) == True
    assert candidate(n = 99) == True
    assert candidate(n = 8388607) == True
    assert candidate(n = 2097151) == True
    assert candidate(n = 4194304) == False
    assert candidate(n = 64) == False
    assert candidate(n = 2147483645) == True
    assert candidate(n = 128) == False
    assert candidate(n = 1073741824) == False
    assert candidate(n = 22) == True
    assert candidate(n = 262144) == False
    assert candidate(n = 39) == True
    assert candidate(n = 2147483640) == False
    assert candidate(n = 2147483642) == True
    assert candidate(n = 65535) == True
    assert candidate(n = 512) == False
    assert candidate(n = 38) == True


