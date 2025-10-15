def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 111111111) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111111111) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 47) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 47) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 456789) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 456789) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 38) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 38) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 45) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 45) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 234567890) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 234567890) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 942) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 942) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 123) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 4567) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4567) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 111) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 19) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 19) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 9999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1010101010101010101) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1010101010101010101) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 222222222) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222222222) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890123456789) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890123456789) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 66666666666666666666) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 66666666666666666666) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 9999999999999999999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999999999999999999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111111) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111111) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789012345678901234567890) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789012345678901234567890) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 27) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 27) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 98765432109876543210) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 98765432109876543210) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 444444444) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 444444444) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 2222222222) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2222222222) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 88888888888888888888) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 88888888888888888888) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 33333333333333333333) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33333333333333333333) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 5555555555555555555) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5555555555555555555) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999999999999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999999999999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 777777777) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777777777) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 888888888888888888) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888888888888888888) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 1999999999999999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1999999999999999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 666666666) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 666666666) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543210) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543210) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 555555555555555555555555555555) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555555555555555555555555555555) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 333333333) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333333333) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 11) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 11) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111111111111111111) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111111111111111111) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 4321098765432109876543210987654321) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4321098765432109876543210987654321) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 101010101010101010101010101010) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101010101010101010101010101010) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 543210987654321) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 543210987654321) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 44444444444444444444) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 44444444444444444444) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 94528) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 94528) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 12345678901234567890) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12345678901234567890) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 8888888888888888888) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8888888888888888888) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 18) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 18) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 77777777777777777777) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 77777777777777777777) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321987654321) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321987654321) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 876543210987654321098765432109876543210) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 876543210987654321098765432109876543210) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 4321) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4321) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 22222222222222222222) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 22222222222222222222) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 9876543210987654321) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9876543210987654321) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 369369369) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 369369369) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 898989898989898989898989898989) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 898989898989898989898989898989) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 2222222222222222222) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2222222222222222222) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789123456789) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789123456789) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 9999999999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999999999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 11111111111111111111) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 11111111111111111111) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 55555555555555555555) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 55555555555555555555) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 99999999999999999999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99999999999999999999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 5689423749832749823749237492374923749237492374923749237492374923749237492374) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5689423749832749823749237492374923749237492374923749237492374923749237492374) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 191919191919191919191919191919) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 191919191919191919191919191919) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321098765432109876543210) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321098765432109876543210) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 12345678987654321) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12345678987654321) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 10) == 1
    assert candidate(num = 9) == 9
    assert candidate(num = 111111111) == 9
    assert candidate(num = 47) == 2
    assert candidate(num = 456789) == 3
    assert candidate(num = 38) == 2
    assert candidate(num = 45) == 9
    assert candidate(num = 234567890) == 8
    assert candidate(num = 1000000000) == 1
    assert candidate(num = 942) == 6
    assert candidate(num = 123) == 6
    assert candidate(num = 987654321) == 9
    assert candidate(num = 0) == 0
    assert candidate(num = 4567) == 4
    assert candidate(num = 1) == 1
    assert candidate(num = 111) == 3
    assert candidate(num = 999999999) == 9
    assert candidate(num = 19) == 1
    assert candidate(num = 9999) == 9
    assert candidate(num = 10000) == 1
    assert candidate(num = 1010101010101010101) == 1
    assert candidate(num = 222222222) == 9
    assert candidate(num = 555555555) == 9
    assert candidate(num = 1234567890123456789) == 9
    assert candidate(num = 66666666666666666666) == 3
    assert candidate(num = 9999999999999999999) == 9
    assert candidate(num = 888888888) == 9
    assert candidate(num = 1111111111) == 1
    assert candidate(num = 123456789012345678901234567890) == 9
    assert candidate(num = 27) == 9
    assert candidate(num = 98765432109876543210) == 9
    assert candidate(num = 444444444) == 9
    assert candidate(num = 2222222222) == 2
    assert candidate(num = 88888888888888888888) == 7
    assert candidate(num = 33333333333333333333) == 6
    assert candidate(num = 5555555555555555555) == 5
    assert candidate(num = 999999999999999999) == 9
    assert candidate(num = 777777777) == 9
    assert candidate(num = 888888888888888888) == 9
    assert candidate(num = 1999999999999999999) == 1
    assert candidate(num = 666666666) == 9
    assert candidate(num = 123456789) == 9
    assert candidate(num = 9876543210) == 9
    assert candidate(num = 5) == 5
    assert candidate(num = 555555555555555555555555555555) == 6
    assert candidate(num = 333333333) == 9
    assert candidate(num = 11) == 2
    assert candidate(num = 1111111111111111111) == 1
    assert candidate(num = 4321098765432109876543210987654321) == 1
    assert candidate(num = 1234567890) == 9
    assert candidate(num = 101010101010101010101010101010) == 6
    assert candidate(num = 543210987654321) == 6
    assert candidate(num = 44444444444444444444) == 8
    assert candidate(num = 94528) == 1
    assert candidate(num = 12345678901234567890) == 9
    assert candidate(num = 8888888888888888888) == 8
    assert candidate(num = 18) == 9
    assert candidate(num = 77777777777777777777) == 5
    assert candidate(num = 987654321987654321) == 9
    assert candidate(num = 876543210987654321098765432109876543210) == 9
    assert candidate(num = 4321) == 1
    assert candidate(num = 22222222222222222222) == 4
    assert candidate(num = 9876543210987654321) == 9
    assert candidate(num = 369369369) == 9
    assert candidate(num = 898989898989898989898989898989) == 3
    assert candidate(num = 2222222222222222222) == 2
    assert candidate(num = 123456789123456789) == 9
    assert candidate(num = 9999999999) == 9
    assert candidate(num = 11111111111111111111) == 2
    assert candidate(num = 55555555555555555555) == 1
    assert candidate(num = 99999999999999999999) == 9
    assert candidate(num = 5689423749832749823749237492374923749237492374923749237492374923749237492374) == 2
    assert candidate(num = 191919191919191919191919191919) == 6
    assert candidate(num = 987654321098765432109876543210) == 9
    assert candidate(num = 12345678987654321) == 9


