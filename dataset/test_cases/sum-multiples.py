def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 9) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 272066
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 272066: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 210) == 12075
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 210) == 12075: {e}')
    
    total += 1
    try:
        result = candidate(n = 666) == 121023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666) == 121023: {e}')
    
    total += 1
    try:
        result = candidate(n = 315) == 27090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 315) == 27090: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 2838
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 2838: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 691
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 691: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 24321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 24321: {e}')
    
    total += 1
    try:
        result = candidate(n = 333) == 30339
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333) == 30339: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 274: {e}')
    
    total += 1
    try:
        result = candidate(n = 550) == 82614
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550) == 82614: {e}')
    
    total += 1
    try:
        result = candidate(n = 103) == 2940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 103) == 2940: {e}')
    
    total += 1
    try:
        result = candidate(n = 840) == 191940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 840) == 191940: {e}')
    
    total += 1
    try:
        result = candidate(n = 42) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42) == 499: {e}')
    
    total += 1
    try:
        result = candidate(n = 888) == 213532
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888) == 213532: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 2838
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 2838: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 17152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 17152: {e}')
    
    total += 1
    try:
        result = candidate(n = 789) == 169111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789) == 169111: {e}')
    
    total += 1
    try:
        result = candidate(n = 630) == 108045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 630) == 108045: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 271066
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 271066: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 17659
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 17659: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 119: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 6109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 6109: {e}')
    
    total += 1
    try:
        result = candidate(n = 800) == 173877
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800) == 173877: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 81: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 10845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 10845: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == 70927
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == 70927: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 153696
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 153696: {e}')
    
    total += 1
    try:
        result = candidate(n = 120) == 4071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120) == 4071: {e}')
    
    total += 1
    try:
        result = candidate(n = 499) == 67389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499) == 67389: {e}')
    
    total += 1
    try:
        result = candidate(n = 700) == 133342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700) == 133342: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 67889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 67889: {e}')
    
    total += 1
    try:
        result = candidate(n = 420) == 48090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 420) == 48090: {e}')
    
    total += 1
    try:
        result = candidate(n = 84) == 1904
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84) == 1904: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 9) == 30
    assert candidate(n = 1) == 0
    assert candidate(n = 1000) == 272066
    assert candidate(n = 7) == 21
    assert candidate(n = 10) == 40
    assert candidate(n = 210) == 12075
    assert candidate(n = 666) == 121023
    assert candidate(n = 315) == 27090
    assert candidate(n = 100) == 2838
    assert candidate(n = 50) == 691
    assert candidate(n = 300) == 24321
    assert candidate(n = 333) == 30339
    assert candidate(n = 60) == 1024
    assert candidate(n = 30) == 274
    assert candidate(n = 550) == 82614
    assert candidate(n = 103) == 2940
    assert candidate(n = 840) == 191940
    assert candidate(n = 42) == 499
    assert candidate(n = 888) == 213532
    assert candidate(n = 101) == 2838
    assert candidate(n = 250) == 17152
    assert candidate(n = 789) == 169111
    assert candidate(n = 630) == 108045
    assert candidate(n = 999) == 271066
    assert candidate(n = 256) == 17659
    assert candidate(n = 20) == 119
    assert candidate(n = 150) == 6109
    assert candidate(n = 800) == 173877
    assert candidate(n = 15) == 81
    assert candidate(n = 200) == 10845
    assert candidate(n = 512) == 70927
    assert candidate(n = 750) == 153696
    assert candidate(n = 120) == 4071
    assert candidate(n = 499) == 67389
    assert candidate(n = 700) == 133342
    assert candidate(n = 500) == 67889
    assert candidate(n = 420) == 48090
    assert candidate(n = 84) == 1904


