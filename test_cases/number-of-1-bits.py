def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4095) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4095) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483645) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483645) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1099511627776) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1099511627776) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483646) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483646) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 239) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 239) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 53) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 53) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 262143) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262143) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 43) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435456) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435456) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2047) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2047) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 549755813888) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 549755813888) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 103) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 103) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 223) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 223) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 211) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 211) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 73) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1022) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1022) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554432) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554432) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 251) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 251) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 181) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 181) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 193) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 193) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 131) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 241) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 241) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 263) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 263) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 32768) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32768) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 313) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 313) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 167) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 167) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 317) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 317) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 107374182) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 107374182) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 271) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 271) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8589934591) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8589934591) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 107) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 107) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 163) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 163) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 524288) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524288) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435455) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435455) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 137) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 137) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217728) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217728) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 257) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 257) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 1610612735) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1610612735) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 68719476735) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 68719476735) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 2199023255551) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2199023255551) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1099511627775) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1099511627775) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 71) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 71) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 151) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 151) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 293) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 293) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 41) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 41) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 83) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 83) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 283) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 283) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388608) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388608) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 79) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 79) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 269) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 269) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 61) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 61) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 227) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 227) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 113) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 113) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 233) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 233) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 511) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 511) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967295) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967295) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 1879048192) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1879048192) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 191) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 191) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4026531840) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4026531840) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 17179869183) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17179869183) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 311) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 311) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 179) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 179) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3221225471) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3221225471) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483644) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483644) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 34359738367) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34359738367) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 255) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 307) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 307) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 26) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 281) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 281) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 277) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 277) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 197) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 197) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 157) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 157) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 16383) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16383) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 59) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 173) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 173) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 67) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 254) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 254) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 4094) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4094) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741824) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741824) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 149) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 149) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1599999999) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1599999999) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 139) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 139) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 109) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 109) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 229) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 229) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 199) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 4095) == 12
    assert candidate(n = 11) == 3
    assert candidate(n = 15) == 4
    assert candidate(n = 2147483647) == 31
    assert candidate(n = 32) == 1
    assert candidate(n = 1023) == 10
    assert candidate(n = 2147483645) == 30
    assert candidate(n = 1) == 1
    assert candidate(n = 65535) == 16
    assert candidate(n = 128) == 1
    assert candidate(n = 3) == 2
    assert candidate(n = 1099511627776) == 1
    assert candidate(n = 2147483646) == 30
    assert candidate(n = 239) == 7
    assert candidate(n = 53) == 4
    assert candidate(n = 262143) == 18
    assert candidate(n = 43) == 4
    assert candidate(n = 268435456) == 1
    assert candidate(n = 2047) == 11
    assert candidate(n = 5) == 2
    assert candidate(n = 549755813888) == 1
    assert candidate(n = 103) == 5
    assert candidate(n = 37) == 3
    assert candidate(n = 223) == 7
    assert candidate(n = 211) == 5
    assert candidate(n = 73) == 3
    assert candidate(n = 1022) == 9
    assert candidate(n = 33554432) == 1
    assert candidate(n = 251) == 7
    assert candidate(n = 181) == 5
    assert candidate(n = 8) == 1
    assert candidate(n = 193) == 3
    assert candidate(n = 131) == 3
    assert candidate(n = 2048) == 1
    assert candidate(n = 241) == 5
    assert candidate(n = 263) == 4
    assert candidate(n = 8191) == 13
    assert candidate(n = 1000000000) == 13
    assert candidate(n = 32768) == 1
    assert candidate(n = 1048575) == 20
    assert candidate(n = 500000000) == 13
    assert candidate(n = 313) == 5
    assert candidate(n = 167) == 5
    assert candidate(n = 97) == 3
    assert candidate(n = 317) == 6
    assert candidate(n = 107374182) == 14
    assert candidate(n = 271) == 5
    assert candidate(n = 8589934591) == 33
    assert candidate(n = 21) == 3
    assert candidate(n = 107) == 5
    assert candidate(n = 163) == 4
    assert candidate(n = 524288) == 1
    assert candidate(n = 524287) == 19
    assert candidate(n = 28) == 3
    assert candidate(n = 268435455) == 28
    assert candidate(n = 137) == 3
    assert candidate(n = 4) == 1
    assert candidate(n = 134217728) == 1
    assert candidate(n = 257) == 2
    assert candidate(n = 1073741823) == 30
    assert candidate(n = 1610612735) == 30
    assert candidate(n = 16777215) == 24
    assert candidate(n = 101) == 4
    assert candidate(n = 68719476735) == 36
    assert candidate(n = 2199023255551) == 41
    assert candidate(n = 89) == 4
    assert candidate(n = 256) == 1
    assert candidate(n = 1099511627775) == 40
    assert candidate(n = 71) == 4
    assert candidate(n = 151) == 5
    assert candidate(n = 293) == 4
    assert candidate(n = 41) == 3
    assert candidate(n = 9) == 2
    assert candidate(n = 83) == 4
    assert candidate(n = 123456789) == 16
    assert candidate(n = 283) == 5
    assert candidate(n = 8388608) == 1
    assert candidate(n = 79) == 5
    assert candidate(n = 63) == 6
    assert candidate(n = 269) == 4
    assert candidate(n = 61) == 5
    assert candidate(n = 999999999) == 21
    assert candidate(n = 49) == 3
    assert candidate(n = 227) == 5
    assert candidate(n = 47) == 5
    assert candidate(n = 4096) == 1
    assert candidate(n = 113) == 4
    assert candidate(n = 233) == 5
    assert candidate(n = 32767) == 15
    assert candidate(n = 511) == 9
    assert candidate(n = 4294967295) == 32
    assert candidate(n = 1879048192) == 3
    assert candidate(n = 4194303) == 22
    assert candidate(n = 191) == 7
    assert candidate(n = 16) == 1
    assert candidate(n = 4026531840) == 4
    assert candidate(n = 17179869183) == 34
    assert candidate(n = 311) == 6
    assert candidate(n = 179) == 5
    assert candidate(n = 2) == 1
    assert candidate(n = 3221225471) == 31
    assert candidate(n = 2147483644) == 29
    assert candidate(n = 34359738367) == 35
    assert candidate(n = 255) == 8
    assert candidate(n = 127) == 7
    assert candidate(n = 987654321) == 17
    assert candidate(n = 307) == 5
    assert candidate(n = 14) == 3
    assert candidate(n = 26) == 3
    assert candidate(n = 281) == 4
    assert candidate(n = 536870911) == 29
    assert candidate(n = 33554431) == 25
    assert candidate(n = 13) == 3
    assert candidate(n = 277) == 4
    assert candidate(n = 197) == 4
    assert candidate(n = 157) == 5
    assert candidate(n = 16383) == 14
    assert candidate(n = 59) == 5
    assert candidate(n = 173) == 5
    assert candidate(n = 67) == 3
    assert candidate(n = 134217727) == 27
    assert candidate(n = 64) == 1
    assert candidate(n = 8388607) == 23
    assert candidate(n = 254) == 7
    assert candidate(n = 4094) == 11
    assert candidate(n = 1024) == 1
    assert candidate(n = 1073741824) == 1
    assert candidate(n = 22) == 3
    assert candidate(n = 149) == 4
    assert candidate(n = 19) == 3
    assert candidate(n = 1599999999) == 23
    assert candidate(n = 139) == 4
    assert candidate(n = 109) == 5
    assert candidate(n = 31) == 5
    assert candidate(n = 229) == 5
    assert candidate(n = 199) == 5
    assert candidate(n = 7) == 3
    assert candidate(n = 25) == 3


