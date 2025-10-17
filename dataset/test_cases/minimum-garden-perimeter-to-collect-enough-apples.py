def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(neededApples = 10000000000) == 10856
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 10000000000) == 10856: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 50) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 50) == 16: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 1000000) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 1000000) == 504: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 13) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 13) == 16: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 1000000000) == 5040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 1000000000) == 5040: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 1000000000000000) == 503968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 1000000000000000) == 503968: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 1000) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 1000) == 48: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 987654321) == 5016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 987654321) == 5016: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 1000000000000) == 50400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 1000000000000) == 50400: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 999999999999999) == 503968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 999999999999999) == 503968: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 100) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 100) == 24: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 100000000) == 2336
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 100000000) == 2336: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 123456789) == 2512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 123456789) == 2512: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 2000000000) == 6352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 2000000000) == 6352: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 50000000000) == 18568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 50000000000) == 18568: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 123456789012345) == 250944
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 123456789012345) == 250944: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 1000000001) == 5040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 1000000001) == 5040: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 18014398509481984) == 1321120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 18014398509481984) == 1321120: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 10000) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 10000) == 112: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 5000000000) == 8616
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 5000000000) == 8616: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 50000) == 184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 50000) == 184: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 120) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 120) == 24: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 20) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 20) == 16: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 2000000000000) == 63496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 2000000000000) == 63496: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 100000000000) == 23392
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 100000000000) == 23392: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 2147483647) == 6504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 2147483647) == 6504: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 100000) == 232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 100000) == 232: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 123456789123) == 25096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 123456789123) == 25096: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 987654321987) == 50192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 987654321987) == 50192: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 2500000000) == 6840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 2500000000) == 6840: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 468) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 468) == 40: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 500000000000) == 40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 500000000000) == 40000: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 20736) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 20736) == 136: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 256) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 256) == 32: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 500000000000000) == 400000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 500000000000000) == 400000: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 111111111111111) == 242280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 111111111111111) == 242280: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 99999999999999999) == 2339216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 99999999999999999) == 2339216: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 8000000000) == 10080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 8000000000) == 10080: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 12) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 12) == 8: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 122500) == 248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 122500) == 248: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 25200) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 25200) == 144: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 598593750000) == 42472
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 598593750000) == 42472: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 9261000) == 1056
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 9261000) == 1056: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 754321098) == 4584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 754321098) == 4584: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 999999999999999999) == 5039688
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 999999999999999999) == 5039688: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 876543210987654) == 482312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 876543210987654) == 482312: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 100000000000000000000) == 23392144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 100000000000000000000) == 23392144: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 100000000000000) == 233920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 100000000000000) == 233920: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 400000000000000) == 371328
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 400000000000000) == 371328: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 1000000000000000000) == 5039688
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 1000000000000000000) == 5039688: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 987654321098765) == 501888
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 987654321098765) == 501888: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 9999999999999999) == 1085768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 9999999999999999) == 1085768: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 5000) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 5000) == 88: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 10000000000000) == 108576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 10000000000000) == 108576: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 3500) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 3500) == 80: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 1024) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 1024) == 48: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 18) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 18) == 16: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 30000000000000) == 156592
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 30000000000000) == 156592: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 500) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 500) == 40: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 10000000000000000000) == 10857672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 10000000000000000000) == 10857672: {e}')
    
    total += 1
    try:
        result = candidate(neededApples = 4608) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(neededApples = 4608) == 80: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(neededApples = 10000000000) == 10856
    assert candidate(neededApples = 10) == 8
    assert candidate(neededApples = 50) == 16
    assert candidate(neededApples = 1000000) == 504
    assert candidate(neededApples = 13) == 16
    assert candidate(neededApples = 1000000000) == 5040
    assert candidate(neededApples = 1000000000000000) == 503968
    assert candidate(neededApples = 1000) == 48
    assert candidate(neededApples = 987654321) == 5016
    assert candidate(neededApples = 1000000000000) == 50400
    assert candidate(neededApples = 999999999999999) == 503968
    assert candidate(neededApples = 100) == 24
    assert candidate(neededApples = 100000000) == 2336
    assert candidate(neededApples = 123456789) == 2512
    assert candidate(neededApples = 1) == 8
    assert candidate(neededApples = 2000000000) == 6352
    assert candidate(neededApples = 50000000000) == 18568
    assert candidate(neededApples = 123456789012345) == 250944
    assert candidate(neededApples = 1000000001) == 5040
    assert candidate(neededApples = 18014398509481984) == 1321120
    assert candidate(neededApples = 10000) == 112
    assert candidate(neededApples = 5000000000) == 8616
    assert candidate(neededApples = 50000) == 184
    assert candidate(neededApples = 120) == 24
    assert candidate(neededApples = 5) == 8
    assert candidate(neededApples = 6) == 8
    assert candidate(neededApples = 20) == 16
    assert candidate(neededApples = 2000000000000) == 63496
    assert candidate(neededApples = 100000000000) == 23392
    assert candidate(neededApples = 2147483647) == 6504
    assert candidate(neededApples = 100000) == 232
    assert candidate(neededApples = 123456789123) == 25096
    assert candidate(neededApples = 987654321987) == 50192
    assert candidate(neededApples = 2500000000) == 6840
    assert candidate(neededApples = 468) == 40
    assert candidate(neededApples = 500000000000) == 40000
    assert candidate(neededApples = 20736) == 136
    assert candidate(neededApples = 256) == 32
    assert candidate(neededApples = 500000000000000) == 400000
    assert candidate(neededApples = 111111111111111) == 242280
    assert candidate(neededApples = 99999999999999999) == 2339216
    assert candidate(neededApples = 8000000000) == 10080
    assert candidate(neededApples = 12) == 8
    assert candidate(neededApples = 122500) == 248
    assert candidate(neededApples = 25200) == 144
    assert candidate(neededApples = 598593750000) == 42472
    assert candidate(neededApples = 9261000) == 1056
    assert candidate(neededApples = 754321098) == 4584
    assert candidate(neededApples = 999999999999999999) == 5039688
    assert candidate(neededApples = 876543210987654) == 482312
    assert candidate(neededApples = 100000000000000000000) == 23392144
    assert candidate(neededApples = 100000000000000) == 233920
    assert candidate(neededApples = 400000000000000) == 371328
    assert candidate(neededApples = 1000000000000000000) == 5039688
    assert candidate(neededApples = 987654321098765) == 501888
    assert candidate(neededApples = 9999999999999999) == 1085768
    assert candidate(neededApples = 5000) == 88
    assert candidate(neededApples = 10000000000000) == 108576
    assert candidate(neededApples = 3500) == 80
    assert candidate(neededApples = 1024) == 48
    assert candidate(neededApples = 18) == 16
    assert candidate(neededApples = 30000000000000) == 156592
    assert candidate(neededApples = 2) == 8
    assert candidate(neededApples = 500) == 40
    assert candidate(neededApples = 4) == 8
    assert candidate(neededApples = 3) == 8
    assert candidate(neededApples = 10000000000000000000) == 10857672
    assert candidate(neededApples = 4608) == 80


