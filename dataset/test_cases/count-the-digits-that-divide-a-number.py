def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 111111111) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111111) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 666) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 666) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 999) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 222) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 1122) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1122) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 4488) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4488) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 444) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 444) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 555) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 1248) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1248) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 13579) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 13579) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 888) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 333) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 2222) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2222) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 121) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 121) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 111) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 777) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 2244) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2244) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 357) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 357) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 3366) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3366) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222222) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222222) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 369125874) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 369125874) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 555666777) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555666777) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 975318642) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 975318642) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111111) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111111) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 222333444555666777888999) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222333444555666777888999) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 32481632) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 32481632) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 889977) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 889977) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 777777777) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777777777) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 1357913579) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1357913579) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 199919991) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199919991) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 248163264128) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 248163264128) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 666666666) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 666666666) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 135792468) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 135792468) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 222444666) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222444666) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 333333333) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333333333) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 595959) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 595959) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 1352468) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1352468) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 272727272) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 272727272) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 135791357) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 135791357) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 363636363) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 363636363) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 31313) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 31313) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 333666999) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333666999) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555555555555) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555555555555) == 18: {e}')
    
    total += 1
    try:
        result = candidate(num = 333366669999) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333366669999) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 7654321) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7654321) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 82436) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 82436) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 135) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 135) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 488848884) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 488848884) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 363636) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 363636) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 1122334455) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1122334455) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 478915) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 478915) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 246813579) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 246813579) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 24682468) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 24682468) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 864213579) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 864213579) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 333999) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333999) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 1133557799) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1133557799) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 369258147) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 369258147) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 111222333444555666777888999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111222333444555666777888999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 899999999) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 899999999) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 29876) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 29876) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 468297351) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 468297351) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 56324) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 56324) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 199199199) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199199199) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 975319753) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 975319753) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 112233) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 112233) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 112233445566778899) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 112233445566778899) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 111111111) == 9
    assert candidate(num = 666) == 3
    assert candidate(num = 999) == 3
    assert candidate(num = 222) == 3
    assert candidate(num = 1122) == 4
    assert candidate(num = 123456789) == 3
    assert candidate(num = 4488) == 4
    assert candidate(num = 444) == 3
    assert candidate(num = 555) == 3
    assert candidate(num = 1248) == 4
    assert candidate(num = 13579) == 1
    assert candidate(num = 888) == 3
    assert candidate(num = 333) == 3
    assert candidate(num = 2222) == 4
    assert candidate(num = 987654321) == 3
    assert candidate(num = 7) == 1
    assert candidate(num = 1111) == 4
    assert candidate(num = 121) == 2
    assert candidate(num = 111) == 3
    assert candidate(num = 777) == 3
    assert candidate(num = 2244) == 4
    assert candidate(num = 357) == 2
    assert candidate(num = 3366) == 4
    assert candidate(num = 222222222) == 9
    assert candidate(num = 369125874) == 5
    assert candidate(num = 555666777) == 0
    assert candidate(num = 555555555) == 9
    assert candidate(num = 888888888) == 9
    assert candidate(num = 975318642) == 5
    assert candidate(num = 1111111111) == 10
    assert candidate(num = 222333444555666777888999) == 3
    assert candidate(num = 32481632) == 5
    assert candidate(num = 889977) == 0
    assert candidate(num = 777777777) == 9
    assert candidate(num = 1357913579) == 2
    assert candidate(num = 199919991) == 3
    assert candidate(num = 248163264128) == 9
    assert candidate(num = 111222333) == 6
    assert candidate(num = 666666666) == 9
    assert candidate(num = 135792468) == 7
    assert candidate(num = 222444666) == 6
    assert candidate(num = 333333333) == 9
    assert candidate(num = 595959) == 0
    assert candidate(num = 1352468) == 3
    assert candidate(num = 272727272) == 5
    assert candidate(num = 135791357) == 2
    assert candidate(num = 363636363) == 5
    assert candidate(num = 31313) == 2
    assert candidate(num = 333666999) == 6
    assert candidate(num = 555555555555555555) == 18
    assert candidate(num = 333366669999) == 8
    assert candidate(num = 7654321) == 1
    assert candidate(num = 82436) == 2
    assert candidate(num = 135) == 3
    assert candidate(num = 488848884) == 3
    assert candidate(num = 363636) == 6
    assert candidate(num = 1122334455) == 6
    assert candidate(num = 478915) == 2
    assert candidate(num = 246813579) == 3
    assert candidate(num = 24682468) == 4
    assert candidate(num = 864213579) == 3
    assert candidate(num = 333999) == 6
    assert candidate(num = 1133557799) == 2
    assert candidate(num = 369258147) == 3
    assert candidate(num = 111222333444555666777888999) == 9
    assert candidate(num = 899999999) == 0
    assert candidate(num = 29876) == 2
    assert candidate(num = 468297351) == 3
    assert candidate(num = 56324) == 2
    assert candidate(num = 199199199) == 3
    assert candidate(num = 975319753) == 1
    assert candidate(num = 112233) == 4
    assert candidate(num = 112233445566778899) == 6


