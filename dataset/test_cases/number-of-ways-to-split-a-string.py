def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "001001001") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001001") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10100101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10100101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "11011011011") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11011011011") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "100010001") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100010001") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000") == 1176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000") == 1176: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000001110000011100000111") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000001110000011100000111") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000010000000100000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000010000000100000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110111011101110111011101110111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110111011101110111011101110111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000100010001000100010001000100010001000100010001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000100010001000100010001000100010001000100010001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "001001001001001001001001001001001001001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001001001001001001001001001001001001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001000010000100001000010000100001000010000100001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001000010000100001000010000100001000010000100001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0010101010100") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0010101010100") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000111100001111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000111100001111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001001001") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001001001") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000000000000000000000000000000000000000000000000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000000000000000000000000000000000000000000000000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "001001001001001001001001001001001001001001001001001001") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001001001001001001001001001001001001001001001001001") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100001111000011110000111100001111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100001111000011110000111100001111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001100110011001100110011") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001100110011001100110011") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100110011") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100110011") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000001000000001") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000001000000001") == 90: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000100000100000100000100000100000") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000100000100000100000100000100000") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10001000100010001000100010001000100010001000100010001000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10001000100010001000100010001000100010001000100010001000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111110000011111000001111100000111110000011111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111110000011111000001111100000111110000011111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100110011001100110011001100") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100110011001100110011001100") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000") == 91: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00010001000100010001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00010001000100010001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000000000100000000010000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000000000100000000010000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000000000000000000000000") == 1225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000000000000000000000000") == 1225: {e}')
    
    total += 1
    try:
        result = candidate(s = "10100100100100100") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10100100100100100") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100100100100100100100100100100100100100100100100100") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100100100100100100100100100100100100100100100100100") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000111111000000111111") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000111111000000111111") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "00010001000100010001000100010001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00010001000100010001000100010001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000") == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000") == 276: {e}')
    
    total += 1
    try:
        result = candidate(s = "11011011011011011011011011011011") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11011011011011011011011011011011") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111000001111100000111110000011111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111000001111100000111110000011111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000010000100001000010000100001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000010000100001000010000100001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "101001010010100101001010010100101001010010100101001") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101001010010100101001010010100101001010010100101001") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000") == 351: {e}')
    
    total += 1
    try:
        result = candidate(s = "01001001001001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01001001001001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000000000000000000") == 946
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000000000000000000") == 946: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "101010101") == 0
    assert candidate(s = "10101010101") == 4
    assert candidate(s = "0000") == 3
    assert candidate(s = "0000000") == 15
    assert candidate(s = "010101010") == 0
    assert candidate(s = "111000") == 1
    assert candidate(s = "11111111111") == 0
    assert candidate(s = "111111") == 1
    assert candidate(s = "10101") == 4
    assert candidate(s = "001001001") == 9
    assert candidate(s = "1111111") == 0
    assert candidate(s = "1001001001") == 0
    assert candidate(s = "111000111000111") == 16
    assert candidate(s = "01010101010") == 0
    assert candidate(s = "1010101010") == 0
    assert candidate(s = "0000000000") == 36
    assert candidate(s = "1100110011") == 9
    assert candidate(s = "00000000000") == 45
    assert candidate(s = "1000000000001") == 0
    assert candidate(s = "0101010101") == 0
    assert candidate(s = "10100101010101") == 0
    assert candidate(s = "11011011011") == 0
    assert candidate(s = "111000111") == 1
    assert candidate(s = "100010001") == 16
    assert candidate(s = "1001") == 0
    assert candidate(s = "01010101010101010101010101010101") == 0
    assert candidate(s = "00000000000000000000000000000000000000000000000000") == 1176
    assert candidate(s = "1001001001001001001001") == 0
    assert candidate(s = "111000111000111000111000111") == 1
    assert candidate(s = "01010101010101010101010101010101010101010101010101010101") == 0
    assert candidate(s = "0000001110000011100000111") == 36
    assert candidate(s = "1000000010000000100000001") == 0
    assert candidate(s = "1110111011101110111011101110111") == 1
    assert candidate(s = "111111111111111111111111111111111111111111111111") == 1
    assert candidate(s = "101010101010101010101010101010101010101010101010") == 4
    assert candidate(s = "1000100010001000100010001000100010001000100010001") == 0
    assert candidate(s = "001001001001001001001001001001001001001") == 0
    assert candidate(s = "1001001001001") == 0
    assert candidate(s = "00001000010000100001000010000100001000010000100001") == 0
    assert candidate(s = "111000111000111000111000111000111000111000111") == 1
    assert candidate(s = "111111111111111111111111111111111111111111111111111") == 1
    assert candidate(s = "1001001001001001001001001001001001001001001001001") == 0
    assert candidate(s = "0010101010100") == 0
    assert candidate(s = "1111000011110000111100001111") == 0
    assert candidate(s = "10101010101010101010101010") == 0
    assert candidate(s = "101010101010101010101010101010101010101010101010101") == 0
    assert candidate(s = "1001001001001001001001001001001001001001001001001001") == 9
    assert candidate(s = "100000000000000000000000000000000000000000000000000000001") == 0
    assert candidate(s = "001001001001001001001001001001001001001001001001001001") == 9
    assert candidate(s = "1100110011001100110011") == 9
    assert candidate(s = "0000111100001111000011110000111100001111") == 0
    assert candidate(s = "0011001100110011001100110011") == 0
    assert candidate(s = "110011001100110011001100110011") == 0
    assert candidate(s = "10000000001000000001") == 90
    assert candidate(s = "110011001100110") == 0
    assert candidate(s = "100000100000100000100000100000100000") == 36
    assert candidate(s = "10101010101010101010101010101010101010101010101") == 4
    assert candidate(s = "0101010101010101010101010101") == 0
    assert candidate(s = "10001000100010001000100010001000100010001000100010001000") == 0
    assert candidate(s = "111110000011111000001111100000111110000011111") == 0
    assert candidate(s = "1100110011001100110011001100110011001100110011001100") == 0
    assert candidate(s = "000000000000000") == 91
    assert candidate(s = "101010101010101010101") == 0
    assert candidate(s = "00010001000100010001") == 0
    assert candidate(s = "100000000000100000000010000000001") == 0
    assert candidate(s = "1000000000000000000001") == 0
    assert candidate(s = "1001001001001001001001001001001001001001") == 0
    assert candidate(s = "101010101010101010101010101") == 0
    assert candidate(s = "000000000000000000000000000000000000000000000000000") == 1225
    assert candidate(s = "10100100100100100") == 9
    assert candidate(s = "0100100100100100100100100100100100100100100100100100") == 0
    assert candidate(s = "111111000000111111000000111111") == 49
    assert candidate(s = "00010001000100010001000100010001") == 0
    assert candidate(s = "0000000000000000000000") == 210
    assert candidate(s = "0000000000000000000000000") == 276
    assert candidate(s = "11011011011011011011011011011011") == 0
    assert candidate(s = "11111000001111100000111110000011111") == 0
    assert candidate(s = "111000111000111000111000") == 1
    assert candidate(s = "1000010000100001000010000100001") == 0
    assert candidate(s = "110011001100110011") == 0
    assert candidate(s = "101001010010100101001010010100101001010010100101001") == 6
    assert candidate(s = "0000000000000000000000000000") == 351
    assert candidate(s = "01001001001001") == 0
    assert candidate(s = "000000000000000000000000000000000000000000000") == 946


