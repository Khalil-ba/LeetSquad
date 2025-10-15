def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "hello") == "holle"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello") == "holle": {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode") == "leotcede"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode") == "leotcede": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "hello") == "holle"
    assert candidate(s = "leetcode") == "leotcede"


