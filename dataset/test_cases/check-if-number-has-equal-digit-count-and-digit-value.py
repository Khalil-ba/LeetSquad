def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = "1111") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "10") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1111111111") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111111111") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "6200000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "6200000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0100100010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0100100010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "6210001000") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "6210001000") == True: {e}')
    
    total += 1
    try:
        result = candidate(num = "030") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "030") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "2020202020") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2020202020") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "5000000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5000000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "21200") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "21200") == True: {e}')
    
    total += 1
    try:
        result = candidate(num = "0987654321") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0987654321") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "2020") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2020") == True: {e}')
    
    total += 1
    try:
        result = candidate(num = "11200") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "11200") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1010101010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1010101010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1210") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1210") == True: {e}')
    
    total += 1
    try:
        result = candidate(num = "6543210") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "6543210") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "50000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "50000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "5000001000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5000001000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1221111111") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1221111111") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "2120000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2120000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "4000400040") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4000400040") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "101010101") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "101010101") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000100000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000100000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1112212100") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1112212100") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "400000000004") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "400000000004") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000100") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000100") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0101010101") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0101010101") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00100000010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00100000010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00000000400") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00000000400") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "9000000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9000000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3110001000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3110001000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0100101010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0100101010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "100010000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100010000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "000020000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000020000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "100201000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100201000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "30003") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "30003") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1221") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1221") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "12101000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12101000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "000010001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000010001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3000000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3000000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0010000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0010000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000101000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000101000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3100000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3100000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3000000010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3000000010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0100000001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0100000001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00001001000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00001001000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "121010000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "121010000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0123400000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0123400000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "2010000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2010000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0010000010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0010000010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "102020100") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "102020100") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "000300003") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000300003") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "500000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "500000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "40000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "40000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "5000011000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5000011000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1001001001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1001001001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1221100000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1221100000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1212121212") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1212121212") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0001000100") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0001000100") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3000100002") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3000100002") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "100002000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100002000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "200000010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "200000010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0012002001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0012002001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "13010003") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "13010003") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "42101000") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "42101000") == True: {e}')
    
    total += 1
    try:
        result = candidate(num = "7000000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "7000000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "6543210000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "6543210000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "5000001400") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5000001400") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00000000050") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00000000050") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "210010010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "210010010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "012020200") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "012020200") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000004") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000004") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "000030000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000030000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "12101") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12101") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "4000010000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4000010000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "2220000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2220000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1210101010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1210101010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "000000003") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000000003") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0210000110") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0210000110") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1000100010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000100010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "100000002") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100000002") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3000300000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3000300000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "400001000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "400001000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0123456789") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0123456789") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000001001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000001001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00000110000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00000110000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "2100100000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2100100000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3110000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3110000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00000020000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00000020000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000020") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000020") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "200100100") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "200100100") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1210100") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1210100") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1020304050") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1020304050") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "6000000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "6000000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "001010101") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "001010101") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000002") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000002") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "000001011") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000001011") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "20200") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "20200") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1111111110") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111111110") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1300102000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1300102000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "10000000001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10000000001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "2020200") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2020200") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "41210000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "41210000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000009") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000009") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0020200") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0020200") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "200001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "200001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "100000101") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100000101") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "010200200") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "010200200") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0123210") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0123210") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3000100000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3000100000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "200000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "200000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "021001001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "021001001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "30000003") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "30000003") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "300020000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "300020000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "300000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "300000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00000000006") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00000000006") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000110") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000110") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "5000000005") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5000000005") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "4000000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4000000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "2010011000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2010011000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "201010101") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "201010101") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "001100110") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "001100110") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0112233445") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0112233445") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "5000000100") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5000000100") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0110001000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0110001000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "01000000001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "01000000001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3110000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3110000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "100010001") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100010001") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "0000010010") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000010010") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00010000100") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00010000100") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00000003000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00000003000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "8000000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "8000000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "00001111") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00001111") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "600000000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "600000000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "1200100000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1200100000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "3330000000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3330000000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "011110000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "011110000") == False: {e}')
    
    total += 1
    try:
        result = candidate(num = "2120001000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2120001000") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = "1111") == False
    assert candidate(num = "00000") == False
    assert candidate(num = "10") == False
    assert candidate(num = "1111111111") == False
    assert candidate(num = "000") == False
    assert candidate(num = "6200000000") == False
    assert candidate(num = "0100100010") == False
    assert candidate(num = "6210001000") == True
    assert candidate(num = "030") == False
    assert candidate(num = "9876543210") == False
    assert candidate(num = "2020202020") == False
    assert candidate(num = "0") == False
    assert candidate(num = "5000000000") == False
    assert candidate(num = "21200") == True
    assert candidate(num = "0987654321") == False
    assert candidate(num = "2020") == True
    assert candidate(num = "11200") == False
    assert candidate(num = "1010101010") == False
    assert candidate(num = "1210") == True
    assert candidate(num = "6543210") == False
    assert candidate(num = "50000") == False
    assert candidate(num = "5000001000") == False
    assert candidate(num = "1234567890") == False
    assert candidate(num = "1221111111") == False
    assert candidate(num = "1001") == False
    assert candidate(num = "0000") == False
    assert candidate(num = "2120000000") == False
    assert candidate(num = "4000400040") == False
    assert candidate(num = "101010101") == False
    assert candidate(num = "0000100000") == False
    assert candidate(num = "1112212100") == False
    assert candidate(num = "0000000000") == False
    assert candidate(num = "400000000004") == False
    assert candidate(num = "0000000100") == False
    assert candidate(num = "0101010101") == False
    assert candidate(num = "00100000010") == False
    assert candidate(num = "00000000400") == False
    assert candidate(num = "9000000000") == False
    assert candidate(num = "3110001000") == False
    assert candidate(num = "0100101010") == False
    assert candidate(num = "100010000") == False
    assert candidate(num = "000020000") == False
    assert candidate(num = "100201000") == False
    assert candidate(num = "30003") == False
    assert candidate(num = "1221") == False
    assert candidate(num = "12101000") == False
    assert candidate(num = "000010001") == False
    assert candidate(num = "3000000000") == False
    assert candidate(num = "0010000000") == False
    assert candidate(num = "0000101000") == False
    assert candidate(num = "3100000") == False
    assert candidate(num = "3000000010") == False
    assert candidate(num = "0100000001") == False
    assert candidate(num = "00001001000") == False
    assert candidate(num = "121010000") == False
    assert candidate(num = "0123400000") == False
    assert candidate(num = "2010000000") == False
    assert candidate(num = "0010000010") == False
    assert candidate(num = "102020100") == False
    assert candidate(num = "000300003") == False
    assert candidate(num = "500000000") == False
    assert candidate(num = "40000000") == False
    assert candidate(num = "5000011000") == False
    assert candidate(num = "1001001001") == False
    assert candidate(num = "1221100000") == False
    assert candidate(num = "1212121212") == False
    assert candidate(num = "0001000100") == False
    assert candidate(num = "0000000010") == False
    assert candidate(num = "3000100002") == False
    assert candidate(num = "100002000") == False
    assert candidate(num = "200000010") == False
    assert candidate(num = "0012002001") == False
    assert candidate(num = "13010003") == False
    assert candidate(num = "42101000") == True
    assert candidate(num = "7000000000") == False
    assert candidate(num = "6543210000") == False
    assert candidate(num = "5000001400") == False
    assert candidate(num = "00000000050") == False
    assert candidate(num = "210010010") == False
    assert candidate(num = "012020200") == False
    assert candidate(num = "0000000004") == False
    assert candidate(num = "000030000") == False
    assert candidate(num = "12101") == False
    assert candidate(num = "4000010000") == False
    assert candidate(num = "2220000000") == False
    assert candidate(num = "1210101010") == False
    assert candidate(num = "000000003") == False
    assert candidate(num = "0210000110") == False
    assert candidate(num = "1000100010") == False
    assert candidate(num = "100000002") == False
    assert candidate(num = "3000300000") == False
    assert candidate(num = "400001000") == False
    assert candidate(num = "0123456789") == False
    assert candidate(num = "0000001001") == False
    assert candidate(num = "00000110000") == False
    assert candidate(num = "2100100000") == False
    assert candidate(num = "3110000") == False
    assert candidate(num = "00000020000") == False
    assert candidate(num = "0000000020") == False
    assert candidate(num = "200100100") == False
    assert candidate(num = "1210100") == False
    assert candidate(num = "1020304050") == False
    assert candidate(num = "6000000000") == False
    assert candidate(num = "001010101") == False
    assert candidate(num = "0000000002") == False
    assert candidate(num = "000001011") == False
    assert candidate(num = "20200") == False
    assert candidate(num = "1111111110") == False
    assert candidate(num = "1300102000") == False
    assert candidate(num = "10000000001") == False
    assert candidate(num = "2020200") == False
    assert candidate(num = "41210000") == False
    assert candidate(num = "0000000009") == False
    assert candidate(num = "0020200") == False
    assert candidate(num = "200001") == False
    assert candidate(num = "100000101") == False
    assert candidate(num = "010200200") == False
    assert candidate(num = "1000000001") == False
    assert candidate(num = "0123210") == False
    assert candidate(num = "3000100000") == False
    assert candidate(num = "200000000") == False
    assert candidate(num = "021001001") == False
    assert candidate(num = "30000003") == False
    assert candidate(num = "300020000") == False
    assert candidate(num = "0000000001") == False
    assert candidate(num = "300000000") == False
    assert candidate(num = "00000000006") == False
    assert candidate(num = "0000000110") == False
    assert candidate(num = "5000000005") == False
    assert candidate(num = "4000000000") == False
    assert candidate(num = "2010011000") == False
    assert candidate(num = "201010101") == False
    assert candidate(num = "001100110") == False
    assert candidate(num = "1000000010") == False
    assert candidate(num = "0112233445") == False
    assert candidate(num = "5000000100") == False
    assert candidate(num = "0110001000") == False
    assert candidate(num = "01000000001") == False
    assert candidate(num = "3110000000") == False
    assert candidate(num = "100010001") == False
    assert candidate(num = "0000010010") == False
    assert candidate(num = "00010000100") == False
    assert candidate(num = "00000003000") == False
    assert candidate(num = "8000000000") == False
    assert candidate(num = "00001111") == False
    assert candidate(num = "600000000000") == False
    assert candidate(num = "1200100000") == False
    assert candidate(num = "3330000000") == False
    assert candidate(num = "011110000") == False
    assert candidate(num = "2120001000") == False


