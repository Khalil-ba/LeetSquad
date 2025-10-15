def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 19999800001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 19999800001: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 19801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 19801: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 199980001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 199980001: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 1998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 1998001: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 181: {e}')
    
    total += 1
    try:
        result = candidate(n = 15000) == 449970001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15000) == 449970001: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 19999400005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 19999400005: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 304773361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 304773361: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 112485001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 112485001: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 7996001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 7996001: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 4999900001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 4999900001: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 4901
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 4901: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 1741
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 1741: {e}')
    
    total += 1
    try:
        result = candidate(n = 60000) == 7199880001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60000) == 7199880001: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500) == 4497001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500) == 4497001: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 30000) == 1799940001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30000) == 1799940001: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 2002001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 2002001: {e}')
    
    total += 1
    try:
        result = candidate(n = 85000) == 14449830001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85000) == 14449830001: {e}')
    
    total += 1
    try:
        result = candidate(n = 80000) == 12799840001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80000) == 12799840001: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 799960001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 799960001: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 49990001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 49990001: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000) == 11249850001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000) == 11249850001: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 761
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 761: {e}')
    
    total += 1
    try:
        result = candidate(n = 40000) == 3199920001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40000) == 3199920001: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 421: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 12495001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 12495001: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000) == 161982001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000) == 161982001: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 79601
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 79601: {e}')
    
    total += 1
    try:
        result = candidate(n = 99998) == 19999000013
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99998) == 19999000013: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 499001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 499001: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 1201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 1201: {e}')
    
    total += 1
    try:
        result = candidate(n = 25000) == 1249950001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25000) == 1249950001: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 13
    assert candidate(n = 100000) == 19999800001
    assert candidate(n = 100) == 19801
    assert candidate(n = 10000) == 199980001
    assert candidate(n = 2) == 5
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 1998001
    assert candidate(n = 10) == 181
    assert candidate(n = 15000) == 449970001
    assert candidate(n = 99999) == 19999400005
    assert candidate(n = 12345) == 304773361
    assert candidate(n = 7500) == 112485001
    assert candidate(n = 2000) == 7996001
    assert candidate(n = 50000) == 4999900001
    assert candidate(n = 50) == 4901
    assert candidate(n = 5) == 41
    assert candidate(n = 30) == 1741
    assert candidate(n = 60000) == 7199880001
    assert candidate(n = 1500) == 4497001
    assert candidate(n = 4) == 25
    assert candidate(n = 30000) == 1799940001
    assert candidate(n = 1001) == 2002001
    assert candidate(n = 85000) == 14449830001
    assert candidate(n = 80000) == 12799840001
    assert candidate(n = 20000) == 799960001
    assert candidate(n = 5000) == 49990001
    assert candidate(n = 75000) == 11249850001
    assert candidate(n = 20) == 761
    assert candidate(n = 40000) == 3199920001
    assert candidate(n = 15) == 421
    assert candidate(n = 2500) == 12495001
    assert candidate(n = 9000) == 161982001
    assert candidate(n = 200) == 79601
    assert candidate(n = 99998) == 19999000013
    assert candidate(n = 500) == 499001
    assert candidate(n = 25) == 1201
    assert candidate(n = 25000) == 1249950001


