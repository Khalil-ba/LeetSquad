def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(c = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1000000001) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1000000001) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 999999999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 999999999) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 500000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 500000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 100000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 100000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 846625) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 846625) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 314159265) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 314159265) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 840000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 840000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 80779853361) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 80779853361) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 16777217) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 16777217) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1215436930) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1215436930) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 999999999999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 999999999999) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 16777216) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 16777216) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 10000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 10000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 325) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 325) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1805306457) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1805306457) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 1000000003) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1000000003) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 2147483600) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 2147483600) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 2000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 2000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 10000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 10000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 4294967296) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 4294967296) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1800000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1800000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 250000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 250000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1000000002) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1000000002) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 846456943) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 846456943) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 3249000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 3249000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 13) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 13) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 846269696200635625) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 846269696200635625) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 18014398509481984) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 18014398509481984) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 123456789) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 123456789) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 1805355528) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1805355528) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 675) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 675) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 4294967295) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 4294967295) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 65535) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 65535) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 50) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 50) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1600000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1600000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 500) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 500) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 1234567890) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 1234567890) == False: {e}')
    
    total += 1
    try:
        result = candidate(c = 10001) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 10001) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 9876543210) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 9876543210) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 82) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 82) == True: {e}')
    
    total += 1
    try:
        result = candidate(c = 67280421310721) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(c = 67280421310721) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(c = 0) == True
    assert candidate(c = 1000000001) == False
    assert candidate(c = 25) == True
    assert candidate(c = 2) == True
    assert candidate(c = 3) == False
    assert candidate(c = 5) == True
    assert candidate(c = 1) == True
    assert candidate(c = 2147483647) == False
    assert candidate(c = 4) == True
    assert candidate(c = 1000000000) == True
    assert candidate(c = 999999999) == False
    assert candidate(c = 500000000) == True
    assert candidate(c = 100000000000) == True
    assert candidate(c = 846625) == True
    assert candidate(c = 314159265) == False
    assert candidate(c = 840000000) == False
    assert candidate(c = 80779853361) == False
    assert candidate(c = 16777217) == True
    assert candidate(c = 1000000) == True
    assert candidate(c = 1215436930) == False
    assert candidate(c = 999999999999) == False
    assert candidate(c = 16777216) == True
    assert candidate(c = 100) == True
    assert candidate(c = 10000) == True
    assert candidate(c = 325) == True
    assert candidate(c = 1805306457) == False
    assert candidate(c = 1000000003) == False
    assert candidate(c = 2147483600) == True
    assert candidate(c = 2000000000) == True
    assert candidate(c = 10000000000) == True
    assert candidate(c = 4294967296) == True
    assert candidate(c = 1800000000) == True
    assert candidate(c = 250000000) == True
    assert candidate(c = 1000000002) == False
    assert candidate(c = 846456943) == False
    assert candidate(c = 3249000000) == True
    assert candidate(c = 13) == True
    assert candidate(c = 846269696200635625) == True
    assert candidate(c = 18014398509481984) == True
    assert candidate(c = 123456789) == False
    assert candidate(c = 1805355528) == False
    assert candidate(c = 675) == False
    assert candidate(c = 4294967295) == False
    assert candidate(c = 65535) == False
    assert candidate(c = 50) == True
    assert candidate(c = 1600000000) == True
    assert candidate(c = 500) == True
    assert candidate(c = 1234567890) == False
    assert candidate(c = 10001) == True
    assert candidate(c = 9876543210) == True
    assert candidate(c = 82) == True
    assert candidate(c = 67280421310721) == True


