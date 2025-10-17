def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5]),val = 3) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5]),val = 3) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 7), tree_node([7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 7), tree_node([7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([2, 1, 3]),val = 1), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([2, 1, 3]),val = 1), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 6), tree_node([6, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 6), tree_node([6, None, 7])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1]),val = 2) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1]),val = 2) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),val = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),val = 10) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([25, 15, 50, 10, 22, 35, 70, 5, 12, 18, 24, 30, 40, 60, 80]),val = 35), tree_node([35, 30, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([25, 15, 50, 10, 22, 35, 70, 5, 12, 18, 24, 30, 40, 60, 80]),val = 35), tree_node([35, 30, 40])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2]),val = 3) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2]),val = 3) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([4, 2, 7, 1, 3]),val = 2), tree_node([2, 1, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([4, 2, 7, 1, 3]),val = 2), tree_node([2, 1, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 0, 2]),val = 1), tree_node([1, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 0, 2]),val = 1), tree_node([1, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),val = 7), tree_node([7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),val = 7), tree_node([7])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 20) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 20) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([2, 1, 3]),val = 2), tree_node([2, 1, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([2, 1, 3]),val = 2), tree_node([2, 1, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 10), tree_node([10, 5, 15, 3, 7, 12, 18]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 10), tree_node([10, 5, 15, 3, 7, 12, 18])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 4) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),val = 13), tree_node([13, 12, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),val = 13), tree_node([13, 12, 14])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 28), tree_node([28]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 28), tree_node([28])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 3), tree_node([3, 2, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 3), tree_node([3, 2, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 4), tree_node([4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 4), tree_node([4])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3]),val = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3]),val = 4) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, 0, 15, None, None, 14, 17]),val = 15), tree_node([15, 14, 17]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, 0, 15, None, None, 14, 17]),val = 15), tree_node([15, 14, 17])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 6), tree_node([6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 6), tree_node([6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),val = 15), tree_node([15, None, 18]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),val = 15), tree_node([15, None, 18])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 50, 10, 22, 35, 70, 5, 12, 18, 24, 30, 40, 60, 80]),val = 100) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 50, 10, 22, 35, 70, 5, 12, 18, 24, 30, 40, 60, 80]),val = 100) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, 20, 28, 35, 55, 65, 85, 95]),val = 30), tree_node([30, 28, 35]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, 20, 28, 35, 55, 65, 85, 95]),val = 30), tree_node([30, 28, 35])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([15, 9, 21, 7, 13, 18, 23, 5, None, 10, 14, None, None, None, None, 11, None]),val = 14), tree_node([14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([15, 9, 21, 7, 13, 18, 23, 5, None, 10, 14, None, None, None, None, 11, None]),val = 14), tree_node([14])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 15), tree_node([15, 12, 18]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 15), tree_node([15, 12, 18])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([3, 1, 4, None, 2]),val = 2), tree_node([2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([3, 1, 4, None, 2]),val = 2), tree_node([2])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 1) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),val = 20) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),val = 20) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 29) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 29) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([2, 1, 3, 4, None, None, 7]),val = 2), tree_node([2, 1, 3, 4, None, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([2, 1, 3, 4, None, None, 7]),val = 2), tree_node([2, 1, 3, 4, None, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 1), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 1), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 30), tree_node([30, 25, 35, 22, 28, 32, 38]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 30), tree_node([30, 25, 35, 22, 28, 32, 38])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([25, 15, 50, 10, 22, 35, 70, 5, 12, 18, 24, 30, 40, 60, 80]),val = 5), tree_node([5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([25, 15, 50, 10, 22, 35, 70, 5, 12, 18, 24, 30, 40, 60, 80]),val = 5), tree_node([5])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, None, 1, 6, None, 4, 7, 13, None, None, None, None, None, None]),val = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, None, 1, 6, None, 4, 7, 13, None, None, None, None, None, None]),val = 1) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),val = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),val = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 7, 1, 3]),val = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 7, 1, 3]),val = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2]),val = 2) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2]),val = 2) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 8) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1, None, 2]),val = 2), tree_node([2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1, None, 2]),val = 2), tree_node([2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([1]),val = 1), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([1]),val = 1), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([5]),val = 5), tree_node([5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([5]),val = 5), tree_node([5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 18), tree_node([18]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 18), tree_node([18])): {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 0) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 0) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),val = 20) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),val = 20) == None: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 8) == None
    assert candidate(root = tree_node([5]),val = 3) == None
    assert is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 7), tree_node([7]))
    assert is_same_tree(candidate(root = tree_node([2, 1, 3]),val = 1), tree_node([1]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 6), tree_node([6, None, 7]))
    assert candidate(root = tree_node([1]),val = 2) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),val = 10) == None
    assert is_same_tree(candidate(root = tree_node([25, 15, 50, 10, 22, 35, 70, 5, 12, 18, 24, 30, 40, 60, 80]),val = 35), tree_node([35, 30, 40]))
    assert candidate(root = tree_node([1, 0, 2]),val = 3) == None
    assert is_same_tree(candidate(root = tree_node([4, 2, 7, 1, 3]),val = 2), tree_node([2, 1, 3]))
    assert is_same_tree(candidate(root = tree_node([1, 0, 2]),val = 1), tree_node([1, 0, 2]))
    assert is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),val = 7), tree_node([7]))
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 20) == None
    assert is_same_tree(candidate(root = tree_node([2, 1, 3]),val = 2), tree_node([2, 1, 3]))
    assert is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 10), tree_node([10, 5, 15, 3, 7, 12, 18]))
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 4) == None
    assert is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),val = 13), tree_node([13, 12, 14]))
    assert is_same_tree(candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 28), tree_node([28]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 3), tree_node([3, 2, 4]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 4), tree_node([4]))
    assert candidate(root = tree_node([2, 1, 3]),val = 4) == None
    assert is_same_tree(candidate(root = tree_node([1, 0, 15, None, None, 14, 17]),val = 15), tree_node([15, 14, 17]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 6), tree_node([6]))
    assert is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),val = 15), tree_node([15, None, 18]))
    assert candidate(root = tree_node([25, 15, 50, 10, 22, 35, 70, 5, 12, 18, 24, 30, 40, 60, 80]),val = 100) == None
    assert is_same_tree(candidate(root = tree_node([50, 25, 75, 10, 30, 60, 90, 5, 20, 28, 35, 55, 65, 85, 95]),val = 30), tree_node([30, 28, 35]))
    assert is_same_tree(candidate(root = tree_node([15, 9, 21, 7, 13, 18, 23, 5, None, 10, 14, None, None, None, None, 11, None]),val = 14), tree_node([14]))
    assert is_same_tree(candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 15), tree_node([15, 12, 18]))
    assert is_same_tree(candidate(root = tree_node([3, 1, 4, None, 2]),val = 2), tree_node([2]))
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 1) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),val = 20) == None
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 29) == None
    assert is_same_tree(candidate(root = tree_node([2, 1, 3, 4, None, None, 7]),val = 2), tree_node([2, 1, 3, 4, None, None, 7]))
    assert is_same_tree(candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 1), tree_node([1]))
    assert is_same_tree(candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 18, 22, 28, 32, 38]),val = 30), tree_node([30, 25, 35, 22, 28, 32, 38]))
    assert is_same_tree(candidate(root = tree_node([25, 15, 50, 10, 22, 35, 70, 5, 12, 18, 24, 30, 40, 60, 80]),val = 5), tree_node([5]))
    assert candidate(root = tree_node([8, 3, 10, None, 1, 6, None, 4, 7, 13, None, None, None, None, None, None]),val = 1) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),val = 5) == None
    assert candidate(root = tree_node([4, 2, 7, 1, 3]),val = 5) == None
    assert candidate(root = tree_node([1, 2]),val = 2) == None
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),val = 8) == None
    assert is_same_tree(candidate(root = tree_node([1, None, 2]),val = 2), tree_node([2]))
    assert is_same_tree(candidate(root = tree_node([1]),val = 1), tree_node([1]))
    assert is_same_tree(candidate(root = tree_node([5]),val = 5), tree_node([5]))
    assert is_same_tree(candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),val = 18), tree_node([18]))
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),val = 0) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),val = 6) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),val = 20) == None


