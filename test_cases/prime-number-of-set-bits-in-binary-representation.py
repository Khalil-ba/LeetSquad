def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(left = 100,right = 105) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100,right = 105) == 3: {e}')
    
    total += 1
    try:
        result = candidate(left = 500,right = 1000) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500,right = 1000) == 253: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 100) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 100) == 65: {e}')
    
    total += 1
    try:
        result = candidate(left = 6,right = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 6,right = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = 999900,right = 1000000) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999900,right = 1000000) == 30: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 20) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 20) == 14: {e}')
    
    total += 1
    try:
        result = candidate(left = 5,right = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5,right = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(left = 10,right = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 10,right = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000,right = 10000) == 3722
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000,right = 10000) == 3722: {e}')
    
    total += 1
    try:
        result = candidate(left = 500,right = 750) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500,right = 750) == 132: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 100010) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 100010) == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = 222222,right = 222322) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 222222,right = 222322) == 18: {e}')
    
    total += 1
    try:
        result = candidate(left = 25000,right = 30000) == 1450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 25000,right = 30000) == 1450: {e}')
    
    total += 1
    try:
        result = candidate(left = 1024,right = 2048) == 476
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1024,right = 2048) == 476: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 100100) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 100100) == 20: {e}')
    
    total += 1
    try:
        result = candidate(left = 750000,right = 750100) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 750000,right = 750100) == 40: {e}')
    
    total += 1
    try:
        result = candidate(left = 262143,right = 262243) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 262143,right = 262243) == 56: {e}')
    
    total += 1
    try:
        result = candidate(left = 1048576,right = 1048676) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1048576,right = 1048676) == 56: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000,right = 1100) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000,right = 1100) == 51: {e}')
    
    total += 1
    try:
        result = candidate(left = 5000,right = 5500) == 217
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5000,right = 5500) == 217: {e}')
    
    total += 1
    try:
        result = candidate(left = 876543,right = 876643) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 876543,right = 876643) == 25: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000000,right = 1000010) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000000,right = 1000010) == 1: {e}')
    
    total += 1
    try:
        result = candidate(left = 6000,right = 7000) == 389
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 6000,right = 7000) == 389: {e}')
    
    total += 1
    try:
        result = candidate(left = 999990,right = 1000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999990,right = 1000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(left = 12345,right = 12445) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 12345,right = 12445) == 49: {e}')
    
    total += 1
    try:
        result = candidate(left = 1048575,right = 1048675) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1048575,right = 1048675) == 56: {e}')
    
    total += 1
    try:
        result = candidate(left = 131072,right = 131272) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 131072,right = 131272) == 107: {e}')
    
    total += 1
    try:
        result = candidate(left = 99999,right = 100010) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 99999,right = 100010) == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = 555555,right = 555655) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 555555,right = 555655) == 23: {e}')
    
    total += 1
    try:
        result = candidate(left = 10000,right = 10100) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 10000,right = 10100) == 34: {e}')
    
    total += 1
    try:
        result = candidate(left = 50000,right = 50100) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 50000,right = 50100) == 26: {e}')
    
    total += 1
    try:
        result = candidate(left = 9999,right = 10010) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 9999,right = 10010) == 6: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000,right = 1050) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000,right = 1050) == 24: {e}')
    
    total += 1
    try:
        result = candidate(left = 999990,right = 999999) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999990,right = 999999) == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = 200000,right = 200100) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 200000,right = 200100) == 19: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000,right = 1024) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000,right = 1024) == 7: {e}')
    
    total += 1
    try:
        result = candidate(left = 524288,right = 524388) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 524288,right = 524388) == 56: {e}')
    
    total += 1
    try:
        result = candidate(left = 100000,right = 101000) == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 100000,right = 101000) == 295: {e}')
    
    total += 1
    try:
        result = candidate(left = 999999,right = 1000099) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999999,right = 1000099) == 23: {e}')
    
    total += 1
    try:
        result = candidate(left = 9999,right = 10099) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 9999,right = 10099) == 34: {e}')
    
    total += 1
    try:
        result = candidate(left = 200000,right = 201000) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 200000,right = 201000) == 290: {e}')
    
    total += 1
    try:
        result = candidate(left = 999,right = 2000) == 473
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999,right = 2000) == 473: {e}')
    
    total += 1
    try:
        result = candidate(left = 250000,right = 250100) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 250000,right = 250100) == 19: {e}')
    
    total += 1
    try:
        result = candidate(left = 1,right = 1000) == 530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1,right = 1000) == 530: {e}')
    
    total += 1
    try:
        result = candidate(left = 3000,right = 4000) == 393
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 3000,right = 4000) == 393: {e}')
    
    total += 1
    try:
        result = candidate(left = 10000,right = 10050) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 10000,right = 10050) == 19: {e}')
    
    total += 1
    try:
        result = candidate(left = 5000,right = 6000) == 402
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5000,right = 6000) == 402: {e}')
    
    total += 1
    try:
        result = candidate(left = 990000,right = 990100) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 990000,right = 990100) == 48: {e}')
    
    total += 1
    try:
        result = candidate(left = 987654,right = 987680) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 987654,right = 987680) == 4: {e}')
    
    total += 1
    try:
        result = candidate(left = 1023,right = 2048) == 476
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1023,right = 2048) == 476: {e}')
    
    total += 1
    try:
        result = candidate(left = 262144,right = 262244) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 262144,right = 262244) == 56: {e}')
    
    total += 1
    try:
        result = candidate(left = 123456,right = 123556) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 123456,right = 123556) == 19: {e}')
    
    total += 1
    try:
        result = candidate(left = 1023,right = 2047) == 476
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1023,right = 2047) == 476: {e}')
    
    total += 1
    try:
        result = candidate(left = 800000,right = 801000) == 291
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 800000,right = 801000) == 291: {e}')
    
    total += 1
    try:
        result = candidate(left = 5000,right = 5100) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5000,right = 5100) == 37: {e}')
    
    total += 1
    try:
        result = candidate(left = 800000,right = 800100) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 800000,right = 800100) == 18: {e}')
    
    total += 1
    try:
        result = candidate(left = 131070,right = 131080) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 131070,right = 131080) == 8: {e}')
    
    total += 1
    try:
        result = candidate(left = 1234,right = 5678) == 1954
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1234,right = 5678) == 1954: {e}')
    
    total += 1
    try:
        result = candidate(left = 999,right = 1010) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999,right = 1010) == 5: {e}')
    
    total += 1
    try:
        result = candidate(left = 543210,right = 543310) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 543210,right = 543310) == 38: {e}')
    
    total += 1
    try:
        result = candidate(left = 111111,right = 111211) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 111111,right = 111211) == 20: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000,right = 2000) == 473
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000,right = 2000) == 473: {e}')
    
    total += 1
    try:
        result = candidate(left = 999950,right = 1000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999950,right = 1000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(left = 500000,right = 500100) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500000,right = 500100) == 24: {e}')
    
    total += 1
    try:
        result = candidate(left = 500,right = 800) == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500,right = 800) == 157: {e}')
    
    total += 1
    try:
        result = candidate(left = 765432,right = 765532) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 765432,right = 765532) == 40: {e}')
    
    total += 1
    try:
        result = candidate(left = 65535,right = 65635) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 65535,right = 65635) == 56: {e}')
    
    total += 1
    try:
        result = candidate(left = 1000,right = 1200) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 1000,right = 1200) == 102: {e}')
    
    total += 1
    try:
        result = candidate(left = 75000,right = 80000) == 1371
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 75000,right = 80000) == 1371: {e}')
    
    total += 1
    try:
        result = candidate(left = 5,right = 10000) == 4251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5,right = 10000) == 4251: {e}')
    
    total += 1
    try:
        result = candidate(left = 987654,right = 987754) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 987654,right = 987754) == 16: {e}')
    
    total += 1
    try:
        result = candidate(left = 999999,right = 1000010) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999999,right = 1000010) == 1: {e}')
    
    total += 1
    try:
        result = candidate(left = 5000,right = 5050) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 5000,right = 5050) == 22: {e}')
    
    total += 1
    try:
        result = candidate(left = 500000,right = 501000) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 500000,right = 501000) == 310: {e}')
    
    total += 1
    try:
        result = candidate(left = 50000,right = 60000) == 2742
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 50000,right = 60000) == 2742: {e}')
    
    total += 1
    try:
        result = candidate(left = 104743,right = 104843) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 104743,right = 104843) == 19: {e}')
    
    total += 1
    try:
        result = candidate(left = 8192,right = 16384) == 2821
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 8192,right = 16384) == 2821: {e}')
    
    total += 1
    try:
        result = candidate(left = 200,right = 300) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 200,right = 300) == 55: {e}')
    
    total += 1
    try:
        result = candidate(left = 999990,right = 1000010) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(left = 999990,right = 1000010) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(left = 100,right = 105) == 3
    assert candidate(left = 500,right = 1000) == 253
    assert candidate(left = 1,right = 100) == 65
    assert candidate(left = 6,right = 10) == 4
    assert candidate(left = 999900,right = 1000000) == 30
    assert candidate(left = 1,right = 20) == 14
    assert candidate(left = 5,right = 5) == 1
    assert candidate(left = 10,right = 15) == 5
    assert candidate(left = 1000,right = 10000) == 3722
    assert candidate(left = 500,right = 750) == 132
    assert candidate(left = 100000,right = 100010) == 4
    assert candidate(left = 222222,right = 222322) == 18
    assert candidate(left = 25000,right = 30000) == 1450
    assert candidate(left = 1024,right = 2048) == 476
    assert candidate(left = 100000,right = 100100) == 20
    assert candidate(left = 750000,right = 750100) == 40
    assert candidate(left = 262143,right = 262243) == 56
    assert candidate(left = 1048576,right = 1048676) == 56
    assert candidate(left = 1000,right = 1100) == 51
    assert candidate(left = 5000,right = 5500) == 217
    assert candidate(left = 876543,right = 876643) == 25
    assert candidate(left = 1000000,right = 1000010) == 1
    assert candidate(left = 6000,right = 7000) == 389
    assert candidate(left = 999990,right = 1000000) == 5
    assert candidate(left = 12345,right = 12445) == 49
    assert candidate(left = 1048575,right = 1048675) == 56
    assert candidate(left = 131072,right = 131272) == 107
    assert candidate(left = 99999,right = 100010) == 4
    assert candidate(left = 555555,right = 555655) == 23
    assert candidate(left = 10000,right = 10100) == 34
    assert candidate(left = 50000,right = 50100) == 26
    assert candidate(left = 9999,right = 10010) == 6
    assert candidate(left = 1000,right = 1050) == 24
    assert candidate(left = 999990,right = 999999) == 4
    assert candidate(left = 200000,right = 200100) == 19
    assert candidate(left = 1000,right = 1024) == 7
    assert candidate(left = 524288,right = 524388) == 56
    assert candidate(left = 100000,right = 101000) == 295
    assert candidate(left = 999999,right = 1000099) == 23
    assert candidate(left = 9999,right = 10099) == 34
    assert candidate(left = 200000,right = 201000) == 290
    assert candidate(left = 999,right = 2000) == 473
    assert candidate(left = 250000,right = 250100) == 19
    assert candidate(left = 1,right = 1000) == 530
    assert candidate(left = 3000,right = 4000) == 393
    assert candidate(left = 10000,right = 10050) == 19
    assert candidate(left = 5000,right = 6000) == 402
    assert candidate(left = 990000,right = 990100) == 48
    assert candidate(left = 987654,right = 987680) == 4
    assert candidate(left = 1023,right = 2048) == 476
    assert candidate(left = 262144,right = 262244) == 56
    assert candidate(left = 123456,right = 123556) == 19
    assert candidate(left = 1023,right = 2047) == 476
    assert candidate(left = 800000,right = 801000) == 291
    assert candidate(left = 5000,right = 5100) == 37
    assert candidate(left = 800000,right = 800100) == 18
    assert candidate(left = 131070,right = 131080) == 8
    assert candidate(left = 1234,right = 5678) == 1954
    assert candidate(left = 999,right = 1010) == 5
    assert candidate(left = 543210,right = 543310) == 38
    assert candidate(left = 111111,right = 111211) == 20
    assert candidate(left = 1000,right = 2000) == 473
    assert candidate(left = 999950,right = 1000000) == 9
    assert candidate(left = 500000,right = 500100) == 24
    assert candidate(left = 500,right = 800) == 157
    assert candidate(left = 765432,right = 765532) == 40
    assert candidate(left = 65535,right = 65635) == 56
    assert candidate(left = 1000,right = 1200) == 102
    assert candidate(left = 75000,right = 80000) == 1371
    assert candidate(left = 5,right = 10000) == 4251
    assert candidate(left = 987654,right = 987754) == 16
    assert candidate(left = 999999,right = 1000010) == 1
    assert candidate(left = 5000,right = 5050) == 22
    assert candidate(left = 500000,right = 501000) == 310
    assert candidate(left = 50000,right = 60000) == 2742
    assert candidate(left = 104743,right = 104843) == 19
    assert candidate(left = 8192,right = 16384) == 2821
    assert candidate(left = 200,right = 300) == 55
    assert candidate(left = 999990,right = 1000010) == 5


