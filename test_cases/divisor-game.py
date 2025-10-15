def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 625) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 576) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 576) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 649) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 649) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 343) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 343) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 640) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 640) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 819) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 819) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 299) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 299) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 777) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 701) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 701) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 129) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 129) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 997) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 997) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 768) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 768) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 503) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 503) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 377) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 377) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 499) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 420) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 420) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == True
    assert candidate(n = 3) == False
    assert candidate(n = 4) == True
    assert candidate(n = 9) == False
    assert candidate(n = 6) == True
    assert candidate(n = 2) == True
    assert candidate(n = 1000) == True
    assert candidate(n = 7) == False
    assert candidate(n = 10) == True
    assert candidate(n = 5) == False
    assert candidate(n = 625) == False
    assert candidate(n = 576) == True
    assert candidate(n = 729) == False
    assert candidate(n = 49) == False
    assert candidate(n = 50) == True
    assert candidate(n = 300) == True
    assert candidate(n = 99) == False
    assert candidate(n = 64) == True
    assert candidate(n = 17) == False
    assert candidate(n = 649) == False
    assert candidate(n = 23) == False
    assert candidate(n = 343) == False
    assert candidate(n = 640) == True
    assert candidate(n = 819) == False
    assert candidate(n = 128) == True
    assert candidate(n = 1024) == True
    assert candidate(n = 299) == False
    assert candidate(n = 777) == False
    assert candidate(n = 701) == False
    assert candidate(n = 999) == False
    assert candidate(n = 129) == False
    assert candidate(n = 18) == True
    assert candidate(n = 32) == True
    assert candidate(n = 256) == True
    assert candidate(n = 997) == False
    assert candidate(n = 768) == True
    assert candidate(n = 127) == False
    assert candidate(n = 81) == False
    assert candidate(n = 150) == True
    assert candidate(n = 503) == False
    assert candidate(n = 24) == True
    assert candidate(n = 15) == False
    assert candidate(n = 400) == True
    assert candidate(n = 512) == True
    assert candidate(n = 31) == False
    assert candidate(n = 377) == False
    assert candidate(n = 499) == False
    assert candidate(n = 1) == False
    assert candidate(n = 500) == True
    assert candidate(n = 420) == True
    assert candidate(n = 13) == False


