def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 5,rollMax = [2, 2, 2, 2, 2, 2]) == 7200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,rollMax = [2, 2, 2, 2, 2, 2]) == 7200: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,rollMax = [1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,rollMax = [1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,rollMax = [15, 15, 15, 15, 15, 15]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,rollMax = [15, 15, 15, 15, 15, 15]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,rollMax = [2, 3, 4, 5, 6, 7]) == 58240426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,rollMax = [2, 3, 4, 5, 6, 7]) == 58240426: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,rollMax = [1, 1, 2, 2, 2, 3]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,rollMax = [1, 1, 2, 2, 2, 3]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,rollMax = [1, 1, 1, 1, 1, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,rollMax = [1, 1, 1, 1, 1, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,rollMax = [1, 2, 3, 4, 5, 6]) == 6919
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,rollMax = [1, 2, 3, 4, 5, 6]) == 6919: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,rollMax = [1, 1, 1, 1, 1, 1]) == 3750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,rollMax = [1, 1, 1, 1, 1, 1]) == 3750: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,rollMax = [1, 2, 3, 4, 5, 6]) == 1188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,rollMax = [1, 2, 3, 4, 5, 6]) == 1188: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,rollMax = [1, 1, 1, 2, 2, 3]) == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,rollMax = [1, 1, 1, 2, 2, 3]) == 181: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,rollMax = [5, 5, 5, 5, 5, 5]) == 808684040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,rollMax = [5, 5, 5, 5, 5, 5]) == 808684040: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,rollMax = [1, 1, 1, 15, 1, 15]) == 728503686
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,rollMax = [1, 1, 1, 15, 1, 15]) == 728503686: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,rollMax = [1, 2, 2, 3, 3, 4]) == 917820088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,rollMax = [1, 2, 2, 3, 3, 4]) == 917820088: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,rollMax = [3, 3, 3, 3, 3, 3]) == 197968606
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,rollMax = [3, 3, 3, 3, 3, 3]) == 197968606: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,rollMax = [15, 14, 13, 12, 11, 10]) == 470351288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,rollMax = [15, 14, 13, 12, 11, 10]) == 470351288: {e}')
    
    total += 1
    try:
        result = candidate(n = 350,rollMax = [2, 3, 4, 5, 6, 7]) == 326686679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 350,rollMax = [2, 3, 4, 5, 6, 7]) == 326686679: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,rollMax = [5, 5, 5, 5, 5, 5]) == 505697887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,rollMax = [5, 5, 5, 5, 5, 5]) == 505697887: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,rollMax = [1, 1, 2, 2, 3, 3]) == 758892805
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,rollMax = [1, 1, 2, 2, 3, 3]) == 758892805: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,rollMax = [3, 2, 1, 2, 3, 4]) == 1176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,rollMax = [3, 2, 1, 2, 3, 4]) == 1176: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,rollMax = [5, 5, 5, 5, 5, 5]) == 488934088
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,rollMax = [5, 5, 5, 5, 5, 5]) == 488934088: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,rollMax = [1, 1, 1, 2, 3, 4]) == 27915907
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,rollMax = [1, 1, 1, 2, 3, 4]) == 27915907: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,rollMax = [2, 3, 4, 5, 6, 7]) == 197242731
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,rollMax = [2, 3, 4, 5, 6, 7]) == 197242731: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,rollMax = [2, 3, 1, 1, 4, 5]) == 36308544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,rollMax = [2, 3, 1, 1, 4, 5]) == 36308544: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,rollMax = [3, 4, 5, 6, 7, 8]) == 753899520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,rollMax = [3, 4, 5, 6, 7, 8]) == 753899520: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,rollMax = [1, 2, 1, 2, 1, 2]) == 987298539
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,rollMax = [1, 2, 1, 2, 1, 2]) == 987298539: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,rollMax = [2, 3, 4, 5, 6, 7]) == 221148447
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,rollMax = [2, 3, 4, 5, 6, 7]) == 221148447: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,rollMax = [1, 2, 1, 2, 1, 2]) == 825497499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,rollMax = [1, 2, 1, 2, 1, 2]) == 825497499: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,rollMax = [1, 2, 3, 4, 5, 15]) == 992520282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,rollMax = [1, 2, 3, 4, 5, 15]) == 992520282: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,rollMax = [2, 2, 2, 2, 2, 2]) == 818530237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,rollMax = [2, 2, 2, 2, 2, 2]) == 818530237: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,rollMax = [1, 1, 1, 1, 1, 1]) == 11718750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,rollMax = [1, 1, 1, 1, 1, 1]) == 11718750: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,rollMax = [10, 10, 10, 10, 10, 10]) == 568370197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,rollMax = [10, 10, 10, 10, 10, 10]) == 568370197: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,rollMax = [1, 2, 1, 2, 1, 2]) == 679107530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,rollMax = [1, 2, 1, 2, 1, 2]) == 679107530: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,rollMax = [1, 1, 2, 2, 3, 3]) == 12398650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,rollMax = [1, 1, 2, 2, 3, 3]) == 12398650: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,rollMax = [1, 1, 1, 1, 1, 1]) == 776377743
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,rollMax = [1, 1, 1, 1, 1, 1]) == 776377743: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,rollMax = [15, 14, 13, 12, 11, 10]) == 379975553
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,rollMax = [15, 14, 13, 12, 11, 10]) == 379975553: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,rollMax = [5, 5, 5, 5, 5, 5]) == 703140572
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,rollMax = [5, 5, 5, 5, 5, 5]) == 703140572: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,rollMax = [1, 1, 2, 2, 3, 3]) == 12398650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,rollMax = [1, 1, 2, 2, 3, 3]) == 12398650: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,rollMax = [2, 3, 4, 5, 6, 7]) == 412603689
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,rollMax = [2, 3, 4, 5, 6, 7]) == 412603689: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,rollMax = [4, 4, 4, 4, 4, 4]) == 418009264
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,rollMax = [4, 4, 4, 4, 4, 4]) == 418009264: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,rollMax = [7, 6, 5, 4, 3, 2]) == 3950632
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,rollMax = [7, 6, 5, 4, 3, 2]) == 3950632: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,rollMax = [3, 1, 2, 4, 1, 3]) == 255974937
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,rollMax = [3, 1, 2, 4, 1, 3]) == 255974937: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 5,rollMax = [2, 2, 2, 2, 2, 2]) == 7200
    assert candidate(n = 1,rollMax = [1, 1, 1, 1, 1, 1]) == 6
    assert candidate(n = 1,rollMax = [15, 15, 15, 15, 15, 15]) == 6
    assert candidate(n = 10,rollMax = [2, 3, 4, 5, 6, 7]) == 58240426
    assert candidate(n = 2,rollMax = [1, 1, 2, 2, 2, 3]) == 34
    assert candidate(n = 2,rollMax = [1, 1, 1, 1, 1, 1]) == 30
    assert candidate(n = 5,rollMax = [1, 2, 3, 4, 5, 6]) == 6919
    assert candidate(n = 5,rollMax = [1, 1, 1, 1, 1, 1]) == 3750
    assert candidate(n = 4,rollMax = [1, 2, 3, 4, 5, 6]) == 1188
    assert candidate(n = 3,rollMax = [1, 1, 1, 2, 2, 3]) == 181
    assert candidate(n = 50,rollMax = [5, 5, 5, 5, 5, 5]) == 808684040
    assert candidate(n = 300,rollMax = [1, 1, 1, 15, 1, 15]) == 728503686
    assert candidate(n = 150,rollMax = [1, 2, 2, 3, 3, 4]) == 917820088
    assert candidate(n = 300,rollMax = [3, 3, 3, 3, 3, 3]) == 197968606
    assert candidate(n = 25,rollMax = [15, 14, 13, 12, 11, 10]) == 470351288
    assert candidate(n = 350,rollMax = [2, 3, 4, 5, 6, 7]) == 326686679
    assert candidate(n = 100,rollMax = [5, 5, 5, 5, 5, 5]) == 505697887
    assert candidate(n = 15,rollMax = [1, 1, 2, 2, 3, 3]) == 758892805
    assert candidate(n = 4,rollMax = [3, 2, 1, 2, 3, 4]) == 1176
    assert candidate(n = 150,rollMax = [5, 5, 5, 5, 5, 5]) == 488934088
    assert candidate(n = 10,rollMax = [1, 1, 1, 2, 3, 4]) == 27915907
    assert candidate(n = 50,rollMax = [2, 3, 4, 5, 6, 7]) == 197242731
    assert candidate(n = 10,rollMax = [2, 3, 1, 1, 4, 5]) == 36308544
    assert candidate(n = 50,rollMax = [3, 4, 5, 6, 7, 8]) == 753899520
    assert candidate(n = 400,rollMax = [1, 2, 1, 2, 1, 2]) == 987298539
    assert candidate(n = 200,rollMax = [2, 3, 4, 5, 6, 7]) == 221148447
    assert candidate(n = 50,rollMax = [1, 2, 1, 2, 1, 2]) == 825497499
    assert candidate(n = 50,rollMax = [1, 2, 3, 4, 5, 15]) == 992520282
    assert candidate(n = 200,rollMax = [2, 2, 2, 2, 2, 2]) == 818530237
    assert candidate(n = 10,rollMax = [1, 1, 1, 1, 1, 1]) == 11718750
    assert candidate(n = 100,rollMax = [10, 10, 10, 10, 10, 10]) == 568370197
    assert candidate(n = 30,rollMax = [1, 2, 1, 2, 1, 2]) == 679107530
    assert candidate(n = 100,rollMax = [1, 1, 2, 2, 3, 3]) == 12398650
    assert candidate(n = 100,rollMax = [1, 1, 1, 1, 1, 1]) == 776377743
    assert candidate(n = 400,rollMax = [15, 14, 13, 12, 11, 10]) == 379975553
    assert candidate(n = 20,rollMax = [5, 5, 5, 5, 5, 5]) == 703140572
    assert candidate(n = 100,rollMax = [1, 1, 2, 2, 3, 3]) == 12398650
    assert candidate(n = 20,rollMax = [2, 3, 4, 5, 6, 7]) == 412603689
    assert candidate(n = 400,rollMax = [4, 4, 4, 4, 4, 4]) == 418009264
    assert candidate(n = 150,rollMax = [7, 6, 5, 4, 3, 2]) == 3950632
    assert candidate(n = 40,rollMax = [3, 1, 2, 4, 1, 3]) == 255974937


