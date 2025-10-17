def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, 2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, 2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-5, -3, -2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-5, -3, -2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([99, 50, 49])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([99, 50, 49])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, 50, 50])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, 50, 50])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -50, 150])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -50, 150])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 4, 6])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 4, 6])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 0, 100])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 0, 100])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, -25, 75])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, -25, 75])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([99, -50, 149])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([99, -50, 149])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, 0, -100])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, 0, -100])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 100, -100])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 100, -100])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -1, 101])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -1, 101])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, -99, -1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, -99, -1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, 100, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, 100, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([99, -1, -98])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([99, -1, -98])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, 33, -67])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, 33, -67])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 25])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 25])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 100, -99])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 100, -99])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-75, -25, -50])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-75, -25, -50])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -1, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -1, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 1, 99])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 1, 99])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, -50, -50])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, -50, -50])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([99, 49, 50])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([99, 49, 50])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-60, -40, -20])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-60, -40, -20])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-50, -25, -25])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-50, -25, -25])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-2, -1, -1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-2, -1, -1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-99, 99, -198])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-99, 99, -198])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([99, 49, 50])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([99, 49, 50])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([33, 16, 17])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([33, 16, 17])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-99, 50, -51])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-99, 50, -51])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 24, 26])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 24, 26])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -100, 200])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -100, 200])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-25, -25, 50])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-25, -25, 50])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, 2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, 2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 99, -98])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 99, -98])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -50, 50])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -50, 50])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, 99, -98])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, 99, -98])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, -25])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, -25])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 99, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 99, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([99, -99, 198])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([99, -99, 198])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 3, 7])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 3, 7])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, 0, 100])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, 0, 100])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 25])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 25])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-99, -49, -50])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-99, -49, -50])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, -1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, -1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -5, -5])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -5, -5])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -100, 200])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -100, 200])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -50, 49])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -50, 49])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-7, -3, -4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-7, -3, -4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, 50, -50])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, 50, -50])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -10, 20])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -10, 20])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, -100, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, -100, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, -25, -25])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, -25, -25])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -50, 51])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -50, 51])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-50, 25, 25])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-50, 25, 25])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([33, 32, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([33, 32, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-100, -50, -50])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-100, -50, -50])) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, -1, 2])) == True
    assert candidate(root = tree_node([-5, -3, -2])) == True
    assert candidate(root = tree_node([5, 3, 1])) == False
    assert candidate(root = tree_node([99, 50, 49])) == True
    assert candidate(root = tree_node([-100, 50, 50])) == False
    assert candidate(root = tree_node([100, -50, 150])) == True
    assert candidate(root = tree_node([1, 0, 1])) == True
    assert candidate(root = tree_node([2, 1, 1])) == True
    assert candidate(root = tree_node([0, 0, 0])) == True
    assert candidate(root = tree_node([10, 4, 6])) == True
    assert candidate(root = tree_node([-1, 1, 0])) == False
    assert candidate(root = tree_node([100, 0, 100])) == True
    assert candidate(root = tree_node([50, -25, 75])) == True
    assert candidate(root = tree_node([99, -50, 149])) == True
    assert candidate(root = tree_node([-100, 0, -100])) == True
    assert candidate(root = tree_node([0, 100, -100])) == True
    assert candidate(root = tree_node([100, -1, 101])) == True
    assert candidate(root = tree_node([2, 1, 1])) == True
    assert candidate(root = tree_node([-100, -99, -1])) == True
    assert candidate(root = tree_node([-100, 100, 0])) == False
    assert candidate(root = tree_node([99, -1, -98])) == False
    assert candidate(root = tree_node([-100, 33, -67])) == False
    assert candidate(root = tree_node([0, -1, 1])) == True
    assert candidate(root = tree_node([-100, 0, 0])) == False
    assert candidate(root = tree_node([0, -1, 1])) == True
    assert candidate(root = tree_node([50, 25, 25])) == True
    assert candidate(root = tree_node([1, 100, -99])) == True
    assert candidate(root = tree_node([-75, -25, -50])) == True
    assert candidate(root = tree_node([-1, -1, 0])) == True
    assert candidate(root = tree_node([5, 5, 0])) == True
    assert candidate(root = tree_node([100, 1, 99])) == True
    assert candidate(root = tree_node([-100, -50, -50])) == True
    assert candidate(root = tree_node([99, 49, 50])) == True
    assert candidate(root = tree_node([-60, -40, -20])) == True
    assert candidate(root = tree_node([100, 50, 50])) == True
    assert candidate(root = tree_node([1, 0, 1])) == True
    assert candidate(root = tree_node([-50, -25, -25])) == True
    assert candidate(root = tree_node([-2, -1, -1])) == True
    assert candidate(root = tree_node([-99, 99, -198])) == True
    assert candidate(root = tree_node([99, 49, 50])) == True
    assert candidate(root = tree_node([33, 16, 17])) == True
    assert candidate(root = tree_node([-99, 50, -51])) == False
    assert candidate(root = tree_node([50, 24, 26])) == True
    assert candidate(root = tree_node([100, -100, 200])) == True
    assert candidate(root = tree_node([-25, -25, 50])) == False
    assert candidate(root = tree_node([1, -1, 2])) == True
    assert candidate(root = tree_node([1, 99, -98])) == True
    assert candidate(root = tree_node([100, 50, 50])) == True
    assert candidate(root = tree_node([100, -50, 50])) == False
    assert candidate(root = tree_node([-1, 99, -98])) == False
    assert candidate(root = tree_node([50, 25, -25])) == False
    assert candidate(root = tree_node([100, 99, 1])) == True
    assert candidate(root = tree_node([99, -99, 198])) == True
    assert candidate(root = tree_node([10, 3, 7])) == True
    assert candidate(root = tree_node([-100, 0, 100])) == False
    assert candidate(root = tree_node([50, 25, 25])) == True
    assert candidate(root = tree_node([1, 1, 0])) == True
    assert candidate(root = tree_node([-99, -49, -50])) == True
    assert candidate(root = tree_node([1, 2, -1])) == True
    assert candidate(root = tree_node([-10, -5, -5])) == True
    assert candidate(root = tree_node([100, -100, 200])) == True
    assert candidate(root = tree_node([-1, -50, 49])) == True
    assert candidate(root = tree_node([-7, -3, -4])) == True
    assert candidate(root = tree_node([-100, 50, -50])) == False
    assert candidate(root = tree_node([10, -10, 20])) == True
    assert candidate(root = tree_node([-100, -100, 0])) == True
    assert candidate(root = tree_node([50, -25, -25])) == False
    assert candidate(root = tree_node([1, -50, 51])) == True
    assert candidate(root = tree_node([7, 3, 4])) == True
    assert candidate(root = tree_node([-50, 25, 25])) == False
    assert candidate(root = tree_node([33, 32, 1])) == True
    assert candidate(root = tree_node([-100, -50, -50])) == True


