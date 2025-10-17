def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(startValue = 2,target = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 2,target = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1000000000,target = 1) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1000000000,target = 1) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 7,target = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 7,target = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 2,target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 2,target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 3,target = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 3,target = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 100,target = 99) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 100,target = 99) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 10,target = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 10,target = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1,target = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1,target = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1,target = 1000000000) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1,target = 1000000000) == 39: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 5,target = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 5,target = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1,target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1,target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 4,target = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 4,target = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 100,target = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 100,target = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 7,target = 19) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 7,target = 19) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 8,target = 16) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 8,target = 16) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 9,target = 28) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 9,target = 28) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1000000,target = 1000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1000000,target = 1000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 123456,target = 654321) == 41671
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 123456,target = 654321) == 41671: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 2,target = 3000000000) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 2,target = 3000000000) == 43: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1000,target = 1001) == 501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1000,target = 1001) == 501: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 15,target = 1) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 15,target = 1) == 14: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1000000,target = 999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1000000,target = 999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 2,target = 1024) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 2,target = 1024) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1024,target = 1) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1024,target = 1) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 2,target = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 2,target = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 10,target = 11) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 10,target = 11) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 50,target = 1000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 50,target = 1000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 7,target = 128) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 7,target = 128) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 3,target = 1023) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 3,target = 1023) == 11: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 23,target = 17) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 23,target = 17) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 500,target = 1000000) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 500,target = 1000000) == 26: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 2,target = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 2,target = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 50,target = 101) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 50,target = 101) == 28: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 15,target = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 15,target = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 12,target = 32) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 12,target = 32) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 3,target = 33) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 3,target = 33) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1000000,target = 1000001) == 500001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1000000,target = 1000001) == 500001: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 500,target = 1023) == 247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 500,target = 1023) == 247: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 7,target = 47) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 7,target = 47) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 13,target = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 13,target = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 15,target = 97) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 15,target = 97) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 123456789,target = 987654321) == 61728401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 123456789,target = 987654321) == 61728401: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 25,target = 24) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 25,target = 24) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 2345678,target = 8765432) == 154322
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 2345678,target = 8765432) == 154322: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 256,target = 2048) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 256,target = 2048) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 12345,target = 54321) == 5560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 12345,target = 54321) == 5560: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 20,target = 25) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 20,target = 25) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 6,target = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 6,target = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 500000000,target = 750000000) == 125000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 500000000,target = 750000000) == 125000001: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 15,target = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 15,target = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1000,target = 500) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1000,target = 500) == 500: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 9,target = 18) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 9,target = 18) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 7,target = 1000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 7,target = 1000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 31,target = 15) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 31,target = 15) == 16: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 15,target = 300) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 15,target = 300) == 12: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 2,target = 2048) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 2,target = 2048) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 10,target = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 10,target = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 5,target = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 5,target = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 25,target = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 25,target = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 20,target = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 20,target = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 15,target = 31) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 15,target = 31) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 7,target = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 7,target = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 8,target = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 8,target = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 7,target = 100) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 7,target = 100) == 6: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 999999999,target = 1000000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 999999999,target = 1000000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 64,target = 32) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 64,target = 32) == 32: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 8,target = 1000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 8,target = 1000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 15,target = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 15,target = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 12345,target = 67890) == 3863
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 12345,target = 67890) == 3863: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 3,target = 123456789) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 3,target = 123456789) == 39: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 5,target = 123) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 5,target = 123) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1024,target = 512) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1024,target = 512) == 512: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1000000,target = 10000000) == 375004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1000000,target = 10000000) == 375004: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 12345,target = 98765) == 6178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 12345,target = 98765) == 6178: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 10,target = 31) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 10,target = 31) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1,target = 1000000) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1,target = 1000000) == 28: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 8,target = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 8,target = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 123,target = 456) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 123,target = 456) == 11: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 100,target = 1) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 100,target = 1) == 99: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 2,target = 1025) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 2,target = 1025) == 20: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 3456,target = 6789) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 3456,target = 6789) == 63: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 500000000,target = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 500000000,target = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 1023,target = 1024) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 1023,target = 1024) == 512: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 8,target = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 8,target = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 7,target = 101) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 7,target = 101) == 7: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 31,target = 8) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 31,target = 8) == 23: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 3,target = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 3,target = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 500,target = 250) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 500,target = 250) == 250: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 987654321,target = 123456789) == 864197532
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 987654321,target = 123456789) == 864197532: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 500,target = 1024) == 246
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 500,target = 1024) == 246: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 7,target = 150) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 7,target = 150) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 8,target = 64) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 8,target = 64) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 6,target = 32) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 6,target = 32) == 5: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 10,target = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 10,target = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 13,target = 169) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 13,target = 169) == 9: {e}')
    
    total += 1
    try:
        result = candidate(startValue = 8,target = 1024) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startValue = 8,target = 1024) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(startValue = 2,target = 3) == 2
    assert candidate(startValue = 1000000000,target = 1) == 999999999
    assert candidate(startValue = 7,target = 15) == 6
    assert candidate(startValue = 2,target = 1) == 1
    assert candidate(startValue = 3,target = 10) == 3
    assert candidate(startValue = 100,target = 99) == 1
    assert candidate(startValue = 10,target = 1) == 9
    assert candidate(startValue = 1,target = 2) == 1
    assert candidate(startValue = 1,target = 1000000000) == 39
    assert candidate(startValue = 5,target = 8) == 2
    assert candidate(startValue = 1,target = 1) == 0
    assert candidate(startValue = 4,target = 7) == 2
    assert candidate(startValue = 100,target = 100) == 0
    assert candidate(startValue = 7,target = 19) == 5
    assert candidate(startValue = 8,target = 16) == 1
    assert candidate(startValue = 9,target = 28) == 4
    assert candidate(startValue = 1000000,target = 1000000) == 0
    assert candidate(startValue = 123456,target = 654321) == 41671
    assert candidate(startValue = 2,target = 3000000000) == 43
    assert candidate(startValue = 1000,target = 1001) == 501
    assert candidate(startValue = 15,target = 1) == 14
    assert candidate(startValue = 1000000,target = 999999) == 1
    assert candidate(startValue = 2,target = 1024) == 9
    assert candidate(startValue = 1024,target = 1) == 1023
    assert candidate(startValue = 2,target = 1023) == 10
    assert candidate(startValue = 10,target = 11) == 6
    assert candidate(startValue = 50,target = 1000) == 25
    assert candidate(startValue = 7,target = 128) == 8
    assert candidate(startValue = 3,target = 1023) == 11
    assert candidate(startValue = 23,target = 17) == 6
    assert candidate(startValue = 500,target = 1000000) == 26
    assert candidate(startValue = 2,target = 100) == 9
    assert candidate(startValue = 50,target = 101) == 28
    assert candidate(startValue = 15,target = 20) == 6
    assert candidate(startValue = 12,target = 32) == 6
    assert candidate(startValue = 3,target = 33) == 8
    assert candidate(startValue = 1000000,target = 1000001) == 500001
    assert candidate(startValue = 500,target = 1023) == 247
    assert candidate(startValue = 7,target = 47) == 5
    assert candidate(startValue = 13,target = 1) == 12
    assert candidate(startValue = 15,target = 97) == 8
    assert candidate(startValue = 123456789,target = 987654321) == 61728401
    assert candidate(startValue = 25,target = 24) == 1
    assert candidate(startValue = 2345678,target = 8765432) == 154322
    assert candidate(startValue = 256,target = 2048) == 3
    assert candidate(startValue = 12345,target = 54321) == 5560
    assert candidate(startValue = 20,target = 25) == 9
    assert candidate(startValue = 6,target = 9) == 3
    assert candidate(startValue = 500000000,target = 750000000) == 125000001
    assert candidate(startValue = 15,target = 10) == 5
    assert candidate(startValue = 1000,target = 500) == 500
    assert candidate(startValue = 9,target = 18) == 1
    assert candidate(startValue = 7,target = 1000) == 13
    assert candidate(startValue = 31,target = 15) == 16
    assert candidate(startValue = 15,target = 300) == 12
    assert candidate(startValue = 2,target = 2048) == 10
    assert candidate(startValue = 10,target = 15) == 4
    assert candidate(startValue = 5,target = 1023) == 10
    assert candidate(startValue = 25,target = 100) == 2
    assert candidate(startValue = 20,target = 5) == 15
    assert candidate(startValue = 15,target = 31) == 10
    assert candidate(startValue = 7,target = 1) == 6
    assert candidate(startValue = 8,target = 20) == 5
    assert candidate(startValue = 7,target = 100) == 6
    assert candidate(startValue = 999999999,target = 1000000000) == 500000000
    assert candidate(startValue = 64,target = 32) == 32
    assert candidate(startValue = 8,target = 1000) == 9
    assert candidate(startValue = 15,target = 7) == 8
    assert candidate(startValue = 12345,target = 67890) == 3863
    assert candidate(startValue = 3,target = 123456789) == 39
    assert candidate(startValue = 5,target = 123) == 8
    assert candidate(startValue = 1024,target = 512) == 512
    assert candidate(startValue = 1000000,target = 10000000) == 375004
    assert candidate(startValue = 12345,target = 98765) == 6178
    assert candidate(startValue = 10,target = 31) == 5
    assert candidate(startValue = 1,target = 1000000) == 28
    assert candidate(startValue = 8,target = 1) == 7
    assert candidate(startValue = 123,target = 456) == 11
    assert candidate(startValue = 100,target = 1) == 99
    assert candidate(startValue = 2,target = 1025) == 20
    assert candidate(startValue = 3456,target = 6789) == 63
    assert candidate(startValue = 500000000,target = 1000000000) == 1
    assert candidate(startValue = 1023,target = 1024) == 512
    assert candidate(startValue = 8,target = 15) == 2
    assert candidate(startValue = 7,target = 101) == 7
    assert candidate(startValue = 31,target = 8) == 23
    assert candidate(startValue = 3,target = 9) == 4
    assert candidate(startValue = 500,target = 250) == 250
    assert candidate(startValue = 987654321,target = 123456789) == 864197532
    assert candidate(startValue = 500,target = 1024) == 246
    assert candidate(startValue = 7,target = 150) == 9
    assert candidate(startValue = 8,target = 64) == 3
    assert candidate(startValue = 6,target = 32) == 5
    assert candidate(startValue = 10,target = 1023) == 10
    assert candidate(startValue = 13,target = 169) == 9
    assert candidate(startValue = 8,target = 1024) == 7


