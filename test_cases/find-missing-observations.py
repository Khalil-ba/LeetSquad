def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(rolls = [1, 2],mean = 3,n = 2) == [5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2],mean = 3,n = 2) == [5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 3, 5],mean = 2,n = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 3, 5],mean = 2,n = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 5, 5, 5],mean = 5,n = 4) == [5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 5, 5, 5],mean = 5,n = 4) == [5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 6, 6, 6],mean = 5,n = 3) == [4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 6, 6, 6],mean = 5,n = 3) == [4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6],mean = 6,n = 3) == [6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6],mean = 6,n = 3) == [6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 3,n = 6) == [3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 3,n = 6) == [3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4],mean = 6,n = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4],mean = 6,n = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 5, 6],mean = 3,n = 4) == [3, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 5, 6],mean = 3,n = 4) == [3, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 5, 5, 5],mean = 5,n = 5) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 5, 5, 5],mean = 5,n = 5) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1],mean = 2,n = 6) == [3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1],mean = 2,n = 6) == [3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 2, 4, 3],mean = 4,n = 2) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 2, 4, 3],mean = 4,n = 2) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 5,n = 6) == [4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 5,n = 6) == [4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1],mean = 2,n = 4) == [3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1],mean = 2,n = 4) == [3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3],mean = 4,n = 1) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3],mean = 4,n = 1) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6],mean = 6,n = 1) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6],mean = 6,n = 1) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1],mean = 2,n = 3) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1],mean = 2,n = 3) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6],mean = 5,n = 3) == [4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6],mean = 5,n = 3) == [4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 3,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 3,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6],mean = 3,n = 6) == [3, 3, 3, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6],mean = 3,n = 6) == [3, 3, 3, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1],mean = 6,n = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1],mean = 6,n = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 15) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 15) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 3) == [6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 3) == [6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1],mean = 2,n = 10) == [3, 3, 3, 3, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1],mean = 2,n = 10) == [3, 3, 3, 3, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1],mean = 5,n = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1],mean = 5,n = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 5) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 5) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 4,n = 20) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 4,n = 20) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 3,n = 3) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 3,n = 3) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 12) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 12) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 6, 3, 4, 2, 5],mean = 3,n = 5) == [3, 3, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 6, 3, 4, 2, 5],mean = 3,n = 5) == [3, 3, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 4, 6, 1, 3, 5],mean = 4,n = 3) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 4, 6, 1, 3, 5],mean = 4,n = 3) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1],mean = 4,n = 12) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1],mean = 4,n = 12) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 6, 1, 6, 1, 6],mean = 4,n = 3) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 6, 1, 6, 1, 6],mean = 4,n = 3) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 6,n = 10) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 6,n = 10) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5],mean = 4,n = 5) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5],mean = 4,n = 5) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],mean = 4,n = 20) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],mean = 4,n = 20) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3],mean = 5,n = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3],mean = 5,n = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 1, 5, 1, 5, 1],mean = 4,n = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 1, 5, 1, 5, 1],mean = 4,n = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1],mean = 4,n = 18) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1],mean = 4,n = 18) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 3,n = 15) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 3,n = 15) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 15) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 15) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1],mean = 2,n = 10) == [3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1],mean = 2,n = 10) == [3, 3, 3, 3, 3, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 3,n = 7) == [3, 3, 3, 3, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 3,n = 7) == [3, 3, 3, 3, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3],mean = 2,n = 9) == [2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3],mean = 2,n = 9) == [2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [4, 4, 4, 4, 4, 4, 4, 4],mean = 4,n = 1) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [4, 4, 4, 4, 4, 4, 4, 4],mean = 4,n = 1) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 2, 2, 2, 2, 2],mean = 2,n = 12) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 2, 2, 2, 2, 2],mean = 2,n = 12) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 20) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 20) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 3, 4, 5, 6],mean = 4,n = 6) == [4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 3, 4, 5, 6],mean = 4,n = 6) == [4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6],mean = 4,n = 3) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6],mean = 4,n = 3) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 12) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 12) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 4, 6, 4, 6, 4],mean = 5,n = 5) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 4, 6, 4, 6, 4],mean = 5,n = 5) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 3,n = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 3,n = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 5,n = 12) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 5,n = 12) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 4,n = 10) == [5, 5, 5, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 4,n = 10) == [5, 5, 5, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 1, 5, 1, 5, 1],mean = 3,n = 6) == [3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 1, 5, 1, 5, 1],mean = 3,n = 6) == [3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [4, 4, 4, 4, 4, 4],mean = 5,n = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [4, 4, 4, 4, 4, 4],mean = 5,n = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 5,n = 10) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 5,n = 10) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 6,n = 6) == [6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 6,n = 6) == [6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 20) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 20) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 1,n = 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 1,n = 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 6,n = 6) == [6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 6,n = 6) == [6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 2, 2, 3, 3],mean = 3,n = 3) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 2, 2, 3, 3],mean = 3,n = 3) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 6) == [5, 5, 5, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 6) == [5, 5, 5, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 18) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 18) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 6, 1, 6, 1, 6],mean = 4,n = 6) == [5, 5, 5, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 6, 1, 6, 1, 6],mean = 4,n = 6) == [5, 5, 5, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 6, 1, 6, 1, 6],mean = 4,n = 3) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 6, 1, 6, 1, 6],mean = 4,n = 3) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 2, 2, 2, 2, 2, 2],mean = 3,n = 4) == [5, 5, 5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 2, 2, 2, 2, 2, 2],mean = 3,n = 4) == [5, 5, 5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5],mean = 2,n = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5],mean = 2,n = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 4, 6, 5, 4, 3, 2],mean = 4,n = 5) == [5, 5, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 4, 6, 5, 4, 3, 2],mean = 4,n = 5) == [5, 5, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 5,n = 5) == [4, 4, 4, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 5,n = 5) == [4, 4, 4, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6],mean = 4,n = 8) == [3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6],mean = 4,n = 8) == [3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 5,n = 20) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 5,n = 20) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 10) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 10) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 4,n = 5) == [5, 5, 5, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 4,n = 5) == [5, 5, 5, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5],mean = 3,n = 5) == [3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5],mean = 3,n = 5) == [3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],mean = 4,n = 5) == [6, 6, 6, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],mean = 4,n = 5) == [6, 6, 6, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],mean = 4,n = 12) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],mean = 4,n = 12) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 4,n = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 4,n = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 4,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 4,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 3,n = 10) == [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 3,n = 10) == [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [4, 5, 6, 1, 2, 3],mean = 4,n = 6) == [5, 5, 5, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [4, 5, 6, 1, 2, 3],mean = 4,n = 6) == [5, 5, 5, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 2, 3, 3, 4, 5, 6],mean = 3,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 2, 3, 3, 4, 5, 6],mean = 3,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 5) == [4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 5) == [4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],mean = 4,n = 5) == [5, 5, 5, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],mean = 4,n = 5) == [5, 5, 5, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 5, 5, 5, 5],mean = 5,n = 5) == [5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 5, 5, 5, 5],mean = 5,n = 5) == [5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 18) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 18) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 5, 5, 5, 5, 5],mean = 4,n = 6) == [3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 5, 5, 5, 5, 5],mean = 4,n = 6) == [3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 5,n = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 5,n = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 4,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 4,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1],mean = 2,n = 9) == [3, 3, 3, 3, 3, 3, 3, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1],mean = 2,n = 9) == [3, 3, 3, 3, 3, 3, 3, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [4, 4, 4, 4, 4, 4],mean = 4,n = 3) == [4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [4, 4, 4, 4, 4, 4],mean = 4,n = 3) == [4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 4,n = 5) == [6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 4,n = 5) == [6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 3,n = 20) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 3,n = 20) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6],mean = 1,n = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6],mean = 1,n = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 3) == [6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 3) == [6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 4, 6, 8, 10],mean = 4,n = 5) == [2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 4, 6, 8, 10],mean = 4,n = 5) == [2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6],mean = 6,n = 1) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6],mean = 6,n = 1) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],mean = 4,n = 12) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],mean = 4,n = 12) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 10) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 10) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6],mean = 5,n = 2) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6],mean = 5,n = 2) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 5,n = 3) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 5,n = 3) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 5,n = 20) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 5,n = 20) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3],mean = 5,n = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3],mean = 5,n = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 4,n = 6) == [5, 5, 5, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 4,n = 6) == [5, 5, 5, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 10) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 10) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6],mean = 4,n = 5) == [5, 5, 5, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6],mean = 4,n = 5) == [5, 5, 5, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 5) == [6, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 5) == [6, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 20) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 20) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 5,n = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 5,n = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5],mean = 3,n = 7) == [3, 3, 3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5],mean = 3,n = 7) == [3, 3, 3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],mean = 5,n = 5) == [4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],mean = 5,n = 5) == [4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],mean = 5,n = 15) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],mean = 5,n = 15) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 2, 2, 3, 3],mean = 3,n = 6) == [4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 2, 2, 3, 3],mean = 3,n = 6) == [4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 10) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 10) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],mean = 3,n = 5) == [3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],mean = 3,n = 5) == [3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(rolls = [1, 2, 3],mean = 4,n = 3) == [6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rolls = [1, 2, 3],mean = 4,n = 3) == [6, 6, 6]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(rolls = [1, 2],mean = 3,n = 2) == [5, 4]
    assert candidate(rolls = [1, 3, 5],mean = 2,n = 2) == []
    assert candidate(rolls = [5, 5, 5, 5],mean = 5,n = 4) == [5, 5, 5, 5]
    assert candidate(rolls = [5, 6, 6, 6],mean = 5,n = 3) == [4, 4, 4]
    assert candidate(rolls = [6, 6, 6, 6],mean = 6,n = 3) == [6, 6, 6]
    assert candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 3,n = 6) == [3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [1, 2, 3, 4],mean = 6,n = 4) == []
    assert candidate(rolls = [1, 5, 6],mean = 3,n = 4) == [3, 2, 2, 2]
    assert candidate(rolls = [5, 5, 5, 5],mean = 5,n = 5) == [5, 5, 5, 5, 5]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1],mean = 2,n = 6) == [3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [3, 2, 4, 3],mean = 4,n = 2) == [6, 6]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 5,n = 6) == [4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [1, 1, 1, 1],mean = 2,n = 4) == [3, 3, 3, 3]
    assert candidate(rolls = [3],mean = 4,n = 1) == [5]
    assert candidate(rolls = [6],mean = 6,n = 1) == [6]
    assert candidate(rolls = [1, 1, 1],mean = 2,n = 3) == [3, 3, 3]
    assert candidate(rolls = [6, 6, 6],mean = 5,n = 3) == [4, 4, 4]
    assert candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 3,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [1, 2, 3, 4, 5, 6],mean = 3,n = 6) == [3, 3, 3, 2, 2, 2]
    assert candidate(rolls = [1],mean = 6,n = 5) == []
    assert candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 15) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 3) == [6, 6, 6]
    assert candidate(rolls = [1, 1, 1, 1],mean = 2,n = 10) == [3, 3, 3, 3, 2, 2, 2, 2, 2, 2]
    assert candidate(rolls = [1, 1, 1, 1, 1],mean = 5,n = 5) == []
    assert candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 5) == [5, 5, 5, 5, 5]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 4,n = 20) == []
    assert candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 3,n = 3) == [3, 3, 3]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 12) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [1, 6, 3, 4, 2, 5],mean = 3,n = 5) == [3, 3, 2, 2, 2]
    assert candidate(rolls = [2, 4, 6, 1, 3, 5],mean = 4,n = 3) == [5, 5, 5]
    assert candidate(rolls = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1],mean = 4,n = 12) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [1, 6, 1, 6, 1, 6],mean = 4,n = 3) == [5, 5, 5]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 6,n = 10) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert candidate(rolls = [1, 2, 3, 4, 5],mean = 4,n = 5) == [5, 5, 5, 5, 5]
    assert candidate(rolls = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],mean = 4,n = 20) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [3, 3, 3, 3],mean = 5,n = 5) == []
    assert candidate(rolls = [5, 1, 5, 1, 5, 1],mean = 4,n = 2) == []
    assert candidate(rolls = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1],mean = 4,n = 18) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 3,n = 15) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 15) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [1, 1, 1, 1, 1],mean = 2,n = 10) == [3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
    assert candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 3,n = 7) == [3, 3, 3, 3, 2, 2, 2]
    assert candidate(rolls = [1, 2, 3],mean = 2,n = 9) == [2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(rolls = [4, 4, 4, 4, 4, 4, 4, 4],mean = 4,n = 1) == [4]
    assert candidate(rolls = [2, 2, 2, 2, 2, 2],mean = 2,n = 12) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 20) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [2, 3, 4, 5, 6],mean = 4,n = 6) == [4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [1, 2, 3, 4, 5, 6],mean = 4,n = 3) == [5, 5, 5]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 12) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert candidate(rolls = [6, 4, 6, 4, 6, 4],mean = 5,n = 5) == [5, 5, 5, 5, 5]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 3,n = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 5,n = 12) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 4,n = 10) == [5, 5, 5, 4, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [5, 1, 5, 1, 5, 1],mean = 3,n = 6) == [3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [4, 4, 4, 4, 4, 4],mean = 5,n = 1) == []
    assert candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 5,n = 10) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 6,n = 6) == [6, 6, 6, 6, 6, 6]
    assert candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 20) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 1,n = 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 6,n = 6) == [6, 6, 6, 6, 6, 6]
    assert candidate(rolls = [1, 1, 2, 2, 3, 3],mean = 3,n = 3) == [5, 5, 5]
    assert candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 6) == [5, 5, 5, 4, 4, 4]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 18) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert candidate(rolls = [1, 6, 1, 6, 1, 6],mean = 4,n = 6) == [5, 5, 5, 4, 4, 4]
    assert candidate(rolls = [1, 6, 1, 6, 1, 6],mean = 4,n = 3) == [5, 5, 5]
    assert candidate(rolls = [2, 2, 2, 2, 2, 2, 2],mean = 3,n = 4) == [5, 5, 5, 4]
    assert candidate(rolls = [1, 2, 3, 4, 5],mean = 2,n = 1) == []
    assert candidate(rolls = [2, 4, 6, 5, 4, 3, 2],mean = 4,n = 5) == [5, 5, 4, 4, 4]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 5,n = 5) == [4, 4, 4, 4, 3]
    assert candidate(rolls = [6, 6, 6, 6],mean = 4,n = 8) == [3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 5,n = 20) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 10) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 4,n = 5) == [5, 5, 5, 4, 4]
    assert candidate(rolls = [1, 2, 3, 4, 5],mean = 3,n = 5) == [3, 3, 3, 3, 3]
    assert candidate(rolls = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],mean = 4,n = 5) == [6, 6, 6, 5, 5]
    assert candidate(rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],mean = 4,n = 12) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 4,n = 5) == []
    assert candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 4,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 3,n = 10) == [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(rolls = [4, 5, 6, 1, 2, 3],mean = 4,n = 6) == [5, 5, 5, 4, 4, 4]
    assert candidate(rolls = [1, 2, 2, 3, 3, 4, 5, 6],mean = 3,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 2, 2]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 5) == [4, 4, 4, 4, 4]
    assert candidate(rolls = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],mean = 4,n = 5) == [5, 5, 5, 4, 4]
    assert candidate(rolls = [5, 5, 5, 5, 5],mean = 5,n = 5) == [5, 5, 5, 5, 5]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 18) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [5, 5, 5, 5, 5, 5],mean = 4,n = 6) == [3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 5,n = 10) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 4,n = 10) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1],mean = 2,n = 9) == [3, 3, 3, 3, 3, 3, 3, 2, 2]
    assert candidate(rolls = [4, 4, 4, 4, 4, 4],mean = 4,n = 3) == [4, 4, 4]
    assert candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 4,n = 5) == [6, 6, 6, 6, 6]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 3,n = 20) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(rolls = [6],mean = 1,n = 5) == []
    assert candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 3) == [6, 6, 6]
    assert candidate(rolls = [2, 4, 6, 8, 10],mean = 4,n = 5) == [2, 2, 2, 2, 2]
    assert candidate(rolls = [6, 6, 6, 6, 6],mean = 6,n = 1) == [6]
    assert candidate(rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],mean = 4,n = 12) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 10) == [5, 5, 5, 5, 5, 5, 4, 4, 4, 4]
    assert candidate(rolls = [6, 6, 6, 6],mean = 5,n = 2) == [3, 3]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6],mean = 5,n = 3) == [3, 3, 3]
    assert candidate(rolls = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],mean = 5,n = 20) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(rolls = [3, 3, 3, 3, 3],mean = 5,n = 5) == []
    assert candidate(rolls = [6, 5, 4, 3, 2, 1],mean = 4,n = 6) == [5, 5, 5, 4, 4, 4]
    assert candidate(rolls = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],mean = 6,n = 10) == [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    assert candidate(rolls = [1, 2, 3, 4, 5, 6],mean = 4,n = 5) == [5, 5, 5, 4, 4]
    assert candidate(rolls = [3, 3, 3, 3, 3, 3],mean = 4,n = 5) == [6, 5, 5, 5, 5]
    assert candidate(rolls = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],mean = 2,n = 20) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],mean = 5,n = 10) == []
    assert candidate(rolls = [1, 2, 3, 4, 5],mean = 3,n = 7) == [3, 3, 3, 3, 3, 3, 3]
    assert candidate(rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],mean = 5,n = 5) == [4, 4, 4, 4, 4]
    assert candidate(rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],mean = 5,n = 15) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(rolls = [1, 1, 2, 2, 3, 3],mean = 3,n = 6) == [4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],mean = 3,n = 10) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    assert candidate(rolls = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],mean = 3,n = 5) == [3, 3, 3, 3, 3]
    assert candidate(rolls = [1, 2, 3],mean = 4,n = 3) == [6, 6, 6]


