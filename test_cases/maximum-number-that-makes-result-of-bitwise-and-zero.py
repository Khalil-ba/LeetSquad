def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 137438953471) == 68719476735
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 137438953471) == 68719476735: {e}')
    
    total += 1
    try:
        result = candidate(n = 1099511627776) == 1099511627775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1099511627776) == 1099511627775: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 1073741823: {e}')
    
    total += 1
    try:
        result = candidate(n = 262143) == 131071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262143) == 131071: {e}')
    
    total += 1
    try:
        result = candidate(n = 2047) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2047) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000000) == 549755813887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000000) == 549755813887: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == 2047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == 2047: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == 4095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == 4095: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000001) == 549755813887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000001) == 549755813887: {e}')
    
    total += 1
    try:
        result = candidate(n = 32768) == 32767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32768) == 32767: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == 524287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == 524287: {e}')
    
    total += 1
    try:
        result = candidate(n = 70368744177663) == 35184372088831
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70368744177663) == 35184372088831: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 140737488355327) == 70368744177663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 140737488355327) == 70368744177663: {e}')
    
    total += 1
    try:
        result = candidate(n = 562949953421311) == 281474976710655
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 562949953421311) == 281474976710655: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(n = 8589934591) == 4294967295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8589934591) == 4294967295: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000000000) == 562949953421311
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000000000) == 562949953421311: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287) == 262143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287) == 262143: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435455) == 134217727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435455) == 134217727: {e}')
    
    total += 1
    try:
        result = candidate(n = 576460752303423487) == 288230376151711743
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 576460752303423487) == 288230376151711743: {e}')
    
    total += 1
    try:
        result = candidate(n = 4611686018427387903) == 2305843009213693951
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4611686018427387903) == 2305843009213693951: {e}')
    
    total += 1
    try:
        result = candidate(n = 549755813887) == 274877906943
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 549755813887) == 274877906943: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == 536870911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == 536870911: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == 8388607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == 8388607: {e}')
    
    total += 1
    try:
        result = candidate(n = 281474976710655) == 140737488355327
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 281474976710655) == 140737488355327: {e}')
    
    total += 1
    try:
        result = candidate(n = 68719476735) == 34359738367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 68719476735) == 34359738367: {e}')
    
    total += 1
    try:
        result = candidate(n = 2199023255551) == 1099511627775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2199023255551) == 1099511627775: {e}')
    
    total += 1
    try:
        result = candidate(n = 8796093022207) == 4398046511103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8796093022207) == 4398046511103: {e}')
    
    total += 1
    try:
        result = candidate(n = 1099511627775) == 549755813887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1099511627775) == 549755813887: {e}')
    
    total += 1
    try:
        result = candidate(n = 131072) == 131071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131072) == 131071: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 1125899906842623) == 562949953421311
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1125899906842623) == 562949953421311: {e}')
    
    total += 1
    try:
        result = candidate(n = 17592186044415) == 8796093022207
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17592186044415) == 8796093022207: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108863) == 33554431
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108863) == 33554431: {e}')
    
    total += 1
    try:
        result = candidate(n = 35184372088831) == 17592186044415
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35184372088831) == 17592186044415: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == 16383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == 16383: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967295) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967295) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(n = 16384) == 16383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16384) == 16383: {e}')
    
    total += 1
    try:
        result = candidate(n = 2251799813685247) == 1125899906842623
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2251799813685247) == 1125899906842623: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303) == 2097151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303) == 2097151: {e}')
    
    total += 1
    try:
        result = candidate(n = 144115188075855871) == 72057594037927935
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 144115188075855871) == 72057594037927935: {e}')
    
    total += 1
    try:
        result = candidate(n = 17179869183) == 8589934591
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17179869183) == 8589934591: {e}')
    
    total += 1
    try:
        result = candidate(n = 9223372036854775807) == 4611686018427387903
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9223372036854775807) == 4611686018427387903: {e}')
    
    total += 1
    try:
        result = candidate(n = 255) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255) == 127: {e}')
    
    total += 1
    try:
        result = candidate(n = 34359738367) == 17179869183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34359738367) == 17179869183: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == 8191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == 8191: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == 511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == 511: {e}')
    
    total += 1
    try:
        result = candidate(n = 274877906943) == 137438953471
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 274877906943) == 137438953471: {e}')
    
    total += 1
    try:
        result = candidate(n = 9007199254740991) == 4503599627370495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9007199254740991) == 4503599627370495: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == 63: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911) == 268435455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911) == 268435455: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431) == 16777215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431) == 16777215: {e}')
    
    total += 1
    try:
        result = candidate(n = 72057594037927935) == 36028797018963967
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72057594037927935) == 36028797018963967: {e}')
    
    total += 1
    try:
        result = candidate(n = 16383) == 8191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16383) == 8191: {e}')
    
    total += 1
    try:
        result = candidate(n = 288230376151711743) == 144115188075855871
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 288230376151711743) == 144115188075855871: {e}')
    
    total += 1
    try:
        result = candidate(n = 4503599627370495) == 2251799813685247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4503599627370495) == 2251799813685247: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727) == 67108863
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727) == 67108863: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 63: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607) == 4194303
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607) == 4194303: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097151) == 1048575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097151) == 1048575: {e}')
    
    total += 1
    try:
        result = candidate(n = 4398046511103) == 2199023255551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4398046511103) == 2199023255551: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == 127: {e}')
    
    total += 1
    try:
        result = candidate(n = 4095) == 2047
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4095) == 2047: {e}')
    
    total += 1
    try:
        result = candidate(n = 18014398509481983) == 9007199254740991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18014398509481983) == 9007199254740991: {e}')
    
    total += 1
    try:
        result = candidate(n = 2305843009213693951) == 1152921504606846975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2305843009213693951) == 1152921504606846975: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == 32767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == 32767: {e}')
    
    total += 1
    try:
        result = candidate(n = 1152921504606846975) == 576460752303423487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1152921504606846975) == 576460752303423487: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 36028797018963967) == 18014398509481983
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36028797018963967) == 18014398509481983: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123456789) == 1152921504606846975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123456789) == 1152921504606846975: {e}')
    
    total += 1
    try:
        result = candidate(n = 18446744073709551615) == 9223372036854775807
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18446744073709551615) == 9223372036854775807: {e}')
    
    total += 1
    try:
        result = candidate(n = 511) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 511) == 255: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000000000001) == 576460752303423487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000000000001) == 576460752303423487: {e}')
    
    total += 1
    try:
        result = candidate(n = 2123366401) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2123366401) == 1073741823: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000000000) == 281474976710655
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000000000) == 281474976710655: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789123456) == 70368744177663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789123456) == 70368744177663: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 536870911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 536870911: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789012345) == 70368744177663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789012345) == 70368744177663: {e}')
    
    total += 1
    try:
        result = candidate(n = 1047552) == 524287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1047552) == 524287: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321987654) == 562949953421311
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321987654) == 562949953421311: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 137438953471) == 68719476735
    assert candidate(n = 1099511627776) == 1099511627775
    assert candidate(n = 2147483647) == 1073741823
    assert candidate(n = 262143) == 131071
    assert candidate(n = 2047) == 1023
    assert candidate(n = 1000000000000) == 549755813887
    assert candidate(n = 2048) == 2047
    assert candidate(n = 8191) == 4095
    assert candidate(n = 1000000000001) == 549755813887
    assert candidate(n = 32768) == 32767
    assert candidate(n = 1048575) == 524287
    assert candidate(n = 70368744177663) == 35184372088831
    assert candidate(n = 1) == 0
    assert candidate(n = 140737488355327) == 70368744177663
    assert candidate(n = 562949953421311) == 281474976710655
    assert candidate(n = 131071) == 65535
    assert candidate(n = 8589934591) == 4294967295
    assert candidate(n = 1000000000000000) == 562949953421311
    assert candidate(n = 524287) == 262143
    assert candidate(n = 268435455) == 134217727
    assert candidate(n = 576460752303423487) == 288230376151711743
    assert candidate(n = 4611686018427387903) == 2305843009213693951
    assert candidate(n = 549755813887) == 274877906943
    assert candidate(n = 17) == 15
    assert candidate(n = 1073741823) == 536870911
    assert candidate(n = 16777215) == 8388607
    assert candidate(n = 281474976710655) == 140737488355327
    assert candidate(n = 68719476735) == 34359738367
    assert candidate(n = 2199023255551) == 1099511627775
    assert candidate(n = 8796093022207) == 4398046511103
    assert candidate(n = 1099511627775) == 549755813887
    assert candidate(n = 131072) == 131071
    assert candidate(n = 9) == 7
    assert candidate(n = 63) == 31
    assert candidate(n = 1125899906842623) == 562949953421311
    assert candidate(n = 17592186044415) == 8796093022207
    assert candidate(n = 67108863) == 33554431
    assert candidate(n = 35184372088831) == 17592186044415
    assert candidate(n = 32767) == 16383
    assert candidate(n = 4294967295) == 2147483647
    assert candidate(n = 16384) == 16383
    assert candidate(n = 2251799813685247) == 1125899906842623
    assert candidate(n = 4194303) == 2097151
    assert candidate(n = 144115188075855871) == 72057594037927935
    assert candidate(n = 17179869183) == 8589934591
    assert candidate(n = 9223372036854775807) == 4611686018427387903
    assert candidate(n = 255) == 127
    assert candidate(n = 34359738367) == 17179869183
    assert candidate(n = 8192) == 8191
    assert candidate(n = 65536) == 65535
    assert candidate(n = 32) == 31
    assert candidate(n = 1023) == 511
    assert candidate(n = 274877906943) == 137438953471
    assert candidate(n = 9007199254740991) == 4503599627370495
    assert candidate(n = 127) == 63
    assert candidate(n = 15) == 7
    assert candidate(n = 536870911) == 268435455
    assert candidate(n = 33554431) == 16777215
    assert candidate(n = 72057594037927935) == 36028797018963967
    assert candidate(n = 16383) == 8191
    assert candidate(n = 288230376151711743) == 144115188075855871
    assert candidate(n = 4503599627370495) == 2251799813685247
    assert candidate(n = 134217727) == 67108863
    assert candidate(n = 64) == 63
    assert candidate(n = 8388607) == 4194303
    assert candidate(n = 2097151) == 1048575
    assert candidate(n = 4398046511103) == 2199023255551
    assert candidate(n = 1024) == 1023
    assert candidate(n = 128) == 127
    assert candidate(n = 4095) == 2047
    assert candidate(n = 18014398509481983) == 9007199254740991
    assert candidate(n = 2305843009213693951) == 1152921504606846975
    assert candidate(n = 65535) == 32767
    assert candidate(n = 1152921504606846975) == 576460752303423487
    assert candidate(n = 31) == 15
    assert candidate(n = 36028797018963967) == 18014398509481983
    assert candidate(n = 7) == 3
    assert candidate(n = 1234567890123456789) == 1152921504606846975
    assert candidate(n = 18446744073709551615) == 9223372036854775807
    assert candidate(n = 511) == 255
    assert candidate(n = 1000000000000000001) == 576460752303423487
    assert candidate(n = 2123366401) == 1073741823
    assert candidate(n = 500000000000000) == 281474976710655
    assert candidate(n = 123456789123456) == 70368744177663
    assert candidate(n = 1000000000) == 536870911
    assert candidate(n = 123456789012345) == 70368744177663
    assert candidate(n = 1047552) == 524287
    assert candidate(n = 987654321987654) == 562949953421311


