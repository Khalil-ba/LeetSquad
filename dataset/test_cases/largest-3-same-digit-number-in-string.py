def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = "999888777666555444333222111000") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999888777666555444333222111000") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "42352338") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "42352338") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "555444555") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "555444555") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "112233445566778899") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "112233445566778899") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "888777666555444333222111000") == "888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "888777666555444333222111000") == "888": {e}')
    
    total += 1
    try:
        result = candidate(num = "2300019") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2300019") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "10000001") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10000001") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "123") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "6777133339") == "777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "6777133339") == "777": {e}')
    
    total += 1
    try:
        result = candidate(num = "1222333444555666777888999000") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1222333444555666777888999000") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "888777666555444333222111") == "888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "888777666555444333222111") == "888": {e}')
    
    total += 1
    try:
        result = candidate(num = "333333333") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "333333333") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "999999999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999999999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "999999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "11223344556677889900") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "11223344556677889900") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "9999999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9999999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "000111222333444555666777888999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000111222333444555666777888999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "888888888888888888888") == "888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "888888888888888888888") == "888": {e}')
    
    total += 1
    try:
        result = candidate(num = "100100100") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100100100") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "000000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "111111111") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111111111") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "111") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "123123123123123123123123123123123123") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123123123123123123123123123123123123") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234444321111234444321") == "444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234444321111234444321") == "444": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345678987654321000000123456789") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345678987654321000000123456789") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "555444333222111000000000000111222333444") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "555444333222111000000000000111222333444") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789123456789123456789123456789123456789") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789123456789123456789123456789123456789") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "1233344445555566666777777") == "777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1233344445555566666777777") == "777": {e}')
    
    total += 1
    try:
        result = candidate(num = "555444333222111000000111222333444555") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "555444333222111000000111222333444555") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "1222222222222222222222222222221") == "222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1222222222222222222222222222221") == "222": {e}')
    
    total += 1
    try:
        result = candidate(num = "555444333222111000999888777666555") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "555444333222111000999888777666555") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "10000001000000100000010000001000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10000001000000100000010000001000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "987654321111111111111111111111987654321000000000") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "987654321111111111111111111111987654321000000000") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "88888888888888888888888888888888888888888888") == "888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "88888888888888888888888888888888888888888888") == "888": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890123456789012345678901234567890") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890123456789012345678901234567890") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345678987654321012345678987654321") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345678987654321012345678987654321") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "999000111222333444555666777888999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999000111222333444555666777888999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "000123456789") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000123456789") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "111111222222333333444444555555666666777777888888999999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111111222222333333444444555555666666777777888888999999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1111111111111111111111111111111111111111111111111") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111111111111111111111111111111111111111111111111") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "123123123123123123123123") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123123123123123123123123") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "123123123123123123123123123123") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123123123123123123123123123123") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000000000000000000000000000000000000000000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000000000000000000000000000000000000000000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "01234567890123456789012345678901234567890") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "01234567890123456789012345678901234567890") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "999999999999999999999999999999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999999999999999999999999999999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "987654321111111111111111111111987654321") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "987654321111111111111111111111987654321") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333444555666777888999000111222333444555666777888999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333444555666777888999000111222333444555666777888999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1221221221221221221221221") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1221221221221221221221221") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "000000000000000000000000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000000000000000000000000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "123123123123123123123123123") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123123123123123123123123123") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "55555555555555555555555555555555555555555555555555555555") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "55555555555555555555555555555555555555555555555555555555") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "123333456789000123456789") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123333456789000123456789") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "00000000000000000000000000000000000000000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00000000000000000000000000000000000000000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "99999999999999999999999999999999999999999999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "99999999999999999999999999999999999999999999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "333333333333333333333333333333") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "333333333333333333333333333333") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "9990000000000000000000000000000000000000000000000000000000") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9990000000000000000000000000000000000000000000000000000000") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1122334455667788990011223344556677889900") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1122334455667788990011223344556677889900") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "33333333333333333333333333333333333333333333") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "33333333333333333333333333333333333333333333") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "987654321000000000987654321") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "987654321000000000987654321") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "122333444555666777888999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "122333444555666777888999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "888999777666555444333222111000") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "888999777666555444333222111000") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333444555666777888999000") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333444555666777888999000") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "123332111112222233333") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123332111112222233333") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "98765432109876543210987654321") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "98765432109876543210987654321") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "000000000000000000000000000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000000000000000000000000000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "11111111111111111111111111111111111111111111") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "11111111111111111111111111111111111111111111") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "98765432111111111111111111111111111111111111") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "98765432111111111111111111111111111111111111") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "999111222333444555666777888") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999111222333444555666777888") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "123332111222222111111") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123332111222222111111") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333444555666777888999111222333444555") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333444555666777888999111222333444555") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "10101010101010101010101010101010101010101010") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10101010101010101010101010101010101010101010") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345678987654321111100000000222222333333") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345678987654321111100000000222222333333") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000000000000000000000000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000000000000000000000000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333444555666777888999000111222") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333444555666777888999000111222") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "98765432111123456789000000") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "98765432111123456789000000") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "999000999000999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999000999000999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000000000000000000000000000000000000000000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000000000000000000000000000000000000000000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "000000111111222222333333444444555555666666777777888888999999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000000111111222222333333444444555555666666777777888888999999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333444555666777888999111") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333444555666777888999111") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "987654321098765432109876543210") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "987654321098765432109876543210") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "888999888999888999888999888999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "888999888999888999888999888999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "111000111000111000111000") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111000111000111000111000") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234555554321") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234555554321") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789123456789123456789") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789123456789123456789") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "111000111000111000111000111000") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111000111000111000111000111000") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "111000222333444555666777888999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111000222333444555666777888999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "333222111333222111333222111") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "333222111333222111333222111") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "101010101010101010101010101") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "101010101010101010101010101") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "1111111111111111111111111111111") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111111111111111111111111111111") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345678999987654321") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345678999987654321") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "111122223333444455556666777788889999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111122223333444455556666777788889999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789000000987654321") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789000000987654321") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "999888777666555444333222111") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999888777666555444333222111") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "555555555555555555555555555555555555555555555555") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "555555555555555555555555555555555555555555555555") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333444555666777888999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333444555666777888999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "999888777666555444333222111000999888777") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999888777666555444333222111000999888777") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "111000111222333") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111000111222333") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789876543211222333444555666777888999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789876543211222333444555666777888999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789876543211111111111111") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789876543211111111111111") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "9999999999999999999999999999999999999999999999999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9999999999999999999999999999999999999999999999999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789000000000000000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789000000000000000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "987654321000000123456789") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "987654321000000123456789") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "111999888777666555444333222111") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111999888777666555444333222111") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "5555555555555555555555555555555") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5555555555555555555555555555555") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "333222111000999888777666555444333222111000") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "333222111000999888777666555444333222111000") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1233321111222223333") == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1233321111222223333") == "333": {e}')
    
    total += 1
    try:
        result = candidate(num = "0011223344556677889900112233445566") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0011223344556677889900112233445566") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789012345678901234567890") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789012345678901234567890") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "000111222333444555666777888999000111222333") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000111222333444555666777888999000111222333") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1111122223333444455556666777788889999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111122223333444455556666777788889999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "5555555555555555555555555") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5555555555555555555555555") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333444555666777888999000111") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333444555666777888999000111") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "999000999000999000999000999000999000") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999000999000999000999000999000999000") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890000000000000000000000000000000") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890000000000000000000000000000000") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789123456789123456789123456789") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789123456789123456789123456789") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "11111111111111111111111111111100000000000000000") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "11111111111111111111111111111100000000000000000") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "555555444444333333222222111111") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "555555444444333333222222111111") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "333222111000777888999") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "333222111000777888999") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "555555555555555555555555555555") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "555555555555555555555555555555") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "1222233333444444555555566666667") == "666"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1222233333444444555555566666667") == "666": {e}')
    
    total += 1
    try:
        result = candidate(num = "123123123123123123123123123123123123123123123123123123123123") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123123123123123123123123123123123123123123123123123123123123") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789999987654321") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789999987654321") == "999": {e}')
    
    total += 1
    try:
        result = candidate(num = "990990990990990990") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "990990990990990990") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "123455567890123456789012345678") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123455567890123456789012345678") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "111111111111111111111111111111") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111111111111111111111111111111") == "111": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345556789000987654321000000") == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345556789000987654321000000") == "555": {e}')
    
    total += 1
    try:
        result = candidate(num = "22222222222222222222222222222222222222222222") == "222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "22222222222222222222222222222222222222222222") == "222": {e}')
    
    total += 1
    try:
        result = candidate(num = "10000000000000000000000000000001") == "000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10000000000000000000000000000001") == "000": {e}')
    
    total += 1
    try:
        result = candidate(num = "000111000111000111000111000111") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000111000111000111000111000111") == "111": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = "999888777666555444333222111000") == "999"
    assert candidate(num = "000") == "000"
    assert candidate(num = "42352338") == ""
    assert candidate(num = "9876543210") == ""
    assert candidate(num = "555444555") == "555"
    assert candidate(num = "112233445566778899") == ""
    assert candidate(num = "888777666555444333222111000") == "888"
    assert candidate(num = "2300019") == "000"
    assert candidate(num = "10000001") == "000"
    assert candidate(num = "123") == ""
    assert candidate(num = "6777133339") == "777"
    assert candidate(num = "1222333444555666777888999000") == "999"
    assert candidate(num = "888777666555444333222111") == "888"
    assert candidate(num = "333333333") == "333"
    assert candidate(num = "999999999") == "999"
    assert candidate(num = "999999") == "999"
    assert candidate(num = "11223344556677889900") == ""
    assert candidate(num = "9999999") == "999"
    assert candidate(num = "1234567890") == ""
    assert candidate(num = "000111222333444555666777888999") == "999"
    assert candidate(num = "111222333") == "333"
    assert candidate(num = "888888888888888888888") == "888"
    assert candidate(num = "100100100") == ""
    assert candidate(num = "000000000") == "000"
    assert candidate(num = "111111111") == "111"
    assert candidate(num = "111") == "111"
    assert candidate(num = "123123123123123123123123123123123123") == ""
    assert candidate(num = "1234444321111234444321") == "444"
    assert candidate(num = "12345678987654321000000123456789") == "000"
    assert candidate(num = "555444333222111000000000000111222333444") == "555"
    assert candidate(num = "123456789123456789123456789123456789123456789") == ""
    assert candidate(num = "1233344445555566666777777") == "777"
    assert candidate(num = "555444333222111000000111222333444555") == "555"
    assert candidate(num = "1222222222222222222222222222221") == "222"
    assert candidate(num = "555444333222111000999888777666555") == "999"
    assert candidate(num = "10000001000000100000010000001000000") == "000"
    assert candidate(num = "987654321111111111111111111111987654321000000000") == "111"
    assert candidate(num = "88888888888888888888888888888888888888888888") == "888"
    assert candidate(num = "1234567890123456789012345678901234567890") == ""
    assert candidate(num = "12345678987654321012345678987654321") == ""
    assert candidate(num = "999000111222333444555666777888999") == "999"
    assert candidate(num = "000123456789") == "000"
    assert candidate(num = "111111222222333333444444555555666666777777888888999999") == "999"
    assert candidate(num = "1111111111111111111111111111111111111111111111111") == "111"
    assert candidate(num = "123123123123123123123123") == ""
    assert candidate(num = "123123123123123123123123123123") == ""
    assert candidate(num = "1000000000000000000000000000000000000000000000000") == "000"
    assert candidate(num = "01234567890123456789012345678901234567890") == ""
    assert candidate(num = "999999999999999999999999999999") == "999"
    assert candidate(num = "987654321111111111111111111111987654321") == "111"
    assert candidate(num = "111222333444555666777888999000111222333444555666777888999") == "999"
    assert candidate(num = "1221221221221221221221221") == ""
    assert candidate(num = "000000000000000000000000000") == "000"
    assert candidate(num = "123123123123123123123123123") == ""
    assert candidate(num = "55555555555555555555555555555555555555555555555555555555") == "555"
    assert candidate(num = "123333456789000123456789") == "333"
    assert candidate(num = "00000000000000000000000000000000000000000000") == "000"
    assert candidate(num = "99999999999999999999999999999999999999999999") == "999"
    assert candidate(num = "333333333333333333333333333333") == "333"
    assert candidate(num = "9990000000000000000000000000000000000000000000000000000000") == "999"
    assert candidate(num = "1122334455667788990011223344556677889900") == ""
    assert candidate(num = "33333333333333333333333333333333333333333333") == "333"
    assert candidate(num = "987654321000000000987654321") == "000"
    assert candidate(num = "122333444555666777888999") == "999"
    assert candidate(num = "888999777666555444333222111000") == "999"
    assert candidate(num = "111222333444555666777888999000") == "999"
    assert candidate(num = "123332111112222233333") == "333"
    assert candidate(num = "98765432109876543210987654321") == ""
    assert candidate(num = "000000000000000000000000000000") == "000"
    assert candidate(num = "11111111111111111111111111111111111111111111") == "111"
    assert candidate(num = "98765432111111111111111111111111111111111111") == "111"
    assert candidate(num = "999111222333444555666777888") == "999"
    assert candidate(num = "123332111222222111111") == "333"
    assert candidate(num = "111222333444555666777888999111222333444555") == "999"
    assert candidate(num = "10101010101010101010101010101010101010101010") == ""
    assert candidate(num = "12345678987654321111100000000222222333333") == "333"
    assert candidate(num = "1000000000000000000000000000000") == "000"
    assert candidate(num = "111222333444555666777888999000111222") == "999"
    assert candidate(num = "98765432111123456789000000") == "111"
    assert candidate(num = "999000999000999") == "999"
    assert candidate(num = "0000000000000000000000000000000000000000000000000") == "000"
    assert candidate(num = "000000111111222222333333444444555555666666777777888888999999") == "999"
    assert candidate(num = "111222333444555666777888999111") == "999"
    assert candidate(num = "987654321098765432109876543210") == ""
    assert candidate(num = "888999888999888999888999888999") == "999"
    assert candidate(num = "111000111000111000111000") == "111"
    assert candidate(num = "1234555554321") == "555"
    assert candidate(num = "123456789123456789123456789") == ""
    assert candidate(num = "111000111000111000111000111000") == "111"
    assert candidate(num = "111000222333444555666777888999") == "999"
    assert candidate(num = "333222111333222111333222111") == "333"
    assert candidate(num = "101010101010101010101010101") == ""
    assert candidate(num = "1111111111111111111111111111111") == "111"
    assert candidate(num = "12345678999987654321") == "999"
    assert candidate(num = "111122223333444455556666777788889999") == "999"
    assert candidate(num = "123456789000000987654321") == "000"
    assert candidate(num = "999888777666555444333222111") == "999"
    assert candidate(num = "555555555555555555555555555555555555555555555555") == "555"
    assert candidate(num = "111222333444555666777888999") == "999"
    assert candidate(num = "999888777666555444333222111000999888777") == "999"
    assert candidate(num = "111000111222333") == "333"
    assert candidate(num = "123456789876543211222333444555666777888999") == "999"
    assert candidate(num = "123456789876543211111111111111") == "111"
    assert candidate(num = "9999999999999999999999999999999999999999999999999") == "999"
    assert candidate(num = "123456789000000000000000000") == "000"
    assert candidate(num = "987654321000000123456789") == "000"
    assert candidate(num = "111999888777666555444333222111") == "999"
    assert candidate(num = "5555555555555555555555555555555") == "555"
    assert candidate(num = "333222111000999888777666555444333222111000") == "999"
    assert candidate(num = "1233321111222223333") == "333"
    assert candidate(num = "0011223344556677889900112233445566") == ""
    assert candidate(num = "123456789012345678901234567890") == ""
    assert candidate(num = "000111222333444555666777888999000111222333") == "999"
    assert candidate(num = "1111122223333444455556666777788889999") == "999"
    assert candidate(num = "5555555555555555555555555") == "555"
    assert candidate(num = "111222333444555666777888999000111") == "999"
    assert candidate(num = "999000999000999000999000999000999000") == "999"
    assert candidate(num = "1234567890000000000000000000000000000000") == "000"
    assert candidate(num = "123456789123456789123456789123456789") == ""
    assert candidate(num = "11111111111111111111111111111100000000000000000") == "111"
    assert candidate(num = "555555444444333333222222111111") == "555"
    assert candidate(num = "333222111000777888999") == "999"
    assert candidate(num = "555555555555555555555555555555") == "555"
    assert candidate(num = "1222233333444444555555566666667") == "666"
    assert candidate(num = "123123123123123123123123123123123123123123123123123123123123") == ""
    assert candidate(num = "123456789999987654321") == "999"
    assert candidate(num = "990990990990990990") == ""
    assert candidate(num = "123455567890123456789012345678") == "555"
    assert candidate(num = "111111111111111111111111111111") == "111"
    assert candidate(num = "12345556789000987654321000000") == "555"
    assert candidate(num = "22222222222222222222222222222222222222222222") == "222"
    assert candidate(num = "10000000000000000000000000000001") == "000"
    assert candidate(num = "000111000111000111000111000111") == "111"


