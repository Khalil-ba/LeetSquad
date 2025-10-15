def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(x = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(x = 23) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 23) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 18) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 18) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 90) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 90) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 57) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 57) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 99) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 99) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 81) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 81) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 45) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 45) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 13) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 13) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(x = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 54) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 54) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 234) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 234) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 621) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 621) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 111) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 111) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 72) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 72) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 42) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 42) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 153) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 153) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 216) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 216) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 990) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 990) == 18: {e}')
    
    total += 1
    try:
        result = candidate(x = 135) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 135) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 132) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 132) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 201) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 201) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 27) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 27) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 729) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 729) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 303) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 303) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 513) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 513) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 981) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 981) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 450) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 450) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 70) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 70) == 7: {e}')
    
    total += 1
    try:
        result = candidate(x = 270) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 270) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 999) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 999) == 27: {e}')
    
    total += 1
    try:
        result = candidate(x = 108) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 108) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 36) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 36) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 200) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 200) == 2: {e}')
    
    total += 1
    try:
        result = candidate(x = 756) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 756) == 18: {e}')
    
    total += 1
    try:
        result = candidate(x = 801) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 801) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 342) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 342) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 49) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 49) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 144) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 144) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 810) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 810) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 405) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 405) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 300) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 300) == 3: {e}')
    
    total += 1
    try:
        result = candidate(x = 504) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 504) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 180) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 180) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 369) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 369) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 75) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 75) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 900) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 900) == 9: {e}')
    
    total += 1
    try:
        result = candidate(x = 123) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 123) == -1: {e}')
    
    total += 1
    try:
        result = candidate(x = 198) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 198) == 18: {e}')
    
    total += 1
    try:
        result = candidate(x = 63) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 63) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(x = 50) == 5
    assert candidate(x = 23) == -1
    assert candidate(x = 10) == 1
    assert candidate(x = 18) == 9
    assert candidate(x = 1) == 1
    assert candidate(x = 90) == 9
    assert candidate(x = 57) == -1
    assert candidate(x = 99) == -1
    assert candidate(x = 81) == 9
    assert candidate(x = 45) == 9
    assert candidate(x = 13) == -1
    assert candidate(x = 100) == 1
    assert candidate(x = 12) == 3
    assert candidate(x = 54) == 9
    assert candidate(x = 234) == 9
    assert candidate(x = 621) == 9
    assert candidate(x = 111) == 3
    assert candidate(x = 72) == 9
    assert candidate(x = 42) == 6
    assert candidate(x = 153) == 9
    assert candidate(x = 216) == 9
    assert candidate(x = 990) == 18
    assert candidate(x = 135) == 9
    assert candidate(x = 132) == 6
    assert candidate(x = 201) == 3
    assert candidate(x = 27) == 9
    assert candidate(x = 729) == -1
    assert candidate(x = 303) == -1
    assert candidate(x = 513) == 9
    assert candidate(x = 981) == -1
    assert candidate(x = 450) == 9
    assert candidate(x = 70) == 7
    assert candidate(x = 270) == 9
    assert candidate(x = 999) == 27
    assert candidate(x = 108) == 9
    assert candidate(x = 36) == 9
    assert candidate(x = 200) == 2
    assert candidate(x = 756) == 18
    assert candidate(x = 801) == 9
    assert candidate(x = 342) == 9
    assert candidate(x = 49) == -1
    assert candidate(x = 144) == 9
    assert candidate(x = 810) == 9
    assert candidate(x = 405) == 9
    assert candidate(x = 300) == 3
    assert candidate(x = 504) == 9
    assert candidate(x = 180) == 9
    assert candidate(x = 369) == -1
    assert candidate(x = 75) == -1
    assert candidate(x = 900) == 9
    assert candidate(x = 123) == -1
    assert candidate(x = 198) == 18
    assert candidate(x = 63) == 9


