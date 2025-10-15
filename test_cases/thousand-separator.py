def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == "1.234"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == "1.234": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == "1.000.000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == "1.000.000": {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == "2.147.483.647"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == "2.147.483.647": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == "123.456.789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == "123.456.789": {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == "1.234.567"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == "1.234.567": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == "123.456"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == "123.456": {e}')
    
    total += 1
    try:
        result = candidate(n = 56789) == "56.789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56789) == "56.789": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == "1.000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == "1.000": {e}')
    
    total += 1
    try:
        result = candidate(n = 987) == "987"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987) == "987": {e}')
    
    total += 1
    try:
        result = candidate(n = 111222333444555666777888999) == "111.222.333.444.555.666.777.888.999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111222333444555666777888999) == "111.222.333.444.555.666.777.888.999": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789012) == "123.456.789.012"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789012) == "123.456.789.012": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == "999.999.999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == "999.999.999": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000000000) == "1.000.000.000.000.000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000000000) == "1.000.000.000.000.000": {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123456789) == "1.234.567.890.123.456.789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123456789) == "1.234.567.890.123.456.789": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789123456789) == "123.456.789.123.456.789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789123456789) == "123.456.789.123.456.789": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999999) == "999.999.999.999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999999) == "999.999.999.999": {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == "100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == "100": {e}')
    
    total += 1
    try:
        result = candidate(n = 456789012) == "456.789.012"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 456789012) == "456.789.012": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000000) == "1.000.000.000.000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000000) == "1.000.000.000.000": {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == "123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == "123": {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 1001001) == "1.001.001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001001) == "1.001.001": {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123456) == "1.234.567.890.123.456"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123456) == "1.234.567.890.123.456": {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == "10.000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == "10.000": {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111111111) == "111.111.111.111.111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111111111) == "111.111.111.111.111": {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == "1.001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == "1.001": {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210987654321) == "9.876.543.210.987.654.321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210987654321) == "9.876.543.210.987.654.321": {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == "101.010.101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == "101.010.101": {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000000) == "10.000.000.000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000000) == "10.000.000.000": {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == "100.000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == "100.000": {e}')
    
    total += 1
    try:
        result = candidate(n = 98765432109876543210987654321) == "98.765.432.109.876.543.210.987.654.321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765432109876543210987654321) == "98.765.432.109.876.543.210.987.654.321": {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210) == "9.876.543.210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210) == "9.876.543.210": {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == "999": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == "1.000.000.000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == "1.000.000.000": {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123) == "1.234.567.890.123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123) == "1.234.567.890.123": {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == "111.111.111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == "111.111.111": {e}')
    
    total += 1
    try:
        result = candidate(n = 1010101010) == "1.010.101.010"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010101010) == "1.010.101.010": {e}')
    
    total += 1
    try:
        result = candidate(n = 456789012345) == "456.789.012.345"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 456789012345) == "456.789.012.345": {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890) == "1.234.567.890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890) == "1.234.567.890": {e}')
    
    total += 1
    try:
        result = candidate(n = 567890123) == "567.890.123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567890123) == "567.890.123": {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == "987.654.321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == "987.654.321": {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321098) == "987.654.321.098"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321098) == "987.654.321.098": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789012345) == "123.456.789.012.345"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789012345) == "123.456.789.012.345": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789123) == "123.456.789.123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789123) == "123.456.789.123": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == "999.999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == "999.999": {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321098765) == "987.654.321.098.765"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321098765) == "987.654.321.098.765": {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == "1.111.111.111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == "1.111.111.111": {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == "54.321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == "54.321": {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == "10": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == "0"
    assert candidate(n = 1234) == "1.234"
    assert candidate(n = 1000000) == "1.000.000"
    assert candidate(n = 2147483647) == "2.147.483.647"
    assert candidate(n = 123456789) == "123.456.789"
    assert candidate(n = 1234567) == "1.234.567"
    assert candidate(n = 123456) == "123.456"
    assert candidate(n = 56789) == "56.789"
    assert candidate(n = 1000) == "1.000"
    assert candidate(n = 987) == "987"
    assert candidate(n = 111222333444555666777888999) == "111.222.333.444.555.666.777.888.999"
    assert candidate(n = 123456789012) == "123.456.789.012"
    assert candidate(n = 999999999) == "999.999.999"
    assert candidate(n = 1000000000000000) == "1.000.000.000.000.000"
    assert candidate(n = 1234567890123456789) == "1.234.567.890.123.456.789"
    assert candidate(n = 123456789123456789) == "123.456.789.123.456.789"
    assert candidate(n = 999999999999) == "999.999.999.999"
    assert candidate(n = 100) == "100"
    assert candidate(n = 456789012) == "456.789.012"
    assert candidate(n = 1000000000000) == "1.000.000.000.000"
    assert candidate(n = 123) == "123"
    assert candidate(n = 1) == "1"
    assert candidate(n = 1001001) == "1.001.001"
    assert candidate(n = 1234567890123456) == "1.234.567.890.123.456"
    assert candidate(n = 10000) == "10.000"
    assert candidate(n = 111111111111111) == "111.111.111.111.111"
    assert candidate(n = 1001) == "1.001"
    assert candidate(n = 9876543210987654321) == "9.876.543.210.987.654.321"
    assert candidate(n = 101010101) == "101.010.101"
    assert candidate(n = 10000000000) == "10.000.000.000"
    assert candidate(n = 100000) == "100.000"
    assert candidate(n = 98765432109876543210987654321) == "98.765.432.109.876.543.210.987.654.321"
    assert candidate(n = 9876543210) == "9.876.543.210"
    assert candidate(n = 999) == "999"
    assert candidate(n = 1000000000) == "1.000.000.000"
    assert candidate(n = 1234567890123) == "1.234.567.890.123"
    assert candidate(n = 111111111) == "111.111.111"
    assert candidate(n = 1010101010) == "1.010.101.010"
    assert candidate(n = 456789012345) == "456.789.012.345"
    assert candidate(n = 1234567890) == "1.234.567.890"
    assert candidate(n = 567890123) == "567.890.123"
    assert candidate(n = 987654321) == "987.654.321"
    assert candidate(n = 987654321098) == "987.654.321.098"
    assert candidate(n = 123456789012345) == "123.456.789.012.345"
    assert candidate(n = 123456789123) == "123.456.789.123"
    assert candidate(n = 999999) == "999.999"
    assert candidate(n = 987654321098765) == "987.654.321.098.765"
    assert candidate(n = 1111111111) == "1.111.111.111"
    assert candidate(n = 54321) == "54.321"
    assert candidate(n = 10) == "10"


