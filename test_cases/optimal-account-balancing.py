def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3], [4, 0, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3], [4, 0, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 0, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 0, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 2], [2, 3, 4], [3, 4, 4], [4, 5, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 2], [2, 3, 4], [3, 4, 4], [4, 5, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 0, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 0, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 3], [2, 3, 4], [3, 1, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 3], [2, 3, 4], [3, 1, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [2, 0, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [2, 0, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 1, 10]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 1, 10]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40], [5, 1, 100]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40], [5, 1, 100]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 10], [2, 3, 10], [3, 1, 5], [1, 3, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 10], [2, 3, 10], [3, 1, 5], [1, 3, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 1], [3, 2, 2], [2, 1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 1], [3, 2, 2], [2, 1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 0, 3], [3, 4, 4], [4, 3, 5], [5, 4, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 0, 3], [3, 4, 4], [4, 3, 5], [5, 4, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 10], [2, 3, 5], [3, 1, 5], [1, 4, 10], [4, 3, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 10], [2, 3, 5], [3, 1, 5], [1, 4, 10], [4, 3, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[2, 0, 5], [3, 4, 4], [2, 3, 3], [4, 0, 1], [0, 1, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[2, 0, 5], [3, 4, 4], [2, 3, 3], [4, 0, 1], [0, 1, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 20], [1, 2, 10], [2, 0, 5], [0, 2, 15]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 20], [1, 2, 10], [2, 0, 5], [0, 2, 15]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 3], [1, 2, 2], [2, 0, 1], [0, 3, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 3], [1, 2, 2], [2, 0, 1], [0, 3, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 0, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 0, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 3], [3, 4, 5], [4, 1, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 3], [3, 4, 5], [4, 1, 9]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 3], [2, 3, 4], [3, 1, 7]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 3], [2, 3, 4], [3, 1, 7]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 0, 1], [0, 2, 2], [2, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 0, 1], [0, 2, 2], [2, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 1], [2, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 1], [2, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 2], [1, 3, 3], [2, 4, 2], [3, 4, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 2], [1, 3, 3], [2, 4, 2], [3, 4, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 1], [2, 0, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 1], [2, 0, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [2, 3, 1], [4, 5, 1], [6, 7, 1], [8, 9, 1], [1, 10, 1], [10, 11, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [2, 3, 1], [4, 5, 1], [6, 7, 1], [8, 9, 1], [1, 10, 1], [10, 11, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[5, 6, 20], [6, 7, 15], [7, 8, 10], [8, 9, 5], [9, 10, 15], [10, 5, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[5, 6, 20], [6, 7, 15], [7, 8, 10], [8, 9, 5], [9, 10, 15], [10, 5, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 0, 2], [0, 4, 4], [4, 5, 3], [5, 0, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 0, 2], [0, 4, 4], [4, 5, 3], [5, 0, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 2, 10], [1, 3, 20], [2, 3, 10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 2, 10], [1, 3, 20], [2, 3, 10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 0, 30], [0, 3, 40], [3, 4, 50], [4, 5, 60], [5, 0, 180], [1, 3, 10], [3, 1, 10], [2, 4, 20], [4, 2, 20]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 0, 30], [0, 3, 40], [3, 4, 50], [4, 5, 60], [5, 0, 180], [1, 3, 10], [3, 1, 10], [2, 4, 20], [4, 2, 20]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 10], [3, 4, 15], [4, 0, 5], [1, 4, 25]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 10], [3, 4, 15], [4, 0, 5], [1, 4, 25]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 5], [0, 2, 10], [1, 2, 10], [1, 3, 15], [2, 3, 5], [0, 3, 15], [1, 4, 20], [2, 4, 25], [3, 4, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 5], [0, 2, 10], [1, 2, 10], [1, 3, 15], [2, 3, 5], [0, 3, 15], [1, 4, 20], [2, 4, 25], [3, 4, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[5, 6, 50], [6, 7, 25], [7, 8, 25], [8, 9, 10], [9, 10, 5], [10, 5, 20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[5, 6, 50], [6, 7, 25], [7, 8, 25], [8, 9, 10], [9, 10, 5], [10, 5, 20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 7, 10], [7, 0, 10], [0, 2, 5], [1, 3, 5], [2, 4, 5], [3, 5, 5], [4, 6, 5], [5, 7, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 7, 10], [7, 0, 10], [0, 2, 5], [1, 3, 5], [2, 4, 5], [3, 5, 5], [4, 6, 5], [5, 7, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 15], [2, 3, 25], [3, 4, 35], [4, 5, 45], [5, 6, 55], [6, 7, 65], [7, 8, 75], [8, 9, 85], [9, 10, 95], [10, 1, 105]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 15], [2, 3, 25], [3, 4, 35], [4, 5, 45], [5, 6, 55], [6, 7, 65], [7, 8, 75], [8, 9, 85], [9, 10, 95], [10, 1, 105]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 100], [1, 2, 200], [2, 0, 150], [0, 3, 50], [3, 4, 100], [4, 2, 50]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 100], [1, 2, 200], [2, 0, 150], [0, 3, 50], [3, 4, 100], [4, 2, 50]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 12], [2, 3, 24], [3, 4, 36], [4, 5, 48], [5, 6, 60], [6, 1, 72]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 12], [2, 3, 24], [3, 4, 36], [4, 5, 48], [5, 6, 60], [6, 1, 72]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 50], [2, 3, 30], [3, 4, 20], [4, 5, 10], [5, 1, 40], [1, 3, 10], [3, 2, 5], [2, 4, 20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 50], [2, 3, 30], [3, 4, 20], [4, 5, 10], [5, 1, 40], [1, 3, 10], [3, 2, 5], [2, 4, 20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 30], [2, 3, 20], [3, 4, 10], [4, 5, 5], [5, 6, 3], [6, 7, 2], [7, 8, 1], [8, 9, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 30], [2, 3, 20], [3, 4, 10], [4, 5, 5], [5, 6, 3], [6, 7, 2], [7, 8, 1], [8, 9, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 0, 40], [2, 0, 50], [3, 0, 60], [1, 2, 5], [2, 1, 5], [2, 3, 5], [3, 2, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 0, 40], [2, 0, 50], [3, 0, 60], [1, 2, 5], [2, 1, 5], [2, 3, 5], [3, 2, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 100], [1, 2, 50], [2, 3, 25], [3, 4, 12], [4, 5, 6], [5, 0, 3], [0, 3, 7], [3, 1, 18]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 100], [1, 2, 50], [2, 3, 25], [3, 4, 12], [4, 5, 6], [5, 0, 3], [0, 3, 7], [3, 1, 18]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[5, 6, 5], [6, 7, 3], [7, 8, 8], [8, 9, 6], [9, 5, 4], [5, 7, 2], [7, 6, 1], [6, 8, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[5, 6, 5], [6, 7, 3], [7, 8, 8], [8, 9, 6], [9, 5, 4], [5, 7, 2], [7, 6, 1], [6, 8, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 7, 10], [7, 1, 10], [1, 8, 10], [8, 9, 10], [9, 10, 10], [10, 1, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 7, 10], [7, 1, 10], [1, 8, 10], [8, 9, 10], [9, 10, 10], [10, 1, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 5, 5], [5, 1, 5], [1, 3, 5], [3, 2, 5], [2, 4, 5], [4, 3, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 5, 5], [5, 1, 5], [1, 3, 5], [3, 2, 5], [2, 4, 5], [4, 3, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 0, 1500]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 0, 1500]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 20], [1, 2, 30], [2, 3, 10], [3, 0, 40], [0, 2, 15], [2, 1, 5], [1, 3, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 20], [1, 2, 30], [2, 3, 10], [3, 0, 40], [0, 2, 15], [2, 1, 5], [1, 3, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 0, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 0, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 2, 5], [2, 3, 15], [3, 1, 25]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 2, 5], [2, 3, 15], [3, 1, 25]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 0, 100]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 0, 100]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 5], [2, 0, 3], [0, 3, 8], [3, 2, 4], [2, 1, 2], [1, 0, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 5], [2, 0, 3], [0, 3, 8], [3, 2, 4], [2, 1, 2], [1, 0, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 5, 6], [5, 8, 12], [6, 9, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 5, 6], [5, 8, 12], [6, 9, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [0, 4, 40], [1, 2, 15], [1, 3, 25], [1, 4, 35], [2, 3, 5], [2, 4, 15], [3, 4, 25]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [0, 4, 40], [1, 2, 15], [1, 3, 25], [1, 4, 35], [2, 3, 5], [2, 4, 15], [3, 4, 25]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 0, 10], [0, 2, 10], [2, 1, 10], [1, 3, 10], [3, 2, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 0, 10], [0, 2, 10], [2, 1, 10], [1, 3, 10], [3, 2, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 15], [2, 3, 5], [3, 0, 10], [0, 2, 10], [2, 1, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 15], [2, 3, 5], [3, 0, 10], [0, 2, 10], [2, 1, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 15], [1, 2, 10], [2, 3, 5], [3, 0, 20], [1, 3, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 15], [1, 2, 10], [2, 3, 5], [3, 0, 20], [1, 3, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 0, 15], [1, 3, 5], [2, 4, 10], [3, 0, 10], [4, 1, 20], [0, 5, 10], [1, 4, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 0, 15], [1, 3, 5], [2, 4, 10], [3, 0, 10], [4, 1, 20], [0, 5, 10], [1, 4, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 15], [2, 3, 10], [3, 4, 5], [4, 1, 20], [1, 3, 5], [3, 2, 10], [2, 4, 5], [4, 3, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 15], [2, 3, 10], [3, 4, 5], [4, 1, 20], [1, 3, 5], [3, 2, 10], [2, 4, 5], [4, 3, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[10, 11, 1], [11, 12, 2], [12, 13, 3], [13, 14, 4], [14, 15, 5], [15, 16, 6], [16, 17, 7], [17, 18, 8]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[10, 11, 1], [11, 12, 2], [12, 13, 3], [13, 14, 4], [14, 15, 5], [15, 16, 6], [16, 17, 7], [17, 18, 8]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 100], [1, 2, 50], [2, 3, 25], [3, 4, 12], [4, 0, 83], [0, 2, 17], [2, 1, 32], [1, 3, 45], [3, 2, 13], [2, 4, 6], [4, 1, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 100], [1, 2, 50], [2, 3, 25], [3, 4, 12], [4, 0, 83], [0, 2, 17], [2, 1, 32], [1, 3, 45], [3, 2, 13], [2, 4, 6], [4, 1, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[10, 11, 10], [11, 12, 5], [12, 13, 15], [13, 14, 20], [14, 10, 25], [10, 13, 10], [11, 14, 15], [12, 10, 5], [13, 11, 20], [14, 12, 25]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[10, 11, 10], [11, 12, 5], [12, 13, 15], [13, 14, 20], [14, 10, 25], [10, 13, 10], [11, 14, 15], [12, 10, 5], [13, 11, 20], [14, 12, 25]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 15], [1, 2, 20], [2, 0, 5], [3, 4, 10], [4, 3, 5], [0, 3, 10]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 15], [1, 2, 20], [2, 0, 5], [3, 4, 10], [4, 3, 5], [0, 3, 10]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[5, 0, 10], [0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 0, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[5, 0, 10], [0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 0, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 50], [1, 2, 100], [2, 3, 150], [3, 4, 200], [4, 5, 250], [5, 6, 300], [6, 7, 350], [7, 0, 400]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 50], [1, 2, 100], [2, 3, 150], [3, 4, 200], [4, 5, 250], [5, 6, 300], [6, 7, 350], [7, 0, 400]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 100], [2, 3, 200], [3, 4, 300], [4, 5, 400], [5, 1, 100], [1, 3, 100], [3, 5, 100], [5, 2, 100]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 100], [2, 3, 200], [3, 4, 300], [4, 5, 400], [5, 1, 100], [1, 3, 100], [3, 5, 100], [5, 2, 100]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 28]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 28]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 25], [2, 3, 15], [3, 4, 5], [4, 5, 10], [5, 6, 5], [6, 1, 20], [1, 3, 15], [3, 5, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 25], [2, 3, 15], [3, 4, 5], [4, 5, 10], [5, 6, 5], [6, 1, 20], [1, 3, 15], [3, 5, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 7]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 7]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 20], [1, 2, 10], [2, 3, 5], [3, 4, 5], [4, 0, 15], [0, 5, 10], [5, 1, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 20], [1, 2, 10], [2, 3, 5], [3, 4, 5], [4, 0, 15], [0, 5, 10], [5, 1, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 25], [2, 3, 15], [3, 4, 10], [4, 5, 5], [5, 6, 30], [6, 1, 20]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 25], [2, 3, 15], [3, 4, 10], [4, 5, 5], [5, 6, 30], [6, 1, 20]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 1, 2], [1, 3, 1], [2, 4, 2], [3, 5, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 1, 2], [1, 3, 1], [2, 4, 2], [3, 5, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 30], [1, 2, 20], [2, 3, 10], [3, 4, 40], [4, 5, 50], [5, 0, 60], [1, 3, 5], [2, 4, 15], [3, 5, 25]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 30], [1, 2, 20], [2, 3, 10], [3, 4, 40], [4, 5, 50], [5, 0, 60], [1, 3, 5], [2, 4, 15], [3, 5, 25]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 0, 40], [0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 0, 40]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 0, 40], [0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 0, 40]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 0, 90]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 0, 90]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 0, 150]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 0, 150]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 20], [2, 3, 15], [3, 4, 25], [4, 1, 20], [1, 3, 10], [3, 2, 5], [2, 4, 20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 20], [2, 3, 15], [3, 4, 25], [4, 1, 20], [1, 3, 10], [3, 2, 5], [2, 4, 20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 6], [1, 0, 7]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 6], [1, 0, 7]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[10, 9, 50], [9, 8, 40], [8, 7, 30], [7, 6, 20], [6, 5, 10], [5, 4, 5], [4, 3, 20], [3, 2, 10], [2, 1, 5], [1, 0, 15]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[10, 9, 50], [9, 8, 40], [8, 7, 30], [7, 6, 20], [6, 5, 10], [5, 4, 5], [4, 3, 20], [3, 2, 10], [2, 1, 5], [1, 0, 15]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[2, 0, 50], [3, 4, 40], [2, 3, 30], [4, 0, 10], [0, 1, 20], [1, 2, 30], [3, 0, 40], [4, 2, 10], [1, 3, 20], [2, 4, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[2, 0, 50], [3, 4, 40], [2, 3, 30], [4, 0, 10], [0, 1, 20], [1, 2, 30], [3, 0, 40], [4, 2, 10], [1, 3, 20], [2, 4, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 50], [2, 3, 30], [3, 4, 20], [4, 5, 10], [5, 1, 15], [1, 3, 10]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 50], [2, 3, 30], [3, 4, 20], [4, 5, 10], [5, 1, 15], [1, 3, 10]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 1, 6], [1, 2, 7], [2, 3, 8], [3, 4, 9], [4, 0, 10]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 1, 6], [1, 2, 7], [2, 3, 8], [3, 4, 9], [4, 0, 10]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[5, 4, 10], [4, 3, 20], [3, 2, 30], [2, 1, 40], [1, 0, 100], [0, 5, 50]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[5, 4, 10], [4, 3, 20], [3, 2, 30], [2, 1, 40], [1, 0, 100], [0, 5, 50]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 10, 100], [10, 1, 110], [1, 11, 120], [11, 2, 130], [2, 12, 140], [12, 3, 150]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 10, 100], [10, 1, 110], [1, 11, 120], [11, 2, 130], [2, 12, 140], [12, 3, 150]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[1, 2, 50], [2, 3, 30], [3, 4, 20], [4, 5, 10], [5, 6, 5], [6, 7, 5], [7, 8, 10], [8, 9, 15], [9, 10, 20], [10, 1, 25]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[1, 2, 50], [2, 3, 30], [3, 4, 20], [4, 5, 10], [5, 6, 5], [6, 7, 5], [7, 8, 10], [8, 9, 15], [9, 10, 20], [10, 1, 25]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 0, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 0, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 20], [1, 2, 30], [2, 3, 40], [3, 4, 50], [4, 5, 60], [5, 6, 70], [6, 7, 80], [7, 0, 350]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 20], [1, 2, 30], [2, 3, 40], [3, 4, 50], [4, 5, 60], [5, 6, 70], [6, 7, 80], [7, 0, 350]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 20], [1, 2, 30], [2, 3, 40], [3, 0, 10], [0, 2, 25], [2, 1, 5], [1, 3, 15]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 20], [1, 2, 30], [2, 3, 40], [3, 0, 10], [0, 2, 25], [2, 1, 5], [1, 3, 15]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 0, 60]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 0, 60]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 6, 600], [6, 7, 700], [7, 8, 800], [8, 9, 900], [9, 0, 1000]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 6, 600], [6, 7, 700], [7, 8, 800], [8, 9, 900], [9, 0, 1000]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 0, 3], [0, 3, 4], [3, 1, 5], [1, 4, 6], [4, 2, 7], [2, 5, 8], [5, 3, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 0, 3], [0, 3, 4], [3, 1, 5], [1, 4, 6], [4, 2, 7], [2, 5, 8], [5, 3, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 5], [2, 0, 5], [0, 3, 10], [3, 1, 10], [1, 4, 5], [4, 2, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 5], [2, 0, 5], [0, 3, 10], [3, 1, 10], [1, 4, 5], [4, 2, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 0, 80]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 0, 80]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 20], [1, 2, 15], [2, 3, 10], [3, 0, 5], [1, 3, 10], [2, 0, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 20], [1, 2, 15], [2, 3, 10], [3, 0, 5], [1, 3, 10], [2, 0, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 0, 5], [1, 3, 5], [3, 5, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 0, 5], [1, 3, 5], [3, 5, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 50], [1, 2, 20], [2, 0, 10], [0, 3, 30], [3, 1, 10], [1, 0, 10], [0, 4, 20], [4, 3, 10], [3, 2, 5], [2, 1, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 50], [1, 2, 20], [2, 0, 10], [0, 3, 30], [3, 1, 10], [1, 0, 10], [0, 4, 20], [4, 3, 10], [3, 2, 5], [2, 1, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 50], [1, 2, 100], [2, 3, 150], [3, 4, 200], [4, 5, 250], [5, 6, 300], [6, 7, 350], [7, 8, 400], [8, 0, 450]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 50], [1, 2, 100], [2, 3, 150], [3, 4, 200], [4, 5, 250], [5, 6, 300], [6, 7, 350], [7, 8, 400], [8, 0, 450]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 15], [1, 2, 25], [2, 3, 35], [3, 4, 45], [4, 5, 55], [5, 6, 65], [6, 0, 240]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 15], [1, 2, 25], [2, 3, 35], [3, 4, 45], [4, 5, 55], [5, 6, 65], [6, 0, 240]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(transactions = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40], [8, 9, 45], [9, 0, 50]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40], [8, 9, 45], [9, 0, 50]]) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(transactions = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3], [4, 0, 3]]) == 0
    assert candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 0, 1]]) == 1
    assert candidate(transactions = [[1, 2, 2], [2, 3, 4], [3, 4, 4], [4, 5, 5]]) == 3
    assert candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 0, 10]]) == 0
    assert candidate(transactions = [[1, 2, 3], [2, 3, 4], [3, 1, 5]]) == 2
    assert candidate(transactions = [[0, 1, 10], [2, 0, 5]]) == 2
    assert candidate(transactions = [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [5, 1, 10]]) == 4
    assert candidate(transactions = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40], [5, 1, 100]]) == 4
    assert candidate(transactions = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 1, 1]]) == 0
    assert candidate(transactions = [[1, 2, 10], [2, 3, 10], [3, 1, 5], [1, 3, 5]]) == 1
    assert candidate(transactions = [[1, 2, 1], [3, 2, 2], [2, 1, 1]]) == 1
    assert candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 0, 3], [3, 4, 4], [4, 3, 5], [5, 4, 6]]) == 4
    assert candidate(transactions = [[1, 2, 10], [2, 3, 5], [3, 1, 5], [1, 4, 10], [4, 3, 10]]) == 2
    assert candidate(transactions = [[2, 0, 5], [3, 4, 4], [2, 3, 3], [4, 0, 1], [0, 1, 2]]) == 4
    assert candidate(transactions = [[0, 1, 20], [1, 2, 10], [2, 0, 5], [0, 2, 15]]) == 2
    assert candidate(transactions = [[0, 1, 3], [1, 2, 2], [2, 0, 1], [0, 3, 3]]) == 3
    assert candidate(transactions = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 0, 1]]) == 3
    assert candidate(transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]) == 1
    assert candidate(transactions = [[1, 2, 3], [3, 4, 5], [4, 1, 9]]) == 3
    assert candidate(transactions = [[1, 2, 3], [2, 3, 4], [3, 1, 7]]) == 2
    assert candidate(transactions = [[0, 1, 1], [1, 0, 1], [0, 2, 2], [2, 0, 2]]) == 0
    assert candidate(transactions = [[0, 1, 1], [1, 2, 1], [2, 0, 2]]) == 1
    assert candidate(transactions = [[1, 2, 2], [1, 3, 3], [2, 4, 2], [3, 4, 4]]) == 2
    assert candidate(transactions = [[0, 1, 1], [1, 2, 1], [2, 0, 1]]) == 0
    assert candidate(transactions = [[0, 1, 1], [2, 3, 1], [4, 5, 1], [6, 7, 1], [8, 9, 1], [1, 10, 1], [10, 11, 1]]) == 5
    assert candidate(transactions = [[5, 6, 20], [6, 7, 15], [7, 8, 10], [8, 9, 5], [9, 10, 15], [10, 5, 5]]) == 4
    assert candidate(transactions = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 0, 2], [0, 4, 4], [4, 5, 3], [5, 0, 3]]) == 3
    assert candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 2, 10], [1, 3, 20], [2, 3, 10]]) == 2
    assert candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 0, 30], [0, 3, 40], [3, 4, 50], [4, 5, 60], [5, 0, 180], [1, 3, 10], [3, 1, 10], [2, 4, 20], [4, 2, 20]]) == 5
    assert candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 10], [3, 4, 15], [4, 0, 5], [1, 4, 25]]) == 3
    assert candidate(transactions = [[0, 1, 5], [0, 2, 10], [1, 2, 10], [1, 3, 15], [2, 3, 5], [0, 3, 15], [1, 4, 20], [2, 4, 25], [3, 4, 5]]) == 3
    assert candidate(transactions = [[5, 6, 50], [6, 7, 25], [7, 8, 25], [8, 9, 10], [9, 10, 5], [10, 5, 20]]) == 3
    assert candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 7, 10], [7, 0, 10], [0, 2, 5], [1, 3, 5], [2, 4, 5], [3, 5, 5], [4, 6, 5], [5, 7, 5]]) == 2
    assert candidate(transactions = [[1, 2, 15], [2, 3, 25], [3, 4, 35], [4, 5, 45], [5, 6, 55], [6, 7, 65], [7, 8, 75], [8, 9, 85], [9, 10, 95], [10, 1, 105]]) == 9
    assert candidate(transactions = [[0, 1, 100], [1, 2, 200], [2, 0, 150], [0, 3, 50], [3, 4, 100], [4, 2, 50]]) == 2
    assert candidate(transactions = [[1, 2, 12], [2, 3, 24], [3, 4, 36], [4, 5, 48], [5, 6, 60], [6, 1, 72]]) == 5
    assert candidate(transactions = [[1, 2, 50], [2, 3, 30], [3, 4, 20], [4, 5, 10], [5, 1, 40], [1, 3, 10], [3, 2, 5], [2, 4, 20]]) == 3
    assert candidate(transactions = [[1, 2, 30], [2, 3, 20], [3, 4, 10], [4, 5, 5], [5, 6, 3], [6, 7, 2], [7, 8, 1], [8, 9, 1]]) == 7
    assert candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 0, 40], [2, 0, 50], [3, 0, 60], [1, 2, 5], [2, 1, 5], [2, 3, 5], [3, 2, 5]]) == 3
    assert candidate(transactions = [[0, 1, 100], [1, 2, 50], [2, 3, 25], [3, 4, 12], [4, 5, 6], [5, 0, 3], [0, 3, 7], [3, 1, 18]]) == 5
    assert candidate(transactions = [[5, 6, 5], [6, 7, 3], [7, 8, 8], [8, 9, 6], [9, 5, 4], [5, 7, 2], [7, 6, 1], [6, 8, 4]]) == 4
    assert candidate(transactions = [[1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 7, 10], [7, 1, 10], [1, 8, 10], [8, 9, 10], [9, 10, 10], [10, 1, 10]]) == 0
    assert candidate(transactions = [[1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 5, 5], [5, 1, 5], [1, 3, 5], [3, 2, 5], [2, 4, 5], [4, 3, 5]]) == 1
    assert candidate(transactions = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 0, 1500]]) == 5
    assert candidate(transactions = [[0, 1, 20], [1, 2, 30], [2, 3, 10], [3, 0, 40], [0, 2, 15], [2, 1, 5], [1, 3, 5]]) == 3
    assert candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 0, 10]]) == 9
    assert candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 2, 5], [2, 3, 15], [3, 1, 25]]) == 3
    assert candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 0, 100]]) == 9
    assert candidate(transactions = [[0, 1, 10], [1, 2, 5], [2, 0, 3], [0, 3, 8], [3, 2, 4], [2, 1, 2], [1, 0, 1]]) == 3
    assert candidate(transactions = [[5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 5, 6], [5, 8, 12], [6, 9, 15]]) == 4
    assert candidate(transactions = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [0, 4, 40], [1, 2, 15], [1, 3, 25], [1, 4, 35], [2, 3, 5], [2, 4, 15], [3, 4, 25]]) == 4
    assert candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 0, 10], [0, 2, 10], [2, 1, 10], [1, 3, 10], [3, 2, 10]]) == 1
    assert candidate(transactions = [[0, 1, 10], [1, 2, 15], [2, 3, 5], [3, 0, 10], [0, 2, 10], [2, 1, 5]]) == 2
    assert candidate(transactions = [[0, 1, 15], [1, 2, 10], [2, 3, 5], [3, 0, 20], [1, 3, 5]]) == 2
    assert candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 0, 15], [1, 3, 5], [2, 4, 10], [3, 0, 10], [4, 1, 20], [0, 5, 10], [1, 4, 5]]) == 4
    assert candidate(transactions = [[1, 2, 15], [2, 3, 10], [3, 4, 5], [4, 1, 20], [1, 3, 5], [3, 2, 10], [2, 4, 5], [4, 3, 5]]) == 2
    assert candidate(transactions = [[10, 11, 1], [11, 12, 2], [12, 13, 3], [13, 14, 4], [14, 15, 5], [15, 16, 6], [16, 17, 7], [17, 18, 8]]) == 8
    assert candidate(transactions = [[0, 1, 100], [1, 2, 50], [2, 3, 25], [3, 4, 12], [4, 0, 83], [0, 2, 17], [2, 1, 32], [1, 3, 45], [3, 2, 13], [2, 4, 6], [4, 1, 2]]) == 4
    assert candidate(transactions = [[10, 11, 10], [11, 12, 5], [12, 13, 15], [13, 14, 20], [14, 10, 25], [10, 13, 10], [11, 14, 15], [12, 10, 5], [13, 11, 20], [14, 12, 25]]) == 4
    assert candidate(transactions = [[0, 1, 15], [1, 2, 20], [2, 0, 5], [3, 4, 10], [4, 3, 5], [0, 3, 10]]) == 3
    assert candidate(transactions = [[5, 0, 10], [0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 0, 10]]) == 1
    assert candidate(transactions = [[0, 1, 50], [1, 2, 100], [2, 3, 150], [3, 4, 200], [4, 5, 250], [5, 6, 300], [6, 7, 350], [7, 0, 400]]) == 7
    assert candidate(transactions = [[1, 2, 100], [2, 3, 200], [3, 4, 300], [4, 5, 400], [5, 1, 100], [1, 3, 100], [3, 5, 100], [5, 2, 100]]) == 3
    assert candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 28]]) == 7
    assert candidate(transactions = [[1, 2, 25], [2, 3, 15], [3, 4, 5], [4, 5, 10], [5, 6, 5], [6, 1, 20], [1, 3, 15], [3, 5, 5]]) == 4
    assert candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 0, 7]]) == 6
    assert candidate(transactions = [[0, 1, 20], [1, 2, 10], [2, 3, 5], [3, 4, 5], [4, 0, 15], [0, 5, 10], [5, 1, 5]]) == 3
    assert candidate(transactions = [[1, 2, 25], [2, 3, 15], [3, 4, 10], [4, 5, 5], [5, 6, 30], [6, 1, 20]]) == 4
    assert candidate(transactions = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 1, 2], [1, 3, 1], [2, 4, 2], [3, 5, 3]]) == 4
    assert candidate(transactions = [[0, 1, 30], [1, 2, 20], [2, 3, 10], [3, 4, 40], [4, 5, 50], [5, 0, 60], [1, 3, 5], [2, 4, 15], [3, 5, 25]]) == 4
    assert candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 0, 40], [0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 0, 40]]) == 3
    assert candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 0, 90]]) == 8
    assert candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 0, 150]]) == 5
    assert candidate(transactions = [[1, 2, 20], [2, 3, 15], [3, 4, 25], [4, 1, 20], [1, 3, 10], [3, 2, 5], [2, 4, 20]]) == 3
    assert candidate(transactions = [[7, 6, 5], [6, 5, 4], [5, 4, 3], [4, 3, 2], [3, 2, 1], [2, 1, 6], [1, 0, 7]]) == 6
    assert candidate(transactions = [[10, 9, 50], [9, 8, 40], [8, 7, 30], [7, 6, 20], [6, 5, 10], [5, 4, 5], [4, 3, 20], [3, 2, 10], [2, 1, 5], [1, 0, 15]]) == 8
    assert candidate(transactions = [[2, 0, 50], [3, 4, 40], [2, 3, 30], [4, 0, 10], [0, 1, 20], [1, 2, 30], [3, 0, 40], [4, 2, 10], [1, 3, 20], [2, 4, 15]]) == 4
    assert candidate(transactions = [[1, 2, 50], [2, 3, 30], [3, 4, 20], [4, 5, 10], [5, 1, 15], [1, 3, 10]]) == 4
    assert candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 0, 5], [0, 1, 6], [1, 2, 7], [2, 3, 8], [3, 4, 9], [4, 0, 10]]) == 4
    assert candidate(transactions = [[5, 4, 10], [4, 3, 20], [3, 2, 30], [2, 1, 40], [1, 0, 100], [0, 5, 50]]) == 5
    assert candidate(transactions = [[1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 10, 100], [10, 1, 110], [1, 11, 120], [11, 2, 130], [2, 12, 140], [12, 3, 150]]) == 11
    assert candidate(transactions = [[1, 2, 50], [2, 3, 30], [3, 4, 20], [4, 5, 10], [5, 6, 5], [6, 7, 5], [7, 8, 10], [8, 9, 15], [9, 10, 20], [10, 1, 25]]) == 6
    assert candidate(transactions = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 0, 10]]) == 0
    assert candidate(transactions = [[0, 1, 20], [1, 2, 30], [2, 3, 40], [3, 4, 50], [4, 5, 60], [5, 6, 70], [6, 7, 80], [7, 0, 350]]) == 7
    assert candidate(transactions = [[0, 1, 20], [1, 2, 30], [2, 3, 40], [3, 0, 10], [0, 2, 25], [2, 1, 5], [1, 3, 15]]) == 3
    assert candidate(transactions = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 2, 1], [1, 3, 1], [2, 4, 1], [3, 0, 1], [4, 1, 1]]) == 0
    assert candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 0, 60]]) == 5
    assert candidate(transactions = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 6, 600], [6, 7, 700], [7, 8, 800], [8, 9, 900], [9, 0, 1000]]) == 9
    assert candidate(transactions = [[0, 1, 1], [1, 2, 2], [2, 0, 3], [0, 3, 4], [3, 1, 5], [1, 4, 6], [4, 2, 7], [2, 5, 8], [5, 3, 9]]) == 5
    assert candidate(transactions = [[0, 1, 10], [1, 2, 5], [2, 0, 5], [0, 3, 10], [3, 1, 10], [1, 4, 5], [4, 2, 5]]) == 2
    assert candidate(transactions = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 0, 80]]) == 7
    assert candidate(transactions = [[0, 1, 20], [1, 2, 15], [2, 3, 10], [3, 0, 5], [1, 3, 10], [2, 0, 5]]) == 2
    assert candidate(transactions = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 0, 5], [1, 3, 5], [3, 5, 5]]) == 1
    assert candidate(transactions = [[0, 1, 50], [1, 2, 20], [2, 0, 10], [0, 3, 30], [3, 1, 10], [1, 0, 10], [0, 4, 20], [4, 3, 10], [3, 2, 5], [2, 1, 5]]) == 4
    assert candidate(transactions = [[0, 1, 50], [1, 2, 100], [2, 3, 150], [3, 4, 200], [4, 5, 250], [5, 6, 300], [6, 7, 350], [7, 8, 400], [8, 0, 450]]) == 8
    assert candidate(transactions = [[0, 1, 15], [1, 2, 25], [2, 3, 35], [3, 4, 45], [4, 5, 55], [5, 6, 65], [6, 0, 240]]) == 6
    assert candidate(transactions = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40], [8, 9, 45], [9, 0, 50]]) == 9


