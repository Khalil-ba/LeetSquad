def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "234Adas") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "234Adas") == True: {e}')
    
    total += 1
    try:
        result = candidate(word = "b3") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "b3") == False: {e}')
    
    total += 1
    try:
        result = candidate(word = "a3$e") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a3$e") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "234Adas") == True
    assert candidate(word = "b3") == False
    assert candidate(word = "a3$e") == False


