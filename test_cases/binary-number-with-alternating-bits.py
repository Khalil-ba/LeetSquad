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
        result = candidate(n = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483646) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483646) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 357913941) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 357913941) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 170) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 170) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 178956970) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 178956970) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 11184810) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11184810) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2863311531) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2863311531) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 341) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 341) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967295) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967295) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108863) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108863) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000001) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000001) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 21845) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21845) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1010101010101010101010101010101) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010101010101010101010101010101) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2047) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2047) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 262143) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262143) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16383) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16383) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435455) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435455) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483649) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483649) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1431655765) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1431655765) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 715827882) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 715827882) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217728) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217728) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097151) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097151) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1365) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1365) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 682) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 682) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 42) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 858993459) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 858993459) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4095) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4095) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 255) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 22369621) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22369621) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967294) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967294) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 44739242) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44739242) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555555) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555555) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 218) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 218) == False: {e}')
    
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
        result = candidate(n = 1010101010) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010101010) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 286331153) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 286331153) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 517) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 517) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 89478485) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89478485) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3427813328) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3427813328) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == False
    assert candidate(n = 11) == False
    assert candidate(n = 15) == False
    assert candidate(n = 2) == True
    assert candidate(n = 1) == True
    assert candidate(n = 7) == False
    assert candidate(n = 10) == True
    assert candidate(n = 5) == True
    assert candidate(n = 63) == False
    assert candidate(n = 33554431) == False
    assert candidate(n = 131071) == False
    assert candidate(n = 2147483646) == False
    assert candidate(n = 357913941) == True
    assert candidate(n = 21) == True
    assert candidate(n = 170) == True
    assert candidate(n = 178956970) == True
    assert candidate(n = 11184810) == True
    assert candidate(n = 2863311531) == False
    assert candidate(n = 341) == True
    assert candidate(n = 4294967295) == False
    assert candidate(n = 2147483647) == False
    assert candidate(n = 32767) == False
    assert candidate(n = 67108863) == False
    assert candidate(n = 100000001) == False
    assert candidate(n = 21845) == True
    assert candidate(n = 1010101010101010101010101010101) == False
    assert candidate(n = 2047) == False
    assert candidate(n = 262143) == False
    assert candidate(n = 16383) == False
    assert candidate(n = 524287) == False
    assert candidate(n = 268435455) == False
    assert candidate(n = 4194303) == False
    assert candidate(n = 2147483649) == False
    assert candidate(n = 1431655765) == True
    assert candidate(n = 4) == False
    assert candidate(n = 134217727) == False
    assert candidate(n = 715827882) == True
    assert candidate(n = 8388607) == False
    assert candidate(n = 134217728) == False
    assert candidate(n = 2097151) == False
    assert candidate(n = 1365) == True
    assert candidate(n = 33) == False
    assert candidate(n = 1073741823) == False
    assert candidate(n = 682) == True
    assert candidate(n = 101010101) == False
    assert candidate(n = 42) == True
    assert candidate(n = 16777215) == False
    assert candidate(n = 858993459) == False
    assert candidate(n = 4095) == False
    assert candidate(n = 8) == False
    assert candidate(n = 255) == False
    assert candidate(n = 22369621) == True
    assert candidate(n = 8191) == False
    assert candidate(n = 4294967294) == False
    assert candidate(n = 18) == False
    assert candidate(n = 44739242) == True
    assert candidate(n = 1023) == False
    assert candidate(n = 555555555) == False
    assert candidate(n = 20) == False
    assert candidate(n = 218) == False
    assert candidate(n = 65535) == False
    assert candidate(n = 1000000001) == False
    assert candidate(n = 1010101010) == False
    assert candidate(n = 286331153) == False
    assert candidate(n = 85) == True
    assert candidate(n = 517) == False
    assert candidate(n = 1048575) == False
    assert candidate(n = 89478485) == True
    assert candidate(n = 536870911) == False
    assert candidate(n = 31) == False
    assert candidate(n = 6) == False
    assert candidate(n = 3427813328) == False


