def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 625) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 9801) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9801) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 156) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 156) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2356) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2356) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 4001) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4001) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 144) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 144) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 8200) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8200) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5678) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5678) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2345) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2345) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1600) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1600) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3333) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3333) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 6250) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6250) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8402) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8402) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 98) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8401) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8401) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 38) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 38) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 7776) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7776) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 169) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 169) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 9500) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9500) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 7199) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7199) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 77) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5625) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5625) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7654) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7654) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 48) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 7777) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7777) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6400) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6400) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 325) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 325) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4999) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4999) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 4369) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4369) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 78) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 78) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3125) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3125) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 2017) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2017) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 196) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 196) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8999) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8999) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 84) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 625) == 1
    assert candidate(n = 8) == 2
    assert candidate(n = 100) == 1
    assert candidate(n = 4) == 1
    assert candidate(n = 12) == 3
    assert candidate(n = 16) == 1
    assert candidate(n = 17) == 2
    assert candidate(n = 10000) == 1
    assert candidate(n = 9) == 1
    assert candidate(n = 9876) == 3
    assert candidate(n = 6) == 3
    assert candidate(n = 9999) == 4
    assert candidate(n = 23) == 4
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 2
    assert candidate(n = 13) == 2
    assert candidate(n = 25) == 1
    assert candidate(n = 3) == 3
    assert candidate(n = 9801) == 1
    assert candidate(n = 156) == 4
    assert candidate(n = 2356) == 3
    assert candidate(n = 63) == 4
    assert candidate(n = 4001) == 2
    assert candidate(n = 144) == 1
    assert candidate(n = 12345) == 3
    assert candidate(n = 8200) == 2
    assert candidate(n = 5678) == 3
    assert candidate(n = 2345) == 3
    assert candidate(n = 1111) == 4
    assert candidate(n = 1600) == 1
    assert candidate(n = 7500) == 3
    assert candidate(n = 50) == 2
    assert candidate(n = 3333) == 3
    assert candidate(n = 300) == 3
    assert candidate(n = 28) == 4
    assert candidate(n = 6250) == 2
    assert candidate(n = 8402) == 2
    assert candidate(n = 3000) == 3
    assert candidate(n = 64) == 1
    assert candidate(n = 98) == 2
    assert candidate(n = 2) == 2
    assert candidate(n = 8401) == 3
    assert candidate(n = 1024) == 1
    assert candidate(n = 38) == 3
    assert candidate(n = 7776) == 3
    assert candidate(n = 8000) == 2
    assert candidate(n = 169) == 1
    assert candidate(n = 75) == 3
    assert candidate(n = 5000) == 2
    assert candidate(n = 9500) == 4
    assert candidate(n = 19) == 3
    assert candidate(n = 7199) == 4
    assert candidate(n = 77) == 3
    assert candidate(n = 1999) == 4
    assert candidate(n = 5625) == 1
    assert candidate(n = 81) == 1
    assert candidate(n = 7654) == 3
    assert candidate(n = 48) == 3
    assert candidate(n = 4321) == 2
    assert candidate(n = 7777) == 3
    assert candidate(n = 6400) == 1
    assert candidate(n = 325) == 2
    assert candidate(n = 9000) == 2
    assert candidate(n = 4999) == 4
    assert candidate(n = 4369) == 2
    assert candidate(n = 400) == 1
    assert candidate(n = 78) == 3
    assert candidate(n = 31) == 4
    assert candidate(n = 1234) == 2
    assert candidate(n = 3125) == 2
    assert candidate(n = 2017) == 2
    assert candidate(n = 85) == 2
    assert candidate(n = 196) == 1
    assert candidate(n = 8999) == 4
    assert candidate(n = 84) == 3


