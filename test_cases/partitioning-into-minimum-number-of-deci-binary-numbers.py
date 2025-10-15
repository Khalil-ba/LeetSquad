def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = "9876543210") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9876543210") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "82734") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "82734") == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = "32") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "32") == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = "11111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "555555555") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "555555555") == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = "9") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "27346209830709182346") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "27346209830709182346") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "55555") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "55555") == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321098765432109876543210") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321098765432109876543210") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "1999199919991999199919991999199919991999199919991999") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1999199919991999199919991999199919991999199919991999") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "11111111112222222222333333333333444444444444555555555") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11111111112222222222333333333333444444444444555555555") == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = "111999888777666555444333222111") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111999888777666555444333222111") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "8888888888888888888888888888888888888888") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "8888888888888888888888888888888888888888") == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = "87654321098765432109") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "87654321098765432109") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "11111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999999999999999999999999") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999999999999999999999999") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "44444444444444444444444444444444444444444444444444") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "44444444444444444444444444444444444444444444444444") == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = "101010101010101010101010101010") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "101010101010101010101010101010") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "5432105432105432105432105432105432105432105432105432") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "5432105432105432105432105432105432105432105432105432") == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "19191919191919191919") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "19191919191919191919") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "77777777777777777777777777777777777777777777777777") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "77777777777777777777777777777777777777777777777777") == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = "222222222222222222222222222222222222222222222222222") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "222222222222222222222222222222222222222222222222222") == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = "99999999999999999999") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "99999999999999999999") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "8456391728391657813265813265") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "8456391728391657813265813265") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "9999999999") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9999999999") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "918273645091827364509182736450") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "918273645091827364509182736450") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "12345678901234567890") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12345678901234567890") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "9999111199991111999911119999111199991111999911119999") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9999111199991111999911119999111199991111999911119999") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "19191919191919191919191919191919191919191919191919191919191919191919191919191919") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "19191919191919191919191919191919191919191919191919191919191919191919191919191919") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000000000000000000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000000000000000000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "55555555555555555555") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "55555555555555555555") == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = "888888888888888888888888888888888888888888888888888") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "888888888888888888888888888888888888888888888888888") == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = "99999") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "99999") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "1111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321012345678987654321") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321012345678987654321") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "10101010101010101010101010101010") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10101010101010101010101010101010") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "24681357924681357924") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "24681357924681357924") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789876543210000000000000000000000000000000000") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789876543210000000000000000000000000000000000") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "12345678987654321") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12345678987654321") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "10101010101010101010") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10101010101010101010") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "111222333444555666777888999") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111222333444555666777888999") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "18181818181818181818") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "18181818181818181818") == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = "13579135791357913579") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "13579135791357913579") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "101010101010101010101010101") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "101010101010101010101010101") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = "765432101023456765432101023456765432101023456765432") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "765432101023456765432101023456765432101023456765432") == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = "8765432109876543210987654321") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "8765432109876543210987654321") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "918273645432187654321") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "918273645432187654321") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "2468135791113151719") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2468135791113151719") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "1234567890") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234567890") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "22222222222222222222") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "22222222222222222222") == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = "98765432109876543210") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "98765432109876543210") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "123123123123123123123123123") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123123123123123123123123123") == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = "191919191919191919191919191919191919191919191919191") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "191919191919191919191919191919191919191919191919191") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "24680246802468024680") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "24680246802468024680") == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = "111122223333444455556666777788889999") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111122223333444455556666777788889999") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "50505050505050505050505050505050505050505050") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "50505050505050505050505050505050505050505050") == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789012345678901234567890") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789012345678901234567890") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "50000000000000000005") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "50000000000000000005") == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = "5555555555") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "5555555555") == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = "192837465056473829109876543210") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "192837465056473829109876543210") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "87654321987654321098") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "87654321987654321098") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "90000000000000000000900000000000000000000009") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "90000000000000000000900000000000000000000009") == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321987654321987654321987654321") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321987654321987654321987654321") == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = "9876543210") == 9
    assert candidate(n = "111") == 1
    assert candidate(n = "123456789") == 9
    assert candidate(n = "1") == 1
    assert candidate(n = "82734") == 8
    assert candidate(n = "32") == 3
    assert candidate(n = "11111") == 1
    assert candidate(n = "555555555") == 5
    assert candidate(n = "9") == 9
    assert candidate(n = "27346209830709182346") == 9
    assert candidate(n = "1000000000") == 1
    assert candidate(n = "55555") == 5
    assert candidate(n = "987654321") == 9
    assert candidate(n = "987654321098765432109876543210") == 9
    assert candidate(n = "1999199919991999199919991999199919991999199919991999") == 9
    assert candidate(n = "11111111112222222222333333333333444444444444555555555") == 5
    assert candidate(n = "111999888777666555444333222111") == 9
    assert candidate(n = "8888888888888888888888888888888888888888") == 8
    assert candidate(n = "87654321098765432109") == 9
    assert candidate(n = "999999999") == 9
    assert candidate(n = "11111111111111111111") == 1
    assert candidate(n = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111") == 1
    assert candidate(n = "999999999999999999999999999999") == 9
    assert candidate(n = "44444444444444444444444444444444444444444444444444") == 4
    assert candidate(n = "101010101010101010101010101010") == 1
    assert candidate(n = "5432105432105432105432105432105432105432105432105432") == 5
    assert candidate(n = "10000000000000000000") == 1
    assert candidate(n = "19191919191919191919") == 9
    assert candidate(n = "77777777777777777777777777777777777777777777777777") == 7
    assert candidate(n = "222222222222222222222222222222222222222222222222222") == 2
    assert candidate(n = "99999999999999999999") == 9
    assert candidate(n = "8456391728391657813265813265") == 9
    assert candidate(n = "9999999999") == 9
    assert candidate(n = "918273645091827364509182736450") == 9
    assert candidate(n = "12345678901234567890") == 9
    assert candidate(n = "9999111199991111999911119999111199991111999911119999") == 9
    assert candidate(n = "19191919191919191919191919191919191919191919191919191919191919191919191919191919") == 9
    assert candidate(n = "10000000000000000000000000000000000000000000") == 1
    assert candidate(n = "55555555555555555555") == 5
    assert candidate(n = "888888888888888888888888888888888888888888888888888") == 8
    assert candidate(n = "99999") == 9
    assert candidate(n = "1111111111") == 1
    assert candidate(n = "987654321012345678987654321") == 9
    assert candidate(n = "10101010101010101010101010101010") == 1
    assert candidate(n = "24681357924681357924") == 9
    assert candidate(n = "123456789876543210000000000000000000000000000000000") == 9
    assert candidate(n = "12345678987654321") == 9
    assert candidate(n = "10101010101010101010") == 1
    assert candidate(n = "111222333444555666777888999") == 9
    assert candidate(n = "18181818181818181818") == 8
    assert candidate(n = "13579135791357913579") == 9
    assert candidate(n = "101010101010101010101010101") == 1
    assert candidate(n = "100000000000000000000000000000") == 1
    assert candidate(n = "765432101023456765432101023456765432101023456765432") == 7
    assert candidate(n = "8765432109876543210987654321") == 9
    assert candidate(n = "918273645432187654321") == 9
    assert candidate(n = "2468135791113151719") == 9
    assert candidate(n = "1234567890") == 9
    assert candidate(n = "22222222222222222222") == 2
    assert candidate(n = "98765432109876543210") == 9
    assert candidate(n = "123123123123123123123123123") == 3
    assert candidate(n = "191919191919191919191919191919191919191919191919191") == 9
    assert candidate(n = "24680246802468024680") == 8
    assert candidate(n = "111122223333444455556666777788889999") == 9
    assert candidate(n = "50505050505050505050505050505050505050505050") == 5
    assert candidate(n = "123456789012345678901234567890") == 9
    assert candidate(n = "50000000000000000005") == 5
    assert candidate(n = "5555555555") == 5
    assert candidate(n = "192837465056473829109876543210") == 9
    assert candidate(n = "87654321987654321098") == 9
    assert candidate(n = "90000000000000000000900000000000000000000009") == 9
    assert candidate(n = "987654321987654321987654321987654321") == 9


