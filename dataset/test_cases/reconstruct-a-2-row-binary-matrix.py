def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(upper = 2,lower = 3,colsum = [2, 2, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 2,lower = 3,colsum = [2, 2, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 1,lower = 1,colsum = [1, 0, 1]) == [[0, 0, 1], [1, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 1,lower = 1,colsum = [1, 0, 1]) == [[0, 0, 1], [1, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 4,lower = 2,colsum = [2, 1, 1, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 4,lower = 2,colsum = [2, 1, 1, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 3,colsum = [2, 0, 2, 0, 2]) == [[1, 0, 1, 0, 1], [1, 0, 1, 0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 3,colsum = [2, 0, 2, 0, 2]) == [[1, 0, 1, 0, 1], [1, 0, 1, 0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 0,lower = 0,colsum = [0, 0, 0, 0]) == [[0, 0, 0, 0], [0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 0,lower = 0,colsum = [0, 0, 0, 0]) == [[0, 0, 0, 0], [0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]) == [[1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]) == [[1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 2,lower = 1,colsum = [1, 1, 1]) == [[1, 0, 1], [0, 1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 2,lower = 1,colsum = [1, 1, 1]) == [[1, 0, 1], [0, 1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 10,lower = 10,colsum = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 10,lower = 10,colsum = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 0,lower = 0,colsum = [0, 0, 0, 0, 0]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 0,lower = 0,colsum = [0, 0, 0, 0, 0]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 15,lower = 5,colsum = [2, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 15,lower = 5,colsum = [2, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 2,colsum = [2, 1, 1, 0, 1]) == [[1, 1, 0, 0, 1], [1, 0, 1, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 2,colsum = [2, 1, 1, 0, 1]) == [[1, 1, 0, 0, 1], [1, 0, 1, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 3,colsum = [1, 1, 1, 1, 1, 1]) == [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 3,colsum = [1, 1, 1, 1, 1, 1]) == [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 6,lower = 4,colsum = [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 6,lower = 4,colsum = [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [2, 1, 1, 0, 0, 0, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [2, 1, 1, 0, 0, 0, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 6,lower = 4,colsum = [2, 2, 1, 1, 0, 0, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 6,lower = 4,colsum = [2, 2, 1, 1, 0, 0, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 10,lower = 6,colsum = [2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 10,lower = 6,colsum = [2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 7,lower = 5,colsum = [1, 2, 1, 2, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 7,lower = 5,colsum = [1, 2, 1, 2, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]) == [[1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]) == [[1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [0, 1, 2, 0, 0, 1, 2, 1, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [0, 1, 2, 0, 0, 1, 2, 1, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 8,lower = 2,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 8,lower = 2,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 1,colsum = [1, 2, 1, 1, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 1,colsum = [1, 2, 1, 1, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 2,colsum = [1, 1, 1, 1, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 2,colsum = [1, 1, 1, 1, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 1,lower = 1,colsum = [2]) == [[1], [1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 1,lower = 1,colsum = [2]) == [[1], [1]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 6,colsum = [2, 2, 1, 1, 1, 2, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 6,colsum = [2, 2, 1, 1, 1, 2, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [2, 1, 0, 1, 0, 2, 1, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [2, 1, 0, 1, 0, 2, 1, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 2,lower = 2,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 2,lower = 2,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 1,lower = 2,colsum = [1, 1, 0, 0, 1]) == [[0, 0, 0, 0, 1], [1, 1, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 1,lower = 2,colsum = [1, 1, 0, 0, 1]) == [[0, 0, 0, 0, 1], [1, 1, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 4,lower = 4,colsum = [2, 0, 1, 1, 2, 1, 1, 0]) == [[1, 0, 0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 4,lower = 4,colsum = [2, 0, 1, 1, 2, 1, 1, 0]) == [[1, 0, 0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 1,lower = 1,colsum = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 1,lower = 1,colsum = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 2,lower = 2,colsum = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 2,lower = 2,colsum = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 3,colsum = [2, 0, 1, 1, 2]) == [[1, 0, 0, 1, 1], [1, 0, 1, 0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 3,colsum = [2, 0, 1, 1, 2]) == [[1, 0, 0, 1, 1], [1, 0, 1, 0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [1, 2, 0, 2, 1, 0, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [1, 2, 0, 2, 1, 0, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 8,lower = 8,colsum = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 8,lower = 8,colsum = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 4,lower = 4,colsum = [2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 4,lower = 4,colsum = [2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 6,lower = 6,colsum = [2, 1, 0, 2, 1, 0, 1, 1, 0, 0, 2, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 6,lower = 6,colsum = [2, 1, 0, 2, 1, 0, 1, 1, 0, 0, 2, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 7,lower = 3,colsum = [1, 0, 1, 2, 1, 0, 1, 1, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 7,lower = 3,colsum = [1, 0, 1, 2, 1, 0, 1, 1, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 3,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 3,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 2,colsum = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 2,colsum = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [0, 1, 2, 1, 1, 0, 2, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [0, 1, 2, 1, 1, 0, 2, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 4,colsum = [1, 2, 1, 1, 0, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 4,colsum = [1, 2, 1, 1, 0, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 6,lower = 4,colsum = [2, 1, 1, 1, 1, 2, 0, 1, 1, 0]) == [[1, 1, 1, 0, 1, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 6,lower = 4,colsum = [2, 1, 1, 1, 1, 2, 0, 1, 1, 0]) == [[1, 1, 1, 0, 1, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 7,lower = 3,colsum = [1, 2, 1, 1, 1, 0, 0, 2]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 7,lower = 3,colsum = [1, 2, 1, 1, 1, 0, 0, 2]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 10,lower = 10,colsum = [2, 2, 2, 2, 2, 0, 0, 0, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 10,lower = 10,colsum = [2, 2, 2, 2, 2, 0, 0, 0, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 3,colsum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 3,colsum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 9,lower = 9,colsum = [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 9,lower = 9,colsum = [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 8,lower = 6,colsum = [2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 8,lower = 6,colsum = [2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 8,lower = 7,colsum = [2, 2, 2, 0, 1, 1, 0, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 8,lower = 7,colsum = [2, 2, 2, 0, 1, 1, 0, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 10,lower = 10,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 10,lower = 10,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 4,colsum = [2, 1, 1, 1, 0, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 4,colsum = [2, 1, 1, 1, 0, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 8,lower = 4,colsum = [2, 2, 2, 2, 0, 0, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 8,lower = 4,colsum = [2, 2, 2, 2, 0, 0, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 4,lower = 5,colsum = [1, 1, 1, 1, 2, 1, 0, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 4,lower = 5,colsum = [1, 1, 1, 1, 2, 1, 0, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 3,colsum = [1, 1, 1, 2, 1, 2, 0, 0]) == [[1, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 3,colsum = [1, 1, 1, 2, 1, 2, 0, 0]) == [[1, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 10,lower = 5,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 10,lower = 5,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 7,lower = 3,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 7,lower = 3,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 3,colsum = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 3,colsum = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 10,lower = 10,colsum = [2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 10,lower = 10,colsum = [2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 8,lower = 8,colsum = [1, 2, 2, 1, 2, 1, 1, 2]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 8,lower = 8,colsum = [1, 2, 2, 1, 2, 1, 1, 2]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 1,lower = 1,colsum = [0, 0, 0, 0, 0, 2]) == [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 1,lower = 1,colsum = [0, 0, 0, 0, 0, 2]) == [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 0,lower = 0,colsum = [0, 0, 0, 0, 0]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 0,lower = 0,colsum = [0, 0, 0, 0, 0]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 4,colsum = [2, 1, 2, 0, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 4,colsum = [2, 1, 2, 0, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 10,lower = 10,colsum = [2, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 0, 0, 0, 1, 1, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 10,lower = 10,colsum = [2, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 0, 0, 0, 1, 1, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 7,lower = 3,colsum = [1, 2, 1, 1, 0, 2, 1, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 7,lower = 3,colsum = [1, 2, 1, 1, 0, 2, 1, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 7,lower = 8,colsum = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 7,lower = 8,colsum = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 7,lower = 5,colsum = [1, 2, 2, 1, 1, 0, 0, 0, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 7,lower = 5,colsum = [1, 2, 2, 1, 1, 0, 0, 0, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 3,lower = 3,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 3,lower = 3,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 5,lower = 5,colsum = [2, 0, 2, 0, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 5,lower = 5,colsum = [2, 0, 2, 0, 1, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 7,lower = 3,colsum = [2, 1, 2, 1, 0, 0, 0, 1, 1, 0, 0, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 7,lower = 3,colsum = [2, 1, 2, 1, 0, 0, 0, 1, 1, 0, 0, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 10,lower = 5,colsum = [2, 2, 2, 1, 1, 1, 1, 1, 1, 0]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 10,lower = 5,colsum = [2, 2, 2, 1, 1, 1, 1, 1, 1, 0]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 6,lower = 6,colsum = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 6,lower = 6,colsum = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == []: {e}')
    
    total += 1
    try:
        result = candidate(upper = 4,lower = 4,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(upper = 4,lower = 4,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(upper = 2,lower = 3,colsum = [2, 2, 1, 1]) == []
    assert candidate(upper = 1,lower = 1,colsum = [1, 0, 1]) == [[0, 0, 1], [1, 0, 0]]
    assert candidate(upper = 4,lower = 2,colsum = [2, 1, 1, 0, 0]) == []
    assert candidate(upper = 3,lower = 3,colsum = [2, 0, 2, 0, 2]) == [[1, 0, 1, 0, 1], [1, 0, 1, 0, 1]]
    assert candidate(upper = 0,lower = 0,colsum = [0, 0, 0, 0]) == [[0, 0, 0, 0], [0, 0, 0, 0]]
    assert candidate(upper = 5,lower = 5,colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]) == [[1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]
    assert candidate(upper = 2,lower = 1,colsum = [1, 1, 1]) == [[1, 0, 1], [0, 1, 0]]
    assert candidate(upper = 10,lower = 10,colsum = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert candidate(upper = 0,lower = 0,colsum = [0, 0, 0, 0, 0]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert candidate(upper = 5,lower = 5,colsum = [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert candidate(upper = 15,lower = 5,colsum = [2, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == []
    assert candidate(upper = 3,lower = 2,colsum = [2, 1, 1, 0, 1]) == [[1, 1, 0, 0, 1], [1, 0, 1, 0, 0]]
    assert candidate(upper = 3,lower = 3,colsum = [1, 1, 1, 1, 1, 1]) == [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0]]
    assert candidate(upper = 6,lower = 4,colsum = [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == []
    assert candidate(upper = 5,lower = 5,colsum = [2, 1, 1, 0, 0, 0, 1, 1, 1, 1]) == []
    assert candidate(upper = 6,lower = 4,colsum = [2, 2, 1, 1, 0, 0, 1]) == []
    assert candidate(upper = 10,lower = 6,colsum = [2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == []
    assert candidate(upper = 7,lower = 5,colsum = [1, 2, 1, 2, 1, 1, 1]) == []
    assert candidate(upper = 5,lower = 5,colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]) == [[1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]
    assert candidate(upper = 5,lower = 5,colsum = [0, 1, 2, 0, 0, 1, 2, 1, 0]) == []
    assert candidate(upper = 8,lower = 2,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert candidate(upper = 3,lower = 1,colsum = [1, 2, 1, 1, 0]) == []
    assert candidate(upper = 3,lower = 2,colsum = [1, 1, 1, 1, 0]) == []
    assert candidate(upper = 1,lower = 1,colsum = [2]) == [[1], [1]]
    assert candidate(upper = 3,lower = 6,colsum = [2, 2, 1, 1, 1, 2, 1]) == []
    assert candidate(upper = 5,lower = 5,colsum = [2, 1, 0, 1, 0, 2, 1, 0]) == []
    assert candidate(upper = 2,lower = 2,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert candidate(upper = 1,lower = 2,colsum = [1, 1, 0, 0, 1]) == [[0, 0, 0, 0, 1], [1, 1, 0, 0, 0]]
    assert candidate(upper = 4,lower = 4,colsum = [2, 0, 1, 1, 2, 1, 1, 0]) == [[1, 0, 0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 0]]
    assert candidate(upper = 1,lower = 1,colsum = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert candidate(upper = 2,lower = 2,colsum = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    assert candidate(upper = 3,lower = 3,colsum = [2, 0, 1, 1, 2]) == [[1, 0, 0, 1, 1], [1, 0, 1, 0, 1]]
    assert candidate(upper = 5,lower = 5,colsum = [1, 2, 0, 2, 1, 0, 1]) == []
    assert candidate(upper = 8,lower = 8,colsum = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == []
    assert candidate(upper = 4,lower = 4,colsum = [2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]) == []
    assert candidate(upper = 6,lower = 6,colsum = [2, 1, 0, 2, 1, 0, 1, 1, 0, 0, 2, 1]) == []
    assert candidate(upper = 7,lower = 3,colsum = [1, 0, 1, 2, 1, 0, 1, 1, 0]) == []
    assert candidate(upper = 3,lower = 3,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert candidate(upper = 3,lower = 2,colsum = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == []
    assert candidate(upper = 5,lower = 5,colsum = [0, 1, 2, 1, 1, 0, 2, 0]) == []
    assert candidate(upper = 3,lower = 4,colsum = [1, 2, 1, 1, 0, 1]) == []
    assert candidate(upper = 6,lower = 4,colsum = [2, 1, 1, 1, 1, 2, 0, 1, 1, 0]) == [[1, 1, 1, 0, 1, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1, 0, 0]]
    assert candidate(upper = 7,lower = 3,colsum = [1, 2, 1, 1, 1, 0, 0, 2]) == []
    assert candidate(upper = 10,lower = 10,colsum = [2, 2, 2, 2, 2, 0, 0, 0, 0, 0]) == []
    assert candidate(upper = 5,lower = 3,colsum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert candidate(upper = 5,lower = 5,colsum = [0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0]) == []
    assert candidate(upper = 9,lower = 9,colsum = [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == []
    assert candidate(upper = 8,lower = 6,colsum = [2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == []
    assert candidate(upper = 8,lower = 7,colsum = [2, 2, 2, 0, 1, 1, 0, 1]) == []
    assert candidate(upper = 10,lower = 10,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2]) == []
    assert candidate(upper = 5,lower = 4,colsum = [2, 1, 1, 1, 0, 1]) == []
    assert candidate(upper = 8,lower = 4,colsum = [2, 2, 2, 2, 0, 0, 0, 0]) == []
    assert candidate(upper = 4,lower = 5,colsum = [1, 1, 1, 1, 2, 1, 0, 1]) == []
    assert candidate(upper = 5,lower = 3,colsum = [1, 1, 1, 2, 1, 2, 0, 0]) == [[1, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0]]
    assert candidate(upper = 10,lower = 5,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == []
    assert candidate(upper = 7,lower = 3,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 1, 0, 1, 0]]
    assert candidate(upper = 3,lower = 3,colsum = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == [[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]]
    assert candidate(upper = 10,lower = 10,colsum = [2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == []
    assert candidate(upper = 8,lower = 8,colsum = [1, 2, 2, 1, 2, 1, 1, 2]) == []
    assert candidate(upper = 1,lower = 1,colsum = [0, 0, 0, 0, 0, 2]) == [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1]]
    assert candidate(upper = 0,lower = 0,colsum = [0, 0, 0, 0, 0]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert candidate(upper = 3,lower = 4,colsum = [2, 1, 2, 0, 1]) == []
    assert candidate(upper = 10,lower = 10,colsum = [2, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 0, 0, 0, 1, 1, 0]) == []
    assert candidate(upper = 7,lower = 3,colsum = [1, 2, 1, 1, 0, 2, 1, 0]) == []
    assert candidate(upper = 7,lower = 8,colsum = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert candidate(upper = 7,lower = 5,colsum = [1, 2, 2, 1, 1, 0, 0, 0, 1, 1]) == []
    assert candidate(upper = 3,lower = 3,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []
    assert candidate(upper = 5,lower = 5,colsum = [2, 0, 2, 0, 1, 1]) == []
    assert candidate(upper = 7,lower = 3,colsum = [2, 1, 2, 1, 0, 0, 0, 1, 1, 0, 0, 1]) == []
    assert candidate(upper = 10,lower = 5,colsum = [2, 2, 2, 1, 1, 1, 1, 1, 1, 0]) == []
    assert candidate(upper = 6,lower = 6,colsum = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == []
    assert candidate(upper = 4,lower = 4,colsum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == []


