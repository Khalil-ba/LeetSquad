def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "000000111111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000111111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "000110") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000110") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001100111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001100111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "01000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000001111111110000000111111") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000001111111110000000111111") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100000000111111110000000011111111") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100000000111111110000000011111111") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001110000111100001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001110000111100001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000011111110000011111") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000011111110000011111") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000011111111111111") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000011111111111111") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000111111111100000000001111111111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000111111111100000000001111111111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "00111111001111110011111100111111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00111111001111110011111100111111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111110000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111110000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001000100010001000100010001000100010001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001000100010001000100010001000100010001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111000111000111000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111000111000111000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000001111111111111111111111111111111") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000001111111111111111111111111111111") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000111111110000000011111111") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000111111110000000011111111") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000111111111111") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000111111111111") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000001111111111000111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000001111111111000111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000001111111111111111") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000001111111111111111") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "11000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "001100110011001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001100110011001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111100000000001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111100000000001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000111110011000111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000111110011000111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001110111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001110111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100010001000100010001000100010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100010001000100010001000100010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000001111111111111111") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000001111111111111111") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "110000001111111111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110000001111111111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "00110011000000111111000000") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00110011000000111111000000") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "110000111100000011111100000000011111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110000111100000011111100000000011111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000011111110000000111111100000001111111") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000011111110000000111111100000001111111") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000111111000000111111000000111111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000111111000000111111000000111111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000011110000011111000000111111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000011110000011111000000111111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111000011110000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111000011110000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "10001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "11000011000011000011000011000011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11000011000011000011000011000011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100011100001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100011100001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111110000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111110000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111110000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111110000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "000001110000011100000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000001110000011100000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100110011") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100110011") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000001111111111111111") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000001111111111111111") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100001111000011110000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100001111000011110000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000111111000011111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000111111000011111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "000100010001000100010001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000100010001000100010001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000001111111111111100000000001111111111111000000000") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000001111111111111100000000001111111111111000000000") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011100110001110011000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011100110001110011000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "00011000110001100011000110001100011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00011000110001100011000110001100011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00110001100011000110001100011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00110001100011000110001100011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000001111111") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000001111111") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110110110110110110110") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110110110110110110110") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000001000000010000000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000001000000010000000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000001111000000111110000000111111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000001111000000111110000000111111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011000011000011000011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011000011000011000011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "00010001000111111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00010001000111111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000111111111") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000111111111") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001110000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001110000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111100000000000000111111111111") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111100000000000000111111111111") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110000111100001111000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110000111100001111000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111100000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111100000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111110000001111000000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111110000001111000000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111100000001111111000000011111110000000111111100000000") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111100000001111111000000011111110000000111111100000000") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000001111111111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000001111111111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000111110000011111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000111110000011111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000111111111100000000001111111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000111111111100000000001111111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000111100000001111000000001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000111100000001111000000001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000011111111000000001111111100000000") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000011111111000000001111111100000000") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "010010001000010000001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010010001000010000001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000011111000000011111000000011111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000011111000000011111000000011111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111110000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111110000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000000111111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000000111111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111100000000111111110000000011111111") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111100000000111111110000000011111111") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000001111000001111000001111000001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000001111000001111000001111000001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000111111100000001111111") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000111111100000001111111") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "010000001111101000111010000111000011111110000011111000001111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010000001111101000111010000111000011111110000011111000001111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "011111110111111101111111") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011111110111111101111111") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "111110000001111100000111110000011111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111110000001111100000111110000011111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "11000110001100011000110001100011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11000110001100011000110001100011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000011111111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000011111111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "00010001000100010001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00010001000100010001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100001111000011111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100001111000011111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111100000000000000111111111111000000000000111111111111") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111100000000000000111111111111000000000000111111111111") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011000011000011000011000011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011000011000011000011000011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011110000111100001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011110000111100001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000111100000000111111110000011111111000001111111000") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000111100000000111111110000011111111000001111111000") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000001111111111") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000001111111111") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111000011110000111100001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111000011110000111100001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "000110001100011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000110001100011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000111111000000111111000000") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000111111000000111111000000") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "00110011001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00110011001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111000111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111000111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000001111100111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000001111100111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110011001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110011001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000011111111") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000011111111") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111110000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111110000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000000000111111111111111000000000001111111111111111") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000000000111111111111111000000000001111111111111111") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000011111100000111110000011111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000011111100000111110000011111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000001111111111111111111111111") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000001111111111111111111111111") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "001001001001001001001001001001001001001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001001001001001001001001001001001001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000111100001110011") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000111100001110011") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "010010010010010010010010010010010010010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010010010010010010010010010010010010010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "001010110011000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001010110011000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110011001100110") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110011001100110") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000001111111111111110000000000011111111111111110000000000011111111111111") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000001111111111111110000000000011111111111111110000000000011111111111111") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000111111111111111111") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000111111111111111111") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "00011100001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00011100001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "001001001001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001001001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001100110011001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001100110011001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101010101010101010101010101010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101010101010101010101010101010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111010001110011") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111010001110011") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000011111111100000000111111000000") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000011111111100000000111111000000") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "000001111100000111110000011111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000001111100000111110000011111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000011111111111111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000011111111111111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110000000111000000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110000000111000000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111110000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111110000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000111111100000111100000111111100000000111111100000000") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000111111100000111100000111111100000000111111100000000") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "000110000111000001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000110000111000001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000000000111111111") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000000000111111111") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000011111000000011111000000011111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000011111000000011111000000011111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000011111111111") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000011111111111") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "010010001000010000000100000000001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010010001000010000000100000000001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111110000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111110000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00111000111000111000111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00111000111000111000111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100001111") == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "000000111111") == 12
    assert candidate(s = "000111000111") == 6
    assert candidate(s = "000110") == 4
    assert candidate(s = "01") == 2
    assert candidate(s = "00111") == 4
    assert candidate(s = "0001100111") == 4
    assert candidate(s = "111") == 0
    assert candidate(s = "111111") == 0
    assert candidate(s = "0") == 0
    assert candidate(s = "111111000000") == 0
    assert candidate(s = "1100") == 0
    assert candidate(s = "") == 0
    assert candidate(s = "00001111") == 8
    assert candidate(s = "000000") == 0
    assert candidate(s = "10") == 0
    assert candidate(s = "01010101") == 2
    assert candidate(s = "010101") == 2
    assert candidate(s = "1") == 0
    assert candidate(s = "101010") == 2
    assert candidate(s = "01000111") == 6
    assert candidate(s = "0000000001111111110000000111111") == 18
    assert candidate(s = "101010101010101010") == 2
    assert candidate(s = "0000111100000000111111110000000011111111") == 16
    assert candidate(s = "111111111111111111111111") == 0
    assert candidate(s = "111000111000111000") == 6
    assert candidate(s = "0001110000111100001111") == 8
    assert candidate(s = "000000011111110000011111") == 14
    assert candidate(s = "0000000000000011111111111111") == 28
    assert candidate(s = "0000000000111111111100000000001111111111") == 20
    assert candidate(s = "00111111001111110011111100111111") == 4
    assert candidate(s = "10101010101010101010101010101010101010101010101010") == 2
    assert candidate(s = "11111111110000000000000000000000") == 0
    assert candidate(s = "0001000100010001000100010001000100010001") == 2
    assert candidate(s = "110011001100110011001100") == 4
    assert candidate(s = "000111000111000111000111000111000111000111000111") == 6
    assert candidate(s = "010101010101010101010101") == 2
    assert candidate(s = "0000000000000000000000000001111111111111111111111111111111") == 54
    assert candidate(s = "00000000111111110000000011111111") == 16
    assert candidate(s = "000000000000111111111111") == 24
    assert candidate(s = "00000000001111111111000111") == 20
    assert candidate(s = "00000000000000001111111111111111") == 32
    assert candidate(s = "11000111000111000111") == 6
    assert candidate(s = "001100110011001100110011") == 4
    assert candidate(s = "111111111100000000001111") == 8
    assert candidate(s = "0000000111110011000111") == 10
    assert candidate(s = "000111000111000111") == 6
    assert candidate(s = "101010101010101010101010") == 2
    assert candidate(s = "0001110111000111000111") == 6
    assert candidate(s = "0100010001000100010001000100010") == 2
    assert candidate(s = "000000000000000000001111111111111111") == 32
    assert candidate(s = "110000001111111111") == 12
    assert candidate(s = "00110011000000111111000000") == 12
    assert candidate(s = "1010101010") == 2
    assert candidate(s = "010101010101010101") == 2
    assert candidate(s = "110000111100000011111100000000011111") == 12
    assert candidate(s = "111000111000111000111000111000") == 6
    assert candidate(s = "000111000111000111000111") == 6
    assert candidate(s = "000000011111110000000111111100000001111111") == 14
    assert candidate(s = "01010101010101010101010101010101010101") == 2
    assert candidate(s = "000000111111000000111111000000111111") == 12
    assert candidate(s = "000111000011110000011111000000111111") == 12
    assert candidate(s = "111100001111000011110000") == 8
    assert candidate(s = "10001100110011") == 4
    assert candidate(s = "11000011000011000011000011000011") == 4
    assert candidate(s = "0000111100011100001111") == 8
    assert candidate(s = "111111111110000000000000000") == 0
    assert candidate(s = "111111111111111111110000000000000000") == 0
    assert candidate(s = "0011001100110011") == 4
    assert candidate(s = "000001110000011100000111") == 6
    assert candidate(s = "0000111100110011") == 8
    assert candidate(s = "10101010101010101010101") == 2
    assert candidate(s = "000000000001111111111111111") == 22
    assert candidate(s = "0000111100001111000011110000") == 8
    assert candidate(s = "0000000111111000011111") == 12
    assert candidate(s = "000100010001000100010001") == 2
    assert candidate(s = "00000000000001111111111111100000000001111111111111000000000") == 26
    assert candidate(s = "111111111111") == 0
    assert candidate(s = "000011100110001110011000111") == 6
    assert candidate(s = "00011000110001100011000110001100011") == 4
    assert candidate(s = "10101010101010101010101010101010101010") == 2
    assert candidate(s = "00110001100011000110001100011") == 4
    assert candidate(s = "101010101010") == 2
    assert candidate(s = "00000001111111") == 14
    assert candidate(s = "0110110110110110110110") == 2
    assert candidate(s = "100000001000000010000000") == 2
    assert candidate(s = "000111000001111000000111110000000111111") == 12
    assert candidate(s = "000011000011000011000011") == 4
    assert candidate(s = "111000111000111000111000111000111") == 6
    assert candidate(s = "00010001000111111111") == 6
    assert candidate(s = "000000000111111111") == 18
    assert candidate(s = "0001110000111000111000111") == 6
    assert candidate(s = "11111100000000000000111111111111") == 24
    assert candidate(s = "1110000111100001111000") == 8
    assert candidate(s = "11111100000000000000") == 0
    assert candidate(s = "111111000000000000000000") == 0
    assert candidate(s = "1111110000001111000000") == 8
    assert candidate(s = "1010101010101010101010101010101010") == 2
    assert candidate(s = "1111111100000001111111000000011111110000000111111100000000") == 14
    assert candidate(s = "00000000001111111111") == 20
    assert candidate(s = "00000111110000011111") == 10
    assert candidate(s = "00000000000111111111100000000001111111") == 20
    assert candidate(s = "000000000111100000001111000000001111") == 8
    assert candidate(s = "0000000011111111000000001111111100000000") == 16
    assert candidate(s = "111000111000111000111") == 6
    assert candidate(s = "010010001000010000001") == 2
    assert candidate(s = "1001001001001001") == 2
    assert candidate(s = "00000011111000000011111000000011111") == 10
    assert candidate(s = "11111111110000000000") == 0
    assert candidate(s = "1111000000111111") == 12
    assert candidate(s = "01010101010101010101010101010101") == 2
    assert candidate(s = "11001100110011001100") == 4
    assert candidate(s = "0101010101010101010101010101010101010101") == 2
    assert candidate(s = "1111111100000000111111110000000011111111") == 16
    assert candidate(s = "1111000001111000001111000001111000001111") == 8
    assert candidate(s = "0000000111111100000001111111") == 14
    assert candidate(s = "010000001111101000111010000111000011111110000011111000001111") == 10
    assert candidate(s = "011111110111111101111111") == 2
    assert candidate(s = "1100110011001100110011001100") == 4
    assert candidate(s = "010101010101") == 2
    assert candidate(s = "111110000001111100000111110000011111") == 10
    assert candidate(s = "11000110001100011000110001100011") == 4
    assert candidate(s = "0101010101010101") == 2
    assert candidate(s = "00000011111111") == 12
    assert candidate(s = "000000000000000000000000") == 0
    assert candidate(s = "000111000111000111000111000111") == 6
    assert candidate(s = "00010001000100010001") == 2
    assert candidate(s = "1100001111000011111") == 8
    assert candidate(s = "111111111111100000000000000111111111111000000000000111111111111") == 24
    assert candidate(s = "000011000011000011000011000011") == 4
    assert candidate(s = "000011110000111100001111") == 8
    assert candidate(s = "00000111100000000111111110000011111111000001111111000") == 16
    assert candidate(s = "10000000001111111111") == 18
    assert candidate(s = "0101010101") == 2
    assert candidate(s = "00001111000011110000111100001111") == 8
    assert candidate(s = "000110001100011") == 4
    assert candidate(s = "111111000000111111000000111111000000") == 12
    assert candidate(s = "00110011001100110011") == 4
    assert candidate(s = "00001111000111") == 8
    assert candidate(s = "0000001111100111") == 10
    assert candidate(s = "0110011001100110011") == 4
    assert candidate(s = "0000000011111111") == 16
    assert candidate(s = "1001001001001001001001001") == 2
    assert candidate(s = "111111111111111111111110000000000000000000000000") == 0
    assert candidate(s = "100000000000111111111111111000000000001111111111111111") == 22
    assert candidate(s = "0101010101010101010101010101010101010101010101") == 2
    assert candidate(s = "0000000011111100000111110000011111") == 12
    assert candidate(s = "000000000000000000000001111111111111111111111111") == 46
    assert candidate(s = "1010101010101010101010101010101010101010101010") == 2
    assert candidate(s = "001001001001001001001001001001001001001") == 2
    assert candidate(s = "00000111100001110011") == 8
    assert candidate(s = "1001001001001") == 2
    assert candidate(s = "010010010010010010010010010010010010010") == 2
    assert candidate(s = "001010110011000111") == 6
    assert candidate(s = "111000111000111000111000111000111000111000111") == 6
    assert candidate(s = "0110011001100110") == 4
    assert candidate(s = "0000000000001111111111111110000000000011111111111111110000000000011111111111111") == 24
    assert candidate(s = "00000000000000111111111111111111") == 28
    assert candidate(s = "00011100001111") == 8
    assert candidate(s = "01010101010101010101010101010101010101010101") == 2
    assert candidate(s = "001001001001") == 2
    assert candidate(s = "0011001100110011001100110011") == 4
    assert candidate(s = "01010101010101010101") == 2
    assert candidate(s = "0101010101010101010101010101010101010101010101010101010101010101010101") == 2
    assert candidate(s = "11001100110011") == 4
    assert candidate(s = "1001001001001001001001001001") == 2
    assert candidate(s = "000111010001110011") == 6
    assert candidate(s = "0000011111111100000000111111000000") == 12
    assert candidate(s = "000001111100000111110000011111") == 10
    assert candidate(s = "000000000011111111111111") == 20
    assert candidate(s = "1110000000111000000111") == 6
    assert candidate(s = "11111111111111110000000000000000") == 0
    assert candidate(s = "10101010101010101010") == 2
    assert candidate(s = "00000000111111100000111100000111111100000000111111100000000") == 14
    assert candidate(s = "000110000111000001111") == 8
    assert candidate(s = "10101010101010") == 2
    assert candidate(s = "111111000000000000111111111") == 18
    assert candidate(s = "111000111000111000111000") == 6
    assert candidate(s = "11001100110011001100110011") == 4
    assert candidate(s = "000000011111000000011111000000011111") == 10
    assert candidate(s = "0000000000011111111111") == 22
    assert candidate(s = "010010001000010000000100000000001") == 2
    assert candidate(s = "11111111111111111111111111110000000000000000000000000000000") == 0
    assert candidate(s = "00111000111000111000111000111") == 6
    assert candidate(s = "001100110011") == 4
    assert candidate(s = "0000111100001111") == 8


