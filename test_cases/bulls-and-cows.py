def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(secret = "1010101010",guess = "0101010101") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1010101010",guess = "0101010101") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234567890",guess = "1111111111") == "1A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234567890",guess = "1111111111") == "1A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "0000",guess = "1111") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "0000",guess = "1111") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "111222333",guess = "333222111") == "3A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "111222333",guess = "333222111") == "3A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9999999999",guess = "1111111111") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9999999999",guess = "1111111111") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1112",guess = "1122") == "3A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1112",guess = "1122") == "3A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9305",guess = "7315") == "2A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9305",guess = "7315") == "2A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1122",guess = "2211") == "0A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1122",guess = "2211") == "0A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234567890",guess = "0987654321") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234567890",guess = "0987654321") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1111",guess = "1111") == "4A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1111",guess = "1111") == "4A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "0000",guess = "0000") == "4A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "0000",guess = "0000") == "4A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "5678901234",guess = "1234567890") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "5678901234",guess = "1234567890") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234",guess = "4321") == "0A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234",guess = "4321") == "0A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "111222333",guess = "123123123") == "3A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "111222333",guess = "123123123") == "3A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234567890",guess = "9876543210") == "2A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234567890",guess = "9876543210") == "2A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1123",guess = "0111") == "1A1B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1123",guess = "0111") == "1A1B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1807",guess = "7810") == "1A3B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1807",guess = "7810") == "1A3B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "2222",guess = "1111") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "2222",guess = "1111") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "0000000000",guess = "0000000000") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "0000000000",guess = "0000000000") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234567890",guess = "1234567890") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234567890",guess = "1234567890") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "0000000000",guess = "1111111111") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "0000000000",guess = "1111111111") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "12345678901234567890",guess = "09876543210987654321") == "0A20B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "12345678901234567890",guess = "09876543210987654321") == "0A20B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1112223334",guess = "4332221110") == "3A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1112223334",guess = "4332221110") == "3A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9876543210",guess = "0123456789") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9876543210",guess = "0123456789") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "5555555555",guess = "5555555555") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "5555555555",guess = "5555555555") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1111111111",guess = "1212121212") == "5A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1111111111",guess = "1212121212") == "5A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "123123",guess = "321321") == "2A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "123123",guess = "321321") == "2A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "111222",guess = "222111") == "0A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "111222",guess = "222111") == "0A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "001122",guess = "221100") == "2A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "001122",guess = "221100") == "2A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "111122223333444455556666777788889999",guess = "999988887777666655554444333322221111") == "4A32B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "111122223333444455556666777788889999",guess = "999988887777666655554444333322221111") == "4A32B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234123412",guess = "1234123412") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234123412",guess = "1234123412") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1111111111111111",guess = "1111111111111111") == "16A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1111111111111111",guess = "1111111111111111") == "16A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "5656565656",guess = "6565656565") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "5656565656",guess = "6565656565") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "11223344",guess = "44332211") == "0A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "11223344",guess = "44332211") == "0A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "888888",guess = "888888") == "6A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "888888",guess = "888888") == "6A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "0123456789",guess = "9876543210") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "0123456789",guess = "9876543210") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1111222233334444",guess = "4444333322221111") == "0A16B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1111222233334444",guess = "4444333322221111") == "0A16B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "12345678901234567890",guess = "12345678900000000000") == "11A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "12345678901234567890",guess = "12345678900000000000") == "11A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "00000000",guess = "88888888") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "00000000",guess = "88888888") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "12345678900000000000",guess = "00000000001234567890") == "2A18B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "12345678900000000000",guess = "00000000001234567890") == "2A18B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1010101010",guess = "1010101010") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1010101010",guess = "1010101010") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "11223344556677889900",guess = "00998877665544332211") == "0A20B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "11223344556677889900",guess = "00998877665544332211") == "0A20B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "12345678901234567890",guess = "12345678901234567890") == "20A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "12345678901234567890",guess = "12345678901234567890") == "20A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "2234567890",guess = "0987654322") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "2234567890",guess = "0987654322") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1000000001",guess = "0111111110") == "0A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1000000001",guess = "0111111110") == "0A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9111111119",guess = "9111111119") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9111111119",guess = "9111111119") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "99887766554433221100",guess = "00112233445566778899") == "0A20B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "99887766554433221100",guess = "00112233445566778899") == "0A20B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1111111111",guess = "0000000001") == "1A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1111111111",guess = "0000000001") == "1A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1000100010",guess = "0111011101") == "0A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1000100010",guess = "0111011101") == "0A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "11112222333344445555",guess = "55554444333322221111") == "4A16B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "11112222333344445555",guess = "55554444333322221111") == "4A16B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1223344556",guess = "1122334455") == "5A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1223344556",guess = "1122334455") == "5A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1112223334",guess = "4332221119") == "3A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1112223334",guess = "4332221119") == "3A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "0011001100",guess = "1100110011") == "0A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "0011001100",guess = "1100110011") == "0A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9876543210",guess = "9876543210") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9876543210",guess = "9876543210") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "2222222222",guess = "2222222222") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "2222222222",guess = "2222222222") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "999988887777",guess = "888877776666") == "0A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "999988887777",guess = "888877776666") == "0A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "98765432109876543210",guess = "01234567890123456789") == "0A20B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "98765432109876543210",guess = "01234567890123456789") == "0A20B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1122334455",guess = "1122334455") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1122334455",guess = "1122334455") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234123412",guess = "2143214321") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234123412",guess = "2143214321") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "12341234",guess = "43214321") == "0A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "12341234",guess = "43214321") == "0A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "555555",guess = "555555") == "6A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "555555",guess = "555555") == "6A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1111111111",guess = "1111111111") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1111111111",guess = "1111111111") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1111111111",guess = "2222222222") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1111111111",guess = "2222222222") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1000000000",guess = "0111111111") == "0A2B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1000000000",guess = "0111111111") == "0A2B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1112223334",guess = "1111111111") == "3A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1112223334",guess = "1111111111") == "3A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "0123012301",guess = "1032103210") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "0123012301",guess = "1032103210") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9999999999",guess = "9999999999") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9999999999",guess = "9999999999") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9876543210",guess = "1234567890") == "2A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9876543210",guess = "1234567890") == "2A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1231231231",guess = "3123123123") == "0A9B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1231231231",guess = "3123123123") == "0A9B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "5638472910",guess = "1092748356") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "5638472910",guess = "1092748356") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1112223334",guess = "4333222111") == "2A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1112223334",guess = "4333222111") == "2A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "12345678901234567890",guess = "98765432109876543210") == "4A16B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "12345678901234567890",guess = "98765432109876543210") == "4A16B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1020304050",guess = "0102030405") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1020304050",guess = "0102030405") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "5678901234",guess = "5566778899") == "1A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "5678901234",guess = "5566778899") == "1A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "101010",guess = "010101") == "0A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "101010",guess = "010101") == "0A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1122334455",guess = "5544332211") == "2A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1122334455",guess = "5544332211") == "2A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234123412",guess = "2341234123") == "0A9B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234123412",guess = "2341234123") == "0A9B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "33331111",guess = "11113333") == "0A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "33331111",guess = "11113333") == "0A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "2222222222",guess = "1111111111") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "2222222222",guess = "1111111111") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1111111111",guess = "1010101010") == "5A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1111111111",guess = "1010101010") == "5A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "111222333444555666777888999000",guess = "000999888777666555444333222111") == "0A30B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "111222333444555666777888999000",guess = "000999888777666555444333222111") == "0A30B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "99998888777766665555",guess = "55554444333322221111") == "0A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "99998888777766665555",guess = "55554444333322221111") == "0A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "0000000000",guess = "9999999999") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "0000000000",guess = "9999999999") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1221122112",guess = "2112211221") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1221122112",guess = "2112211221") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "5678901234",guess = "0123456789") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "5678901234",guess = "0123456789") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "04730865",guess = "58600074") == "1A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "04730865",guess = "58600074") == "1A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1223344556",guess = "1223344556") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1223344556",guess = "1223344556") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234567890",guess = "5432109876") == "2A8B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234567890",guess = "5432109876") == "2A8B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "12345678901234567890",guess = "01234567890123456789") == "0A20B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "12345678901234567890",guess = "01234567890123456789") == "0A20B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "0000111122223333",guess = "3333222211110000") == "0A16B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "0000111122223333",guess = "3333222211110000") == "0A16B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234567890",guess = "0123456789") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234567890",guess = "0123456789") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "000000",guess = "000000") == "6A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "000000",guess = "000000") == "6A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "111122223333",guess = "111122223333") == "12A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "111122223333",guess = "111122223333") == "12A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "111122223333",guess = "333344445555") == "0A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "111122223333",guess = "333344445555") == "0A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "25432109876543210987654321",guess = "10987654321098765432125432") == "0A26B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "25432109876543210987654321",guess = "10987654321098765432125432") == "0A26B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9999999999",guess = "8888888888") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9999999999",guess = "8888888888") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "8888888888",guess = "8888888888") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "8888888888",guess = "8888888888") == "10A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "2457",guess = "5247") == "1A3B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "2457",guess = "5247") == "1A3B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "5608055740",guess = "5708055640") == "8A2B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "5608055740",guess = "5708055640") == "8A2B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234555555",guess = "5555555551") == "5A2B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234555555",guess = "5555555551") == "5A2B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1223344556",guess = "6554433221") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1223344556",guess = "6554433221") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "00112233445566778899",guess = "99887766554433221100") == "0A20B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "00112233445566778899",guess = "99887766554433221100") == "0A20B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1234123412",guess = "2345234523") == "0A7B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1234123412",guess = "2345234523") == "0A7B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "122112",guess = "211221") == "0A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "122112",guess = "211221") == "0A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "112233",guess = "332211") == "2A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "112233",guess = "332211") == "2A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1231231231",guess = "3213213213") == "3A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1231231231",guess = "3213213213") == "3A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1212121212",guess = "2121212121") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1212121212",guess = "2121212121") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "1221",guess = "1122") == "2A2B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "1221",guess = "1122") == "2A2B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "123456",guess = "654321") == "0A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "123456",guess = "654321") == "0A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "000111222",guess = "222111000") == "3A6B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "000111222",guess = "222111000") == "3A6B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "12213312",guess = "21123312") == "4A4B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "12213312",guess = "21123312") == "4A4B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "8888",guess = "8888") == "4A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "8888",guess = "8888") == "4A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "999999",guess = "123456") == "0A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "999999",guess = "123456") == "0A0B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9876543210",guess = "1098765432") == "0A10B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9876543210",guess = "1098765432") == "0A10B": {e}')
    
    total += 1
    try:
        result = candidate(secret = "9000000000",guess = "9000000000") == "10A0B"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(secret = "9000000000",guess = "9000000000") == "10A0B": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(secret = "1010101010",guess = "0101010101") == "0A10B"
    assert candidate(secret = "1234567890",guess = "1111111111") == "1A0B"
    assert candidate(secret = "0000",guess = "1111") == "0A0B"
    assert candidate(secret = "111222333",guess = "333222111") == "3A6B"
    assert candidate(secret = "9999999999",guess = "1111111111") == "0A0B"
    assert candidate(secret = "1112",guess = "1122") == "3A0B"
    assert candidate(secret = "9305",guess = "7315") == "2A0B"
    assert candidate(secret = "1122",guess = "2211") == "0A4B"
    assert candidate(secret = "1234567890",guess = "0987654321") == "0A10B"
    assert candidate(secret = "1111",guess = "1111") == "4A0B"
    assert candidate(secret = "0000",guess = "0000") == "4A0B"
    assert candidate(secret = "5678901234",guess = "1234567890") == "0A10B"
    assert candidate(secret = "1234",guess = "4321") == "0A4B"
    assert candidate(secret = "111222333",guess = "123123123") == "3A6B"
    assert candidate(secret = "1234567890",guess = "9876543210") == "2A8B"
    assert candidate(secret = "1123",guess = "0111") == "1A1B"
    assert candidate(secret = "1807",guess = "7810") == "1A3B"
    assert candidate(secret = "2222",guess = "1111") == "0A0B"
    assert candidate(secret = "0000000000",guess = "0000000000") == "10A0B"
    assert candidate(secret = "1234567890",guess = "1234567890") == "10A0B"
    assert candidate(secret = "0000000000",guess = "1111111111") == "0A0B"
    assert candidate(secret = "12345678901234567890",guess = "09876543210987654321") == "0A20B"
    assert candidate(secret = "1112223334",guess = "4332221110") == "3A6B"
    assert candidate(secret = "9876543210",guess = "0123456789") == "0A10B"
    assert candidate(secret = "5555555555",guess = "5555555555") == "10A0B"
    assert candidate(secret = "1111111111",guess = "1212121212") == "5A0B"
    assert candidate(secret = "123123",guess = "321321") == "2A4B"
    assert candidate(secret = "111222",guess = "222111") == "0A6B"
    assert candidate(secret = "001122",guess = "221100") == "2A4B"
    assert candidate(secret = "111122223333444455556666777788889999",guess = "999988887777666655554444333322221111") == "4A32B"
    assert candidate(secret = "1234123412",guess = "1234123412") == "10A0B"
    assert candidate(secret = "1111111111111111",guess = "1111111111111111") == "16A0B"
    assert candidate(secret = "5656565656",guess = "6565656565") == "0A10B"
    assert candidate(secret = "11223344",guess = "44332211") == "0A8B"
    assert candidate(secret = "888888",guess = "888888") == "6A0B"
    assert candidate(secret = "0123456789",guess = "9876543210") == "0A10B"
    assert candidate(secret = "1111222233334444",guess = "4444333322221111") == "0A16B"
    assert candidate(secret = "12345678901234567890",guess = "12345678900000000000") == "11A0B"
    assert candidate(secret = "00000000",guess = "88888888") == "0A0B"
    assert candidate(secret = "12345678900000000000",guess = "00000000001234567890") == "2A18B"
    assert candidate(secret = "1010101010",guess = "1010101010") == "10A0B"
    assert candidate(secret = "11223344556677889900",guess = "00998877665544332211") == "0A20B"
    assert candidate(secret = "12345678901234567890",guess = "12345678901234567890") == "20A0B"
    assert candidate(secret = "2234567890",guess = "0987654322") == "0A10B"
    assert candidate(secret = "1000000001",guess = "0111111110") == "0A4B"
    assert candidate(secret = "9111111119",guess = "9111111119") == "10A0B"
    assert candidate(secret = "99887766554433221100",guess = "00112233445566778899") == "0A20B"
    assert candidate(secret = "1111111111",guess = "0000000001") == "1A0B"
    assert candidate(secret = "1000100010",guess = "0111011101") == "0A6B"
    assert candidate(secret = "11112222333344445555",guess = "55554444333322221111") == "4A16B"
    assert candidate(secret = "1223344556",guess = "1122334455") == "5A4B"
    assert candidate(secret = "1112223334",guess = "4332221119") == "3A6B"
    assert candidate(secret = "0011001100",guess = "1100110011") == "0A8B"
    assert candidate(secret = "9876543210",guess = "9876543210") == "10A0B"
    assert candidate(secret = "2222222222",guess = "2222222222") == "10A0B"
    assert candidate(secret = "999988887777",guess = "888877776666") == "0A8B"
    assert candidate(secret = "98765432109876543210",guess = "01234567890123456789") == "0A20B"
    assert candidate(secret = "1122334455",guess = "1122334455") == "10A0B"
    assert candidate(secret = "1234123412",guess = "2143214321") == "0A10B"
    assert candidate(secret = "12341234",guess = "43214321") == "0A8B"
    assert candidate(secret = "555555",guess = "555555") == "6A0B"
    assert candidate(secret = "1111111111",guess = "1111111111") == "10A0B"
    assert candidate(secret = "1111111111",guess = "2222222222") == "0A0B"
    assert candidate(secret = "1000000000",guess = "0111111111") == "0A2B"
    assert candidate(secret = "1112223334",guess = "1111111111") == "3A0B"
    assert candidate(secret = "0123012301",guess = "1032103210") == "0A10B"
    assert candidate(secret = "9999999999",guess = "9999999999") == "10A0B"
    assert candidate(secret = "9876543210",guess = "1234567890") == "2A8B"
    assert candidate(secret = "1231231231",guess = "3123123123") == "0A9B"
    assert candidate(secret = "5638472910",guess = "1092748356") == "0A10B"
    assert candidate(secret = "1112223334",guess = "4333222111") == "2A8B"
    assert candidate(secret = "12345678901234567890",guess = "98765432109876543210") == "4A16B"
    assert candidate(secret = "1020304050",guess = "0102030405") == "0A10B"
    assert candidate(secret = "5678901234",guess = "5566778899") == "1A4B"
    assert candidate(secret = "101010",guess = "010101") == "0A6B"
    assert candidate(secret = "1122334455",guess = "5544332211") == "2A8B"
    assert candidate(secret = "1234123412",guess = "2341234123") == "0A9B"
    assert candidate(secret = "33331111",guess = "11113333") == "0A8B"
    assert candidate(secret = "2222222222",guess = "1111111111") == "0A0B"
    assert candidate(secret = "1111111111",guess = "1010101010") == "5A0B"
    assert candidate(secret = "111222333444555666777888999000",guess = "000999888777666555444333222111") == "0A30B"
    assert candidate(secret = "99998888777766665555",guess = "55554444333322221111") == "0A4B"
    assert candidate(secret = "0000000000",guess = "9999999999") == "0A0B"
    assert candidate(secret = "1221122112",guess = "2112211221") == "0A10B"
    assert candidate(secret = "5678901234",guess = "0123456789") == "0A10B"
    assert candidate(secret = "04730865",guess = "58600074") == "1A6B"
    assert candidate(secret = "1223344556",guess = "1223344556") == "10A0B"
    assert candidate(secret = "1234567890",guess = "5432109876") == "2A8B"
    assert candidate(secret = "12345678901234567890",guess = "01234567890123456789") == "0A20B"
    assert candidate(secret = "0000111122223333",guess = "3333222211110000") == "0A16B"
    assert candidate(secret = "1234567890",guess = "0123456789") == "0A10B"
    assert candidate(secret = "000000",guess = "000000") == "6A0B"
    assert candidate(secret = "111122223333",guess = "111122223333") == "12A0B"
    assert candidate(secret = "111122223333",guess = "333344445555") == "0A4B"
    assert candidate(secret = "25432109876543210987654321",guess = "10987654321098765432125432") == "0A26B"
    assert candidate(secret = "9999999999",guess = "8888888888") == "0A0B"
    assert candidate(secret = "8888888888",guess = "8888888888") == "10A0B"
    assert candidate(secret = "2457",guess = "5247") == "1A3B"
    assert candidate(secret = "5608055740",guess = "5708055640") == "8A2B"
    assert candidate(secret = "1234555555",guess = "5555555551") == "5A2B"
    assert candidate(secret = "1223344556",guess = "6554433221") == "0A10B"
    assert candidate(secret = "00112233445566778899",guess = "99887766554433221100") == "0A20B"
    assert candidate(secret = "1234123412",guess = "2345234523") == "0A7B"
    assert candidate(secret = "122112",guess = "211221") == "0A6B"
    assert candidate(secret = "112233",guess = "332211") == "2A4B"
    assert candidate(secret = "1231231231",guess = "3213213213") == "3A6B"
    assert candidate(secret = "1212121212",guess = "2121212121") == "0A10B"
    assert candidate(secret = "1221",guess = "1122") == "2A2B"
    assert candidate(secret = "123456",guess = "654321") == "0A6B"
    assert candidate(secret = "000111222",guess = "222111000") == "3A6B"
    assert candidate(secret = "12213312",guess = "21123312") == "4A4B"
    assert candidate(secret = "8888",guess = "8888") == "4A0B"
    assert candidate(secret = "999999",guess = "123456") == "0A0B"
    assert candidate(secret = "9876543210",guess = "1098765432") == "0A10B"
    assert candidate(secret = "9000000000",guess = "9000000000") == "10A0B"


