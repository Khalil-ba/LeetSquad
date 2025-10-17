def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(n = 1804289383) == 60070
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1804289383) == 60070: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 180) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 210) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 210) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 171) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 171) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 576) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 576) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483646) == 65535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483646) == 65535: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 70) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 140: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 165) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 165) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 6678) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6678) == 115: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 446
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 446: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 44720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 44720: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999) == 62: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 44443
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 44443: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000000) == 3161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000000) == 3161: {e}')
    
    total += 1
    try:
        result = candidate(n = 325) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 325) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 441) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 441) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 136) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 136) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 31622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 31622: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 1413
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 1413: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 15712
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 15712: {e}')
    
    total += 1
    try:
        result = candidate(n = 120) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999999) == 63245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999999) == 63245: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 496: {e}')
    
    total += 1
    try:
        result = candidate(n = 5050) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5050) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 84) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84) == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 3
    assert candidate(n = 100) == 13
    assert candidate(n = 30) == 7
    assert candidate(n = 15) == 5
    assert candidate(n = 22) == 6
    assert candidate(n = 21) == 6
    assert candidate(n = 2147483647) == 65535
    assert candidate(n = 1804289383) == 60070
    assert candidate(n = 1) == 1
    assert candidate(n = 180) == 18
    assert candidate(n = 10) == 4
    assert candidate(n = 5) == 2
    assert candidate(n = 210) == 20
    assert candidate(n = 45) == 9
    assert candidate(n = 171) == 18
    assert candidate(n = 3) == 2
    assert candidate(n = 576) == 33
    assert candidate(n = 2147483646) == 65535
    assert candidate(n = 12) == 4
    assert candidate(n = 7) == 3
    assert candidate(n = 70) == 11
    assert candidate(n = 1000) == 44
    assert candidate(n = 28) == 7
    assert candidate(n = 64) == 10
    assert candidate(n = 16) == 5
    assert candidate(n = 10000) == 140
    assert candidate(n = 1001) == 44
    assert candidate(n = 2) == 1
    assert candidate(n = 80) == 12
    assert candidate(n = 165) == 17
    assert candidate(n = 6678) == 115
    assert candidate(n = 101) == 13
    assert candidate(n = 100000) == 446
    assert candidate(n = 18) == 5
    assert candidate(n = 256) == 22
    assert candidate(n = 36) == 8
    assert candidate(n = 500) == 31
    assert candidate(n = 1000000000) == 44720
    assert candidate(n = 1999) == 62
    assert candidate(n = 987654321) == 44443
    assert candidate(n = 5000000) == 3161
    assert candidate(n = 325) == 25
    assert candidate(n = 441) == 29
    assert candidate(n = 136) == 16
    assert candidate(n = 500000000) == 31622
    assert candidate(n = 1000000) == 1413
    assert candidate(n = 6) == 3
    assert candidate(n = 123456789) == 15712
    assert candidate(n = 120) == 15
    assert candidate(n = 1999999999) == 63245
    assert candidate(n = 123456) == 496
    assert candidate(n = 5050) == 100
    assert candidate(n = 55) == 10
    assert candidate(n = 84) == 12


