def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = [3, 4, 5],n = 5) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 4, 5],n = 5) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 4, 6],n = 7) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 4, 6],n = 7) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 5, 7, 9],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 5, 7, 9],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 9],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 9],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2],n = 4) == ['Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2],n = 4) == ['Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5],n = 5) == ['Push', 'Push', 'Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5],n = 5) == ['Push', 'Push', 'Push', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 3, 5],n = 5) == ['Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 3, 5],n = 5) == ['Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 3, 4],n = 5) == ['Push', 'Pop', 'Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 3, 4],n = 5) == ['Push', 'Pop', 'Push', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 4, 6, 8],n = 10) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 4, 6, 8],n = 10) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 3, 4],n = 4) == ['Push', 'Pop', 'Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 3, 4],n = 4) == ['Push', 'Pop', 'Push', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1],n = 1) == ['Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1],n = 1) == ['Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3],n = 3) == ['Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3],n = 3) == ['Push', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [4, 5, 6],n = 6) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [4, 5, 6],n = 6) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5],n = 5) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5],n = 5) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 6, 7, 8],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 6, 7, 8],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3],n = 3) == ['Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3],n = 3) == ['Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 6],n = 7) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 6],n = 7) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 6, 7, 10],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 6, 7, 10],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 6, 7, 8, 9, 10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 6, 7, 8, 9, 10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 6, 9],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 6, 9],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 9, 13, 17, 21],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 9, 13, 17, 21],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 4, 8, 16],n = 20) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 4, 8, 16],n = 20) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 6, 9, 12, 15, 18],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 6, 9, 12, 15, 18],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 4, 5, 7, 8, 10],n = 12) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 4, 5, 7, 8, 10],n = 12) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 9, 11, 13, 15],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 9, 11, 13, 15],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [4, 8, 16, 32, 64],n = 100) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [4, 8, 16, 32, 64],n = 100) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [6, 8, 10, 12, 14],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [6, 8, 10, 12, 14],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 6, 10, 14, 18],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 6, 10, 14, 18],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 4, 8, 16, 32, 64, 128],n = 150) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 4, 8, 16, 32, 64, 128],n = 150) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 8, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 8, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7, 9, 11],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7, 9, 11],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15],n = 20) == ['Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15],n = 20) == ['Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 4, 6, 8, 10, 12, 14, 16],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 4, 6, 8, 10, 12, 14, 16],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 6, 7, 9],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 6, 7, 9],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 11, 13, 15],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 11, 13, 15],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 5, 8, 11, 14, 17],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 5, 8, 11, 14, 17],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 7, 10, 13, 16, 19, 22, 25],n = 30) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 7, 10, 13, 16, 19, 22, 25],n = 30) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 14, 21, 28],n = 35) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 14, 21, 28],n = 35) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 6, 9, 12, 15, 18, 21],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 6, 9, 12, 15, 18, 21],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 7, 10, 13],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 7, 10, 13],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 8, 11, 14],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 8, 11, 14],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 7, 11, 15, 19, 23, 27, 31, 35],n = 40) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 7, 11, 15, 19, 23, 27, 31, 35],n = 40) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 7, 10, 11],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 7, 10, 11],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 12, 15, 19, 20],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 12, 15, 19, 20],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 5, 7, 9, 11, 13, 15],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 5, 7, 9, 11, 13, 15],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 5, 10, 15, 20, 25, 30],n = 30) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 5, 10, 15, 20, 25, 30],n = 30) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 5, 10, 15, 20, 25, 30, 35],n = 40) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 5, 10, 15, 20, 25, 30, 35],n = 40) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [4, 7, 10, 13, 16, 19],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [4, 7, 10, 13, 16, 19],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 8, 9, 11],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 8, 9, 11],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 5, 6, 7, 9, 10],n = 10) == ['Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 5, 6, 7, 9, 10],n = 10) == ['Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 5, 6, 8, 11, 12],n = 15) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 5, 6, 8, 11, 12],n = 15) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 5, 6, 7, 9, 10],n = 10) == ['Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 5, 6, 7, 9, 10],n = 10) == ['Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 5, 7, 11, 13],n = 20) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 5, 7, 11, 13],n = 20) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50],n = 55) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50],n = 55) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 14, 21, 28],n = 35) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 14, 21, 28],n = 35) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 6, 8],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 6, 8],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 11, 13, 17, 19],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 11, 13, 17, 19],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 4, 6, 8, 10, 12],n = 15) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 4, 6, 8, 10, 12],n = 15) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 25) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 25) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 14, 21, 28, 35, 42],n = 42) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 14, 21, 28, 35, 42],n = 42) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7, 9, 11, 13],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7, 9, 11, 13],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 7, 10, 13],n = 13) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 7, 10, 13],n = 13) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 5, 9, 13, 17, 21],n = 25) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 5, 9, 13, 17, 21],n = 25) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 11],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 11],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 11, 13],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 11, 13],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 7, 11, 15, 19],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 7, 11, 15, 19],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 14, 21, 28],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 14, 21, 28],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 5, 8, 11, 14, 17, 20],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 5, 8, 11, 14, 17, 20],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 9, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 9, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 6, 8, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 6, 8, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [6, 12, 18, 24, 30],n = 35) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [6, 12, 18, 24, 30],n = 35) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 6],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 6],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 4, 7, 10, 12],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 4, 7, 10, 12],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 6, 9, 12],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 6, 9, 12],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 5, 7, 10, 13],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 5, 7, 10, 13],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 6, 9, 12, 15, 18],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 6, 9, 12, 15, 18],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 5, 8, 11, 14, 17, 20],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 5, 8, 11, 14, 17, 20],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 6, 10, 14, 18],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 6, 10, 14, 18],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 15, 20, 25],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 15, 20, 25],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 6, 9, 12, 15, 18, 21, 24],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 6, 9, 12, 15, 18, 21, 24],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 4, 7, 10],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 4, 7, 10],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 5, 7, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 5, 7, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 12, 14],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 12, 14],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 8, 10, 12],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 8, 10, 12],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 6, 8, 10],n = 12) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 6, 8, 10],n = 12) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],n = 15) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],n = 15) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [11, 22, 33, 44, 55, 66, 77, 88, 99],n = 100) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [11, 22, 33, 44, 55, 66, 77, 88, 99],n = 100) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 5, 7, 9, 10],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 5, 7, 9, 10],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 9, 10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 9, 10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 3, 5, 7, 9, 11],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 3, 5, 7, 9, 11],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 5, 7, 9, 11],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 5, 7, 9, 11],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 5, 7, 8, 10],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 5, 7, 8, 10],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [4, 8, 12, 16, 20, 24, 28],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [4, 8, 12, 16, 20, 24, 28],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [6, 7, 8, 10, 12, 14, 15],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [6, 7, 8, 10, 12, 14, 15],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 6, 10, 14, 18],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 6, 10, 14, 18],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 5, 9, 13, 17],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 5, 9, 13, 17],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 6, 10, 14, 18, 22, 26],n = 30) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 6, 10, 14, 18, 22, 26],n = 30) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 11, 12],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 11, 12],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = [3, 4, 5],n = 5) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push']
    assert candidate(target = [3, 4, 6],n = 7) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [5],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 5, 7, 9],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 7, 9],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 2],n = 4) == ['Push', 'Push']
    assert candidate(target = [1, 2, 3, 4, 5],n = 5) == ['Push', 'Push', 'Push', 'Push', 'Push']
    assert candidate(target = [2, 3, 5],n = 5) == ['Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 3, 4],n = 5) == ['Push', 'Pop', 'Push', 'Push', 'Push']
    assert candidate(target = [2, 4, 6, 8],n = 10) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 3, 4],n = 4) == ['Push', 'Pop', 'Push', 'Push', 'Push']
    assert candidate(target = [1],n = 1) == ['Push']
    assert candidate(target = [1, 2, 3],n = 3) == ['Push', 'Push', 'Push']
    assert candidate(target = [4, 5, 6],n = 6) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push']
    assert candidate(target = [1, 3, 5],n = 5) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 6, 7, 8],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push']
    assert candidate(target = [1, 3],n = 3) == ['Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 4, 6],n = 7) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 4, 6, 7, 10],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 6, 7, 8, 9, 10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push']
    assert candidate(target = [1, 4, 6, 9],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 9, 13, 17, 21],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 2, 4, 8, 16],n = 20) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 6, 9, 12, 15, 18],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 2, 4, 5, 7, 8, 10],n = 12) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 9, 11, 13, 15],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [4, 8, 16, 32, 64],n = 100) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [6, 8, 10, 12, 14],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 6, 10, 14, 18],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 4, 8, 16, 32, 64, 128],n = 150) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 7, 8, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 3, 5, 7, 9, 11],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15],n = 20) == ['Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [2, 4, 6, 8, 10, 12, 14, 16],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 4, 6, 7, 9],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 7, 11, 13, 15],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 5, 8, 11, 14, 17],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 4, 7, 10, 13, 16, 19, 22, 25],n = 30) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [10, 20, 30, 40],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [7, 14, 21, 28],n = 35) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 6, 9, 12, 15, 18, 21],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 4, 7, 10, 13],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 8, 11, 14],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 7, 11, 15, 19, 23, 27, 31, 35],n = 40) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [10, 20, 30],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [7, 8, 9, 10, 11, 12, 13, 14, 15],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push', 'Push']
    assert candidate(target = [3, 7, 10, 11],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [10, 12, 15, 19, 20],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [3, 5, 7, 9, 11, 13, 15],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 5, 10, 15, 20, 25, 30],n = 30) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 5, 10, 15, 20, 25, 30, 35],n = 40) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [4, 7, 10, 13, 16, 19],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 8, 9, 11],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 2, 3, 5, 6, 7, 9, 10],n = 10) == ['Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [2, 5, 6, 8, 11, 12],n = 15) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [1, 2, 3, 5, 6, 7, 9, 10],n = 10) == ['Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [1, 2, 5, 7, 11, 13],n = 20) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [10, 20, 30, 40, 50],n = 55) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [7, 14, 21, 28],n = 35) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 4, 6, 8],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [7, 11, 13, 17, 19],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 4, 6, 8, 10, 12],n = 15) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 25) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [7, 14, 21, 28, 35, 42],n = 42) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 3, 5, 7, 9, 11, 13],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 4, 7, 10, 13],n = 13) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 5, 9, 13, 17, 21],n = 25) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 7, 11],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 7, 11, 13],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 7, 11, 15, 19],n = 25) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [7, 14, 21, 28],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 5, 8, 11, 14, 17, 20],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 7, 9, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [3, 6, 8, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [6, 12, 18, 24, 30],n = 35) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 4, 6],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 3, 4, 7, 10, 12],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 6, 9, 12],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 5, 7, 10, 13],n = 20) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 6, 9, 12, 15, 18],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 5, 8, 11, 14, 17, 20],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 6, 10, 14, 18],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [10, 15, 20, 25],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 6, 9, 12, 15, 18, 21, 24],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 4, 7, 10],n = 10) == ['Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [5, 7, 10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 5, 7, 10],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [10, 12, 14],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [10, 20, 30, 40, 50],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [7, 8, 10, 12],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 3, 6, 8, 10],n = 12) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],n = 15) == ['Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [11, 22, 33, 44, 55, 66, 77, 88, 99],n = 100) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 5, 7, 9, 10],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [5, 7, 9, 10],n = 10) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [1, 3, 5, 7, 9, 11],n = 15) == ['Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 5, 7, 9, 11],n = 12) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [10, 20, 30, 40, 50],n = 50) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [3, 5, 7, 8, 10],n = 15) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Pop', 'Push']
    assert candidate(target = [4, 8, 12, 16, 20, 24, 28],n = 30) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [6, 7, 8, 10, 12, 14, 15],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push']
    assert candidate(target = [2, 6, 10, 14, 18],n = 25) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 5, 9, 13, 17],n = 20) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [2, 6, 10, 14, 18, 22, 26],n = 30) == ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push']
    assert candidate(target = [10, 11, 12],n = 20) == ['Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Pop', 'Push', 'Push', 'Push']


