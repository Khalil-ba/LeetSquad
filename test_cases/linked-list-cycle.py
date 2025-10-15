def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([])) == False: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 2, 0, -4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 2, 0, -4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(head = list_node([1, 2])) == False
    assert candidate(head = list_node([1])) == False
    assert candidate(head = list_node([])) == False
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])) == False
    assert candidate(head = list_node([3, 2, 0, -4])) == False
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == False


