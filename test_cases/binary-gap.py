def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1041) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1041) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001001001) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001001001) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 8589934591) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8589934591) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 67890) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67890) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108863) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108863) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100111011000110001) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100111011000110001) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001001001001001001001001001001) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001001001001001001001001001001) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870913) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870913) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 511) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 511) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 21845) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21845) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870912) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870912) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1177777777) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1177777777) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1879048192) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1879048192) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000100001) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000100001) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 665772) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 665772) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 6754321) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6754321) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 67) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 983041) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 983041) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217729) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217729) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000010000100001) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000010000100001) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 777777777) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777777777) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741824) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741824) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194305) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194305) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 807798533) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 807798533) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 131073) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131073) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 1010101010101010101) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010101010101010101) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10011001100110011001100110011001) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10011001100110011001100110011001) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999937) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999937) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741825) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741825) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10011001100110011001) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10011001100110011001) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 11001100110011001100110011001100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11001100110011001100110011001100) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 0
    assert candidate(n = 3) == 1
    assert candidate(n = 1041) == 6
    assert candidate(n = 15) == 1
    assert candidate(n = 22) == 2
    assert candidate(n = 32) == 0
    assert candidate(n = 6) == 1
    assert candidate(n = 1) == 0
    assert candidate(n = 1000000000) == 3
    assert candidate(n = 7) == 1
    assert candidate(n = 13) == 2
    assert candidate(n = 5) == 2
    assert candidate(n = 29) == 2
    assert candidate(n = 1001001001) == 7
    assert candidate(n = 131071) == 1
    assert candidate(n = 999999999) == 3
    assert candidate(n = 8589934591) == 1
    assert candidate(n = 47) == 2
    assert candidate(n = 67890) == 5
    assert candidate(n = 67108863) == 1
    assert candidate(n = 2147483647) == 1
    assert candidate(n = 100111011000110001) == 6
    assert candidate(n = 1001001001001001001001001001001) == 8
    assert candidate(n = 536870913) == 29
    assert candidate(n = 511) == 1
    assert candidate(n = 21845) == 2
    assert candidate(n = 536870912) == 0
    assert candidate(n = 1177777777) == 4
    assert candidate(n = 1879048192) == 1
    assert candidate(n = 10000100001) == 7
    assert candidate(n = 665772) == 4
    assert candidate(n = 6754321) == 8
    assert candidate(n = 67) == 5
    assert candidate(n = 134217727) == 1
    assert candidate(n = 37) == 3
    assert candidate(n = 33) == 5
    assert candidate(n = 8388607) == 1
    assert candidate(n = 983041) == 16
    assert candidate(n = 1001) == 3
    assert candidate(n = 134217729) == 27
    assert candidate(n = 1000010000100001) == 8
    assert candidate(n = 101010101) == 7
    assert candidate(n = 1024) == 0
    assert candidate(n = 16777215) == 1
    assert candidate(n = 777777777) == 4
    assert candidate(n = 1073741824) == 0
    assert candidate(n = 4194305) == 22
    assert candidate(n = 1048576) == 0
    assert candidate(n = 807798533) == 7
    assert candidate(n = 18) == 3
    assert candidate(n = 131073) == 17
    assert candidate(n = 1010101010101010101) == 7
    assert candidate(n = 65535) == 1
    assert candidate(n = 127) == 1
    assert candidate(n = 10011001100110011001100110011001) == 8
    assert candidate(n = 987654321) == 4
    assert candidate(n = 1111111111) == 5
    assert candidate(n = 999999937) == 6
    assert candidate(n = 500000000) == 3
    assert candidate(n = 31) == 1
    assert candidate(n = 123456789) == 4
    assert candidate(n = 1073741825) == 30
    assert candidate(n = 33554431) == 1
    assert candidate(n = 10011001100110011001) == 5
    assert candidate(n = 11001100110011001100110011001100) == 5


