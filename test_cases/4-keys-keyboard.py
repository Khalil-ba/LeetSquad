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
        result = candidate(n = 15) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 81: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 324: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 1327104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 1327104: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 4096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 4096: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 331776
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 331776: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 1048576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 1048576: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == 589824
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == 589824: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == 432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == 432: {e}')
    
    total += 1
    try:
        result = candidate(n = 34) == 16384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34) == 16384: {e}')
    
    total += 1
    try:
        result = candidate(n = 43) == 196608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43) == 196608: {e}')
    
    total += 1
    try:
        result = candidate(n = 44) == 262144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44) == 262144: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 3072
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 3072: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 5184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 5184: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 82944
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 82944: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 36864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 36864: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 108: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 144: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == 12288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == 12288: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == 768: {e}')
    
    total += 1
    try:
        result = candidate(n = 42) == 147456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42) == 147456: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 38) == 49152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 38) == 49152: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 576: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == 2304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == 2304: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 20736
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 20736: {e}')
    
    total += 1
    try:
        result = candidate(n = 46) == 442368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 46) == 442368: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 192: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 9216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 9216: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == 27648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == 27648: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 256: {e}')
    
    total += 1
    try:
        result = candidate(n = 39) == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 39) == 65536: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(n = 48) == 786432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48) == 786432: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 26) == 1728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26) == 1728: {e}')
    
    total += 1
    try:
        result = candidate(n = 41) == 110592
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 41) == 110592: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 6912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 6912: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 48: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 1296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 1296: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 3
    assert candidate(n = 15) == 81
    assert candidate(n = 20) == 324
    assert candidate(n = 2) == 2
    assert candidate(n = 1) == 1
    assert candidate(n = 50) == 1327104
    assert candidate(n = 7) == 9
    assert candidate(n = 10) == 20
    assert candidate(n = 29) == 4096
    assert candidate(n = 45) == 331776
    assert candidate(n = 49) == 1048576
    assert candidate(n = 12) == 36
    assert candidate(n = 47) == 589824
    assert candidate(n = 21) == 432
    assert candidate(n = 34) == 16384
    assert candidate(n = 43) == 196608
    assert candidate(n = 44) == 262144
    assert candidate(n = 5) == 5
    assert candidate(n = 28) == 3072
    assert candidate(n = 30) == 5184
    assert candidate(n = 40) == 82944
    assert candidate(n = 37) == 36864
    assert candidate(n = 16) == 108
    assert candidate(n = 17) == 144
    assert candidate(n = 33) == 12288
    assert candidate(n = 23) == 768
    assert candidate(n = 42) == 147456
    assert candidate(n = 8) == 12
    assert candidate(n = 38) == 49152
    assert candidate(n = 22) == 576
    assert candidate(n = 27) == 2304
    assert candidate(n = 35) == 20736
    assert candidate(n = 46) == 442368
    assert candidate(n = 18) == 192
    assert candidate(n = 32) == 9216
    assert candidate(n = 36) == 27648
    assert candidate(n = 19) == 256
    assert candidate(n = 39) == 65536
    assert candidate(n = 24) == 1024
    assert candidate(n = 48) == 786432
    assert candidate(n = 11) == 27
    assert candidate(n = 14) == 64
    assert candidate(n = 26) == 1728
    assert candidate(n = 41) == 110592
    assert candidate(n = 31) == 6912
    assert candidate(n = 9) == 16
    assert candidate(n = 6) == 6
    assert candidate(n = 13) == 48
    assert candidate(n = 25) == 1296


