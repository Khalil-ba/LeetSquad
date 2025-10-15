def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = 7,b = 14,n = 4) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 14,n = 4) == 98: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 9,n = 4) == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 9,n = 4) == 143: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2,n = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2,n = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 7,n = 5) == 930
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 7,n = 5) == 930: {e}')
    
    total += 1
    try:
        result = candidate(a = 1024,b = 512,n = 11) == 1570305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1024,b = 512,n = 11) == 1570305: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 12,n = 4) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 12,n = 4) == 56: {e}')
    
    total += 1
    try:
        result = candidate(a = 12,b = 5,n = 4) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 12,b = 5,n = 4) == 98: {e}')
    
    total += 1
    try:
        result = candidate(a = 249,b = 249,n = 50) == 178448631
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 249,b = 249,n = 50) == 178448631: {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 0,n = 50) == 178448631
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 0,n = 50) == 178448631: {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 0,n = 5) == 961
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 0,n = 5) == 961: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 3,n = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 3,n = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 8,n = 4) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 8,n = 4) == 225: {e}')
    
    total += 1
    try:
        result = candidate(a = 1024,b = 512,n = 10) == 1570305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1024,b = 512,n = 10) == 1570305: {e}')
    
    total += 1
    try:
        result = candidate(a = 249,b = 248,n = 50) == 279487308
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 249,b = 248,n = 50) == 279487308: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 3,n = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 3,n = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 6,n = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 6,n = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = 1099511627776,b = 2199023255552,n = 42) == 421746426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1099511627776,b = 2199023255552,n = 42) == 421746426: {e}')
    
    total += 1
    try:
        result = candidate(a = 123,b = 456,n = 10) == 647348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123,b = 456,n = 10) == 647348: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000000000,b = 1000000000,n = 30) == 388912871
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000000000,b = 1000000000,n = 30) == 388912871: {e}')
    
    total += 1
    try:
        result = candidate(a = 1023456789,b = 9876543210,n = 30) == 443244632
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1023456789,b = 9876543210,n = 30) == 443244632: {e}')
    
    total += 1
    try:
        result = candidate(a = 4294967295,b = 1,n = 32) == 145586001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4294967295,b = 1,n = 32) == 145586001: {e}')
    
    total += 1
    try:
        result = candidate(a = 256,b = 1024,n = 11) == 1832193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 256,b = 1024,n = 11) == 1832193: {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 25,n = 5) == 961
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 25,n = 5) == 961: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2499999999999,n = 50) == 63711638
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2499999999999,n = 50) == 63711638: {e}')
    
    total += 1
    try:
        result = candidate(a = 4294967295,b = 4294967295,n = 32) == 992409480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4294967295,b = 4294967295,n = 32) == 992409480: {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 1,n = 50) == 279487308
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 1,n = 50) == 279487308: {e}')
    
    total += 1
    try:
        result = candidate(a = 1023,b = 512,n = 10) == 589056
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1023,b = 512,n = 10) == 589056: {e}')
    
    total += 1
    try:
        result = candidate(a = 123456,b = 654321,n = 20) == 306001604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123456,b = 654321,n = 20) == 306001604: {e}')
    
    total += 1
    try:
        result = candidate(a = 123456789,b = 987654321,n = 35) == 251423918
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123456789,b = 987654321,n = 35) == 251423918: {e}')
    
    total += 1
    try:
        result = candidate(a = 4294967294,b = 4294967295,n = 32) == 697442213
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4294967294,b = 4294967295,n = 32) == 697442213: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 15,n = 4) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 15,n = 4) == 132: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 3,n = 50) == 279487308
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 3,n = 50) == 279487308: {e}')
    
    total += 1
    try:
        result = candidate(a = 500000000,b = 500000001,n = 30) == 315171055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 500000000,b = 500000001,n = 30) == 315171055: {e}')
    
    total += 1
    try:
        result = candidate(a = 45,b = 28,n = 6) == 1426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 45,b = 28,n = 6) == 1426: {e}')
    
    total += 1
    try:
        result = candidate(a = 500000000,b = 1000000000,n = 35) == 632039372
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 500000000,b = 1000000000,n = 35) == 632039372: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 4,n = 3) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 4,n = 3) == 77: {e}')
    
    total += 1
    try:
        result = candidate(a = 9876543210987654,b = 1234567890123456,n = 50) == 300686351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 9876543210987654,b = 1234567890123456,n = 50) == 300686351: {e}')
    
    total += 1
    try:
        result = candidate(a = 1023,b = 2047,n = 11) == 2094081
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1023,b = 2047,n = 11) == 2094081: {e}')
    
    total += 1
    try:
        result = candidate(a = 456789123,b = 234567891,n = 35) == 765343141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 456789123,b = 234567891,n = 35) == 765343141: {e}')
    
    total += 1
    try:
        result = candidate(a = 999999999,b = 888888888,n = 45) == 179328999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 999999999,b = 888888888,n = 45) == 179328999: {e}')
    
    total += 1
    try:
        result = candidate(a = 789,b = 101112,n = 15) == 211542482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 789,b = 101112,n = 15) == 211542482: {e}')
    
    total += 1
    try:
        result = candidate(a = 123456789,b = 987654321,n = 20) == 309102622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123456789,b = 987654321,n = 20) == 309102622: {e}')
    
    total += 1
    try:
        result = candidate(a = 67890,b = 13579,n = 15) == 715925548
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 67890,b = 13579,n = 15) == 715925548: {e}')
    
    total += 1
    try:
        result = candidate(a = 31,b = 15,n = 5) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 31,b = 15,n = 5) == 465: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000000000,b = 500000000,n = 30) == 446861332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000000000,b = 500000000,n = 30) == 446861332: {e}')
    
    total += 1
    try:
        result = candidate(a = 111111111,b = 222222222,n = 40) == 554920250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 111111111,b = 222222222,n = 40) == 554920250: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000000000,b = 2000000000,n = 49) == 857287546
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000000000,b = 2000000000,n = 49) == 857287546: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2147483647,n = 30) == 536396503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2147483647,n = 30) == 536396503: {e}')
    
    total += 1
    try:
        result = candidate(a = 987654321,b = 123456789,n = 30) == 664805056
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 987654321,b = 123456789,n = 30) == 664805056: {e}')
    
    total += 1
    try:
        result = candidate(a = 555555555,b = 666666666,n = 48) == 651387213
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 555555555,b = 666666666,n = 48) == 651387213: {e}')
    
    total += 1
    try:
        result = candidate(a = 299999999,b = 299999998,n = 28) == 523486406
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 299999999,b = 299999998,n = 28) == 523486406: {e}')
    
    total += 1
    try:
        result = candidate(a = 1048576,b = 2097152,n = 22) == 64477598
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1048576,b = 2097152,n = 22) == 64477598: {e}')
    
    total += 1
    try:
        result = candidate(a = 2147483647,b = 1073741823,n = 31) == 851567558
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2147483647,b = 1073741823,n = 31) == 851567558: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2147483647,n = 50) == 519485508
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2147483647,n = 50) == 519485508: {e}')
    
    total += 1
    try:
        result = candidate(a = 135792468,b = 246813579,n = 32) == 736568943
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 135792468,b = 246813579,n = 32) == 736568943: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000000000000,b = 999999999999,n = 40) == 810111777
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000000000000,b = 999999999999,n = 40) == 810111777: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2,n = 50) == 481564664
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2,n = 50) == 481564664: {e}')
    
    total += 1
    try:
        result = candidate(a = 18446744073709551615,b = 18446744073709551614,n = 50) == 532600269
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 18446744073709551615,b = 18446744073709551614,n = 50) == 532600269: {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 50,n = 10) == 1046529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 50,n = 10) == 1046529: {e}')
    
    total += 1
    try:
        result = candidate(a = 2147483647,b = 2147483647,n = 32) == 992409480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2147483647,b = 2147483647,n = 32) == 992409480: {e}')
    
    total += 1
    try:
        result = candidate(a = 65535,b = 131071,n = 17) == 589737929
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 65535,b = 131071,n = 17) == 589737929: {e}')
    
    total += 1
    try:
        result = candidate(a = 13,b = 29,n = 5) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 13,b = 29,n = 5) == 465: {e}')
    
    total += 1
    try:
        result = candidate(a = 123456789,b = 987654321,n = 30) == 664805056
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123456789,b = 987654321,n = 30) == 664805056: {e}')
    
    total += 1
    try:
        result = candidate(a = 2147483647,b = 1,n = 30) == 536396503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2147483647,b = 1,n = 30) == 536396503: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000000000,b = 1000000000,n = 31) == 850618742
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000000000,b = 1000000000,n = 31) == 850618742: {e}')
    
    total += 1
    try:
        result = candidate(a = 123,b = 456,n = 8) == 84660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 123,b = 456,n = 8) == 84660: {e}')
    
    total += 1
    try:
        result = candidate(a = 12345,b = 67890,n = 15) == 742597886
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 12345,b = 67890,n = 15) == 742597886: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 3,n = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 3,n = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2147483647,n = 31) == 536396503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2147483647,n = 31) == 536396503: {e}')
    
    total += 1
    try:
        result = candidate(a = 248,b = 231,n = 10) == 1015056
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 248,b = 231,n = 10) == 1015056: {e}')
    
    total += 1
    try:
        result = candidate(a = 999999999,b = 999999998,n = 30) == 315171055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 999999999,b = 999999998,n = 30) == 315171055: {e}')
    
    total += 1
    try:
        result = candidate(a = 511,b = 1023,n = 10) == 522753
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 511,b = 1023,n = 10) == 522753: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 0,n = 50) == 279487308
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 0,n = 50) == 279487308: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = 7,b = 14,n = 4) == 98
    assert candidate(a = 15,b = 9,n = 4) == 143
    assert candidate(a = 1,b = 2,n = 1) == 2
    assert candidate(a = 6,b = 7,n = 5) == 930
    assert candidate(a = 1024,b = 512,n = 11) == 1570305
    assert candidate(a = 3,b = 12,n = 4) == 56
    assert candidate(a = 12,b = 5,n = 4) == 98
    assert candidate(a = 249,b = 249,n = 50) == 178448631
    assert candidate(a = 0,b = 0,n = 50) == 178448631
    assert candidate(a = 0,b = 0,n = 5) == 961
    assert candidate(a = 3,b = 3,n = 2) == 9
    assert candidate(a = 8,b = 8,n = 4) == 225
    assert candidate(a = 1024,b = 512,n = 10) == 1570305
    assert candidate(a = 249,b = 248,n = 50) == 279487308
    assert candidate(a = 7,b = 3,n = 3) == 21
    assert candidate(a = 1,b = 1,n = 1) == 1
    assert candidate(a = 1,b = 6,n = 3) == 12
    assert candidate(a = 1099511627776,b = 2199023255552,n = 42) == 421746426
    assert candidate(a = 123,b = 456,n = 10) == 647348
    assert candidate(a = 1000000000,b = 1000000000,n = 30) == 388912871
    assert candidate(a = 1023456789,b = 9876543210,n = 30) == 443244632
    assert candidate(a = 4294967295,b = 1,n = 32) == 145586001
    assert candidate(a = 256,b = 1024,n = 11) == 1832193
    assert candidate(a = 25,b = 25,n = 5) == 961
    assert candidate(a = 1,b = 2499999999999,n = 50) == 63711638
    assert candidate(a = 4294967295,b = 4294967295,n = 32) == 992409480
    assert candidate(a = 0,b = 1,n = 50) == 279487308
    assert candidate(a = 1023,b = 512,n = 10) == 589056
    assert candidate(a = 123456,b = 654321,n = 20) == 306001604
    assert candidate(a = 123456789,b = 987654321,n = 35) == 251423918
    assert candidate(a = 4294967294,b = 4294967295,n = 32) == 697442213
    assert candidate(a = 8,b = 15,n = 4) == 132
    assert candidate(a = 2,b = 3,n = 50) == 279487308
    assert candidate(a = 500000000,b = 500000001,n = 30) == 315171055
    assert candidate(a = 45,b = 28,n = 6) == 1426
    assert candidate(a = 500000000,b = 1000000000,n = 35) == 632039372
    assert candidate(a = 8,b = 4,n = 3) == 77
    assert candidate(a = 9876543210987654,b = 1234567890123456,n = 50) == 300686351
    assert candidate(a = 1023,b = 2047,n = 11) == 2094081
    assert candidate(a = 456789123,b = 234567891,n = 35) == 765343141
    assert candidate(a = 999999999,b = 888888888,n = 45) == 179328999
    assert candidate(a = 789,b = 101112,n = 15) == 211542482
    assert candidate(a = 123456789,b = 987654321,n = 20) == 309102622
    assert candidate(a = 67890,b = 13579,n = 15) == 715925548
    assert candidate(a = 31,b = 15,n = 5) == 465
    assert candidate(a = 1000000000,b = 500000000,n = 30) == 446861332
    assert candidate(a = 111111111,b = 222222222,n = 40) == 554920250
    assert candidate(a = 1000000000,b = 2000000000,n = 49) == 857287546
    assert candidate(a = 1,b = 2147483647,n = 30) == 536396503
    assert candidate(a = 987654321,b = 123456789,n = 30) == 664805056
    assert candidate(a = 555555555,b = 666666666,n = 48) == 651387213
    assert candidate(a = 299999999,b = 299999998,n = 28) == 523486406
    assert candidate(a = 1048576,b = 2097152,n = 22) == 64477598
    assert candidate(a = 2147483647,b = 1073741823,n = 31) == 851567558
    assert candidate(a = 1,b = 2147483647,n = 50) == 519485508
    assert candidate(a = 135792468,b = 246813579,n = 32) == 736568943
    assert candidate(a = 1000000000000,b = 999999999999,n = 40) == 810111777
    assert candidate(a = 1,b = 2,n = 50) == 481564664
    assert candidate(a = 18446744073709551615,b = 18446744073709551614,n = 50) == 532600269
    assert candidate(a = 50,b = 50,n = 10) == 1046529
    assert candidate(a = 2147483647,b = 2147483647,n = 32) == 992409480
    assert candidate(a = 65535,b = 131071,n = 17) == 589737929
    assert candidate(a = 13,b = 29,n = 5) == 465
    assert candidate(a = 123456789,b = 987654321,n = 30) == 664805056
    assert candidate(a = 2147483647,b = 1,n = 30) == 536396503
    assert candidate(a = 1000000000,b = 1000000000,n = 31) == 850618742
    assert candidate(a = 123,b = 456,n = 8) == 84660
    assert candidate(a = 12345,b = 67890,n = 15) == 742597886
    assert candidate(a = 2,b = 3,n = 1) == 6
    assert candidate(a = 1,b = 2147483647,n = 31) == 536396503
    assert candidate(a = 248,b = 231,n = 10) == 1015056
    assert candidate(a = 999999999,b = 999999998,n = 30) == 315171055
    assert candidate(a = 511,b = 1023,n = 10) == 522753
    assert candidate(a = 1,b = 0,n = 50) == 279487308


