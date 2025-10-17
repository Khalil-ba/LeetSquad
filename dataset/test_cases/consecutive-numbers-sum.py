def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 210) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 210) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 897) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 897) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 67890) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67890) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 76543210) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 76543210) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 56789) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56789) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 89123456) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89123456) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2019) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2019) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 6789) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6789) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 43210987) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43210987) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 56789123) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56789123) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 845123) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 845123) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 89754321) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89754321) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8472187) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8472187) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 84521) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84521) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 121) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 121) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 100) == 3
    assert candidate(n = 15) == 4
    assert candidate(n = 9) == 3
    assert candidate(n = 1000000) == 7
    assert candidate(n = 25) == 3
    assert candidate(n = 1) == 1
    assert candidate(n = 1000000000) == 10
    assert candidate(n = 1000) == 4
    assert candidate(n = 10) == 2
    assert candidate(n = 5) == 2
    assert candidate(n = 3) == 2
    assert candidate(n = 45) == 6
    assert candidate(n = 210) == 8
    assert candidate(n = 897) == 8
    assert candidate(n = 999999999) == 20
    assert candidate(n = 49) == 3
    assert candidate(n = 12345) == 8
    assert candidate(n = 67890) == 16
    assert candidate(n = 2147483647) == 2
    assert candidate(n = 76543210) == 8
    assert candidate(n = 56789) == 4
    assert candidate(n = 89123456) == 4
    assert candidate(n = 2019) == 4
    assert candidate(n = 6789) == 8
    assert candidate(n = 10000) == 5
    assert candidate(n = 43210987) == 8
    assert candidate(n = 1001) == 8
    assert candidate(n = 2) == 1
    assert candidate(n = 200000000) == 9
    assert candidate(n = 50000000) == 9
    assert candidate(n = 1024) == 1
    assert candidate(n = 101) == 2
    assert candidate(n = 8) == 1
    assert candidate(n = 10000000) == 8
    assert candidate(n = 56789123) == 2
    assert candidate(n = 845123) == 4
    assert candidate(n = 1048576) == 1
    assert candidate(n = 89) == 2
    assert candidate(n = 89754321) == 4
    assert candidate(n = 8472187) == 4
    assert candidate(n = 84521) == 2
    assert candidate(n = 13) == 2
    assert candidate(n = 150) == 6
    assert candidate(n = 987654321) == 18
    assert candidate(n = 123456789) == 12
    assert candidate(n = 1234567) == 4
    assert candidate(n = 121) == 3
    assert candidate(n = 999999) == 64
    assert candidate(n = 123456) == 4
    assert candidate(n = 500) == 4
    assert candidate(n = 54321) == 8
    assert candidate(n = 100000000) == 9
    assert candidate(n = 1500) == 8


