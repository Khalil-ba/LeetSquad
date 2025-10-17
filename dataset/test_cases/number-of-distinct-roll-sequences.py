def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 534856607
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 534856607: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 184: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 874574246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 874574246: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 497171723
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 497171723: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 93120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 93120: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 784558903
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 784558903: {e}')
    
    total += 1
    try:
        result = candidate(n = 104) == 920649565
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104) == 920649565: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 516
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 516: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 846205927
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 846205927: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000) == 366597434
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000) == 366597434: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 798977852
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 798977852: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 455330915
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 455330915: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 996985946
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 996985946: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 16706688
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 16706688: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 1472
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 1472: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 498714087
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 498714087: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 353640467
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 353640467: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 4136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 4136: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 66
    assert candidate(n = 100) == 534856607
    assert candidate(n = 4) == 184
    assert candidate(n = 10000) == 874574246
    assert candidate(n = 2) == 22
    assert candidate(n = 1) == 6
    assert candidate(n = 1000) == 497171723
    assert candidate(n = 10) == 93120
    assert candidate(n = 2000) == 784558903
    assert candidate(n = 104) == 920649565
    assert candidate(n = 5) == 516
    assert candidate(n = 20000) == 846205927
    assert candidate(n = 8000) == 366597434
    assert candidate(n = 5000) == 798977852
    assert candidate(n = 9999) == 455330915
    assert candidate(n = 20) == 996985946
    assert candidate(n = 15) == 16706688
    assert candidate(n = 6) == 1472
    assert candidate(n = 750) == 498714087
    assert candidate(n = 500) == 353640467
    assert candidate(n = 7) == 4136


