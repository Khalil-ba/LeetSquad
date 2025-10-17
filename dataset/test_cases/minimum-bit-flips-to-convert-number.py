def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(start = 123456789,goal = 987654321) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 123456789,goal = 987654321) == 15: {e}')
    
    total += 1
    try:
        result = candidate(start = 5,goal = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 5,goal = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(start = 1000000000,goal = 500000000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1000000000,goal = 500000000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(start = 8,goal = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 8,goal = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(start = 15,goal = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 15,goal = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(start = 5,goal = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 5,goal = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(start = 1000000000,goal = 999999999) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1000000000,goal = 999999999) == 10: {e}')
    
    total += 1
    try:
        result = candidate(start = 1023,goal = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1023,goal = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(start = 3,goal = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 3,goal = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(start = 29,goal = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 29,goal = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(start = 10,goal = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 10,goal = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(start = 54321,goal = 12345) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 54321,goal = 12345) == 5: {e}')
    
    total += 1
    try:
        result = candidate(start = 1023,goal = 512) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1023,goal = 512) == 9: {e}')
    
    total += 1
    try:
        result = candidate(start = 512,goal = 256) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 512,goal = 256) == 2: {e}')
    
    total += 1
    try:
        result = candidate(start = 0,goal = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 0,goal = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(start = 255,goal = 0) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 255,goal = 0) == 8: {e}')
    
    total += 1
    try:
        result = candidate(start = 15,goal = 0) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 15,goal = 0) == 4: {e}')
    
    total += 1
    try:
        result = candidate(start = 1,goal = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1,goal = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(start = 1,goal = 1023) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1,goal = 1023) == 9: {e}')
    
    total += 1
    try:
        result = candidate(start = 5,goal = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 5,goal = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(start = 111111111,goal = 999999999) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 111111111,goal = 999999999) == 13: {e}')
    
    total += 1
    try:
        result = candidate(start = 1234567890,goal = 1098765432) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1234567890,goal = 1098765432) == 16: {e}')
    
    total += 1
    try:
        result = candidate(start = 8589934591,goal = 536870912) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 8589934591,goal = 536870912) == 32: {e}')
    
    total += 1
    try:
        result = candidate(start = 4294967295,goal = 268435456) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 4294967295,goal = 268435456) == 31: {e}')
    
    total += 1
    try:
        result = candidate(start = 1,goal = 1073741824) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1,goal = 1073741824) == 2: {e}')
    
    total += 1
    try:
        result = candidate(start = 101010101,goal = 111111111) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 101010101,goal = 111111111) == 10: {e}')
    
    total += 1
    try:
        result = candidate(start = 1001100110,goal = 1110011001) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1001100110,goal = 1110011001) == 20: {e}')
    
    total += 1
    try:
        result = candidate(start = 987654321,goal = 123456789) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 987654321,goal = 123456789) == 15: {e}')
    
    total += 1
    try:
        result = candidate(start = 1000000000,goal = 0) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1000000000,goal = 0) == 13: {e}')
    
    total += 1
    try:
        result = candidate(start = 888888888,goal = 111111111) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 888888888,goal = 111111111) == 18: {e}')
    
    total += 1
    try:
        result = candidate(start = 67890,goal = 54321) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 67890,goal = 54321) == 9: {e}')
    
    total += 1
    try:
        result = candidate(start = 536870912,goal = 858993459) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 536870912,goal = 858993459) == 15: {e}')
    
    total += 1
    try:
        result = candidate(start = 1048575,goal = 2097151) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1048575,goal = 2097151) == 1: {e}')
    
    total += 1
    try:
        result = candidate(start = 1001001001,goal = 1100110011) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1001001001,goal = 1100110011) == 13: {e}')
    
    total += 1
    try:
        result = candidate(start = 858993459,goal = 1717986918) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 858993459,goal = 1717986918) == 16: {e}')
    
    total += 1
    try:
        result = candidate(start = 987654321,goal = 876543219) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 987654321,goal = 876543219) == 11: {e}')
    
    total += 1
    try:
        result = candidate(start = 123,goal = 321) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 123,goal = 321) == 5: {e}')
    
    total += 1
    try:
        result = candidate(start = 3486784401,goal = 2123366401) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 3486784401,goal = 2123366401) == 12: {e}')
    
    total += 1
    try:
        result = candidate(start = 1000000000,goal = 1) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1000000000,goal = 1) == 14: {e}')
    
    total += 1
    try:
        result = candidate(start = 1,goal = 2147483647) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1,goal = 2147483647) == 30: {e}')
    
    total += 1
    try:
        result = candidate(start = 1073741823,goal = 134217728) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1073741823,goal = 134217728) == 29: {e}')
    
    total += 1
    try:
        result = candidate(start = 999999999,goal = 111111111) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 999999999,goal = 111111111) == 13: {e}')
    
    total += 1
    try:
        result = candidate(start = 1100110011,goal = 1010101010) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1100110011,goal = 1010101010) == 19: {e}')
    
    total += 1
    try:
        result = candidate(start = 999999999,goal = 999999998) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 999999999,goal = 999999998) == 1: {e}')
    
    total += 1
    try:
        result = candidate(start = 293847,goal = 987654) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 293847,goal = 987654) == 11: {e}')
    
    total += 1
    try:
        result = candidate(start = 111111111,goal = 222222222) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 111111111,goal = 222222222) == 14: {e}')
    
    total += 1
    try:
        result = candidate(start = 1001001,goal = 1100110) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1001001,goal = 1100110) == 15: {e}')
    
    total += 1
    try:
        result = candidate(start = 123456789,goal = 123456788) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 123456789,goal = 123456788) == 1: {e}')
    
    total += 1
    try:
        result = candidate(start = 500000000,goal = 500000001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 500000000,goal = 500000001) == 1: {e}')
    
    total += 1
    try:
        result = candidate(start = 33554431,goal = 67108864) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 33554431,goal = 67108864) == 26: {e}')
    
    total += 1
    try:
        result = candidate(start = 8388607,goal = 8388608) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 8388607,goal = 8388608) == 24: {e}')
    
    total += 1
    try:
        result = candidate(start = 13579,goal = 24680) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 13579,goal = 24680) == 8: {e}')
    
    total += 1
    try:
        result = candidate(start = 134217727,goal = 268435455) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 134217727,goal = 268435455) == 1: {e}')
    
    total += 1
    try:
        result = candidate(start = 54321,goal = 100000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 54321,goal = 100000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(start = 2147483647,goal = 2147483646) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 2147483647,goal = 2147483646) == 1: {e}')
    
    total += 1
    try:
        result = candidate(start = 16777215,goal = 8388608) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 16777215,goal = 8388608) == 23: {e}')
    
    total += 1
    try:
        result = candidate(start = 86420,goal = 13579) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 86420,goal = 13579) == 10: {e}')
    
    total += 1
    try:
        result = candidate(start = 1111111111,goal = 2222222222) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1111111111,goal = 2222222222) == 16: {e}')
    
    total += 1
    try:
        result = candidate(start = 1,goal = 1000000000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1,goal = 1000000000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(start = 0,goal = 1000000000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 0,goal = 1000000000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(start = 789012345,goal = 543210987) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 789012345,goal = 543210987) == 16: {e}')
    
    total += 1
    try:
        result = candidate(start = 536870911,goal = 2147483648) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 536870911,goal = 2147483648) == 30: {e}')
    
    total += 1
    try:
        result = candidate(start = 123456789,goal = 987654322) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 123456789,goal = 987654322) == 17: {e}')
    
    total += 1
    try:
        result = candidate(start = 134217728,goal = 268435455) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 134217728,goal = 268435455) == 27: {e}')
    
    total += 1
    try:
        result = candidate(start = 536870912,goal = 268435456) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 536870912,goal = 268435456) == 2: {e}')
    
    total += 1
    try:
        result = candidate(start = 536870911,goal = 1073741823) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 536870911,goal = 1073741823) == 1: {e}')
    
    total += 1
    try:
        result = candidate(start = 0,goal = 1073741823) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 0,goal = 1073741823) == 30: {e}')
    
    total += 1
    try:
        result = candidate(start = 54321,goal = 65432) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 54321,goal = 65432) == 8: {e}')
    
    total += 1
    try:
        result = candidate(start = 268435455,goal = 67108863) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 268435455,goal = 67108863) == 2: {e}')
    
    total += 1
    try:
        result = candidate(start = 999999999,goal = 888888888) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 999999999,goal = 888888888) == 17: {e}')
    
    total += 1
    try:
        result = candidate(start = 135792468,goal = 246813579) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 135792468,goal = 246813579) == 16: {e}')
    
    total += 1
    try:
        result = candidate(start = 8675309,goal = 5309867) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 8675309,goal = 5309867) == 12: {e}')
    
    total += 1
    try:
        result = candidate(start = 999999999,goal = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 999999999,goal = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(start = 1610612735,goal = 1342177280) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1610612735,goal = 1342177280) == 28: {e}')
    
    total += 1
    try:
        result = candidate(start = 1048575,goal = 1) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1048575,goal = 1) == 19: {e}')
    
    total += 1
    try:
        result = candidate(start = 100000000,goal = 1) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 100000000,goal = 1) == 13: {e}')
    
    total += 1
    try:
        result = candidate(start = 134217728,goal = 134217729) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 134217728,goal = 134217729) == 1: {e}')
    
    total += 1
    try:
        result = candidate(start = 67890,goal = 98765) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 67890,goal = 98765) == 10: {e}')
    
    total += 1
    try:
        result = candidate(start = 1234,goal = 5678) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1234,goal = 5678) == 8: {e}')
    
    total += 1
    try:
        result = candidate(start = 67890,goal = 12345) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 67890,goal = 12345) == 8: {e}')
    
    total += 1
    try:
        result = candidate(start = 1073741824,goal = 2147483647) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 1073741824,goal = 2147483647) == 30: {e}')
    
    total += 1
    try:
        result = candidate(start = 123456,goal = 654321) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 123456,goal = 654321) == 8: {e}')
    
    total += 1
    try:
        result = candidate(start = 65535,goal = 32768) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 65535,goal = 32768) == 15: {e}')
    
    total += 1
    try:
        result = candidate(start = 555555555,goal = 444444444) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 555555555,goal = 444444444) == 20: {e}')
    
    total += 1
    try:
        result = candidate(start = 2147483647,goal = 0) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(start = 2147483647,goal = 0) == 31: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(start = 123456789,goal = 987654321) == 15
    assert candidate(start = 5,goal = 2) == 3
    assert candidate(start = 1000000000,goal = 500000000) == 14
    assert candidate(start = 8,goal = 15) == 3
    assert candidate(start = 15,goal = 8) == 3
    assert candidate(start = 5,goal = 8) == 3
    assert candidate(start = 1000000000,goal = 999999999) == 10
    assert candidate(start = 1023,goal = 0) == 10
    assert candidate(start = 3,goal = 4) == 3
    assert candidate(start = 29,goal = 15) == 2
    assert candidate(start = 10,goal = 7) == 3
    assert candidate(start = 54321,goal = 12345) == 5
    assert candidate(start = 1023,goal = 512) == 9
    assert candidate(start = 512,goal = 256) == 2
    assert candidate(start = 0,goal = 0) == 0
    assert candidate(start = 255,goal = 0) == 8
    assert candidate(start = 15,goal = 0) == 4
    assert candidate(start = 1,goal = 1) == 0
    assert candidate(start = 1,goal = 1023) == 9
    assert candidate(start = 5,goal = 10) == 4
    assert candidate(start = 111111111,goal = 999999999) == 13
    assert candidate(start = 1234567890,goal = 1098765432) == 16
    assert candidate(start = 8589934591,goal = 536870912) == 32
    assert candidate(start = 4294967295,goal = 268435456) == 31
    assert candidate(start = 1,goal = 1073741824) == 2
    assert candidate(start = 101010101,goal = 111111111) == 10
    assert candidate(start = 1001100110,goal = 1110011001) == 20
    assert candidate(start = 987654321,goal = 123456789) == 15
    assert candidate(start = 1000000000,goal = 0) == 13
    assert candidate(start = 888888888,goal = 111111111) == 18
    assert candidate(start = 67890,goal = 54321) == 9
    assert candidate(start = 536870912,goal = 858993459) == 15
    assert candidate(start = 1048575,goal = 2097151) == 1
    assert candidate(start = 1001001001,goal = 1100110011) == 13
    assert candidate(start = 858993459,goal = 1717986918) == 16
    assert candidate(start = 987654321,goal = 876543219) == 11
    assert candidate(start = 123,goal = 321) == 5
    assert candidate(start = 3486784401,goal = 2123366401) == 12
    assert candidate(start = 1000000000,goal = 1) == 14
    assert candidate(start = 1,goal = 2147483647) == 30
    assert candidate(start = 1073741823,goal = 134217728) == 29
    assert candidate(start = 999999999,goal = 111111111) == 13
    assert candidate(start = 1100110011,goal = 1010101010) == 19
    assert candidate(start = 999999999,goal = 999999998) == 1
    assert candidate(start = 293847,goal = 987654) == 11
    assert candidate(start = 111111111,goal = 222222222) == 14
    assert candidate(start = 1001001,goal = 1100110) == 15
    assert candidate(start = 123456789,goal = 123456788) == 1
    assert candidate(start = 500000000,goal = 500000001) == 1
    assert candidate(start = 33554431,goal = 67108864) == 26
    assert candidate(start = 8388607,goal = 8388608) == 24
    assert candidate(start = 13579,goal = 24680) == 8
    assert candidate(start = 134217727,goal = 268435455) == 1
    assert candidate(start = 54321,goal = 100000) == 7
    assert candidate(start = 2147483647,goal = 2147483646) == 1
    assert candidate(start = 16777215,goal = 8388608) == 23
    assert candidate(start = 86420,goal = 13579) == 10
    assert candidate(start = 1111111111,goal = 2222222222) == 16
    assert candidate(start = 1,goal = 1000000000) == 14
    assert candidate(start = 0,goal = 1000000000) == 13
    assert candidate(start = 789012345,goal = 543210987) == 16
    assert candidate(start = 536870911,goal = 2147483648) == 30
    assert candidate(start = 123456789,goal = 987654322) == 17
    assert candidate(start = 134217728,goal = 268435455) == 27
    assert candidate(start = 536870912,goal = 268435456) == 2
    assert candidate(start = 536870911,goal = 1073741823) == 1
    assert candidate(start = 0,goal = 1073741823) == 30
    assert candidate(start = 54321,goal = 65432) == 8
    assert candidate(start = 268435455,goal = 67108863) == 2
    assert candidate(start = 999999999,goal = 888888888) == 17
    assert candidate(start = 135792468,goal = 246813579) == 16
    assert candidate(start = 8675309,goal = 5309867) == 12
    assert candidate(start = 999999999,goal = 1) == 20
    assert candidate(start = 1610612735,goal = 1342177280) == 28
    assert candidate(start = 1048575,goal = 1) == 19
    assert candidate(start = 100000000,goal = 1) == 13
    assert candidate(start = 134217728,goal = 134217729) == 1
    assert candidate(start = 67890,goal = 98765) == 10
    assert candidate(start = 1234,goal = 5678) == 8
    assert candidate(start = 67890,goal = 12345) == 8
    assert candidate(start = 1073741824,goal = 2147483647) == 30
    assert candidate(start = 123456,goal = 654321) == 8
    assert candidate(start = 65535,goal = 32768) == 15
    assert candidate(start = 555555555,goal = 444444444) == 20
    assert candidate(start = 2147483647,goal = 0) == 31


