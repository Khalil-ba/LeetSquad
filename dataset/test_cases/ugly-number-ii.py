def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 15) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 16200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 16200: {e}')
    
    total += 1
    try:
        result = candidate(n = 1690) == 2123366400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1690) == 2123366400: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 243: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1400) == 516560652
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1400) == 516560652: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1575) == 1230187500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1575) == 1230187500: {e}')
    
    total += 1
    try:
        result = candidate(n = 1600) == 1399680000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1600) == 1399680000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1685) == 2066242608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1685) == 2066242608: {e}')
    
    total += 1
    try:
        result = candidate(n = 900) == 26244000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900) == 26244000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1688) == 2099520000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1688) == 2099520000: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 1536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 1536: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 51200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 51200000: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 82944
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 82944: {e}')
    
    total += 1
    try:
        result = candidate(n = 550) == 1555200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550) == 1555200: {e}')
    
    total += 1
    try:
        result = candidate(n = 1200) == 174960000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1200) == 174960000: {e}')
    
    total += 1
    try:
        result = candidate(n = 600) == 2460375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600) == 2460375: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1675) == 1990656000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1675) == 1990656000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1650) == 1769472000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1650) == 1769472000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1550) == 1093500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1550) == 1093500000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1300) == 306110016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1300) == 306110016: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 60466176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 60466176: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1689) == 2109375000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1689) == 2109375000: {e}')
    
    total += 1
    try:
        result = candidate(n = 800) == 12754584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800) == 12754584: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 311040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 311040: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 8748000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 8748000: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 937500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 937500: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1680) == 2025000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1680) == 2025000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500) == 859963392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500) == 859963392: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 15) == 24
    assert candidate(n = 200) == 16200
    assert candidate(n = 1690) == 2123366400
    assert candidate(n = 1) == 1
    assert candidate(n = 50) == 243
    assert candidate(n = 10) == 12
    assert candidate(n = 5) == 5
    assert candidate(n = 1400) == 516560652
    assert candidate(n = 3) == 3
    assert candidate(n = 1575) == 1230187500
    assert candidate(n = 1600) == 1399680000
    assert candidate(n = 1685) == 2066242608
    assert candidate(n = 900) == 26244000
    assert candidate(n = 1688) == 2099520000
    assert candidate(n = 100) == 1536
    assert candidate(n = 1000) == 51200000
    assert candidate(n = 300) == 82944
    assert candidate(n = 550) == 1555200
    assert candidate(n = 1200) == 174960000
    assert candidate(n = 600) == 2460375
    assert candidate(n = 4) == 4
    assert candidate(n = 1675) == 1990656000
    assert candidate(n = 1650) == 1769472000
    assert candidate(n = 1550) == 1093500000
    assert candidate(n = 1300) == 306110016
    assert candidate(n = 2) == 2
    assert candidate(n = 1024) == 60466176
    assert candidate(n = 8) == 9
    assert candidate(n = 1689) == 2109375000
    assert candidate(n = 800) == 12754584
    assert candidate(n = 400) == 311040
    assert candidate(n = 9) == 10
    assert candidate(n = 750) == 8748000
    assert candidate(n = 6) == 6
    assert candidate(n = 500) == 937500
    assert candidate(n = 7) == 8
    assert candidate(n = 1680) == 2025000000
    assert candidate(n = 1500) == 859963392


