def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8,num2 = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8,num2 = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 29,num2 = 15) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 29,num2 = 15) == 29: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 3,num2 = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 3,num2 = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 7,num2 = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 7,num2 = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = 1) == 536870912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = 1) == 536870912: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 2000000000) == 8191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 2000000000) == 8191: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 987654321,num2 = 1000000000) == 987654144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 987654321,num2 = 1000000000) == 987654144: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8,num2 = 31) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8,num2 = 31) == 31: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2147483647,num2 = 2147483647) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2147483647,num2 = 2147483647) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 134217728,num2 = 671088640) == 134217729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 134217728,num2 = 671088640) == 134217729: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = 511) == 1022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = 511) == 1022: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8388607,num2 = 16777215) == 16777215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8388607,num2 = 16777215) == 16777215: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123456789,num2 = 31) == 122683392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123456789,num2 = 31) == 122683392: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 1023) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 1023) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 32768,num2 = 65535) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 32768,num2 = 65535) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1234567890,num2 = 9876543210) == 1234567903
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1234567890,num2 = 9876543210) == 1234567903: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2147483647,num2 = 1) == 1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2147483647,num2 = 1) == 1073741824: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = 1) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = 1) == 512: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123456789,num2 = 987654321) == 123456791
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123456789,num2 = 987654321) == 123456791: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2147483647,num2 = 1073741823) == 2147483646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2147483647,num2 = 1073741823) == 2147483646: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = 100000000) == 999999488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = 100000000) == 999999488: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123,num2 = 987654321) == 131071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123,num2 = 987654321) == 131071: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 500000000,num2 = 750000000) == 499999744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 500000000,num2 = 750000000) == 499999744: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741823,num2 = 1) == 536870912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741823,num2 = 1) == 536870912: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741824,num2 = 4294967295) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741824,num2 = 4294967295) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 134217728,num2 = 32767) == 134234111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 134217728,num2 = 32767) == 134234111: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 858993459,num2 = 12) == 805306368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 858993459,num2 = 12) == 805306368: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 4294967295,num2 = 2) == 1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 4294967295,num2 = 2) == 1073741824: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123456,num2 = 32) == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123456,num2 = 32) == 65536: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 512,num2 = 256) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 512,num2 = 256) == 512: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 894567321,num2 = 987654321) == 894567423
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 894567321,num2 = 987654321) == 894567423: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 1073741823) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 1073741823) == 1073741823: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 65535,num2 = 8) == 32768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 65535,num2 = 8) == 32768: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 536870911,num2 = 2147483647) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 536870911,num2 = 2147483647) == 1073741823: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 111111111,num2 = 222222222) == 111111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 111111111,num2 = 222222222) == 111111111: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 2147483647) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 2147483647) == 1073741823: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 512,num2 = 255) == 639
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 512,num2 = 255) == 639: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 834567,num2 = 987654) == 834564
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 834567,num2 = 987654) == 834564: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999999999,num2 = 1) == 536870912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999999999,num2 = 1) == 536870912: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 134217728,num2 = 1073741824) == 134217728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 134217728,num2 = 1073741824) == 134217728: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741823,num2 = 536870912) == 536870912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741823,num2 = 536870912) == 536870912: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 54321,num2 = 98765) == 54323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 54321,num2 = 98765) == 54323: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 987654321,num2 = 16) == 536870912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 987654321,num2 = 16) == 536870912: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = 10) == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = 10) == 768: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 987654,num2 = 24) == 786432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 987654,num2 = 24) == 786432: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 777777777,num2 = 333333333) == 777777760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 777777777,num2 = 333333333) == 777777760: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048575,num2 = 1048575) == 1048575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048575,num2 = 1048575) == 1048575: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 987654321,num2 = 123456789) == 987654320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 987654321,num2 = 123456789) == 987654320: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 131071,num2 = 65535) == 131070
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 131071,num2 = 65535) == 131070: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999999999,num2 = 1000000000) == 999999744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999999999,num2 = 1000000000) == 999999744: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741824,num2 = 536870912) == 1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741824,num2 = 536870912) == 1073741824: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 4294967295,num2 = 15) == 2013265920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 4294967295,num2 = 15) == 2013265920: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1073741824,num2 = 2147483647) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1073741824,num2 = 2147483647) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 16777215,num2 = 8388607) == 16777214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 16777215,num2 = 8388607) == 16777214: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8192,num2 = 16384) == 8192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8192,num2 = 16384) == 8192: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023,num2 = 2047) == 2047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023,num2 = 2047) == 2047: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 987654321,num2 = 135792468) == 987496448
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 987654321,num2 = 135792468) == 987496448: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 134217728,num2 = 25) == 134217731
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 134217728,num2 = 25) == 134217731: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = 1000000000) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = 1000000000) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 16,num2 = 3) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 16,num2 = 3) == 17: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2147483646,num2 = 2147483646) == 2147483646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2147483646,num2 = 2147483646) == 2147483646: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2147483647,num2 = 1073741824) == 1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2147483647,num2 = 1073741824) == 1073741824: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1048575,num2 = 524288) == 524288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1048575,num2 = 524288) == 524288: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 134217728,num2 = 67108864) == 134217728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 134217728,num2 = 67108864) == 134217728: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 888888888,num2 = 888888888) == 888888888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 888888888,num2 = 888888888) == 888888888: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000007,num2 = 20) == 805306368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000007,num2 = 20) == 805306368: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000000,num2 = 500000000) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000000,num2 = 500000000) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 4294967295,num2 = 2147483647) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 4294967295,num2 = 2147483647) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8388607,num2 = 2147483647) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8388607,num2 = 2147483647) == 1073741823: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1023456789,num2 = 987654321) == 1023456895
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1023456789,num2 = 987654321) == 1023456895: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 67890,num2 = 13579) == 67891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 67890,num2 = 13579) == 67891: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999999999,num2 = 888888888) == 999999992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999999999,num2 = 888888888) == 999999992: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2147483647,num2 = 4294967294) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2147483647,num2 = 4294967294) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 1048575) == 1048575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 1048575) == 1048575: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123456789,num2 = 123456789) == 123456789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123456789,num2 = 123456789) == 123456789: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8388607,num2 = 4194304) == 4194304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8388607,num2 = 4194304) == 4194304: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8388607,num2 = 1048575) == 8388600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8388607,num2 = 1048575) == 8388600: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 536870911,num2 = 268435456) == 268435456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 536870911,num2 = 268435456) == 268435456: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 135792468,num2 = 246813579) == 135794687
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 135792468,num2 = 246813579) == 135794687: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 65535,num2 = 65535) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 65535,num2 = 65535) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 500000000,num2 = 800000000) == 499999744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 500000000,num2 = 800000000) == 499999744: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 4294967295,num2 = 1073741824) == 1073741824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 4294967295,num2 = 1073741824) == 1073741824: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1024,num2 = 1023) == 1535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1024,num2 = 1023) == 1535: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000000007,num2 = 1000000008) == 1000000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000000007,num2 = 1000000008) == 1000000004: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num1 = 1,num2 = 12) == 3
    assert candidate(num1 = 8,num2 = 3) == 9
    assert candidate(num1 = 29,num2 = 15) == 29
    assert candidate(num1 = 3,num2 = 5) == 3
    assert candidate(num1 = 7,num2 = 10) == 6
    assert candidate(num1 = 1000000000,num2 = 1) == 536870912
    assert candidate(num1 = 1,num2 = 2000000000) == 8191
    assert candidate(num1 = 987654321,num2 = 1000000000) == 987654144
    assert candidate(num1 = 8,num2 = 31) == 31
    assert candidate(num1 = 2147483647,num2 = 2147483647) == 2147483647
    assert candidate(num1 = 134217728,num2 = 671088640) == 134217729
    assert candidate(num1 = 1023,num2 = 511) == 1022
    assert candidate(num1 = 8388607,num2 = 16777215) == 16777215
    assert candidate(num1 = 123456789,num2 = 31) == 122683392
    assert candidate(num1 = 1,num2 = 1023) == 1023
    assert candidate(num1 = 32768,num2 = 65535) == 65535
    assert candidate(num1 = 1234567890,num2 = 9876543210) == 1234567903
    assert candidate(num1 = 2147483647,num2 = 1) == 1073741824
    assert candidate(num1 = 1023,num2 = 1) == 512
    assert candidate(num1 = 123456789,num2 = 987654321) == 123456791
    assert candidate(num1 = 2147483647,num2 = 1073741823) == 2147483646
    assert candidate(num1 = 1000000000,num2 = 100000000) == 999999488
    assert candidate(num1 = 123,num2 = 987654321) == 131071
    assert candidate(num1 = 500000000,num2 = 750000000) == 499999744
    assert candidate(num1 = 1073741823,num2 = 1) == 536870912
    assert candidate(num1 = 1073741824,num2 = 4294967295) == 2147483647
    assert candidate(num1 = 134217728,num2 = 32767) == 134234111
    assert candidate(num1 = 858993459,num2 = 12) == 805306368
    assert candidate(num1 = 4294967295,num2 = 2) == 1073741824
    assert candidate(num1 = 123456,num2 = 32) == 65536
    assert candidate(num1 = 512,num2 = 256) == 512
    assert candidate(num1 = 894567321,num2 = 987654321) == 894567423
    assert candidate(num1 = 1,num2 = 1073741823) == 1073741823
    assert candidate(num1 = 65535,num2 = 8) == 32768
    assert candidate(num1 = 536870911,num2 = 2147483647) == 1073741823
    assert candidate(num1 = 111111111,num2 = 222222222) == 111111111
    assert candidate(num1 = 1,num2 = 2147483647) == 1073741823
    assert candidate(num1 = 512,num2 = 255) == 639
    assert candidate(num1 = 834567,num2 = 987654) == 834564
    assert candidate(num1 = 999999999,num2 = 1) == 536870912
    assert candidate(num1 = 134217728,num2 = 1073741824) == 134217728
    assert candidate(num1 = 1073741823,num2 = 536870912) == 536870912
    assert candidate(num1 = 54321,num2 = 98765) == 54323
    assert candidate(num1 = 987654321,num2 = 16) == 536870912
    assert candidate(num1 = 1023,num2 = 10) == 768
    assert candidate(num1 = 987654,num2 = 24) == 786432
    assert candidate(num1 = 777777777,num2 = 333333333) == 777777760
    assert candidate(num1 = 1048575,num2 = 1048575) == 1048575
    assert candidate(num1 = 987654321,num2 = 123456789) == 987654320
    assert candidate(num1 = 131071,num2 = 65535) == 131070
    assert candidate(num1 = 999999999,num2 = 1000000000) == 999999744
    assert candidate(num1 = 1073741824,num2 = 536870912) == 1073741824
    assert candidate(num1 = 4294967295,num2 = 15) == 2013265920
    assert candidate(num1 = 1073741824,num2 = 2147483647) == 2147483647
    assert candidate(num1 = 16777215,num2 = 8388607) == 16777214
    assert candidate(num1 = 8192,num2 = 16384) == 8192
    assert candidate(num1 = 1023,num2 = 2047) == 2047
    assert candidate(num1 = 987654321,num2 = 135792468) == 987496448
    assert candidate(num1 = 134217728,num2 = 25) == 134217731
    assert candidate(num1 = 1000000000,num2 = 1000000000) == 1000000000
    assert candidate(num1 = 16,num2 = 3) == 17
    assert candidate(num1 = 2147483646,num2 = 2147483646) == 2147483646
    assert candidate(num1 = 2147483647,num2 = 1073741824) == 1073741824
    assert candidate(num1 = 1048575,num2 = 524288) == 524288
    assert candidate(num1 = 134217728,num2 = 67108864) == 134217728
    assert candidate(num1 = 888888888,num2 = 888888888) == 888888888
    assert candidate(num1 = 1000000007,num2 = 20) == 805306368
    assert candidate(num1 = 1000000000,num2 = 500000000) == 1000000000
    assert candidate(num1 = 4294967295,num2 = 2147483647) == 2147483647
    assert candidate(num1 = 8388607,num2 = 2147483647) == 1073741823
    assert candidate(num1 = 1023456789,num2 = 987654321) == 1023456895
    assert candidate(num1 = 67890,num2 = 13579) == 67891
    assert candidate(num1 = 999999999,num2 = 888888888) == 999999992
    assert candidate(num1 = 2147483647,num2 = 4294967294) == 2147483647
    assert candidate(num1 = 1,num2 = 1048575) == 1048575
    assert candidate(num1 = 123456789,num2 = 123456789) == 123456789
    assert candidate(num1 = 8388607,num2 = 4194304) == 4194304
    assert candidate(num1 = 8388607,num2 = 1048575) == 8388600
    assert candidate(num1 = 536870911,num2 = 268435456) == 268435456
    assert candidate(num1 = 135792468,num2 = 246813579) == 135794687
    assert candidate(num1 = 65535,num2 = 65535) == 65535
    assert candidate(num1 = 500000000,num2 = 800000000) == 499999744
    assert candidate(num1 = 4294967295,num2 = 1073741824) == 1073741824
    assert candidate(num1 = 1024,num2 = 1023) == 1535
    assert candidate(num1 = 1000000007,num2 = 1000000008) == 1000000004


