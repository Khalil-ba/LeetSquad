def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 183389504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 183389504: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 944828409
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 944828409: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 381587473
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 381587473: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 102701088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 102701088: {e}')
    
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
        result = candidate(n = 1000) == 37043040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 37043040: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 1334961
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 1334961: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 429456667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 429456667: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 77829876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 77829876: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 14833
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 14833: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 22658429
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 22658429: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 927799753
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 927799753: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 66512367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 66512367: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 243851595
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 243851595: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 133496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 133496: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 265
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 265: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 185559104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 185559104: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 732014705
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 732014705: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 1854
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 1854: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 63529464
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 63529464: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 2
    assert candidate(n = 100000) == 183389504
    assert candidate(n = 100) == 944828409
    assert candidate(n = 4) == 9
    assert candidate(n = 10000) == 381587473
    assert candidate(n = 1000000) == 102701088
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 0
    assert candidate(n = 1000) == 37043040
    assert candidate(n = 10) == 1334961
    assert candidate(n = 5) == 44
    assert candidate(n = 50000) == 429456667
    assert candidate(n = 50) == 77829876
    assert candidate(n = 8) == 14833
    assert candidate(n = 5000) == 22658429
    assert candidate(n = 20) == 927799753
    assert candidate(n = 15) == 66512367
    assert candidate(n = 500000) == 243851595
    assert candidate(n = 9) == 133496
    assert candidate(n = 6) == 265
    assert candidate(n = 999999) == 185559104
    assert candidate(n = 500) == 732014705
    assert candidate(n = 7) == 1854
    assert candidate(n = 25) == 63529464


