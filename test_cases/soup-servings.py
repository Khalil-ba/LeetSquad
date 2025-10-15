def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 0.7421875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 0.7421875: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 0.796875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 0.796875: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 0.71875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 0.71875: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 0.625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 0.625: {e}')
    
    total += 1
    try:
        result = candidate(n = 625) == 0.9417028725147247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625) == 0.9417028725147247: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000003) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000003) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999996) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999996) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 0.9977163163248763
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 0.9977163163248763: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 0.9765650521094358
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 0.9765650521094358: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000002) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000002) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3333) == 0.9998851608898072
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3333) == 0.9998851608898072: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999998) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999998) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 0.9997529725570642
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 0.9997529725570642: {e}')
    
    total += 1
    try:
        result = candidate(n = 875000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 875000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1200) == 0.9855064973468473
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1200) == 0.9855064973468473: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345678) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345678) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == 0.82763671875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 0.82763671875: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999995) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999995) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 375) == 0.88482666015625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 375) == 0.88482666015625: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 0.9765650521094358
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 0.9765650521094358: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 800) == 0.961617625085637
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800) == 0.961617625085637: {e}')
    
    total += 1
    try:
        result = candidate(n = 567890123) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567890123) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 0.99925483400331
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 0.99925483400331: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999997) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999997) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 0.8896331787109375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 0.8896331787109375: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 0.9564644806087017
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 0.9564644806087017: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 0.916344165802002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 0.916344165802002: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 0.625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 0.625: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500) == 0.9928319024738018
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500) == 0.9928319024738018: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0.5
    assert candidate(n = 125) == 0.7421875
    assert candidate(n = 200) == 0.796875
    assert candidate(n = 100) == 0.71875
    assert candidate(n = 1000000000) == 1
    assert candidate(n = 50) == 0.625
    assert candidate(n = 625) == 0.9417028725147247
    assert candidate(n = 1000000003) == 1
    assert candidate(n = 999999999) == 1
    assert candidate(n = 12345) == 1
    assert candidate(n = 999999996) == 1
    assert candidate(n = 7500) == 1
    assert candidate(n = 2000) == 0.9977163163248763
    assert candidate(n = 300000) == 1
    assert candidate(n = 50000) == 1
    assert candidate(n = 1000) == 0.9765650521094358
    assert candidate(n = 1000000002) == 1
    assert candidate(n = 3333) == 0.9998851608898072
    assert candidate(n = 250000) == 1
    assert candidate(n = 999999998) == 1
    assert candidate(n = 3000) == 0.9997529725570642
    assert candidate(n = 875000000) == 1
    assert candidate(n = 1200) == 0.9855064973468473
    assert candidate(n = 750000) == 1
    assert candidate(n = 10000) == 1
    assert candidate(n = 750000000) == 1
    assert candidate(n = 12345678) == 1
    assert candidate(n = 250) == 0.82763671875
    assert candidate(n = 999999995) == 1
    assert candidate(n = 100000) == 1
    assert candidate(n = 20000) == 1
    assert candidate(n = 375) == 0.88482666015625
    assert candidate(n = 999) == 0.9765650521094358
    assert candidate(n = 5000) == 1
    assert candidate(n = 75000) == 1
    assert candidate(n = 25000) == 1
    assert candidate(n = 9999) == 1
    assert candidate(n = 1000000001) == 1
    assert candidate(n = 987654321) == 1
    assert candidate(n = 800) == 0.961617625085637
    assert candidate(n = 567890123) == 1
    assert candidate(n = 2500) == 0.99925483400331
    assert candidate(n = 500000) == 1
    assert candidate(n = 999999997) == 1
    assert candidate(n = 400) == 0.8896331787109375
    assert candidate(n = 500000000) == 1
    assert candidate(n = 1000000) == 1
    assert candidate(n = 750) == 0.9564644806087017
    assert candidate(n = 123456789) == 1
    assert candidate(n = 1234567) == 1
    assert candidate(n = 999999) == 1
    assert candidate(n = 123456) == 1
    assert candidate(n = 500) == 0.916344165802002
    assert candidate(n = 25) == 0.625
    assert candidate(n = 1500) == 0.9928319024738018


