def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 46875) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 46875) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3245) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3245) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 86) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 86) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4326) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4326) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 82084) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 82084) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 821) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 821) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 46) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 46) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4102) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4102) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 462) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 462) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 862467834) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 862467834) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8258) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8258) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097152) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097152) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 786432) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 786432) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3145728) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3145728) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 885842624) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 885842624) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2359296) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2359296) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108864) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108864) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 891891891) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 891891891) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8256) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8256) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 683184) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 683184) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870912) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870912) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 111222333) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111222333) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 524288) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524288) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 82944) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 82944) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 94371840) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 94371840) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16384) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16384) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 393216) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 393216) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777216) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777216) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 258048) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 258048) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 125874) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125874) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 78125) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 78125) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024576) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024576) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2415919) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2415919) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217728) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217728) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 46340) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 46340) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9437184) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9437184) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554432) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554432) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 900000000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900000000) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741824) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741824) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2176782336) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2176782336) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 24681357) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24681357) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 333333333) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333333) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2621440) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2621440) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 22448811) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22448811) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 112233445566778899) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 112233445566778899) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 327684) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 327684) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 768) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 768) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 196608) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 196608) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 27962028) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27962028) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 894784864) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 894784864) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 43112) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43112) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 262144) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262144) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 131072) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131072) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 82128) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 82128) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 31415926) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31415926) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 499999999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499999999) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 318666) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 318666) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 180) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8589934592) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8589934592) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 32768) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32768) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3221225472) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3221225472) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4104) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4104) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 35184372088832) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35184372088832) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4608) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4608) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388608) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388608) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 46875) == False
    assert candidate(n = 3245) == False
    assert candidate(n = 86) == False
    assert candidate(n = 10) == False
    assert candidate(n = 4326) == False
    assert candidate(n = 16) == True
    assert candidate(n = 82084) == False
    assert candidate(n = 1024) == True
    assert candidate(n = 128) == True
    assert candidate(n = 821) == True
    assert candidate(n = 8192) == True
    assert candidate(n = 65536) == True
    assert candidate(n = 46) == True
    assert candidate(n = 256) == True
    assert candidate(n = 1000000000) == False
    assert candidate(n = 24) == False
    assert candidate(n = 987654321) == False
    assert candidate(n = 512) == True
    assert candidate(n = 4102) == True
    assert candidate(n = 1) == True
    assert candidate(n = 462) == False
    assert candidate(n = 862467834) == False
    assert candidate(n = 8258) == False
    assert candidate(n = 2097152) == True
    assert candidate(n = 786432) == False
    assert candidate(n = 3145728) == False
    assert candidate(n = 885842624) == False
    assert candidate(n = 999999999) == False
    assert candidate(n = 2359296) == False
    assert candidate(n = 67108864) == True
    assert candidate(n = 4096) == True
    assert candidate(n = 891891891) == False
    assert candidate(n = 2147483647) == False
    assert candidate(n = 8256) == False
    assert candidate(n = 683184) == False
    assert candidate(n = 536870912) == True
    assert candidate(n = 111222333) == False
    assert candidate(n = 524288) == True
    assert candidate(n = 82944) == False
    assert candidate(n = 94371840) == False
    assert candidate(n = 16384) == True
    assert candidate(n = 393216) == False
    assert candidate(n = 16777216) == True
    assert candidate(n = 258048) == False
    assert candidate(n = 125874) == False
    assert candidate(n = 78125) == False
    assert candidate(n = 1024576) == False
    assert candidate(n = 2415919) == False
    assert candidate(n = 134217728) == True
    assert candidate(n = 46340) == False
    assert candidate(n = 9437184) == False
    assert candidate(n = 33554432) == True
    assert candidate(n = 900000000) == False
    assert candidate(n = 1073741824) == False
    assert candidate(n = 2176782336) == False
    assert candidate(n = 24681357) == False
    assert candidate(n = 333333333) == False
    assert candidate(n = 2621440) == False
    assert candidate(n = 1048576) == True
    assert candidate(n = 9876543210) == False
    assert candidate(n = 2048) == True
    assert candidate(n = 22448811) == False
    assert candidate(n = 112233445566778899) == False
    assert candidate(n = 327684) == False
    assert candidate(n = 18) == False
    assert candidate(n = 768) == False
    assert candidate(n = 196608) == False
    assert candidate(n = 27962028) == False
    assert candidate(n = 894784864) == False
    assert candidate(n = 43112) == False
    assert candidate(n = 262144) == True
    assert candidate(n = 131072) == True
    assert candidate(n = 82128) == False
    assert candidate(n = 111111111) == False
    assert candidate(n = 31415926) == False
    assert candidate(n = 499999999) == False
    assert candidate(n = 318666) == False
    assert candidate(n = 180) == False
    assert candidate(n = 8589934592) == False
    assert candidate(n = 32768) == True
    assert candidate(n = 3221225472) == False
    assert candidate(n = 4104) == False
    assert candidate(n = 35184372088832) == False
    assert candidate(n = 123456789) == False
    assert candidate(n = 555555) == False
    assert candidate(n = 4608) == False
    assert candidate(n = 8388608) == True


