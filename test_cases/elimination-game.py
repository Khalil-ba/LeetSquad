def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 11) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 54: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 481110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 481110: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 534765398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 534765398: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 510: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 244140) == 130558
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 244140) == 130558: {e}')
    
    total += 1
    try:
        result = candidate(n = 15258) == 8160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15258) == 8160: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3814) == 2040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3814) == 2040: {e}')
    
    total += 1
    try:
        result = candidate(n = 119) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 119) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 534765056
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 534765056: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 5502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 5502: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == 1366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == 1366: {e}')
    
    total += 1
    try:
        result = candidate(n = 976562) == 522232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 976562) == 522232: {e}')
    
    total += 1
    try:
        result = candidate(n = 1953125) == 908662
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1953125) == 908662: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 2047) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2047) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(n = 16383) == 8192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16383) == 8192: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10001) == 5974
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10001) == 5974: {e}')
    
    total += 1
    try:
        result = candidate(n = 16384) == 5462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16384) == 5462: {e}')
    
    total += 1
    try:
        result = candidate(n = 59) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000000) == 133691350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000000) == 133691350: {e}')
    
    total += 1
    try:
        result = candidate(n = 238) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 238) == 128: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 125000000) == 58154326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125000000) == 58154326: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 5974
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 5974: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 510: {e}')
    
    total += 1
    try:
        result = candidate(n = 15625000) == 8355710
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15625000) == 8355710: {e}')
    
    total += 1
    try:
        result = candidate(n = 7812500) == 3634646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7812500) == 3634646: {e}')
    
    total += 1
    try:
        result = candidate(n = 62500000) == 33422838
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 62500000) == 33422838: {e}')
    
    total += 1
    try:
        result = candidate(n = 122070) == 56792
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 122070) == 56792: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000) == 33551830
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000) == 33551830: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == 86: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 342: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 54: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == 6150102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == 6150102: {e}')
    
    total += 1
    try:
        result = candidate(n = 61035) == 32640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 61035) == 32640: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 55286
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 55286: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == 1366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == 1366: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == 349526
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == 349526: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 504: {e}')
    
    total += 1
    try:
        result = candidate(n = 953) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 953) == 510: {e}')
    
    total += 1
    try:
        result = candidate(n = 3906250) == 2088928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3906250) == 2088928: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == 5462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == 5462: {e}')
    
    total += 1
    try:
        result = candidate(n = 30517) == 14198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30517) == 14198: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == 21846
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == 21846: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 2014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 2014: {e}')
    
    total += 1
    try:
        result = candidate(n = 7629) == 3550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7629) == 3550: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 86: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == 512: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 5984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 5984: {e}')
    
    total += 1
    try:
        result = candidate(n = 31250000) == 14538582
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31250000) == 14538582: {e}')
    
    total += 1
    try:
        result = candidate(n = 476) == 222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 476) == 222: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == 534765398
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == 534765398: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 534740470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 534740470: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000000) == 1924950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000000) == 1924950: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 259446
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 259446: {e}')
    
    total += 1
    try:
        result = candidate(n = 488281) == 227166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 488281) == 227166: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765) == 54750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765) == 54750: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 232617302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 232617302: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000001) == 481110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000001) == 481110: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == 342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == 342: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 481152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 481152: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 63318
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 63318: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 246: {e}')
    
    total += 1
    try:
        result = candidate(n = 1907) == 888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1907) == 888: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 11) == 8
    assert candidate(n = 100) == 54
    assert candidate(n = 9) == 6
    assert candidate(n = 1000000) == 481110
    assert candidate(n = 2) == 2
    assert candidate(n = 20) == 6
    assert candidate(n = 1) == 1
    assert candidate(n = 1000000000) == 534765398
    assert candidate(n = 1000) == 510
    assert candidate(n = 10) == 8
    assert candidate(n = 25) == 14
    assert candidate(n = 244140) == 130558
    assert candidate(n = 15258) == 8160
    assert candidate(n = 3) == 2
    assert candidate(n = 3814) == 2040
    assert candidate(n = 119) == 56
    assert candidate(n = 29) == 14
    assert candidate(n = 999999999) == 534765056
    assert candidate(n = 12345) == 5502
    assert candidate(n = 4096) == 1366
    assert candidate(n = 976562) == 522232
    assert candidate(n = 1953125) == 908662
    assert candidate(n = 50) == 24
    assert candidate(n = 2047) == 1024
    assert candidate(n = 16383) == 8192
    assert candidate(n = 5) == 2
    assert candidate(n = 10001) == 5974
    assert candidate(n = 16384) == 5462
    assert candidate(n = 59) == 32
    assert candidate(n = 250000000) == 133691350
    assert candidate(n = 238) == 128
    assert candidate(n = 4) == 2
    assert candidate(n = 125000000) == 58154326
    assert candidate(n = 10000) == 5974
    assert candidate(n = 1001) == 510
    assert candidate(n = 15625000) == 8355710
    assert candidate(n = 7812500) == 3634646
    assert candidate(n = 62500000) == 33422838
    assert candidate(n = 122070) == 56792
    assert candidate(n = 50000000) == 33551830
    assert candidate(n = 128) == 86
    assert candidate(n = 1024) == 342
    assert candidate(n = 101) == 54
    assert candidate(n = 10000000) == 6150102
    assert candidate(n = 61035) == 32640
    assert candidate(n = 100000) == 55286
    assert candidate(n = 2048) == 1366
    assert candidate(n = 1048576) == 349526
    assert candidate(n = 999) == 504
    assert candidate(n = 953) == 510
    assert candidate(n = 3906250) == 2088928
    assert candidate(n = 8192) == 5462
    assert candidate(n = 30517) == 14198
    assert candidate(n = 65536) == 21846
    assert candidate(n = 5000) == 2014
    assert candidate(n = 7629) == 3550
    assert candidate(n = 256) == 86
    assert candidate(n = 1023) == 512
    assert candidate(n = 9999) == 5984
    assert candidate(n = 31250000) == 14538582
    assert candidate(n = 476) == 222
    assert candidate(n = 1000000001) == 534765398
    assert candidate(n = 127) == 64
    assert candidate(n = 987654321) == 534740470
    assert candidate(n = 5000000) == 1924950
    assert candidate(n = 500000) == 259446
    assert candidate(n = 488281) == 227166
    assert candidate(n = 98765) == 54750
    assert candidate(n = 500000000) == 232617302
    assert candidate(n = 31) == 16
    assert candidate(n = 1000001) == 481110
    assert candidate(n = 14) == 8
    assert candidate(n = 512) == 342
    assert candidate(n = 999999) == 481152
    assert candidate(n = 123456) == 63318
    assert candidate(n = 500) == 246
    assert candidate(n = 1907) == 888
    assert candidate(n = 7) == 4


