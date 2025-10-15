def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 5) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 5) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 2) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 2) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 15) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 15) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 1) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 1) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 0, 1, 1, 1, 0],n = 2) == [0, 1, 0, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 0, 1, 1, 1, 0],n = 2) == [0, 1, 0, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 15) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 15) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 1, 0, 0, 1, 1],n = 15) == [0, 0, 1, 1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 1, 0, 0, 1, 1],n = 15) == [0, 0, 1, 1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 1, 0, 0, 1, 0],n = 1000000000) == [0, 0, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 1, 0, 0, 1, 0],n = 1000000000) == [0, 0, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 2) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 2) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 0, 1, 1, 0, 0],n = 15) == [0, 0, 0, 1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 0, 1, 1, 0, 0],n = 15) == [0, 0, 0, 1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 3) == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 3) == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 0, 0, 1, 0, 0],n = 5) == [0, 1, 1, 1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 0, 0, 1, 0, 0],n = 5) == [0, 1, 1, 1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 1) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 1) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 1, 1, 1, 1, 0],n = 14) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 1, 1, 1, 1, 0],n = 14) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 1, 1, 0, 0, 1],n = 7) == [0, 0, 1, 1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 1, 1, 0, 0, 1],n = 7) == [0, 0, 1, 1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 30) == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 30) == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 0, 0, 1, 1, 0],n = 20) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 0, 0, 1, 1, 0],n = 20) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 1, 0, 0, 1, 0],n = 28) == [0, 0, 1, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 1, 0, 0, 1, 0],n = 28) == [0, 0, 1, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 15) == [0, 0, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 15) == [0, 0, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 1, 1, 0, 1, 1],n = 7) == [0, 0, 1, 0, 0, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 1, 1, 0, 1, 1],n = 7) == [0, 0, 1, 0, 0, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 1, 1, 1, 1, 0],n = 1000) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 1, 1, 1, 1, 0],n = 1000) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 0, 0, 1, 1],n = 10) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 0, 0, 1, 1],n = 10) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 0, 0, 0, 1, 1],n = 100) == [0, 0, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 0, 0, 0, 1, 1],n = 100) == [0, 0, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 20) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 20) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 0, 1, 0, 0, 1],n = 1000) == [0, 1, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 0, 1, 0, 0, 1],n = 1000) == [0, 1, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 1, 0, 1, 1, 0],n = 500) == [0, 1, 1, 0, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 1, 0, 1, 1, 0],n = 500) == [0, 1, 1, 0, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 0, 0, 1, 0, 0],n = 1000000000) == [0, 0, 1, 0, 0, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 0, 0, 1, 0, 0],n = 1000000000) == [0, 0, 1, 0, 0, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 50) == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 50) == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 1, 1, 1, 1, 0],n = 10) == [0, 1, 1, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 1, 1, 1, 1, 0],n = 10) == [0, 1, 1, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 0, 0, 1, 0, 1],n = 300) == [0, 0, 1, 1, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 0, 0, 1, 0, 1],n = 300) == [0, 0, 1, 1, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 1, 0, 0, 1, 0],n = 10) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 1, 0, 0, 1, 0],n = 10) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 1, 0, 1, 1, 0],n = 2000000000) == [0, 1, 0, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 1, 0, 1, 1, 0],n = 2000000000) == [0, 1, 0, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 1, 1, 1, 0, 0],n = 999999999) == [0, 1, 0, 1, 0, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 1, 1, 1, 0, 0],n = 999999999) == [0, 1, 0, 1, 0, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 1, 1, 0, 0, 1],n = 1250) == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 1, 1, 0, 0, 1],n = 1250) == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 0, 0, 1, 1, 1],n = 25) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 0, 0, 1, 1, 1],n = 25) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 1, 0, 1, 1, 0],n = 20) == [0, 0, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 1, 0, 1, 1, 0],n = 20) == [0, 0, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 0, 0, 1, 0, 0],n = 1000) == [0, 0, 0, 0, 0, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 0, 0, 1, 0, 0],n = 1000) == [0, 0, 0, 0, 0, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 1000000000) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 1000000000) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 1, 0, 0, 1],n = 1000) == [0, 1, 0, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 1, 0, 0, 1],n = 1000) == [0, 1, 0, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 1000000) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 1000000) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 0, 1, 0, 1, 1],n = 1000000000) == [0, 1, 1, 1, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 0, 1, 0, 1, 1],n = 1000000000) == [0, 1, 1, 1, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 5) == [0, 1, 0, 0, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 5) == [0, 1, 0, 0, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 1, 1, 0, 0],n = 500000000) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 1, 1, 0, 0],n = 500000000) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 30) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 30) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 1, 1, 0, 0],n = 67890) == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 1, 1, 0, 0],n = 67890) == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 200) == [0, 1, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 200) == [0, 1, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 100000000) == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 100000000) == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 1, 1, 1, 1, 0],n = 100) == [0, 1, 0, 0, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 1, 1, 1, 1, 0],n = 100) == [0, 1, 0, 0, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 50) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 50) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 1000000000) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 1000000000) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 1, 1, 1, 1, 0],n = 10000) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 1, 1, 1, 1, 0],n = 10000) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 1000000000) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 1000000000) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 0, 0, 0, 1, 1],n = 50) == [0, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 0, 0, 0, 1, 1],n = 50) == [0, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 1, 0, 0, 0, 0],n = 50) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 1, 0, 0, 0, 0],n = 50) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 0, 0, 1, 0, 0],n = 30) == [0, 0, 1, 0, 0, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 0, 0, 1, 0, 0],n = 30) == [0, 0, 1, 0, 0, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 1, 0, 0, 0, 0],n = 500) == [0, 1, 0, 0, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 1, 0, 0, 0, 0],n = 500) == [0, 1, 0, 0, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 0, 1, 1, 0],n = 15) == [0, 0, 0, 1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 0, 1, 1, 0],n = 15) == [0, 0, 0, 1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 0, 1, 0, 0],n = 15) == [0, 0, 0, 1, 0, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 0, 1, 0, 0],n = 15) == [0, 0, 0, 1, 0, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 0, 0, 1, 0, 1],n = 1000000) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 0, 0, 1, 0, 1],n = 1000000) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 1, 1, 1, 1, 0],n = 50) == [0, 0, 1, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 1, 1, 1, 1, 0],n = 50) == [0, 0, 1, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 999999999) == [0, 1, 0, 0, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 999999999) == [0, 1, 0, 0, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 1, 1, 0, 1],n = 15) == [0, 0, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 1, 1, 0, 1],n = 15) == [0, 0, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 1, 0, 0, 1, 1],n = 1000) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 1, 0, 0, 1, 1],n = 1000) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 78654321) == [0, 1, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 78654321) == [0, 1, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 1500000000) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 1500000000) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 50) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 50) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 0, 1, 0, 1, 0],n = 1000000000) == [0, 0, 0, 1, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 0, 1, 0, 1, 0],n = 1000000000) == [0, 0, 0, 1, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 1, 0, 1, 0, 0],n = 200) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 1, 0, 1, 0, 0],n = 200) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 1, 1, 0, 0, 1],n = 1000000000) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 1, 1, 0, 0, 1],n = 1000000000) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 0, 1, 1, 0, 1],n = 10) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 0, 1, 1, 0, 1],n = 10) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 0, 1, 0, 1, 0],n = 1000000) == [0, 1, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 0, 1, 0, 1, 0],n = 1000000) == [0, 1, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 100) == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 100) == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 0, 0, 1, 1, 1],n = 15) == [0, 1, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 0, 0, 1, 1, 1],n = 15) == [0, 1, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 14) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 14) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 1000) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 1000) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 999999999) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 999999999) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 0, 0, 1, 1, 0],n = 1000) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 0, 0, 1, 1, 0],n = 1000) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 0, 1, 0, 1, 0],n = 14) == [0, 1, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 0, 1, 0, 1, 0],n = 14) == [0, 1, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 1, 1, 1, 0, 1],n = 10) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 1, 1, 1, 0, 1],n = 10) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 0, 0, 1, 0, 1],n = 60) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 0, 0, 1, 0, 1],n = 60) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 1, 1, 0, 0, 0],n = 30) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 1, 1, 0, 0, 0],n = 30) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 100) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 100) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 500000000) == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 500000000) == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 1, 0, 0, 1, 0],n = 150) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 1, 0, 0, 1, 0],n = 150) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 1500) == [0, 1, 0, 0, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 1500) == [0, 1, 0, 0, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 7) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 7) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 1, 0, 1, 0, 1],n = 1000000000) == [0, 0, 0, 1, 0, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 1, 0, 1, 0, 1],n = 1000000000) == [0, 0, 0, 1, 0, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 1, 0, 0, 1, 1],n = 100000) == [0, 1, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 1, 0, 0, 1, 1],n = 100000) == [0, 1, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 0, 0, 1, 1],n = 50) == [0, 0, 0, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 0, 0, 1, 1],n = 50) == [0, 0, 0, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 1, 0, 0, 1, 1],n = 30) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 1, 0, 0, 1, 1],n = 30) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 20) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 20) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 1, 1, 0, 1, 0, 1, 0],n = 1000000) == [0, 1, 1, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 1, 1, 0, 1, 0, 1, 0],n = 1000000) == [0, 1, 1, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 750) == [0, 1, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 750) == [0, 1, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 0, 1, 0, 1, 1],n = 12) == [0, 0, 0, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 0, 1, 0, 1, 1],n = 12) == [0, 0, 0, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 100) == [0, 0, 1, 1, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 100) == [0, 0, 1, 1, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 1, 1, 0, 0],n = 20) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 1, 1, 0, 0],n = 20) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 0, 1, 1, 0, 0, 1],n = 1000) == [0, 1, 0, 1, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 0, 1, 1, 0, 0, 1],n = 1000) == [0, 1, 0, 1, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 0, 0, 1, 1],n = 10000) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 0, 0, 1, 1],n = 10000) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 1, 0, 0, 0, 0, 0, 1],n = 8) == [0, 0, 1, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 1, 0, 0, 0, 0, 0, 1],n = 8) == [0, 0, 1, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 0, 1, 1, 0, 0, 0],n = 500000000) == [0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 0, 1, 1, 0, 0, 0],n = 500000000) == [0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [1, 0, 1, 1, 0, 1, 1, 1],n = 20) == [0, 0, 1, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [1, 0, 1, 1, 0, 1, 1, 1],n = 20) == [0, 0, 1, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(cells = [0, 0, 1, 1, 0, 0, 1, 1],n = 100) == [0, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cells = [0, 0, 1, 1, 0, 0, 1, 1],n = 100) == [0, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 5) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 2) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 15) == [0, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 1) == [0, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [0, 1, 1, 0, 1, 1, 1, 0],n = 2) == [0, 1, 0, 1, 1, 1, 0, 0]
    assert candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 15) == [0, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [1, 1, 0, 1, 0, 0, 1, 1],n = 15) == [0, 0, 1, 1, 0, 0, 0, 0]
    assert candidate(cells = [1, 0, 0, 1, 0, 0, 1, 0],n = 1000000000) == [0, 0, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 2) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [0, 1, 1, 0, 1, 1, 0, 0],n = 15) == [0, 0, 0, 1, 0, 0, 0, 0]
    assert candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 3) == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(cells = [0, 0, 0, 0, 0, 1, 0, 0],n = 5) == [0, 1, 1, 1, 0, 0, 0, 0]
    assert candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 1) == [0, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [0, 1, 1, 1, 1, 1, 1, 0],n = 14) == [0, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [0, 1, 0, 1, 1, 0, 0, 1],n = 7) == [0, 0, 1, 1, 0, 0, 0, 0]
    assert candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 30) == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(cells = [0, 1, 1, 0, 0, 1, 1, 0],n = 20) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [1, 0, 0, 1, 0, 0, 1, 0],n = 28) == [0, 0, 1, 1, 1, 0, 0, 0]
    assert candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 15) == [0, 0, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [1, 1, 0, 1, 1, 0, 1, 1],n = 7) == [0, 0, 1, 0, 0, 1, 0, 0]
    assert candidate(cells = [0, 1, 1, 1, 1, 1, 1, 0],n = 1000) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(cells = [1, 1, 0, 0, 0, 0, 1, 1],n = 10) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [1, 0, 1, 0, 0, 0, 1, 1],n = 100) == [0, 0, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 20) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(cells = [0, 1, 0, 0, 1, 0, 0, 1],n = 1000) == [0, 1, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [0, 1, 1, 1, 0, 1, 1, 0],n = 500) == [0, 1, 1, 0, 1, 0, 0, 0]
    assert candidate(cells = [0, 0, 1, 0, 0, 1, 0, 0],n = 1000000000) == [0, 0, 1, 0, 0, 1, 0, 0]
    assert candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 50) == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(cells = [0, 0, 0, 1, 1, 1, 1, 0],n = 10) == [0, 1, 1, 1, 1, 0, 1, 0]
    assert candidate(cells = [0, 1, 0, 0, 0, 1, 0, 1],n = 300) == [0, 0, 1, 1, 0, 1, 1, 0]
    assert candidate(cells = [1, 0, 1, 1, 0, 0, 1, 0],n = 10) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [0, 1, 1, 1, 0, 1, 1, 0],n = 2000000000) == [0, 1, 0, 0, 0, 1, 1, 0]
    assert candidate(cells = [0, 0, 0, 1, 1, 1, 0, 0],n = 999999999) == [0, 1, 0, 1, 0, 1, 0, 0]
    assert candidate(cells = [1, 0, 0, 1, 1, 0, 0, 1],n = 1250) == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(cells = [1, 1, 1, 0, 0, 1, 1, 1],n = 25) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(cells = [0, 1, 1, 1, 0, 1, 1, 0],n = 20) == [0, 0, 0, 0, 1, 0, 1, 0]
    assert candidate(cells = [1, 0, 0, 0, 0, 1, 0, 0],n = 1000) == [0, 0, 0, 0, 0, 1, 0, 0]
    assert candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 1000000000) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [1, 1, 0, 0, 1, 0, 0, 1],n = 1000) == [0, 1, 0, 1, 1, 1, 1, 0]
    assert candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 1000000) == [0, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [1, 1, 1, 0, 1, 0, 1, 1],n = 1000000000) == [0, 1, 1, 1, 0, 1, 1, 0]
    assert candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 5) == [0, 1, 0, 0, 1, 1, 1, 0]
    assert candidate(cells = [1, 1, 0, 0, 1, 1, 0, 0],n = 500000000) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 30) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [1, 1, 0, 0, 1, 1, 0, 0],n = 67890) == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 200) == [0, 1, 0, 0, 0, 0, 1, 0]
    assert candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 100000000) == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(cells = [0, 0, 1, 1, 1, 1, 1, 0],n = 100) == [0, 1, 0, 0, 1, 0, 0, 0]
    assert candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 50) == [0, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [0, 0, 0, 0, 0, 0, 0, 0],n = 1000000000) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [0, 1, 1, 1, 1, 1, 1, 0],n = 10000) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 1000000000) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(cells = [1, 1, 1, 0, 0, 0, 1, 1],n = 50) == [0, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(cells = [1, 1, 1, 1, 0, 0, 0, 0],n = 50) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [0, 0, 1, 0, 0, 1, 0, 0],n = 30) == [0, 0, 1, 0, 0, 1, 0, 0]
    assert candidate(cells = [0, 0, 0, 1, 0, 0, 0, 0],n = 500) == [0, 1, 0, 0, 1, 1, 0, 0]
    assert candidate(cells = [1, 1, 0, 0, 0, 1, 1, 0],n = 15) == [0, 0, 0, 1, 0, 0, 0, 0]
    assert candidate(cells = [1, 1, 0, 0, 0, 1, 0, 0],n = 15) == [0, 0, 0, 1, 0, 1, 0, 0]
    assert candidate(cells = [1, 0, 1, 0, 0, 1, 0, 1],n = 1000000) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [0, 0, 1, 1, 1, 1, 1, 0],n = 50) == [0, 0, 1, 1, 1, 0, 0, 0]
    assert candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 999999999) == [0, 1, 0, 0, 1, 1, 1, 0]
    assert candidate(cells = [1, 1, 0, 0, 1, 1, 0, 1],n = 15) == [0, 0, 0, 0, 0, 0, 1, 0]
    assert candidate(cells = [0, 0, 1, 1, 0, 0, 1, 1],n = 1000) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 78654321) == [0, 1, 0, 0, 0, 0, 1, 0]
    assert candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 1500000000) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 50) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [0, 1, 1, 0, 1, 0, 1, 0],n = 1000000000) == [0, 0, 0, 1, 0, 0, 0, 0]
    assert candidate(cells = [1, 1, 0, 1, 0, 1, 0, 0],n = 200) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [1, 0, 0, 1, 1, 0, 0, 1],n = 1000000000) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [0, 1, 0, 0, 1, 1, 0, 1],n = 10) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [0, 0, 1, 0, 1, 0, 1, 0],n = 1000000) == [0, 1, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [1, 0, 0, 0, 0, 0, 0, 1],n = 100) == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(cells = [1, 1, 1, 0, 0, 1, 1, 1],n = 15) == [0, 1, 0, 0, 0, 0, 1, 0]
    assert candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 14) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 1000) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [1, 0, 1, 0, 1, 0, 1, 0],n = 999999999) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [0, 1, 1, 0, 0, 1, 1, 0],n = 1000) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [0, 1, 0, 0, 1, 0, 1, 0],n = 14) == [0, 1, 0, 0, 1, 0, 1, 0]
    assert candidate(cells = [1, 0, 1, 1, 1, 1, 0, 1],n = 10) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(cells = [1, 0, 1, 0, 0, 1, 0, 1],n = 60) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [0, 0, 0, 1, 1, 0, 0, 0],n = 30) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 100) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [0, 1, 0, 1, 0, 1, 0, 1],n = 500000000) == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(cells = [1, 0, 1, 1, 0, 0, 1, 0],n = 150) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 1500) == [0, 1, 0, 0, 0, 0, 1, 0]
    assert candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 7) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [1, 0, 1, 1, 0, 1, 0, 1],n = 1000000000) == [0, 0, 0, 1, 0, 0, 1, 0]
    assert candidate(cells = [1, 0, 1, 1, 0, 0, 1, 1],n = 100000) == [0, 1, 1, 0, 1, 0, 1, 0]
    assert candidate(cells = [1, 1, 0, 0, 0, 0, 1, 1],n = 50) == [0, 0, 0, 1, 1, 0, 0, 0]
    assert candidate(cells = [0, 0, 1, 1, 0, 0, 1, 1],n = 30) == [0, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [0, 0, 1, 1, 1, 1, 0, 0],n = 20) == [0, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(cells = [0, 1, 1, 0, 1, 0, 1, 0],n = 1000000) == [0, 1, 1, 1, 1, 0, 0, 0]
    assert candidate(cells = [1, 1, 0, 1, 0, 1, 0, 1],n = 750) == [0, 1, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [1, 1, 1, 0, 1, 0, 1, 1],n = 12) == [0, 0, 0, 0, 1, 0, 1, 0]
    assert candidate(cells = [1, 1, 1, 1, 1, 1, 1, 1],n = 100) == [0, 0, 1, 1, 1, 1, 0, 0]
    assert candidate(cells = [1, 1, 0, 0, 1, 1, 0, 0],n = 20) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [1, 0, 0, 1, 1, 0, 0, 1],n = 1000) == [0, 1, 0, 1, 1, 0, 1, 0]
    assert candidate(cells = [1, 1, 0, 0, 0, 0, 1, 1],n = 10000) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [1, 1, 0, 0, 0, 0, 0, 1],n = 8) == [0, 0, 1, 1, 1, 0, 0, 0]
    assert candidate(cells = [0, 0, 0, 1, 1, 0, 0, 0],n = 500000000) == [0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(cells = [1, 0, 1, 1, 0, 1, 1, 1],n = 20) == [0, 0, 1, 1, 1, 0, 0, 0]
    assert candidate(cells = [0, 0, 1, 1, 0, 0, 1, 1],n = 100) == [0, 1, 1, 1, 1, 1, 1, 0]


