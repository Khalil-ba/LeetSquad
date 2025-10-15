def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 757631812
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 757631812: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 310828084
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 310828084: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 505379714
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 505379714: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 356435599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 356435599: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 632668867
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 632668867: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 499361981
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 499361981: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 462911642
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 462911642: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 1765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 1765: {e}')
    
    total += 1
    try:
        result = candidate(n = 15000) == 760107204
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15000) == 760107204: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 880407397
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 880407397: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 836722104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 836722104: {e}')
    
    total += 1
    try:
        result = candidate(n = 67890) == 121883656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67890) == 121883656: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == 351669993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == 351669993: {e}')
    
    total += 1
    try:
        result = candidate(n = 90000) == 333354001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90000) == 333354001: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 305317209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 305317209: {e}')
    
    total += 1
    try:
        result = candidate(n = 60000) == 841047212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60000) == 841047212: {e}')
    
    total += 1
    try:
        result = candidate(n = 30000) == 789968936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30000) == 789968936: {e}')
    
    total += 1
    try:
        result = candidate(n = 80000) == 801174769
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80000) == 801174769: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == 853721666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == 853721666: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == 273282097
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == 273282097: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 754628255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 754628255: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000) == 363627085
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000) == 363627085: {e}')
    
    total += 1
    try:
        result = candidate(n = 40000) == 162370743
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40000) == 162370743: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == 183542430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == 183542430: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 715412131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 715412131: {e}')
    
    total += 1
    try:
        result = candidate(n = 25000) == 110872861
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25000) == 110872861: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 27
    assert candidate(n = 100000) == 757631812
    assert candidate(n = 100) == 310828084
    assert candidate(n = 12) == 505379714
    assert candidate(n = 10000) == 356435599
    assert candidate(n = 20) == 632668867
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 499361981
    assert candidate(n = 10) == 462911642
    assert candidate(n = 5) == 1765
    assert candidate(n = 15000) == 760107204
    assert candidate(n = 99999) == 880407397
    assert candidate(n = 12345) == 836722104
    assert candidate(n = 67890) == 121883656
    assert candidate(n = 32767) == 351669993
    assert candidate(n = 90000) == 333354001
    assert candidate(n = 50000) == 305317209
    assert candidate(n = 60000) == 841047212
    assert candidate(n = 30000) == 789968936
    assert candidate(n = 80000) == 801174769
    assert candidate(n = 8192) == 853721666
    assert candidate(n = 65536) == 273282097
    assert candidate(n = 5000) == 754628255
    assert candidate(n = 75000) == 363627085
    assert candidate(n = 40000) == 162370743
    assert candidate(n = 65535) == 183542430
    assert candidate(n = 500) == 715412131
    assert candidate(n = 25000) == 110872861


