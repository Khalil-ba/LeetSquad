def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "**|**|***|",queries = [[2, 5], [5, 9]]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "**|**|***|",queries = [[2, 5], [5, 9]]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "***||***",queries = [[0, 5], [2, 4]]) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "***||***",queries = [[0, 5], [2, 4]]) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "*|*|*|*|*|*|*|",queries = [[0, 7], [1, 6], [2, 5]]) == [3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "*|*|*|*|*|*|*|",queries = [[0, 7], [1, 6], [2, 5]]) == [3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "|||***|||",queries = [[0, 8], [1, 7], [2, 6]]) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "|||***|||",queries = [[0, 8], [1, 7], [2, 6]]) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "||*|*|*|*|*|*|",queries = [[0, 10], [1, 9], [2, 8], [3, 7]]) == [4, 4, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "||*|*|*|*|*|*|",queries = [[0, 10], [1, 9], [2, 8], [3, 7]]) == [4, 4, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "|||****|****|****||",queries = [[0, 10], [5, 15], [1, 4]]) == [4, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "|||****|****|****||",queries = [[0, 10], [5, 15], [1, 4]]) == [4, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "*|*|*|*|*|",queries = [[0, 5], [1, 4]]) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "*|*|*|*|*|",queries = [[0, 5], [1, 4]]) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "|*|*|*|*|*|*|*|*|*|*|",queries = [[0, 10], [1, 9], [2, 8], [3, 7]]) == [5, 3, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "|*|*|*|*|*|*|*|*|*|*|",queries = [[0, 10], [1, 9], [2, 8], [3, 7]]) == [5, 3, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "|||*****|||",queries = [[0, 2], [3, 8], [7, 10]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "|||*****|||",queries = [[0, 2], [3, 8], [7, 10]]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "*|*|*|*|*|*|*|*|*|*|*|",queries = [[0, 11], [1, 10], [2, 9], [3, 8]]) == [5, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "*|*|*|*|*|*|*|*|*|*|*|",queries = [[0, 11], [1, 10], [2, 9], [3, 8]]) == [5, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "*|*|*|*|*|*|*|*|*|*|",queries = [[0, 10], [1, 9], [2, 8], [3, 7]]) == [4, 4, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "*|*|*|*|*|*|*|*|*|*|",queries = [[0, 10], [1, 9], [2, 8], [3, 7]]) == [4, 4, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "***|**|*****|**||**|*",queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) == [9, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "***|**|*****|**||**|*",queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) == [9, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "***||****|**|",queries = [[0, 4], [5, 8], [9, 11]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "***||****|**|",queries = [[0, 4], [5, 8], [9, 11]]) == [0, 0, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "**|**|***|",queries = [[2, 5], [5, 9]]) == [2, 3]
    assert candidate(s = "***||***",queries = [[0, 5], [2, 4]]) == [0, 0]
    assert candidate(s = "*|*|*|*|*|*|*|",queries = [[0, 7], [1, 6], [2, 5]]) == [3, 2, 1]
    assert candidate(s = "|||***|||",queries = [[0, 8], [1, 7], [2, 6]]) == [3, 3, 3]
    assert candidate(s = "||*|*|*|*|*|*|",queries = [[0, 10], [1, 9], [2, 8], [3, 7]]) == [4, 4, 2, 2]
    assert candidate(s = "|||****|****|****||",queries = [[0, 10], [5, 15], [1, 4]]) == [4, 4, 0]
    assert candidate(s = "*|*|*|*|*|",queries = [[0, 5], [1, 4]]) == [2, 1]
    assert candidate(s = "|*|*|*|*|*|*|*|*|*|*|",queries = [[0, 10], [1, 9], [2, 8], [3, 7]]) == [5, 3, 3, 1]
    assert candidate(s = "|||*****|||",queries = [[0, 2], [3, 8], [7, 10]]) == [0, 0, 0]
    assert candidate(s = "*|*|*|*|*|*|*|*|*|*|*|",queries = [[0, 11], [1, 10], [2, 9], [3, 8]]) == [5, 4, 3, 2]
    assert candidate(s = "*|*|*|*|*|*|*|*|*|*|",queries = [[0, 10], [1, 9], [2, 8], [3, 7]]) == [4, 4, 2, 2]
    assert candidate(s = "***|**|*****|**||**|*",queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) == [9, 0, 0, 0, 0]
    assert candidate(s = "***||****|**|",queries = [[0, 4], [5, 8], [9, 11]]) == [0, 0, 0]


