def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "the sky is blue") == "blue is sky the"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "the sky is blue") == "blue is sky the": {e}')
    
    total += 1
    try:
        result = candidate(s = "  hello world  ") == "world hello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  hello world  ") == "world hello": {e}')
    
    total += 1
    try:
        result = candidate(s = "a good   example") == "example good a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a good   example") == "example good a": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "the sky is blue") == "blue is sky the"
    assert candidate(s = "  hello world  ") == "world hello"
    assert candidate(s = "a good   example") == "example good a"


