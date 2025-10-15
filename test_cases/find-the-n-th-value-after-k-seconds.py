def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 7,k = 4) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 4) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 4) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 4) == 330: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 2) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 2) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 5) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 5) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 7) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 7) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10) == 92378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10) == 92378: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 100) == 5151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 100) == 5151: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 4) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 4) == 495: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 200) == 793946740
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 200) == 793946740: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 8) == 1287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 8) == 1287: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 100) == 824578740
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 100) == 824578740: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 15) == 77558760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 15) == 77558760: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 18) == 1562275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 18) == 1562275: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3) == 84: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 3) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 3) == 680: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 20) == 527148437
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 20) == 527148437: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 20) == 923263934
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 20) == 923263934: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1000) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1000) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 15) == 54264
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 15) == 54264: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50) == 475860182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50) == 475860182: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 500) == 540818587
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 500) == 540818587: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 999) == 482800871
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 999) == 482800871: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 25) == 462115415
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 25) == 462115415: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5) == 2002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5) == 2002: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 10) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 10) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 3) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 3) == 120: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 10) == 1961256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 10) == 1961256: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 15) == 15504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 15) == 15504: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 30) == 368504682
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 30) == 368504682: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,k = 75) == 133231804
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,k = 75) == 133231804: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 7) == 3432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 7) == 3432: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 7) == 1716
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 7) == 1716: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 500) == 579917918
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 500) == 579917918: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 5) == 42504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 5) == 42504: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5) == 126: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 15) == 855967513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 15) == 855967513: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 20) == 1771
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 20) == 1771: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 5) == 462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 5) == 462: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 50) == 769496025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 50) == 769496025: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 1000) == 36237869
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 1000) == 36237869: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 3) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 3) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 7) == 116280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 7) == 116280: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,k = 50) == 46410598
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,k = 50) == 46410598: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 6) == 462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 6) == 462: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 1) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 1) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 8) == 6435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 8) == 6435: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 250) == 244556185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 250) == 244556185: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,k = 25) == 183579396
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,k = 25) == 183579396: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 20) == 230230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 20) == 230230: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 12) == 1352078
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 12) == 1352078: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 40) == 280099481
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 40) == 280099481: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 100) == 703668401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 100) == 703668401: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 250) == 81637167
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 250) == 81637167: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 7,k = 4) == 210
    assert candidate(n = 2,k = 4) == 5
    assert candidate(n = 2,k = 5) == 6
    assert candidate(n = 8,k = 4) == 330
    assert candidate(n = 2,k = 1) == 2
    assert candidate(n = 1,k = 1) == 1
    assert candidate(n = 3,k = 2) == 6
    assert candidate(n = 6,k = 2) == 21
    assert candidate(n = 4,k = 5) == 56
    assert candidate(n = 3,k = 7) == 36
    assert candidate(n = 10,k = 10) == 92378
    assert candidate(n = 5,k = 3) == 35
    assert candidate(n = 3,k = 100) == 5151
    assert candidate(n = 9,k = 4) == 495
    assert candidate(n = 200,k = 200) == 793946740
    assert candidate(n = 6,k = 8) == 1287
    assert candidate(n = 200,k = 100) == 824578740
    assert candidate(n = 15,k = 15) == 77558760
    assert candidate(n = 9,k = 18) == 1562275
    assert candidate(n = 7,k = 3) == 84
    assert candidate(n = 15,k = 3) == 680
    assert candidate(n = 15,k = 1) == 15
    assert candidate(n = 30,k = 20) == 527148437
    assert candidate(n = 20,k = 20) == 923263934
    assert candidate(n = 10,k = 1) == 10
    assert candidate(n = 2,k = 1000) == 1001
    assert candidate(n = 7,k = 15) == 54264
    assert candidate(n = 8,k = 1) == 8
    assert candidate(n = 100,k = 50) == 475860182
    assert candidate(n = 250,k = 500) == 540818587
    assert candidate(n = 999,k = 999) == 482800871
    assert candidate(n = 30,k = 25) == 462115415
    assert candidate(n = 10,k = 5) == 2002
    assert candidate(n = 5,k = 10) == 1001
    assert candidate(n = 8,k = 3) == 120
    assert candidate(n = 15,k = 10) == 1961256
    assert candidate(n = 6,k = 15) == 15504
    assert candidate(n = 30,k = 30) == 368504682
    assert candidate(n = 75,k = 75) == 133231804
    assert candidate(n = 8,k = 7) == 3432
    assert candidate(n = 7,k = 7) == 1716
    assert candidate(n = 500,k = 500) == 579917918
    assert candidate(n = 20,k = 5) == 42504
    assert candidate(n = 5,k = 5) == 126
    assert candidate(n = 20,k = 15) == 855967513
    assert candidate(n = 4,k = 20) == 1771
    assert candidate(n = 7,k = 5) == 462
    assert candidate(n = 50,k = 50) == 769496025
    assert candidate(n = 1000,k = 1000) == 36237869
    assert candidate(n = 6,k = 3) == 56
    assert candidate(n = 15,k = 7) == 116280
    assert candidate(n = 250,k = 50) == 46410598
    assert candidate(n = 6,k = 6) == 462
    assert candidate(n = 1000,k = 1) == 1000
    assert candidate(n = 8,k = 8) == 6435
    assert candidate(n = 300,k = 250) == 244556185
    assert candidate(n = 11,k = 25) == 183579396
    assert candidate(n = 7,k = 20) == 230230
    assert candidate(n = 12,k = 12) == 1352078
    assert candidate(n = 50,k = 40) == 280099481
    assert candidate(n = 1,k = 1000) == 1
    assert candidate(n = 100,k = 100) == 703668401
    assert candidate(n = 500,k = 250) == 81637167


