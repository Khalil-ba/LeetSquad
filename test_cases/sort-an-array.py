def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [0]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000]) == [50000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000]) == [50000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50000]) == [-50000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50000]) == [-50000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == [1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [0]) == [0]
    assert candidate(nums = [-1]) == [-1]
    assert candidate(nums = [50000]) == [50000]
    assert candidate(nums = [-50000]) == [-50000]
    assert candidate(nums = [1]) == [1]


