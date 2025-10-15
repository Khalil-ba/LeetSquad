def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(number = "222333",digit = "2") == "22333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "222333",digit = "2") == "22333": {e}')
    
    total += 1
    try:
        result = candidate(number = "99999",digit = "9") == "9999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "99999",digit = "9") == "9999": {e}')
    
    total += 1
    try:
        result = candidate(number = "999",digit = "9") == "99"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "999",digit = "9") == "99": {e}')
    
    total += 1
    try:
        result = candidate(number = "551",digit = "5") == "51"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "551",digit = "5") == "51": {e}')
    
    total += 1
    try:
        result = candidate(number = "10001",digit = "0") == "1001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "10001",digit = "0") == "1001": {e}')
    
    total += 1
    try:
        result = candidate(number = "987654321",digit = "9") == "87654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "987654321",digit = "9") == "87654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "123456789",digit = "5") == "12346789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123456789",digit = "5") == "12346789": {e}')
    
    total += 1
    try:
        result = candidate(number = "11111",digit = "1") == "1111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "11111",digit = "1") == "1111": {e}')
    
    total += 1
    try:
        result = candidate(number = "123456789123456789",digit = "4") == "12356789123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123456789123456789",digit = "4") == "12356789123456789": {e}')
    
    total += 1
    try:
        result = candidate(number = "1000001",digit = "0") == "100001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1000001",digit = "0") == "100001": {e}')
    
    total += 1
    try:
        result = candidate(number = "11211",digit = "1") == "1211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "11211",digit = "1") == "1211": {e}')
    
    total += 1
    try:
        result = candidate(number = "123",digit = "3") == "12"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123",digit = "3") == "12": {e}')
    
    total += 1
    try:
        result = candidate(number = "111111111",digit = "1") == "11111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "111111111",digit = "1") == "11111111": {e}')
    
    total += 1
    try:
        result = candidate(number = "1112",digit = "1") == "112"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1112",digit = "1") == "112": {e}')
    
    total += 1
    try:
        result = candidate(number = "999999999",digit = "9") == "99999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "999999999",digit = "9") == "99999999": {e}')
    
    total += 1
    try:
        result = candidate(number = "1231",digit = "1") == "231"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1231",digit = "1") == "231": {e}')
    
    total += 1
    try:
        result = candidate(number = "1221",digit = "1") == "221"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1221",digit = "1") == "221": {e}')
    
    total += 1
    try:
        result = candidate(number = "100000001",digit = "0") == "10000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "100000001",digit = "0") == "10000001": {e}')
    
    total += 1
    try:
        result = candidate(number = "87654321",digit = "8") == "7654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "87654321",digit = "8") == "7654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "3141592653589793",digit = "1") == "341592653589793"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "3141592653589793",digit = "1") == "341592653589793": {e}')
    
    total += 1
    try:
        result = candidate(number = "123456789",digit = "8") == "12345679"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123456789",digit = "8") == "12345679": {e}')
    
    total += 1
    try:
        result = candidate(number = "987654321",digit = "2") == "98765431"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "987654321",digit = "2") == "98765431": {e}')
    
    total += 1
    try:
        result = candidate(number = "1221",digit = "2") == "121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1221",digit = "2") == "121": {e}')
    
    total += 1
    try:
        result = candidate(number = "2222222",digit = "2") == "222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "2222222",digit = "2") == "222222": {e}')
    
    total += 1
    try:
        result = candidate(number = "1111",digit = "1") == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1111",digit = "1") == "111": {e}')
    
    total += 1
    try:
        result = candidate(number = "123456789",digit = "9") == "12345678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123456789",digit = "9") == "12345678": {e}')
    
    total += 1
    try:
        result = candidate(number = "5656565656",digit = "6") == "565656565"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "5656565656",digit = "6") == "565656565": {e}')
    
    total += 1
    try:
        result = candidate(number = "987654321123456789",digit = "4") == "98765432112356789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "987654321123456789",digit = "4") == "98765432112356789": {e}')
    
    total += 1
    try:
        result = candidate(number = "123123123123",digit = "2") == "13123123123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123123123123",digit = "2") == "13123123123": {e}')
    
    total += 1
    try:
        result = candidate(number = "10101010101010101010101010101010101010101010101010",digit = "1") == "1010101010101010101010101010101010101010101010100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "10101010101010101010101010101010101010101010101010",digit = "1") == "1010101010101010101010101010101010101010101010100": {e}')
    
    total += 1
    try:
        result = candidate(number = "9898989898",digit = "8") == "998989898"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "9898989898",digit = "8") == "998989898": {e}')
    
    total += 1
    try:
        result = candidate(number = "1122334455",digit = "1") == "122334455"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1122334455",digit = "1") == "122334455": {e}')
    
    total += 1
    try:
        result = candidate(number = "333333333",digit = "3") == "33333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "333333333",digit = "3") == "33333333": {e}')
    
    total += 1
    try:
        result = candidate(number = "1000000000",digit = "1") == "000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1000000000",digit = "1") == "000000000": {e}')
    
    total += 1
    try:
        result = candidate(number = "9876543210",digit = "5") == "987643210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "9876543210",digit = "5") == "987643210": {e}')
    
    total += 1
    try:
        result = candidate(number = "12345654321",digit = "3") == "1245654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "12345654321",digit = "3") == "1245654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "112233445566778899",digit = "5") == "11223344566778899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "112233445566778899",digit = "5") == "11223344566778899": {e}')
    
    total += 1
    try:
        result = candidate(number = "100000000",digit = "0") == "10000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "100000000",digit = "0") == "10000000": {e}')
    
    total += 1
    try:
        result = candidate(number = "987987987",digit = "7") == "98987987"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "987987987",digit = "7") == "98987987": {e}')
    
    total += 1
    try:
        result = candidate(number = "101010101010",digit = "0") == "11010101010"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "101010101010",digit = "0") == "11010101010": {e}')
    
    total += 1
    try:
        result = candidate(number = "5959595959",digit = "9") == "595959595"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "5959595959",digit = "9") == "595959595": {e}')
    
    total += 1
    try:
        result = candidate(number = "11223344556677889900",digit = "1") == "1223344556677889900"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "11223344556677889900",digit = "1") == "1223344556677889900": {e}')
    
    total += 1
    try:
        result = candidate(number = "987654321123456789987654321",digit = "3") == "98765432112456789987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "987654321123456789987654321",digit = "3") == "98765432112456789987654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "12345678901234567890",digit = "0") == "1234567891234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "12345678901234567890",digit = "0") == "1234567891234567890": {e}')
    
    total += 1
    try:
        result = candidate(number = "122122122",digit = "2") == "12212212"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "122122122",digit = "2") == "12212212": {e}')
    
    total += 1
    try:
        result = candidate(number = "12345678901234567890",digit = "4") == "1235678901234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "12345678901234567890",digit = "4") == "1235678901234567890": {e}')
    
    total += 1
    try:
        result = candidate(number = "123456789101112",digit = "1") == "23456789101112"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123456789101112",digit = "1") == "23456789101112": {e}')
    
    total += 1
    try:
        result = candidate(number = "98765432109876543210",digit = "5") == "9876543210987643210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "98765432109876543210",digit = "5") == "9876543210987643210": {e}')
    
    total += 1
    try:
        result = candidate(number = "11111111111111111111111111111111111111111111111111",digit = "1") == "1111111111111111111111111111111111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "11111111111111111111111111111111111111111111111111",digit = "1") == "1111111111111111111111111111111111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(number = "1919191919191919",digit = "9") == "191919191919191"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1919191919191919",digit = "9") == "191919191919191": {e}')
    
    total += 1
    try:
        result = candidate(number = "1000000001",digit = "0") == "100000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1000000001",digit = "0") == "100000001": {e}')
    
    total += 1
    try:
        result = candidate(number = "543219876",digit = "9") == "54321876"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "543219876",digit = "9") == "54321876": {e}')
    
    total += 1
    try:
        result = candidate(number = "56789101112131415161718192021",digit = "1") == "5678910112131415161718192021"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "56789101112131415161718192021",digit = "1") == "5678910112131415161718192021": {e}')
    
    total += 1
    try:
        result = candidate(number = "987654321987654321987654321987654321",digit = "8") == "98765432198765432198765432197654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "987654321987654321987654321987654321",digit = "8") == "98765432198765432198765432197654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "123412341234",digit = "2") == "13412341234"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123412341234",digit = "2") == "13412341234": {e}')
    
    total += 1
    try:
        result = candidate(number = "11223344556677889900",digit = "0") == "1122334455667788990"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "11223344556677889900",digit = "0") == "1122334455667788990": {e}')
    
    total += 1
    try:
        result = candidate(number = "12345678901234567890123456789012345678901234567890",digit = "0") == "1234567891234567890123456789012345678901234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "12345678901234567890123456789012345678901234567890",digit = "0") == "1234567891234567890123456789012345678901234567890": {e}')
    
    total += 1
    try:
        result = candidate(number = "1919191919",digit = "9") == "191919191"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1919191919",digit = "9") == "191919191": {e}')
    
    total += 1
    try:
        result = candidate(number = "1919191919191919191919191919191919191919191919191",digit = "9") == "191919191919191919191919191919191919191919191911"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1919191919191919191919191919191919191919191919191",digit = "9") == "191919191919191919191919191919191919191919191911": {e}')
    
    total += 1
    try:
        result = candidate(number = "9999999999",digit = "9") == "999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "9999999999",digit = "9") == "999999999": {e}')
    
    total += 1
    try:
        result = candidate(number = "543219876987654321",digit = "9") == "54321987687654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "543219876987654321",digit = "9") == "54321987687654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "987654321123456789",digit = "1") == "98765432123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "987654321123456789",digit = "1") == "98765432123456789": {e}')
    
    total += 1
    try:
        result = candidate(number = "3131313131",digit = "1") == "331313131"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "3131313131",digit = "1") == "331313131": {e}')
    
    total += 1
    try:
        result = candidate(number = "555555555555555555555",digit = "5") == "55555555555555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "555555555555555555555",digit = "5") == "55555555555555555555": {e}')
    
    total += 1
    try:
        result = candidate(number = "123456789876543210987654321",digit = "9") == "12345678987654321087654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123456789876543210987654321",digit = "9") == "12345678987654321087654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "9999999999999999999",digit = "9") == "999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "9999999999999999999",digit = "9") == "999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(number = "1212121212",digit = "2") == "121212121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1212121212",digit = "2") == "121212121": {e}')
    
    total += 1
    try:
        result = candidate(number = "12345123451234512345",digit = "4") == "1235123451234512345"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "12345123451234512345",digit = "4") == "1235123451234512345": {e}')
    
    total += 1
    try:
        result = candidate(number = "91827364591827364591",digit = "1") == "9827364591827364591"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "91827364591827364591",digit = "1") == "9827364591827364591": {e}')
    
    total += 1
    try:
        result = candidate(number = "567567567",digit = "7") == "56756756"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "567567567",digit = "7") == "56756756": {e}')
    
    total += 1
    try:
        result = candidate(number = "999888777666555444333222111",digit = "9") == "99888777666555444333222111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "999888777666555444333222111",digit = "9") == "99888777666555444333222111": {e}')
    
    total += 1
    try:
        result = candidate(number = "10000000001",digit = "0") == "1000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "10000000001",digit = "0") == "1000000001": {e}')
    
    total += 1
    try:
        result = candidate(number = "876543210",digit = "0") == "87654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "876543210",digit = "0") == "87654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "5645645645645645645645645645645645645645645645645",digit = "5") == "645645645645645645645645645645645645645645645645"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "5645645645645645645645645645645645645645645645645",digit = "5") == "645645645645645645645645645645645645645645645645": {e}')
    
    total += 1
    try:
        result = candidate(number = "1234321",digit = "3") == "124321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1234321",digit = "3") == "124321": {e}')
    
    total += 1
    try:
        result = candidate(number = "123456789123456789123456789",digit = "8") == "12345679123456789123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123456789123456789123456789",digit = "8") == "12345679123456789123456789": {e}')
    
    total += 1
    try:
        result = candidate(number = "123123123123123",digit = "1") == "23123123123123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123123123123123",digit = "1") == "23123123123123": {e}')
    
    total += 1
    try:
        result = candidate(number = "5656565656",digit = "5") == "656565656"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "5656565656",digit = "5") == "656565656": {e}')
    
    total += 1
    try:
        result = candidate(number = "20202020202020202020202020202020202020202020202020",digit = "2") == "2020202020202020202020202020202020202020202020200"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "20202020202020202020202020202020202020202020202020",digit = "2") == "2020202020202020202020202020202020202020202020200": {e}')
    
    total += 1
    try:
        result = candidate(number = "2345678901234567890",digit = "0") == "234567891234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "2345678901234567890",digit = "0") == "234567891234567890": {e}')
    
    total += 1
    try:
        result = candidate(number = "918273645",digit = "9") == "18273645"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "918273645",digit = "9") == "18273645": {e}')
    
    total += 1
    try:
        result = candidate(number = "12233445566778899",digit = "9") == "1223344556677889"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "12233445566778899",digit = "9") == "1223344556677889": {e}')
    
    total += 1
    try:
        result = candidate(number = "5555555555555555555",digit = "5") == "555555555555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "5555555555555555555",digit = "5") == "555555555555555555": {e}')
    
    total += 1
    try:
        result = candidate(number = "101010101",digit = "0") == "11010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "101010101",digit = "0") == "11010101": {e}')
    
    total += 1
    try:
        result = candidate(number = "999999999999999999999",digit = "9") == "99999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "999999999999999999999",digit = "9") == "99999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(number = "8765432109876543210",digit = "5") == "876543210987643210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "8765432109876543210",digit = "5") == "876543210987643210": {e}')
    
    total += 1
    try:
        result = candidate(number = "33333333333333333333333333333333333333333333333333",digit = "3") == "3333333333333333333333333333333333333333333333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "33333333333333333333333333333333333333333333333333",digit = "3") == "3333333333333333333333333333333333333333333333333": {e}')
    
    total += 1
    try:
        result = candidate(number = "98765432109876543210",digit = "6") == "9876543210987543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "98765432109876543210",digit = "6") == "9876543210987543210": {e}')
    
    total += 1
    try:
        result = candidate(number = "100000000000000000000",digit = "0") == "10000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "100000000000000000000",digit = "0") == "10000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(number = "12345678901234567890",digit = "7") == "1234568901234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "12345678901234567890",digit = "7") == "1234568901234567890": {e}')
    
    total += 1
    try:
        result = candidate(number = "3232323232323232",digit = "3") == "323232323232322"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "3232323232323232",digit = "3") == "323232323232322": {e}')
    
    total += 1
    try:
        result = candidate(number = "123456789",digit = "2") == "13456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123456789",digit = "2") == "13456789": {e}')
    
    total += 1
    try:
        result = candidate(number = "19191919191919191919",digit = "9") == "1919191919191919191"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "19191919191919191919",digit = "9") == "1919191919191919191": {e}')
    
    total += 1
    try:
        result = candidate(number = "123123123",digit = "1") == "23123123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123123123",digit = "1") == "23123123": {e}')
    
    total += 1
    try:
        result = candidate(number = "5645645645645645645645645645645645645645645645645",digit = "6") == "564564564564564564564564564564564564564564564545"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "5645645645645645645645645645645645645645645645645",digit = "6") == "564564564564564564564564564564564564564564564545": {e}')
    
    total += 1
    try:
        result = candidate(number = "123987654321987654321987654321",digit = "9") == "12398765432198765432187654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123987654321987654321987654321",digit = "9") == "12398765432198765432187654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "1212121212121212121",digit = "2") == "121212121212121211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1212121212121212121",digit = "2") == "121212121212121211": {e}')
    
    total += 1
    try:
        result = candidate(number = "123123123123123123123",digit = "3") == "12312312312312312312"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123123123123123123123",digit = "3") == "12312312312312312312": {e}')
    
    total += 1
    try:
        result = candidate(number = "11111111111111111111",digit = "1") == "1111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "11111111111111111111",digit = "1") == "1111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(number = "112233445566778899",digit = "1") == "12233445566778899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "112233445566778899",digit = "1") == "12233445566778899": {e}')
    
    total += 1
    try:
        result = candidate(number = "2222222222222222222222222222222",digit = "2") == "222222222222222222222222222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "2222222222222222222222222222222",digit = "2") == "222222222222222222222222222222": {e}')
    
    total += 1
    try:
        result = candidate(number = "123987654321987654321987654321",digit = "1") == "23987654321987654321987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123987654321987654321987654321",digit = "1") == "23987654321987654321987654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "987654321987654321",digit = "9") == "98765432187654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "987654321987654321",digit = "9") == "98765432187654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "11111111111111111111111111111111111111111111",digit = "1") == "1111111111111111111111111111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "11111111111111111111111111111111111111111111",digit = "1") == "1111111111111111111111111111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(number = "9999999999999999999999999999999999999999999999999",digit = "9") == "999999999999999999999999999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "9999999999999999999999999999999999999999999999999",digit = "9") == "999999999999999999999999999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(number = "111222333444555666777888999",digit = "3") == "11122233444555666777888999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "111222333444555666777888999",digit = "3") == "11122233444555666777888999": {e}')
    
    total += 1
    try:
        result = candidate(number = "23333332",digit = "3") == "2333332"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "23333332",digit = "3") == "2333332": {e}')
    
    total += 1
    try:
        result = candidate(number = "22222222222222222222222222222222222222222222",digit = "2") == "2222222222222222222222222222222222222222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "22222222222222222222222222222222222222222222",digit = "2") == "2222222222222222222222222222222222222222222": {e}')
    
    total += 1
    try:
        result = candidate(number = "99999999991",digit = "9") == "9999999991"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "99999999991",digit = "9") == "9999999991": {e}')
    
    total += 1
    try:
        result = candidate(number = "333333",digit = "3") == "33333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "333333",digit = "3") == "33333": {e}')
    
    total += 1
    try:
        result = candidate(number = "123456789123456789123456789",digit = "9") == "12345678912345678912345678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123456789123456789123456789",digit = "9") == "12345678912345678912345678": {e}')
    
    total += 1
    try:
        result = candidate(number = "123412341234",digit = "1") == "23412341234"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "123412341234",digit = "1") == "23412341234": {e}')
    
    total += 1
    try:
        result = candidate(number = "987654321123456789",digit = "9") == "98765432112345678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "987654321123456789",digit = "9") == "98765432112345678": {e}')
    
    total += 1
    try:
        result = candidate(number = "543212345",digit = "2") == "54321345"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "543212345",digit = "2") == "54321345": {e}')
    
    total += 1
    try:
        result = candidate(number = "1111111111",digit = "1") == "111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1111111111",digit = "1") == "111111111": {e}')
    
    total += 1
    try:
        result = candidate(number = "432143214321",digit = "2") == "43214321431"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "432143214321",digit = "2") == "43214321431": {e}')
    
    total += 1
    try:
        result = candidate(number = "12233445566778899",digit = "1") == "2233445566778899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "12233445566778899",digit = "1") == "2233445566778899": {e}')
    
    total += 1
    try:
        result = candidate(number = "5555555555555555555555555555555555555555555555555",digit = "5") == "555555555555555555555555555555555555555555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "5555555555555555555555555555555555555555555555555",digit = "5") == "555555555555555555555555555555555555555555555555": {e}')
    
    total += 1
    try:
        result = candidate(number = "9876543210123456789",digit = "9") == "987654321012345678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "9876543210123456789",digit = "9") == "987654321012345678": {e}')
    
    total += 1
    try:
        result = candidate(number = "11112222",digit = "2") == "1111222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "11112222",digit = "2") == "1111222": {e}')
    
    total += 1
    try:
        result = candidate(number = "31415926535",digit = "1") == "3415926535"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "31415926535",digit = "1") == "3415926535": {e}')
    
    total += 1
    try:
        result = candidate(number = "1234567890987654321",digit = "5") == "123467890987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1234567890987654321",digit = "5") == "123467890987654321": {e}')
    
    total += 1
    try:
        result = candidate(number = "98877665544332211",digit = "8") == "9877665544332211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "98877665544332211",digit = "8") == "9877665544332211": {e}')
    
    total += 1
    try:
        result = candidate(number = "1000000000",digit = "0") == "100000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "1000000000",digit = "0") == "100000000": {e}')
    
    total += 1
    try:
        result = candidate(number = "2468135791113151719",digit = "1") == "246835791113151719"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "2468135791113151719",digit = "1") == "246835791113151719": {e}')
    
    total += 1
    try:
        result = candidate(number = "12345678987654321",digit = "7") == "1234568987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(number = "12345678987654321",digit = "7") == "1234568987654321": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(number = "222333",digit = "2") == "22333"
    assert candidate(number = "99999",digit = "9") == "9999"
    assert candidate(number = "999",digit = "9") == "99"
    assert candidate(number = "551",digit = "5") == "51"
    assert candidate(number = "10001",digit = "0") == "1001"
    assert candidate(number = "987654321",digit = "9") == "87654321"
    assert candidate(number = "123456789",digit = "5") == "12346789"
    assert candidate(number = "11111",digit = "1") == "1111"
    assert candidate(number = "123456789123456789",digit = "4") == "12356789123456789"
    assert candidate(number = "1000001",digit = "0") == "100001"
    assert candidate(number = "11211",digit = "1") == "1211"
    assert candidate(number = "123",digit = "3") == "12"
    assert candidate(number = "111111111",digit = "1") == "11111111"
    assert candidate(number = "1112",digit = "1") == "112"
    assert candidate(number = "999999999",digit = "9") == "99999999"
    assert candidate(number = "1231",digit = "1") == "231"
    assert candidate(number = "1221",digit = "1") == "221"
    assert candidate(number = "100000001",digit = "0") == "10000001"
    assert candidate(number = "87654321",digit = "8") == "7654321"
    assert candidate(number = "3141592653589793",digit = "1") == "341592653589793"
    assert candidate(number = "123456789",digit = "8") == "12345679"
    assert candidate(number = "987654321",digit = "2") == "98765431"
    assert candidate(number = "1221",digit = "2") == "121"
    assert candidate(number = "2222222",digit = "2") == "222222"
    assert candidate(number = "1111",digit = "1") == "111"
    assert candidate(number = "123456789",digit = "9") == "12345678"
    assert candidate(number = "5656565656",digit = "6") == "565656565"
    assert candidate(number = "987654321123456789",digit = "4") == "98765432112356789"
    assert candidate(number = "123123123123",digit = "2") == "13123123123"
    assert candidate(number = "10101010101010101010101010101010101010101010101010",digit = "1") == "1010101010101010101010101010101010101010101010100"
    assert candidate(number = "9898989898",digit = "8") == "998989898"
    assert candidate(number = "1122334455",digit = "1") == "122334455"
    assert candidate(number = "333333333",digit = "3") == "33333333"
    assert candidate(number = "1000000000",digit = "1") == "000000000"
    assert candidate(number = "9876543210",digit = "5") == "987643210"
    assert candidate(number = "12345654321",digit = "3") == "1245654321"
    assert candidate(number = "112233445566778899",digit = "5") == "11223344566778899"
    assert candidate(number = "100000000",digit = "0") == "10000000"
    assert candidate(number = "987987987",digit = "7") == "98987987"
    assert candidate(number = "101010101010",digit = "0") == "11010101010"
    assert candidate(number = "5959595959",digit = "9") == "595959595"
    assert candidate(number = "11223344556677889900",digit = "1") == "1223344556677889900"
    assert candidate(number = "987654321123456789987654321",digit = "3") == "98765432112456789987654321"
    assert candidate(number = "12345678901234567890",digit = "0") == "1234567891234567890"
    assert candidate(number = "122122122",digit = "2") == "12212212"
    assert candidate(number = "12345678901234567890",digit = "4") == "1235678901234567890"
    assert candidate(number = "123456789101112",digit = "1") == "23456789101112"
    assert candidate(number = "98765432109876543210",digit = "5") == "9876543210987643210"
    assert candidate(number = "11111111111111111111111111111111111111111111111111",digit = "1") == "1111111111111111111111111111111111111111111111111"
    assert candidate(number = "1919191919191919",digit = "9") == "191919191919191"
    assert candidate(number = "1000000001",digit = "0") == "100000001"
    assert candidate(number = "543219876",digit = "9") == "54321876"
    assert candidate(number = "56789101112131415161718192021",digit = "1") == "5678910112131415161718192021"
    assert candidate(number = "987654321987654321987654321987654321",digit = "8") == "98765432198765432198765432197654321"
    assert candidate(number = "123412341234",digit = "2") == "13412341234"
    assert candidate(number = "11223344556677889900",digit = "0") == "1122334455667788990"
    assert candidate(number = "12345678901234567890123456789012345678901234567890",digit = "0") == "1234567891234567890123456789012345678901234567890"
    assert candidate(number = "1919191919",digit = "9") == "191919191"
    assert candidate(number = "1919191919191919191919191919191919191919191919191",digit = "9") == "191919191919191919191919191919191919191919191911"
    assert candidate(number = "9999999999",digit = "9") == "999999999"
    assert candidate(number = "543219876987654321",digit = "9") == "54321987687654321"
    assert candidate(number = "987654321123456789",digit = "1") == "98765432123456789"
    assert candidate(number = "3131313131",digit = "1") == "331313131"
    assert candidate(number = "555555555555555555555",digit = "5") == "55555555555555555555"
    assert candidate(number = "123456789876543210987654321",digit = "9") == "12345678987654321087654321"
    assert candidate(number = "9999999999999999999",digit = "9") == "999999999999999999"
    assert candidate(number = "1212121212",digit = "2") == "121212121"
    assert candidate(number = "12345123451234512345",digit = "4") == "1235123451234512345"
    assert candidate(number = "91827364591827364591",digit = "1") == "9827364591827364591"
    assert candidate(number = "567567567",digit = "7") == "56756756"
    assert candidate(number = "999888777666555444333222111",digit = "9") == "99888777666555444333222111"
    assert candidate(number = "10000000001",digit = "0") == "1000000001"
    assert candidate(number = "876543210",digit = "0") == "87654321"
    assert candidate(number = "5645645645645645645645645645645645645645645645645",digit = "5") == "645645645645645645645645645645645645645645645645"
    assert candidate(number = "1234321",digit = "3") == "124321"
    assert candidate(number = "123456789123456789123456789",digit = "8") == "12345679123456789123456789"
    assert candidate(number = "123123123123123",digit = "1") == "23123123123123"
    assert candidate(number = "5656565656",digit = "5") == "656565656"
    assert candidate(number = "20202020202020202020202020202020202020202020202020",digit = "2") == "2020202020202020202020202020202020202020202020200"
    assert candidate(number = "2345678901234567890",digit = "0") == "234567891234567890"
    assert candidate(number = "918273645",digit = "9") == "18273645"
    assert candidate(number = "12233445566778899",digit = "9") == "1223344556677889"
    assert candidate(number = "5555555555555555555",digit = "5") == "555555555555555555"
    assert candidate(number = "101010101",digit = "0") == "11010101"
    assert candidate(number = "999999999999999999999",digit = "9") == "99999999999999999999"
    assert candidate(number = "8765432109876543210",digit = "5") == "876543210987643210"
    assert candidate(number = "33333333333333333333333333333333333333333333333333",digit = "3") == "3333333333333333333333333333333333333333333333333"
    assert candidate(number = "98765432109876543210",digit = "6") == "9876543210987543210"
    assert candidate(number = "100000000000000000000",digit = "0") == "10000000000000000000"
    assert candidate(number = "12345678901234567890",digit = "7") == "1234568901234567890"
    assert candidate(number = "3232323232323232",digit = "3") == "323232323232322"
    assert candidate(number = "123456789",digit = "2") == "13456789"
    assert candidate(number = "19191919191919191919",digit = "9") == "1919191919191919191"
    assert candidate(number = "123123123",digit = "1") == "23123123"
    assert candidate(number = "5645645645645645645645645645645645645645645645645",digit = "6") == "564564564564564564564564564564564564564564564545"
    assert candidate(number = "123987654321987654321987654321",digit = "9") == "12398765432198765432187654321"
    assert candidate(number = "1212121212121212121",digit = "2") == "121212121212121211"
    assert candidate(number = "123123123123123123123",digit = "3") == "12312312312312312312"
    assert candidate(number = "11111111111111111111",digit = "1") == "1111111111111111111"
    assert candidate(number = "112233445566778899",digit = "1") == "12233445566778899"
    assert candidate(number = "2222222222222222222222222222222",digit = "2") == "222222222222222222222222222222"
    assert candidate(number = "123987654321987654321987654321",digit = "1") == "23987654321987654321987654321"
    assert candidate(number = "987654321987654321",digit = "9") == "98765432187654321"
    assert candidate(number = "11111111111111111111111111111111111111111111",digit = "1") == "1111111111111111111111111111111111111111111"
    assert candidate(number = "9999999999999999999999999999999999999999999999999",digit = "9") == "999999999999999999999999999999999999999999999999"
    assert candidate(number = "111222333444555666777888999",digit = "3") == "11122233444555666777888999"
    assert candidate(number = "23333332",digit = "3") == "2333332"
    assert candidate(number = "22222222222222222222222222222222222222222222",digit = "2") == "2222222222222222222222222222222222222222222"
    assert candidate(number = "99999999991",digit = "9") == "9999999991"
    assert candidate(number = "333333",digit = "3") == "33333"
    assert candidate(number = "123456789123456789123456789",digit = "9") == "12345678912345678912345678"
    assert candidate(number = "123412341234",digit = "1") == "23412341234"
    assert candidate(number = "987654321123456789",digit = "9") == "98765432112345678"
    assert candidate(number = "543212345",digit = "2") == "54321345"
    assert candidate(number = "1111111111",digit = "1") == "111111111"
    assert candidate(number = "432143214321",digit = "2") == "43214321431"
    assert candidate(number = "12233445566778899",digit = "1") == "2233445566778899"
    assert candidate(number = "5555555555555555555555555555555555555555555555555",digit = "5") == "555555555555555555555555555555555555555555555555"
    assert candidate(number = "9876543210123456789",digit = "9") == "987654321012345678"
    assert candidate(number = "11112222",digit = "2") == "1111222"
    assert candidate(number = "31415926535",digit = "1") == "3415926535"
    assert candidate(number = "1234567890987654321",digit = "5") == "123467890987654321"
    assert candidate(number = "98877665544332211",digit = "8") == "9877665544332211"
    assert candidate(number = "1000000000",digit = "0") == "100000000"
    assert candidate(number = "2468135791113151719",digit = "1") == "246835791113151719"
    assert candidate(number = "12345678987654321",digit = "7") == "1234568987654321"


