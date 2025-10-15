def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(piles = [5, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 7, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 7, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 7, 7, 7, 7, 7, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 7, 7, 7, 7, 7, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 4, 4, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 4, 4, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 2, 2, 2, 2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 2, 2, 2, 2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 1, 3, 5, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 1, 3, 5, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 2, 1, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 2, 1, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 4, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 4, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 2, 3, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 2, 3, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 2, 2, 3, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 2, 2, 3, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 4, 4, 4, 4, 4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 4, 4, 4, 4, 4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 3, 5, 7, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 3, 5, 7, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 2, 2, 2, 2, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 2, 2, 2, 2, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 7, 7, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 7, 7, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 5, 6, 7, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 5, 6, 7, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 4, 3, 2, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 4, 3, 2, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 2, 3, 4, 4, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 2, 3, 4, 4, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 4, 4, 3, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 4, 4, 3, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 3, 3, 2, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 3, 3, 2, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 5, 5, 5, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 5, 5, 5, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 7, 5, 5, 3, 3, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 7, 5, 5, 3, 3, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 5, 5, 4, 4, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 5, 5, 4, 4, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 2, 2, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 2, 2, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 3, 3, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 3, 3, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [6, 5, 4, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [6, 5, 4, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 4, 3, 3, 2, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 4, 3, 3, 2, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 3, 2, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 3, 2, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [6, 6, 6, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [6, 6, 6, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [6, 3, 5, 2, 4, 1, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [6, 3, 5, 2, 4, 1, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [6, 5, 4, 3, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [6, 5, 4, 3, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 1, 2, 3, 4, 5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 1, 2, 3, 4, 5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 5, 5, 5, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 5, 5, 5, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 4, 4, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 4, 4, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 1, 2, 3, 4, 5, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 1, 2, 3, 4, 5, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [6, 3, 3, 2, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [6, 3, 3, 2, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 2, 2, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 2, 2, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [6, 3, 1, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [6, 3, 1, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 2, 3, 4, 5, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 2, 3, 4, 5, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 2, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 2, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 4, 4, 4, 4, 4, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 4, 4, 4, 4, 4, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 2, 3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 2, 3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 3, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 3, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 4, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 4, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(piles = [6, 3, 4, 2, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [6, 3, 4, 2, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [7, 7, 7, 7, 7, 7, 7]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [7, 7, 7, 7, 7, 7, 7]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [6, 3, 1, 2, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [6, 3, 1, 2, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [4, 3, 2, 2, 2, 2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [4, 3, 2, 2, 2, 2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 3, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 3, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(piles = [6, 6, 6, 6, 6, 6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [6, 6, 6, 6, 6, 6, 6]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(piles = [5, 3, 1]) == True
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7]) == False
    assert candidate(piles = [7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(piles = [1, 2, 3]) == False
    assert candidate(piles = [1]) == True
    assert candidate(piles = [1, 3, 5, 7]) == False
    assert candidate(piles = [3, 3, 3, 3]) == False
    assert candidate(piles = [2, 2, 2]) == True
    assert candidate(piles = [1, 2, 3, 4]) == True
    assert candidate(piles = [7, 7, 7]) == True
    assert candidate(piles = [2, 2, 2, 2]) == False
    assert candidate(piles = [7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(piles = [4, 1, 2]) == True
    assert candidate(piles = [4, 4, 4, 4]) == False
    assert candidate(piles = [1, 1]) == False
    assert candidate(piles = [2, 2, 2, 2, 2, 2, 2]) == True
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 7]) == True
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 2]) == True
    assert candidate(piles = [7, 1, 3, 5, 2]) == True
    assert candidate(piles = [2, 2, 2, 2, 2, 2]) == False
    assert candidate(piles = [4, 2, 1, 3]) == True
    assert candidate(piles = [2, 4, 6]) == False
    assert candidate(piles = [1, 2, 2, 3, 3, 4]) == True
    assert candidate(piles = [1, 2, 2, 3, 4, 5, 6]) == True
    assert candidate(piles = [1, 1, 2, 2, 3, 3, 4]) == True
    assert candidate(piles = [1, 3, 3]) == True
    assert candidate(piles = [1, 2, 3, 4, 3, 2, 1]) == True
    assert candidate(piles = [1, 1, 1, 1, 1, 1]) == False
    assert candidate(piles = [4, 4, 4, 4, 4, 4, 4]) == True
    assert candidate(piles = [2, 3, 5, 7, 11]) == True
    assert candidate(piles = [2, 3, 4, 5, 6]) == True
    assert candidate(piles = [2, 2, 2, 2, 2, 2, 1]) == True
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13]) == True
    assert candidate(piles = [7, 7, 7, 7]) == False
    assert candidate(piles = [4, 5, 6, 7, 1]) == True
    assert candidate(piles = [5, 4, 3, 2, 1, 1, 1]) == True
    assert candidate(piles = [1, 2, 2, 3, 4, 4, 5]) == True
    assert candidate(piles = [1, 3, 5]) == True
    assert candidate(piles = [4, 4, 4, 3, 3, 2, 1]) == True
    assert candidate(piles = [7, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(piles = [5, 5, 5, 5, 1]) == True
    assert candidate(piles = [7, 7, 5, 5, 3, 3, 1]) == True
    assert candidate(piles = [5, 5, 5, 4, 4, 3]) == True
    assert candidate(piles = [3, 3, 2, 2, 1, 1]) == False
    assert candidate(piles = [2, 3, 3, 2]) == False
    assert candidate(piles = [6, 5, 4, 3, 2, 1]) == True
    assert candidate(piles = [1, 1, 1, 1, 2, 2, 2]) == True
    assert candidate(piles = [4, 4, 3, 3, 2, 2, 1]) == True
    assert candidate(piles = [3, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(piles = [6, 6, 6, 1, 1]) == True
    assert candidate(piles = [6, 3, 5, 2, 4, 1, 7]) == False
    assert candidate(piles = [6, 5, 4, 3, 2, 1, 1]) == True
    assert candidate(piles = [7, 1, 2, 3, 4, 5, 6]) == False
    assert candidate(piles = [5, 5, 5, 5, 1]) == True
    assert candidate(piles = [4, 4, 4, 1]) == True
    assert candidate(piles = [7, 1, 2, 3, 4, 5, 6]) == False
    assert candidate(piles = [3, 3, 2, 1]) == True
    assert candidate(piles = [6, 3, 3, 2, 2, 1, 1]) == True
    assert candidate(piles = [5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(piles = [2, 2, 2, 2, 1]) == True
    assert candidate(piles = [1, 3, 5, 7]) == False
    assert candidate(piles = [6, 3, 1, 4]) == False
    assert candidate(piles = [1, 2, 2, 3, 4, 5, 6]) == True
    assert candidate(piles = [3, 5, 5, 5]) == True
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(piles = [1, 2, 2, 1, 1]) == True
    assert candidate(piles = [4, 4, 4, 4, 4, 4, 3]) == True
    assert candidate(piles = [1, 1, 2, 3, 4]) == True
    assert candidate(piles = [7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(piles = [3, 3, 3, 3, 3, 3, 3]) == True
    assert candidate(piles = [2, 4, 6]) == False
    assert candidate(piles = [6, 3, 4, 2, 1]) == True
    assert candidate(piles = [3, 3, 3, 3, 3]) == True
    assert candidate(piles = [7, 7, 7, 7, 7, 7, 7]) == True
    assert candidate(piles = [6, 3, 1, 2, 5]) == True
    assert candidate(piles = [4, 3, 2, 2, 2, 2, 2]) == True
    assert candidate(piles = [1, 3, 3, 3]) == True
    assert candidate(piles = [3, 3, 3, 1, 1]) == True
    assert candidate(piles = [6, 6, 6, 6, 6, 6, 6]) == True


