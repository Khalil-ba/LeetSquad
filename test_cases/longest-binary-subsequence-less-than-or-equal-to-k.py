def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "0000000",k = 0) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000",k = 0) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111",k = 127) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111",k = 127) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111",k = 127) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111",k = 127) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011",k = 255) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011",k = 255) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011",k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011",k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010",k = 512) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010",k = 512) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010",k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010",k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111",k = 50) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111",k = 50) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101001",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101001",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111",k = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111",k = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101",k = 512) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101",k = 512) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101",k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101",k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011",k = 500) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011",k = 500) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000",k = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000",k = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001010",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001010",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000",k = 1000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000",k = 1000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101",k = 255) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101",k = 255) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "1",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111",k = 255) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111",k = 255) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100",k = 31) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100",k = 31) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0",k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0",k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000",k = 100000) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000",k = 100000) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011",k = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011",k = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010",k = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010",k = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "100110011001100110",k = 1000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100110011001100110",k = 1000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000",k = 0) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000",k = 0) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100",k = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100",k = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000",k = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000",k = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "00101001",k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00101001",k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101",k = 10000) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101",k = 10000) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "100101010010101010101010",k = 1024) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100101010010101010101010",k = 1024) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101",k = 1048575) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101",k = 1048575) == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100110011001100110011001100110011001100",k = 1000000) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100110011001100110011001100110011001100",k = 1000000) == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010",k = 10) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010",k = 10) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010101010",k = 1023) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010101010",k = 1023) == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100110011001100110011001100",k = 65535) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100110011001100110011001100",k = 65535) == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "001100110011001100110011001100110011001100110011001100110011",k = 4096) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001100110011001100110011001100110011001100110011001100110011",k = 4096) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",k = 0) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",k = 0) == 87: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111111111111111",k = 1073741823) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111111111111111",k = 1073741823) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101101101101101101101",k = 1000) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101101101101101101101",k = 1000) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111111111111111111111111111",k = 2047) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111111111111111111111111111",k = 2047) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000000000",k = 1000) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000000000",k = 1000) == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101",k = 1023) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101",k = 1023) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111000011110000111100001111000011110000111100001111",k = 32767) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111000011110000111100001111000011110000111100001111",k = 32767) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001",k = 10000) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001",k = 10000) == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "11010110101101011010110101101011010110101101011010110101",k = 1048575) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11010110101101011010110101101011010110101101011010110101",k = 1048575) == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001001001001001",k = 5000) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001001001001001",k = 5000) == 43: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100110011001100110011001100110011001100110011001100110011001100",k = 128) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100110011001100110011001100110011001100110011001100110011001100",k = 128) == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "10010101010101010101",k = 30000) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10010101010101010101",k = 30000) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000111000111000111000111000111000",k = 50000) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000111000111000111000111000111000",k = 50000) == 43: {e}')
    
    total += 1
    try:
        result = candidate(s = "11010101010101010101",k = 16383) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11010101010101010101",k = 16383) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101001101001101001101001101001",k = 1024) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101001101001101001101001101001",k = 1024) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111",k = 1024) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111",k = 1024) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101",k = 10) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101",k = 10) == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001100110011001100110011001100110011001",k = 2000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001100110011001100110011001100110011001",k = 2000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100",k = 1000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100",k = 1000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010",k = 1000000) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010",k = 1000000) == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101010101010101010101010101",k = 1000) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101010101010101010101010101",k = 1000) == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010",k = 2147483647) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010",k = 2147483647) == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111",k = 1048575) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111",k = 1048575) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111",k = 1048575) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111",k = 1048575) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 500) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 500) == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",k = 1000000000) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",k = 1000000000) == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000000000000000000",k = 1) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000000000000000000",k = 1) == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001100110011001100110011001100110011",k = 5000) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001100110011001100110011001100110011",k = 5000) == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000",k = 0) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000",k = 0) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111100000000111111111000000011111111100000001111111110000000111111111000000011111111",k = 10000000) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111100000000111111111000000011111111100000001111111110000000111111111000000011111111",k = 10000000) == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101101101101101101101101101101101101",k = 500) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101101101101101101101101101101101101",k = 500) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000",k = 500000000) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000",k = 500000000) == 115: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100001111000011110000111100001111000011110000",k = 65535) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100001111000011110000111100001111000011110000",k = 65535) == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000000000000000000000000000000000000000000000",k = 1000000000) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000000000000000000000000000000000000000000000",k = 1000000000) == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100110011001100",k = 2048) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100110011001100",k = 2048) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010101",k = 2048) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010101",k = 2048) == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 100) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 100) == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000111000111000111000111000111",k = 500) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000111000111000111000111000111",k = 500) == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101010101010101",k = 511) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101010101010101",k = 511) == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000000000000000000000000000",k = 0) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000000000000000000000000000",k = 0) == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "01110111011101110111011101110111011101110111011101110111",k = 524287) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01110111011101110111011101110111011101110111011101110111",k = 524287) == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 1048575) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 1048575) == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010",k = 65535) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010",k = 65535) == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000111100001111000011110000",k = 10000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000111100001111000011110000",k = 10000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000",k = 1) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000",k = 1) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111000111000111000111000111000111000111000111000111000111",k = 25000) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111000111000111000111000111000111000111000111000111000111",k = 25000) == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110000011100000111000001110000011100000111000001110000011100000111000001110000011100000",k = 255) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110000011100000111000001110000011100000111000001110000011100000111000001110000011100000",k = 255) == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111",k = 2147483647) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111",k = 2147483647) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101010101",k = 524287) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101010101",k = 524287) == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110001110001110001110001",k = 2048) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110001110001110001110001",k = 2048) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000111100001111000011110000111100001111000011110000",k = 10000) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000111100001111000011110000111100001111000011110000",k = 10000) == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111111111111111",k = 1000000000) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111111111111111",k = 1000000000) == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "000100010001000100010001000100010001000100010001000100010001000100010",k = 1023) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000100010001000100010001000100010001000100010001000100010001000100010",k = 1023) == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111111111111111111111",k = 1048575) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111111111111111111111",k = 1048575) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001100110011001100110011001100110011001100110011001100110011001100110011001100110011",k = 50) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001100110011001100110011001100110011001100110011001100110011001100110011001100110011",k = 50) == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000000000000000000000000000000000000000000000000000000000000000",k = 1) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000000000000000000000000000000000000000000000000000000000000000",k = 1) == 67: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010",k = 1023) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010",k = 1023) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "110010011001001100100110010011001001100100110011001001",k = 1023) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110010011001001100100110010011001001100100110011001001",k = 1023) == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000",k = 1000) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000",k = 1000) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111111111111111",k = 2047) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111111111111111",k = 2047) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111111111111111111111",k = 1000000000) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111111111111111111111",k = 1000000000) == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "001010101010101010101010101010101010101010101010",k = 1024) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001010101010101010101010101010101010101010101010",k = 1024) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010",k = 999999999) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010",k = 999999999) == 94: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "0000000",k = 0) == 7
    assert candidate(s = "111000111",k = 127) == 7
    assert candidate(s = "1111111",k = 127) == 7
    assert candidate(s = "1111000011",k = 255) == 8
    assert candidate(s = "1100110011",k = 10) == 6
    assert candidate(s = "1010101010",k = 512) == 9
    assert candidate(s = "10101010",k = 10) == 6
    assert candidate(s = "111000111",k = 50) == 6
    assert candidate(s = "1101001",k = 4) == 4
    assert candidate(s = "11111111",k = 15) == 4
    assert candidate(s = "0101010101",k = 512) == 10
    assert candidate(s = "1101101",k = 7) == 4
    assert candidate(s = "1100110011",k = 500) == 9
    assert candidate(s = "0000000",k = 10) == 7
    assert candidate(s = "1001010",k = 5) == 5
    assert candidate(s = "00000",k = 1000) == 5
    assert candidate(s = "0101010101",k = 255) == 9
    assert candidate(s = "1",k = 1) == 1
    assert candidate(s = "11111111",k = 255) == 8
    assert candidate(s = "0000111100",k = 31) == 9
    assert candidate(s = "101010",k = 3) == 4
    assert candidate(s = "0",k = 0) == 1
    assert candidate(s = "1111000011110000",k = 100000) == 16
    assert candidate(s = "1100110011",k = 100) == 8
    assert candidate(s = "1010101010",k = 10) == 7
    assert candidate(s = "100110011001100110",k = 1000) == 14
    assert candidate(s = "00000000",k = 0) == 8
    assert candidate(s = "11001100",k = 20) == 6
    assert candidate(s = "00000000",k = 8) == 8
    assert candidate(s = "00101001",k = 1) == 6
    assert candidate(s = "010101010101010101",k = 10000) == 16
    assert candidate(s = "100101010010101010101010",k = 1024) == 18
    assert candidate(s = "1010101010101010101010101",k = 1048575) == 22
    assert candidate(s = "11001100110011001100110011001100110011001100110011001100",k = 1000000) == 38
    assert candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010",k = 10) == 36
    assert candidate(s = "10101010101010101010101010101010101010101010101010101010",k = 1023) == 33
    assert candidate(s = "110011001100110011001100110011001100110011001100",k = 65535) == 32
    assert candidate(s = "001100110011001100110011001100110011001100110011001100110011",k = 4096) == 36
    assert candidate(s = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",k = 0) == 87
    assert candidate(s = "11111111111111111111111111111111111111111111111111111111",k = 1073741823) == 30
    assert candidate(s = "1101101101101101101101101",k = 1000) == 15
    assert candidate(s = "11111111111111111111111111111111111111111111111111111111111111111111",k = 2047) == 11
    assert candidate(s = "00000000000000000000000000000000000000000000000000000000",k = 1000) == 56
    assert candidate(s = "0101010101010101010101010101010101010101",k = 1023) == 25
    assert candidate(s = "00001111000011110000111100001111000011110000111100001111",k = 32767) == 36
    assert candidate(s = "1001001001001001001001001001001001001001",k = 10000) == 31
    assert candidate(s = "11010110101101011010110101101011010110101101011010110101",k = 1048575) == 34
    assert candidate(s = "1001001001001001001001001001001001001001001001001001001001",k = 5000) == 43
    assert candidate(s = "1100110011001100110011001100110011001100110011001100110011001100110011001100110011001100",k = 128) == 47
    assert candidate(s = "10010101010101010101",k = 30000) == 18
    assert candidate(s = "111000111000111000111000111000111000111000111000111000111000111000111000",k = 50000) == 43
    assert candidate(s = "11010101010101010101",k = 16383) == 16
    assert candidate(s = "1101001101001101001101001101001",k = 1024) == 20
    assert candidate(s = "1111111111111111111111111111111111111111",k = 1024) == 10
    assert candidate(s = "0101010101010101010101010101010101010101",k = 10) == 22
    assert candidate(s = "1001100110011001100110011001100110011001",k = 2000) == 25
    assert candidate(s = "1100110011001100",k = 1000) == 12
    assert candidate(s = "10101010101010101010101010101010101010101010",k = 1000000) == 32
    assert candidate(s = "01010101010101010101010101010101010101010101010101010101010101010101",k = 1000) == 39
    assert candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010",k = 2147483647) == 49
    assert candidate(s = "11111111111111111111111111111111111111111111",k = 1048575) == 20
    assert candidate(s = "1111111111111111111111111",k = 1048575) == 20
    assert candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 500) == 48
    assert candidate(s = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",k = 1000000000) == 29
    assert candidate(s = "00000000000000000000000000000000000000000000000000000000000000000",k = 1) == 65
    assert candidate(s = "0011001100110011001100110011001100110011",k = 5000) == 27
    assert candidate(s = "0000000000000000000000000000000000000000",k = 0) == 40
    assert candidate(s = "111111111100000000111111111000000011111111100000001111111110000000111111111000000011111111",k = 10000000) == 52
    assert candidate(s = "1101101101101101101101101101101101101101",k = 500) == 19
    assert candidate(s = "100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000",k = 500000000) == 115
    assert candidate(s = "11110000111100001111000011110000111100001111000011110000",k = 65535) == 36
    assert candidate(s = "100000000000000000000000000000000000000000000000",k = 1000000000) == 47
    assert candidate(s = "11001100110011001100110011001100",k = 2048) == 21
    assert candidate(s = "101010101010101010101010101010101010101010101010101010101",k = 2048) == 34
    assert candidate(s = "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 100) == 48
    assert candidate(s = "111000111000111000111000111000111000111000111000111000111000111000111",k = 500) == 39
    assert candidate(s = "01010101010101010101010101010101010101010101010101010101",k = 511) == 33
    assert candidate(s = "0000000000000000000000000000000000000000000000000000000000000000",k = 0) == 64
    assert candidate(s = "01110111011101110111011101110111011101110111011101110111",k = 524287) == 29
    assert candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 1048575) == 53
    assert candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010",k = 65535) == 44
    assert candidate(s = "1111000011110000111100001111000011110000",k = 10000) == 25
    assert candidate(s = "0000000000000000000000000",k = 1) == 25
    assert candidate(s = "000111000111000111000111000111000111000111000111000111000111000111000111",k = 25000) == 44
    assert candidate(s = "1110000011100000111000001110000011100000111000001110000011100000111000001110000011100000",k = 255) == 58
    assert candidate(s = "111111111111111111111111111111111111111111111111",k = 2147483647) == 30
    assert candidate(s = "010101010101010101010101010101010101010101010101",k = 524287) == 34
    assert candidate(s = "1110001110001110001110001",k = 2048) == 17
    assert candidate(s = "1111000011110000111100001111000011110000111100001111000011110000",k = 10000) == 37
    assert candidate(s = "11111111111111111111111111111111111111111111111111111111",k = 1000000000) == 29
    assert candidate(s = "000100010001000100010001000100010001000100010001000100010001000100010",k = 1023) == 55
    assert candidate(s = "0000111111111111111111111",k = 1048575) == 24
    assert candidate(s = "0011001100110011001100110011001100110011001100110011001100110011001100110011001100110011",k = 50) == 47
    assert candidate(s = "10000000000000000000000000000000000000000000000000000000000000000000",k = 1) == 67
    assert candidate(s = "1010101010101010101010101010101010101010",k = 1023) == 25
    assert candidate(s = "110010011001001100100110010011001001100100110011001001",k = 1023) == 34
    assert candidate(s = "00000000000000000000",k = 1000) == 20
    assert candidate(s = "11111111111111111111111111111111111111111111111111111111",k = 2047) == 11
    assert candidate(s = "1111111111111111111111111111111111111111111111111111111111111111",k = 1000000000) == 29
    assert candidate(s = "001010101010101010101010101010101010101010101010",k = 1024) == 30
    assert candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010",k = 999999999) == 94


