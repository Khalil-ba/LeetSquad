def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 625) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 97: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 144) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 144) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 841) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 841) == 58: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 600) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 72) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 343) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 343) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 225) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 819) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 819) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 46: {e}')
    
    total += 1
    try:
        result = candidate(n = 96) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 96) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 997) == 997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 997) == 997: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 529) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 529) == 46: {e}')
    
    total += 1
    try:
        result = candidate(n = 91) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 91) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 77) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 48) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 961) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 961) == 62: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 196) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 196) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 121) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 121) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 361) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 361) == 38: {e}')
    
    total += 1
    try:
        result = candidate(n = 441) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 441) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 3
    assert candidate(n = 12) == 7
    assert candidate(n = 100) == 14
    assert candidate(n = 10) == 7
    assert candidate(n = 1000) == 21
    assert candidate(n = 5) == 5
    assert candidate(n = 4) == 4
    assert candidate(n = 16) == 8
    assert candidate(n = 17) == 17
    assert candidate(n = 2) == 2
    assert candidate(n = 8) == 6
    assert candidate(n = 27) == 9
    assert candidate(n = 18) == 8
    assert candidate(n = 20) == 9
    assert candidate(n = 19) == 19
    assert candidate(n = 11) == 11
    assert candidate(n = 15) == 8
    assert candidate(n = 14) == 9
    assert candidate(n = 9) == 6
    assert candidate(n = 6) == 5
    assert candidate(n = 1) == 0
    assert candidate(n = 7) == 7
    assert candidate(n = 13) == 13
    assert candidate(n = 625) == 20
    assert candidate(n = 97) == 97
    assert candidate(n = 729) == 18
    assert candidate(n = 144) == 14
    assert candidate(n = 49) == 14
    assert candidate(n = 125) == 15
    assert candidate(n = 4096) == 24
    assert candidate(n = 300) == 17
    assert candidate(n = 841) == 58
    assert candidate(n = 60) == 12
    assert candidate(n = 30) == 10
    assert candidate(n = 600) == 19
    assert candidate(n = 64) == 12
    assert candidate(n = 72) == 12
    assert candidate(n = 99) == 17
    assert candidate(n = 343) == 21
    assert candidate(n = 225) == 16
    assert candidate(n = 819) == 26
    assert candidate(n = 1024) == 20
    assert candidate(n = 128) == 14
    assert candidate(n = 999) == 46
    assert candidate(n = 96) == 13
    assert candidate(n = 256) == 16
    assert candidate(n = 997) == 997
    assert candidate(n = 36) == 10
    assert candidate(n = 529) == 46
    assert candidate(n = 91) == 20
    assert candidate(n = 77) == 18
    assert candidate(n = 81) == 12
    assert candidate(n = 48) == 11
    assert candidate(n = 961) == 62
    assert candidate(n = 200) == 16
    assert candidate(n = 400) == 18
    assert candidate(n = 512) == 18
    assert candidate(n = 196) == 18
    assert candidate(n = 750) == 20
    assert candidate(n = 121) == 22
    assert candidate(n = 361) == 38
    assert candidate(n = 441) == 20
    assert candidate(n = 500) == 19
    assert candidate(n = 55) == 16
    assert candidate(n = 25) == 10


