def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000000) == 348513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000000) == 348513: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 168: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500000) == 114155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500000) == 114155: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 78498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 78498: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4999999) == 348512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4999999) == 348512: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 1229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 1229: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 7890123) == 532888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7890123) == 532888: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000) == 148933
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000) == 148933: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000000) == 283146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000000) == 283146: {e}')
    
    total += 1
    try:
        result = candidate(n = 3141592) == 226277
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3141592) == 226277: {e}')
    
    total += 1
    try:
        result = candidate(n = 499979) == 41537
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499979) == 41537: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == 664579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == 664579: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000001) == 348513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000001) == 348513: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 669
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 669: {e}')
    
    total += 1
    try:
        result = candidate(n = 999983) == 78497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999983) == 78497: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000000) == 216816
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000000) == 216816: {e}')
    
    total += 1
    try:
        result = candidate(n = 789654) == 63183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789654) == 63183: {e}')
    
    total += 1
    try:
        result = candidate(n = 31337) == 3378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31337) == 3378: {e}')
    
    total += 1
    try:
        result = candidate(n = 104729) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104729) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 41538
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 41538: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == 95360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == 95360: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 5000000) == 348513
    assert candidate(n = 1000) == 168
    assert candidate(n = 100) == 25
    assert candidate(n = 30) == 10
    assert candidate(n = 1500000) == 114155
    assert candidate(n = 1000000) == 78498
    assert candidate(n = 20) == 8
    assert candidate(n = 2) == 0
    assert candidate(n = 1) == 0
    assert candidate(n = 50) == 15
    assert candidate(n = 10) == 4
    assert candidate(n = 5) == 2
    assert candidate(n = 3) == 1
    assert candidate(n = 4999999) == 348512
    assert candidate(n = 10000) == 1229
    assert candidate(n = 17) == 6
    assert candidate(n = 7890123) == 532888
    assert candidate(n = 2000000) == 148933
    assert candidate(n = 4000000) == 283146
    assert candidate(n = 3141592) == 226277
    assert candidate(n = 499979) == 41537
    assert candidate(n = 10000000) == 664579
    assert candidate(n = 5000001) == 348513
    assert candidate(n = 18) == 7
    assert candidate(n = 5000) == 669
    assert candidate(n = 999983) == 78497
    assert candidate(n = 3000000) == 216816
    assert candidate(n = 789654) == 63183
    assert candidate(n = 31337) == 3378
    assert candidate(n = 104729) == 9999
    assert candidate(n = 500000) == 41538
    assert candidate(n = 1234567) == 95360


