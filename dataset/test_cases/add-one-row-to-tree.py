def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 0,depth = 2), tree_node([1, 0, 0, 2, None, None, 3, 4, 5, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 0,depth = 2), tree_node([1, 0, 0, 2, None, None, 3, 4, 5, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 0,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 0,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4]),val = 5,depth = 5), tree_node([1, 2, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4]),val = 5,depth = 5), tree_node([1, 2, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 10,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 10, 10, 10, 10, 10, 10, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 10,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 10, 10, 10, 10, 10, 10, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 1,depth = 3), tree_node([1, 2, 3, 1, 1, 1, 1, 4, None, None, 5, 6, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 1,depth = 3), tree_node([1, 2, 3, 1, 1, 1, 1, 4, None, None, 5, 6, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 2, None, 3]),val = 4,depth = 4), tree_node([1, None, 2, None, 3, 4, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 2, None, 3]),val = 4,depth = 4), tree_node([1, None, 2, None, 3, 4, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),val = 5,depth = 5), tree_node([1, None, 2, None, 3, None, 4, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),val = 5,depth = 5), tree_node([1, None, 2, None, 3, None, 4, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 4,depth = 4), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 4,depth = 4), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),val = 5,depth = 4), tree_node([1, None, 2, None, 3, 5, 5, None, None, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),val = 5,depth = 4), tree_node([1, None, 2, None, 3, 5, 5, None, None, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 5,depth = 4), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 5,depth = 4), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]),val = 1,depth = 3), tree_node([5, 4, 8, 1, 1, 1, 1, 11, None, None, None, 17, None, None, 4, 7, 1, None, None, 5, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]),val = 1,depth = 3), tree_node([5, 4, 8, 1, 1, 1, 1, 11, None, None, None, 17, None, None, 4, 7, 1, None, None, 5, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 1,depth = 1), tree_node([1, 1, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 1,depth = 1), tree_node([1, 1, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 0,depth = 3), tree_node([1, 2, 3, 0, 0, 0, 0, 4, None, None, 5, 6, None, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 0,depth = 3), tree_node([1, 2, 3, 0, 0, 0, 0, 4, None, None, 5, 6, None, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 8,depth = 1), tree_node([8, 1, None, 2, 3, 4, 5, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 8,depth = 1), tree_node([8, 1, None, 2, 3, 4, 5, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 8,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 8,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1]),val = 2,depth = 1), tree_node([2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1]),val = 2,depth = 1), tree_node([2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 3,depth = 3), tree_node([1, 2, 3, 3, 3, 3, 3, 4, None, None, 5, 6, None, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 3,depth = 3), tree_node([1, 2, 3, 3, 3, 3, 3, 4, None, None, 5, 6, None, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4]),val = 5,depth = 4), tree_node([1, 2, 3, 4, None, None, None, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4]),val = 5,depth = 4), tree_node([1, 2, 3, 4, None, None, None, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),val = 2,depth = 3), tree_node([1, None, 2, 2, 2, None, None, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),val = 2,depth = 3), tree_node([1, None, 2, 2, 2, None, None, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),val = 3,depth = 3), tree_node([5, 4, 8, 3, 3, 3, 3, 11, None, None, None, 13, None, None, 4, 7, 2, None, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),val = 3,depth = 3), tree_node([5, 4, 8, 3, 3, 3, 3, 11, None, None, None, 13, None, None, 4, 7, 2, None, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),val = 5,depth = 3), tree_node([1, None, 2, 5, 5, None, None, None, 3, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),val = 5,depth = 3), tree_node([1, None, 2, 5, 5, None, None, None, 3, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([4, 2, 6, 3, 1, 5]),val = 1,depth = 2), tree_node([4, 1, 1, 2, None, None, 6, 3, 1, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([4, 2, 6, 3, 1, 5]),val = 1,depth = 2), tree_node([4, 1, 1, 2, None, None, 6, 3, 1, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 4,depth = 5), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 4,depth = 5), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([4, 2, None, 3, 1]),val = 1,depth = 3), tree_node([4, 2, None, 1, 1, 3, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([4, 2, None, 3, 1]),val = 1,depth = 3), tree_node([4, 2, None, 1, 1, 3, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 2]),val = 3,depth = 2), tree_node([1, 3, 3, None, None, None, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 2]),val = 3,depth = 2), tree_node([1, 3, 3, None, None, None, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9]),val = 6,depth = 2), tree_node([1, 6, 6, 2, None, None, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9]),val = 6,depth = 2), tree_node([1, 6, 6, 2, None, None, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5]),val = -1,depth = 2), tree_node([1, -1, -1, 2, None, None, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5]),val = -1,depth = 2), tree_node([1, -1, -1, 2, None, None, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, None, 4]),val = 5,depth = 3), tree_node([1, 2, 3, 5, 5, 5, 5, None, None, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, None, 4]),val = 5,depth = 3), tree_node([1, 2, 3, 5, 5, 5, 5, None, None, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4]),val = 5,depth = 2), tree_node([1, 5, 5, 2, None, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4]),val = 5,depth = 2), tree_node([1, 5, 5, 2, None, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 4,depth = 2), tree_node([1, 4, 4, 2, None, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 4,depth = 2), tree_node([1, 4, 4, 2, None, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 3,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 3, 3, 3, 3, 3, 3, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 3,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 3, 3, 3, 3, 3, 3, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5]),val = 0,depth = 4), tree_node([1, 2, 3, 4, 5, None, None, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5]),val = 0,depth = 4), tree_node([1, 2, 3, 4, 5, None, None, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),val = 1,depth = 2), tree_node([5, 1, 1, 4, None, None, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),val = 1,depth = 2), tree_node([5, 1, 1, 4, None, None, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 0,depth = 2), tree_node([1, 0, 0, 2, None, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 0,depth = 2), tree_node([1, 0, 0, 2, None, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),val = 1,depth = 3), tree_node([1, None, 2, 1, 1, None, None, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),val = 1,depth = 3), tree_node([1, None, 2, 1, 1, None, None, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 2, None, 3]),val = 4,depth = 2), tree_node([1, 4, 4, None, None, None, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 2, None, 3]),val = 4,depth = 2), tree_node([1, 4, 4, None, None, None, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, 5, 3]),val = 2,depth = 3), tree_node([5, 4, 8, 2, 2, 2, 2, 11, None, None, None, 17, None, None, 4, 7, 1, 5, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, 5, 3]),val = 2,depth = 3), tree_node([5, 4, 8, 2, 2, 2, 2, 11, None, None, None, 17, None, None, 4, 7, 1, 5, 3])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 0,depth = 2), tree_node([1, 0, 0, 2, None, None, 3, 4, 5, 6, 7]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 0,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4]),val = 5,depth = 5), tree_node([1, 2, 3, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 10,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 10, 10, 10, 10, 10, 10, 10, 10]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 1,depth = 3), tree_node([1, 2, 3, 1, 1, 1, 1, 4, None, None, 5, 6, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3]),val = 4,depth = 4), tree_node([1, None, 2, None, 3, 4, 4]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),val = 5,depth = 5), tree_node([1, None, 2, None, 3, None, 4, 5, 5]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 4,depth = 4), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),val = 5,depth = 4), tree_node([1, None, 2, None, 3, 5, 5, None, None, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 5,depth = 4), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]),val = 1,depth = 3), tree_node([5, 4, 8, 1, 1, 1, 1, 11, None, None, None, 17, None, None, 4, 7, 1, None, None, 5, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),val = 1,depth = 1), tree_node([1, 1, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 0,depth = 3), tree_node([1, 2, 3, 0, 0, 0, 0, 4, None, None, 5, 6, None, None, 7]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 8,depth = 1), tree_node([8, 1, None, 2, 3, 4, 5, 6, 7]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 8,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8]))
    assert is_same_tree(candidate(root = tree_node([1]),val = 2,depth = 1), tree_node([2, 1]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 3,depth = 3), tree_node([1, 2, 3, 3, 3, 3, 3, 4, None, None, 5, 6, None, None, 7]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4]),val = 5,depth = 4), tree_node([1, 2, 3, 4, None, None, None, 5, 5]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),val = 2,depth = 3), tree_node([1, None, 2, 2, 2, None, None, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),val = 3,depth = 3), tree_node([5, 4, 8, 3, 3, 3, 3, 11, None, None, None, 13, None, None, 4, 7, 2, None, None, None, 1]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4]),val = 5,depth = 3), tree_node([1, None, 2, 5, 5, None, None, None, 3, None, 4]))
    assert is_same_tree(candidate(root = tree_node([4, 2, 6, 3, 1, 5]),val = 1,depth = 2), tree_node([4, 1, 1, 2, None, None, 6, 3, 1, 5]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 4,depth = 5), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(root = tree_node([4, 2, None, 3, 1]),val = 1,depth = 3), tree_node([4, 2, None, 1, 1, 3, None, None, 1]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2]),val = 3,depth = 2), tree_node([1, 3, 3, None, None, None, 2]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9]),val = 6,depth = 2), tree_node([1, 6, 6, 2, None, None, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5]),val = -1,depth = 2), tree_node([1, -1, -1, 2, None, None, 3, 4, 5]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, None, 4]),val = 5,depth = 3), tree_node([1, 2, 3, 5, 5, 5, 5, None, None, None, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4]),val = 5,depth = 2), tree_node([1, 5, 5, 2, None, None, 3, 4]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 4,depth = 2), tree_node([1, 4, 4, 2, None, None, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 3,depth = 4), tree_node([1, 2, 3, 4, 5, 6, 7, 3, 3, 3, 3, 3, 3, 3, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3, 4, 5]),val = 0,depth = 4), tree_node([1, 2, 3, 4, 5, None, None, 0, 0, 0, 0]))
    assert is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),val = 1,depth = 2), tree_node([5, 1, 1, 4, None, None, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]))
    assert is_same_tree(candidate(root = tree_node([1, 2, 3]),val = 0,depth = 2), tree_node([1, 0, 0, 2, None, None, 3]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),val = 1,depth = 3), tree_node([1, None, 2, 1, 1, None, None, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(root = tree_node([1, None, 2, None, 3]),val = 4,depth = 2), tree_node([1, 4, 4, None, None, None, 2, None, 3]))
    assert is_same_tree(candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, 5, 3]),val = 2,depth = 3), tree_node([5, 4, 8, 2, 2, 2, 2, 11, None, None, None, 17, None, None, 4, 7, 1, 5, 3]))


