def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 100000) == 49972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 49972: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 4996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 4996: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 502: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 32000) == 15996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32000) == 15996: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 49972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 49972: {e}')
    
    total += 1
    try:
        result = candidate(n = 15000) == 7501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15000) == 7501: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 6172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 6172: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 3747
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 3747: {e}')
    
    total += 1
    try:
        result = candidate(n = 90000) == 44975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90000) == 44975: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 24985
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 24985: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 60000) == 29976
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60000) == 29976: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 30000) == 14993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30000) == 14993: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 45000) == 22491
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45000) == 22491: {e}')
    
    total += 1
    try:
        result = candidate(n = 85000) == 42478
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85000) == 42478: {e}')
    
    total += 1
    try:
        result = candidate(n = 80000) == 39982
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80000) == 39982: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 9996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 9996: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000) == 37487
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000) == 37487: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 4995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 4995: {e}')
    
    total += 1
    try:
        result = candidate(n = 50001) == 24986
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50001) == 24986: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 199: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 249: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 25000) == 12495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25000) == 12495: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 100000) == 49972
    assert candidate(n = 100) == 49
    assert candidate(n = 15) == 7
    assert candidate(n = 10000) == 4996
    assert candidate(n = 6) == 3
    assert candidate(n = 20) == 10
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 502
    assert candidate(n = 10) == 5
    assert candidate(n = 32000) == 15996
    assert candidate(n = 99999) == 49972
    assert candidate(n = 15000) == 7501
    assert candidate(n = 3) == 1
    assert candidate(n = 12345) == 6172
    assert candidate(n = 7500) == 3747
    assert candidate(n = 90000) == 44975
    assert candidate(n = 50000) == 24985
    assert candidate(n = 50) == 25
    assert candidate(n = 5) == 3
    assert candidate(n = 300) == 150
    assert candidate(n = 30) == 15
    assert candidate(n = 60000) == 29976
    assert candidate(n = 40) == 20
    assert candidate(n = 4) == 2
    assert candidate(n = 30000) == 14993
    assert candidate(n = 2) == 1
    assert candidate(n = 45000) == 22491
    assert candidate(n = 85000) == 42478
    assert candidate(n = 80000) == 39982
    assert candidate(n = 8) == 4
    assert candidate(n = 20000) == 9996
    assert candidate(n = 5000) == 2500
    assert candidate(n = 75000) == 37487
    assert candidate(n = 9999) == 4995
    assert candidate(n = 50001) == 24986
    assert candidate(n = 200) == 100
    assert candidate(n = 400) == 199
    assert candidate(n = 9) == 4
    assert candidate(n = 500) == 249
    assert candidate(n = 7) == 4
    assert candidate(n = 25000) == 12495


