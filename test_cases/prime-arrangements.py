def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 30) == 13697484
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 13697484: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 75763854
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 75763854: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 918450925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 918450925: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 344376809
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 344376809: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 445364737
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 445364737: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 682289015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 682289015: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 451768713
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 451768713: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 17280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 17280: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 519081041
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 519081041: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 61) == 250895270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 61) == 250895270: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == 627742601
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == 627742601: {e}')
    
    total += 1
    try:
        result = candidate(n = 70) == 892906519
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70) == 892906519: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 125049738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 125049738: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 965722612
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 965722612: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 546040181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 546040181: {e}')
    
    total += 1
    try:
        result = candidate(n = 98) == 892915734
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98) == 892915734: {e}')
    
    total += 1
    try:
        result = candidate(n = 73) == 78238453
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73) == 78238453: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == 405243354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == 405243354: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == 673469112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == 673469112: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == 430788419
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == 430788419: {e}')
    
    total += 1
    try:
        result = candidate(n = 83) == 913651722
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 83) == 913651722: {e}')
    
    total += 1
    try:
        result = candidate(n = 90) == 448961084
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90) == 448961084: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 30) == 13697484
    assert candidate(n = 99) == 75763854
    assert candidate(n = 75) == 918450925
    assert candidate(n = 20) == 344376809
    assert candidate(n = 2) == 1
    assert candidate(n = 19) == 445364737
    assert candidate(n = 100) == 682289015
    assert candidate(n = 50) == 451768713
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 17280
    assert candidate(n = 5) == 12
    assert candidate(n = 97) == 519081041
    assert candidate(n = 3) == 2
    assert candidate(n = 61) == 250895270
    assert candidate(n = 47) == 627742601
    assert candidate(n = 70) == 892906519
    assert candidate(n = 60) == 125049738
    assert candidate(n = 40) == 965722612
    assert candidate(n = 4) == 4
    assert candidate(n = 37) == 546040181
    assert candidate(n = 98) == 892915734
    assert candidate(n = 73) == 78238453
    assert candidate(n = 80) == 405243354
    assert candidate(n = 89) == 673469112
    assert candidate(n = 85) == 430788419
    assert candidate(n = 83) == 913651722
    assert candidate(n = 90) == 448961084


