def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 14) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 14) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 49) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 49) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 50) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 50) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 1524157875) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1524157875) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 152415787501905210) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 152415787501905210) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 99) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 101) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 16) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 26) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 26) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 12345678987654321) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12345678987654321) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 361294659455137) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 361294659455137) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 9801) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9801) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 4503599627370496) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4503599627370496) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 401) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 401) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 12345678987654322) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12345678987654322) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 104976) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 104976) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 1025) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1025) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 18014398509481984) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 18014398509481984) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 18014398509481985) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 18014398509481985) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 9223372036854775807) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9223372036854775807) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000001) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000001) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 2500) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2500) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000001) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000001) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 2304) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2304) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 207936) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 207936) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 400) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 400) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 4294967296) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4294967296) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 46656000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 46656000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 141376) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 141376) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 1024) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1024) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 16777216) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 16777216) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000001) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000001) == False: {e}')
    
    total += 1
    try:
        result = candidate(num = 1073741824) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1073741824) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 14) == False
    assert candidate(num = 9) == True
    assert candidate(num = 1000000000) == False
    assert candidate(num = 49) == True
    assert candidate(num = 50) == False
    assert candidate(num = 25) == True
    assert candidate(num = 0) == False
    assert candidate(num = 4) == True
    assert candidate(num = 1524157875) == False
    assert candidate(num = 1) == True
    assert candidate(num = 100) == True
    assert candidate(num = 152415787501905210) == False
    assert candidate(num = 99) == False
    assert candidate(num = 2147483647) == False
    assert candidate(num = 101) == False
    assert candidate(num = 16) == True
    assert candidate(num = 26) == False
    assert candidate(num = 15) == False
    assert candidate(num = 12345678987654321) == True
    assert candidate(num = 10) == False
    assert candidate(num = 361294659455137) == False
    assert candidate(num = 9801) == True
    assert candidate(num = 100000000) == True
    assert candidate(num = 4503599627370496) == True
    assert candidate(num = 401) == False
    assert candidate(num = 12345678987654322) == False
    assert candidate(num = 104976) == True
    assert candidate(num = 1025) == False
    assert candidate(num = 123456789) == False
    assert candidate(num = 18014398509481984) == True
    assert candidate(num = 18014398509481985) == False
    assert candidate(num = 9223372036854775807) == False
    assert candidate(num = 1000000001) == False
    assert candidate(num = 2500) == True
    assert candidate(num = 100000001) == False
    assert candidate(num = 2304) == True
    assert candidate(num = 207936) == True
    assert candidate(num = 400) == True
    assert candidate(num = 4294967296) == True
    assert candidate(num = 2) == False
    assert candidate(num = 46656000000) == True
    assert candidate(num = 3) == False
    assert candidate(num = 141376) == True
    assert candidate(num = 1024) == True
    assert candidate(num = 1000000000000) == True
    assert candidate(num = 16777216) == True
    assert candidate(num = 999999999) == False
    assert candidate(num = 1000000) == True
    assert candidate(num = 1000001) == False
    assert candidate(num = 1073741824) == True


