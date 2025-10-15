def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 83943898
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 83943898: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 1460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 1460: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 558399309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 558399309: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 86731066
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 86731066: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 232825199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 232825199: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 52805056
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 52805056: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == 974106352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == 974106352: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 295164156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 295164156: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 889526859
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 889526859: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 842828500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 842828500: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 291395991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 291395991: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 430509685
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 430509685: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 947613240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 947613240: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 106620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 106620: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 6058192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 6058192: {e}')
    
    total += 1
    try:
        result = candidate(n = 90) == 122933939
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90) == 122933939: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 935610434
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 935610434: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4) == 12
    assert candidate(n = 1) == 0
    assert candidate(n = 10) == 83943898
    assert candidate(n = 5) == 1460
    assert candidate(n = 3) == 0
    assert candidate(n = 125) == 558399309
    assert candidate(n = 100) == 86731066
    assert candidate(n = 50) == 232825199
    assert candidate(n = 30) == 52805056
    assert candidate(n = 2) == 0
    assert candidate(n = 80) == 974106352
    assert candidate(n = 8) == 295164156
    assert candidate(n = 250) == 889526859
    assert candidate(n = 75) == 842828500
    assert candidate(n = 20) == 291395991
    assert candidate(n = 15) == 430509685
    assert candidate(n = 9) == 947613240
    assert candidate(n = 6) == 106620
    assert candidate(n = 7) == 6058192
    assert candidate(n = 90) == 122933939
    assert candidate(n = 25) == 935610434


