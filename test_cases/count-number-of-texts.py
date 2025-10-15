def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(pressedKeys = "99999999") == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "99999999") == 108: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "3333") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "3333") == 7: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "33") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "33") == 2: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "4444") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "4444") == 7: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "555555") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "555555") == 24: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "9999999") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "9999999") == 56: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "888888888") == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "888888888") == 149: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "888888") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "888888") == 24: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "7777777") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "7777777") == 56: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "66") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "66") == 2: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "55555") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "55555") == 13: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "888") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "888") == 4: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "33344455566677778889999") == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "33344455566677778889999") == 65536: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "2222") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "2222") == 7: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "7777") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "7777") == 8: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "77777777") == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "77777777") == 108: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "8888") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "8888") == 7: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "6666666") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "6666666") == 44: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "23456789") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "23456789") == 1: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "666") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "666") == 4: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "22233") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "22233") == 8: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "555") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "555") == 4: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "9999999999") == 401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "9999999999") == 401: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "44444") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "44444") == 13: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "333333") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "333333") == 24: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "99999") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "99999") == 15: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "88888") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "88888") == 13: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "222222222222222222222222222222222222") == 82876089
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "222222222222222222222222222222222222") == 82876089: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "9999888777666555444333222111") == 524288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "9999888777666555444333222111") == 524288: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "777777777777777777777777777777777777") == 312882411
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "777777777777777777777777777777777777") == 312882411: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "2222222222222222222222222222222222227777777777777777777777777777777") == 168766023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "2222222222222222222222222222222222227777777777777777777777777777777") == 168766023: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "2223333333333333333333333333333333334444444444444444444444444444444") == 151530826
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "2223333333333333333333333333333333334444444444444444444444444444444") == 151530826: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "234567898765432345678987654323456789876543234567898765432") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "234567898765432345678987654323456789876543234567898765432") == 1: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "7773333322225555555555444446666688888") == 219119992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "7773333322225555555555444446666688888") == 219119992: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "222222222222222222222222222222222222444444444444444444444444444") == 964547839
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "222222222222222222222222222222222222444444444444444444444444444") == 964547839: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "9999999999999999999999999999999999999999999999999999999999999999999") == 831813694
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "9999999999999999999999999999999999999999999999999999999999999999999") == 831813694: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "55555555555555555555555555555555555577777777777777777777777777777778888888888888888888888888888888") == 60492310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "55555555555555555555555555555555555577777777777777777777777777777778888888888888888888888888888888") == 60492310: {e}')
    
    total += 1
    try:
        result = candidate(pressedKeys = "333322225555444466668888") == 117649
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pressedKeys = "333322225555444466668888") == 117649: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(pressedKeys = "99999999") == 108
    assert candidate(pressedKeys = "3333") == 7
    assert candidate(pressedKeys = "33") == 2
    assert candidate(pressedKeys = "4444") == 7
    assert candidate(pressedKeys = "555555") == 24
    assert candidate(pressedKeys = "9999999") == 56
    assert candidate(pressedKeys = "888888888") == 149
    assert candidate(pressedKeys = "888888") == 24
    assert candidate(pressedKeys = "7777777") == 56
    assert candidate(pressedKeys = "66") == 2
    assert candidate(pressedKeys = "55555") == 13
    assert candidate(pressedKeys = "888") == 4
    assert candidate(pressedKeys = "33344455566677778889999") == 65536
    assert candidate(pressedKeys = "2222") == 7
    assert candidate(pressedKeys = "7777") == 8
    assert candidate(pressedKeys = "77777777") == 108
    assert candidate(pressedKeys = "8888") == 7
    assert candidate(pressedKeys = "6666666") == 44
    assert candidate(pressedKeys = "23456789") == 1
    assert candidate(pressedKeys = "666") == 4
    assert candidate(pressedKeys = "22233") == 8
    assert candidate(pressedKeys = "555") == 4
    assert candidate(pressedKeys = "9999999999") == 401
    assert candidate(pressedKeys = "44444") == 13
    assert candidate(pressedKeys = "333333") == 24
    assert candidate(pressedKeys = "99999") == 15
    assert candidate(pressedKeys = "88888") == 13
    assert candidate(pressedKeys = "222222222222222222222222222222222222") == 82876089
    assert candidate(pressedKeys = "9999888777666555444333222111") == 524288
    assert candidate(pressedKeys = "777777777777777777777777777777777777") == 312882411
    assert candidate(pressedKeys = "2222222222222222222222222222222222227777777777777777777777777777777") == 168766023
    assert candidate(pressedKeys = "2223333333333333333333333333333333334444444444444444444444444444444") == 151530826
    assert candidate(pressedKeys = "234567898765432345678987654323456789876543234567898765432") == 1
    assert candidate(pressedKeys = "7773333322225555555555444446666688888") == 219119992
    assert candidate(pressedKeys = "222222222222222222222222222222222222444444444444444444444444444") == 964547839
    assert candidate(pressedKeys = "9999999999999999999999999999999999999999999999999999999999999999999") == 831813694
    assert candidate(pressedKeys = "55555555555555555555555555555555555577777777777777777777777777777778888888888888888888888888888888") == 60492310
    assert candidate(pressedKeys = "333322225555444466668888") == 117649


