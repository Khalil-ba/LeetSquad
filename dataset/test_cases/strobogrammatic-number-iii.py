def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(low = "1",high = "10") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "10") == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000",high = "9999999999") == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000",high = "9999999999") == 2500: {e}')
    
    total += 1
    try:
        result = candidate(low = "0",high = "150") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "0",high = "150") == 9: {e}')
    
    total += 1
    try:
        result = candidate(low = "100",high = "200") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100",high = "200") == 3: {e}')
    
    total += 1
    try:
        result = candidate(low = "500",high = "1000") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "500",high = "1000") == 9: {e}')
    
    total += 1
    try:
        result = candidate(low = "69",high = "96") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "69",high = "96") == 3: {e}')
    
    total += 1
    try:
        result = candidate(low = "88",high = "88") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "88",high = "88") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "1111",high = "2222") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1111",high = "2222") == 4: {e}')
    
    total += 1
    try:
        result = candidate(low = "0",high = "0") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "0",high = "0") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000",high = "90000") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000",high = "90000") == 45: {e}')
    
    total += 1
    try:
        result = candidate(low = "50",high = "100") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "50",high = "100") == 3: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000",high = "100000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000",high = "100000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "696969696969696969",high = "696969696969696969") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "696969696969696969",high = "696969696969696969") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000",high = "1111111111") == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000",high = "1111111111") == 157: {e}')
    
    total += 1
    try:
        result = candidate(low = "555555555555555",high = "666666666666666") == 23438
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "555555555555555",high = "666666666666666") == 23438: {e}')
    
    total += 1
    try:
        result = candidate(low = "99999",high = "100000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "99999",high = "100000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "696969",high = "969696") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "696969",high = "969696") == 43: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000",high = "10000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000",high = "10000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "180",high = "180") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "180",high = "180") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "868",high = "868") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "868",high = "868") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "6",high = "9") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "6",high = "9") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000000",high = "9999999999999") == 37500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000000",high = "9999999999999") == 37500: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "2147483647") == 3123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "2147483647") == 3123: {e}')
    
    total += 1
    try:
        result = candidate(low = "888888888888888",high = "888888888888888") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "888888888888888",high = "888888888888888") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000000000",high = "10000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000000000",high = "10000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "9876543210",high = "9876543210") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9876543210",high = "9876543210") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "110011",high = "880088") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "110011",high = "880088") == 61: {e}')
    
    total += 1
    try:
        result = candidate(low = "100100100",high = "111111111") == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100100100",high = "111111111") == 92: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000000000",high = "999999999999999") == 187500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000000000",high = "999999999999999") == 187500: {e}')
    
    total += 1
    try:
        result = candidate(low = "11111111111111",high = "22222222222222") == 11719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "11111111111111",high = "22222222222222") == 11719: {e}')
    
    total += 1
    try:
        result = candidate(low = "111111111111111",high = "999999999999999") == 175781
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "111111111111111",high = "999999999999999") == 175781: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000",high = "999999") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000",high = "999999") == 100: {e}')
    
    total += 1
    try:
        result = candidate(low = "1001",high = "1000000000") == 2480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1001",high = "1000000000") == 2480: {e}')
    
    total += 1
    try:
        result = candidate(low = "6969696969696969",high = "9696969696969696") == 130209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "6969696969696969",high = "9696969696969696") == 130209: {e}')
    
    total += 1
    try:
        result = candidate(low = "12321",high = "98789") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "12321",high = "98789") == 50: {e}')
    
    total += 1
    try:
        result = candidate(low = "0",high = "999999999999999") == 312499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "0",high = "999999999999999") == 312499: {e}')
    
    total += 1
    try:
        result = candidate(low = "0",high = "1000000000") == 2499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "0",high = "1000000000") == 2499: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000",high = "10000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000",high = "10000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "123456789012345",high = "987654321098765") == 155625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123456789012345",high = "987654321098765") == 155625: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "111111111",high = "999999999") == 1406
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "111111111",high = "999999999") == 1406: {e}')
    
    total += 1
    try:
        result = candidate(low = "111",high = "999999") == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "111",high = "999999") == 191: {e}')
    
    total += 1
    try:
        result = candidate(low = "888888888",high = "999999999") == 469
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "888888888",high = "999999999") == 469: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000000001",high = "100000000000002") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000000001",high = "100000000000002") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000000000000",high = "200000000000000000") == 390625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000000000000",high = "200000000000000000") == 390625: {e}')
    
    total += 1
    try:
        result = candidate(low = "0",high = "1000000") == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "0",high = "1000000") == 199: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000000000",high = "9000000000000000") == 234375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000000000",high = "9000000000000000") == 234375: {e}')
    
    total += 1
    try:
        result = candidate(low = "101",high = "1001") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "101",high = "1001") == 13: {e}')
    
    total += 1
    try:
        result = candidate(low = "110011",high = "988989") == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "110011",high = "988989") == 89: {e}')
    
    total += 1
    try:
        result = candidate(low = "200000000000000",high = "300000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "200000000000000",high = "300000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000000000",high = "199999999999999") == 46875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000000000",high = "199999999999999") == 46875: {e}')
    
    total += 1
    try:
        result = candidate(low = "999999999",high = "1000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "999999999",high = "1000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000",high = "9999999") == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000",high = "9999999") == 300: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "2000000000") == 3123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "2000000000") == 3123: {e}')
    
    total += 1
    try:
        result = candidate(low = "696969696969696",high = "969696969696969") == 78125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "696969696969696",high = "969696969696969") == 78125: {e}')
    
    total += 1
    try:
        result = candidate(low = "111",high = "111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "111",high = "111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "12345678987654321",high = "98765432123456789") == 778125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "12345678987654321",high = "98765432123456789") == 778125: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000000000",high = "180000000000000") == 28125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000000000",high = "180000000000000") == 28125: {e}')
    
    total += 1
    try:
        result = candidate(low = "101010101010101",high = "110011001100110") == 7513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "101010101010101",high = "110011001100110") == 7513: {e}')
    
    total += 1
    try:
        result = candidate(low = "110011",high = "980089") == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "110011",high = "980089") == 86: {e}')
    
    total += 1
    try:
        result = candidate(low = "69",high = "969696969696969") == 292964
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "69",high = "969696969696969") == 292964: {e}')
    
    total += 1
    try:
        result = candidate(low = "111",high = "999") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "111",high = "999") == 11: {e}')
    
    total += 1
    try:
        result = candidate(low = "8888888888888888",high = "8888888888888888") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8888888888888888",high = "8888888888888888") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000000000",high = "20000000000000000") == 234375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000000000",high = "20000000000000000") == 234375: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000000000",high = "99999999999999999") == 937500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000000000",high = "99999999999999999") == 937500: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000000000",high = "1000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000000000",high = "1000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000000",high = "2000000000000") == 9375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000000",high = "2000000000000") == 9375: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "999999999999999") == 312498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "999999999999999") == 312498: {e}')
    
    total += 1
    try:
        result = candidate(low = "110011001",high = "980089008") == 1276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "110011001",high = "980089008") == 1276: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000",high = "9999") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000",high = "9999") == 20: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000",high = "1800000000") == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000",high = "1800000000") == 375: {e}')
    
    total += 1
    try:
        result = candidate(low = "11",high = "88") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "11",high = "88") == 3: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000000000000",high = "999999999999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000000000000",high = "999999999999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000",high = "2000000000") == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000",high = "2000000000") == 625: {e}')
    
    total += 1
    try:
        result = candidate(low = "123456789",high = "987654321") == 1245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123456789",high = "987654321") == 1245: {e}')
    
    total += 1
    try:
        result = candidate(low = "111111111111111",high = "222222222222222") == 35156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "111111111111111",high = "222222222222222") == 35156: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000",high = "10000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000",high = "10000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "2000000000",high = "3000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "2000000000",high = "3000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "11000000000000011",high = "98000000000000899") == 796876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "11000000000000011",high = "98000000000000899") == 796876: {e}')
    
    total += 1
    try:
        result = candidate(low = "69000069",high = "96000096") == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "69000069",high = "96000096") == 201: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000",high = "1000000000") == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000",high = "1000000000") == 1500: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000",high = "11000000001") == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000",high = "11000000001") == 375: {e}')
    
    total += 1
    try:
        result = candidate(low = "555555555",high = "666666666") == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "555555555",high = "666666666") == 188: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000",high = "9000000000") == 1875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000",high = "9000000000") == 1875: {e}')
    
    total += 1
    try:
        result = candidate(low = "123456789012345",high = "123456789012345") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123456789012345",high = "123456789012345") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000",high = "200000000") == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000",high = "200000000") == 375: {e}')
    
    total += 1
    try:
        result = candidate(low = "888888888888888",high = "999999999999999") == 58594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "888888888888888",high = "999999999999999") == 58594: {e}')
    
    total += 1
    try:
        result = candidate(low = "1111",high = "1111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1111",high = "1111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "1234567890",high = "12345678900") == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1234567890",high = "12345678900") == 3000: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000000",high = "1000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000000",high = "1000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "1111",high = "8888") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1111",high = "8888") == 13: {e}')
    
    total += 1
    try:
        result = candidate(low = "18000000000000001",high = "68000000000000089") == 234376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "18000000000000001",high = "68000000000000089") == 234376: {e}')
    
    total += 1
    try:
        result = candidate(low = "696969696969",high = "969696969696") == 5209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "696969696969",high = "969696969696") == 5209: {e}')
    
    total += 1
    try:
        result = candidate(low = "111111111",high = "888888888") == 938
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "111111111",high = "888888888") == 938: {e}')
    
    total += 1
    try:
        result = candidate(low = "8888",high = "888888") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8888",high = "888888") == 136: {e}')
    
    total += 1
    try:
        result = candidate(low = "110011",high = "111111") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "110011",high = "111111") == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000",high = "200000") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000",high = "200000") == 25: {e}')
    
    total += 1
    try:
        result = candidate(low = "200000000000000",high = "210000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "200000000000000",high = "210000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "8000000000",high = "8999999999") == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8000000000",high = "8999999999") == 625: {e}')
    
    total += 1
    try:
        result = candidate(low = "8888888888",high = "8888888888") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8888888888",high = "8888888888") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "0",high = "1") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "0",high = "1") == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = "100",high = "999") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100",high = "999") == 12: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000000",high = "999999999999") == 12500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000000",high = "999999999999") == 12500: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000000001",high = "10000000000000009") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000000001",high = "10000000000000009") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "9876543210",high = "10987654321") == 529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9876543210",high = "10987654321") == 529: {e}')
    
    total += 1
    try:
        result = candidate(low = "200000000",high = "200000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "200000000",high = "200000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "690069",high = "690069") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "690069",high = "690069") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(low = "1",high = "10") == 2
    assert candidate(low = "1000000000",high = "9999999999") == 2500
    assert candidate(low = "0",high = "150") == 9
    assert candidate(low = "100",high = "200") == 3
    assert candidate(low = "500",high = "1000") == 9
    assert candidate(low = "69",high = "96") == 3
    assert candidate(low = "88",high = "88") == 1
    assert candidate(low = "1111",high = "2222") == 4
    assert candidate(low = "0",high = "0") == 1
    assert candidate(low = "10000",high = "90000") == 45
    assert candidate(low = "50",high = "100") == 3
    assert candidate(low = "100000000",high = "100000001") == 1
    assert candidate(low = "696969696969696969",high = "696969696969696969") == 1
    assert candidate(low = "1000000000",high = "1111111111") == 157
    assert candidate(low = "555555555555555",high = "666666666666666") == 23438
    assert candidate(low = "99999",high = "100000") == 0
    assert candidate(low = "696969",high = "969696") == 43
    assert candidate(low = "10000000000",high = "10000000001") == 1
    assert candidate(low = "180",high = "180") == 0
    assert candidate(low = "868",high = "868") == 0
    assert candidate(low = "6",high = "9") == 1
    assert candidate(low = "1000000000000",high = "9999999999999") == 37500
    assert candidate(low = "1",high = "2147483647") == 3123
    assert candidate(low = "888888888888888",high = "888888888888888") == 1
    assert candidate(low = "10000000000000000",high = "10000000000000000") == 0
    assert candidate(low = "9876543210",high = "9876543210") == 0
    assert candidate(low = "110011",high = "880088") == 61
    assert candidate(low = "100100100",high = "111111111") == 92
    assert candidate(low = "100000000000000",high = "999999999999999") == 187500
    assert candidate(low = "11111111111111",high = "22222222222222") == 11719
    assert candidate(low = "111111111111111",high = "999999999999999") == 175781
    assert candidate(low = "100000",high = "999999") == 100
    assert candidate(low = "1001",high = "1000000000") == 2480
    assert candidate(low = "6969696969696969",high = "9696969696969696") == 130209
    assert candidate(low = "12321",high = "98789") == 50
    assert candidate(low = "0",high = "999999999999999") == 312499
    assert candidate(low = "0",high = "1000000000") == 2499
    assert candidate(low = "10000000",high = "10000001") == 1
    assert candidate(low = "123456789012345",high = "987654321098765") == 155625
    assert candidate(low = "1",high = "1") == 1
    assert candidate(low = "111111111",high = "999999999") == 1406
    assert candidate(low = "111",high = "999999") == 191
    assert candidate(low = "888888888",high = "999999999") == 469
    assert candidate(low = "100000000000001",high = "100000000000002") == 1
    assert candidate(low = "100000000000000000",high = "200000000000000000") == 390625
    assert candidate(low = "0",high = "1000000") == 199
    assert candidate(low = "1000000000000000",high = "9000000000000000") == 234375
    assert candidate(low = "101",high = "1001") == 13
    assert candidate(low = "110011",high = "988989") == 89
    assert candidate(low = "200000000000000",high = "300000000000000") == 0
    assert candidate(low = "100000000000000",high = "199999999999999") == 46875
    assert candidate(low = "999999999",high = "1000000000") == 0
    assert candidate(low = "1000000",high = "9999999") == 300
    assert candidate(low = "1",high = "2000000000") == 3123
    assert candidate(low = "696969696969696",high = "969696969696969") == 78125
    assert candidate(low = "111",high = "111") == 1
    assert candidate(low = "12345678987654321",high = "98765432123456789") == 778125
    assert candidate(low = "100000000000000",high = "180000000000000") == 28125
    assert candidate(low = "101010101010101",high = "110011001100110") == 7513
    assert candidate(low = "110011",high = "980089") == 86
    assert candidate(low = "69",high = "969696969696969") == 292964
    assert candidate(low = "111",high = "999") == 11
    assert candidate(low = "8888888888888888",high = "8888888888888888") == 1
    assert candidate(low = "10000000000000000",high = "20000000000000000") == 234375
    assert candidate(low = "10000000000000000",high = "99999999999999999") == 937500
    assert candidate(low = "1000000000000000",high = "1000000000000000") == 0
    assert candidate(low = "1000000000000",high = "2000000000000") == 9375
    assert candidate(low = "1",high = "999999999999999") == 312498
    assert candidate(low = "110011001",high = "980089008") == 1276
    assert candidate(low = "1000",high = "9999") == 20
    assert candidate(low = "1000000000",high = "1800000000") == 375
    assert candidate(low = "11",high = "88") == 3
    assert candidate(low = "1000000000000000000",high = "999999999999999999") == 0
    assert candidate(low = "1000000000",high = "2000000000") == 625
    assert candidate(low = "123456789",high = "987654321") == 1245
    assert candidate(low = "111111111111111",high = "222222222222222") == 35156
    assert candidate(low = "10000000000",high = "10000000000") == 0
    assert candidate(low = "2000000000",high = "3000000000") == 0
    assert candidate(low = "11000000000000011",high = "98000000000000899") == 796876
    assert candidate(low = "69000069",high = "96000096") == 201
    assert candidate(low = "100000000",high = "1000000000") == 1500
    assert candidate(low = "10000000000",high = "11000000001") == 375
    assert candidate(low = "555555555",high = "666666666") == 188
    assert candidate(low = "1000000000",high = "9000000000") == 1875
    assert candidate(low = "123456789012345",high = "123456789012345") == 0
    assert candidate(low = "100000000",high = "200000000") == 375
    assert candidate(low = "888888888888888",high = "999999999999999") == 58594
    assert candidate(low = "1111",high = "1111") == 1
    assert candidate(low = "1234567890",high = "12345678900") == 3000
    assert candidate(low = "1000000000000",high = "1000000000000") == 0
    assert candidate(low = "1111",high = "8888") == 13
    assert candidate(low = "18000000000000001",high = "68000000000000089") == 234376
    assert candidate(low = "696969696969",high = "969696969696") == 5209
    assert candidate(low = "111111111",high = "888888888") == 938
    assert candidate(low = "8888",high = "888888") == 136
    assert candidate(low = "110011",high = "111111") == 2
    assert candidate(low = "100000",high = "200000") == 25
    assert candidate(low = "200000000000000",high = "210000000000000") == 0
    assert candidate(low = "8000000000",high = "8999999999") == 625
    assert candidate(low = "8888888888",high = "8888888888") == 1
    assert candidate(low = "0",high = "1") == 2
    assert candidate(low = "100",high = "999") == 12
    assert candidate(low = "100000000000",high = "999999999999") == 12500
    assert candidate(low = "10000000000000001",high = "10000000000000009") == 1
    assert candidate(low = "9876543210",high = "10987654321") == 529
    assert candidate(low = "200000000",high = "200000000") == 0
    assert candidate(low = "690069",high = "690069") == 1


