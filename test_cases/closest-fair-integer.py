def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 100000) == 100011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 100011: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(n = 2222222) == 10000111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222222) == 10000111: {e}')
    
    total += 1
    try:
        result = candidate(n = 13579) == 100011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13579) == 100011: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 403) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 403) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111) == 111200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111) == 111200: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 1234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 1234: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 10000111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 10000111: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 123456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 123456: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 222222222) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222222) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 100011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 100011: {e}')
    
    total += 1
    try:
        result = candidate(n = 8642013579) == 8642013579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8642013579) == 8642013579: {e}')
    
    total += 1
    try:
        result = candidate(n = 899999999) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 899999999) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 22222222) == 22223111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22222222) == 22223111: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000001) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000001) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 86420) == 100011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 86420) == 100011: {e}')
    
    total += 1
    try:
        result = candidate(n = 24680) == 100011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24680) == 100011: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654) == 987654
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654) == 987654: {e}')
    
    total += 1
    try:
        result = candidate(n = 99000099) == 99000099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99000099) == 99000099: {e}')
    
    total += 1
    try:
        result = candidate(n = 444444444) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 444444444) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 10001) == 100011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10001) == 100011: {e}')
    
    total += 1
    try:
        result = candidate(n = 82468246) == 82469111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 82468246) == 82469111: {e}')
    
    total += 1
    try:
        result = candidate(n = 135792468) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135792468) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 505050505) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 505050505) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 345678901) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 345678901) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 1100110011) == 1100110012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1100110011) == 1100110012: {e}')
    
    total += 1
    try:
        result = candidate(n = 50050050) == 50050051
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50050050) == 50050051: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 2468013579) == 2468013579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2468013579) == 2468013579: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345678) == 12345678
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345678) == 12345678: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == 10000111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == 10000111: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000005) == 50000111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000005) == 50000111: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567891) == 1234567892
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567891) == 1234567892: {e}')
    
    total += 1
    try:
        result = candidate(n = 55555555) == 55556000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55555555) == 55556000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111) == 10000111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111) == 10000111: {e}')
    
    total += 1
    try:
        result = candidate(n = 864208642) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 864208642) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321) == 4321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321) == 4321: {e}')
    
    total += 1
    try:
        result = candidate(n = 44444444) == 44445111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44444444) == 44445111: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 246801357) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 246801357) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 11223344) == 11223344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11223344) == 11223344: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 500011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 500011: {e}')
    
    total += 1
    try:
        result = candidate(n = 111112222) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111112222) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 543210) == 543210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543210) == 543210: {e}')
    
    total += 1
    try:
        result = candidate(n = 135791) == 135800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135791) == 135800: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111111) == 11112000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111111) == 11112000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 10000111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 10000111: {e}')
    
    total += 1
    try:
        result = candidate(n = 88888888) == 88889111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88888888) == 88889111: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == 10000111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == 10000111: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000001) == 10000111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000001) == 10000111: {e}')
    
    total += 1
    try:
        result = candidate(n = 1357924680) == 1357924680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1357924680) == 1357924680: {e}')
    
    total += 1
    try:
        result = candidate(n = 543210987) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543210987) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555) == 555600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555) == 555600: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == 100011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == 100011: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == 1000001111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == 1000001111: {e}')
    
    total += 1
    try:
        result = candidate(n = 222222) == 222311
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222) == 222311: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 100000) == 100011
    assert candidate(n = 100) == 1001
    assert candidate(n = 2222222) == 10000111
    assert candidate(n = 13579) == 100011
    assert candidate(n = 999999999) == 1000001111
    assert candidate(n = 11) == 12
    assert candidate(n = 403) == 1001
    assert candidate(n = 111111) == 111200
    assert candidate(n = 1234) == 1234
    assert candidate(n = 123456789) == 1000001111
    assert candidate(n = 2) == 10
    assert candidate(n = 999999) == 10000111
    assert candidate(n = 123456) == 123456
    assert candidate(n = 1) == 10
    assert candidate(n = 1000) == 1001
    assert candidate(n = 10) == 10
    assert candidate(n = 222222222) == 1000001111
    assert candidate(n = 99999) == 100011
    assert candidate(n = 8642013579) == 8642013579
    assert candidate(n = 899999999) == 1000001111
    assert candidate(n = 22222222) == 22223111
    assert candidate(n = 100000001) == 1000001111
    assert candidate(n = 86420) == 100011
    assert candidate(n = 24680) == 100011
    assert candidate(n = 987654) == 987654
    assert candidate(n = 99000099) == 99000099
    assert candidate(n = 444444444) == 1000001111
    assert candidate(n = 10001) == 100011
    assert candidate(n = 82468246) == 82469111
    assert candidate(n = 135792468) == 1000001111
    assert candidate(n = 505050505) == 1000001111
    assert candidate(n = 345678901) == 1000001111
    assert candidate(n = 1100110011) == 1100110012
    assert candidate(n = 50050050) == 50050051
    assert candidate(n = 101010101) == 1000001111
    assert candidate(n = 2468013579) == 2468013579
    assert candidate(n = 12345678) == 12345678
    assert candidate(n = 800000000) == 1000001111
    assert candidate(n = 10000000) == 10000111
    assert candidate(n = 99999999) == 1000001111
    assert candidate(n = 50000005) == 50000111
    assert candidate(n = 1234567891) == 1234567892
    assert candidate(n = 55555555) == 55556000
    assert candidate(n = 1111111) == 10000111
    assert candidate(n = 864208642) == 1000001111
    assert candidate(n = 4321) == 4321
    assert candidate(n = 44444444) == 44445111
    assert candidate(n = 111111111) == 1000001111
    assert candidate(n = 987654321) == 1000001111
    assert candidate(n = 888888888) == 1000001111
    assert candidate(n = 246801357) == 1000001111
    assert candidate(n = 11223344) == 11223344
    assert candidate(n = 500000) == 500011
    assert candidate(n = 111112222) == 1000001111
    assert candidate(n = 543210) == 543210
    assert candidate(n = 135791) == 135800
    assert candidate(n = 11111111) == 11112000
    assert candidate(n = 1000000) == 10000111
    assert candidate(n = 88888888) == 88889111
    assert candidate(n = 1234567) == 10000111
    assert candidate(n = 1000001) == 10000111
    assert candidate(n = 1357924680) == 1357924680
    assert candidate(n = 543210987) == 1000001111
    assert candidate(n = 555555) == 555600
    assert candidate(n = 54321) == 100011
    assert candidate(n = 100000000) == 1000001111
    assert candidate(n = 222222) == 222311


