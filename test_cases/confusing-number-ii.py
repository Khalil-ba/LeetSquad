def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 999999999) == 1950626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 1950626: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 226
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 226: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 1196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 1196: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 107: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 226
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 226: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 587
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 587: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == 77627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == 77627: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 3027
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 3027: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 226
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 226: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 1950627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 1950627: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 1841356
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 1841356: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 15427
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 15427: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 545726
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 545726: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == 389627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == 389627: {e}')
    
    total += 1
    try:
        result = candidate(n = 222222222) == 779876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222222) == 779876: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 3026
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 3026: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 830
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 830: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999999) == 77626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999999) == 77626: {e}')
    
    total += 1
    try:
        result = candidate(n = 67890) == 1562
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67890) == 1562: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 3903126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 3903126: {e}')
    
    total += 1
    try:
        result = candidate(n = 909090909) == 1625418
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 909090909) == 1625418: {e}')
    
    total += 1
    try:
        result = candidate(n = 90000) == 2417
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90000) == 2417: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000000) == 155626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000000) == 155626: {e}')
    
    total += 1
    try:
        result = candidate(n = 666666666) == 975001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666666666) == 975001: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000001) == 1170128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000001) == 1170128: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000000) == 1170126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000000) == 1170126: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000) == 779876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000) == 779876: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == 405886
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == 405886: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000) == 155626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000) == 155626: {e}')
    
    total += 1
    try:
        result = candidate(n = 900000000) == 1560377
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900000000) == 1560377: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000) == 1170127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000) == 1170127: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765432) == 367786
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765432) == 367786: {e}')
    
    total += 1
    try:
        result = candidate(n = 678901234) == 1014026
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 678901234) == 1014026: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999) == 389626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999) == 389626: {e}')
    
    total += 1
    try:
        result = candidate(n = 600000000) == 779877
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600000000) == 779877: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000010) == 1950631
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000010) == 1950631: {e}')
    
    total += 1
    try:
        result = candidate(n = 168888888) == 604264
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 168888888) == 604264: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == 1950627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == 1950627: {e}')
    
    total += 1
    try:
        result = candidate(n = 456789123) == 779876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 456789123) == 779876: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == 487188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == 487188: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888) == 1462813
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888) == 1462813: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000000) == 779876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000000) == 779876: {e}')
    
    total += 1
    try:
        result = candidate(n = 499999999) == 779876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499999999) == 779876: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111) == 738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111) == 738: {e}')
    
    total += 1
    try:
        result = candidate(n = 599999999) == 779876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 599999999) == 779876: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 6126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 6126: {e}')
    
    total += 1
    try:
        result = candidate(n = 700000000) == 1170126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700000000) == 1170126: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 779876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 779876: {e}')
    
    total += 1
    try:
        result = candidate(n = 43210) == 1196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43210) == 1196: {e}')
    
    total += 1
    try:
        result = candidate(n = 88888888) == 292126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88888888) == 292126: {e}')
    
    total += 1
    try:
        result = candidate(n = 689012345) == 1077339
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 689012345) == 1077339: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 15426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 15426: {e}')
    
    total += 1
    try:
        result = candidate(n = 899999999) == 1560376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 899999999) == 1560376: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 999999999) == 1950626
    assert candidate(n = 2000) == 226
    assert candidate(n = 100) == 19
    assert candidate(n = 50000) == 1196
    assert candidate(n = 1000) == 107
    assert candidate(n = 50) == 6
    assert candidate(n = 10) == 3
    assert candidate(n = 3000) == 226
    assert candidate(n = 10000) == 587
    assert candidate(n = 10000000) == 77627
    assert candidate(n = 100000) == 3027
    assert candidate(n = 5000) == 226
    assert candidate(n = 20) == 6
    assert candidate(n = 1000000000) == 1950627
    assert candidate(n = 987654321) == 1841356
    assert candidate(n = 1000000) == 15427
    assert candidate(n = 9) == 2
    assert candidate(n = 123456789) == 545726
    assert candidate(n = 1) == 0
    assert candidate(n = 500) == 40
    assert candidate(n = 100000000) == 389627
    assert candidate(n = 222222222) == 779876
    assert candidate(n = 99999) == 3026
    assert candidate(n = 12345) == 830
    assert candidate(n = 9999999) == 77626
    assert candidate(n = 67890) == 1562
    assert candidate(n = 2147483647) == 3903126
    assert candidate(n = 909090909) == 1625418
    assert candidate(n = 90000) == 2417
    assert candidate(n = 20000000) == 155626
    assert candidate(n = 666666666) == 975001
    assert candidate(n = 800000001) == 1170128
    assert candidate(n = 750000000) == 1170126
    assert candidate(n = 200000000) == 779876
    assert candidate(n = 101010101) == 405886
    assert candidate(n = 50000000) == 155626
    assert candidate(n = 900000000) == 1560377
    assert candidate(n = 800000000) == 1170127
    assert candidate(n = 98765432) == 367786
    assert candidate(n = 678901234) == 1014026
    assert candidate(n = 99999999) == 389626
    assert candidate(n = 600000000) == 779877
    assert candidate(n = 1000000010) == 1950631
    assert candidate(n = 168888888) == 604264
    assert candidate(n = 1000000001) == 1950627
    assert candidate(n = 456789123) == 779876
    assert candidate(n = 111111111) == 487188
    assert candidate(n = 888888888) == 1462813
    assert candidate(n = 300000000) == 779876
    assert candidate(n = 499999999) == 779876
    assert candidate(n = 11111) == 738
    assert candidate(n = 599999999) == 779876
    assert candidate(n = 500000) == 6126
    assert candidate(n = 700000000) == 1170126
    assert candidate(n = 500000000) == 779876
    assert candidate(n = 43210) == 1196
    assert candidate(n = 88888888) == 292126
    assert candidate(n = 689012345) == 1077339
    assert candidate(n = 999999) == 15426
    assert candidate(n = 899999999) == 1560376


