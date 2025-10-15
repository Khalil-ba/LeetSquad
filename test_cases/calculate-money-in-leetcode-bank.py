def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 30) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 165: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 96: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 74926
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 74926: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 159: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 504: {e}')
    
    total += 1
    try:
        result = candidate(n = 210) == 3885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 210) == 3885: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 343
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 343: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 1551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 1551: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == 105: {e}')
    
    total += 1
    try:
        result = candidate(n = 70) == 595
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70) == 595: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 1060
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 1060: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 351: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 7476
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 7476: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 154: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 462: {e}')
    
    total += 1
    try:
        result = candidate(n = 56) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56) == 420: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 250: {e}')
    
    total += 1
    try:
        result = candidate(n = 600) == 27810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600) == 27810: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 1044
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 1044: {e}')
    
    total += 1
    try:
        result = candidate(n = 98) == 1029
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98) == 1029: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 365) == 10791
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 365) == 10791: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == 732
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == 732: {e}')
    
    total += 1
    try:
        result = candidate(n = 700) == 37450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700) == 37450: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 5335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 5335: {e}')
    
    total += 1
    try:
        result = candidate(n = 777) == 45843
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777) == 45843: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 74778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 74778: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 109: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 140) == 1890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 140) == 1890: {e}')
    
    total += 1
    try:
        result = candidate(n = 91) == 910
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 91) == 910: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 2127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 2127: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 180) == 2940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180) == 2940: {e}')
    
    total += 1
    try:
        result = candidate(n = 899) == 60870
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 899) == 60870: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == 811
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == 811: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 3552
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 3552: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 63: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 12826
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 12826: {e}')
    
    total += 1
    try:
        result = candidate(n = 120) == 1446
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120) == 1446: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 19602
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 19602: {e}')
    
    total += 1
    try:
        result = candidate(n = 52) == 370
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 52) == 370: {e}')
    
    total += 1
    try:
        result = candidate(n = 90) == 891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90) == 891: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 127: {e}')
    
    total += 1
    try:
        result = candidate(n = 84) == 798
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84) == 798: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 30) == 165
    assert candidate(n = 4) == 10
    assert candidate(n = 20) == 96
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 74926
    assert candidate(n = 7) == 28
    assert candidate(n = 10) == 37
    assert candidate(n = 29) == 159
    assert candidate(n = 63) == 504
    assert candidate(n = 210) == 3885
    assert candidate(n = 49) == 343
    assert candidate(n = 125) == 1551
    assert candidate(n = 21) == 105
    assert candidate(n = 70) == 595
    assert candidate(n = 100) == 1060
    assert candidate(n = 50) == 351
    assert candidate(n = 300) == 7476
    assert candidate(n = 28) == 154
    assert candidate(n = 60) == 462
    assert candidate(n = 56) == 420
    assert candidate(n = 40) == 250
    assert candidate(n = 600) == 27810
    assert candidate(n = 99) == 1044
    assert candidate(n = 98) == 1029
    assert candidate(n = 2) == 3
    assert candidate(n = 365) == 10791
    assert candidate(n = 80) == 732
    assert candidate(n = 700) == 37450
    assert candidate(n = 8) == 30
    assert candidate(n = 250) == 5335
    assert candidate(n = 777) == 45843
    assert candidate(n = 999) == 74778
    assert candidate(n = 22) == 109
    assert candidate(n = 35) == 210
    assert candidate(n = 140) == 1890
    assert candidate(n = 91) == 910
    assert candidate(n = 150) == 2127
    assert candidate(n = 15) == 66
    assert candidate(n = 180) == 2940
    assert candidate(n = 899) == 60870
    assert candidate(n = 85) == 811
    assert candidate(n = 200) == 3552
    assert candidate(n = 14) == 63
    assert candidate(n = 400) == 12826
    assert candidate(n = 120) == 1446
    assert candidate(n = 500) == 19602
    assert candidate(n = 52) == 370
    assert candidate(n = 90) == 891
    assert candidate(n = 25) == 127
    assert candidate(n = 84) == 798


