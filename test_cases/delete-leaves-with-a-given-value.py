def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, None, 2, None, 2]),target = 2), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, None, 2, None, 2]),target = 2), tree_node([1])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 1000, 1000, 1000, 1000, 1000, 1000]),target = 1000) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 1000, 1000, 1000, 1000, 1000, 1000]),target = 1000) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),target = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),target = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, 10]),target = 5), tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, 10]),target = 5), tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 2, None, 2, 4]),target = 2), tree_node([1, None, 3, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 2, None, 2, 4]),target = 2), tree_node([1, None, 3, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 2, 2, 4, 2, None, 2, None, 2, None, 2]),target = 2), tree_node([1, 2, 3, 4, None, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 2, 2, 4, 2, None, 2, None, 2, None, 2]),target = 2), tree_node([1, 2, 3, 4, None, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 3, 3, 3, 2]),target = 3), tree_node([1, 3, None, None, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 3, 3, 3, 2]),target = 3), tree_node([1, 3, None, None, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, None, 4]),target = 4), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, None, 4]),target = 4), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),target = 15), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),target = 15), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]),target = 3), tree_node([1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]),target = 3), tree_node([1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3]),target = 4), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3]),target = 4), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),target = 2), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),target = 2), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),target = 2), tree_node([1, None, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),target = 2), tree_node([1, None, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, None, 1, None, 1]),target = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, None, 1, None, 1]),target = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3]),target = 2), tree_node([1, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3]),target = 2), tree_node([1, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),target = 7), tree_node([1, 2, 3, 4, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),target = 7), tree_node([1, 2, 3, 4, 5, 6])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1]),target = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1]),target = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),target = 2), tree_node([1, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),target = 2), tree_node([1, None, 3])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1]),target = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1]),target = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),target = 10), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),target = 10), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 3, None, 4, 5, None, 6, 7]),target = 2), tree_node([1, None, 3, None, 4, 5, None, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 3, None, 4, 5, None, 6, 7]),target = 2), tree_node([1, None, 3, None, 4, 5, None, 6, 7])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1]),target = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1]),target = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),target = 5), tree_node([1, 2, 3, None, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),target = 5), tree_node([1, 2, 3, None, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 4]),target = 2), tree_node([1, None, 3, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 4]),target = 2), tree_node([1, None, 3, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 3, 3, 3]),target = 3), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 3, 3, 3]),target = 3), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 3, 2, 2, None, 4, 2, None, 2]),target = 2), tree_node([1, None, 3, 2, None, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 3, 2, 2, None, 4, 2, None, 2]),target = 2), tree_node([1, None, 3, 2, None, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),target = 3), tree_node([1, 2, 3, 4, 5, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),target = 3), tree_node([1, 2, 3, 4, 5, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 2]),target = 2), tree_node([1, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 2]),target = 2), tree_node([1, None, 3])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, 1, 1, 1, 1, 1]),target = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, 1, 1, 1, 1, 1]),target = 1) == None: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_tree(candidate(root = tree_node([1, 2, None, 2, None, 2]),target = 2), tree_node([1]))
    assert candidate(root = tree_node([1000, 1000, 1000, 1000, 1000, 1000, 1000]),target = 1000) == None
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, 10]),target = 5), tree_node([1, 2, 3, None, 4, 5, None, 6, 7, None, 8, 9, 10]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 2, None, 2, 4]),target = 2), tree_node([1, None, 3, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 2, 2, 4, 2, None, 2, None, 2, None, 2]),target = 2), tree_node([1, 2, 3, 4, None, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 3, 3, 3, 2]),target = 3), tree_node([1, 3, None, None, 2]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, None, 4]),target = 4), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),target = 15), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]),target = 3), tree_node([1, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3]),target = 4), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),target = 2), tree_node([1]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),target = 2), tree_node([1, None, 3, 4, 5]))
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3]),target = 2), tree_node([1, None, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),target = 7), tree_node([1, 2, 3, 4, 5, 6]))
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),target = 2), tree_node([1, None, 3]))
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),target = 10), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, 11, 12, 13, 14, 15]))
    assert is_same_tree(candidate(root = tree_node([1, None, 3, None, 4, 5, None, 6, 7]),target = 2), tree_node([1, None, 3, None, 4, 5, None, 6, 7]))
    assert candidate(root = tree_node([1]),target = 1) == None
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),target = 5), tree_node([1, 2, 3, None, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 4]),target = 2), tree_node([1, None, 3, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, None, 3, 3, 3]),target = 3), tree_node([1]))
    assert is_same_tree(candidate(root = tree_node([1, None, 3, 2, 2, None, 4, 2, None, 2]),target = 2), tree_node([1, None, 3, 2, None, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),target = 3), tree_node([1, 2, 3, 4, 5, 6, 7]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 2, 2, 2, 2]),target = 2), tree_node([1, None, 3]))
    assert candidate(root = tree_node([1, None, 1, 1, 1, 1, 1, 1]),target = 1) == None


