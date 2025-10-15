def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 100000,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 240,k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 240,k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 430043,k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 430043,k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 99999,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99999,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456,k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456,k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111,k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111,k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 2345678901234567890,k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2345678901234567890,k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 100100100,k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100100100,k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 135792468013579246,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 135792468013579246,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 10101010101010101010,k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10101010101010101010,k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 123412341234,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123412341234,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111111,k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111111,k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543210,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543210,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890123456789,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890123456789,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 7777777,k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7777777,k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 12301230,k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12301230,k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789101112131415,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789101112131415,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1145141919810,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1145141919810,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789123456789123456789,k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789123456789123456789,k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 7777777777,k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7777777777,k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000001,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000001,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 112233445566778899,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 112233445566778899,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 2222222222,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2222222222,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 333333333,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333333333,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1010101010,k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1010101010,k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111111,k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111111,k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999,k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999,k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 567890123,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 567890123,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1100110011001100,k = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1100110011001100,k = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 112233445566778899,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 112233445566778899,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 100100100,k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100100100,k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 864208642086420,k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 864208642086420,k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 86420,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 86420,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 10000000001000000000,k = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000000001000000000,k = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890123456789,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890123456789,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000100010001,k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000100010001,k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000007,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000007,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 5432109876543210,k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5432109876543210,k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222222,k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222222,k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999,k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999,k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 1357924680,k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1357924680,k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 33333333333,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33333333333,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 5555555555555555555,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5555555555555555555,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 864208642,k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 864208642,k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101,k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101,k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 5555555555,k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5555555555,k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321,k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321,k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 112233445566,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 112233445566,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 789012345678,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 789012345678,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 314159265358979323,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 314159265358979323,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222222,k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222222,k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111111,k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111111,k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 123123123,k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123123123,k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000,k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000,k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888888888888,k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888888888888,k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789101112131415,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789101112131415,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1357924680,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1357924680,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543210987654321,k = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543210987654321,k = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 10203040506070809,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10203040506070809,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 777000777,k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777000777,k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321987654321,k = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321987654321,k = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 123123123,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123123123,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 98765432109876543210987654321,k = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98765432109876543210987654321,k = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222222,k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222222,k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 10203040506070809,k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10203040506070809,k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101,k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101,k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 567890123,k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 567890123,k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222222,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222222,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 12345678987654321,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12345678987654321,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999,k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999,k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 864197532,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 864197532,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 12301230123,k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12301230123,k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101010101010,k = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101010101010,k = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000,k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000,k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 444444444,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 444444444,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 222333444555,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222333444555,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1001001001001001001,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1001001001001001001,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 7777777,k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7777777,k = 2) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 100000,k = 2) == 1
    assert candidate(num = 240,k = 2) == 2
    assert candidate(num = 1111,k = 2) == 3
    assert candidate(num = 430043,k = 2) == 2
    assert candidate(num = 99999,k = 5) == 1
    assert candidate(num = 123456,k = 3) == 0
    assert candidate(num = 987654,k = 1) == 1
    assert candidate(num = 1111,k = 1) == 4
    assert candidate(num = 987654321,k = 4) == 0
    assert candidate(num = 999999999,k = 9) == 1
    assert candidate(num = 111222333,k = 5) == 0
    assert candidate(num = 2345678901234567890,k = 10) == 0
    assert candidate(num = 100100100,k = 4) == 4
    assert candidate(num = 135792468013579246,k = 7) == 0
    assert candidate(num = 10101010101010101010,k = 5) == 8
    assert candidate(num = 123412341234,k = 6) == 0
    assert candidate(num = 111111111,k = 1) == 9
    assert candidate(num = 9876543210,k = 3) == 1
    assert candidate(num = 1234567890123456789,k = 6) == 0
    assert candidate(num = 7777777,k = 7) == 1
    assert candidate(num = 12301230,k = 4) == 3
    assert candidate(num = 123456789101112131415,k = 6) == 0
    assert candidate(num = 1145141919810,k = 5) == 0
    assert candidate(num = 1000000000,k = 9) == 1
    assert candidate(num = 123456789123456789123456789,k = 8) == 0
    assert candidate(num = 7777777777,k = 8) == 0
    assert candidate(num = 1000000001,k = 9) == 1
    assert candidate(num = 112233445566778899,k = 6) == 0
    assert candidate(num = 2222222222,k = 4) == 0
    assert candidate(num = 333333333,k = 4) == 0
    assert candidate(num = 1010101010,k = 2) == 9
    assert candidate(num = 1111111111,k = 3) == 0
    assert candidate(num = 999999999,k = 2) == 0
    assert candidate(num = 567890123,k = 6) == 0
    assert candidate(num = 1100110011001100,k = 8) == 7
    assert candidate(num = 112233445566778899,k = 5) == 0
    assert candidate(num = 555555555,k = 6) == 0
    assert candidate(num = 100100100,k = 3) == 7
    assert candidate(num = 864208642086420,k = 4) == 3
    assert candidate(num = 86420,k = 2) == 1
    assert candidate(num = 10000000001000000000,k = 10) == 11
    assert candidate(num = 1234567890123456789,k = 7) == 0
    assert candidate(num = 1000100010001,k = 6) == 2
    assert candidate(num = 1000000007,k = 7) == 0
    assert candidate(num = 987654321,k = 9) == 1
    assert candidate(num = 5432109876543210,k = 2) == 4
    assert candidate(num = 222222222,k = 2) == 0
    assert candidate(num = 999999999,k = 1) == 9
    assert candidate(num = 1357924680,k = 2) == 4
    assert candidate(num = 33333333333,k = 4) == 0
    assert candidate(num = 5555555555555555555,k = 6) == 0
    assert candidate(num = 864208642,k = 3) == 0
    assert candidate(num = 101010101,k = 3) == 0
    assert candidate(num = 5555555555,k = 2) == 9
    assert candidate(num = 987654321,k = 3) == 0
    assert candidate(num = 112233445566,k = 6) == 0
    assert candidate(num = 789012345678,k = 7) == 0
    assert candidate(num = 314159265358979323,k = 4) == 0
    assert candidate(num = 222222222,k = 3) == 7
    assert candidate(num = 1111111111,k = 5) == 6
    assert candidate(num = 123123123,k = 2) == 0
    assert candidate(num = 1000000,k = 4) == 1
    assert candidate(num = 888888888888888888,k = 11) == 0
    assert candidate(num = 123456789101112131415,k = 7) == 0
    assert candidate(num = 1357924680,k = 5) == 0
    assert candidate(num = 9876543210987654321,k = 9) == 2
    assert candidate(num = 10203040506070809,k = 6) == 0
    assert candidate(num = 777000777,k = 4) == 2
    assert candidate(num = 101010101,k = 5) == 0
    assert candidate(num = 987654321987654321,k = 9) == 2
    assert candidate(num = 123123123,k = 4) == 0
    assert candidate(num = 1000000000,k = 5) == 1
    assert candidate(num = 98765432109876543210987654321,k = 10) == 2
    assert candidate(num = 222222222,k = 1) == 9
    assert candidate(num = 10203040506070809,k = 9) == 0
    assert candidate(num = 101010101,k = 2) == 4
    assert candidate(num = 567890123,k = 3) == 0
    assert candidate(num = 222222222,k = 5) == 0
    assert candidate(num = 12345678987654321,k = 7) == 0
    assert candidate(num = 999999999,k = 7) == 0
    assert candidate(num = 999999999,k = 3) == 7
    assert candidate(num = 864197532,k = 4) == 0
    assert candidate(num = 12301230123,k = 4) == 2
    assert candidate(num = 101010101010101010,k = 6) == 13
    assert candidate(num = 1000000000,k = 4) == 1
    assert candidate(num = 444444444,k = 5) == 0
    assert candidate(num = 222333444555,k = 4) == 0
    assert candidate(num = 1001001001001001001,k = 5) == 0
    assert candidate(num = 555555555,k = 5) == 0
    assert candidate(num = 7777777,k = 2) == 0


