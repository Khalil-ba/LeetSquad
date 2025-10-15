def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 100) == "455"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == "455": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == "7"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == "7": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == "555555555888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == "555555555888": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 105) == "357"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 105) == "357": {e}')
    
    total += 1
    try:
        result = candidate(n = 387420489) == "999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 387420489) == "999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = 44) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == "25"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == "25": {e}')
    
    total += 1
    try:
        result = candidate(n = 59049) == "99999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59049) == "99999": {e}')
    
    total += 1
    try:
        result = candidate(n = 1836934518575681) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1836934518575681) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 86400000) == "5555568889"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 86400000) == "5555568889": {e}')
    
    total += 1
    try:
        result = candidate(n = 9999999999) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999999999) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 945) == "3579"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 945) == "3579": {e}')
    
    total += 1
    try:
        result = candidate(n = 4665600000) == "455555888999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4665600000) == "455555888999": {e}')
    
    total += 1
    try:
        result = candidate(n = 37822859361) == "777777779999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37822859361) == "777777779999": {e}')
    
    total += 1
    try:
        result = candidate(n = 86400) == "556889"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 86400) == "556889": {e}')
    
    total += 1
    try:
        result = candidate(n = 135792468) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135792468) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 5040) == "25789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5040) == "25789": {e}')
    
    total += 1
    try:
        result = candidate(n = 270) == "569"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 270) == "569": {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111111111111) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111111111111) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 1679616) == "4889999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1679616) == "4889999": {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888888888888) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888888888888) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 720) == "2589"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 720) == "2589": {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == "2888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == "2888": {e}')
    
    total += 1
    try:
        result = candidate(n = 2520) == "5789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2520) == "5789": {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == "288888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == "288888": {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == "488"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == "488": {e}')
    
    total += 1
    try:
        result = candidate(n = 222222222222222222) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222222222222222) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 2073600) == "25588899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2073600) == "25588899": {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 2222222222) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222222222) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 189) == "379"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 189) == "379": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999999999999) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999999999999) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 3125) == "55555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3125) == "55555": {e}')
    
    total += 1
    try:
        result = candidate(n = 1800000000) == "555555558889"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1800000000) == "555555558889": {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == "-1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == "-1": {e}')
    
    total += 1
    try:
        result = candidate(n = 3628800) == "45578899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3628800) == "45578899": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 100) == "455"
    assert candidate(n = 999999999) == "-1"
    assert candidate(n = 7) == "7"
    assert candidate(n = 1000000000) == "555555555888"
    assert candidate(n = 123456789) == "-1"
    assert candidate(n = 1) == "1"
    assert candidate(n = 105) == "357"
    assert candidate(n = 387420489) == "999999999"
    assert candidate(n = 44) == "-1"
    assert candidate(n = 10) == "25"
    assert candidate(n = 59049) == "99999"
    assert candidate(n = 1836934518575681) == "-1"
    assert candidate(n = 86400000) == "5555568889"
    assert candidate(n = 9999999999) == "-1"
    assert candidate(n = 945) == "3579"
    assert candidate(n = 4665600000) == "455555888999"
    assert candidate(n = 37822859361) == "777777779999"
    assert candidate(n = 86400) == "556889"
    assert candidate(n = 135792468) == "-1"
    assert candidate(n = 5040) == "25789"
    assert candidate(n = 270) == "569"
    assert candidate(n = 111111111111111111) == "-1"
    assert candidate(n = 1679616) == "4889999"
    assert candidate(n = 888888888888888888) == "-1"
    assert candidate(n = 720) == "2589"
    assert candidate(n = 1024) == "2888"
    assert candidate(n = 2520) == "5789"
    assert candidate(n = 9876543210) == "-1"
    assert candidate(n = 65536) == "288888"
    assert candidate(n = 256) == "488"
    assert candidate(n = 222222222222222222) == "-1"
    assert candidate(n = 2073600) == "25588899"
    assert candidate(n = 111111111) == "-1"
    assert candidate(n = 987654321) == "-1"
    assert candidate(n = 2222222222) == "-1"
    assert candidate(n = 189) == "379"
    assert candidate(n = 999999999999999999) == "-1"
    assert candidate(n = 3125) == "55555"
    assert candidate(n = 1800000000) == "555555558889"
    assert candidate(n = 1111111111) == "-1"
    assert candidate(n = 3628800) == "45578899"


