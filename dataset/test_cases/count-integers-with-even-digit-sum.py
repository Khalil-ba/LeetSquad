def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 30) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 30) == 14: {e}')
    
    total += 1
    try:
        result = candidate(num = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 999) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999) == 499: {e}')
    
    total += 1
    try:
        result = candidate(num = 500) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500) == 249: {e}')
    
    total += 1
    try:
        result = candidate(num = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == 49: {e}')
    
    total += 1
    try:
        result = candidate(num = 750) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 750) == 375: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000) == 499: {e}')
    
    total += 1
    try:
        result = candidate(num = 432) == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 432) == 215: {e}')
    
    total += 1
    try:
        result = candidate(num = 666) == 333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 666) == 333: {e}')
    
    total += 1
    try:
        result = candidate(num = 456) == 227
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 456) == 227: {e}')
    
    total += 1
    try:
        result = candidate(num = 250) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 250) == 124: {e}')
    
    total += 1
    try:
        result = candidate(num = 345) == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 345) == 172: {e}')
    
    total += 1
    try:
        result = candidate(num = 99) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99) == 49: {e}')
    
    total += 1
    try:
        result = candidate(num = 222) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222) == 111: {e}')
    
    total += 1
    try:
        result = candidate(num = 200) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 200) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num = 444) == 222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 444) == 222: {e}')
    
    total += 1
    try:
        result = candidate(num = 555) == 277
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555) == 277: {e}')
    
    total += 1
    try:
        result = candidate(num = 888) == 444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888) == 444: {e}')
    
    total += 1
    try:
        result = candidate(num = 123) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123) == 61: {e}')
    
    total += 1
    try:
        result = candidate(num = 789) == 394
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 789) == 394: {e}')
    
    total += 1
    try:
        result = candidate(num = 333) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333) == 166: {e}')
    
    total += 1
    try:
        result = candidate(num = 375) == 187
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 375) == 187: {e}')
    
    total += 1
    try:
        result = candidate(num = 256) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 256) == 127: {e}')
    
    total += 1
    try:
        result = candidate(num = 800) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 800) == 400: {e}')
    
    total += 1
    try:
        result = candidate(num = 678) == 338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 678) == 338: {e}')
    
    total += 1
    try:
        result = candidate(num = 623) == 311
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 623) == 311: {e}')
    
    total += 1
    try:
        result = candidate(num = 600) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 600) == 300: {e}')
    
    total += 1
    try:
        result = candidate(num = 777) == 388
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777) == 388: {e}')
    
    total += 1
    try:
        result = candidate(num = 850) == 424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 850) == 424: {e}')
    
    total += 1
    try:
        result = candidate(num = 899) == 449
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 899) == 449: {e}')
    
    total += 1
    try:
        result = candidate(num = 299) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 299) == 149: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 30) == 14
    assert candidate(num = 10) == 4
    assert candidate(num = 999) == 499
    assert candidate(num = 500) == 249
    assert candidate(num = 4) == 2
    assert candidate(num = 2) == 1
    assert candidate(num = 1) == 0
    assert candidate(num = 100) == 49
    assert candidate(num = 750) == 375
    assert candidate(num = 1000) == 499
    assert candidate(num = 432) == 215
    assert candidate(num = 666) == 333
    assert candidate(num = 456) == 227
    assert candidate(num = 250) == 124
    assert candidate(num = 345) == 172
    assert candidate(num = 99) == 49
    assert candidate(num = 222) == 111
    assert candidate(num = 200) == 100
    assert candidate(num = 444) == 222
    assert candidate(num = 555) == 277
    assert candidate(num = 888) == 444
    assert candidate(num = 123) == 61
    assert candidate(num = 789) == 394
    assert candidate(num = 333) == 166
    assert candidate(num = 375) == 187
    assert candidate(num = 256) == 127
    assert candidate(num = 800) == 400
    assert candidate(num = 678) == 338
    assert candidate(num = 623) == 311
    assert candidate(num = 600) == 300
    assert candidate(num = 777) == 388
    assert candidate(num = 850) == 424
    assert candidate(num = 899) == 449
    assert candidate(num = 299) == 149


