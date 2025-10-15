def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 31622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 31622: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1089) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1089) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 324) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 324) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 2304) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2304) == 48: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 529) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 529) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 676) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 676) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 32768) == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32768) == 181: {e}')
    
    total += 1
    try:
        result = candidate(n = 1156) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1156) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 576) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 576) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 144) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 144) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 900) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 223
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 223: {e}')
    
    total += 1
    try:
        result = candidate(n = 1681) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1681) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1225) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1225) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 784) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 784) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 2401) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2401) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == 3162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == 3162: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 316
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 316: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 141: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 2025) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2025) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 11111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 11111: {e}')
    
    total += 1
    try:
        result = candidate(n = 121) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 121) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 999: {e}')
    
    total += 1
    try:
        result = candidate(n = 2209) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2209) == 47: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 31622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 31622: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 2116) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2116) == 46: {e}')
    
    total += 1
    try:
        result = candidate(n = 16384) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16384) == 128: {e}')
    
    total += 1
    try:
        result = candidate(n = 289) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 289) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 23456789) == 4843
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23456789) == 4843: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 225) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 1764) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1764) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == 256: {e}')
    
    total += 1
    try:
        result = candidate(n = 1296) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1296) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 31426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 31426: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 707
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 707: {e}')
    
    total += 1
    try:
        result = candidate(n = 961) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 961) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 196) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 196) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 361) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 361) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 625) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 789456) == 888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789456) == 888: {e}')
    
    total += 1
    try:
        result = candidate(n = 1600) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1600) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 1849) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1849) == 43: {e}')
    
    total += 1
    try:
        result = candidate(n = 841) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 841) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 484) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 484) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 1369) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1369) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 1936) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1936) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 1444) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1444) == 38: {e}')
    
    total += 1
    try:
        result = candidate(n = 169) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 169) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 1049) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1049) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 351: {e}')
    
    total += 1
    try:
        result = candidate(n = 441) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 441) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 1521) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1521) == 39: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 3) == 1
    assert candidate(n = 100) == 10
    assert candidate(n = 4) == 2
    assert candidate(n = 16) == 4
    assert candidate(n = 9) == 3
    assert candidate(n = 1000000) == 1000
    assert candidate(n = 1) == 1
    assert candidate(n = 1000000000) == 31622
    assert candidate(n = 1000) == 31
    assert candidate(n = 10) == 3
    assert candidate(n = 25) == 5
    assert candidate(n = 1089) == 33
    assert candidate(n = 729) == 27
    assert candidate(n = 324) == 18
    assert candidate(n = 2304) == 48
    assert candidate(n = 23) == 4
    assert candidate(n = 2048) == 45
    assert candidate(n = 5000) == 70
    assert candidate(n = 36) == 6
    assert candidate(n = 529) == 23
    assert candidate(n = 676) == 26
    assert candidate(n = 2500) == 50
    assert candidate(n = 32768) == 181
    assert candidate(n = 1156) == 34
    assert candidate(n = 100000000) == 10000
    assert candidate(n = 29) == 5
    assert candidate(n = 576) == 24
    assert candidate(n = 144) == 12
    assert candidate(n = 900) == 30
    assert candidate(n = 50000) == 223
    assert candidate(n = 1681) == 41
    assert candidate(n = 17) == 4
    assert candidate(n = 1225) == 35
    assert candidate(n = 784) == 28
    assert candidate(n = 2401) == 49
    assert candidate(n = 10000000) == 3162
    assert candidate(n = 100000) == 316
    assert candidate(n = 20000) == 141
    assert candidate(n = 256) == 16
    assert candidate(n = 2025) == 45
    assert candidate(n = 81) == 9
    assert candidate(n = 123456789) == 11111
    assert candidate(n = 121) == 11
    assert candidate(n = 999999) == 999
    assert candidate(n = 2209) == 47
    assert candidate(n = 999999999) == 31622
    assert candidate(n = 49) == 7
    assert candidate(n = 4096) == 64
    assert candidate(n = 2116) == 46
    assert candidate(n = 16384) == 128
    assert candidate(n = 289) == 17
    assert candidate(n = 23456789) == 4843
    assert candidate(n = 2) == 1
    assert candidate(n = 225) == 15
    assert candidate(n = 8192) == 90
    assert candidate(n = 1764) == 42
    assert candidate(n = 65536) == 256
    assert candidate(n = 1296) == 36
    assert candidate(n = 987654321) == 31426
    assert candidate(n = 15) == 3
    assert candidate(n = 500000) == 707
    assert candidate(n = 961) == 31
    assert candidate(n = 196) == 14
    assert candidate(n = 361) == 19
    assert candidate(n = 13) == 3
    assert candidate(n = 625) == 25
    assert candidate(n = 789456) == 888
    assert candidate(n = 1600) == 40
    assert candidate(n = 1849) == 43
    assert candidate(n = 841) == 29
    assert candidate(n = 64) == 8
    assert candidate(n = 484) == 22
    assert candidate(n = 10000) == 100
    assert candidate(n = 1024) == 32
    assert candidate(n = 1369) == 37
    assert candidate(n = 1936) == 44
    assert candidate(n = 1444) == 38
    assert candidate(n = 169) == 13
    assert candidate(n = 19) == 4
    assert candidate(n = 400) == 20
    assert candidate(n = 1049) == 32
    assert candidate(n = 123456) == 351
    assert candidate(n = 441) == 21
    assert candidate(n = 1521) == 39


