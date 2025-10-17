def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', '2', 'b', '2', 'c', '3']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', '2', 'b', '2', 'c', '3']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'a', 'b', 'b', 'a', 'a']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'a', 'b', 'b', 'a', 'a']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'b', 'c']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'b', 'c']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f', 'f', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f', 'f', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', '1', '1', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', '1', '1', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'b', 'b', 'a', 'a', 'a', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 'e']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'b', 'b', 'a', 'a', 'a', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 'e']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f', 'g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i', 'j', 'j', 'j', 'k', 'k', 'k', 'l', 'l', 'l', 'm', 'm', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'p', 'p', 'p', 'q', 'q', 'q', 'r', 'r', 'r', 's', 's', 's', 't', 't', 't', 'u', 'u', 'u', 'v', 'v', 'v', 'w', 'w', 'w', 'x', 'x', 'x', 'y', 'y', 'y', 'z', 'z', 'z']) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f', 'g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i', 'j', 'j', 'j', 'k', 'k', 'k', 'l', 'l', 'l', 'm', 'm', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'p', 'p', 'p', 'q', 'q', 'q', 'r', 'r', 'r', 's', 's', 's', 't', 't', 't', 'u', 'u', 'u', 'v', 'v', 'v', 'w', 'w', 'w', 'x', 'x', 'x', 'y', 'y', 'y', 'z', 'z', 'z']) == 52: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['x', 'y', 'y', 'z', 'z', 'z', 'x', 'y', 'y', 'z', 'z', 'z', 'x', 'y', 'y', 'z', 'z', 'z', 'x', 'y', 'y', 'z', 'z', 'z']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['x', 'y', 'y', 'z', 'z', 'z', 'x', 'y', 'y', 'z', 'z', 'z', 'x', 'y', 'y', 'z', 'z', 'z', 'x', 'y', 'y', 'z', 'z', 'z']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['x', 'x', 'x', 'y', 'y', 'z', 'z', 'z', 'z', 'z', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['x', 'x', 'x', 'y', 'y', 'z', 'z', 'z', 'z', 'z', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(chars = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(chars = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) == 82: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(chars = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == 3
    assert candidate(chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 10
    assert candidate(chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']) == 4
    assert candidate(chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']) == 6
    assert candidate(chars = ['a', '2', 'b', '2', 'c', '3']) == 6
    assert candidate(chars = ['a', 'a', 'a', 'b', 'b', 'a', 'a']) == 6
    assert candidate(chars = ['a']) == 1
    assert candidate(chars = ['a', 'b', 'c']) == 3
    assert candidate(chars = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']) == 9
    assert candidate(chars = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']) == 3
    assert candidate(chars = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f', 'f', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']) == 14
    assert candidate(chars = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']) == 20
    assert candidate(chars = ['a', '1', '1', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']) == 12
    assert candidate(chars = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']) == 3
    assert candidate(chars = ['a', 'b', 'b', 'a', 'a', 'a', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 'e']) == 11
    assert candidate(chars = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c']) == 12
    assert candidate(chars = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) == 20
    assert candidate(chars = ['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm']) == 3
    assert candidate(chars = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f', 'g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i', 'j', 'j', 'j', 'k', 'k', 'k', 'l', 'l', 'l', 'm', 'm', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'p', 'p', 'p', 'q', 'q', 'q', 'r', 'r', 'r', 's', 's', 's', 't', 't', 't', 'u', 'u', 'u', 'v', 'v', 'v', 'w', 'w', 'w', 'x', 'x', 'x', 'y', 'y', 'y', 'z', 'z', 'z']) == 52
    assert candidate(chars = ['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']) == 9
    assert candidate(chars = ['a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']) == 9
    assert candidate(chars = ['x', 'y', 'y', 'z', 'z', 'z', 'x', 'y', 'y', 'z', 'z', 'z', 'x', 'y', 'y', 'z', 'z', 'z', 'x', 'y', 'y', 'z', 'z', 'z']) == 20
    assert candidate(chars = ['x', 'x', 'x', 'y', 'y', 'z', 'z', 'z', 'z', 'z', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']) == 9
    assert candidate(chars = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == 24
    assert candidate(chars = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) == 82


