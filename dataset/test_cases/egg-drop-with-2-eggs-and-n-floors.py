def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 450) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 600) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 990) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 990) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 850) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 850) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 900) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 995) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 995) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 505) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 505) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 650) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 550) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 460) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 460) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 501) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 501) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 997) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 997) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 925) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 925) == 43: {e}')
    
    total += 1
    try:
        result = candidate(n = 504) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 504) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 350) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 503) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 503) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 800) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 39: {e}')
    
    total += 1
    try:
        result = candidate(n = 502) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 502) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 950) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 700) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 366) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 366) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 998) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 998) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 4
    assert candidate(n = 1000) == 45
    assert candidate(n = 5) == 3
    assert candidate(n = 81) == 13
    assert candidate(n = 999) == 45
    assert candidate(n = 15) == 5
    assert candidate(n = 64) == 11
    assert candidate(n = 450) == 30
    assert candidate(n = 600) == 35
    assert candidate(n = 6) == 3
    assert candidate(n = 2) == 2
    assert candidate(n = 100) == 14
    assert candidate(n = 500) == 32
    assert candidate(n = 50) == 10
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 4
    assert candidate(n = 300) == 24
    assert candidate(n = 990) == 44
    assert candidate(n = 850) == 41
    assert candidate(n = 125) == 16
    assert candidate(n = 900) == 42
    assert candidate(n = 995) == 45
    assert candidate(n = 505) == 32
    assert candidate(n = 650) == 36
    assert candidate(n = 550) == 33
    assert candidate(n = 460) == 30
    assert candidate(n = 99) == 14
    assert candidate(n = 501) == 32
    assert candidate(n = 250) == 22
    assert candidate(n = 75) == 12
    assert candidate(n = 997) == 45
    assert candidate(n = 925) == 43
    assert candidate(n = 504) == 32
    assert candidate(n = 350) == 26
    assert candidate(n = 503) == 32
    assert candidate(n = 150) == 17
    assert candidate(n = 800) == 40
    assert candidate(n = 200) == 20
    assert candidate(n = 400) == 28
    assert candidate(n = 750) == 39
    assert candidate(n = 502) == 32
    assert candidate(n = 950) == 44
    assert candidate(n = 700) == 37
    assert candidate(n = 366) == 27
    assert candidate(n = 998) == 45
    assert candidate(n = 25) == 7


