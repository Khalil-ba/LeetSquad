def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 987654321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 230241) == 230412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 230241) == 230412: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483476) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483476) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 1243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 1243: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483486) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483486) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 534976) == 536479
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 534976) == 536479: {e}')
    
    total += 1
    try:
        result = candidate(n = 111) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1010101010) == 1010101100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010101010) == 1010101100: {e}')
    
    total += 1
    try:
        result = candidate(n = 43214321) == 43221134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43214321) == 43221134: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789876543210) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789876543210) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 567898765) == 567956788
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567898765) == 567956788: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483646) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483646) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5432109876) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5432109876) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123456789) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123456789) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 321321321) == 321322113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 321321321) == 321322113: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345678987654321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345678987654321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789123456789) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789123456789) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321098765) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321098765) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 223344556677889900) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 223344556677889900) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1225444333111) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1225444333111) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 543212345) == 543212354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543212345) == 543212354: {e}')
    
    total += 1
    try:
        result = candidate(n = 432143214321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 432143214321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 111122223333) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111122223333) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999998) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999998) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 531) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 531) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2233445566778899) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2233445566778899) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1098765432) == 1203456789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1098765432) == 1203456789: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111111111111111111) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111111111111111111) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5364768910) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5364768910) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5432109876543210) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5432109876543210) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483645) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483645) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2100000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2100000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 450210) == 451002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450210) == 451002: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == 101010110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == 101010110: {e}')
    
    total += 1
    try:
        result = candidate(n = 2121212121) == 2121212211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2121212121) == 2121212211: {e}')
    
    total += 1
    try:
        result = candidate(n = 11223344556677889900) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11223344556677889900) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 898989898) == 898989988
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 898989898) == 898989988: {e}')
    
    total += 1
    try:
        result = candidate(n = 536421) == 541236
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536421) == 541236: {e}')
    
    total += 1
    try:
        result = candidate(n = 12341234) == 12341243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12341234) == 12341243: {e}')
    
    total += 1
    try:
        result = candidate(n = 12344321) == 12412334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12344321) == 12412334: {e}')
    
    total += 1
    try:
        result = candidate(n = 333333333) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333333) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 33333333333333333333) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33333333333333333333) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3456789012) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3456789012) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3214321) == 3221134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3214321) == 3221134: {e}')
    
    total += 1
    try:
        result = candidate(n = 112233445566778899) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 112233445566778899) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789987654321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789987654321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 432123456789) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 432123456789) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3333333333) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3333333333) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1099999999) == 1909999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1099999999) == 1909999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345678901234567890) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345678901234567890) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890) == 1234567908
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890) == 1234567908: {e}')
    
    total += 1
    try:
        result = candidate(n = 2222222222) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222222222) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 43212341) == 43212413
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43212341) == 43212413: {e}')
    
    total += 1
    try:
        result = candidate(n = 499999999) == 949999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499999999) == 949999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 1121121121) == 1121121211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1121121121) == 1121121211: {e}')
    
    total += 1
    try:
        result = candidate(n = 1221) == 2112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1221) == 2112: {e}')
    
    total += 1
    try:
        result = candidate(n = 123454321) == 123512344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123454321) == 123512344: {e}')
    
    total += 1
    try:
        result = candidate(n = 8999999999999999999999999999999999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8999999999999999999999999999999999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 543210) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543210) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8765432109) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8765432109) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 543210987654321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543210987654321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999999999999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999999999999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 123456798
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 123456798: {e}')
    
    total += 1
    try:
        result = candidate(n = 1112111111) == 1121111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1112111111) == 1121111111: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765432109876543210) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765432109876543210) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321123456789) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321123456789) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 450340561) == 450340615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450340561) == 450340615: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 987654321) == -1
    assert candidate(n = 230241) == 230412
    assert candidate(n = 2147483476) == 2147483647
    assert candidate(n = 12) == 21
    assert candidate(n = 21) == -1
    assert candidate(n = 1234) == 1243
    assert candidate(n = 2147483647) == -1
    assert candidate(n = 2147483486) == -1
    assert candidate(n = 534976) == 536479
    assert candidate(n = 111) == -1
    assert candidate(n = 1999999999) == -1
    assert candidate(n = 1) == -1
    assert candidate(n = 4321) == -1
    assert candidate(n = 1010101010) == 1010101100
    assert candidate(n = 43214321) == 43221134
    assert candidate(n = 123456789876543210) == -1
    assert candidate(n = 567898765) == 567956788
    assert candidate(n = 2147483646) == -1
    assert candidate(n = 999999999) == -1
    assert candidate(n = 5432109876) == -1
    assert candidate(n = 1234567890123456789) == -1
    assert candidate(n = 321321321) == 321322113
    assert candidate(n = 12345678987654321) == -1
    assert candidate(n = 123456789123456789) == -1
    assert candidate(n = 4321098765) == -1
    assert candidate(n = 223344556677889900) == -1
    assert candidate(n = 1225444333111) == -1
    assert candidate(n = 543212345) == 543212354
    assert candidate(n = 432143214321) == -1
    assert candidate(n = 111122223333) == -1
    assert candidate(n = 999999998) == -1
    assert candidate(n = 531) == -1
    assert candidate(n = 2233445566778899) == -1
    assert candidate(n = 1098765432) == 1203456789
    assert candidate(n = 11111111111111111111) == -1
    assert candidate(n = 5364768910) == -1
    assert candidate(n = 5432109876543210) == -1
    assert candidate(n = 2147483645) == -1
    assert candidate(n = 2100000000) == -1
    assert candidate(n = 450210) == 451002
    assert candidate(n = 101010101) == 101010110
    assert candidate(n = 2121212121) == 2121212211
    assert candidate(n = 11223344556677889900) == -1
    assert candidate(n = 898989898) == 898989988
    assert candidate(n = 536421) == 541236
    assert candidate(n = 12341234) == 12341243
    assert candidate(n = 12344321) == 12412334
    assert candidate(n = 333333333) == -1
    assert candidate(n = 9876543210) == -1
    assert candidate(n = 33333333333333333333) == -1
    assert candidate(n = 3456789012) == -1
    assert candidate(n = 3214321) == 3221134
    assert candidate(n = 112233445566778899) == -1
    assert candidate(n = 123456789987654321) == -1
    assert candidate(n = 432123456789) == -1
    assert candidate(n = 3333333333) == -1
    assert candidate(n = 1000000000) == -1
    assert candidate(n = 1099999999) == 1909999999
    assert candidate(n = 12345678901234567890) == -1
    assert candidate(n = 111111111) == -1
    assert candidate(n = 1234567890) == 1234567908
    assert candidate(n = 2222222222) == -1
    assert candidate(n = 43212341) == 43212413
    assert candidate(n = 499999999) == 949999999
    assert candidate(n = 1121121121) == 1121121211
    assert candidate(n = 1221) == 2112
    assert candidate(n = 123454321) == 123512344
    assert candidate(n = 8999999999999999999999999999999999) == -1
    assert candidate(n = 543210) == -1
    assert candidate(n = 8765432109) == -1
    assert candidate(n = 543210987654321) == -1
    assert candidate(n = 98765) == -1
    assert candidate(n = 999999999999999999) == -1
    assert candidate(n = 123456789) == 123456798
    assert candidate(n = 1112111111) == 1121111111
    assert candidate(n = 98765432109876543210) == -1
    assert candidate(n = 987654321123456789) == -1
    assert candidate(n = 1111111111) == -1
    assert candidate(n = 54321) == -1
    assert candidate(n = 450340561) == 450340615


