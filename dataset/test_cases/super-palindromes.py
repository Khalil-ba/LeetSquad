def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(left = "1000000000",right = "1000000000000000000") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000",right = "1000000000000000000") == 49: {e}')
    
    total += 1
    try:
        result = candidate(left = "123",right = "456") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "123",right = "456") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "50",right = "10000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "50",right = "10000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(left = "4",right = "1000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "4",right = "1000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = "1",right = "2") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1",right = "2") == 1: {e}')
    
    total += 1
    try:
        result = candidate(left = "123",right = "456789") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "123",right = "456789") == 6: {e}')
    
    total += 1
    try:
        result = candidate(left = "100",right = "1000000") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100",right = "1000000") == 7: {e}')
    
    total += 1
    try:
        result = candidate(left = "1",right = "100000000000000000") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1",right = "100000000000000000") == 70: {e}')
    
    total += 1
    try:
        result = candidate(left = "9",right = "9") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "9",right = "9") == 1: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000000000000",right = "999999999999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000000000000",right = "999999999999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "50",right = "1000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "50",right = "1000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(left = "999999999999999999",right = "999999999999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "999999999999999999",right = "999999999999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000",right = "1000000000000000000") == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000",right = "1000000000000000000") == 57: {e}')
    
    total += 1
    try:
        result = candidate(left = "10",right = "100") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "10",right = "100") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "123456789",right = "987654321") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "123456789",right = "987654321") == 3: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000000000000",right = "1000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000000000000",right = "1000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "987654321",right = "987654321987654321") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "987654321",right = "987654321987654321") == 49: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000",right = "10000000000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000",right = "10000000000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(left = "800000000000000000",right = "888888888888888888") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "800000000000000000",right = "888888888888888888") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "987654321098765432",right = "999999999999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "987654321098765432",right = "999999999999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000000",right = "2000000000000") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000000",right = "2000000000000") == 11: {e}')
    
    total += 1
    try:
        result = candidate(left = "12345678987654321",right = "12345678987654321") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "12345678987654321",right = "12345678987654321") == 1: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000000000",right = "1000000000000000") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000000000",right = "1000000000000000") == 9: {e}')
    
    total += 1
    try:
        result = candidate(left = "1",right = "1000000000000000000") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1",right = "1000000000000000000") == 70: {e}')
    
    total += 1
    try:
        result = candidate(left = "123456789012345678",right = "876543210987654321") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "123456789012345678",right = "876543210987654321") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000",right = "1234567890123456789") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000",right = "1234567890123456789") == 64: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000000000000",right = "2000000000000000000") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000000000000",right = "2000000000000000000") == 15: {e}')
    
    total += 1
    try:
        result = candidate(left = "12345678987654321",right = "98765432123456789") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "12345678987654321",right = "98765432123456789") == 3: {e}')
    
    total += 1
    try:
        result = candidate(left = "2000000000",right = "3000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "2000000000",right = "3000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "500000000000000000",right = "555555555555555555") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "500000000000000000",right = "555555555555555555") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "12345678987654321",right = "12345678987654321987654321987654321") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "12345678987654321",right = "12345678987654321987654321987654321") == 21: {e}')
    
    total += 1
    try:
        result = candidate(left = "333333333333333333",right = "444444444444444444") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "333333333333333333",right = "444444444444444444") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "900000000000000000",right = "999999999999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "900000000000000000",right = "999999999999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "9007199254740992",right = "900719925474099200") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "9007199254740992",right = "900719925474099200") == 22: {e}')
    
    total += 1
    try:
        result = candidate(left = "8765432101234567876543210",right = "987654321123456789876543210") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "8765432101234567876543210",right = "987654321123456789876543210") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "10000000000",right = "100000000000000000") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "10000000000",right = "100000000000000000") == 49: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000000",right = "9999999999999") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000000",right = "9999999999999") == 13: {e}')
    
    total += 1
    try:
        result = candidate(left = "500000000",right = "600000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "500000000",right = "600000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "499",right = "501") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "499",right = "501") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "123",right = "123456789012345678") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "123",right = "123456789012345678") == 66: {e}')
    
    total += 1
    try:
        result = candidate(left = "1",right = "999999999999999999") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1",right = "999999999999999999") == 70: {e}')
    
    total += 1
    try:
        result = candidate(left = "99999999999999998",right = "999999999999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "99999999999999998",right = "999999999999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "999999999",right = "10000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "999999999",right = "10000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "9876543210",right = "9876543210987654321") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "9876543210",right = "9876543210987654321") == 65: {e}')
    
    total += 1
    try:
        result = candidate(left = "9876543210123456789",right = "9876543210123456789") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "9876543210123456789",right = "9876543210123456789") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "98000000000000000",right = "98100000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "98000000000000000",right = "98100000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "888888888888888888",right = "999999999999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "888888888888888888",right = "999999999999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "123456789123456789",right = "987654321987654321") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "123456789123456789",right = "987654321987654321") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000000000",right = "110000000000000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000000000",right = "110000000000000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = "50000000000",right = "60000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "50000000000",right = "60000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "12321",right = "98789") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "12321",right = "98789") == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = "9223372036854775807",right = "9223372036854775808") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "9223372036854775807",right = "9223372036854775808") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "111111111",right = "222222222") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "111111111",right = "222222222") == 3: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000000000000",right = "18446744073709551615") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000000000000",right = "18446744073709551615") == 16: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000000000000",right = "100000000000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000000000000",right = "100000000000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "99999999999999999",right = "1000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "99999999999999999",right = "1000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "987654321",right = "987654321012345678") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "987654321",right = "987654321012345678") == 49: {e}')
    
    total += 1
    try:
        result = candidate(left = "999999999999999999",right = "1000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "999999999999999999",right = "1000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000",right = "100000000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000",right = "100000000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000000000",right = "1000000000000000000") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000000000",right = "1000000000000000000") == 31: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000000000000",right = "9999999999999999999") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000000000000",right = "9999999999999999999") == 16: {e}')
    
    total += 1
    try:
        result = candidate(left = "10000",right = "100000000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "10000",right = "100000000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(left = "10000000000",right = "11000000000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "10000000000",right = "11000000000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(left = "3000000000000",right = "4000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "3000000000000",right = "4000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "123456789012345678",right = "987654321098765432") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "123456789012345678",right = "987654321098765432") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000000000000",right = "1000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000000000000",right = "1000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "123",right = "12345678987654321") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "123",right = "12345678987654321") == 64: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000",right = "999999999999999999") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000",right = "999999999999999999") == 49: {e}')
    
    total += 1
    try:
        result = candidate(left = "1234567891011121314",right = "15161718192021222324") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1234567891011121314",right = "15161718192021222324") == 1: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000000000000",right = "900000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000000000000",right = "900000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000",right = "1000000000000") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000",right = "1000000000000") == 5: {e}')
    
    total += 1
    try:
        result = candidate(left = "7000000000000000000",right = "8000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "7000000000000000000",right = "8000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000000000000",right = "1000000000000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000000000000",right = "1000000000000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000000",right = "9999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000000",right = "9999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "50000000000000000",right = "60000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "50000000000000000",right = "60000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "555555555555555555",right = "666666666666666666") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "555555555555555555",right = "666666666666666666") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "10000000000000000",right = "1000000000000000000") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "10000000000000000",right = "1000000000000000000") == 22: {e}')
    
    total += 1
    try:
        result = candidate(left = "100000000000000000",right = "18014398509481983") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "100000000000000000",right = "18014398509481983") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "111111111",right = "999999999999999") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "111111111",right = "999999999999999") == 32: {e}')
    
    total += 1
    try:
        result = candidate(left = "800000000000000000",right = "899999999999999999") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "800000000000000000",right = "899999999999999999") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "111111111111111111",right = "222222222222222222") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "111111111111111111",right = "222222222222222222") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "500000000000000000",right = "600000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "500000000000000000",right = "600000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "484",right = "576") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "484",right = "576") == 1: {e}')
    
    total += 1
    try:
        result = candidate(left = "999999999999999",right = "999999999999999999") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "999999999999999",right = "999999999999999999") == 22: {e}')
    
    total += 1
    try:
        result = candidate(left = "80000000000",right = "90000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "80000000000",right = "90000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(left = "1000000",right = "1000000000") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = "1000000",right = "1000000000") == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(left = "1000000000",right = "1000000000000000000") == 49
    assert candidate(left = "123",right = "456") == 0
    assert candidate(left = "50",right = "10000") == 2
    assert candidate(left = "4",right = "1000") == 4
    assert candidate(left = "1",right = "2") == 1
    assert candidate(left = "123",right = "456789") == 6
    assert candidate(left = "100",right = "1000000") == 7
    assert candidate(left = "1",right = "100000000000000000") == 70
    assert candidate(left = "9",right = "9") == 1
    assert candidate(left = "100000000000000000",right = "999999999999999999") == 0
    assert candidate(left = "50",right = "1000") == 2
    assert candidate(left = "999999999999999999",right = "999999999999999999") == 0
    assert candidate(left = "100000000",right = "1000000000000000000") == 57
    assert candidate(left = "10",right = "100") == 0
    assert candidate(left = "123456789",right = "987654321") == 3
    assert candidate(left = "100000000000000000",right = "1000000000000000000") == 0
    assert candidate(left = "987654321",right = "987654321987654321") == 49
    assert candidate(left = "100000000",right = "10000000000") == 8
    assert candidate(left = "800000000000000000",right = "888888888888888888") == 0
    assert candidate(left = "987654321098765432",right = "999999999999999999") == 0
    assert candidate(left = "1000000000000",right = "2000000000000") == 11
    assert candidate(left = "12345678987654321",right = "12345678987654321") == 1
    assert candidate(left = "100000000000000",right = "1000000000000000") == 9
    assert candidate(left = "1",right = "1000000000000000000") == 70
    assert candidate(left = "123456789012345678",right = "876543210987654321") == 0
    assert candidate(left = "1000000000",right = "1234567890123456789") == 64
    assert candidate(left = "1000000000000000000",right = "2000000000000000000") == 15
    assert candidate(left = "12345678987654321",right = "98765432123456789") == 3
    assert candidate(left = "2000000000",right = "3000000000") == 0
    assert candidate(left = "500000000000000000",right = "555555555555555555") == 0
    assert candidate(left = "12345678987654321",right = "12345678987654321987654321987654321") == 21
    assert candidate(left = "333333333333333333",right = "444444444444444444") == 0
    assert candidate(left = "900000000000000000",right = "999999999999999999") == 0
    assert candidate(left = "9007199254740992",right = "900719925474099200") == 22
    assert candidate(left = "8765432101234567876543210",right = "987654321123456789876543210") == 0
    assert candidate(left = "10000000000",right = "100000000000000000") == 49
    assert candidate(left = "1000000000000",right = "9999999999999") == 13
    assert candidate(left = "500000000",right = "600000000") == 0
    assert candidate(left = "499",right = "501") == 0
    assert candidate(left = "123",right = "123456789012345678") == 66
    assert candidate(left = "1",right = "999999999999999999") == 70
    assert candidate(left = "99999999999999998",right = "999999999999999999") == 0
    assert candidate(left = "999999999",right = "10000000000") == 0
    assert candidate(left = "9876543210",right = "9876543210987654321") == 65
    assert candidate(left = "9876543210123456789",right = "9876543210123456789") == 0
    assert candidate(left = "98000000000000000",right = "98100000000000000") == 0
    assert candidate(left = "888888888888888888",right = "999999999999999999") == 0
    assert candidate(left = "123456789123456789",right = "987654321987654321") == 0
    assert candidate(left = "100000000000000",right = "110000000000000") == 4
    assert candidate(left = "50000000000",right = "60000000000") == 0
    assert candidate(left = "12321",right = "98789") == 4
    assert candidate(left = "9223372036854775807",right = "9223372036854775808") == 0
    assert candidate(left = "111111111",right = "222222222") == 3
    assert candidate(left = "100000000000000000",right = "18446744073709551615") == 16
    assert candidate(left = "100000000000000000",right = "100000000000000001") == 0
    assert candidate(left = "99999999999999999",right = "1000000000000000000") == 0
    assert candidate(left = "987654321",right = "987654321012345678") == 49
    assert candidate(left = "999999999999999999",right = "1000000000000000000") == 0
    assert candidate(left = "1000000",right = "100000000") == 3
    assert candidate(left = "100000000000000",right = "1000000000000000000") == 31
    assert candidate(left = "1000000000000000000",right = "9999999999999999999") == 16
    assert candidate(left = "10000",right = "100000000") == 8
    assert candidate(left = "10000000000",right = "11000000000") == 2
    assert candidate(left = "3000000000000",right = "4000000000000") == 0
    assert candidate(left = "123456789012345678",right = "987654321098765432") == 0
    assert candidate(left = "1000000000000000000",right = "1000000000000000000") == 0
    assert candidate(left = "123",right = "12345678987654321") == 64
    assert candidate(left = "1000000000",right = "999999999999999999") == 49
    assert candidate(left = "1234567891011121314",right = "15161718192021222324") == 1
    assert candidate(left = "100000000000000000",right = "900000000000000000") == 0
    assert candidate(left = "1000000000",right = "1000000000000") == 5
    assert candidate(left = "7000000000000000000",right = "8000000000000000000") == 0
    assert candidate(left = "1000000000000000000",right = "1000000000000000001") == 0
    assert candidate(left = "1000000000",right = "9999999999") == 0
    assert candidate(left = "50000000000000000",right = "60000000000000000") == 0
    assert candidate(left = "555555555555555555",right = "666666666666666666") == 0
    assert candidate(left = "10000000000000000",right = "1000000000000000000") == 22
    assert candidate(left = "100000000000000000",right = "18014398509481983") == 0
    assert candidate(left = "111111111",right = "999999999999999") == 32
    assert candidate(left = "800000000000000000",right = "899999999999999999") == 0
    assert candidate(left = "111111111111111111",right = "222222222222222222") == 0
    assert candidate(left = "500000000000000000",right = "600000000000000000") == 0
    assert candidate(left = "484",right = "576") == 1
    assert candidate(left = "999999999999999",right = "999999999999999999") == 22
    assert candidate(left = "80000000000",right = "90000000000") == 0
    assert candidate(left = "1000000",right = "1000000000") == 11


