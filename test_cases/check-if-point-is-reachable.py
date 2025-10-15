def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(targetX = 7,targetY = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 7,targetY = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 6,targetY = 9) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 6,targetY = 9) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 16,targetY = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 16,targetY = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 3,targetY = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 3,targetY = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 10,targetY = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 10,targetY = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1,targetY = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1,targetY = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 9,targetY = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 9,targetY = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 2,targetY = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 2,targetY = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 8,targetY = 16) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 8,targetY = 16) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 4,targetY = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 4,targetY = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 31,targetY = 47) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 31,targetY = 47) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 2,targetY = 1048576) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 2,targetY = 1048576) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 17,targetY = 34) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 17,targetY = 34) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 100,targetY = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 100,targetY = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 19,targetY = 38) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 19,targetY = 38) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 13,targetY = 19) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 13,targetY = 19) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 100,targetY = 200) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 100,targetY = 200) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 63,targetY = 27) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 63,targetY = 27) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 13,targetY = 21) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 13,targetY = 21) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 5,targetY = 13) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 5,targetY = 13) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 16,targetY = 32) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 16,targetY = 32) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 10,targetY = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 10,targetY = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 987654321,targetY = 987654321) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 987654321,targetY = 987654321) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 27,targetY = 18) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 27,targetY = 18) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 77,targetY = 154) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 77,targetY = 154) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 49,targetY = 147) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 49,targetY = 147) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 31,targetY = 62) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 31,targetY = 62) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 255,targetY = 1023) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 255,targetY = 1023) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 512,targetY = 384) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 512,targetY = 384) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 16384,targetY = 8192) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 16384,targetY = 8192) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 88888,targetY = 55555) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 88888,targetY = 55555) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 512,targetY = 1025) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 512,targetY = 1025) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 128,targetY = 192) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 128,targetY = 192) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 18,targetY = 33) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 18,targetY = 33) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 77,targetY = 44) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 77,targetY = 44) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 27,targetY = 81) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 27,targetY = 81) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 999999999,targetY = 333333333) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 999999999,targetY = 333333333) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 17,targetY = 1024) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 17,targetY = 1024) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 5,targetY = 25) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 5,targetY = 25) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 65536,targetY = 129) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 65536,targetY = 129) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 3125,targetY = 243) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 3125,targetY = 243) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1234567,targetY = 7654321) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1234567,targetY = 7654321) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 32,targetY = 48) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 32,targetY = 48) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 999,targetY = 333) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 999,targetY = 333) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 987,targetY = 654) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 987,targetY = 654) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1023,targetY = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1023,targetY = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 123456,targetY = 654321) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 123456,targetY = 654321) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 123,targetY = 456) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 123,targetY = 456) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 31,targetY = 31) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 31,targetY = 31) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 63,targetY = 21) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 63,targetY = 21) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 8192,targetY = 16384) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 8192,targetY = 16384) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 511,targetY = 256) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 511,targetY = 256) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 54,targetY = 36) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 54,targetY = 36) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 19,targetY = 23) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 19,targetY = 23) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 99999,targetY = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 99999,targetY = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1000000000,targetY = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1000000000,targetY = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1000000000,targetY = 500000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1000000000,targetY = 500000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1024,targetY = 512) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1024,targetY = 512) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 81,targetY = 27) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 81,targetY = 27) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 15,targetY = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 15,targetY = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 256,targetY = 513) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 256,targetY = 513) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 256,targetY = 512) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 256,targetY = 512) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 81,targetY = 243) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 81,targetY = 243) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1073741824,targetY = 536870912) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1073741824,targetY = 536870912) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 32,targetY = 128) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 32,targetY = 128) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 97,targetY = 83) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 97,targetY = 83) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 256,targetY = 256) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 256,targetY = 256) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 77,targetY = 49) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 77,targetY = 49) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 256,targetY = 1024) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 256,targetY = 1024) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1001,targetY = 1003) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1001,targetY = 1003) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 511,targetY = 1024) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 511,targetY = 1024) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 128,targetY = 256) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 128,targetY = 256) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 65536,targetY = 32768) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 65536,targetY = 32768) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 777,targetY = 111) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 777,targetY = 111) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1,targetY = 1000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1,targetY = 1000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 33333,targetY = 22222) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 33333,targetY = 22222) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 999999937,targetY = 999999937) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 999999937,targetY = 999999937) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 33,targetY = 55) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 33,targetY = 55) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 3,targetY = 12) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 3,targetY = 12) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 1024,targetY = 2048) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 1024,targetY = 2048) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 255,targetY = 127) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 255,targetY = 127) == True: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 100,targetY = 25) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 100,targetY = 25) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 77,targetY = 33) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 77,targetY = 33) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 101,targetY = 101) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 101,targetY = 101) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 13,targetY = 39) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 13,targetY = 39) == False: {e}')
    
    total += 1
    try:
        result = candidate(targetX = 123456789,targetY = 987654321) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(targetX = 123456789,targetY = 987654321) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(targetX = 7,targetY = 3) == True
    assert candidate(targetX = 6,targetY = 9) == False
    assert candidate(targetX = 16,targetY = 8) == True
    assert candidate(targetX = 3,targetY = 5) == True
    assert candidate(targetX = 10,targetY = 1) == True
    assert candidate(targetX = 1,targetY = 1) == True
    assert candidate(targetX = 9,targetY = 6) == False
    assert candidate(targetX = 2,targetY = 2) == True
    assert candidate(targetX = 8,targetY = 16) == True
    assert candidate(targetX = 4,targetY = 7) == True
    assert candidate(targetX = 31,targetY = 47) == True
    assert candidate(targetX = 2,targetY = 1048576) == True
    assert candidate(targetX = 17,targetY = 34) == False
    assert candidate(targetX = 100,targetY = 1) == True
    assert candidate(targetX = 19,targetY = 38) == False
    assert candidate(targetX = 13,targetY = 19) == True
    assert candidate(targetX = 100,targetY = 200) == False
    assert candidate(targetX = 63,targetY = 27) == False
    assert candidate(targetX = 13,targetY = 21) == True
    assert candidate(targetX = 5,targetY = 13) == True
    assert candidate(targetX = 16,targetY = 32) == True
    assert candidate(targetX = 10,targetY = 10) == False
    assert candidate(targetX = 987654321,targetY = 987654321) == False
    assert candidate(targetX = 27,targetY = 18) == False
    assert candidate(targetX = 77,targetY = 154) == False
    assert candidate(targetX = 49,targetY = 147) == False
    assert candidate(targetX = 31,targetY = 62) == False
    assert candidate(targetX = 255,targetY = 1023) == False
    assert candidate(targetX = 512,targetY = 384) == True
    assert candidate(targetX = 16384,targetY = 8192) == True
    assert candidate(targetX = 88888,targetY = 55555) == False
    assert candidate(targetX = 512,targetY = 1025) == True
    assert candidate(targetX = 128,targetY = 192) == True
    assert candidate(targetX = 18,targetY = 33) == False
    assert candidate(targetX = 77,targetY = 44) == False
    assert candidate(targetX = 27,targetY = 81) == False
    assert candidate(targetX = 999999999,targetY = 333333333) == False
    assert candidate(targetX = 17,targetY = 1024) == True
    assert candidate(targetX = 5,targetY = 25) == False
    assert candidate(targetX = 65536,targetY = 129) == True
    assert candidate(targetX = 3125,targetY = 243) == True
    assert candidate(targetX = 1234567,targetY = 7654321) == True
    assert candidate(targetX = 32,targetY = 48) == True
    assert candidate(targetX = 999,targetY = 333) == False
    assert candidate(targetX = 987,targetY = 654) == False
    assert candidate(targetX = 1023,targetY = 1) == True
    assert candidate(targetX = 123456,targetY = 654321) == False
    assert candidate(targetX = 123,targetY = 456) == False
    assert candidate(targetX = 31,targetY = 31) == False
    assert candidate(targetX = 63,targetY = 21) == False
    assert candidate(targetX = 8192,targetY = 16384) == True
    assert candidate(targetX = 511,targetY = 256) == True
    assert candidate(targetX = 54,targetY = 36) == False
    assert candidate(targetX = 19,targetY = 23) == True
    assert candidate(targetX = 99999,targetY = 1) == True
    assert candidate(targetX = 1000000000,targetY = 1) == True
    assert candidate(targetX = 1000000000,targetY = 500000000) == False
    assert candidate(targetX = 1024,targetY = 512) == True
    assert candidate(targetX = 81,targetY = 27) == False
    assert candidate(targetX = 15,targetY = 10) == False
    assert candidate(targetX = 256,targetY = 513) == True
    assert candidate(targetX = 256,targetY = 512) == True
    assert candidate(targetX = 81,targetY = 243) == False
    assert candidate(targetX = 1073741824,targetY = 536870912) == True
    assert candidate(targetX = 32,targetY = 128) == True
    assert candidate(targetX = 97,targetY = 83) == True
    assert candidate(targetX = 256,targetY = 256) == True
    assert candidate(targetX = 77,targetY = 49) == False
    assert candidate(targetX = 256,targetY = 1024) == True
    assert candidate(targetX = 1001,targetY = 1003) == True
    assert candidate(targetX = 511,targetY = 1024) == True
    assert candidate(targetX = 128,targetY = 256) == True
    assert candidate(targetX = 65536,targetY = 32768) == True
    assert candidate(targetX = 777,targetY = 111) == False
    assert candidate(targetX = 1,targetY = 1000000000) == True
    assert candidate(targetX = 33333,targetY = 22222) == False
    assert candidate(targetX = 999999937,targetY = 999999937) == False
    assert candidate(targetX = 33,targetY = 55) == False
    assert candidate(targetX = 3,targetY = 12) == False
    assert candidate(targetX = 1024,targetY = 2048) == True
    assert candidate(targetX = 255,targetY = 127) == True
    assert candidate(targetX = 100,targetY = 25) == False
    assert candidate(targetX = 77,targetY = 33) == False
    assert candidate(targetX = 101,targetY = 101) == False
    assert candidate(targetX = 13,targetY = 39) == False
    assert candidate(targetX = 123456789,targetY = 987654321) == False


