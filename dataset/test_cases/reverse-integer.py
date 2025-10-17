def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(x = -2147483412) == -2143847412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2147483412) == -2143847412: {e}')
    
    total += 1
    try:
        result = candidate(x = 2147483647) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2147483647) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = 120) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 120) == 21: {e}')
    
    total += 1
    try:
        result = candidate(x = -123) == -321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -123) == -321: {e}')
    
    total += 1
    try:
        result = candidate(x = 1534236469) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1534236469) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = -2147483648) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2147483648) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = -1534236469) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1534236469) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = 123) == 321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 123) == 321: {e}')
    
    total += 1
    try:
        result = candidate(x = -10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = -100000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -100000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = -999999999) == -999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -999999999) == -999999999: {e}')
    
    total += 1
    try:
        result = candidate(x = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 2147483646) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2147483646) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = -123000) == -321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -123000) == -321: {e}')
    
    total += 1
    try:
        result = candidate(x = -900000) == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -900000) == -9: {e}')
    
    total += 1
    try:
        result = candidate(x = -100100100) == -1001001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -100100100) == -1001001: {e}')
    
    total += 1
    try:
        result = candidate(x = -2147483647) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2147483647) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = -1010101010) == -101010101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1010101010) == -101010101: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000000001) == 1000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000000001) == 1000000001: {e}')
    
    total += 1
    try:
        result = candidate(x = -1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 123000) == 321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 123000) == 321: {e}')
    
    total += 1
    try:
        result = candidate(x = -2000000002) == -2000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2000000002) == -2000000002: {e}')
    
    total += 1
    try:
        result = candidate(x = 101010101) == 101010101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 101010101) == 101010101: {e}')
    
    total += 1
    try:
        result = candidate(x = 1111111111) == 1111111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1111111111) == 1111111111: {e}')
    
    total += 1
    try:
        result = candidate(x = 2147447412) == 2147447412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2147447412) == 2147447412: {e}')
    
    total += 1
    try:
        result = candidate(x = -101010101) == -101010101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -101010101) == -101010101: {e}')
    
    total += 1
    try:
        result = candidate(x = 900000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 900000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 987654321) == 123456789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 987654321) == 123456789: {e}')
    
    total += 1
    try:
        result = candidate(x = 999999999) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 999999999) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(x = -1000000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1000000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 1001001001) == 1001001001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1001001001) == 1001001001: {e}')
    
    total += 1
    try:
        result = candidate(x = -987654321) == -123456789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -987654321) == -123456789: {e}')
    
    total += 1
    try:
        result = candidate(x = -1000000001) == -1000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1000000001) == -1000000001: {e}')
    
    total += 1
    try:
        result = candidate(x = 10000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 11000000001) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 11000000001) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = 876543210) == 12345678
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 876543210) == 12345678: {e}')
    
    total += 1
    try:
        result = candidate(x = 2147483640) == 463847412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2147483640) == 463847412: {e}')
    
    total += 1
    try:
        result = candidate(x = 100100100) == 1001001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100100100) == 1001001: {e}')
    
    total += 1
    try:
        result = candidate(x = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 2000000002) == 2000000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2000000002) == 2000000002: {e}')
    
    total += 1
    try:
        result = candidate(x = -9646324351) == -1534236469
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -9646324351) == -1534236469: {e}')
    
    total += 1
    try:
        result = candidate(x = -123456789) == -987654321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -123456789) == -987654321: {e}')
    
    total += 1
    try:
        result = candidate(x = 7463847412) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7463847412) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(x = -1000000003) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1000000003) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = -3000000001) == -1000000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -3000000001) == -1000000003: {e}')
    
    total += 1
    try:
        result = candidate(x = -876543210) == -12345678
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -876543210) == -12345678: {e}')
    
    total += 1
    try:
        result = candidate(x = -1111111111) == -1111111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1111111111) == -1111111111: {e}')
    
    total += 1
    try:
        result = candidate(x = -1001001001) == -1001001001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -1001001001) == -1001001001: {e}')
    
    total += 1
    try:
        result = candidate(x = 9646324351) == 1534236469
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9646324351) == 1534236469: {e}')
    
    total += 1
    try:
        result = candidate(x = 1010101010) == 101010101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1010101010) == 101010101: {e}')
    
    total += 1
    try:
        result = candidate(x = 123456789) == 987654321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 123456789) == 987654321: {e}')
    
    total += 1
    try:
        result = candidate(x = -10000000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -10000000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = -2147483640) == -463847412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -2147483640) == -463847412: {e}')
    
    total += 1
    try:
        result = candidate(x = -7463847412) == -2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -7463847412) == -2147483647: {e}')
    
    total += 1
    try:
        result = candidate(x = 3000000001) == 1000000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3000000001) == 1000000003: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 1000000003) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1000000003) == 0: {e}')
    
    total += 1
    try:
        result = candidate(x = -214748364) == -463847412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = -214748364) == -463847412: {e}')
    
    total += 1
    try:
        result = candidate(x = 9000000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9000000000) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(x = -2147483412) == -2143847412
    assert candidate(x = 2147483647) == 0
    assert candidate(x = 120) == 21
    assert candidate(x = -123) == -321
    assert candidate(x = 1534236469) == 0
    assert candidate(x = 0) == 0
    assert candidate(x = -2147483648) == 0
    assert candidate(x = -1534236469) == 0
    assert candidate(x = 123) == 321
    assert candidate(x = -10) == -1
    assert candidate(x = -100000) == -1
    assert candidate(x = 10) == 1
    assert candidate(x = -999999999) == -999999999
    assert candidate(x = 1) == 1
    assert candidate(x = 2147483646) == 0
    assert candidate(x = -123000) == -321
    assert candidate(x = -900000) == -9
    assert candidate(x = -100100100) == -1001001
    assert candidate(x = -2147483647) == 0
    assert candidate(x = -1010101010) == -101010101
    assert candidate(x = 1000000001) == 1000000001
    assert candidate(x = -1) == -1
    assert candidate(x = 123000) == 321
    assert candidate(x = -2000000002) == -2000000002
    assert candidate(x = 101010101) == 101010101
    assert candidate(x = 1111111111) == 1111111111
    assert candidate(x = 2147447412) == 2147447412
    assert candidate(x = -101010101) == -101010101
    assert candidate(x = 900000) == 9
    assert candidate(x = 987654321) == 123456789
    assert candidate(x = 999999999) == 999999999
    assert candidate(x = -1000000000) == -1
    assert candidate(x = 1001001001) == 1001001001
    assert candidate(x = -987654321) == -123456789
    assert candidate(x = -1000000001) == -1000000001
    assert candidate(x = 10000000000) == 1
    assert candidate(x = 11000000001) == 0
    assert candidate(x = 876543210) == 12345678
    assert candidate(x = 2147483640) == 463847412
    assert candidate(x = 100100100) == 1001001
    assert candidate(x = 100000) == 1
    assert candidate(x = 2000000002) == 2000000002
    assert candidate(x = -9646324351) == -1534236469
    assert candidate(x = -123456789) == -987654321
    assert candidate(x = 7463847412) == 2147483647
    assert candidate(x = -1000000003) == 0
    assert candidate(x = -3000000001) == -1000000003
    assert candidate(x = -876543210) == -12345678
    assert candidate(x = -1111111111) == -1111111111
    assert candidate(x = -1001001001) == -1001001001
    assert candidate(x = 9646324351) == 1534236469
    assert candidate(x = 1010101010) == 101010101
    assert candidate(x = 123456789) == 987654321
    assert candidate(x = -10000000000) == -1
    assert candidate(x = -2147483640) == -463847412
    assert candidate(x = -7463847412) == -2147483647
    assert candidate(x = 3000000001) == 1000000003
    assert candidate(x = 1000000000) == 1
    assert candidate(x = 1000000003) == 0
    assert candidate(x = -214748364) == -463847412
    assert candidate(x = 9000000000) == 9


