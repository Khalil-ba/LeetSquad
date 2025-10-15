def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "Hello World") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Hello World") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "   fly me   to   the moon  ") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   fly me   to   the moon  ") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "luffy is still joyboy") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "luffy is still joyboy") == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "Hello World") == 5
    assert candidate(s = "   fly me   to   the moon  ") == 4
    assert candidate(s = "luffy is still joyboy") == 6


