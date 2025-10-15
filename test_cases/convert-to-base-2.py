def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == "111": {e}')
    
    total += 1
    try:
        result = candidate(n = 104730) == "1101110100101101110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104730) == "1101110100101101110": {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == "110100100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == "110100100": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == "10000111000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == "10000111000": {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == "101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == "101": {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == "100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == "100": {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == "10000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == "10000": {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == "111101100010000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == "111101100010000": {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == "110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == "110": {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == "10000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == "10000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 0) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == "0": {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == "11000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == "11000": {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == "10000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == "10000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == "1001100111011111101111000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == "1001100111011111101111000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 104729) == "1101110100101101001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104729) == "1101110100101101001": {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == "10011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == "10011": {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == "11001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == "11001": {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == "11010"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == "11010": {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == "1": {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == "11011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == "11011": {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == "11110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == "11110": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999992) == "1001100111011111101111000001000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999992) == "1001100111011111101111000001000": {e}')
    
    total += 1
    try:
        result = candidate(n = 1099511627776) == "10000000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1099511627776) == "10000000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == "1001100111011111101111000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == "1001100111011111101111000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999996) == "1001100111011111101111000001100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999996) == "1001100111011111101111000001100": {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == "110000000000000000000000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == "110000000000000000000000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 32767) == "11000000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32767) == "11000000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 511) == "11000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 511) == "11000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 536870912) == "1100000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870912) == "1100000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967295) == "100000000000000000000000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967295) == "100000000000000000000000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 524288) == "110000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524288) == "110000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 2047) == "1100000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2047) == "1100000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 16383) == "100000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16383) == "100000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999998) == "1001100111011111101111000000010"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999998) == "1001100111011111101111000000010": {e}')
    
    total += 1
    try:
        result = candidate(n = 134217728) == "11000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217728) == "11000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823) == "1000000000000000000000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823) == "1000000000000000000000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000) == "1110000111100110001100000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000) == "1110000111100110001100000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741824) == "1000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741824) == "1000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 333333333) == "10100001000100100011101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333333) == "10100001000100100011101010101": {e}')
    
    total += 1
    try:
        result = candidate(n = 4095) == "1000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4095) == "1000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999995) == "1001100111011111101111000001111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999995) == "1001100111011111101111000001111": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999994) == "1001100111011111101111000001110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999994) == "1001100111011111101111000001110": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999991) == "1001100111011111101111000001011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999991) == "1001100111011111101111000001011": {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576) == "100000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576) == "100000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == "110000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == "110000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 255) == "100000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255) == "100000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 8191) == "110000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8191) == "110000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == "10000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == "10000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 68719476736) == "1000000000000000000000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 68719476736) == "1000000000000000000000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 1099511627775) == "10000000000000000000000000000000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1099511627775) == "10000000000000000000000000000000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 262144) == "1000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 262144) == "1000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == "10000000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == "10000000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 131072) == "1100000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131072) == "1100000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 127) == "110000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 127) == "110000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999993) == "1001100111011111101111000001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999993) == "1001100111011111101111000001001": {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == "1001111001000111011100111110001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == "1001111001000111011100111110001": {e}')
    
    total += 1
    try:
        result = candidate(n = 894752631) == "1110101010101010010100010001011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 894752631) == "1110101010101010010100010001011": {e}')
    
    total += 1
    try:
        result = candidate(n = 897410135) == "1001010100000101010010110101011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 897410135) == "1001010100000101010010110101011": {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == "110001110000101100000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == "110001110000101100000": {e}')
    
    total += 1
    try:
        result = candidate(n = 32768) == "11000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32768) == "11000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999997) == "1001100111011111101111000001101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999997) == "1001100111011111101111000001101": {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575) == "100000000000000000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575) == "100000000000000000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == "1100010110100101010010100000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == "1100010110100101010010100000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == "1100011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == "1100011": {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == "100110100011001000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == "100110100011001000000": {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == "11000101011001101110100010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == "11000101011001101110100010101": {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == "100110100011001000011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == "100110100011001000011": {e}')
    
    total += 1
    try:
        result = candidate(n = 1099511627777) == "10000000000000000000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1099511627777) == "10000000000000000000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(n = 531441) == "110000110110000110001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 531441) == "110000110110000110001": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == "111"
    assert candidate(n = 104730) == "1101110100101101110"
    assert candidate(n = 100) == "110100100"
    assert candidate(n = 1000) == "10000111000"
    assert candidate(n = 5) == "101"
    assert candidate(n = 4) == "100"
    assert candidate(n = 16) == "10000"
    assert candidate(n = 10000) == "111101100010000"
    assert candidate(n = 2) == "110"
    assert candidate(n = 1024) == "10000000000"
    assert candidate(n = 0) == "0"
    assert candidate(n = 8) == "11000"
    assert candidate(n = 1023) == "10000000011"
    assert candidate(n = 1000000000) == "1001100111011111101111000000000"
    assert candidate(n = 104729) == "1101110100101101001"
    assert candidate(n = 15) == "10011"
    assert candidate(n = 9) == "11001"
    assert candidate(n = 6) == "11010"
    assert candidate(n = 1) == "1"
    assert candidate(n = 7) == "11011"
    assert candidate(n = 10) == "11110"
    assert candidate(n = 999999992) == "1001100111011111101111000001000"
    assert candidate(n = 1099511627776) == "10000000000000000000000000000000000000000"
    assert candidate(n = 999999999) == "1001100111011111101111000000011"
    assert candidate(n = 999999996) == "1001100111011111101111000001100"
    assert candidate(n = 2147483647) == "110000000000000000000000000000011"
    assert candidate(n = 32767) == "11000000000000011"
    assert candidate(n = 511) == "11000000011"
    assert candidate(n = 536870912) == "1100000000000000000000000000000"
    assert candidate(n = 4294967295) == "100000000000000000000000000000011"
    assert candidate(n = 524288) == "110000000000000000000"
    assert candidate(n = 2047) == "1100000000011"
    assert candidate(n = 16383) == "100000000000011"
    assert candidate(n = 999999998) == "1001100111011111101111000000010"
    assert candidate(n = 134217728) == "11000000000000000000000000000"
    assert candidate(n = 1073741823) == "1000000000000000000000000000011"
    assert candidate(n = 800000000) == "1110000111100110001100000000000"
    assert candidate(n = 1073741824) == "1000000000000000000000000000000"
    assert candidate(n = 333333333) == "10100001000100100011101010101"
    assert candidate(n = 4095) == "1000000000011"
    assert candidate(n = 999999995) == "1001100111011111101111000001111"
    assert candidate(n = 999999994) == "1001100111011111101111000001110"
    assert candidate(n = 999999991) == "1001100111011111101111000001011"
    assert candidate(n = 1048576) == "100000000000000000000"
    assert candidate(n = 8192) == "110000000000000"
    assert candidate(n = 255) == "100000011"
    assert candidate(n = 8191) == "110000000000011"
    assert candidate(n = 65536) == "10000000000000000"
    assert candidate(n = 68719476736) == "1000000000000000000000000000000000000"
    assert candidate(n = 1099511627775) == "10000000000000000000000000000000000000011"
    assert candidate(n = 262144) == "1000000000000000000"
    assert candidate(n = 65535) == "10000000000000011"
    assert candidate(n = 131072) == "1100000000000000000"
    assert candidate(n = 127) == "110000011"
    assert candidate(n = 999999993) == "1001100111011111101111000001001"
    assert candidate(n = 987654321) == "1001111001000111011100111110001"
    assert candidate(n = 894752631) == "1110101010101010010100010001011"
    assert candidate(n = 897410135) == "1001010100000101010010110101011"
    assert candidate(n = 500000) == "110001110000101100000"
    assert candidate(n = 32768) == "11000000000000000"
    assert candidate(n = 999999997) == "1001100111011111101111000001101"
    assert candidate(n = 1048575) == "100000000000000000011"
    assert candidate(n = 500000000) == "1100010110100101010010100000000"
    assert candidate(n = 31) == "1100011"
    assert candidate(n = 1000000) == "100110100011001000000"
    assert candidate(n = 123456789) == "11000101011001101110100010101"
    assert candidate(n = 999999) == "100110100011001000011"
    assert candidate(n = 1099511627777) == "10000000000000000000000000000000000000001"
    assert candidate(n = 531441) == "110000110110000110001"


