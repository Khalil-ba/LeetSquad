def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 100) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 400: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 952
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 952: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 692
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 692: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 130) == 585
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 130) == 585: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 560: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 110) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 110) == 460: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 172: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 214: {e}')
    
    total += 1
    try:
        result = candidate(n = 155) == 718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 155) == 718: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 79: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 119: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == 295: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 274: {e}')
    
    total += 1
    try:
        result = candidate(n = 140) == 635
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 140) == 635: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 120) == 529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120) == 529: {e}')
    
    total += 1
    try:
        result = candidate(n = 160) == 743
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 160) == 743: {e}')
    
    total += 1
    try:
        result = candidate(n = 199) == 946
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199) == 946: {e}')
    
    total += 1
    try:
        result = candidate(n = 180) == 843
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180) == 843: {e}')
    
    total += 1
    try:
        result = candidate(n = 90) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90) == 345: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 100) == 400
    assert candidate(n = 15) == 30
    assert candidate(n = 200) == 952
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 0
    assert candidate(n = 10) == 16
    assert candidate(n = 5) == 6
    assert candidate(n = 150) == 692
    assert candidate(n = 3) == 2
    assert candidate(n = 130) == 585
    assert candidate(n = 125) == 560
    assert candidate(n = 12) == 21
    assert candidate(n = 110) == 460
    assert candidate(n = 50) == 172
    assert candidate(n = 60) == 214
    assert candidate(n = 155) == 718
    assert candidate(n = 30) == 79
    assert candidate(n = 40) == 119
    assert candidate(n = 4) == 4
    assert candidate(n = 80) == 295
    assert candidate(n = 75) == 274
    assert candidate(n = 140) == 635
    assert candidate(n = 18) == 42
    assert candidate(n = 120) == 529
    assert candidate(n = 160) == 743
    assert candidate(n = 199) == 946
    assert candidate(n = 180) == 843
    assert candidate(n = 90) == 345


