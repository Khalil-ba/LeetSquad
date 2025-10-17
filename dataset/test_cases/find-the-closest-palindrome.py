def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = "10") == "9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10") == "9": {e}')
    
    total += 1
    try:
        result = candidate(n = "1001") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1001") == "999": {e}')
    
    total += 1
    try:
        result = candidate(n = "1234") == "1221"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234") == "1221": {e}')
    
    total += 1
    try:
        result = candidate(n = "123321") == "122221"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123321") == "122221": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999") == "1000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999") == "1000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "11") == "9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11") == "9": {e}')
    
    total += 1
    try:
        result = candidate(n = "9999") == "10001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9999") == "10001": {e}')
    
    total += 1
    try:
        result = candidate(n = "111111111") == "111101111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111111111") == "111101111": {e}')
    
    total += 1
    try:
        result = candidate(n = "9") == "8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9") == "8": {e}')
    
    total += 1
    try:
        result = candidate(n = "111111111111111111") == "111111110011111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111111111111111111") == "111111110011111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "10001") == "9999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10001") == "9999": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000") == "999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000") == "999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "233") == "232"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "233") == "232": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321") == "987656789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321") == "987656789": {e}')
    
    total += 1
    try:
        result = candidate(n = "1221") == "1111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1221") == "1111": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789") == "123454321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789") == "123454321": {e}')
    
    total += 1
    try:
        result = candidate(n = "101") == "99"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "101") == "99": {e}')
    
    total += 1
    try:
        result = candidate(n = "1") == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1") == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = "10000") == "9999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000") == "9999": {e}')
    
    total += 1
    try:
        result = candidate(n = "123454321") == "123444321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123454321") == "123444321": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000001") == "999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000001") == "999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "12321") == "12221"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12321") == "12221": {e}')
    
    total += 1
    try:
        result = candidate(n = "99") == "101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "99") == "101": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999999999999") == "1000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999999999999") == "1000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000") == "999": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000001") == "999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000001") == "999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "123") == "121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123") == "121": {e}')
    
    total += 1
    try:
        result = candidate(n = "1234321") == "1233321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234321") == "1233321": {e}')
    
    total += 1
    try:
        result = candidate(n = "999") == "1001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999") == "1001": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456") == "123321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456") == "123321": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000000000000") == "999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000000000000") == "999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "100") == "99"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100") == "99": {e}')
    
    total += 1
    try:
        result = candidate(n = "9223372036854775807") == "9223372037302733229"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9223372036854775807") == "9223372037302733229": {e}')
    
    total += 1
    try:
        result = candidate(n = "923429") == "923329"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "923429") == "923329": {e}')
    
    total += 1
    try:
        result = candidate(n = "1234567887654321") == "1234567777654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234567887654321") == "1234567777654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "2345678987654321") == "2345678998765432"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2345678987654321") == "2345678998765432": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000000000000000000001") == "999999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000000000000000000001") == "999999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789876543210") == "123456789987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789876543210") == "123456789987654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000000000000100") == "10000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000000000000100") == "10000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "99999999999999999999") == "100000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "99999999999999999999") == "100000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "9999999999") == "10000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9999999999") == "10000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000000") == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000000") == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "2000002") == "1999991"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2000002") == "1999991": {e}')
    
    total += 1
    try:
        result = candidate(n = "100001") == "99999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100001") == "99999": {e}')
    
    total += 1
    try:
        result = candidate(n = "101010101010101010") == "101010101101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "101010101010101010") == "101010101101010101": {e}')
    
    total += 1
    try:
        result = candidate(n = "112233445566778899") == "112233445544332211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "112233445566778899") == "112233445544332211": {e}')
    
    total += 1
    try:
        result = candidate(n = "200000000000000000001") == "200000000000000000002"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "200000000000000000001") == "200000000000000000002": {e}')
    
    total += 1
    try:
        result = candidate(n = "12345678987654322") == "12345678987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12345678987654322") == "12345678987654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "888888888") == "888878888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "888888888") == "888878888": {e}')
    
    total += 1
    try:
        result = candidate(n = "221122") == "220022"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "221122") == "220022": {e}')
    
    total += 1
    try:
        result = candidate(n = "222222222222222222") == "222222221122222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "222222222222222222") == "222222221122222222": {e}')
    
    total += 1
    try:
        result = candidate(n = "99999999999999999999999999") == "100000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "99999999999999999999999999") == "100000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "1234567890123456789") == "1234567889887654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234567890123456789") == "1234567889887654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "98765432123456789") == "98765432023456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "98765432123456789") == "98765432023456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000000000000000") == "9999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000000000000000") == "9999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789876543221") == "123456789987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789876543221") == "123456789987654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "5555555555555555") == "5555555445555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "5555555555555555") == "5555555445555555": {e}')
    
    total += 1
    try:
        result = candidate(n = "1111111111") == "1111001111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1111111111") == "1111001111": {e}')
    
    total += 1
    try:
        result = candidate(n = "12345678987654321") == "12345678887654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12345678987654321") == "12345678887654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000000000000000001") == "9999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000000000000000001") == "9999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "1111") == "1001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1111") == "1001": {e}')
    
    total += 1
    try:
        result = candidate(n = "111") == "101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111") == "101": {e}')
    
    total += 1
    try:
        result = candidate(n = "9998") == "9999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9998") == "9999": {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000001") == "99999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000001") == "99999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "8888888888") == "8888778888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "8888888888") == "8888778888": {e}')
    
    total += 1
    try:
        result = candidate(n = "11111111111111111") == "11111111011111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11111111111111111") == "11111111011111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "888888888888888888") == "888888887788888888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "888888888888888888") == "888888887788888888": {e}')
    
    total += 1
    try:
        result = candidate(n = "135797531") == "135787531"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "135797531") == "135787531": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789012345678901234567890123456789") == "123456789012345678898876543210987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789012345678901234567890123456789") == "123456789012345678898876543210987654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "9876543210123456789") == "9876543211123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9876543210123456789") == "9876543211123456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "11122111") == "11111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11122111") == "11111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000000000000000000001") == "99999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000000000000000000001") == "99999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "100010001") == "100000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100010001") == "100000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000000000000000000000000") == "999999999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000000000000000000000000") == "999999999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "12344321") == "12333321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12344321") == "12333321": {e}')
    
    total += 1
    try:
        result = candidate(n = "12345678900987654321") == "12345678899887654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12345678900987654321") == "12345678899887654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "2147483647") == "2147447412"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2147483647") == "2147447412": {e}')
    
    total += 1
    try:
        result = candidate(n = "1800000000") == "1799999971"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1800000000") == "1799999971": {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000000000000") == "99999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000000000000") == "99999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "9999999999999999999999999") == "10000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9999999999999999999999999") == "10000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "9999999999999999999") == "10000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9999999999999999999") == "10000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "9876543210") == "9876556789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9876543210") == "9876556789": {e}')
    
    total += 1
    try:
        result = candidate(n = "99999") == "100001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "99999") == "100001": {e}')
    
    total += 1
    try:
        result = candidate(n = "1111111111111111111") == "1111111110111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1111111111111111111") == "1111111110111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321098765432109876543210987654321") == "987654321098765432111234567890123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321098765432109876543210987654321") == "987654321098765432111234567890123456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "112233445544332211") == "112233444444332211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "112233445544332211") == "112233444444332211": {e}')
    
    total += 1
    try:
        result = candidate(n = "9999999999999999") == "10000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9999999999999999") == "10000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "9999999999999999999999") == "10000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9999999999999999999999") == "10000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000001") == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000001") == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999999999999999") == "1000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999999999999999") == "1000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999999999998") == "999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999999999998") == "999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000000000000000000") == "999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000000000000000000") == "999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000000000000001") == "99999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000000000000001") == "99999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "2000000000000000000") == "2000000000000000002"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2000000000000000000") == "2000000000000000002": {e}')
    
    total += 1
    try:
        result = candidate(n = "1234567898765432") == "1234567887654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234567898765432") == "1234567887654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000000000000000000000000000000000001") == "99999999999999999999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000000000000000000000000000000000001") == "99999999999999999999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000000000000001") == "999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000000000000001") == "999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "11111111111111111111") == "11111111100111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11111111111111111111") == "11111111100111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999999999999999999") == "1000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999999999999999999") == "1000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321123456789") == "987654320023456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321123456789") == "987654320023456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "876543210") == "876545678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "876543210") == "876545678": {e}')
    
    total += 1
    try:
        result = candidate(n = "1234567890987654321") == "1234567891987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234567890987654321") == "1234567891987654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "1001001001001") == "1001000001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1001001001001") == "1001000001001": {e}')
    
    total += 1
    try:
        result = candidate(n = "99999999999999999") == "100000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "99999999999999999") == "100000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "98765432109876543210") == "98765432111123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "98765432109876543210") == "98765432111123456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "111111111111111110") == "111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111111111111111110") == "111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "92345678987654322") == "92345678987654329"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "92345678987654322") == "92345678987654329": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000000000001") == "999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000000000001") == "999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "111111111111111111111") == "111111111101111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111111111111111111111") == "111111111101111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "8000000000000000000") == "7999999999999999997"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "8000000000000000000") == "7999999999999999997": {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000000000001") == "99999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000000000001") == "99999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000000000000") == "9999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000000000000") == "9999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000000000000001") == "9999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000000000000001") == "9999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "246808642") == "246818642"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "246808642") == "246818642": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = "10") == "9"
    assert candidate(n = "1001") == "999"
    assert candidate(n = "1234") == "1221"
    assert candidate(n = "123321") == "122221"
    assert candidate(n = "999999999") == "1000000001"
    assert candidate(n = "11") == "9"
    assert candidate(n = "9999") == "10001"
    assert candidate(n = "111111111") == "111101111"
    assert candidate(n = "9") == "8"
    assert candidate(n = "111111111111111111") == "111111110011111111"
    assert candidate(n = "10001") == "9999"
    assert candidate(n = "1000000000") == "999999999"
    assert candidate(n = "233") == "232"
    assert candidate(n = "987654321") == "987656789"
    assert candidate(n = "1221") == "1111"
    assert candidate(n = "123456789") == "123454321"
    assert candidate(n = "101") == "99"
    assert candidate(n = "1") == "0"
    assert candidate(n = "10000") == "9999"
    assert candidate(n = "123454321") == "123444321"
    assert candidate(n = "1000000001") == "999999999"
    assert candidate(n = "12321") == "12221"
    assert candidate(n = "99") == "101"
    assert candidate(n = "999999999999999999") == "1000000000000000001"
    assert candidate(n = "1000") == "999"
    assert candidate(n = "1000001") == "999999"
    assert candidate(n = "123") == "121"
    assert candidate(n = "1234321") == "1233321"
    assert candidate(n = "999") == "1001"
    assert candidate(n = "123456") == "123321"
    assert candidate(n = "1000000000000000000") == "999999999999999999"
    assert candidate(n = "100") == "99"
    assert candidate(n = "9223372036854775807") == "9223372037302733229"
    assert candidate(n = "923429") == "923329"
    assert candidate(n = "1234567887654321") == "1234567777654321"
    assert candidate(n = "2345678987654321") == "2345678998765432"
    assert candidate(n = "1000000000000000000000000001") == "999999999999999999999999999"
    assert candidate(n = "123456789876543210") == "123456789987654321"
    assert candidate(n = "10000000000000000100") == "10000000000000000001"
    assert candidate(n = "99999999999999999999") == "100000000000000000001"
    assert candidate(n = "9999999999") == "10000000001"
    assert candidate(n = "10000000000") == "9999999999"
    assert candidate(n = "2000002") == "1999991"
    assert candidate(n = "100001") == "99999"
    assert candidate(n = "101010101010101010") == "101010101101010101"
    assert candidate(n = "112233445566778899") == "112233445544332211"
    assert candidate(n = "200000000000000000001") == "200000000000000000002"
    assert candidate(n = "12345678987654322") == "12345678987654321"
    assert candidate(n = "888888888") == "888878888"
    assert candidate(n = "221122") == "220022"
    assert candidate(n = "222222222222222222") == "222222221122222222"
    assert candidate(n = "99999999999999999999999999") == "100000000000000000000000001"
    assert candidate(n = "1234567890123456789") == "1234567889887654321"
    assert candidate(n = "98765432123456789") == "98765432023456789"
    assert candidate(n = "10000000000000000000") == "9999999999999999999"
    assert candidate(n = "123456789876543221") == "123456789987654321"
    assert candidate(n = "5555555555555555") == "5555555445555555"
    assert candidate(n = "1111111111") == "1111001111"
    assert candidate(n = "12345678987654321") == "12345678887654321"
    assert candidate(n = "10000000000000000000001") == "9999999999999999999999"
    assert candidate(n = "1111") == "1001"
    assert candidate(n = "111") == "101"
    assert candidate(n = "9998") == "9999"
    assert candidate(n = "100000000001") == "99999999999"
    assert candidate(n = "8888888888") == "8888778888"
    assert candidate(n = "11111111111111111") == "11111111011111111"
    assert candidate(n = "888888888888888888") == "888888887788888888"
    assert candidate(n = "135797531") == "135787531"
    assert candidate(n = "123456789012345678901234567890123456789") == "123456789012345678898876543210987654321"
    assert candidate(n = "9876543210123456789") == "9876543211123456789"
    assert candidate(n = "11122111") == "11111111"
    assert candidate(n = "100000000000000000000000001") == "99999999999999999999999999"
    assert candidate(n = "100010001") == "100000001"
    assert candidate(n = "1000000000000000000000000000000") == "999999999999999999999999999999"
    assert candidate(n = "12344321") == "12333321"
    assert candidate(n = "12345678900987654321") == "12345678899887654321"
    assert candidate(n = "2147483647") == "2147447412"
    assert candidate(n = "1800000000") == "1799999971"
    assert candidate(n = "100000000000000000") == "99999999999999999"
    assert candidate(n = "9999999999999999999999999") == "10000000000000000000000001"
    assert candidate(n = "9999999999999999999") == "10000000000000000001"
    assert candidate(n = "9876543210") == "9876556789"
    assert candidate(n = "99999") == "100001"
    assert candidate(n = "1111111111111111111") == "1111111110111111111"
    assert candidate(n = "987654321098765432109876543210987654321") == "987654321098765432111234567890123456789"
    assert candidate(n = "112233445544332211") == "112233444444332211"
    assert candidate(n = "9999999999999999") == "10000000000000001"
    assert candidate(n = "9999999999999999999999") == "10000000000000000000001"
    assert candidate(n = "10000000001") == "9999999999"
    assert candidate(n = "999999999999999999999") == "1000000000000000000001"
    assert candidate(n = "999999999999999998") == "999999999999999999"
    assert candidate(n = "1000000000000000000000000") == "999999999999999999999999"
    assert candidate(n = "100000000000000000001") == "99999999999999999999"
    assert candidate(n = "2000000000000000000") == "2000000000000000002"
    assert candidate(n = "1234567898765432") == "1234567887654321"
    assert candidate(n = "100000000000000000000000000000000000000001") == "99999999999999999999999999999999999999999"
    assert candidate(n = "1000000000000000000001") == "999999999999999999999"
    assert candidate(n = "11111111111111111111") == "11111111100111111111"
    assert candidate(n = "999999999999999999999999") == "1000000000000000000000001"
    assert candidate(n = "987654321123456789") == "987654320023456789"
    assert candidate(n = "876543210") == "876545678"
    assert candidate(n = "1234567890987654321") == "1234567891987654321"
    assert candidate(n = "1001001001001") == "1001000001001"
    assert candidate(n = "99999999999999999") == "100000000000000001"
    assert candidate(n = "98765432109876543210") == "98765432111123456789"
    assert candidate(n = "111111111111111110") == "111111111111111111"
    assert candidate(n = "92345678987654322") == "92345678987654329"
    assert candidate(n = "1000000000000000001") == "999999999999999999"
    assert candidate(n = "111111111111111111111") == "111111111101111111111"
    assert candidate(n = "8000000000000000000") == "7999999999999999997"
    assert candidate(n = "100000000000000001") == "99999999999999999"
    assert candidate(n = "10000000000000000") == "9999999999999999"
    assert candidate(n = "10000000000000000001") == "9999999999999999999"
    assert candidate(n = "246808642") == "246818642"


