def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6]),x = 5,y = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6]),x = 5,y = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5]),x = 5,y = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5]),x = 5,y = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 9,y = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 9,y = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, 6]),x = 5,y = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, 6]),x = 5,y = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 2,y = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 2,y = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, None, 9]),x = 6,y = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, None, 9]),x = 6,y = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, 12, 13]),x = 10,y = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, 12, 13]),x = 10,y = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4]),x = 4,y = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4]),x = 4,y = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7]),x = 6,y = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7]),x = 6,y = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4]),x = 2,y = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4]),x = 2,y = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),x = 4,y = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),x = 4,y = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 3,y = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 3,y = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 4,y = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 4,y = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 2,y = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 2,y = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7]),x = 6,y = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7]),x = 6,y = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 6, 7, 8, 9]),x = 8,y = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 6, 7, 8, 9]),x = 8,y = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, 7, 8]),x = 7,y = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, 7, 8]),x = 7,y = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 6, 7]),x = 6,y = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 6, 7]),x = 6,y = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 4,y = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 4,y = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9]),x = 4,y = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9]),x = 4,y = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5]),x = 5,y = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5]),x = 5,y = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 4,y = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 4,y = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, None, None, 7]),x = 6,y = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, None, None, 7]),x = 6,y = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9]),x = 8,y = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9]),x = 8,y = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 4,y = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 4,y = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, None, None, 5]),x = 4,y = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, None, None, 5]),x = 4,y = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 5,y = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 5,y = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, None, 7, 8]),x = 7,y = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, None, 7, 8]),x = 7,y = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7]),x = 6,y = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7]),x = 6,y = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 6,y = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 6,y = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),x = 8,y = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),x = 8,y = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12]),x = 12,y = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12]),x = 12,y = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, None, None, 5]),x = 2,y = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, None, None, 5]),x = 2,y = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, None, None, 7]),x = 6,y = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, None, None, 7]),x = 6,y = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None, 10]),x = 8,y = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None, 10]),x = 8,y = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5]),x = 4,y = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5]),x = 4,y = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7]),x = 6,y = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7]),x = 6,y = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6]),x = 5,y = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6]),x = 5,y = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 10,y = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 10,y = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 4,y = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 4,y = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9]),x = 8,y = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9]),x = 8,y = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, None]),x = 4,y = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, None]),x = 4,y = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7]),x = 4,y = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7]),x = 4,y = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 8,y = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 8,y = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9]),x = 8,y = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9]),x = 8,y = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),x = 10,y = 14) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),x = 10,y = 14) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, 9, 10, 11]),x = 10,y = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, 9, 10, 11]),x = 10,y = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7]),x = 6,y = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7]),x = 6,y = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9]),x = 8,y = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9]),x = 8,y = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, 9]),x = 8,y = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, 9]),x = 8,y = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),x = 3,y = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),x = 3,y = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, 6]),x = 5,y = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, 6]),x = 5,y = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13]),x = 12,y = 13) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13]),x = 12,y = 13) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6]),x = 6,y = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6]),x = 6,y = 5) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, None, 6]),x = 5,y = 6) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5]),x = 5,y = 4) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 9,y = 11) == True
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, 6]),x = 5,y = 6) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 2,y = 3) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, None, 9]),x = 6,y = 8) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, 12, 13]),x = 10,y = 11) == False
    assert candidate(root = tree_node([1, 2, 3, 4]),x = 4,y = 3) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7]),x = 6,y = 7) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4]),x = 2,y = 3) == False
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5]),x = 4,y = 5) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 3,y = 7) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 4,y = 7) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 2,y = 3) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7]),x = 6,y = 7) == False
    assert candidate(root = tree_node([1, 2, 3, None, None, 6, 7, 8, 9]),x = 8,y = 9) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, 7, 8]),x = 7,y = 8) == False
    assert candidate(root = tree_node([1, 2, 3, None, None, 6, 7]),x = 6,y = 7) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 4,y = 9) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9]),x = 4,y = 9) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5]),x = 5,y = 4) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 4,y = 6) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, None, None, 7]),x = 6,y = 7) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9]),x = 8,y = 5) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 4,y = 6) == True
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, None, None, 5]),x = 4,y = 5) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 5,y = 7) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, None, 7, 8]),x = 7,y = 8) == False
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7]),x = 6,y = 7) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 6,y = 5) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),x = 8,y = 11) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12]),x = 12,y = 11) == False
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, None, None, 5]),x = 2,y = 3) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, None, None, 7]),x = 6,y = 7) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None, 10]),x = 8,y = 10) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5]),x = 4,y = 5) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7]),x = 6,y = 7) == False
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6]),x = 5,y = 6) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 10,y = 11) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),x = 4,y = 5) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9]),x = 8,y = 9) == False
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, None]),x = 4,y = 3) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7]),x = 4,y = 7) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11]),x = 8,y = 9) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9]),x = 8,y = 9) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),x = 10,y = 14) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, 9, 10, 11]),x = 10,y = 11) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, None, None, 6, 7]),x = 6,y = 5) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9]),x = 8,y = 9) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, 8, 9]),x = 8,y = 9) == True
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),x = 3,y = 15) == False
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, None, 5, 6]),x = 5,y = 6) == False
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11, None, None, 12, 13]),x = 12,y = 13) == False
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6]),x = 6,y = 5) == False


