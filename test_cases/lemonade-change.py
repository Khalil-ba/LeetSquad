def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 20, 20, 5, 5, 20, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 20, 20, 5, 5, 20, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 10, 5, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 10, 5, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 20, 5, 5, 5, 10, 5, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 20, 5, 5, 5, 10, 5, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 10, 5, 20, 10, 5, 5, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 10, 5, 20, 10, 5, 5, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 5, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 5, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 10, 5, 10, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 10, 5, 10, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 20, 10, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 20, 10, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 20, 5, 10, 5, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 20, 5, 10, 5, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 20, 5, 5, 10, 10, 5, 10, 20, 5, 5, 10, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 20, 5, 5, 10, 10, 5, 10, 20, 5, 5, 10, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 10, 10, 5, 5, 10, 10, 5, 10, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 10, 10, 5, 5, 10, 10, 5, 10, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 5, 10, 20, 10, 5, 5, 20, 5, 5, 5, 10, 10, 5, 20, 10, 20, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 5, 10, 20, 10, 5, 5, 20, 5, 5, 5, 10, 10, 5, 20, 10, 20, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 5, 5, 10, 5, 5, 10, 20, 5, 5, 10, 5, 5, 20, 10, 5, 20, 5, 5, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 5, 5, 10, 5, 5, 10, 20, 5, 5, 10, 5, 5, 20, 10, 5, 20, 5, 5, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 5, 5, 10, 5, 10, 20, 20, 5, 10, 20, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 5, 5, 10, 5, 10, 20, 20, 5, 10, 20, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [20, 5, 5, 10, 5, 10, 20, 5, 10, 5, 10, 20, 5, 10, 5, 10, 20, 5, 10, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [20, 5, 5, 10, 5, 10, 20, 5, 10, 5, 10, 20, 5, 10, 5, 10, 20, 5, 10, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 5, 10, 10, 20, 5, 10, 20, 5, 10, 20, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 5, 10, 10, 20, 5, 10, 20, 5, 10, 20, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 20, 10, 5, 20, 10, 5, 10, 20, 5, 5, 5, 10, 10, 5, 20, 10, 20, 5, 5, 10, 10, 10, 20, 5, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 20, 10, 5, 20, 10, 5, 10, 20, 5, 5, 5, 10, 10, 5, 20, 10, 20, 5, 5, 10, 10, 10, 20, 5, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 10, 5, 10, 5, 5, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10, 10, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10, 10, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 10, 5, 10, 5, 5, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10, 10, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10, 10, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 10, 10, 20, 5, 10, 5, 10, 20, 10, 5, 5, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 10, 10, 20, 5, 10, 5, 10, 20, 10, 5, 5, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 10, 5, 20, 10, 5, 5, 20, 20, 5, 10, 5, 10, 5, 20, 10, 20, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 10, 5, 20, 10, 5, 5, 20, 20, 5, 10, 5, 10, 5, 20, 10, 20, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 10, 5, 10, 20, 5, 10, 10, 20, 5, 5, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 10, 5, 10, 20, 5, 10, 10, 20, 5, 5, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 5, 10, 20, 5, 10, 10, 20, 5, 10, 20, 10, 5, 5, 5, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 5, 10, 20, 5, 10, 10, 20, 5, 10, 20, 10, 5, 5, 5, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [20, 5, 5, 5, 10, 10, 20, 5, 5, 10, 5, 10, 20, 20, 5, 5, 10, 5, 10, 20, 5, 5, 10, 5, 10, 20, 20, 5, 5, 10, 5, 10, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [20, 5, 5, 5, 10, 10, 20, 5, 5, 10, 5, 10, 20, 20, 5, 5, 10, 5, 10, 20, 5, 5, 10, 5, 10, 20, 20, 5, 5, 10, 5, 10, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 20, 5, 10, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 20, 5, 10, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 10, 5, 5, 10, 20, 5, 10, 5, 5, 10, 10, 5, 5, 10, 20, 5, 10, 5, 5, 10, 20, 5, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 10, 5, 5, 10, 20, 5, 10, 5, 5, 10, 10, 5, 5, 10, 20, 5, 10, 5, 5, 10, 20, 5, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 10, 10, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 10, 10, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 5, 10, 20, 10, 5, 20, 5, 10, 5, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 5, 10, 20, 10, 5, 20, 5, 10, 5, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 10, 10, 20, 20, 20, 10, 10, 10, 10, 10, 10, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 10, 10, 20, 20, 20, 10, 10, 10, 10, 10, 10, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 20, 5, 5, 5, 10, 10, 10, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 20, 5, 5, 5, 10, 10, 10, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 20, 10, 10, 20, 5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 20, 10, 10, 20, 5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 10, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 10, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 20, 10, 20, 5, 10, 5, 20, 10, 20, 5, 10, 5, 20, 10, 20, 5, 10, 5, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 20, 10, 20, 5, 10, 5, 20, 10, 20, 5, 10, 5, 20, 10, 20, 5, 10, 5, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 5, 10, 10, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 5, 10, 10, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 10, 20, 5, 10, 10, 20, 5, 5, 10, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 10, 20, 5, 10, 10, 20, 5, 5, 10, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 10, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 10, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [20, 5, 5, 5, 10, 10, 5, 5, 20, 5, 10, 5, 5, 20, 10, 5, 10, 20, 5, 10, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [20, 5, 5, 5, 10, 10, 5, 5, 20, 5, 10, 5, 5, 20, 10, 5, 10, 20, 5, 10, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 20, 20, 20, 5, 5, 10, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 20, 20, 20, 5, 5, 10, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [20, 5, 5, 5, 10, 10, 5, 20, 10, 5, 10, 20, 10, 5, 20, 5, 10, 10, 20, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [20, 5, 5, 5, 10, 10, 5, 20, 10, 5, 10, 20, 10, 5, 20, 5, 10, 10, 20, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [20, 5, 5, 5, 10, 10, 20, 5, 5, 10, 5, 10, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [20, 5, 5, 5, 10, 10, 20, 5, 5, 10, 5, 10, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 20, 5, 5, 10, 5, 20, 10, 10, 20, 5, 10, 5, 20, 10, 5, 5, 10, 20, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 20, 5, 5, 10, 5, 20, 10, 10, 20, 5, 10, 5, 20, 10, 5, 5, 10, 20, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 20, 10, 5, 20, 10, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 20, 10, 5, 20, 10, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [20, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [20, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 10, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 10, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 20, 5, 10, 10, 20, 5, 5, 5, 10, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 20, 5, 10, 10, 20, 5, 5, 5, 10, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 20, 20, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 20, 20, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 10, 20, 5, 5, 5, 10, 20, 10, 5, 5, 10, 20, 5, 5, 5, 10, 20, 10, 5, 5, 10, 20, 5, 5, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 10, 20, 5, 5, 5, 10, 20, 10, 5, 5, 10, 20, 5, 5, 5, 10, 20, 10, 5, 5, 10, 20, 5, 5, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [20, 5, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 5, 10, 5, 10, 5, 10, 5, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [20, 5, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 5, 10, 5, 10, 5, 10, 5, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 20, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 20, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 10, 10, 5, 20, 10, 5, 5, 20, 10, 5, 5, 20, 10, 5, 5, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 10, 10, 5, 20, 10, 5, 5, 20, 10, 5, 5, 20, 10, 5, 5, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 10, 5, 10, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 10, 5, 10, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(bills = [5, 20, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bills = [5, 20, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(bills = [5, 5, 5, 5, 20, 20, 5, 5, 20, 5]) == False
    assert candidate(bills = [5, 5, 10, 10, 5, 20]) == True
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20]) == True
    assert candidate(bills = [5, 5, 5, 5, 20, 5, 5, 5, 10, 5, 20]) == True
    assert candidate(bills = [5, 5, 10, 10, 20]) == False
    assert candidate(bills = [5, 5, 10, 10, 5, 20, 10, 5, 5, 20]) == False
    assert candidate(bills = [5, 10, 5, 5, 20]) == True
    assert candidate(bills = [5, 5, 5, 5, 10, 5, 10, 20]) == True
    assert candidate(bills = [5, 10, 5, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 20]) == True
    assert candidate(bills = [10, 10]) == False
    assert candidate(bills = [5, 5, 5, 10, 20]) == True
    assert candidate(bills = [5, 5, 5, 5, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 10]) == True
    assert candidate(bills = [5, 10, 20, 10, 5]) == False
    assert candidate(bills = [5, 10, 5, 20]) == True
    assert candidate(bills = [5, 5, 5, 5, 20, 5, 10, 5, 20]) == True
    assert candidate(bills = [5, 20, 5, 5, 10, 10, 5, 10, 20, 5, 5, 10, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 10, 10, 5, 5, 10, 10, 5, 10, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 10, 5, 10, 20, 10, 5, 5, 20, 5, 5, 5, 10, 10, 5, 20, 10, 20, 5]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20]) == True
    assert candidate(bills = [5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 10, 5, 5, 5, 10, 5, 5, 10, 20, 5, 5, 10, 5, 5, 20, 10, 5, 20, 5, 5, 20]) == True
    assert candidate(bills = [5, 5, 10, 5, 5, 10, 5, 10, 20, 20, 5, 10, 20, 5]) == False
    assert candidate(bills = [20, 5, 5, 10, 5, 10, 20, 5, 10, 5, 10, 20, 5, 10, 5, 10, 20, 5, 10, 5, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 5, 10, 10, 20, 5, 10, 20, 5, 10, 20, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == False
    assert candidate(bills = [5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == True
    assert candidate(bills = [5, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20]) == False
    assert candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5]) == False
    assert candidate(bills = [5, 10, 20, 10, 5, 20, 10, 5, 10, 20, 5, 5, 5, 10, 10, 5, 20, 10, 20, 5, 5, 10, 10, 10, 20, 5, 10]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 10, 5, 10, 5, 5, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10, 10, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10, 10, 20, 20]) == False
    assert candidate(bills = [5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == True
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 10, 10, 20, 5, 10, 5, 10, 20, 10, 5, 5, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 10, 10, 5, 20, 10, 5, 5, 20, 20, 5, 10, 5, 10, 5, 20, 10, 20, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(bills = [5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 10, 5, 10, 20, 5, 10, 10, 20, 5, 5, 5, 10, 20]) == False
    assert candidate(bills = [5, 5, 10, 5, 10, 20, 5, 10, 10, 20, 5, 10, 20, 10, 5, 5, 5, 20, 20, 20]) == False
    assert candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [20, 5, 5, 5, 10, 10, 20, 5, 5, 10, 5, 10, 20, 20, 5, 5, 10, 5, 10, 20, 5, 5, 10, 5, 10, 20, 20, 5, 5, 10, 5, 10, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == True
    assert candidate(bills = [5, 10, 20, 5, 10, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20, 5, 5, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 10, 5, 5, 10, 20, 5, 10, 5, 5, 10, 10, 5, 5, 10, 20, 5, 10, 5, 5, 10, 20, 5, 10]) == True
    assert candidate(bills = [5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 10, 10, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20]) == False
    assert candidate(bills = [5, 5, 10, 5, 10, 20, 10, 5, 20, 5, 10, 5, 5, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 10, 10, 20, 20, 20, 10, 10, 10, 10, 10, 10, 5, 5, 5]) == False
    assert candidate(bills = [5, 20, 5, 5, 5, 10, 10, 10, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 10, 5, 20, 10, 10, 20, 5, 10, 5, 20, 5, 10, 5, 20, 5, 10, 5, 20]) == False
    assert candidate(bills = [5, 5, 10, 10, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20]) == False
    assert candidate(bills = [5, 10, 5, 20, 10, 20, 5, 10, 5, 20, 10, 20, 5, 10, 5, 20, 10, 20, 5, 10, 5, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 10, 5, 5, 20, 20, 5, 5, 10, 10, 20, 20]) == False
    assert candidate(bills = [5, 5, 10, 10, 20, 5, 10, 10, 20, 5, 5, 10, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 10, 20, 20, 5, 5, 10, 10, 20, 5, 5, 10]) == False
    assert candidate(bills = [20, 5, 5, 5, 10, 10, 5, 5, 20, 5, 10, 5, 5, 20, 10, 5, 10, 20, 5, 10, 20, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 10, 10, 10, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 20, 20, 20, 5, 5, 10, 10, 20]) == False
    assert candidate(bills = [20, 5, 5, 5, 10, 10, 5, 20, 10, 5, 10, 20, 10, 5, 20, 5, 10, 10, 20, 5, 5]) == False
    assert candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [20, 5, 5, 5, 10, 10, 20, 5, 5, 10, 5, 10, 20, 20]) == False
    assert candidate(bills = [5, 20, 5, 5, 10, 5, 20, 10, 10, 20, 5, 10, 5, 20, 10, 5, 5, 10, 20, 5, 5]) == False
    assert candidate(bills = [5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20, 5, 20]) == False
    assert candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 10, 20, 10, 5, 20, 10, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20, 10, 5, 20]) == False
    assert candidate(bills = [20, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10, 5, 5, 5, 10, 10]) == False
    assert candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 20, 20, 20]) == False
    assert candidate(bills = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == True
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5, 5, 10, 10, 20, 5, 5]) == True
    assert candidate(bills = [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 20, 20, 20, 20, 5, 5, 10, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 5, 10, 20, 5, 10, 10, 20, 5, 5, 5, 10, 20, 20]) == False
    assert candidate(bills = [5, 10, 20, 20, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5]) == False
    assert candidate(bills = [5, 10, 10, 20, 5, 5, 5, 10, 20, 10, 5, 5, 10, 20, 5, 5, 5, 10, 20, 10, 5, 5, 10, 20, 5, 5, 5, 10, 20]) == False
    assert candidate(bills = [20, 5, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 20, 5, 10, 5, 10, 5, 10, 5, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(bills = [5, 5, 10, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20, 5, 10, 10, 20]) == False
    assert candidate(bills = [5, 5, 10, 20, 20, 20, 20, 5, 5, 5, 10, 10, 10, 20, 20, 20, 20, 10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(bills = [5, 5, 10, 10, 5, 20, 10, 5, 5, 20, 10, 5, 5, 20, 10, 5, 5, 5, 10, 20]) == False
    assert candidate(bills = [5, 10, 5, 10, 5, 10, 20, 5, 10, 20, 5, 10, 20]) == False
    assert candidate(bills = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20]) == False
    assert candidate(bills = [5, 20, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == False


