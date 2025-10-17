def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = "5486",x = 7) == "75486"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "5486",x = 7) == "75486": {e}')
    
    total += 1
    try:
        result = candidate(n = "-11111",x = 1) == "-111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-11111",x = 1) == "-111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "-123456789",x = 5) == "-1234556789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-123456789",x = 5) == "-1234556789": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321",x = 5) == "9876554321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321",x = 5) == "9876554321": {e}')
    
    total += 1
    try:
        result = candidate(n = "-98765",x = 3) == "-398765"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-98765",x = 3) == "-398765": {e}')
    
    total += 1
    try:
        result = candidate(n = "-1000",x = 1) == "-10001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-1000",x = 1) == "-10001": {e}')
    
    total += 1
    try:
        result = candidate(n = "-987654321",x = 5) == "-5987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-987654321",x = 5) == "-5987654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "-54321",x = 4) == "-454321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-54321",x = 4) == "-454321": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789",x = 5) == "5123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789",x = 5) == "5123456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "5",x = 9) == "95"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "5",x = 9) == "95": {e}')
    
    total += 1
    try:
        result = candidate(n = "-1000",x = 5) == "-10005"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-1000",x = 5) == "-10005": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000",x = 1) == "11000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000",x = 1) == "11000": {e}')
    
    total += 1
    try:
        result = candidate(n = "54321",x = 6) == "654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "54321",x = 6) == "654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "12345",x = 3) == "312345"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12345",x = 3) == "312345": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000",x = 5) == "51000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000",x = 5) == "51000": {e}')
    
    total += 1
    try:
        result = candidate(n = "-973",x = 8) == "-8973"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-973",x = 8) == "-8973": {e}')
    
    total += 1
    try:
        result = candidate(n = "-13",x = 2) == "-123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-13",x = 2) == "-123": {e}')
    
    total += 1
    try:
        result = candidate(n = "54823",x = 7) == "754823"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "54823",x = 7) == "754823": {e}')
    
    total += 1
    try:
        result = candidate(n = "1",x = 1) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1",x = 1) == "11": {e}')
    
    total += 1
    try:
        result = candidate(n = "99",x = 9) == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "99",x = 9) == "999": {e}')
    
    total += 1
    try:
        result = candidate(n = "-64823",x = 7) == "-647823"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-64823",x = 7) == "-647823": {e}')
    
    total += 1
    try:
        result = candidate(n = "567",x = 8) == "8567"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "567",x = 8) == "8567": {e}')
    
    total += 1
    try:
        result = candidate(n = "-9",x = 1) == "-19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-9",x = 1) == "-19": {e}')
    
    total += 1
    try:
        result = candidate(n = "-9",x = 9) == "-99"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-9",x = 9) == "-99": {e}')
    
    total += 1
    try:
        result = candidate(n = "54893",x = 7) == "754893"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "54893",x = 7) == "754893": {e}')
    
    total += 1
    try:
        result = candidate(n = "-987",x = 7) == "-7987"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-987",x = 7) == "-7987": {e}')
    
    total += 1
    try:
        result = candidate(n = "-222222222",x = 2) == "-2222222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-222222222",x = 2) == "-2222222222": {e}')
    
    total += 1
    try:
        result = candidate(n = "1234567890",x = 0) == "12345678900"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234567890",x = 0) == "12345678900": {e}')
    
    total += 1
    try:
        result = candidate(n = "-1",x = 1) == "-11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-1",x = 1) == "-11": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000",x = 9) == "91000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000",x = 9) == "91000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = "123123123",x = 3) == "3123123123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123123123",x = 3) == "3123123123": {e}')
    
    total += 1
    try:
        result = candidate(n = "-101010101",x = 5) == "-1010101015"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-101010101",x = 5) == "-1010101015": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999",x = 1) == "9999999991"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999",x = 1) == "9999999991": {e}')
    
    total += 1
    try:
        result = candidate(n = "500000000",x = 5) == "5500000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "500000000",x = 5) == "5500000000": {e}')
    
    total += 1
    try:
        result = candidate(n = "555555555",x = 5) == "5555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "555555555",x = 5) == "5555555555": {e}')
    
    total += 1
    try:
        result = candidate(n = "-595959595",x = 5) == "-5595959595"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-595959595",x = 5) == "-5595959595": {e}')
    
    total += 1
    try:
        result = candidate(n = "-123456789",x = 3) == "-1233456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-123456789",x = 3) == "-1233456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "222222222",x = 1) == "2222222221"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "222222222",x = 1) == "2222222221": {e}')
    
    total += 1
    try:
        result = candidate(n = "876543210",x = 0) == "8765432100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "876543210",x = 0) == "8765432100": {e}')
    
    total += 1
    try:
        result = candidate(n = "192837465",x = 4) == "4192837465"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "192837465",x = 4) == "4192837465": {e}')
    
    total += 1
    try:
        result = candidate(n = "-900000000",x = 1) == "-1900000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-900000000",x = 1) == "-1900000000": {e}')
    
    total += 1
    try:
        result = candidate(n = "-999999999",x = 9) == "-9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-999999999",x = 9) == "-9999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "-9876543210",x = 1) == "-19876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-9876543210",x = 1) == "-19876543210": {e}')
    
    total += 1
    try:
        result = candidate(n = "-100000000",x = 0) == "-0100000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-100000000",x = 0) == "-0100000000": {e}')
    
    total += 1
    try:
        result = candidate(n = "9876543210",x = 9) == "99876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9876543210",x = 9) == "99876543210": {e}')
    
    total += 1
    try:
        result = candidate(n = "-5432109876",x = 9) == "-54321098769"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-5432109876",x = 9) == "-54321098769": {e}')
    
    total += 1
    try:
        result = candidate(n = "-123456789",x = 4) == "-1234456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-123456789",x = 4) == "-1234456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "-199999999",x = 9) == "-1999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-199999999",x = 9) == "-1999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "-101010101",x = 0) == "-0101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-101010101",x = 0) == "-0101010101": {e}')
    
    total += 1
    try:
        result = candidate(n = "-123123123",x = 5) == "-1231231235"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-123123123",x = 5) == "-1231231235": {e}')
    
    total += 1
    try:
        result = candidate(n = "199999999",x = 9) == "9199999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "199999999",x = 9) == "9199999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789",x = 9) == "9123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789",x = 9) == "9123456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "111111111",x = 2) == "2111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111111111",x = 2) == "2111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "53284769",x = 5) == "553284769"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "53284769",x = 5) == "553284769": {e}')
    
    total += 1
    try:
        result = candidate(n = "9876543210",x = 8) == "98876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9876543210",x = 8) == "98876543210": {e}')
    
    total += 1
    try:
        result = candidate(n = "1999999999",x = 0) == "19999999990"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1999999999",x = 0) == "19999999990": {e}')
    
    total += 1
    try:
        result = candidate(n = "9",x = 1) == "91"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9",x = 1) == "91": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321",x = 9) == "9987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321",x = 9) == "9987654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "111000111",x = 1) == "1111000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111000111",x = 1) == "1111000111": {e}')
    
    total += 1
    try:
        result = candidate(n = "-1000000000",x = 9) == "-10000000009"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-1000000000",x = 9) == "-10000000009": {e}')
    
    total += 1
    try:
        result = candidate(n = "-123456789",x = 1) == "-1123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-123456789",x = 1) == "-1123456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "54321",x = 3) == "543321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "54321",x = 3) == "543321": {e}')
    
    total += 1
    try:
        result = candidate(n = "-9999999999",x = 5) == "-59999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-9999999999",x = 5) == "-59999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "505050505",x = 5) == "5505050505"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "505050505",x = 5) == "5505050505": {e}')
    
    total += 1
    try:
        result = candidate(n = "121212121",x = 3) == "3121212121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "121212121",x = 3) == "3121212121": {e}')
    
    total += 1
    try:
        result = candidate(n = "123454321",x = 5) == "5123454321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123454321",x = 5) == "5123454321": {e}')
    
    total += 1
    try:
        result = candidate(n = "333333333",x = 3) == "3333333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "333333333",x = 3) == "3333333333": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321",x = 8) == "9887654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321",x = 8) == "9887654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "11111111111111111111",x = 2) == "211111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11111111111111111111",x = 2) == "211111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "-987654321",x = 1) == "-1987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-987654321",x = 1) == "-1987654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "-500000000",x = 5) == "-5000000005"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-500000000",x = 5) == "-5000000005": {e}')
    
    total += 1
    try:
        result = candidate(n = "-53284769",x = 5) == "-532584769"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-53284769",x = 5) == "-532584769": {e}')
    
    total += 1
    try:
        result = candidate(n = "101010101",x = 5) == "5101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "101010101",x = 5) == "5101010101": {e}')
    
    total += 1
    try:
        result = candidate(n = "-9876543210",x = 5) == "-59876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-9876543210",x = 5) == "-59876543210": {e}')
    
    total += 1
    try:
        result = candidate(n = "666666666",x = 5) == "6666666665"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "666666666",x = 5) == "6666666665": {e}')
    
    total += 1
    try:
        result = candidate(n = "111111111",x = 1) == "1111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111111111",x = 1) == "1111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "12345678901234567890",x = 5) == "512345678901234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12345678901234567890",x = 5) == "512345678901234567890": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321",x = 6) == "9876654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321",x = 6) == "9876654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "-123456789",x = 9) == "-1234567899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-123456789",x = 9) == "-1234567899": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789",x = 1) == "1234567891"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789",x = 1) == "1234567891": {e}')
    
    total += 1
    try:
        result = candidate(n = "-555555555",x = 6) == "-5555555556"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-555555555",x = 6) == "-5555555556": {e}')
    
    total += 1
    try:
        result = candidate(n = "-333333333",x = 2) == "-2333333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-333333333",x = 2) == "-2333333333": {e}')
    
    total += 1
    try:
        result = candidate(n = "595959595",x = 9) == "9595959595"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "595959595",x = 9) == "9595959595": {e}')
    
    total += 1
    try:
        result = candidate(n = "-54321",x = 6) == "-543216"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-54321",x = 6) == "-543216": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321",x = 7) == "9877654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321",x = 7) == "9877654321": {e}')
    
    total += 1
    try:
        result = candidate(n = "9",x = 9) == "99"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9",x = 9) == "99": {e}')
    
    total += 1
    try:
        result = candidate(n = "-86420",x = 1) == "-186420"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-86420",x = 1) == "-186420": {e}')
    
    total += 1
    try:
        result = candidate(n = "-111111111",x = 9) == "-1111111119"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-111111111",x = 9) == "-1111111119": {e}')
    
    total += 1
    try:
        result = candidate(n = "-54321",x = 3) == "-354321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-54321",x = 3) == "-354321": {e}')
    
    total += 1
    try:
        result = candidate(n = "-505050505",x = 5) == "-5050505055"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-505050505",x = 5) == "-5050505055": {e}')
    
    total += 1
    try:
        result = candidate(n = "-1000000001",x = 0) == "-01000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-1000000001",x = 0) == "-01000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000",x = 9) == "9100000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000",x = 9) == "9100000000": {e}')
    
    total += 1
    try:
        result = candidate(n = "-9876543210987654321",x = 9) == "-98765432109876543219"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-9876543210987654321",x = 9) == "-98765432109876543219": {e}')
    
    total += 1
    try:
        result = candidate(n = "333333333",x = 4) == "4333333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "333333333",x = 4) == "4333333333": {e}')
    
    total += 1
    try:
        result = candidate(n = "-2222222222",x = 1) == "-12222222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-2222222222",x = 1) == "-12222222222": {e}')
    
    total += 1
    try:
        result = candidate(n = "122222222",x = 2) == "2122222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "122222222",x = 2) == "2122222222": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789",x = 3) == "3123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789",x = 3) == "3123456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "-321321321",x = 2) == "-2321321321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-321321321",x = 2) == "-2321321321": {e}')
    
    total += 1
    try:
        result = candidate(n = "1122334455",x = 6) == "61122334455"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1122334455",x = 6) == "61122334455": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789",x = 6) == "6123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789",x = 6) == "6123456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "1111111111",x = 1) == "11111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1111111111",x = 1) == "11111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "-999999999",x = 1) == "-1999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-999999999",x = 1) == "-1999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "-333333333",x = 3) == "-3333333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-333333333",x = 3) == "-3333333333": {e}')
    
    total += 1
    try:
        result = candidate(n = "-1122334455",x = 3) == "-11223334455"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-1122334455",x = 3) == "-11223334455": {e}')
    
    total += 1
    try:
        result = candidate(n = "-9876543210",x = 8) == "-89876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-9876543210",x = 8) == "-89876543210": {e}')
    
    total += 1
    try:
        result = candidate(n = "98765432109876543210",x = 5) == "987655432109876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "98765432109876543210",x = 5) == "987655432109876543210": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789",x = 0) == "1234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789",x = 0) == "1234567890": {e}')
    
    total += 1
    try:
        result = candidate(n = "-12345678901234567890",x = 5) == "-123455678901234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-12345678901234567890",x = 5) == "-123455678901234567890": {e}')
    
    total += 1
    try:
        result = candidate(n = "1",x = 9) == "91"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1",x = 9) == "91": {e}')
    
    total += 1
    try:
        result = candidate(n = "-2000000000",x = 1) == "-12000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-2000000000",x = 1) == "-12000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = "11111",x = 1) == "111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11111",x = 1) == "111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000",x = 1) == "1100000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000",x = 1) == "1100000000": {e}')
    
    total += 1
    try:
        result = candidate(n = "1234567890",x = 5) == "51234567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234567890",x = 5) == "51234567890": {e}')
    
    total += 1
    try:
        result = candidate(n = "-999000999",x = 9) == "-9990009999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-999000999",x = 9) == "-9990009999": {e}')
    
    total += 1
    try:
        result = candidate(n = "1111111111",x = 2) == "21111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1111111111",x = 2) == "21111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "-876543210",x = 0) == "-0876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-876543210",x = 0) == "-0876543210": {e}')
    
    total += 1
    try:
        result = candidate(n = "-99999",x = 1) == "-199999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-99999",x = 1) == "-199999": {e}')
    
    total += 1
    try:
        result = candidate(n = "-10000",x = 0) == "-010000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-10000",x = 0) == "-010000": {e}')
    
    total += 1
    try:
        result = candidate(n = "555555555",x = 6) == "6555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "555555555",x = 6) == "6555555555": {e}')
    
    total += 1
    try:
        result = candidate(n = "-98765432109876543210",x = 5) == "-598765432109876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-98765432109876543210",x = 5) == "-598765432109876543210": {e}')
    
    total += 1
    try:
        result = candidate(n = "1999999999",x = 2) == "21999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1999999999",x = 2) == "21999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "123123123",x = 4) == "4123123123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123123123",x = 4) == "4123123123": {e}')
    
    total += 1
    try:
        result = candidate(n = "86420",x = 9) == "986420"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "86420",x = 9) == "986420": {e}')
    
    total += 1
    try:
        result = candidate(n = "-1",x = 9) == "-19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-1",x = 9) == "-19": {e}')
    
    total += 1
    try:
        result = candidate(n = "-1000000000",x = 1) == "-10000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-1000000000",x = 1) == "-10000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = "989898989",x = 7) == "9898989897"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "989898989",x = 7) == "9898989897": {e}')
    
    total += 1
    try:
        result = candidate(n = "-222222222",x = 3) == "-2222222223"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-222222222",x = 3) == "-2222222223": {e}')
    
    total += 1
    try:
        result = candidate(n = "192837465",x = 8) == "8192837465"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "192837465",x = 8) == "8192837465": {e}')
    
    total += 1
    try:
        result = candidate(n = "33333",x = 3) == "333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "33333",x = 3) == "333333": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000",x = 1) == "11000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000",x = 1) == "11000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789",x = 4) == "4123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789",x = 4) == "4123456789": {e}')
    
    total += 1
    try:
        result = candidate(n = "-123456789",x = 8) == "-1234567889"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "-123456789",x = 8) == "-1234567889": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999",x = 9) == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999",x = 9) == "9999999999": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = "5486",x = 7) == "75486"
    assert candidate(n = "-11111",x = 1) == "-111111"
    assert candidate(n = "-123456789",x = 5) == "-1234556789"
    assert candidate(n = "987654321",x = 5) == "9876554321"
    assert candidate(n = "-98765",x = 3) == "-398765"
    assert candidate(n = "-1000",x = 1) == "-10001"
    assert candidate(n = "-987654321",x = 5) == "-5987654321"
    assert candidate(n = "-54321",x = 4) == "-454321"
    assert candidate(n = "123456789",x = 5) == "5123456789"
    assert candidate(n = "5",x = 9) == "95"
    assert candidate(n = "-1000",x = 5) == "-10005"
    assert candidate(n = "1000",x = 1) == "11000"
    assert candidate(n = "54321",x = 6) == "654321"
    assert candidate(n = "12345",x = 3) == "312345"
    assert candidate(n = "1000",x = 5) == "51000"
    assert candidate(n = "-973",x = 8) == "-8973"
    assert candidate(n = "-13",x = 2) == "-123"
    assert candidate(n = "54823",x = 7) == "754823"
    assert candidate(n = "1",x = 1) == "11"
    assert candidate(n = "99",x = 9) == "999"
    assert candidate(n = "-64823",x = 7) == "-647823"
    assert candidate(n = "567",x = 8) == "8567"
    assert candidate(n = "-9",x = 1) == "-19"
    assert candidate(n = "-9",x = 9) == "-99"
    assert candidate(n = "54893",x = 7) == "754893"
    assert candidate(n = "-987",x = 7) == "-7987"
    assert candidate(n = "-222222222",x = 2) == "-2222222222"
    assert candidate(n = "1234567890",x = 0) == "12345678900"
    assert candidate(n = "-1",x = 1) == "-11"
    assert candidate(n = "1000000000",x = 9) == "91000000000"
    assert candidate(n = "123123123",x = 3) == "3123123123"
    assert candidate(n = "-101010101",x = 5) == "-1010101015"
    assert candidate(n = "999999999",x = 1) == "9999999991"
    assert candidate(n = "500000000",x = 5) == "5500000000"
    assert candidate(n = "555555555",x = 5) == "5555555555"
    assert candidate(n = "-595959595",x = 5) == "-5595959595"
    assert candidate(n = "-123456789",x = 3) == "-1233456789"
    assert candidate(n = "222222222",x = 1) == "2222222221"
    assert candidate(n = "876543210",x = 0) == "8765432100"
    assert candidate(n = "192837465",x = 4) == "4192837465"
    assert candidate(n = "-900000000",x = 1) == "-1900000000"
    assert candidate(n = "-999999999",x = 9) == "-9999999999"
    assert candidate(n = "-9876543210",x = 1) == "-19876543210"
    assert candidate(n = "-100000000",x = 0) == "-0100000000"
    assert candidate(n = "9876543210",x = 9) == "99876543210"
    assert candidate(n = "-5432109876",x = 9) == "-54321098769"
    assert candidate(n = "-123456789",x = 4) == "-1234456789"
    assert candidate(n = "-199999999",x = 9) == "-1999999999"
    assert candidate(n = "-101010101",x = 0) == "-0101010101"
    assert candidate(n = "-123123123",x = 5) == "-1231231235"
    assert candidate(n = "199999999",x = 9) == "9199999999"
    assert candidate(n = "123456789",x = 9) == "9123456789"
    assert candidate(n = "111111111",x = 2) == "2111111111"
    assert candidate(n = "53284769",x = 5) == "553284769"
    assert candidate(n = "9876543210",x = 8) == "98876543210"
    assert candidate(n = "1999999999",x = 0) == "19999999990"
    assert candidate(n = "9",x = 1) == "91"
    assert candidate(n = "987654321",x = 9) == "9987654321"
    assert candidate(n = "111000111",x = 1) == "1111000111"
    assert candidate(n = "-1000000000",x = 9) == "-10000000009"
    assert candidate(n = "-123456789",x = 1) == "-1123456789"
    assert candidate(n = "54321",x = 3) == "543321"
    assert candidate(n = "-9999999999",x = 5) == "-59999999999"
    assert candidate(n = "505050505",x = 5) == "5505050505"
    assert candidate(n = "121212121",x = 3) == "3121212121"
    assert candidate(n = "123454321",x = 5) == "5123454321"
    assert candidate(n = "333333333",x = 3) == "3333333333"
    assert candidate(n = "987654321",x = 8) == "9887654321"
    assert candidate(n = "11111111111111111111",x = 2) == "211111111111111111111"
    assert candidate(n = "-987654321",x = 1) == "-1987654321"
    assert candidate(n = "-500000000",x = 5) == "-5000000005"
    assert candidate(n = "-53284769",x = 5) == "-532584769"
    assert candidate(n = "101010101",x = 5) == "5101010101"
    assert candidate(n = "-9876543210",x = 5) == "-59876543210"
    assert candidate(n = "666666666",x = 5) == "6666666665"
    assert candidate(n = "111111111",x = 1) == "1111111111"
    assert candidate(n = "12345678901234567890",x = 5) == "512345678901234567890"
    assert candidate(n = "987654321",x = 6) == "9876654321"
    assert candidate(n = "-123456789",x = 9) == "-1234567899"
    assert candidate(n = "123456789",x = 1) == "1234567891"
    assert candidate(n = "-555555555",x = 6) == "-5555555556"
    assert candidate(n = "-333333333",x = 2) == "-2333333333"
    assert candidate(n = "595959595",x = 9) == "9595959595"
    assert candidate(n = "-54321",x = 6) == "-543216"
    assert candidate(n = "987654321",x = 7) == "9877654321"
    assert candidate(n = "9",x = 9) == "99"
    assert candidate(n = "-86420",x = 1) == "-186420"
    assert candidate(n = "-111111111",x = 9) == "-1111111119"
    assert candidate(n = "-54321",x = 3) == "-354321"
    assert candidate(n = "-505050505",x = 5) == "-5050505055"
    assert candidate(n = "-1000000001",x = 0) == "-01000000001"
    assert candidate(n = "100000000",x = 9) == "9100000000"
    assert candidate(n = "-9876543210987654321",x = 9) == "-98765432109876543219"
    assert candidate(n = "333333333",x = 4) == "4333333333"
    assert candidate(n = "-2222222222",x = 1) == "-12222222222"
    assert candidate(n = "122222222",x = 2) == "2122222222"
    assert candidate(n = "123456789",x = 3) == "3123456789"
    assert candidate(n = "-321321321",x = 2) == "-2321321321"
    assert candidate(n = "1122334455",x = 6) == "61122334455"
    assert candidate(n = "123456789",x = 6) == "6123456789"
    assert candidate(n = "1111111111",x = 1) == "11111111111"
    assert candidate(n = "-999999999",x = 1) == "-1999999999"
    assert candidate(n = "-333333333",x = 3) == "-3333333333"
    assert candidate(n = "-1122334455",x = 3) == "-11223334455"
    assert candidate(n = "-9876543210",x = 8) == "-89876543210"
    assert candidate(n = "98765432109876543210",x = 5) == "987655432109876543210"
    assert candidate(n = "123456789",x = 0) == "1234567890"
    assert candidate(n = "-12345678901234567890",x = 5) == "-123455678901234567890"
    assert candidate(n = "1",x = 9) == "91"
    assert candidate(n = "-2000000000",x = 1) == "-12000000000"
    assert candidate(n = "11111",x = 1) == "111111"
    assert candidate(n = "100000000",x = 1) == "1100000000"
    assert candidate(n = "1234567890",x = 5) == "51234567890"
    assert candidate(n = "-999000999",x = 9) == "-9990009999"
    assert candidate(n = "1111111111",x = 2) == "21111111111"
    assert candidate(n = "-876543210",x = 0) == "-0876543210"
    assert candidate(n = "-99999",x = 1) == "-199999"
    assert candidate(n = "-10000",x = 0) == "-010000"
    assert candidate(n = "555555555",x = 6) == "6555555555"
    assert candidate(n = "-98765432109876543210",x = 5) == "-598765432109876543210"
    assert candidate(n = "1999999999",x = 2) == "21999999999"
    assert candidate(n = "123123123",x = 4) == "4123123123"
    assert candidate(n = "86420",x = 9) == "986420"
    assert candidate(n = "-1",x = 9) == "-19"
    assert candidate(n = "-1000000000",x = 1) == "-10000000001"
    assert candidate(n = "989898989",x = 7) == "9898989897"
    assert candidate(n = "-222222222",x = 3) == "-2222222223"
    assert candidate(n = "192837465",x = 8) == "8192837465"
    assert candidate(n = "33333",x = 3) == "333333"
    assert candidate(n = "1000000000",x = 1) == "11000000000"
    assert candidate(n = "123456789",x = 4) == "4123456789"
    assert candidate(n = "-123456789",x = 8) == "-1234567889"
    assert candidate(n = "999999999",x = 9) == "9999999999"


