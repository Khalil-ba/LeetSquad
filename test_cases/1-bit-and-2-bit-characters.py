def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 1, 1, 0, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 1, 1, 0, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 1, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 1, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 0, 1, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 0, 1, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 0, 1, 0, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 0, 1, 0, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 0, 1, 1, 0, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 0, 1, 1, 0, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 0, 1, 0, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 0, 1, 0, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 0, 0, 0, 0, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 0, 0, 0, 0, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 1, 1, 0, 1, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 1, 1, 0, 1, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 1, 0, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 1, 0, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [0, 1, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [0, 1, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bits = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bits = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(bits = [1, 1, 1, 0]) == False
    assert candidate(bits = [0, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0]) == True
    assert candidate(bits = [0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 0, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 1, 1, 0]) == False
    assert candidate(bits = [0, 0, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 0]) == True
    assert candidate(bits = [0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 1, 0, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]) == True
    assert candidate(bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(bits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 0, 1, 1, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1]) == True
    assert candidate(bits = [0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 1, 1, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 0, 0, 0, 0]) == True
    assert candidate(bits = [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(bits = [0, 1, 1, 0, 1, 1, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]) == True
    assert candidate(bits = [0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [0, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True


