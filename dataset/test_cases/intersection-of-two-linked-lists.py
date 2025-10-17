def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(headA = list_node([1, 2, 3]),headB = list_node([4, 5, 1, 2, 3])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([1, 2, 3]),headB = list_node([4, 5, 1, 2, 3])) == None: {e}')
    
    total += 1
    try:
        result = candidate(headA = list_node([3, 6, 9, 12]),headB = list_node([15, 18, 21, 3])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([3, 6, 9, 12]),headB = list_node([15, 18, 21, 3])) == None: {e}')
    
    total += 1
    try:
        result = candidate(headA = list_node([2, 6, 4]),headB = list_node([1, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([2, 6, 4]),headB = list_node([1, 5])) == None: {e}')
    
    total += 1
    try:
        result = candidate(headA = list_node([1, 9, 1, 2, 4]),headB = list_node([3, 2, 4])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([1, 9, 1, 2, 4]),headB = list_node([3, 2, 4])) == None: {e}')
    
    total += 1
    try:
        result = candidate(headA = list_node([4, 1, 8, 4, 5]),headB = list_node([5, 6, 1, 8, 4, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([4, 1, 8, 4, 5]),headB = list_node([5, 6, 1, 8, 4, 5])) == None: {e}')
    
    total += 1
    try:
        result = candidate(headA = list_node([1, 2, 3, 4, 5]),headB = list_node([1, 2, 3, 4, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([1, 2, 3, 4, 5]),headB = list_node([1, 2, 3, 4, 5])) == None: {e}')
    
    total += 1
    try:
        result = candidate(headA = list_node([1]),headB = list_node([1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([1]),headB = list_node([1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(headA = list_node([1, 2, 3, 4, 5]),headB = list_node([6, 7, 8, 9, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([1, 2, 3, 4, 5]),headB = list_node([6, 7, 8, 9, 10])) == None: {e}')
    
    total += 1
    try:
        result = candidate(headA = list_node([1, 3, 5, 7, 9]),headB = list_node([2, 4, 6, 8, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([1, 3, 5, 7, 9]),headB = list_node([2, 4, 6, 8, 10])) == None: {e}')
    
    total += 1
    try:
        result = candidate(headA = list_node([1, 2, 3, 4, 5]),headB = list_node([6, 7, 8, 9, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(headA = list_node([1, 2, 3, 4, 5]),headB = list_node([6, 7, 8, 9, 1])) == None: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(headA = list_node([1, 2, 3]),headB = list_node([4, 5, 1, 2, 3])) == None
    assert candidate(headA = list_node([3, 6, 9, 12]),headB = list_node([15, 18, 21, 3])) == None
    assert candidate(headA = list_node([2, 6, 4]),headB = list_node([1, 5])) == None
    assert candidate(headA = list_node([1, 9, 1, 2, 4]),headB = list_node([3, 2, 4])) == None
    assert candidate(headA = list_node([4, 1, 8, 4, 5]),headB = list_node([5, 6, 1, 8, 4, 5])) == None
    assert candidate(headA = list_node([1, 2, 3, 4, 5]),headB = list_node([1, 2, 3, 4, 5])) == None
    assert candidate(headA = list_node([1]),headB = list_node([1])) == None
    assert candidate(headA = list_node([1, 2, 3, 4, 5]),headB = list_node([6, 7, 8, 9, 10])) == None
    assert candidate(headA = list_node([1, 3, 5, 7, 9]),headB = list_node([2, 4, 6, 8, 10])) == None
    assert candidate(headA = list_node([1, 2, 3, 4, 5]),headB = list_node([6, 7, 8, 9, 1])) == None


