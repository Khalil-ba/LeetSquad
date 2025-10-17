def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 3, 2],postorder = [3, 2, 1]), tree_node([1, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 3, 2],postorder = [3, 2, 1]), tree_node([1, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1],postorder = [1]), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1],postorder = [1]), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 3],postorder = [2, 3, 1]), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 3],postorder = [2, 3, 1]), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 7],postorder = [4, 5, 2, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 7],postorder = [4, 5, 2, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 5, 3],postorder = [4, 5, 2, 3, 1]), tree_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 5, 3],postorder = [4, 5, 2, 3, 1]), tree_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 3, 4, 5],postorder = [4, 5, 3, 2, 1]), tree_node([1, 2, None, 3, None, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 3, 4, 5],postorder = [4, 5, 3, 2, 1]), tree_node([1, 2, None, 3, None, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7],postorder = [4, 5, 2, 8, 9, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7],postorder = [4, 5, 2, 8, 9, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 3, 6, 11, 12, 7, 13, 2, 4, 8, 9, 5, 10],postorder = [11, 12, 6, 13, 7, 3, 8, 9, 4, 10, 5, 2, 1]), tree_node([1, 3, 2, 6, 7, 4, 5, 11, 12, 13, None, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 3, 6, 11, 12, 7, 13, 2, 4, 8, 9, 5, 10],postorder = [11, 12, 6, 13, 7, 3, 8, 9, 4, 10, 5, 2, 1]), tree_node([1, 3, 2, 6, 7, 4, 5, 11, 12, 13, None, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 3, 2, 5, 4, 6],postorder = [3, 4, 5, 2, 6, 1]), tree_node([1, 3, 2, None, None, 5, 6, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 3, 2, 5, 4, 6],postorder = [3, 4, 5, 2, 6, 1]), tree_node([1, 3, 2, None, None, 5, 6, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 3, 5, 6, 2, 4, 7],postorder = [5, 6, 3, 7, 4, 2, 1]), tree_node([1, 3, 2, 5, 6, 4, None, None, None, None, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 3, 5, 6, 2, 4, 7],postorder = [5, 6, 3, 7, 4, 2, 1]), tree_node([1, 3, 2, 5, 6, 4, None, None, None, None, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 7, 8, 5, 9, 3, 6],postorder = [7, 8, 4, 9, 5, 2, 6, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, None, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 7, 8, 5, 9, 3, 6],postorder = [7, 8, 4, 9, 5, 2, 6, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, None, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 7, 13, 14],postorder = [8, 9, 4, 10, 11, 5, 2, 12, 6, 13, 14, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, 13, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 7, 13, 14],postorder = [8, 9, 4, 10, 11, 5, 2, 12, 6, 13, 14, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, 13, 14])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 10, 3, 6, 11, 12, 7, 13, 14],postorder = [8, 9, 4, 10, 5, 2, 11, 12, 6, 13, 14, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, 11, 12, 13, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 10, 3, 6, 11, 12, 7, 13, 14],postorder = [8, 9, 4, 10, 5, 2, 11, 12, 6, 13, 14, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, 11, 12, 13, 14])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [6, 2, 1, 0, 3, 5, 4, 8, 7, 9],postorder = [0, 1, 5, 4, 3, 2, 7, 9, 8, 6]), tree_node([6, 2, 8, 1, 3, 7, 9, 0, None, 5, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [6, 2, 1, 0, 3, 5, 4, 8, 7, 9],postorder = [0, 1, 5, 4, 3, 2, 7, 9, 8, 6]), tree_node([6, 2, 8, 1, 3, 7, 9, 0, None, 5, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 8, 5, 9, 3, 6, 10, 7, 11],postorder = [8, 4, 9, 5, 2, 10, 6, 11, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, 10, None, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 8, 5, 9, 3, 6, 10, 7, 11],postorder = [8, 4, 9, 5, 2, 10, 6, 11, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, 10, None, 11])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 3, 6, 5, 2, 4, 7, 8, 9],postorder = [6, 5, 3, 8, 9, 7, 4, 2, 1]), tree_node([1, 3, 2, 6, 5, 4, None, None, None, None, None, 7, None, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 3, 6, 5, 2, 4, 7, 8, 9],postorder = [6, 5, 3, 8, 9, 7, 4, 2, 1]), tree_node([1, 3, 2, 6, 5, 4, None, None, None, None, None, 7, None, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 3, 6, 7],postorder = [8, 9, 4, 5, 2, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 3, 6, 7],postorder = [8, 9, 4, 5, 2, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [5, 4, 2, 1, 3, 6, 7, 8, 9, 10],postorder = [1, 3, 2, 4, 10, 9, 8, 7, 6, 5]), tree_node([5, 4, 6, 2, None, 7, None, 1, 3, 8, None, None, None, None, None, 9, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [5, 4, 2, 1, 3, 6, 7, 8, 9, 10],postorder = [1, 3, 2, 4, 10, 9, 8, 7, 6, 5]), tree_node([5, 4, 6, 2, None, 7, None, 1, 3, 8, None, None, None, None, None, 9, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 3, 2, 5, 4, 6],postorder = [2, 4, 6, 5, 3, 1]), tree_node([1, 3, None, 2, 5, None, None, 4, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 3, 2, 5, 4, 6],postorder = [2, 4, 6, 5, 3, 1]), tree_node([1, 3, None, 2, 5, None, None, 4, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 8, 7, 9],postorder = [4, 5, 2, 8, 6, 9, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, None, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 8, 7, 9],postorder = [4, 5, 2, 8, 6, 9, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, None, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 7, 8, 9],postorder = [4, 5, 2, 6, 8, 9, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 7, 8, 9],postorder = [4, 5, 2, 6, 8, 9, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 3, 5, 4, 2, 6, 7],postorder = [5, 4, 3, 6, 7, 2, 1]), tree_node([1, 3, 2, 5, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 3, 5, 4, 2, 6, 7],postorder = [5, 4, 3, 6, 7, 2, 1]), tree_node([1, 3, 2, 5, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 3, 2, 6, 5, 4, 7, 9, 8, 11, 10],postorder = [2, 5, 6, 4, 3, 9, 10, 11, 8, 7, 1]), tree_node([1, 3, 7, 2, 6, 9, 8, None, None, 5, 4, None, None, 11, None, None, None, None, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 3, 2, 6, 5, 4, 7, 9, 8, 11, 10],postorder = [2, 5, 6, 4, 3, 9, 10, 11, 8, 7, 1]), tree_node([1, 3, 7, 2, 6, 9, 8, None, None, 5, 4, None, None, 11, None, None, None, None, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 3, 5, 6],postorder = [4, 2, 6, 5, 3, 1]), tree_node([1, 2, 3, 4, None, 5, None, None, None, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 3, 5, 6],postorder = [4, 2, 6, 5, 3, 1]), tree_node([1, 2, 3, 4, None, 5, None, None, None, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 10, 3, 6, 7],postorder = [8, 9, 4, 10, 5, 2, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 10, 3, 6, 7],postorder = [8, 9, 4, 10, 5, 2, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7, 10, 11],postorder = [4, 5, 2, 8, 9, 6, 10, 11, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9, 10, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7, 10, 11],postorder = [4, 5, 2, 8, 9, 6, 10, 11, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9, 10, 11])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 3, 5, 6, 4, 7, 8],postorder = [5, 6, 3, 7, 8, 4, 2, 1]), tree_node([1, 2, None, 3, 4, 5, 6, 7, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 3, 5, 6, 4, 7, 8],postorder = [5, 6, 3, 7, 8, 4, 2, 1]), tree_node([1, 2, None, 3, 4, 5, 6, 7, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 5, 9, 10, 6, 7, 3, 8, 4],postorder = [9, 10, 5, 7, 6, 2, 8, 4, 3, 1]), tree_node([1, 2, 3, 5, 6, 8, 4, 9, 10, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 5, 9, 10, 6, 7, 3, 8, 4],postorder = [9, 10, 5, 7, 6, 2, 8, 4, 3, 1]), tree_node([1, 2, 3, 5, 6, 8, 4, 9, 10, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(preorder = [1, 2, 4, 7, 8, 5, 9, 6, 3, 10, 11],postorder = [7, 8, 4, 9, 5, 6, 2, 10, 11, 3, 1]), tree_node([1, 2, 3, 4, 5, 10, 11, 7, 8, 9, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(preorder = [1, 2, 4, 7, 8, 5, 9, 6, 3, 10, 11],postorder = [7, 8, 4, 9, 5, 6, 2, 10, 11, 3, 1]), tree_node([1, 2, 3, 4, 5, 10, 11, 7, 8, 9, 6])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_tree(candidate(preorder = [1, 3, 2],postorder = [3, 2, 1]), tree_node([1, 3, 2]))
    assert is_same_tree(candidate(preorder = [1],postorder = [1]), tree_node([1]))
    assert is_same_tree(candidate(preorder = [1, 2, 3],postorder = [2, 3, 1]), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 7],postorder = [4, 5, 2, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 5, 3],postorder = [4, 5, 2, 3, 1]), tree_node([1, 2, 3, 4, 5]))
    assert is_same_tree(candidate(preorder = [1, 2, 3, 4, 5],postorder = [4, 5, 3, 2, 1]), tree_node([1, 2, None, 3, None, 4, 5]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7],postorder = [4, 5, 2, 8, 9, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9]))
    assert is_same_tree(candidate(preorder = [1, 3, 6, 11, 12, 7, 13, 2, 4, 8, 9, 5, 10],postorder = [11, 12, 6, 13, 7, 3, 8, 9, 4, 10, 5, 2, 1]), tree_node([1, 3, 2, 6, 7, 4, 5, 11, 12, 13, None, 8, 9, 10]))
    assert is_same_tree(candidate(preorder = [1, 3, 2, 5, 4, 6],postorder = [3, 4, 5, 2, 6, 1]), tree_node([1, 3, 2, None, None, 5, 6, 4]))
    assert is_same_tree(candidate(preorder = [1, 3, 5, 6, 2, 4, 7],postorder = [5, 6, 3, 7, 4, 2, 1]), tree_node([1, 3, 2, 5, 6, 4, None, None, None, None, None, 7]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 7, 8, 5, 9, 3, 6],postorder = [7, 8, 4, 9, 5, 2, 6, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, None, 7, 8, 9]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 7, 13, 14],postorder = [8, 9, 4, 10, 11, 5, 2, 12, 6, 13, 14, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, 13, 14]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 10, 3, 6, 11, 12, 7, 13, 14],postorder = [8, 9, 4, 10, 5, 2, 11, 12, 6, 13, 14, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, 11, 12, 13, 14]))
    assert is_same_tree(candidate(preorder = [6, 2, 1, 0, 3, 5, 4, 8, 7, 9],postorder = [0, 1, 5, 4, 3, 2, 7, 9, 8, 6]), tree_node([6, 2, 8, 1, 3, 7, 9, 0, None, 5, 4]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 8, 5, 9, 3, 6, 10, 7, 11],postorder = [8, 4, 9, 5, 2, 10, 6, 11, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, 10, None, 11]))
    assert is_same_tree(candidate(preorder = [1, 3, 6, 5, 2, 4, 7, 8, 9],postorder = [6, 5, 3, 8, 9, 7, 4, 2, 1]), tree_node([1, 3, 2, 6, 5, 4, None, None, None, None, None, 7, None, 8, 9]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 3, 6, 7],postorder = [8, 9, 4, 5, 2, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_tree(candidate(preorder = [5, 4, 2, 1, 3, 6, 7, 8, 9, 10],postorder = [1, 3, 2, 4, 10, 9, 8, 7, 6, 5]), tree_node([5, 4, 6, 2, None, 7, None, 1, 3, 8, None, None, None, None, None, 9, None, 10]))
    assert is_same_tree(candidate(preorder = [1, 3, 2, 5, 4, 6],postorder = [2, 4, 6, 5, 3, 1]), tree_node([1, 3, None, 2, 5, None, None, 4, 6]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 8, 7, 9],postorder = [4, 5, 2, 8, 6, 9, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, None, 9]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 7, 8, 9],postorder = [4, 5, 2, 6, 8, 9, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9]))
    assert is_same_tree(candidate(preorder = [1, 3, 5, 4, 2, 6, 7],postorder = [5, 4, 3, 6, 7, 2, 1]), tree_node([1, 3, 2, 5, 4, 6, 7]))
    assert is_same_tree(candidate(preorder = [1, 3, 2, 6, 5, 4, 7, 9, 8, 11, 10],postorder = [2, 5, 6, 4, 3, 9, 10, 11, 8, 7, 1]), tree_node([1, 3, 7, 2, 6, 9, 8, None, None, 5, 4, None, None, 11, None, None, None, None, None, 10]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 3, 5, 6],postorder = [4, 2, 6, 5, 3, 1]), tree_node([1, 2, 3, 4, None, 5, None, None, None, 6]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 8, 9, 5, 10, 3, 6, 7],postorder = [8, 9, 4, 10, 5, 2, 6, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7, 10, 11],postorder = [4, 5, 2, 8, 9, 6, 10, 11, 7, 3, 1]), tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9, 10, 11]))
    assert is_same_tree(candidate(preorder = [1, 2, 3, 5, 6, 4, 7, 8],postorder = [5, 6, 3, 7, 8, 4, 2, 1]), tree_node([1, 2, None, 3, 4, 5, 6, 7, 8]))
    assert is_same_tree(candidate(preorder = [1, 2, 5, 9, 10, 6, 7, 3, 8, 4],postorder = [9, 10, 5, 7, 6, 2, 8, 4, 3, 1]), tree_node([1, 2, 3, 5, 6, 8, 4, 9, 10, 7]))
    assert is_same_tree(candidate(preorder = [1, 2, 4, 7, 8, 5, 9, 6, 3, 10, 11],postorder = [7, 8, 4, 9, 5, 6, 2, 10, 11, 3, 1]), tree_node([1, 2, 3, 4, 5, 10, 11, 7, 8, 9, 6]))


