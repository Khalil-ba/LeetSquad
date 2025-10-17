def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 3249) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3249) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 10) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10) == 25: {e}')
    
    total += 1
    try:
        result = candidate(num = 48) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 48) == 68: {e}')
    
    total += 1
    try:
        result = candidate(num = 210) == 567
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 210) == 567: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 360) == 589
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 360) == 589: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 216) == 389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 216) == 389: {e}')
    
    total += 1
    try:
        result = candidate(num = 18) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 18) == 29: {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == 455: {e}')
    
    total += 1
    try:
        result = candidate(num = 1024) == 2888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1024) == 2888: {e}')
    
    total += 1
    try:
        result = candidate(num = 2147483647) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2147483647) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 72) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 72) == 89: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 231) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 231) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 180) == 459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 180) == 459: {e}')
    
    total += 1
    try:
        result = candidate(num = 37) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 37) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 15) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15) == 35: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222222) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222222) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 12345678) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12345678) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 512) == 888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 512) == 888: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111111) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111111) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 4294967295) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4294967295) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 2384185791015625) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2384185791015625) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 6789) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 6789) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 444444444) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 444444444) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 5184) == 8899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5184) == 8899: {e}')
    
    total += 1
    try:
        result = candidate(num = 777777777) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777777777) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 82944) == 288899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 82944) == 288899: {e}')
    
    total += 1
    try:
        result = candidate(num = 666666666) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 666666666) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 65535) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65535) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 333333333) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333333333) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1999999999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1999999999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 3628800) == 45578899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3628800) == 45578899: {e}')
    
    total += 1
    try:
        result = candidate(num = 46656) == 88999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 46656) == 88999: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 86420) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 86420) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 94143178827) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 94143178827) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 46189) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 46189) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 268435456) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 268435456) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 86400000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 86400000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000007) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000007) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 55555) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 55555) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 86400) == 556889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 86400) == 556889: {e}')
    
    total += 1
    try:
        result = candidate(num = 99999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == 55555588
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == 55555588: {e}')
    
    total += 1
    try:
        result = candidate(num = 65536) == 288888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 65536) == 288888: {e}')
    
    total += 1
    try:
        result = candidate(num = 199999999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199999999) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 3249) == 0
    assert candidate(num = 10) == 25
    assert candidate(num = 48) == 68
    assert candidate(num = 210) == 567
    assert candidate(num = 1000000000) == 0
    assert candidate(num = 360) == 589
    assert candidate(num = 123456789) == 0
    assert candidate(num = 216) == 389
    assert candidate(num = 18) == 29
    assert candidate(num = 1) == 1
    assert candidate(num = 100) == 455
    assert candidate(num = 1024) == 2888
    assert candidate(num = 2147483647) == 0
    assert candidate(num = 72) == 89
    assert candidate(num = 999999999) == 0
    assert candidate(num = 231) == 0
    assert candidate(num = 180) == 459
    assert candidate(num = 37) == 0
    assert candidate(num = 15) == 35
    assert candidate(num = 222222222) == 0
    assert candidate(num = 12345678) == 0
    assert candidate(num = 512) == 888
    assert candidate(num = 111111111) == 0
    assert candidate(num = 555555555) == 0
    assert candidate(num = 4294967295) == 0
    assert candidate(num = 2384185791015625) == 0
    assert candidate(num = 888888888) == 0
    assert candidate(num = 6789) == 0
    assert candidate(num = 444444444) == 0
    assert candidate(num = 5184) == 8899
    assert candidate(num = 777777777) == 0
    assert candidate(num = 82944) == 288899
    assert candidate(num = 666666666) == 0
    assert candidate(num = 65535) == 0
    assert candidate(num = 333333333) == 0
    assert candidate(num = 1999999999) == 0
    assert candidate(num = 3628800) == 45578899
    assert candidate(num = 46656) == 88999
    assert candidate(num = 1234567890) == 0
    assert candidate(num = 86420) == 0
    assert candidate(num = 94143178827) == 0
    assert candidate(num = 46189) == 0
    assert candidate(num = 987654321) == 0
    assert candidate(num = 268435456) == 0
    assert candidate(num = 86400000) == 0
    assert candidate(num = 1000000007) == 0
    assert candidate(num = 55555) == 0
    assert candidate(num = 86400) == 556889
    assert candidate(num = 99999) == 0
    assert candidate(num = 1000000) == 55555588
    assert candidate(num = 65536) == 288888
    assert candidate(num = 199999999) == 0


