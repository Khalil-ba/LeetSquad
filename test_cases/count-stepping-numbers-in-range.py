def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(low = "123",high = "456") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123",high = "456") == 13: {e}')
    
    total += 1
    try:
        result = candidate(low = "5555555555",high = "6666666666") == 436
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "5555555555",high = "6666666666") == 436: {e}')
    
    total += 1
    try:
        result = candidate(low = "1111111111",high = "2222222222") == 307
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1111111111",high = "2222222222") == 307: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000",high = "1000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000",high = "1000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "10",high = "100") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10",high = "100") == 17: {e}')
    
    total += 1
    try:
        result = candidate(low = "9999999999",high = "9999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9999999999",high = "9999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "9876543210") == 6111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "9876543210") == 6111: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "11") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "11") == 10: {e}')
    
    total += 1
    try:
        result = candidate(low = "9876543210",high = "9876543210") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9876543210",high = "9876543210") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "90",high = "101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "90",high = "101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000000000000",high = "10000000000000000010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000000000000",high = "10000000000000000010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "12345678901234567890",high = "98765432109876543210") == 1768804
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "12345678901234567890",high = "98765432109876543210") == 1768804: {e}')
    
    total += 1
    try:
        result = candidate(low = "12345678901234567890",high = "12345678901234567891") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "12345678901234567890",high = "12345678901234567891") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "999999999999999999",high = "1000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "999999999999999999",high = "1000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "321098765432109876543210987",high = "432109876543210987654321098") == 25767582
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "321098765432109876543210987",high = "432109876543210987654321098") == 25767582: {e}')
    
    total += 1
    try:
        result = candidate(low = "8888888888",high = "8888888899") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8888888888",high = "8888888899") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "9999999999999999999",high = "10000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9999999999999999999",high = "10000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "3333333333",high = "4444444444") == 436
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "3333333333",high = "4444444444") == 436: {e}')
    
    total += 1
    try:
        result = candidate(low = "989898989898989898",high = "999999999999999999") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "989898989898989898",high = "999999999999999999") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "9",high = "9") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9",high = "9") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "1234567890",high = "2345678901") == 333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1234567890",high = "2345678901") == 333: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "2147483647") == 3627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "2147483647") == 3627: {e}')
    
    total += 1
    try:
        result = candidate(low = "1010101010",high = "2020202020") == 251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1010101010",high = "2020202020") == 251: {e}')
    
    total += 1
    try:
        result = candidate(low = "8888888888",high = "9999999999") == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8888888888",high = "9999999999") == 196: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "12345678901234567890") == 2358711
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "12345678901234567890") == 2358711: {e}')
    
    total += 1
    try:
        result = candidate(low = "54321098765432109876543210",high = "65432109876543210987654321") == 14851321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "54321098765432109876543210",high = "65432109876543210987654321") == 14851321: {e}')
    
    total += 1
    try:
        result = candidate(low = "5",high = "5555555555") == 4904
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "5",high = "5555555555") == 4904: {e}')
    
    total += 1
    try:
        result = candidate(low = "987654321",high = "9876543211") == 2931
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "987654321",high = "9876543211") == 2931: {e}')
    
    total += 1
    try:
        result = candidate(low = "54321098765432109876",high = "65432109876543210987") == 297140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "54321098765432109876",high = "65432109876543210987") == 297140: {e}')
    
    total += 1
    try:
        result = candidate(low = "5000000000",high = "5000000010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "5000000000",high = "5000000010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "500",high = "600") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "500",high = "600") == 4: {e}')
    
    total += 1
    try:
        result = candidate(low = "5",high = "5") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "5",high = "5") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "12345678912345678912",high = "23456789123456789123") == 226942
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "12345678912345678912",high = "23456789123456789123") == 226942: {e}')
    
    total += 1
    try:
        result = candidate(low = "8888888888",high = "8989898989") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8888888888",high = "8989898989") == 70: {e}')
    
    total += 1
    try:
        result = candidate(low = "9876543210",high = "9876543219") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9876543210",high = "9876543219") == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = "888888888",high = "999999999") == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "888888888",high = "999999999") == 105: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000",high = "9999999999") == 2986
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000",high = "9999999999") == 2986: {e}')
    
    total += 1
    try:
        result = candidate(low = "8989898989",high = "9898989898") == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8989898989",high = "9898989898") == 127: {e}')
    
    total += 1
    try:
        result = candidate(low = "1212121212",high = "2121212121") == 202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1212121212",high = "2121212121") == 202: {e}')
    
    total += 1
    try:
        result = candidate(low = "987654321",high = "987654322") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "987654321",high = "987654322") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000000000000",high = "10000000000000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000000000000",high = "10000000000000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "54321",high = "65432") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "54321",high = "65432") == 17: {e}')
    
    total += 1
    try:
        result = candidate(low = "8999999999999999999",high = "9000000000000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8999999999999999999",high = "9000000000000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "1010101010",high = "1121212121") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1010101010",high = "1121212121") == 70: {e}')
    
    total += 1
    try:
        result = candidate(low = "1010101010",high = "9090909090") == 2860
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1010101010",high = "9090909090") == 2860: {e}')
    
    total += 1
    try:
        result = candidate(low = "9999999999",high = "10000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9999999999",high = "10000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "9999999990",high = "9999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9999999990",high = "9999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "9876543210987654321",high = "9876543210987654322") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9876543210987654321",high = "9876543210987654322") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "9999999999") == 6236
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "9999999999") == 6236: {e}')
    
    total += 1
    try:
        result = candidate(low = "98765432109876543210",high = "98765432109876543211") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "98765432109876543210",high = "98765432109876543211") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "1234567890",high = "1234567899") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1234567890",high = "1234567899") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "123",high = "45678901234567890123") == 3157659
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123",high = "45678901234567890123") == 3157659: {e}')
    
    total += 1
    try:
        result = candidate(low = "7777777777",high = "8888888888") == 307
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "7777777777",high = "8888888888") == 307: {e}')
    
    total += 1
    try:
        result = candidate(low = "12121212121212121212",high = "13131313131313131313") == 102885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "12121212121212121212",high = "13131313131313131313") == 102885: {e}')
    
    total += 1
    try:
        result = candidate(low = "321",high = "654") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "321",high = "654") == 13: {e}')
    
    total += 1
    try:
        result = candidate(low = "9876543210123456789",high = "9876543210123456790") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9876543210123456789",high = "9876543210123456790") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "1010101010",high = "1111111111") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1010101010",high = "1111111111") == 70: {e}')
    
    total += 1
    try:
        result = candidate(low = "98765432101234567890",high = "98765432101234567899") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "98765432101234567890",high = "98765432101234567899") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "4444444444",high = "5555555555") == 456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "4444444444",high = "5555555555") == 456: {e}')
    
    total += 1
    try:
        result = candidate(low = "200",high = "210") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "200",high = "210") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "1234567890") == 3500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "1234567890") == 3500: {e}')
    
    total += 1
    try:
        result = candidate(low = "987654321",high = "9876543210") == 2931
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "987654321",high = "9876543210") == 2931: {e}')
    
    total += 1
    try:
        result = candidate(low = "9876543210",high = "10123456789") == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "9876543210",high = "10123456789") == 252: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000000000000000000000000000000000000000000000",high = "99999999999999999999999999999999999999999999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000000000000000000000000000000000000000000000",high = "99999999999999999999999999999999999999999999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "99999999999999999999",high = "100000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "99999999999999999999",high = "100000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "1111111111111111111",high = "1212121212121212121") == 8551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1111111111111111111",high = "1212121212121212121") == 8551: {e}')
    
    total += 1
    try:
        result = candidate(low = "1111111111",high = "1111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1111111111",high = "1111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "8989898989",high = "9090909090") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8989898989",high = "9090909090") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "98765432101234567890",high = "98765432101234567891") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "98765432101234567890",high = "98765432101234567891") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "5432109876",high = "5432109877") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "5432109876",high = "5432109877") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "50505050505050505050",high = "60606060606060606060") == 298777
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "50505050505050505050",high = "60606060606060606060") == 298777: {e}')
    
    total += 1
    try:
        result = candidate(low = "11111111111111111111",high = "22222222222222222222") == 204289
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "11111111111111111111",high = "22222222222222222222") == 204289: {e}')
    
    total += 1
    try:
        result = candidate(low = "98765432101234567890",high = "98765432109876543210") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "98765432101234567890",high = "98765432109876543210") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "10000000000",high = "20000000000") == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10000000000",high = "20000000000") == 460: {e}')
    
    total += 1
    try:
        result = candidate(low = "123",high = "135") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123",high = "135") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "1000000000",high = "2000000000") == 251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1000000000",high = "2000000000") == 251: {e}')
    
    total += 1
    try:
        result = candidate(low = "123456789",high = "987654321") == 1362
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123456789",high = "987654321") == 1362: {e}')
    
    total += 1
    try:
        result = candidate(low = "98765432109876543210987654321",high = "98765432109876543210987654322") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "98765432109876543210987654321",high = "98765432109876543210987654322") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "98765",high = "98766") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "98765",high = "98766") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "123456789",high = "1234567891") == 1681
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123456789",high = "1234567891") == 1681: {e}')
    
    total += 1
    try:
        result = candidate(low = "987654321",high = "9876543219") == 2932
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "987654321",high = "9876543219") == 2932: {e}')
    
    total += 1
    try:
        result = candidate(low = "987654321",high = "987654329") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "987654321",high = "987654329") == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = "543210",high = "6543210") == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "543210",high = "6543210") == 380: {e}')
    
    total += 1
    try:
        result = candidate(low = "1234567890",high = "1234567891") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1234567890",high = "1234567891") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "123",high = "321") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123",high = "321") == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = "1010101010101010101",high = "1111111111111111111") == 22950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1010101010101010101",high = "1111111111111111111") == 22950: {e}')
    
    total += 1
    try:
        result = candidate(low = "8999999999",high = "9000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "8999999999",high = "9000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = "555555555",high = "666666666") == 228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "555555555",high = "666666666") == 228: {e}')
    
    total += 1
    try:
        result = candidate(low = "10101010101010101010",high = "21212121212121212121") == 195908
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10101010101010101010",high = "21212121212121212121") == 195908: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "10000000000000000000") == 2194764
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "10000000000000000000") == 2194764: {e}')
    
    total += 1
    try:
        result = candidate(low = "12345",high = "123456789012345") == 90485
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "12345",high = "123456789012345") == 90485: {e}')
    
    total += 1
    try:
        result = candidate(low = "2222222222",high = "3333333333") == 389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "2222222222",high = "3333333333") == 389: {e}')
    
    total += 1
    try:
        result = candidate(low = "1",high = "99999999999999999999999999999999999999999999999999") == 254219541
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1",high = "99999999999999999999999999999999999999999999999999") == 254219541: {e}')
    
    total += 1
    try:
        result = candidate(low = "123454321",high = "123456789") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123454321",high = "123456789") == 16: {e}')
    
    total += 1
    try:
        result = candidate(low = "1010101010",high = "1010101011") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1010101010",high = "1010101011") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "112233445566778899",high = "122334455667788990") == 12190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "112233445566778899",high = "122334455667788990") == 12190: {e}')
    
    total += 1
    try:
        result = candidate(low = "100000000000000000000000000000000000000000000000000",high = "200000000000000000000000000000000000000000000000000") == 251590529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "100000000000000000000000000000000000000000000000000",high = "200000000000000000000000000000000000000000000000000") == 251590529: {e}')
    
    total += 1
    try:
        result = candidate(low = "1111111111",high = "9999999999") == 2916
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "1111111111",high = "9999999999") == 2916: {e}')
    
    total += 1
    try:
        result = candidate(low = "10101010101010101010",high = "20202020202020202020") == 164407
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10101010101010101010",high = "20202020202020202020") == 164407: {e}')
    
    total += 1
    try:
        result = candidate(low = "123",high = "133") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "123",high = "133") == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = "10",high = "1111111111") == 3311
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = "10",high = "1111111111") == 3311: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(low = "123",high = "456") == 13
    assert candidate(low = "5555555555",high = "6666666666") == 436
    assert candidate(low = "1111111111",high = "2222222222") == 307
    assert candidate(low = "1000000000",high = "1000000001") == 0
    assert candidate(low = "10",high = "100") == 17
    assert candidate(low = "9999999999",high = "9999999999") == 0
    assert candidate(low = "1",high = "9876543210") == 6111
    assert candidate(low = "1",high = "11") == 10
    assert candidate(low = "9876543210",high = "9876543210") == 1
    assert candidate(low = "90",high = "101") == 2
    assert candidate(low = "10000000000000000000",high = "10000000000000000010") == 0
    assert candidate(low = "12345678901234567890",high = "98765432109876543210") == 1768804
    assert candidate(low = "12345678901234567890",high = "12345678901234567891") == 0
    assert candidate(low = "999999999999999999",high = "1000000000000000000") == 0
    assert candidate(low = "321098765432109876543210987",high = "432109876543210987654321098") == 25767582
    assert candidate(low = "8888888888",high = "8888888899") == 0
    assert candidate(low = "9999999999999999999",high = "10000000000000000000") == 0
    assert candidate(low = "3333333333",high = "4444444444") == 436
    assert candidate(low = "989898989898989898",high = "999999999999999999") == 1
    assert candidate(low = "9",high = "9") == 1
    assert candidate(low = "1234567890",high = "2345678901") == 333
    assert candidate(low = "1",high = "2147483647") == 3627
    assert candidate(low = "1010101010",high = "2020202020") == 251
    assert candidate(low = "8888888888",high = "9999999999") == 196
    assert candidate(low = "1",high = "12345678901234567890") == 2358711
    assert candidate(low = "54321098765432109876543210",high = "65432109876543210987654321") == 14851321
    assert candidate(low = "5",high = "5555555555") == 4904
    assert candidate(low = "987654321",high = "9876543211") == 2931
    assert candidate(low = "54321098765432109876",high = "65432109876543210987") == 297140
    assert candidate(low = "5000000000",high = "5000000010") == 0
    assert candidate(low = "500",high = "600") == 4
    assert candidate(low = "5",high = "5") == 1
    assert candidate(low = "12345678912345678912",high = "23456789123456789123") == 226942
    assert candidate(low = "8888888888",high = "8989898989") == 70
    assert candidate(low = "9876543210",high = "9876543219") == 2
    assert candidate(low = "888888888",high = "999999999") == 105
    assert candidate(low = "1000000000",high = "9999999999") == 2986
    assert candidate(low = "8989898989",high = "9898989898") == 127
    assert candidate(low = "1212121212",high = "2121212121") == 202
    assert candidate(low = "987654321",high = "987654322") == 1
    assert candidate(low = "10000000000000000000",high = "10000000000000000001") == 0
    assert candidate(low = "54321",high = "65432") == 17
    assert candidate(low = "8999999999999999999",high = "9000000000000000001") == 0
    assert candidate(low = "1010101010",high = "1121212121") == 70
    assert candidate(low = "1010101010",high = "9090909090") == 2860
    assert candidate(low = "9999999999",high = "10000000000") == 0
    assert candidate(low = "9999999990",high = "9999999999") == 0
    assert candidate(low = "9876543210987654321",high = "9876543210987654322") == 0
    assert candidate(low = "1",high = "9999999999") == 6236
    assert candidate(low = "98765432109876543210",high = "98765432109876543211") == 0
    assert candidate(low = "1234567890",high = "1234567899") == 1
    assert candidate(low = "123",high = "45678901234567890123") == 3157659
    assert candidate(low = "7777777777",high = "8888888888") == 307
    assert candidate(low = "12121212121212121212",high = "13131313131313131313") == 102885
    assert candidate(low = "321",high = "654") == 13
    assert candidate(low = "9876543210123456789",high = "9876543210123456790") == 1
    assert candidate(low = "1010101010",high = "1111111111") == 70
    assert candidate(low = "98765432101234567890",high = "98765432101234567899") == 1
    assert candidate(low = "4444444444",high = "5555555555") == 456
    assert candidate(low = "200",high = "210") == 1
    assert candidate(low = "1",high = "1234567890") == 3500
    assert candidate(low = "987654321",high = "9876543210") == 2931
    assert candidate(low = "9876543210",high = "10123456789") == 252
    assert candidate(low = "100000000000000000000000000000000000000000000000000",high = "99999999999999999999999999999999999999999999999999") == 0
    assert candidate(low = "99999999999999999999",high = "100000000000000000000") == 0
    assert candidate(low = "1111111111111111111",high = "1212121212121212121") == 8551
    assert candidate(low = "1111111111",high = "1111111111") == 0
    assert candidate(low = "8989898989",high = "9090909090") == 1
    assert candidate(low = "98765432101234567890",high = "98765432101234567891") == 0
    assert candidate(low = "5432109876",high = "5432109877") == 0
    assert candidate(low = "50505050505050505050",high = "60606060606060606060") == 298777
    assert candidate(low = "11111111111111111111",high = "22222222222222222222") == 204289
    assert candidate(low = "98765432101234567890",high = "98765432109876543210") == 1
    assert candidate(low = "10000000000",high = "20000000000") == 460
    assert candidate(low = "123",high = "135") == 1
    assert candidate(low = "1000000000",high = "2000000000") == 251
    assert candidate(low = "123456789",high = "987654321") == 1362
    assert candidate(low = "98765432109876543210987654321",high = "98765432109876543210987654322") == 0
    assert candidate(low = "98765",high = "98766") == 1
    assert candidate(low = "123456789",high = "1234567891") == 1681
    assert candidate(low = "987654321",high = "9876543219") == 2932
    assert candidate(low = "987654321",high = "987654329") == 2
    assert candidate(low = "543210",high = "6543210") == 380
    assert candidate(low = "1234567890",high = "1234567891") == 0
    assert candidate(low = "123",high = "321") == 6
    assert candidate(low = "1010101010101010101",high = "1111111111111111111") == 22950
    assert candidate(low = "8999999999",high = "9000000000") == 0
    assert candidate(low = "555555555",high = "666666666") == 228
    assert candidate(low = "10101010101010101010",high = "21212121212121212121") == 195908
    assert candidate(low = "1",high = "10000000000000000000") == 2194764
    assert candidate(low = "12345",high = "123456789012345") == 90485
    assert candidate(low = "2222222222",high = "3333333333") == 389
    assert candidate(low = "1",high = "99999999999999999999999999999999999999999999999999") == 254219541
    assert candidate(low = "123454321",high = "123456789") == 16
    assert candidate(low = "1010101010",high = "1010101011") == 1
    assert candidate(low = "112233445566778899",high = "122334455667788990") == 12190
    assert candidate(low = "100000000000000000000000000000000000000000000000000",high = "200000000000000000000000000000000000000000000000000") == 251590529
    assert candidate(low = "1111111111",high = "9999999999") == 2916
    assert candidate(low = "10101010101010101010",high = "20202020202020202020") == 164407
    assert candidate(low = "123",high = "133") == 1
    assert candidate(low = "10",high = "1111111111") == 3311


