def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "473289651",k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "473289651",k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "2222222222222222222",k = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2222222222222222222",k = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321",k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321",k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "999",k = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "999",k = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "999999999",k = 999999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "999999999",k = 999999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "999999999",k = 1000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "999999999",k = 1000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "47328165",k = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "47328165",k = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "99999",k = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "99999",k = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111",k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111",k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321",k = 987654321) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321",k = 987654321) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789",k = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789",k = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "9",k = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9",k = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "823847291",k = 823) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "823847291",k = 823) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "456",k = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "456",k = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "555555555",k = 55) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "555555555",k = 55) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111",k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111",k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321",k = 50) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321",k = 50) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "238182",k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "238182",k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "123",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "165462",k = 60) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "165462",k = 60) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789101112131415",k = 1000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789101112131415",k = 1000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "88888888888888888888",k = 888) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "88888888888888888888",k = 888) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111",k = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111",k = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "8888888888888888888888888888888888",k = 1000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "8888888888888888888888888888888888",k = 1000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567891011121314151617181920",k = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567891011121314151617181920",k = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789",k = 987654321) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789",k = 987654321) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1919191919191919191919191919191919191919191919",k = 19) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1919191919191919191919191919191919191919191919",k = 19) == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321",k = 250) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321",k = 250) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789987654321",k = 9999) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789987654321",k = 9999) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "5678956789567895678956789",k = 10000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5678956789567895678956789",k = 10000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "12345678901234567890123456789012345678901234567890",k = 123456789) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12345678901234567890123456789012345678901234567890",k = 123456789) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "9999999999999999999",k = 1000000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9999999999999999999",k = 1000000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "1212121212121212121",k = 12) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1212121212121212121",k = 12) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "123123123123123123123123123123123123123123123123",k = 123) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123123123123123123123123123123123123123123123123",k = 123) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "876543219876543219",k = 50000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "876543219876543219",k = 50000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "5555555555555555555555555555555",k = 555) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5555555555555555555555555555555",k = 555) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "9999999999999999999",k = 999999999) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9999999999999999999",k = 999999999) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "1",k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1",k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "77777777777777777777777777777777777777777777",k = 777777) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "77777777777777777777777777777777777777777777",k = 777777) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "9999999999999999999",k = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9999999999999999999",k = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "135792468",k = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "135792468",k = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321123456789987654321",k = 98765) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321123456789987654321",k = 98765) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "99999999999999999999999999999999999999999999",k = 999999999) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "99999999999999999999999999999999999999999999",k = 999999999) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "33333333333333333333333333333333333333333333",k = 333) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "33333333333333333333333333333333333333333333",k = 333) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "102030405060708090",k = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "102030405060708090",k = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",k = 10) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",k = 10) == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789987654321",k = 123456789) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789987654321",k = 123456789) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321",k = 987654320) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321",k = 987654320) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789123456789123456789",k = 123456789) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789123456789123456789",k = 123456789) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "7777777777777777777",k = 50) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7777777777777777777",k = 50) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",k = 999999999) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",k = 999999999) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "246813579",k = 1000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "246813579",k = 1000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "19191919191919191919",k = 19) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "19191919191919191919",k = 19) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "3333333333333333333",k = 33333) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3333333333333333333",k = 33333) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "3333333333333333333",k = 333) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3333333333333333333",k = 333) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "55555555555555555555555555555555555555555555",k = 55555) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "55555555555555555555555555555555555555555555",k = 55555) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "3333333333333333333333333333333333",k = 33) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3333333333333333333333333333333333",k = 33) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "321321321321321321321",k = 321) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "321321321321321321321",k = 321) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "111222333444555666777888999",k = 333) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111222333444555666777888999",k = 333) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "1357924680135792468",k = 1000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1357924680135792468",k = 1000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567891011121314151617181920",k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567891011121314151617181920",k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111",k = 1) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111",k = 1) == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "87654321",k = 543) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "87654321",k = 543) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321",k = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321",k = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "505050505050505050505050505050505050505050505050",k = 505) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "505050505050505050505050505050505050505050505050",k = 505) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "91827364510987654321",k = 1000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "91827364510987654321",k = 1000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789123456789123456789123456789123456789",k = 123456789) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789123456789123456789123456789123456789",k = 123456789) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890123456789",k = 123456789) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890123456789",k = 123456789) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "88888888888888888888888888888888888888888888",k = 88888888) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "88888888888888888888888888888888888888888888",k = 88888888) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "99999999999999999999",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "99999999999999999999",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "135792468",k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "135792468",k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111",k = 1) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111",k = 1) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111",k = 1) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111",k = 1) == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",k = 111) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",k = 111) == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567890987654321",k = 12345) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567890987654321",k = 12345) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "9999999999999999999",k = 1000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9999999999999999999",k = 1000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "1231231231231231231",k = 123123) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1231231231231231231",k = 123123) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1919191919191919191919191919191919191919191919",k = 20) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1919191919191919191919191919191919191919191919",k = 20) == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "99999999999999999999",k = 999999999) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "99999999999999999999",k = 999999999) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101",k = 101) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101",k = 101) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321987654321987654321987654321987654321",k = 987654321) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321987654321987654321987654321987654321",k = 987654321) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "98765432109876543210987654321098765432109876543210",k = 987654321) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "98765432109876543210987654321098765432109876543210",k = 987654321) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "9283746554321",k = 10000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9283746554321",k = 10000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789",k = 123456789) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789",k = 123456789) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "99999999999999999999999999999999999999999999999",k = 999999999) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "99999999999999999999999999999999999999999999999",k = 999999999) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567891011121314151617181920",k = 150) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567891011121314151617181920",k = 150) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321",k = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321",k = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "55555555555555555555555555555555555555555555555",k = 60) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "55555555555555555555555555555555555555555555555",k = 60) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789",k = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789",k = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "987654321",k = 999999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "987654321",k = 999999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1999999999999999999999999999999999",k = 1000000000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1999999999999999999999999999999999",k = 1000000000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567891011121314151617181920",k = 100) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567891011121314151617181920",k = 100) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "77777777777777777777777777777777777777777777777",k = 77) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "77777777777777777777777777777777777777777777777",k = 77) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789",k = 89) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789",k = 89) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "3333333333333333333",k = 33) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3333333333333333333",k = 33) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789",k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789",k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "8888888888888888888",k = 9) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "8888888888888888888",k = 9) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789123456789",k = 1000000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789123456789",k = 1000000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111",k = 111111111) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111",k = 111111111) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "246813579",k = 250) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "246813579",k = 250) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "123456789101112131415",k = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123456789101112131415",k = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "98765432187654321",k = 1000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "98765432187654321",k = 1000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1234567891011121314151617181920",k = 99) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1234567891011121314151617181920",k = 99) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555",k = 555) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555",k = 555) == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "54321",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "54321",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "543215432154321",k = 543) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "543215432154321",k = 543) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "9876543210987654321",k = 100000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "9876543210987654321",k = 100000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "112233445566778899112233445566778899112233",k = 112233) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "112233445566778899112233445566778899112233",k = 112233) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "473289651",k = 10) == 9
    assert candidate(s = "2222222222222222222",k = 2) == 19
    assert candidate(s = "987654321",k = 10) == 9
    assert candidate(s = "999",k = 1000) == 1
    assert candidate(s = "999999999",k = 999999999) == 1
    assert candidate(s = "999999999",k = 1000) == 3
    assert candidate(s = "47328165",k = 100) == 4
    assert candidate(s = "99999",k = 100000) == 1
    assert candidate(s = "1",k = 1) == 1
    assert candidate(s = "1111111111",k = 1) == 10
    assert candidate(s = "987654321",k = 987654321) == 1
    assert candidate(s = "123456789",k = 9) == 9
    assert candidate(s = "9",k = 8) == -1
    assert candidate(s = "823847291",k = 823) == 4
    assert candidate(s = "456",k = 100) == 2
    assert candidate(s = "555555555",k = 55) == 5
    assert candidate(s = "111111111",k = 1) == 9
    assert candidate(s = "987654321",k = 50) == 7
    assert candidate(s = "238182",k = 5) == -1
    assert candidate(s = "123",k = 3) == 3
    assert candidate(s = "165462",k = 60) == 4
    assert candidate(s = "123456789101112131415",k = 1000) == 7
    assert candidate(s = "88888888888888888888",k = 888) == 7
    assert candidate(s = "11111111111111111111",k = 11) == 10
    assert candidate(s = "8888888888888888888888888888888888",k = 1000) == 12
    assert candidate(s = "1234567891011121314151617181920",k = 10) == 30
    assert candidate(s = "123456789",k = 987654321) == 1
    assert candidate(s = "1919191919191919191919191919191919191919191919",k = 19) == 23
    assert candidate(s = "987654321",k = 250) == 5
    assert candidate(s = "123456789987654321",k = 9999) == 5
    assert candidate(s = "5678956789567895678956789",k = 10000) == 7
    assert candidate(s = "12345678901234567890123456789012345678901234567890",k = 123456789) == 6
    assert candidate(s = "9999999999999999999",k = 1000000000) == 3
    assert candidate(s = "1212121212121212121",k = 12) == 10
    assert candidate(s = "123123123123123123123123123123123123123123123123",k = 123) == 16
    assert candidate(s = "876543219876543219",k = 50000) == 4
    assert candidate(s = "5555555555555555555555555555555",k = 555) == 11
    assert candidate(s = "9999999999999999999",k = 999999999) == 3
    assert candidate(s = "1",k = 9) == 1
    assert candidate(s = "77777777777777777777777777777777777777777777",k = 777777) == 8
    assert candidate(s = "9999999999999999999",k = 10) == 19
    assert candidate(s = "135792468",k = 100) == 5
    assert candidate(s = "987654321123456789987654321",k = 98765) == 6
    assert candidate(s = "99999999999999999999999999999999999999999999",k = 999999999) == 5
    assert candidate(s = "33333333333333333333333333333333333333333333",k = 333) == 15
    assert candidate(s = "102030405060708090",k = 100) == 9
    assert candidate(s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",k = 10) == 99
    assert candidate(s = "123456789987654321",k = 123456789) == 3
    assert candidate(s = "987654321",k = 987654320) == 2
    assert candidate(s = "123456789123456789123456789",k = 123456789) == 3
    assert candidate(s = "7777777777777777777",k = 50) == 19
    assert candidate(s = "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",k = 999999999) == 12
    assert candidate(s = "246813579",k = 1000) == 3
    assert candidate(s = "19191919191919191919",k = 19) == 10
    assert candidate(s = "3333333333333333333",k = 33333) == 4
    assert candidate(s = "3333333333333333333",k = 333) == 7
    assert candidate(s = "55555555555555555555555555555555555555555555",k = 55555) == 9
    assert candidate(s = "3333333333333333333333333333333333",k = 33) == 17
    assert candidate(s = "321321321321321321321",k = 321) == 7
    assert candidate(s = "111222333444555666777888999",k = 333) == 12
    assert candidate(s = "1357924680135792468",k = 1000) == 6
    assert candidate(s = "1234567891011121314151617181920",k = 1) == -1
    assert candidate(s = "1111111111111111111111111111111111111111111111",k = 1) == 46
    assert candidate(s = "87654321",k = 543) == 4
    assert candidate(s = "987654321",k = 100) == 5
    assert candidate(s = "505050505050505050505050505050505050505050505050",k = 505) == 13
    assert candidate(s = "91827364510987654321",k = 1000) == 7
    assert candidate(s = "123456789123456789123456789123456789123456789",k = 123456789) == 5
    assert candidate(s = "1234567890123456789",k = 123456789) == 2
    assert candidate(s = "88888888888888888888888888888888888888888888",k = 88888888) == 6
    assert candidate(s = "99999999999999999999",k = 10) == 20
    assert candidate(s = "135792468",k = 10) == 9
    assert candidate(s = "1111111111111111111",k = 1) == 19
    assert candidate(s = "111111111111111111111111111111111111111111111111",k = 1) == 48
    assert candidate(s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",k = 111) == 33
    assert candidate(s = "1234567890987654321",k = 12345) == 5
    assert candidate(s = "9999999999999999999",k = 1000) == 7
    assert candidate(s = "1231231231231231231",k = 123123) == 4
    assert candidate(s = "1919191919191919191919191919191919191919191919",k = 20) == 23
    assert candidate(s = "99999999999999999999",k = 999999999) == 3
    assert candidate(s = "1010101010101010101",k = 101) == 5
    assert candidate(s = "987654321987654321987654321987654321987654321",k = 987654321) == 5
    assert candidate(s = "98765432109876543210987654321098765432109876543210",k = 987654321) == 6
    assert candidate(s = "9283746554321",k = 10000) == 4
    assert candidate(s = "123456789",k = 123456789) == 1
    assert candidate(s = "99999999999999999999999999999999999999999999999",k = 999999999) == 6
    assert candidate(s = "1234567891011121314151617181920",k = 150) == 14
    assert candidate(s = "987654321",k = 500) == 4
    assert candidate(s = "55555555555555555555555555555555555555555555555",k = 60) == 24
    assert candidate(s = "123456789",k = 8) == -1
    assert candidate(s = "987654321",k = 999999999) == 1
    assert candidate(s = "1999999999999999999999999999999999",k = 1000000000) == 4
    assert candidate(s = "1234567891011121314151617181920",k = 100) == 15
    assert candidate(s = "77777777777777777777777777777777777777777777777",k = 77) == 24
    assert candidate(s = "123456789",k = 89) == 5
    assert candidate(s = "3333333333333333333",k = 33) == 10
    assert candidate(s = "123456789",k = 5) == -1
    assert candidate(s = "8888888888888888888",k = 9) == 19
    assert candidate(s = "123456789123456789",k = 1000000000) == 2
    assert candidate(s = "11111111111111111111111111111111111111111111",k = 111111111) == 5
    assert candidate(s = "246813579",k = 250) == 4
    assert candidate(s = "123456789101112131415",k = 100) == 10
    assert candidate(s = "98765432187654321",k = 1000) == 6
    assert candidate(s = "1234567891011121314151617181920",k = 99) == 15
    assert candidate(s = "55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555",k = 555) == 33
    assert candidate(s = "54321",k = 5) == 5
    assert candidate(s = "543215432154321",k = 543) == 5
    assert candidate(s = "9876543210987654321",k = 100000) == 4
    assert candidate(s = "112233445566778899112233445566778899112233",k = 112233) == 8


