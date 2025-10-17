def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1000) == 89945857
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 89945857: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 173981881
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 173981881: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 759959057
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 759959057: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 670333618
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 670333618: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 76428576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 76428576: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 598627501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 598627501: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 793084836
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 793084836: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 1151090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 1151090: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 518032023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 518032023: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 227130014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 227130014: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 1739
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 1739: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 68: {e}')
    
    total += 1
    try:
        result = candidate(n = 15000) == 381635004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15000) == 381635004: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 480007966
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 480007966: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 30000) == 770607143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30000) == 770607143: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 467397509
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 467397509: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 965179800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 965179800: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 129: {e}')
    
    total += 1
    try:
        result = candidate(n = 19999) == 706457669
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19999) == 706457669: {e}')
    
    total += 1
    try:
        result = candidate(n = 19000) == 70562691
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19000) == 70562691: {e}')
    
    total += 1
    try:
        result = candidate(n = 18000) == 596349393
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18000) == 596349393: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 29599477
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 29599477: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1000) == 89945857
    assert candidate(n = 100) == 173981881
    assert candidate(n = 20000) == 759959057
    assert candidate(n = 200) == 670333618
    assert candidate(n = 10000) == 76428576
    assert candidate(n = 5000) == 598627501
    assert candidate(n = 2000) == 793084836
    assert candidate(n = 2) == 10
    assert candidate(n = 20) == 1151090
    assert candidate(n = 1) == 5
    assert candidate(n = 500) == 518032023
    assert candidate(n = 50) == 227130014
    assert candidate(n = 10) == 1739
    assert candidate(n = 5) == 68
    assert candidate(n = 15000) == 381635004
    assert candidate(n = 3) == 19
    assert candidate(n = 12345) == 480007966
    assert candidate(n = 4) == 35
    assert candidate(n = 30000) == 770607143
    assert candidate(n = 75) == 467397509
    assert candidate(n = 150) == 965179800
    assert candidate(n = 6) == 129
    assert candidate(n = 19999) == 706457669
    assert candidate(n = 19000) == 70562691
    assert candidate(n = 18000) == 596349393
    assert candidate(n = 25) == 29599477


