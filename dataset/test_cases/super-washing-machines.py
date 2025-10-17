def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(machines = [0, 2, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 2, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [9, 1, 8, 8, 9]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [9, 1, 8, 8, 9]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 18]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 18]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 0, 0, 3, 0, 2, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 0, 0, 3, 0, 2, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [100000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [100000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [4, 0, 0, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [4, 0, 0, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(machines = [5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 0, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 0, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 3, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 3, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(machines = [10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 2, 3, 4, 5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 2, 3, 4, 5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 0, 0, 3, 0, 0, 2, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 0, 0, 3, 0, 0, 2, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 11, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 11, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 0, 5, 4, 0, 0, 2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 0, 5, 4, 0, 0, 2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 12500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 12500: {e}')
    
    total += 1
    try:
        result = candidate(machines = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(machines = [2, 2, 2, 2, 1, 2, 2, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [2, 2, 2, 2, 1, 2, 2, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(machines = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 12500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 12500: {e}')
    
    total += 1
    try:
        result = candidate(machines = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 0, 0, 0, 0, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 0, 0, 0, 0, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(machines = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [4, 5, 6, 7, 8]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [4, 5, 6, 7, 8]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(machines = [10, 15, 10, 15, 10, 15, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [10, 15, 10, 15, 10, 15, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 0, 0, 0, 0, 21, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 0, 0, 0, 0, 21, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(machines = [10, 1, 1, 1, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [10, 1, 1, 1, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 0, 0, 0, 0, 10, 0, 0, 0, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 0, 0, 0, 0, 10, 0, 0, 0, 0, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(machines = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(machines = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(machines = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(machines = [0, 2, 0]) == -1
    assert candidate(machines = [9, 1, 8, 8, 9]) == 4
    assert candidate(machines = [0, 0, 18]) == 12
    assert candidate(machines = [1, 0, 0, 3, 0, 2, 0]) == -1
    assert candidate(machines = [100000]) == 0
    assert candidate(machines = [0, 0, 0, 0, 0]) == 0
    assert candidate(machines = [4, 0, 0, 4]) == 2
    assert candidate(machines = [5, 5, 5, 5, 5]) == 0
    assert candidate(machines = [1]) == 0
    assert candidate(machines = [1, 1, 1, 1]) == 0
    assert candidate(machines = [1, 0, 5]) == 3
    assert candidate(machines = [0, 3, 0]) == 2
    assert candidate(machines = [10, 10, 10, 10]) == 0
    assert candidate(machines = [1, 2, 3, 4, 5]) == 3
    assert candidate(machines = [1, 0, 0, 3, 0, 0, 2, 0]) == -1
    assert candidate(machines = [0, 0, 11, 5]) == 8
    assert candidate(machines = [1, 0, 5, 4, 0, 0, 2, 3]) == -1
    assert candidate(machines = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(machines = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(machines = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 12500
    assert candidate(machines = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 95
    assert candidate(machines = [2, 2, 2, 2, 1, 2, 2, 2, 2]) == -1
    assert candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 10]) == 9
    assert candidate(machines = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(machines = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1
    assert candidate(machines = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 12500
    assert candidate(machines = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == -1
    assert candidate(machines = [1, 0, 0, 0, 0, 5]) == 4
    assert candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == -1
    assert candidate(machines = [20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 19
    assert candidate(machines = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(machines = [4, 5, 6, 7, 8]) == 3
    assert candidate(machines = [10, 15, 10, 15, 10, 15, 10]) == -1
    assert candidate(machines = [0, 0, 0, 0, 0, 0, 21, 0]) == -1
    assert candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 95
    assert candidate(machines = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == -1
    assert candidate(machines = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28
    assert candidate(machines = [10, 1, 1, 1, 10]) == -1
    assert candidate(machines = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(machines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 28
    assert candidate(machines = [1, 0, 0, 0, 0, 10, 0, 0, 0, 0, 1]) == -1
    assert candidate(machines = [0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == -1
    assert candidate(machines = [5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(machines = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(machines = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(machines = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(machines = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 95
    assert candidate(machines = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == -1
    assert candidate(machines = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == -1


