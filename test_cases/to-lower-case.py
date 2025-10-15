def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "Hello") == "hello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Hello") == "hello": {e}')
    
    total += 1
    try:
        result = candidate(s = "here") == "here"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "here") == "here": {e}')
    
    total += 1
    try:
        result = candidate(s = "LOVELY") == "lovely"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "LOVELY") == "lovely": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "Hello") == "hello"
    assert candidate(s = "here") == "here"
    assert candidate(s = "LOVELY") == "lovely"


