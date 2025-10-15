def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 25000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 25000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 250000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 15000) == 56250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15000) == 56250000: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 38099756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 38099756: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000) == 12250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000) == 12250000: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 600: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 14062500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 14062500: {e}')
    
    total += 1
    try:
        result = candidate(n = 8888) == 19749136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8888) == 19749136: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 625: {e}')
    
    total += 1
    try:
        result = candidate(n = 3333) == 2777222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3333) == 2777222: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 2250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 2250000: {e}')
    
    total += 1
    try:
        result = candidate(n = 6789) == 11522630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6789) == 11522630: {e}')
    
    total += 1
    try:
        result = candidate(n = 1200) == 360000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1200) == 360000: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 2450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 2450: {e}')
    
    total += 1
    try:
        result = candidate(n = 5001) == 6252500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5001) == 6252500: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 250500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 250500: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 2550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 2550: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 9998) == 24990001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9998) == 24990001: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 249500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 249500: {e}')
    
    total += 1
    try:
        result = candidate(n = 5555) == 7714506
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5555) == 7714506: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000) == 16000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000) == 16000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 6250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 6250000: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 24995000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 24995000: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 77) == 1482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77) == 1482: {e}')
    
    total += 1
    try:
        result = candidate(n = 12000) == 36000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12000) == 36000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 6667) == 11112222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6667) == 11112222: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 5625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 5625: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 7654) == 14645929
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7654) == 14645929: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111) == 30863580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111) == 30863580: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 1562500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 1562500: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000) == 20250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000) == 20250000: {e}')
    
    total += 1
    try:
        result = candidate(n = 4999) == 6247500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4999) == 6247500: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000) == 9000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000) == 9000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 499) == 62250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499) == 62250: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 62500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 62500: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 156: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500) == 562500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500) == 562500: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 2
    assert candidate(n = 100) == 2500
    assert candidate(n = 10000) == 25000000
    assert candidate(n = 6) == 9
    assert candidate(n = 1) == 0
    assert candidate(n = 1000) == 250000
    assert candidate(n = 10) == 25
    assert candidate(n = 15000) == 56250000
    assert candidate(n = 12345) == 38099756
    assert candidate(n = 7000) == 12250000
    assert candidate(n = 49) == 600
    assert candidate(n = 2000) == 1000000
    assert candidate(n = 7500) == 14062500
    assert candidate(n = 8888) == 19749136
    assert candidate(n = 50) == 625
    assert candidate(n = 3333) == 2777222
    assert candidate(n = 5) == 6
    assert candidate(n = 3000) == 2250000
    assert candidate(n = 6789) == 11522630
    assert candidate(n = 1200) == 360000
    assert candidate(n = 99) == 2450
    assert candidate(n = 5001) == 6252500
    assert candidate(n = 1001) == 250500
    assert candidate(n = 2) == 1
    assert candidate(n = 101) == 2550
    assert candidate(n = 8) == 16
    assert candidate(n = 9998) == 24990001
    assert candidate(n = 20000) == 100000000
    assert candidate(n = 999) == 249500
    assert candidate(n = 5555) == 7714506
    assert candidate(n = 8000) == 16000000
    assert candidate(n = 5000) == 6250000
    assert candidate(n = 9999) == 24995000
    assert candidate(n = 19) == 90
    assert candidate(n = 77) == 1482
    assert candidate(n = 12000) == 36000000
    assert candidate(n = 6667) == 11112222
    assert candidate(n = 150) == 5625
    assert candidate(n = 13) == 42
    assert candidate(n = 7654) == 14645929
    assert candidate(n = 11111) == 30863580
    assert candidate(n = 11) == 30
    assert candidate(n = 15) == 56
    assert candidate(n = 2500) == 1562500
    assert candidate(n = 9000) == 20250000
    assert candidate(n = 4999) == 6247500
    assert candidate(n = 200) == 10000
    assert candidate(n = 6000) == 9000000
    assert candidate(n = 499) == 62250
    assert candidate(n = 500) == 62500
    assert candidate(n = 7) == 12
    assert candidate(n = 25) == 156
    assert candidate(n = 1500) == 562500


