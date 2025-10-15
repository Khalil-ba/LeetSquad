def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "race a car") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "race a car") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = " ") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " ") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "race a car") == False
    assert candidate(s = " ") == True


