def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 100) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 2320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 2320: {e}')
    
    total += 1
    try:
        result = candidate(n = 104) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 9: {e}')
    
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
        result = candidate(n = 1000) == 316
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 316: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000) == 975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000) == 975: {e}')
    
    total += 1
    try:
        result = candidate(n = 1010) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010) == 320: {e}')
    
    total += 1
    try:
        result = candidate(n = 8765) == 1888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8765) == 1888: {e}')
    
    total += 1
    try:
        result = candidate(n = 5678) == 1206
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5678) == 1206: {e}')
    
    total += 1
    try:
        result = candidate(n = 5959) == 1297
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5959) == 1297: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111) == 360: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000) == 1661
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000) == 1661: {e}')
    
    total += 1
    try:
        result = candidate(n = 6172) == 1402
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6172) == 1402: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 633
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 633: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 1661
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 1661: {e}')
    
    total += 1
    try:
        result = candidate(n = 8888) == 1920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8888) == 1920: {e}')
    
    total += 1
    try:
        result = candidate(n = 3333) == 975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3333) == 975: {e}')
    
    total += 1
    try:
        result = candidate(n = 2525) == 797
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2525) == 797: {e}')
    
    total += 1
    try:
        result = candidate(n = 6969) == 1647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6969) == 1647: {e}')
    
    total += 1
    try:
        result = candidate(n = 3500) == 975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3500) == 975: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 129: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 975: {e}')
    
    total += 1
    try:
        result = candidate(n = 3456) == 975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3456) == 975: {e}')
    
    total += 1
    try:
        result = candidate(n = 6789) == 1563
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6789) == 1563: {e}')
    
    total += 1
    try:
        result = candidate(n = 6666) == 1547
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6666) == 1547: {e}')
    
    total += 1
    try:
        result = candidate(n = 9652) == 2197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9652) == 2197: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 327
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 327: {e}')
    
    total += 1
    try:
        result = candidate(n = 2020) == 647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2020) == 647: {e}')
    
    total += 1
    try:
        result = candidate(n = 789) == 227
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789) == 227: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 316
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 316: {e}')
    
    total += 1
    try:
        result = candidate(n = 5555) == 1147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5555) == 1147: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000) == 1661
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000) == 1661: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 976
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 976: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 2320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 2320: {e}')
    
    total += 1
    try:
        result = candidate(n = 4444) == 975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4444) == 975: {e}')
    
    total += 1
    try:
        result = candidate(n = 7890) == 1661
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7890) == 1661: {e}')
    
    total += 1
    try:
        result = candidate(n = 6174) == 1402
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6174) == 1402: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321) == 975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321) == 975: {e}')
    
    total += 1
    try:
        result = candidate(n = 7654) == 1661
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7654) == 1661: {e}')
    
    total += 1
    try:
        result = candidate(n = 7777) == 1661
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7777) == 1661: {e}')
    
    total += 1
    try:
        result = candidate(n = 2222) == 747
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222) == 747: {e}')
    
    total += 1
    try:
        result = candidate(n = 8080) == 1690
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8080) == 1690: {e}')
    
    total += 1
    try:
        result = candidate(n = 9265) == 2107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9265) == 2107: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 780
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 780: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000) == 1978
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000) == 1978: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 417
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 417: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 227
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 227: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000) == 1319
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000) == 1319: {e}')
    
    total += 1
    try:
        result = candidate(n = 2569) == 814
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2569) == 814: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 130: {e}')
    
    total += 1
    try:
        result = candidate(n = 9090) == 2020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9090) == 2020: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 100) == 40
    assert candidate(n = 10000) == 2320
    assert candidate(n = 104) == 41
    assert candidate(n = 20) == 9
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 0
    assert candidate(n = 1000) == 316
    assert candidate(n = 10) == 4
    assert candidate(n = 50) == 16
    assert candidate(n = 4000) == 975
    assert candidate(n = 1010) == 320
    assert candidate(n = 8765) == 1888
    assert candidate(n = 5678) == 1206
    assert candidate(n = 5959) == 1297
    assert candidate(n = 1111) == 360
    assert candidate(n = 7000) == 1661
    assert candidate(n = 6172) == 1402
    assert candidate(n = 2000) == 633
    assert candidate(n = 7500) == 1661
    assert candidate(n = 8888) == 1920
    assert candidate(n = 3333) == 975
    assert candidate(n = 2525) == 797
    assert candidate(n = 6969) == 1647
    assert candidate(n = 3500) == 975
    assert candidate(n = 300) == 129
    assert candidate(n = 3000) == 975
    assert candidate(n = 3456) == 975
    assert candidate(n = 6789) == 1563
    assert candidate(n = 6666) == 1547
    assert candidate(n = 9652) == 2197
    assert candidate(n = 1024) == 327
    assert candidate(n = 2020) == 647
    assert candidate(n = 789) == 227
    assert candidate(n = 999) == 316
    assert candidate(n = 5555) == 1147
    assert candidate(n = 8000) == 1661
    assert candidate(n = 5000) == 976
    assert candidate(n = 9999) == 2320
    assert candidate(n = 4444) == 975
    assert candidate(n = 7890) == 1661
    assert candidate(n = 6174) == 1402
    assert candidate(n = 4321) == 975
    assert candidate(n = 7654) == 1661
    assert candidate(n = 7777) == 1661
    assert candidate(n = 2222) == 747
    assert candidate(n = 8080) == 1690
    assert candidate(n = 9265) == 2107
    assert candidate(n = 2500) == 780
    assert candidate(n = 9000) == 1978
    assert candidate(n = 1234) == 417
    assert candidate(n = 750) == 227
    assert candidate(n = 6000) == 1319
    assert candidate(n = 2569) == 814
    assert candidate(n = 500) == 130
    assert candidate(n = 9090) == 2020


