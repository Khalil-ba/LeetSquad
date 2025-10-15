def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -2147483648) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -2147483648) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -1) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483648) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483648) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 59049) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59049) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 72057594037927935) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72057594037927935) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 180000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 135) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2250000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2250000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8589934591) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8589934591) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 216) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 216) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000002) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000002) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1968300000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1968300000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 86400) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 86400) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 30000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 34359738368) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34359738368) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 225) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 15625) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15625) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3126) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3126) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 720) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 720) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 46656) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 46656) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -10) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3600) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3600) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1600000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1600000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2430000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2430000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2187000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2187000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 307200000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 307200000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 112500000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 112500000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 9765625) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9765625) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 531441) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 531441) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 180) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3125000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3125000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 150000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8589934592) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8589934592) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1800000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1800000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3125) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3125) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 6103515625) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6103515625) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2352) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2352) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 120) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 72057594037927936) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72057594037927936) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 40500000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40500000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 105) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 105) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388608) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388608) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 243) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 243) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 84) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == False
    assert candidate(n = 8) == True
    assert candidate(n = -2147483648) == False
    assert candidate(n = 100000) == True
    assert candidate(n = 100) == True
    assert candidate(n = 30) == True
    assert candidate(n = -1) == False
    assert candidate(n = 2147483648) == True
    assert candidate(n = 125) == True
    assert candidate(n = 14) == False
    assert candidate(n = 2147483647) == False
    assert candidate(n = 6) == True
    assert candidate(n = 1) == True
    assert candidate(n = 1000000000) == True
    assert candidate(n = 7) == False
    assert candidate(n = 1024) == True
    assert candidate(n = 59049) == True
    assert candidate(n = 72057594037927935) == False
    assert candidate(n = 45) == True
    assert candidate(n = 180000000) == True
    assert candidate(n = 135) == True
    assert candidate(n = 729) == True
    assert candidate(n = 2250000000) == True
    assert candidate(n = 8589934591) == False
    assert candidate(n = 216) == True
    assert candidate(n = 2000000000) == True
    assert candidate(n = 50000) == True
    assert candidate(n = 1000000002) == False
    assert candidate(n = 1968300000) == True
    assert candidate(n = 86400) == True
    assert candidate(n = 1000000000000) == True
    assert candidate(n = 60) == True
    assert candidate(n = 1500000000) == True
    assert candidate(n = 30000) == True
    assert candidate(n = 34359738368) == True
    assert candidate(n = 2500000000) == True
    assert candidate(n = 225) == True
    assert candidate(n = 15625) == True
    assert candidate(n = 3126) == False
    assert candidate(n = 720) == True
    assert candidate(n = 46656) == True
    assert candidate(n = 16000000) == True
    assert candidate(n = 250) == True
    assert candidate(n = 1048576) == True
    assert candidate(n = -10) == False
    assert candidate(n = 3600) == True
    assert candidate(n = 256) == True
    assert candidate(n = 1600000000) == True
    assert candidate(n = 2430000000) == True
    assert candidate(n = 2187000) == True
    assert candidate(n = 307200000) == True
    assert candidate(n = 1000000001) == False
    assert candidate(n = 112500000000) == True
    assert candidate(n = 24) == True
    assert candidate(n = 9765625) == True
    assert candidate(n = 531441) == True
    assert candidate(n = 987654321) == False
    assert candidate(n = 15) == True
    assert candidate(n = 180) == True
    assert candidate(n = 3125000000) == True
    assert candidate(n = 500000) == True
    assert candidate(n = 150000000) == True
    assert candidate(n = 8589934592) == True
    assert candidate(n = 1800000000) == True
    assert candidate(n = 3125) == True
    assert candidate(n = 6103515625) == True
    assert candidate(n = 2352) == False
    assert candidate(n = 120) == True
    assert candidate(n = 72057594037927936) == True
    assert candidate(n = 40500000) == True
    assert candidate(n = 105) == False
    assert candidate(n = 8388608) == True
    assert candidate(n = 243) == True
    assert candidate(n = 84) == False


