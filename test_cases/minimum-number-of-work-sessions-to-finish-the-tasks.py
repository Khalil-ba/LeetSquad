def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 2, 4],sessionTime = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 2, 4],sessionTime = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 7, 4, 2, 6],sessionTime = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 7, 4, 2, 6],sessionTime = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],sessionTime = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],sessionTime = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3],sessionTime = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3],sessionTime = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5],sessionTime = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5],sessionTime = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 9, 9, 9],sessionTime = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 9, 9, 9],sessionTime = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 3, 4, 6],sessionTime = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 3, 4, 6],sessionTime = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [14],sessionTime = 14) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [14],sessionTime = 14) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 7, 7, 7],sessionTime = 14) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 7, 7, 7],sessionTime = 14) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10],sessionTime = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10],sessionTime = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10],sessionTime = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10],sessionTime = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1],sessionTime = 14) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1],sessionTime = 14) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 4, 5, 1],sessionTime = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 4, 5, 1],sessionTime = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5],sessionTime = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5],sessionTime = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 2, 7, 2, 7],sessionTime = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 2, 7, 2, 7],sessionTime = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8],sessionTime = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8],sessionTime = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4],sessionTime = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4],sessionTime = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 14) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 14) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 1: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 1, 3, 1, 1],sessionTime = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 1, 3, 1, 1],sessionTime = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 2, 4, 3, 5],sessionTime = 12) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 2, 4, 3, 5],sessionTime = 12) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7],sessionTime = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7],sessionTime = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1],sessionTime = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1],sessionTime = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 1, 3, 5, 7, 9, 11, 13],sessionTime = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 1, 3, 5, 7, 9, 11, 13],sessionTime = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7],sessionTime = 13) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7],sessionTime = 13) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5],sessionTime = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5],sessionTime = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6],sessionTime = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6],sessionTime = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1],sessionTime = 11) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1],sessionTime = 11) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 15) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 15) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],sessionTime = 14) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],sessionTime = 14) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2],sessionTime = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2],sessionTime = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 14],sessionTime = 14) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 14],sessionTime = 14) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 28) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 28) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 6, 7, 9, 10, 1, 2, 4, 5, 8, 2, 3, 4, 6],sessionTime = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 6, 7, 9, 10, 1, 2, 4, 5, 8, 2, 3, 4, 6],sessionTime = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 8, 7, 8, 7, 8, 7, 8],sessionTime = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 8, 7, 8, 7, 8, 7, 8],sessionTime = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7],sessionTime = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7],sessionTime = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 5, 7, 11, 13],sessionTime = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 5, 7, 11, 13],sessionTime = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],sessionTime = 14) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],sessionTime = 14) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6],sessionTime = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6],sessionTime = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],sessionTime = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],sessionTime = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7],sessionTime = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7],sessionTime = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1],sessionTime = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1],sessionTime = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 14],sessionTime = 14) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 14],sessionTime = 14) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 1, 2, 3, 4],sessionTime = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 1, 2, 3, 4],sessionTime = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 1, 4, 8, 3, 2, 5, 6, 7, 10, 1, 2, 3, 4],sessionTime = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 1, 4, 8, 3, 2, 5, 6, 7, 10, 1, 2, 3, 4],sessionTime = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 1, 2],sessionTime = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 1, 2],sessionTime = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 3, 4, 5, 6, 2, 8, 9, 10, 1, 2, 3, 4, 5],sessionTime = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 3, 4, 5, 6, 2, 8, 9, 10, 1, 2, 3, 4, 5],sessionTime = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4],sessionTime = 14) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4],sessionTime = 14) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5],sessionTime = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5],sessionTime = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],sessionTime = 14) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],sessionTime = 14) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],sessionTime = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],sessionTime = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],sessionTime = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],sessionTime = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],sessionTime = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],sessionTime = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],sessionTime = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],sessionTime = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],sessionTime = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],sessionTime = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2],sessionTime = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2],sessionTime = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],sessionTime = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],sessionTime = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],sessionTime = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],sessionTime = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4],sessionTime = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4],sessionTime = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4],sessionTime = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4],sessionTime = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],sessionTime = 16) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],sessionTime = 16) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1],sessionTime = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1],sessionTime = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],sessionTime = 13) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],sessionTime = 13) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13],sessionTime = 14) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13],sessionTime = 14) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],sessionTime = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],sessionTime = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43],sessionTime = 15) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43],sessionTime = 15) == inf: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],sessionTime = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],sessionTime = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 6, 7, 8, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14],sessionTime = 14) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 6, 7, 8, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14],sessionTime = 14) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],sessionTime = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],sessionTime = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],sessionTime = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],sessionTime = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [9, 6, 3, 2, 1, 9, 6, 3, 2, 1, 9, 6, 3, 2],sessionTime = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [9, 6, 3, 2, 1, 9, 6, 3, 2, 1, 9, 6, 3, 2],sessionTime = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],sessionTime = 13) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],sessionTime = 13) == 3: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 10) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 10) == inf: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2],sessionTime = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2],sessionTime = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 14],sessionTime = 10) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 14],sessionTime = 10) == inf: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4],sessionTime = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4],sessionTime = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7],sessionTime = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7],sessionTime = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 2, 4, 6, 5, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 14) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 2, 4, 6, 5, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 14) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 2: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 13) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 13) == inf: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],sessionTime = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],sessionTime = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1],sessionTime = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1],sessionTime = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],sessionTime = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],sessionTime = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],sessionTime = 12) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],sessionTime = 12) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],sessionTime = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],sessionTime = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],sessionTime = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],sessionTime = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],sessionTime = 8) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],sessionTime = 8) == 14: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [3, 2, 3, 2, 3, 2, 3, 2],sessionTime = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [3, 2, 3, 2, 3, 2, 3, 2],sessionTime = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],sessionTime = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],sessionTime = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43],sessionTime = 20) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43],sessionTime = 20) == inf: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3, 1],sessionTime = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3, 1],sessionTime = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],sessionTime = 14) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],sessionTime = 14) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 10) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 10) == inf: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2],sessionTime = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2],sessionTime = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5],sessionTime = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5],sessionTime = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 1, 3, 5, 7, 9, 11],sessionTime = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 1, 3, 5, 7, 9, 11],sessionTime = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [7, 7, 7, 7, 6, 6, 6, 5, 5, 4, 4, 3, 3, 2],sessionTime = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [7, 7, 7, 7, 6, 6, 6, 5, 5, 4, 4, 3, 3, 2],sessionTime = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],sessionTime = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],sessionTime = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7],sessionTime = 14) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7],sessionTime = 14) == 5: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],sessionTime = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],sessionTime = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 7) == inf
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 7) == inf: {e}')
    
    total += 1
    try:
        result = candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 20) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tasks = [1, 3, 2, 4],sessionTime = 5) == 2
    assert candidate(tasks = [5, 7, 4, 2, 6],sessionTime = 10) == 3
    assert candidate(tasks = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],sessionTime = 12) == 5
    assert candidate(tasks = [1, 2, 3],sessionTime = 3) == 2
    assert candidate(tasks = [5, 5, 5, 5],sessionTime = 5) == 4
    assert candidate(tasks = [9, 9, 9, 9],sessionTime = 9) == 4
    assert candidate(tasks = [2, 3, 3, 4, 6],sessionTime = 6) == 3
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 2) == 7
    assert candidate(tasks = [14],sessionTime = 14) == 1
    assert candidate(tasks = [7, 7, 7, 7],sessionTime = 14) == 2
    assert candidate(tasks = [10, 10, 10, 10],sessionTime = 10) == 4
    assert candidate(tasks = [10, 10, 10],sessionTime = 10) == 3
    assert candidate(tasks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1],sessionTime = 14) == 8
    assert candidate(tasks = [14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 2
    assert candidate(tasks = [2, 3, 4, 5, 1],sessionTime = 6) == 3
    assert candidate(tasks = [1, 2, 3, 4, 5],sessionTime = 15) == 1
    assert candidate(tasks = [7, 2, 7, 2, 7],sessionTime = 12) == 3
    assert candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8],sessionTime = 15) == 8
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 15) == 7
    assert candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 10) == 14
    assert candidate(tasks = [1, 2, 3, 4],sessionTime = 10) == 1
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 15) == 5
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 14) == 8
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 1
    assert candidate(tasks = [3, 1, 3, 1, 1],sessionTime = 8) == 2
    assert candidate(tasks = [7, 2, 4, 3, 5],sessionTime = 12) == 2
    assert candidate(tasks = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7],sessionTime = 10) == 6
    assert candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1],sessionTime = 10) == 6
    assert candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 1, 3, 5, 7, 9, 11, 13],sessionTime = 15) == 7
    assert candidate(tasks = [7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7],sessionTime = 13) == 5
    assert candidate(tasks = [2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5],sessionTime = 12) == 5
    assert candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6],sessionTime = 12) == 5
    assert candidate(tasks = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1],sessionTime = 11) == 7
    assert candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 15) == 14
    assert candidate(tasks = [10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 15) == 4
    assert candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],sessionTime = 14) == 7
    assert candidate(tasks = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2],sessionTime = 8) == 5
    assert candidate(tasks = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 14],sessionTime = 14) == 5
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 28) == 4
    assert candidate(tasks = [3, 6, 7, 9, 10, 1, 2, 4, 5, 8, 2, 3, 4, 6],sessionTime = 10) == 7
    assert candidate(tasks = [7, 8, 7, 8, 7, 8, 7, 8],sessionTime = 15) == 4
    assert candidate(tasks = [7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7],sessionTime = 12) == 5
    assert candidate(tasks = [2, 3, 5, 7, 11, 13],sessionTime = 15) == 3
    assert candidate(tasks = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],sessionTime = 14) == 6
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 20) == 6
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6],sessionTime = 10) == 6
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 20) == 6
    assert candidate(tasks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],sessionTime = 10) == 4
    assert candidate(tasks = [8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 15) == 4
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 15) == 5
    assert candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7],sessionTime = 15) == 6
    assert candidate(tasks = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1],sessionTime = 7) == 5
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 14],sessionTime = 14) == 2
    assert candidate(tasks = [10, 10, 10, 10, 1, 2, 3, 4],sessionTime = 15) == 4
    assert candidate(tasks = [9, 1, 4, 8, 3, 2, 5, 6, 7, 10, 1, 2, 3, 4],sessionTime = 10) == 7
    assert candidate(tasks = [7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 4
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 5) == 14
    assert candidate(tasks = [10, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 1, 2],sessionTime = 10) == 8
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 10) == 4
    assert candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 30) == 5
    assert candidate(tasks = [7, 3, 4, 5, 6, 2, 8, 9, 10, 1, 2, 3, 4, 5],sessionTime = 10) == 7
    assert candidate(tasks = [10, 10, 10, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4],sessionTime = 14) == 4
    assert candidate(tasks = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5],sessionTime = 10) == 5
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],sessionTime = 14) == 4
    assert candidate(tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],sessionTime = 9) == 5
    assert candidate(tasks = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],sessionTime = 12) == 6
    assert candidate(tasks = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],sessionTime = 9) == 5
    assert candidate(tasks = [2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],sessionTime = 12) == 6
    assert candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],sessionTime = 10) == 5
    assert candidate(tasks = [1, 2, 3, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2],sessionTime = 8) == 5
    assert candidate(tasks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],sessionTime = 10) == 14
    assert candidate(tasks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],sessionTime = 9) == 5
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 10) == 7
    assert candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4],sessionTime = 20) == 4
    assert candidate(tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4],sessionTime = 10) == 4
    assert candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],sessionTime = 16) == 7
    assert candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1],sessionTime = 10) == 14
    assert candidate(tasks = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],sessionTime = 13) == 5
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 10) == 7
    assert candidate(tasks = [2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13],sessionTime = 14) == 8
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],sessionTime = 6) == 4
    assert candidate(tasks = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43],sessionTime = 15) == inf
    assert candidate(tasks = [10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 10) == 5
    assert candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],sessionTime = 4) == 7
    assert candidate(tasks = [9, 6, 7, 8, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14],sessionTime = 14) == 8
    assert candidate(tasks = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],sessionTime = 6) == 6
    assert candidate(tasks = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],sessionTime = 10) == 6
    assert candidate(tasks = [9, 6, 3, 2, 1, 9, 6, 3, 2, 1, 9, 6, 3, 2],sessionTime = 10) == 7
    assert candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],sessionTime = 13) == 3
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 10) == inf
    assert candidate(tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2],sessionTime = 10) == 5
    assert candidate(tasks = [10, 10, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sessionTime = 15) == 6
    assert candidate(tasks = [10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 10) == 5
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 14],sessionTime = 10) == inf
    assert candidate(tasks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4],sessionTime = 8) == 4
    assert candidate(tasks = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7],sessionTime = 12) == 6
    assert candidate(tasks = [1, 3, 2, 4, 6, 5, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 14) == 8
    assert candidate(tasks = [14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 14) == 2
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 13) == inf
    assert candidate(tasks = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],sessionTime = 4) == 6
    assert candidate(tasks = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1],sessionTime = 9) == 4
    assert candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],sessionTime = 15) == 5
    assert candidate(tasks = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],sessionTime = 12) == 7
    assert candidate(tasks = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],sessionTime = 6) == 7
    assert candidate(tasks = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],sessionTime = 8) == 4
    assert candidate(tasks = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1],sessionTime = 8) == 14
    assert candidate(tasks = [3, 2, 3, 2, 3, 2, 3, 2],sessionTime = 5) == 4
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],sessionTime = 10) == 6
    assert candidate(tasks = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43],sessionTime = 20) == inf
    assert candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 11, 9, 7, 5, 3, 1],sessionTime = 15) == 6
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 2) == 8
    assert candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],sessionTime = 14) == 5
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 10) == inf
    assert candidate(tasks = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2],sessionTime = 5) == 6
    assert candidate(tasks = [2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5],sessionTime = 10) == 5
    assert candidate(tasks = [1, 3, 5, 7, 9, 11, 13, 15, 1, 3, 5, 7, 9, 11],sessionTime = 15) == 7
    assert candidate(tasks = [7, 7, 7, 7, 6, 6, 6, 5, 5, 4, 4, 3, 3, 2],sessionTime = 15) == 5
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],sessionTime = 8) == 7
    assert candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7],sessionTime = 14) == 5
    assert candidate(tasks = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],sessionTime = 12) == 6
    assert candidate(tasks = [10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1],sessionTime = 20) == 4
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],sessionTime = 7) == inf
    assert candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],sessionTime = 20) == 7


