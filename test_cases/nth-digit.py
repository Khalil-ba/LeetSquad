def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 231) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 231) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483646) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483646) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 190) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 190) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 8976543) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8976543) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2100000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2100000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 360) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 360) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483645) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483645) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 777777777) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777777777) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000010) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000010) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 189) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 189) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 150000000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150000000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 19999) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19999) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 3
    assert candidate(n = 11) == 0
    assert candidate(n = 231) == 3
    assert candidate(n = 15) == 2
    assert candidate(n = 2147483647) == 2
    assert candidate(n = 1000000) == 1
    assert candidate(n = 123456789) == 2
    assert candidate(n = 100) == 5
    assert candidate(n = 1000) == 3
    assert candidate(n = 99999) == 1
    assert candidate(n = 999999999) == 9
    assert candidate(n = 2147483646) == 2
    assert candidate(n = 12345) == 3
    assert candidate(n = 2000000000) == 3
    assert candidate(n = 50000) == 1
    assert candidate(n = 50) == 3
    assert candidate(n = 190) == 1
    assert candidate(n = 987654) == 3
    assert candidate(n = 123) == 6
    assert candidate(n = 300) == 6
    assert candidate(n = 99) == 4
    assert candidate(n = 10000) == 7
    assert candidate(n = 1001) == 7
    assert candidate(n = 8976543) == 4
    assert candidate(n = 2100000000) == 5
    assert candidate(n = 360) == 6
    assert candidate(n = 2147483645) == 7
    assert candidate(n = 777777777) == 0
    assert candidate(n = 100000) == 2
    assert candidate(n = 20000) == 7
    assert candidate(n = 999) == 9
    assert candidate(n = 1000000010) == 2
    assert candidate(n = 5000) == 2
    assert candidate(n = 256) == 1
    assert candidate(n = 1000000000) == 1
    assert candidate(n = 1000000001) == 2
    assert candidate(n = 111111111) == 7
    assert candidate(n = 987654321) == 7
    assert candidate(n = 888888888) == 0
    assert candidate(n = 2500) == 8
    assert candidate(n = 500000) == 5
    assert candidate(n = 189) == 9
    assert candidate(n = 150000000) == 8
    assert candidate(n = 500000000) == 8
    assert candidate(n = 9) == 9
    assert candidate(n = 1234567) == 2
    assert candidate(n = 19999) == 2
    assert candidate(n = 999999) == 4
    assert candidate(n = 123456) == 6
    assert candidate(n = 10) == 1


