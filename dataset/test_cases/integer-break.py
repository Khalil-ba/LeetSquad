def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 11) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 54: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 59049
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 59049: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 1458
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 1458: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 58) == 1549681956
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 58) == 1549681956: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 39366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 39366: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 14348907
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 14348907: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 57395628
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 57395628: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 81: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == 28697814
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == 28697814: {e}')
    
    total += 1
    try:
        result = candidate(n = 53) == 258280326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 53) == 258280326: {e}')
    
    total += 1
    try:
        result = candidate(n = 57) == 1162261467
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 57) == 1162261467: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 86093442
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 86093442: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 26244
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 26244: {e}')
    
    total += 1
    try:
        result = candidate(n = 56) == 774840978
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56) == 774840978: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 2125764
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 2125764: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 708588
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 708588: {e}')
    
    total += 1
    try:
        result = candidate(n = 42) == 4782969
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42) == 4782969: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 354294
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 354294: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 729: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 118098
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 118098: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == 531441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == 531441: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 972: {e}')
    
    total += 1
    try:
        result = candidate(n = 48) == 43046721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48) == 43046721: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 243: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == 516560652
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == 516560652: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 108: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 8748
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 8748: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 11) == 54
    assert candidate(n = 30) == 59049
    assert candidate(n = 20) == 1458
    assert candidate(n = 2) == 1
    assert candidate(n = 10) == 36
    assert candidate(n = 58) == 1549681956
    assert candidate(n = 29) == 39366
    assert candidate(n = 45) == 14348907
    assert candidate(n = 49) == 57395628
    assert candidate(n = 12) == 81
    assert candidate(n = 47) == 28697814
    assert candidate(n = 53) == 258280326
    assert candidate(n = 57) == 1162261467
    assert candidate(n = 50) == 86093442
    assert candidate(n = 28) == 26244
    assert candidate(n = 56) == 774840978
    assert candidate(n = 40) == 2125764
    assert candidate(n = 37) == 708588
    assert candidate(n = 42) == 4782969
    assert candidate(n = 35) == 354294
    assert candidate(n = 18) == 729
    assert candidate(n = 32) == 118098
    assert candidate(n = 36) == 531441
    assert candidate(n = 19) == 972
    assert candidate(n = 48) == 43046721
    assert candidate(n = 15) == 243
    assert candidate(n = 6) == 9
    assert candidate(n = 55) == 516560652
    assert candidate(n = 13) == 108
    assert candidate(n = 25) == 8748


