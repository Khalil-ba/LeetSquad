def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(m = 4,n = 4) == 1624
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4) == 1624: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 7) == 72912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 7) == 72912: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 8) == 213616
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 8) == 213616: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2) == 56: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 5) == 8776
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 5) == 8776: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 9) == 387488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 9) == 387488: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 2) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 2) == 65: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5) == 7152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5) == 7152: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 6) == 26016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 6) == 26016: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 9) == 281408
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 9) == 281408: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9) == 140704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9) == 140704: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 9) == 389488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 9) == 389488: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8) == 140704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8) == 140704: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3) == 320: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 9) == 389497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 9) == 389497: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 3) == 376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 3) == 376: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 7) == 106080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 7) == 106080: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 9) == 380336
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 9) == 380336: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 5) == 9161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 5) == 9161: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 6) == 33168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 6) == 33168: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 7) == 98928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 7) == 98928: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 5) == 9096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 5) == 9096: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 9) == 389432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 9) == 389432: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 9) == 354320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 9) == 354320: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 7) == 108024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 7) == 108024: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 8) == 246784
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 8) == 246784: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 6) == 34792
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 6) == 34792: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 4) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 4) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 5) == 9152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 5) == 9152: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 9) == 389112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 9) == 389112: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 8) == 248728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 8) == 248728: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 7) == 108080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 7) == 108080: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 3) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 3) == 385: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 8) == 248793
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 8) == 248793: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 8) == 248784
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 8) == 248784: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 4) == 2009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 4) == 2009: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 8) == 239632
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 8) == 239632: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(m = 4,n = 4) == 1624
    assert candidate(m = 7,n = 7) == 72912
    assert candidate(m = 7,n = 8) == 213616
    assert candidate(m = 2,n = 2) == 56
    assert candidate(m = 4,n = 5) == 8776
    assert candidate(m = 5,n = 9) == 387488
    assert candidate(m = 1,n = 2) == 65
    assert candidate(m = 5,n = 5) == 7152
    assert candidate(m = 6,n = 6) == 26016
    assert candidate(m = 8,n = 9) == 281408
    assert candidate(m = 9,n = 9) == 140704
    assert candidate(m = 1,n = 1) == 9
    assert candidate(m = 2,n = 9) == 389488
    assert candidate(m = 8,n = 8) == 140704
    assert candidate(m = 3,n = 3) == 320
    assert candidate(m = 1,n = 9) == 389497
    assert candidate(m = 2,n = 3) == 376
    assert candidate(m = 5,n = 7) == 106080
    assert candidate(m = 6,n = 9) == 380336
    assert candidate(m = 1,n = 5) == 9161
    assert candidate(m = 5,n = 6) == 33168
    assert candidate(m = 6,n = 7) == 98928
    assert candidate(m = 3,n = 5) == 9096
    assert candidate(m = 3,n = 9) == 389432
    assert candidate(m = 7,n = 9) == 354320
    assert candidate(m = 3,n = 7) == 108024
    assert candidate(m = 5,n = 8) == 246784
    assert candidate(m = 4,n = 6) == 34792
    assert candidate(m = 2,n = 4) == 2000
    assert candidate(m = 2,n = 5) == 9152
    assert candidate(m = 4,n = 9) == 389112
    assert candidate(m = 3,n = 8) == 248728
    assert candidate(m = 2,n = 7) == 108080
    assert candidate(m = 1,n = 3) == 385
    assert candidate(m = 1,n = 8) == 248793
    assert candidate(m = 2,n = 8) == 248784
    assert candidate(m = 1,n = 4) == 2009
    assert candidate(m = 6,n = 8) == 239632


