def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1,k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 31,k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31,k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,k = 999999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,k = 999999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 11) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 11) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 31,k = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31,k = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023,k = 512) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023,k = 512) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 21,k = 21) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21,k = 21) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,k = 13) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,k = 13) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023,k = 511) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023,k = 511) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,k = 500000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,k = 500000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1047552,k = 523776) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1047552,k = 523776) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767,k = 16384) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767,k = 16384) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999,k = 1000000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999,k = 1000000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535,k = 32767) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535,k = 32767) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111,k = 222222) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111,k = 222222) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,k = 524288) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,k = 524288) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,k = 4194304) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,k = 4194304) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191,k = 4096) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191,k = 4096) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 255,k = 128) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255,k = 128) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456,k = 65536) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456,k = 65536) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 983040,k = 524288) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 983040,k = 524288) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 777777,k = 777777) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777777,k = 777777) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576,k = 1048576) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576,k = 1048576) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191,k = 8191) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191,k = 8191) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575,k = 1) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575,k = 1) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456,k = 123455) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456,k = 123455) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,k = 524286) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,k = 524286) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,k = 4194303) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,k = 4194303) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048574,k = 1048573) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048574,k = 1048573) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456,k = 123456) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456,k = 123456) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 786432,k = 393216) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 786432,k = 393216) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 777777,k = 888888) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777777,k = 888888) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575,k = 524288) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575,k = 524288) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888,k = 999999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888,k = 999999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535,k = 65534) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535,k = 65534) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1048575) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1048575) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097151,k = 1048576) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097151,k = 1048576) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215,k = 16777214) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215,k = 16777214) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071,k = 65535) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071,k = 65535) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999,k = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999,k = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,k = 8388607) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,k = 8388607) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567,k = 1234566) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567,k = 1234566) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 983041,k = 262144) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 983041,k = 262144) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555,k = 555554) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555,k = 555554) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654,k = 123456) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654,k = 123456) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567,k = 1234568) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567,k = 1234568) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456,k = 654321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456,k = 654321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567,k = 7654321) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567,k = 7654321) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191,k = 4095) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191,k = 4095) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024,k = 1023) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024,k = 1023) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001,k = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001,k = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,k = 262143) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,k = 262143) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,k = 1000001) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,k = 1000001) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888,k = 888880) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888,k = 888880) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535,k = 4095) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535,k = 4095) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023,k = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023,k = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 333333,k = 666666) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333,k = 666666) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,k = 262144) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,k = 262144) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,k = 1) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,k = 1) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071,k = 131072) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071,k = 131072) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215,k = 8388608) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215,k = 8388608) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535,k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535,k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,k = 524287) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,k = 524287) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654,k = 987653) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654,k = 987653) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 897531,k = 897532) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 897531,k = 897532) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543,k = 9876542) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543,k = 9876542) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 777777,k = 666666) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777777,k = 666666) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 32768,k = 16384) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32768,k = 16384) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654,k = 987655) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654,k = 987655) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192,k = 4096) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192,k = 4096) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535,k = 32768) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535,k = 32768) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388608,k = 4194304) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388608,k = 4194304) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575,k = 524287) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575,k = 524287) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 983040,k = 491520) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 983040,k = 491520) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071,k = 262142) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071,k = 262142) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6143,k = 1024) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6143,k = 1024) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575,k = 0) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575,k = 0) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071,k = 1) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071,k = 1) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303,k = 2097152) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303,k = 2097152) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 262144,k = 131072) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262144,k = 131072) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4095,k = 1023) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4095,k = 1023) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 0) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 0) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1,k = 2) == -1
    assert candidate(n = 31,k = 1) == 4
    assert candidate(n = 15,k = 9) == 2
    assert candidate(n = 8,k = 8) == 0
    assert candidate(n = 1000000,k = 999999) == -1
    assert candidate(n = 7,k = 11) == -1
    assert candidate(n = 7,k = 3) == 1
    assert candidate(n = 5,k = 3) == -1
    assert candidate(n = 9,k = 8) == 1
    assert candidate(n = 6,k = 5) == -1
    assert candidate(n = 31,k = 15) == 1
    assert candidate(n = 1023,k = 512) == 9
    assert candidate(n = 21,k = 21) == 0
    assert candidate(n = 13,k = 4) == 2
    assert candidate(n = 14,k = 13) == -1
    assert candidate(n = 1023,k = 511) == 1
    assert candidate(n = 1000000,k = 500000) == -1
    assert candidate(n = 1047552,k = 523776) == -1
    assert candidate(n = 32767,k = 16384) == 14
    assert candidate(n = 999999,k = 1000000) == -1
    assert candidate(n = 65535,k = 32767) == 1
    assert candidate(n = 111111,k = 222222) == -1
    assert candidate(n = 524287,k = 524288) == -1
    assert candidate(n = 8388607,k = 4194304) == 22
    assert candidate(n = 8191,k = 4096) == 12
    assert candidate(n = 1000000,k = 1) == -1
    assert candidate(n = 255,k = 128) == 7
    assert candidate(n = 123456,k = 65536) == 5
    assert candidate(n = 983040,k = 524288) == 3
    assert candidate(n = 777777,k = 777777) == 0
    assert candidate(n = 1048576,k = 1048576) == 0
    assert candidate(n = 8191,k = 8191) == 0
    assert candidate(n = 1048575,k = 1) == 19
    assert candidate(n = 2,k = 1) == -1
    assert candidate(n = 123456,k = 123455) == -1
    assert candidate(n = 524287,k = 524286) == 1
    assert candidate(n = 8388607,k = 4194303) == 1
    assert candidate(n = 1048574,k = 1048573) == -1
    assert candidate(n = 123456,k = 123456) == 0
    assert candidate(n = 786432,k = 393216) == -1
    assert candidate(n = 777777,k = 888888) == -1
    assert candidate(n = 1048575,k = 524288) == 19
    assert candidate(n = 888888,k = 999999) == -1
    assert candidate(n = 65535,k = 65534) == 1
    assert candidate(n = 1,k = 1048575) == -1
    assert candidate(n = 2097151,k = 1048576) == 20
    assert candidate(n = 16777215,k = 16777214) == 1
    assert candidate(n = 131071,k = 65535) == 1
    assert candidate(n = 999999,k = 1) == 11
    assert candidate(n = 8388607,k = 8388607) == 0
    assert candidate(n = 1234567,k = 1234566) == 1
    assert candidate(n = 983041,k = 262144) == 4
    assert candidate(n = 555555,k = 555554) == 1
    assert candidate(n = 987654,k = 123456) == -1
    assert candidate(n = 1234567,k = 1234568) == -1
    assert candidate(n = 123456,k = 654321) == -1
    assert candidate(n = 1234567,k = 7654321) == -1
    assert candidate(n = 8191,k = 4095) == 1
    assert candidate(n = 1024,k = 1023) == -1
    assert candidate(n = 1001,k = 1000) == 1
    assert candidate(n = 524287,k = 262143) == 1
    assert candidate(n = 1000000,k = 1000001) == -1
    assert candidate(n = 888888,k = 888880) == 1
    assert candidate(n = 65535,k = 4095) == 4
    assert candidate(n = 1023,k = 0) == 10
    assert candidate(n = 333333,k = 666666) == -1
    assert candidate(n = 524287,k = 262144) == 18
    assert candidate(n = 524287,k = 1) == 18
    assert candidate(n = 131071,k = 131072) == -1
    assert candidate(n = 16777215,k = 8388608) == 23
    assert candidate(n = 65535,k = 1) == 15
    assert candidate(n = 524287,k = 524287) == 0
    assert candidate(n = 987654,k = 987653) == -1
    assert candidate(n = 897531,k = 897532) == -1
    assert candidate(n = 9876543,k = 9876542) == 1
    assert candidate(n = 777777,k = 666666) == -1
    assert candidate(n = 32768,k = 16384) == -1
    assert candidate(n = 987654,k = 987655) == -1
    assert candidate(n = 8192,k = 4096) == -1
    assert candidate(n = 65535,k = 32768) == 15
    assert candidate(n = 8388608,k = 4194304) == -1
    assert candidate(n = 1048575,k = 524287) == 1
    assert candidate(n = 983040,k = 491520) == -1
    assert candidate(n = 131071,k = 262142) == -1
    assert candidate(n = 6143,k = 1024) == 11
    assert candidate(n = 1048575,k = 0) == 20
    assert candidate(n = 131071,k = 1) == 16
    assert candidate(n = 4194303,k = 2097152) == 21
    assert candidate(n = 262144,k = 131072) == -1
    assert candidate(n = 4095,k = 1023) == 2
    assert candidate(n = 7,k = 0) == 3


