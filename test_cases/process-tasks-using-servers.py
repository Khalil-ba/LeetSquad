def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(servers = [3, 3, 2],tasks = [1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 3, 2],tasks = [1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1],tasks = [10, 20, 30, 40, 50]) == [0, 1, 2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1],tasks = [10, 20, 30, 40, 50]) == [0, 1, 2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 1, 4, 3, 2],tasks = [2, 1, 2, 4, 5, 2, 1]) == [1, 4, 1, 4, 1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 1, 4, 3, 2],tasks = [2, 1, 2, 4, 5, 2, 1]) == [1, 4, 1, 4, 1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1],tasks = [10]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1],tasks = [10]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30],tasks = [3, 2, 1]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30],tasks = [3, 2, 1]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3],tasks = [3, 2, 1]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3],tasks = [3, 2, 1]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5],tasks = [5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5],tasks = [5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30],tasks = [1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30],tasks = [1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 4, 3, 2, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 4, 3, 4, 2, 3, 1, 4, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 4, 3, 2, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 4, 3, 4, 2, 3, 1, 4, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30],tasks = [1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30],tasks = [1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1],tasks = [10, 10, 10, 10, 10]) == [0, 1, 2, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1],tasks = [10, 10, 10, 10, 10]) == [0, 1, 2, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 4, 3, 2, 1],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 4, 3, 2, 1],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 5, 1, 3, 0, 5, 1, 4, 2, 3, 0, 3, 0, 5, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 5, 1, 3, 0, 5, 1, 4, 2, 3, 0, 3, 0, 5, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 15, 20, 25, 30],tasks = [5, 10, 15, 20, 25, 30, 35, 40]) == [0, 1, 2, 3, 4, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 15, 20, 25, 30],tasks = [5, 10, 15, 20, 25, 30, 35, 40]) == [0, 1, 2, 3, 4, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50],tasks = [5, 15, 25, 35, 45, 55, 65]) == [0, 1, 2, 3, 4, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50],tasks = [5, 15, 25, 35, 45, 55, 65]) == [0, 1, 2, 3, 4, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],tasks = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 3, 6, 0, 9, 2, 4, 8, 10, 7, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],tasks = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 3, 6, 0, 9, 2, 4, 8, 10, 7, 5]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 1, 2],tasks = [2, 3, 1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3]) == [1, 2, 1, 1, 2, 1, 2, 0, 1, 2, 1, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 1, 2],tasks = [2, 3, 1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3]) == [1, 2, 1, 1, 2, 1, 2, 0, 1, 2, 1, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 5, 2, 7, 6],tasks = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 0, 2, 1, 0, 4, 2, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 5, 2, 7, 6],tasks = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 0, 2, 1, 0, 4, 2, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8, 9, 8, 9, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8, 9, 8, 9, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 4, 3, 2, 1],tasks = [2, 3, 4, 5, 1, 2, 3, 4, 5]) == [4, 3, 4, 2, 3, 3, 4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 4, 3, 2, 1],tasks = [2, 3, 4, 5, 1, 2, 3, 4, 5]) == [4, 3, 4, 2, 3, 3, 4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [100, 200, 150, 50],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [100, 200, 150, 50],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [100, 100, 100, 100, 100],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [100, 100, 100, 100, 100],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [20, 10, 30, 40, 50],tasks = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [1, 0, 2, 3, 4, 1, 0, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [20, 10, 30, 40, 50],tasks = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [1, 0, 2, 3, 4, 1, 0, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 3, 1, 4, 5, 2, 3, 1, 4, 5],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [2, 7, 0, 5, 1, 6, 3, 8, 4, 9, 2, 7, 0, 5, 1, 6, 3, 8, 4, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 3, 1, 4, 5, 2, 3, 1, 4, 5],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [2, 7, 0, 5, 1, 6, 3, 8, 4, 9, 2, 7, 0, 5, 1, 6, 3, 8, 4, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [15, 25, 5, 20, 10],tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == [2, 4, 0, 3, 1, 2, 4, 0, 3, 1, 2, 4, 0, 3, 1, 2, 4, 0, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [15, 25, 5, 20, 10],tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == [2, 4, 0, 3, 1, 2, 4, 0, 3, 1, 2, 4, 0, 3, 1, 2, 4, 0, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 3, 5, 7, 11],tasks = [30, 10, 20, 40, 50, 15, 25, 35, 45, 55]) == [0, 1, 2, 3, 4, 1, 2, 1, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 3, 5, 7, 11],tasks = [30, 10, 20, 40, 50, 15, 25, 35, 45, 55]) == [0, 1, 2, 3, 4, 1, 2, 1, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [7, 5, 3, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [3, 3, 2, 3, 1, 2, 0, 3, 1, 2, 0, 3, 1, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [7, 5, 3, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [3, 3, 2, 3, 1, 2, 0, 3, 1, 2, 0, 3, 1, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 3, 8, 6],tasks = [2, 6, 4, 1, 7, 3, 5]) == [1, 0, 1, 3, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 3, 8, 6],tasks = [2, 6, 4, 1, 7, 3, 5]) == [1, 0, 1, 3, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 2, 1, 4, 5],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [2, 1, 0, 3, 4, 2, 1, 0, 3, 4, 2, 1, 0, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 2, 1, 4, 5],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [2, 1, 0, 3, 4, 2, 1, 0, 3, 4, 2, 1, 0, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 3, 8, 6, 2],tasks = [2, 4, 1, 5, 7, 3, 6, 8, 9, 10]) == [4, 1, 4, 4, 0, 1, 3, 2, 4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 3, 8, 6, 2],tasks = [2, 4, 1, 5, 7, 3, 6, 8, 9, 10]) == [4, 1, 4, 4, 0, 1, 3, 2, 4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 1, 4, 3, 2, 6],tasks = [2, 1, 2, 4, 5, 2, 1, 3, 5, 7, 9, 11, 13, 15]) == [1, 4, 1, 4, 1, 3, 2, 4, 3, 1, 4, 2, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 1, 4, 3, 2, 6],tasks = [2, 1, 2, 4, 5, 2, 1, 3, 5, 7, 9, 11, 13, 15]) == [1, 4, 1, 4, 1, 3, 2, 4, 3, 1, 4, 2, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50],tasks = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50],tasks = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [7, 1, 1, 1, 1, 1],tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [7, 1, 1, 1, 1, 1],tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [23, 45, 12, 67, 89, 34, 56, 78, 90, 10],tasks = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == [9, 2, 0, 5, 1, 6, 3, 7, 4, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [23, 45, 12, 67, 89, 34, 56, 78, 90, 10],tasks = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == [9, 2, 0, 5, 1, 6, 3, 7, 4, 8]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [100, 200, 300, 400, 500],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [100, 200, 300, 400, 500],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 3, 3, 3, 3],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 3, 3, 3, 3],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [100, 200, 300, 400, 500],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [100, 200, 300, 400, 500],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 3, 3, 3, 3],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 3, 3, 3, 3],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 10, 10, 10],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 10, 10, 10],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [100, 200, 300, 400, 500],tasks = [500, 400, 300, 200, 100, 500, 400, 300, 200, 100]) == [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [100, 200, 300, 400, 500],tasks = [500, 400, 300, 200, 100, 500, 400, 300, 200, 100]) == [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 1, 3, 4],tasks = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]) == [1, 0, 2, 3, 1, 0, 2, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 1, 3, 4],tasks = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]) == [1, 0, 2, 3, 1, 0, 2, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 0, 1, 2, 3, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 0, 1, 2, 3, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 5, 5, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 5, 5, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 5, 1, 4, 2],tasks = [15, 10, 5, 20, 25, 30, 5, 10, 15, 20]) == [2, 4, 0, 3, 1, 0, 4, 2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 5, 1, 4, 2],tasks = [15, 10, 5, 20, 25, 30, 5, 10, 15, 20]) == [2, 4, 0, 3, 1, 0, 4, 2, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [7, 8, 9, 10, 11],tasks = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [7, 8, 9, 10, 11],tasks = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 10, 1, 10, 1, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 10, 1, 10, 1, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 10, 15, 20, 25],tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 10, 15, 20, 25],tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50],tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50],tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],tasks = [29, 23, 19, 17, 13, 11, 7, 5, 3, 2]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],tasks = [29, 23, 19, 17, 13, 11, 7, 5, 3, 2]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 2, 1, 4, 5],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [2, 1, 0, 3, 4, 2, 1, 0, 3, 4, 2, 1, 0, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 2, 1, 4, 5],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [2, 1, 0, 3, 4, 2, 1, 0, 3, 4, 2, 1, 0, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 3, 8, 6, 2],tasks = [2, 5, 7, 4, 9, 1, 3, 6, 8, 10]) == [4, 1, 4, 0, 3, 2, 1, 0, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 3, 8, 6, 2],tasks = [2, 5, 7, 4, 9, 1, 3, 6, 8, 10]) == [4, 1, 4, 0, 3, 2, 1, 0, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [7, 11, 13, 17, 19, 23, 29],tasks = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == [0, 1, 0, 2, 1, 3, 4, 0, 5, 6, 2, 1, 3, 4, 0, 5, 6, 2, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [7, 11, 13, 17, 19, 23, 29],tasks = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == [0, 1, 0, 2, 1, 3, 4, 0, 5, 6, 2, 1, 3, 4, 0, 5, 6, 2, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 9, 8, 9, 7, 8, 6, 9, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 9, 8, 9, 7, 8, 6, 9, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 2, 1],tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [2, 1, 0, 2, 1, 0, 2, 1, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 2, 1],tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [2, 1, 0, 2, 1, 0, 2, 1, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 15, 25, 30],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 2, 0, 1, 2, 3, 0, 4, 1, 2, 3, 0, 4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 15, 25, 30],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 2, 0, 1, 2, 3, 0, 4, 1, 2, 3, 0, 4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 3, 8, 6, 2],tasks = [4, 3, 6, 2, 5, 4, 3, 7]) == [4, 1, 0, 3, 4, 1, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 3, 8, 6, 2],tasks = [4, 3, 6, 2, 5, 4, 3, 7]) == [4, 1, 0, 3, 4, 1, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [100, 200, 300, 400, 500],tasks = [500, 400, 300, 200, 100, 500, 400, 300, 200, 100]) == [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [100, 200, 300, 400, 500],tasks = [500, 400, 300, 200, 100, 500, 400, 300, 200, 100]) == [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 5, 8, 3],tasks = [2, 8, 10, 3, 5, 7, 6, 4]) == [3, 1, 3, 2, 0, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 5, 8, 3],tasks = [2, 8, 10, 3, 5, 7, 6, 4]) == [3, 1, 3, 2, 0, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 3, 7, 1, 4],tasks = [10, 5, 3, 8, 2, 1, 9, 6]) == [3, 1, 4, 0, 2, 4, 1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 3, 7, 1, 4],tasks = [10, 5, 3, 8, 2, 1, 9, 6]) == [3, 1, 4, 0, 2, 4, 1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1],tasks = [2, 3, 2, 4, 5, 2, 3, 1, 4, 5]) == [0, 1, 0, 2, 0, 1, 3, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1],tasks = [2, 3, 2, 4, 5, 2, 3, 1, 4, 5]) == [0, 1, 0, 2, 0, 1, 3, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [5, 5, 5, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [5, 5, 5, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [7, 7, 7, 7, 7],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [7, 7, 7, 7, 7],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [15, 10, 20, 5, 25],tasks = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]) == [3, 1, 0, 3, 2, 4, 1, 0, 3, 2, 4, 1, 0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [15, 10, 20, 5, 25],tasks = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]) == [3, 1, 0, 3, 2, 4, 1, 0, 3, 2, 4, 1, 0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5],tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [0, 0, 1, 0, 2, 1, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5],tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [0, 0, 1, 0, 2, 1, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [1, 3, 5, 7, 9, 1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [1, 3, 5, 7, 9, 1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 3, 2],tasks = [3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1]) == [0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 3, 2],tasks = [3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1]) == [0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [10, 1, 10, 1, 10, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 1, 3, 1, 5, 3, 0, 1, 2, 5, 4, 3, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [10, 1, 10, 1, 10, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 1, 3, 1, 5, 3, 0, 1, 2, 5, 4, 3, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [50, 25, 75, 100, 125],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [1, 0, 2, 3, 4, 1, 0, 2, 3, 4, 1, 0, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [50, 25, 75, 100, 125],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [1, 0, 2, 3, 4, 1, 0, 2, 3, 4, 1, 0, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 4, 6, 8, 10],tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 0, 1, 2, 0, 3, 4, 1, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 4, 6, 8, 10],tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 0, 1, 2, 0, 3, 4, 1, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],tasks = [97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],tasks = [97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 23]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [1, 1, 1, 1, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [1, 1, 1, 1, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(servers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],tasks = [8, 9, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 3, 6, 0, 9, 2, 4, 8, 1, 1, 1, 3, 6, 0, 9, 2, 4, 8, 10, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(servers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],tasks = [8, 9, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 3, 6, 0, 9, 2, 4, 8, 1, 1, 1, 3, 6, 0, 9, 2, 4, 8, 10, 7]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(servers = [3, 3, 2],tasks = [1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2]
    assert candidate(servers = [1, 1, 1],tasks = [10, 20, 30, 40, 50]) == [0, 1, 2, 0, 1]
    assert candidate(servers = [5, 1, 4, 3, 2],tasks = [2, 1, 2, 4, 5, 2, 1]) == [1, 4, 1, 4, 1, 3, 2]
    assert candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0]
    assert candidate(servers = [1],tasks = [10]) == [0]
    assert candidate(servers = [10, 20, 30],tasks = [3, 2, 1]) == [0, 1, 2]
    assert candidate(servers = [1, 2, 3],tasks = [3, 2, 1]) == [0, 1, 2]
    assert candidate(servers = [1, 2, 3, 4, 5],tasks = [5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4]
    assert candidate(servers = [10, 20, 30],tasks = [1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0]
    assert candidate(servers = [5, 4, 3, 2, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 4, 3, 4, 2, 3, 1, 4, 0, 2]
    assert candidate(servers = [10, 20, 30],tasks = [1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0]
    assert candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [1, 1, 1],tasks = [10, 10, 10, 10, 10]) == [0, 1, 2, 0, 1]
    assert candidate(servers = [1, 2, 3, 4, 5],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    assert candidate(servers = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7]
    assert candidate(servers = [5, 4, 3, 2, 1],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
    assert candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 5, 1, 3, 0, 5, 1, 4, 2, 3, 0, 3, 0, 5, 1, 3, 0, 4, 2]
    assert candidate(servers = [10, 15, 20, 25, 30],tasks = [5, 10, 15, 20, 25, 30, 35, 40]) == [0, 1, 2, 3, 4, 0, 1, 2]
    assert candidate(servers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    assert candidate(servers = [10, 20, 30, 40, 50],tasks = [5, 15, 25, 35, 45, 55, 65]) == [0, 1, 2, 3, 4, 0, 1]
    assert candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(servers = [1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
    assert candidate(servers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],tasks = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 3, 6, 0, 9, 2, 4, 8, 10, 7, 5]
    assert candidate(servers = [3, 1, 2],tasks = [2, 3, 1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3]) == [1, 2, 1, 1, 2, 1, 2, 0, 1, 2, 1, 1, 2]
    assert candidate(servers = [3, 5, 2, 7, 6],tasks = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 0, 2, 1, 0, 4, 2, 3, 1]
    assert candidate(servers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    assert candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8, 9, 8, 9, 7, 8]
    assert candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(servers = [5, 4, 3, 2, 1],tasks = [2, 3, 4, 5, 1, 2, 3, 4, 5]) == [4, 3, 4, 2, 3, 3, 4, 3, 2]
    assert candidate(servers = [100, 200, 150, 50],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2]
    assert candidate(servers = [100, 100, 100, 100, 100],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [20, 10, 30, 40, 50],tasks = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == [1, 0, 2, 3, 4, 1, 0, 2, 3, 4]
    assert candidate(servers = [2, 3, 1, 4, 5, 2, 3, 1, 4, 5],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [2, 7, 0, 5, 1, 6, 3, 8, 4, 9, 2, 7, 0, 5, 1, 6, 3, 8, 4, 9]
    assert candidate(servers = [15, 25, 5, 20, 10],tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == [2, 4, 0, 3, 1, 2, 4, 0, 3, 1, 2, 4, 0, 3, 1, 2, 4, 0, 3, 1]
    assert candidate(servers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    assert candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [2, 3, 5, 7, 11],tasks = [30, 10, 20, 40, 50, 15, 25, 35, 45, 55]) == [0, 1, 2, 3, 4, 1, 2, 1, 0, 3]
    assert candidate(servers = [7, 5, 3, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [3, 3, 2, 3, 1, 2, 0, 3, 1, 2, 0, 3, 1, 2, 0]
    assert candidate(servers = [5, 3, 8, 6],tasks = [2, 6, 4, 1, 7, 3, 5]) == [1, 0, 1, 3, 3, 2, 1]
    assert candidate(servers = [3, 2, 1, 4, 5],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [2, 1, 0, 3, 4, 2, 1, 0, 3, 4, 2, 1, 0, 3, 4]
    assert candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(servers = [10, 20, 30, 40, 50],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
    assert candidate(servers = [10, 20, 30, 40, 50],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(servers = [5, 3, 8, 6, 2],tasks = [2, 4, 1, 5, 7, 3, 6, 8, 9, 10]) == [4, 1, 4, 4, 0, 1, 3, 2, 4, 1]
    assert candidate(servers = [5, 1, 4, 3, 2, 6],tasks = [2, 1, 2, 4, 5, 2, 1, 3, 5, 7, 9, 11, 13, 15]) == [1, 4, 1, 4, 1, 3, 2, 4, 3, 1, 4, 2, 0, 3]
    assert candidate(servers = [10, 20, 30, 40, 50],tasks = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    assert candidate(servers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(servers = [7, 1, 1, 1, 1, 1],tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
    assert candidate(servers = [23, 45, 12, 67, 89, 34, 56, 78, 90, 10],tasks = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == [9, 2, 0, 5, 1, 6, 3, 7, 4, 8]
    assert candidate(servers = [100, 200, 300, 400, 500],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [10, 20, 30, 40, 50],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [3, 3, 3, 3, 3],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
    assert candidate(servers = [100, 200, 300, 400, 500],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [3, 3, 3, 3, 3],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [10, 10, 10, 10],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0, 2, 1, 3, 0]
    assert candidate(servers = [100, 200, 300, 400, 500],tasks = [500, 400, 300, 200, 100, 500, 400, 300, 200, 100]) == [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]
    assert candidate(servers = [2, 1, 3, 4],tasks = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]) == [1, 0, 2, 3, 1, 0, 2, 3, 1, 0]
    assert candidate(servers = [7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 0, 1, 2, 3, 3, 2]
    assert candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(servers = [5, 5, 5, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [3, 5, 1, 4, 2],tasks = [15, 10, 5, 20, 25, 30, 5, 10, 15, 20]) == [2, 4, 0, 3, 1, 0, 4, 2, 4, 3]
    assert candidate(servers = [7, 8, 9, 10, 11],tasks = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 4]
    assert candidate(servers = [1, 10, 1, 10, 1, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [5, 10, 15, 20, 25],tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    assert candidate(servers = [10, 20, 30, 40, 50],tasks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    assert candidate(servers = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7]
    assert candidate(servers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],tasks = [29, 23, 19, 17, 13, 11, 7, 5, 3, 2]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(servers = [3, 2, 1, 4, 5],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [2, 1, 0, 3, 4, 2, 1, 0, 3, 4, 2, 1, 0, 3, 4]
    assert candidate(servers = [5, 3, 8, 6, 2],tasks = [2, 5, 7, 4, 9, 1, 3, 6, 8, 10]) == [4, 1, 4, 0, 3, 2, 1, 0, 2, 4]
    assert candidate(servers = [7, 11, 13, 17, 19, 23, 29],tasks = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == [0, 1, 0, 2, 1, 3, 4, 0, 5, 6, 2, 1, 3, 4, 0, 5, 6, 2, 1, 3]
    assert candidate(servers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 9, 8, 9, 7, 8, 6, 9, 5, 7]
    assert candidate(servers = [1, 2, 3, 4, 5],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    assert candidate(servers = [3, 2, 1],tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [2, 1, 0, 2, 1, 0, 2, 1, 0, 2]
    assert candidate(servers = [10, 20, 15, 25, 30],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 2, 0, 1, 2, 3, 0, 4, 1, 2, 3, 0, 4, 1]
    assert candidate(servers = [5, 3, 8, 6, 2],tasks = [4, 3, 6, 2, 5, 4, 3, 7]) == [4, 1, 0, 3, 4, 1, 3, 2]
    assert candidate(servers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
    assert candidate(servers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
    assert candidate(servers = [100, 200, 300, 400, 500],tasks = [500, 400, 300, 200, 100, 500, 400, 300, 200, 100]) == [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]
    assert candidate(servers = [10, 5, 8, 3],tasks = [2, 8, 10, 3, 5, 7, 6, 4]) == [3, 1, 3, 2, 0, 2, 1, 0]
    assert candidate(servers = [5, 3, 7, 1, 4],tasks = [10, 5, 3, 8, 2, 1, 9, 6]) == [3, 1, 4, 0, 2, 4, 1, 4]
    assert candidate(servers = [1, 1, 1, 1, 1],tasks = [2, 3, 2, 4, 5, 2, 3, 1, 4, 5]) == [0, 1, 0, 2, 0, 1, 3, 1, 1, 0]
    assert candidate(servers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [5, 5, 5, 5, 5],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [7, 7, 7, 7, 7],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [15, 10, 20, 5, 25],tasks = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]) == [3, 1, 0, 3, 2, 4, 1, 0, 3, 2, 4, 1, 0, 3]
    assert candidate(servers = [1, 2, 3, 4, 5],tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [0, 0, 1, 0, 2, 1, 1, 0, 1, 2]
    assert candidate(servers = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [1, 3, 5, 7, 9, 1, 3, 5, 7, 9]
    assert candidate(servers = [2, 2, 2, 2],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(servers = [1, 3, 2],tasks = [3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1]) == [0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 2, 0]
    assert candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
    assert candidate(servers = [10, 1, 10, 1, 10, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 1, 3, 1, 5, 3, 0, 1, 2, 5, 4, 3, 0, 1, 2]
    assert candidate(servers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 5, 1, 6, 3, 7, 0, 8, 4, 9, 2]
    assert candidate(servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(servers = [50, 25, 75, 100, 125],tasks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == [1, 0, 2, 3, 4, 1, 0, 2, 3, 4, 1, 0, 2, 3, 4]
    assert candidate(servers = [2, 4, 6, 8, 10],tasks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [0, 0, 1, 2, 0, 3, 4, 1, 2, 0]
    assert candidate(servers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],tasks = [97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 23]
    assert candidate(servers = [1, 1, 1, 1, 1],tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 0, 1, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 4, 2]
    assert candidate(servers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],tasks = [8, 9, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 3, 6, 0, 9, 2, 4, 8, 1, 1, 1, 3, 6, 0, 9, 2, 4, 8, 10, 7]


