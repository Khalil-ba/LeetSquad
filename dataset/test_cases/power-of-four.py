def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -16) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -16) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870912) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870912) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967295) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967295) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435456) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435456) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777216) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777216) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -2147483648) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -2147483648) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -4) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967296) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967296) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000003) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000003) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1099511627776) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1099511627776) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -4294967296) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -4294967296) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 18446744073709551615) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18446744073709551615) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1431655765) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1431655765) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000002) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000002) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16384) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16384) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483649) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483649) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = -1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -1) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2199023255552) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2199023255552) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194304) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194304) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1152921504606846976) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1152921504606846976) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = -65536) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = -65536) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 34359738368) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34359738368) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 9223372036854775807) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9223372036854775807) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741824) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741824) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 18014398509481984) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18014398509481984) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 255) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483648) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483648) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 17179869184) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17179869184) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4611686018427387904) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4611686018427387904) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000004) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000004) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 35184372088832) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35184372088832) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 72057594037927936) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72057594037927936) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741825) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741825) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18446744073709551616) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18446744073709551616) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == False
    assert candidate(n = -16) == False
    assert candidate(n = 2147483647) == False
    assert candidate(n = 536870912) == False
    assert candidate(n = 4294967295) == False
    assert candidate(n = 268435456) == True
    assert candidate(n = 5) == False
    assert candidate(n = 16777216) == True
    assert candidate(n = 4) == True
    assert candidate(n = 64) == True
    assert candidate(n = 16) == True
    assert candidate(n = 2) == False
    assert candidate(n = 1024) == True
    assert candidate(n = 0) == False
    assert candidate(n = 8) == False
    assert candidate(n = -2147483648) == False
    assert candidate(n = 1048576) == True
    assert candidate(n = 2048) == False
    assert candidate(n = 65536) == True
    assert candidate(n = 18) == False
    assert candidate(n = 256) == True
    assert candidate(n = -4) == False
    assert candidate(n = 4294967296) == True
    assert candidate(n = 1) == True
    assert candidate(n = 1000000003) == False
    assert candidate(n = 1099511627776) == True
    assert candidate(n = -4294967296) == False
    assert candidate(n = 4096) == True
    assert candidate(n = 18446744073709551615) == False
    assert candidate(n = 1431655765) == False
    assert candidate(n = 1000000002) == False
    assert candidate(n = 16384) == True
    assert candidate(n = 2147483649) == False
    assert candidate(n = -1) == False
    assert candidate(n = 2199023255552) == True
    assert candidate(n = 4194304) == True
    assert candidate(n = 1073741823) == False
    assert candidate(n = 1152921504606846976) == True
    assert candidate(n = -65536) == False
    assert candidate(n = 34359738368) == True
    assert candidate(n = 9223372036854775807) == False
    assert candidate(n = 1073741824) == True
    assert candidate(n = 18014398509481984) == True
    assert candidate(n = 255) == False
    assert candidate(n = 2147483648) == False
    assert candidate(n = 17179869184) == True
    assert candidate(n = 4611686018427387904) == True
    assert candidate(n = 1000000000) == False
    assert candidate(n = 65535) == False
    assert candidate(n = 1000000001) == False
    assert candidate(n = 1000000004) == False
    assert candidate(n = 15) == False
    assert candidate(n = 35184372088832) == True
    assert candidate(n = 72057594037927936) == True
    assert candidate(n = 1073741825) == False
    assert candidate(n = 7) == False
    assert candidate(n = 10) == False
    assert candidate(n = 18446744073709551616) == True


