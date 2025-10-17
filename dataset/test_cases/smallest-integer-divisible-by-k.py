def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(k = 29) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 29) == 28: {e}')
    
    total += 1
    try:
        result = candidate(k = 101) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 101) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 83) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 83) == 41: {e}')
    
    total += 1
    try:
        result = candidate(k = 43) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 43) == 21: {e}')
    
    total += 1
    try:
        result = candidate(k = 89) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 89) == 44: {e}')
    
    total += 1
    try:
        result = candidate(k = 17) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 17) == 16: {e}')
    
    total += 1
    try:
        result = candidate(k = 73) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 73) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 67) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 67) == 33: {e}')
    
    total += 1
    try:
        result = candidate(k = 53) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 53) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(k = 99) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99) == 18: {e}')
    
    total += 1
    try:
        result = candidate(k = 31) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 31) == 15: {e}')
    
    total += 1
    try:
        result = candidate(k = 13) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 13) == 6: {e}')
    
    total += 1
    try:
        result = candidate(k = 71) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 71) == 35: {e}')
    
    total += 1
    try:
        result = candidate(k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 59) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 59) == 58: {e}')
    
    total += 1
    try:
        result = candidate(k = 99999) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99999) == 45: {e}')
    
    total += 1
    try:
        result = candidate(k = 97) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 97) == 96: {e}')
    
    total += 1
    try:
        result = candidate(k = 37) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 37) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 61) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 61) == 60: {e}')
    
    total += 1
    try:
        result = candidate(k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 79) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 79) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 103) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 103) == 34: {e}')
    
    total += 1
    try:
        result = candidate(k = 107) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 107) == 53: {e}')
    
    total += 1
    try:
        result = candidate(k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 109) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 109) == 108: {e}')
    
    total += 1
    try:
        result = candidate(k = 113) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 113) == 112: {e}')
    
    total += 1
    try:
        result = candidate(k = 23) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 23) == 22: {e}')
    
    total += 1
    try:
        result = candidate(k = 11) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 11) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 41) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 41) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 100000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 19) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 19) == 18: {e}')
    
    total += 1
    try:
        result = candidate(k = 47) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 47) == 46: {e}')
    
    total += 1
    try:
        result = candidate(k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 77777) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 77777) == 30: {e}')
    
    total += 1
    try:
        result = candidate(k = 234567) == 38412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 234567) == 38412: {e}')
    
    total += 1
    try:
        result = candidate(k = 4567) == 4566
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4567) == 4566: {e}')
    
    total += 1
    try:
        result = candidate(k = 24680) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 24680) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 1234567) == 34020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1234567) == 34020: {e}')
    
    total += 1
    try:
        result = candidate(k = 1000001) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1000001) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 999) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999) == 27: {e}')
    
    total += 1
    try:
        result = candidate(k = 99991) == 49995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99991) == 49995: {e}')
    
    total += 1
    try:
        result = candidate(k = 199) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 199) == 99: {e}')
    
    total += 1
    try:
        result = candidate(k = 100003) == 50001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100003) == 50001: {e}')
    
    total += 1
    try:
        result = candidate(k = 789012) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 789012) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 111111111) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 111111111) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 777777) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 777777) == 42: {e}')
    
    total += 1
    try:
        result = candidate(k = 827) == 413
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 827) == 413: {e}')
    
    total += 1
    try:
        result = candidate(k = 81) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 81) == 81: {e}')
    
    total += 1
    try:
        result = candidate(k = 131071) == 3855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 131071) == 3855: {e}')
    
    total += 1
    try:
        result = candidate(k = 7919) == 3959
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7919) == 3959: {e}')
    
    total += 1
    try:
        result = candidate(k = 34567) == 2658
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 34567) == 2658: {e}')
    
    total += 1
    try:
        result = candidate(k = 99997) == 7866
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99997) == 7866: {e}')
    
    total += 1
    try:
        result = candidate(k = 54321) == 8568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 54321) == 8568: {e}')
    
    total += 1
    try:
        result = candidate(k = 12345) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 12345) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 57) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 57) == 18: {e}')
    
    total += 1
    try:
        result = candidate(k = 59999) == 29999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 59999) == 29999: {e}')
    
    total += 1
    try:
        result = candidate(k = 500001) == 249999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500001) == 249999: {e}')
    
    total += 1
    try:
        result = candidate(k = 76543) == 25514
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 76543) == 25514: {e}')
    
    total += 1
    try:
        result = candidate(k = 100001) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100001) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 700003) == 9459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 700003) == 9459: {e}')
    
    total += 1
    try:
        result = candidate(k = 13579) == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 13579) == 366: {e}')
    
    total += 1
    try:
        result = candidate(k = 89753) == 89752
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 89753) == 89752: {e}')
    
    total += 1
    try:
        result = candidate(k = 990001) == 495000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 990001) == 495000: {e}')
    
    total += 1
    try:
        result = candidate(k = 123) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 123) == 15: {e}')
    
    total += 1
    try:
        result = candidate(k = 500003) == 214284
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 500003) == 214284: {e}')
    
    total += 1
    try:
        result = candidate(k = 65537) == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 65537) == 65536: {e}')
    
    total += 1
    try:
        result = candidate(k = 999999999) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999999999) == 81: {e}')
    
    total += 1
    try:
        result = candidate(k = 99998) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99998) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 89999) == 462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 89999) == 462: {e}')
    
    total += 1
    try:
        result = candidate(k = 50003) == 6045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50003) == 6045: {e}')
    
    total += 1
    try:
        result = candidate(k = 333) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 333) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 999983) == 999982
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 999983) == 999982: {e}')
    
    total += 1
    try:
        result = candidate(k = 899999) == 10197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 899999) == 10197: {e}')
    
    total += 1
    try:
        result = candidate(k = 88889) == 14654
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 88889) == 14654: {e}')
    
    total += 1
    try:
        result = candidate(k = 1001) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1001) == 6: {e}')
    
    total += 1
    try:
        result = candidate(k = 89765) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 89765) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 98765) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 98765) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 313) == 312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 313) == 312: {e}')
    
    total += 1
    try:
        result = candidate(k = 987654) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987654) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 104729) == 52364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 104729) == 52364: {e}')
    
    total += 1
    try:
        result = candidate(k = 75321) == 37656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75321) == 37656: {e}')
    
    total += 1
    try:
        result = candidate(k = 137) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 137) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 79999) == 13333
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 79999) == 13333: {e}')
    
    total += 1
    try:
        result = candidate(k = 23456) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 23456) == -1: {e}')
    
    total += 1
    try:
        result = candidate(k = 987654321) == 116194320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 987654321) == 116194320: {e}')
    
    total += 1
    try:
        result = candidate(k = 11111) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 11111) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 997) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 997) == 166: {e}')
    
    total += 1
    try:
        result = candidate(k = 300007) == 100002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 300007) == 100002: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(k = 29) == 28
    assert candidate(k = 101) == 4
    assert candidate(k = 83) == 41
    assert candidate(k = 43) == 21
    assert candidate(k = 89) == 44
    assert candidate(k = 17) == 16
    assert candidate(k = 73) == 8
    assert candidate(k = 67) == 33
    assert candidate(k = 53) == 13
    assert candidate(k = 7) == 6
    assert candidate(k = 99) == 18
    assert candidate(k = 31) == 15
    assert candidate(k = 13) == 6
    assert candidate(k = 71) == 35
    assert candidate(k = 2) == -1
    assert candidate(k = 59) == 58
    assert candidate(k = 99999) == 45
    assert candidate(k = 97) == 96
    assert candidate(k = 37) == 3
    assert candidate(k = 61) == 60
    assert candidate(k = 1) == 1
    assert candidate(k = 79) == 13
    assert candidate(k = 103) == 34
    assert candidate(k = 107) == 53
    assert candidate(k = 3) == 3
    assert candidate(k = 9) == 9
    assert candidate(k = 109) == 108
    assert candidate(k = 113) == 112
    assert candidate(k = 23) == 22
    assert candidate(k = 11) == 2
    assert candidate(k = 41) == 5
    assert candidate(k = 100000) == -1
    assert candidate(k = 19) == 18
    assert candidate(k = 47) == 46
    assert candidate(k = 5) == -1
    assert candidate(k = 77777) == 30
    assert candidate(k = 234567) == 38412
    assert candidate(k = 4567) == 4566
    assert candidate(k = 24680) == -1
    assert candidate(k = 1234567) == 34020
    assert candidate(k = 1000001) == 12
    assert candidate(k = 999) == 27
    assert candidate(k = 99991) == 49995
    assert candidate(k = 199) == 99
    assert candidate(k = 100003) == 50001
    assert candidate(k = 789012) == -1
    assert candidate(k = 111111111) == 9
    assert candidate(k = 777777) == 42
    assert candidate(k = 827) == 413
    assert candidate(k = 81) == 81
    assert candidate(k = 131071) == 3855
    assert candidate(k = 7919) == 3959
    assert candidate(k = 34567) == 2658
    assert candidate(k = 99997) == 7866
    assert candidate(k = 54321) == 8568
    assert candidate(k = 12345) == -1
    assert candidate(k = 57) == 18
    assert candidate(k = 59999) == 29999
    assert candidate(k = 500001) == 249999
    assert candidate(k = 76543) == 25514
    assert candidate(k = 100001) == 10
    assert candidate(k = 700003) == 9459
    assert candidate(k = 13579) == 366
    assert candidate(k = 89753) == 89752
    assert candidate(k = 990001) == 495000
    assert candidate(k = 123) == 15
    assert candidate(k = 500003) == 214284
    assert candidate(k = 65537) == 65536
    assert candidate(k = 999999999) == 81
    assert candidate(k = 99998) == -1
    assert candidate(k = 89999) == 462
    assert candidate(k = 50003) == 6045
    assert candidate(k = 333) == 9
    assert candidate(k = 999983) == 999982
    assert candidate(k = 899999) == 10197
    assert candidate(k = 88889) == 14654
    assert candidate(k = 1001) == 6
    assert candidate(k = 89765) == -1
    assert candidate(k = 98765) == -1
    assert candidate(k = 313) == 312
    assert candidate(k = 987654) == -1
    assert candidate(k = 104729) == 52364
    assert candidate(k = 75321) == 37656
    assert candidate(k = 137) == 8
    assert candidate(k = 79999) == 13333
    assert candidate(k = 23456) == -1
    assert candidate(k = 987654321) == 116194320
    assert candidate(k = 11111) == 5
    assert candidate(k = 997) == 166
    assert candidate(k = 300007) == 100002


