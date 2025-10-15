def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(team = [0],dist = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0],dist = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 1, 1, 0, 0, 1, 0],dist = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 1, 1, 0, 0, 1, 0],dist = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 1],dist = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 1],dist = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 1, 1, 0, 0, 1],dist = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 1, 1, 0, 0, 1],dist = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 1, 1, 1, 1],dist = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 1, 1, 1, 1],dist = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0],dist = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0],dist = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 1, 1, 0, 0],dist = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 1, 1, 0, 0],dist = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 0, 0, 0, 0],dist = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 0, 0, 0, 0],dist = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0],dist = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0],dist = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 0, 1, 0, 1, 0],dist = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 0, 1, 0, 1, 0],dist = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 0, 0, 0, 0],dist = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 0, 0, 0, 0],dist = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1],dist = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1],dist = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [1],dist = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1],dist = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],dist = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],dist = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],dist = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],dist = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],dist = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],dist = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],dist = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],dist = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],dist = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],dist = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],dist = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],dist = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 1) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 1) == 17: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],dist = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],dist = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],dist = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],dist = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],dist = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],dist = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 4) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 4) == 14: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],dist = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],dist = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],dist = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],dist = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],dist = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],dist = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],dist = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],dist = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],dist = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],dist = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],dist = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],dist = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],dist = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],dist = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],dist = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],dist = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],dist = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],dist = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 12) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 12) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],dist = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],dist = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],dist = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],dist = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],dist = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],dist = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],dist = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],dist = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 17: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],dist = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],dist = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],dist = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],dist = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],dist = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],dist = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 32: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(team = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(team = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 3) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(team = [0],dist = 1) == 0
    assert candidate(team = [0, 0, 1, 1, 0, 0, 1, 0],dist = 2) == 3
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 1],dist = 2) == 1
    assert candidate(team = [0, 0, 1, 1, 0, 0, 1],dist = 2) == 3
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1],dist = 4) == 4
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0],dist = 2) == 1
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
    assert candidate(team = [0, 0, 1, 1, 0, 0],dist = 2) == 2
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 4
    assert candidate(team = [1, 1, 1, 1, 0, 0, 0, 0],dist = 4) == 4
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
    assert candidate(team = [0, 1, 0, 1, 0],dist = 3) == 2
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0],dist = 2) == 3
    assert candidate(team = [1, 1, 1, 1, 0, 0, 0, 0],dist = 2) == 2
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 5
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1],dist = 3) == 4
    assert candidate(team = [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 2) == 5
    assert candidate(team = [1],dist = 1) == 0
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 6
    assert candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],dist = 3) == 6
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 7) == 2
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 20) == 2
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 20) == 10
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 3) == 3
    assert candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],dist = 2) == 6
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 15
    assert candidate(team = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],dist = 6) == 5
    assert candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],dist = 2) == 6
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],dist = 3) == 8
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 0
    assert candidate(team = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 8
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 10
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 5
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 10) == 2
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 2) == 9
    assert candidate(team = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],dist = 4) == 4
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 1) == 17
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 1) == 5
    assert candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],dist = 3) == 8
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 8) == 8
    assert candidate(team = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],dist = 5) == 5
    assert candidate(team = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],dist = 3) == 18
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 12
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 19
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 6
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 10
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 7
    assert candidate(team = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 3) == 6
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 4
    assert candidate(team = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],dist = 6) == 3
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 4) == 14
    assert candidate(team = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],dist = 2) == 6
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],dist = 2) == 4
    assert candidate(team = [0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 7
    assert candidate(team = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],dist = 2) == 4
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 12
    assert candidate(team = [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 5) == 6
    assert candidate(team = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],dist = 2) == 6
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 10
    assert candidate(team = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],dist = 5) == 5
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 17
    assert candidate(team = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],dist = 4) == 6
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 10) == 12
    assert candidate(team = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 3) == 10
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 5
    assert candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],dist = 3) == 6
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 4) == 4
    assert candidate(team = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 6) == 6
    assert candidate(team = [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],dist = 2) == 6
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 13
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 1) == 1
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 3) == 10
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 7
    assert candidate(team = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],dist = 3) == 3
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 11
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 10
    assert candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 12
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 5
    assert candidate(team = [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 3) == 8
    assert candidate(team = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 3) == 9
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 7) == 7
    assert candidate(team = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],dist = 4) == 7
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 4) == 6
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 12) == 2
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],dist = 3) == 12
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 6
    assert candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],dist = 4) == 6
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 4
    assert candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],dist = 5) == 15
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 3) == 4
    assert candidate(team = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],dist = 3) == 5
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 17
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],dist = 3) == 11
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],dist = 4) == 3
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],dist = 4) == 4
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 32
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 8
    assert candidate(team = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 6) == 8
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 10) == 10
    assert candidate(team = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 2) == 4
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 20) == 2
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 13
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 5
    assert candidate(team = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 3) == 5


