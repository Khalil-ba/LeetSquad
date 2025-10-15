def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(x = 2147483647) == 46340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2147483647) == 46340: {e}')
    
    total += 1
    try:
        result = candidate(x = 26) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 26) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = 101) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 101) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 1025) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1025) == 32: {e}')
    
    total += 1
    try:
        result = candidate(x = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 1234567890123456789) == 1111111106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1234567890123456789) == 1111111106: {e}')
    
    total += 1
    try:
        result = candidate(x = 40000000000) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40000000000) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(x = 18014398509481984) == 134217728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 18014398509481984) == 134217728: {e}')
    
    total += 1
    try:
        result = candidate(x = 16384) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 16384) == 128: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000) == 31: {e}')
    
    total += 1
    try:
        result = candidate(x = 1524157875) == 39040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1524157875) == 39040: {e}')
    
    total += 1
    try:
        result = candidate(x = 2147483646) == 46340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2147483646) == 46340: {e}')
    
    total += 1
    try:
        result = candidate(x = 99) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 99) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 4294967296) == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4294967296) == 65536: {e}')
    
    total += 1
    try:
        result = candidate(x = 225) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 225) == 15: {e}')
    
    total += 1
    try:
        result = candidate(x = 1522756) == 1234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1522756) == 1234: {e}')
    
    total += 1
    try:
        result = candidate(x = 17) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 17) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 2147395600) == 46340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2147395600) == 46340: {e}')
    
    total += 1
    try:
        result = candidate(x = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 18446744073709551615) == 4294967295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 18446744073709551615) == 4294967295: {e}')
    
    total += 1
    try:
        result = candidate(x = 16777215) == 4095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 16777215) == 4095: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(x = 18014398509481983) == 134217727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 18014398509481983) == 134217727: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000000001) == 31622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000000001) == 31622: {e}')
    
    total += 1
    try:
        result = candidate(x = 169) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 169) == 13: {e}')
    
    total += 1
    try:
        result = candidate(x = 150) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 150) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 141421356237) == 376060
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 141421356237) == 376060: {e}')
    
    total += 1
    try:
        result = candidate(x = 10000) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10000) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 4294967295) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4294967295) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(x = 361) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 361) == 19: {e}')
    
    total += 1
    try:
        result = candidate(x = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 987654321) == 31426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 987654321) == 31426: {e}')
    
    total += 1
    try:
        result = candidate(x = 999999999) == 31622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 999999999) == 31622: {e}')
    
    total += 1
    try:
        result = candidate(x = 499999999) == 22360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 499999999) == 22360: {e}')
    
    total += 1
    try:
        result = candidate(x = 2048) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2048) == 45: {e}')
    
    total += 1
    try:
        result = candidate(x = 1024) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1024) == 32: {e}')
    
    total += 1
    try:
        result = candidate(x = 1048575) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1048575) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(x = 16777216) == 4096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 16777216) == 4096: {e}')
    
    total += 1
    try:
        result = candidate(x = 256) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 256) == 16: {e}')
    
    total += 1
    try:
        result = candidate(x = 131072) == 362
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 131072) == 362: {e}')
    
    total += 1
    try:
        result = candidate(x = 2097152) == 1448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2097152) == 1448: {e}')
    
    total += 1
    try:
        result = candidate(x = 441) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 441) == 21: {e}')
    
    total += 1
    try:
        result = candidate(x = 1048576) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1048576) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(x = 65536) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 65536) == 256: {e}')
    
    total += 1
    try:
        result = candidate(x = 10000000) == 3162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10000000) == 3162: {e}')
    
    total += 1
    try:
        result = candidate(x = 49) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 49) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 144) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 144) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 121) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 121) == 11: {e}')
    
    total += 1
    try:
        result = candidate(x = 1234567890123456788) == 1111111106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1234567890123456788) == 1111111106: {e}')
    
    total += 1
    try:
        result = candidate(x = 4096) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4096) == 64: {e}')
    
    total += 1
    try:
        result = candidate(x = 196) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 196) == 14: {e}')
    
    total += 1
    try:
        result = candidate(x = 9223372036854775807) == 3037000499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9223372036854775807) == 3037000499: {e}')
    
    total += 1
    try:
        result = candidate(x = 123456789) == 11111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 123456789) == 11111: {e}')
    
    total += 1
    try:
        result = candidate(x = 289) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 289) == 17: {e}')
    
    total += 1
    try:
        result = candidate(x = 324) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 324) == 18: {e}')
    
    total += 1
    try:
        result = candidate(x = 24) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 24) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 16) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 16) == 4: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000000000) == 31622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000000000) == 31622: {e}')
    
    total += 1
    try:
        result = candidate(x = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 36028797018963968) == 189812531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 36028797018963968) == 189812531: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(x = 2147483647) == 46340
    assert candidate(x = 26) == 5
    assert candidate(x = 4) == 2
    assert candidate(x = 1) == 1
    assert candidate(x = 25) == 5
    assert candidate(x = 0) == 0
    assert candidate(x = 101) == 10
    assert candidate(x = 100) == 10
    assert candidate(x = 8) == 2
    assert candidate(x = 1025) == 32
    assert candidate(x = 10) == 3
    assert candidate(x = 1234567890123456789) == 1111111106
    assert candidate(x = 40000000000) == 200000
    assert candidate(x = 18014398509481984) == 134217728
    assert candidate(x = 16384) == 128
    assert candidate(x = 1000) == 31
    assert candidate(x = 1524157875) == 39040
    assert candidate(x = 2147483646) == 46340
    assert candidate(x = 99) == 9
    assert candidate(x = 4294967296) == 65536
    assert candidate(x = 225) == 15
    assert candidate(x = 1522756) == 1234
    assert candidate(x = 17) == 4
    assert candidate(x = 2147395600) == 46340
    assert candidate(x = 15) == 3
    assert candidate(x = 18446744073709551615) == 4294967295
    assert candidate(x = 16777215) == 4095
    assert candidate(x = 1000000) == 1000
    assert candidate(x = 18014398509481983) == 134217727
    assert candidate(x = 1000000001) == 31622
    assert candidate(x = 169) == 13
    assert candidate(x = 150) == 12
    assert candidate(x = 2) == 1
    assert candidate(x = 141421356237) == 376060
    assert candidate(x = 10000) == 100
    assert candidate(x = 4294967295) == 65535
    assert candidate(x = 361) == 19
    assert candidate(x = 30) == 5
    assert candidate(x = 987654321) == 31426
    assert candidate(x = 999999999) == 31622
    assert candidate(x = 499999999) == 22360
    assert candidate(x = 2048) == 45
    assert candidate(x = 1024) == 32
    assert candidate(x = 1048575) == 1023
    assert candidate(x = 16777216) == 4096
    assert candidate(x = 256) == 16
    assert candidate(x = 131072) == 362
    assert candidate(x = 2097152) == 1448
    assert candidate(x = 441) == 21
    assert candidate(x = 1048576) == 1024
    assert candidate(x = 65536) == 256
    assert candidate(x = 10000000) == 3162
    assert candidate(x = 49) == 7
    assert candidate(x = 144) == 12
    assert candidate(x = 121) == 11
    assert candidate(x = 1234567890123456788) == 1111111106
    assert candidate(x = 4096) == 64
    assert candidate(x = 196) == 14
    assert candidate(x = 9223372036854775807) == 3037000499
    assert candidate(x = 123456789) == 11111
    assert candidate(x = 289) == 17
    assert candidate(x = 324) == 18
    assert candidate(x = 24) == 4
    assert candidate(x = 16) == 4
    assert candidate(x = 1000000000) == 31622
    assert candidate(x = 3) == 1
    assert candidate(x = 36028797018963968) == 189812531


