def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "100100100100") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100100100100") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "110110110110110110110110110110110110110110110110") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110110110110110110110110110110110110110110110110") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100101") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100101") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "0") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "101101101101101") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101101101101101") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101001010111001010111001010111001010111001010111001") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101001010111001010111001010111001010111001010111001") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010101010101") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010101010101") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "11010101010101010101010101010101010101") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11010101010101010101010101010101010101") == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000100010001000100010001000100010001000100010001000") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000100010001000100010001000100010001000100010001000") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111011101110111011101110111011101110111011101110") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111011101110111011101110111011101110111011101110") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111000011110000") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111000011110000") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "100011110000111100001111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100011110000111100001111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010") == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "110101010101010101010101010101010101010101010101") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110101010101010101010101010101010101010101010101") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111110111111111111") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111110111111111111") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100110011001100110011001100") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100110011001100110011001100") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000000001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000000001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "000001000001000001000001") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000001000001000001000001") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000000000001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000000000001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000111111000000") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000111111000000") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111000011110000") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111000011110000") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "0010101010101010101010101010101010101010101010101010") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0010101010101010101010101010101010101010101010101010") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "0111111111111111111111111111111111111110") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0111111111111111111111111111111111111110") == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "011011011011011011011011011011011011011011011011") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011011011011011011011011011011011011011011011011") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101011") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101011") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001010101010101000") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001010101010101000") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110010100101001010010100101001010010100101001010010") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110010100101001010010100101001010010100101001010010") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111111") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111111") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101010101") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101010101") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101010101010101010101010101010101") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101010101010101010101010101010101") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000111111111111000000000000111111111111") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000111111111111000000000000111111111111") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000111000111000111000") == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000111000111000111000") == 57: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100110011001100110011001100") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100110011001100110011001100") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110001110001110001110001110001110001110001110001110") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110001110001110001110001110001110001110001110001110") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000011111111111111110000000000000000") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000011111111111111110000000000000000") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101010101010101010") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101010101010101010") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "000110001100011000110001100011000110001100011000110001100011") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000110001100011000110001100011000110001100011000110001100011") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111111111") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111111111") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "00110011001100110011001100") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00110011001100110011001100") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000000000000000000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000000000000000000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111000011110000111100001111000011110000") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111000011110000111100001111000011110000") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100001111000011110000111100001111000011110000") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100001111000011110000111100001111000011110000") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000111111110000000011111111000000001111111100000000") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000111111110000000011111111000000001111111100000000") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000011111000001111100000111110000011111000001111100") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000011111000001111100000111110000011111000001111100") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101010101010101010101") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101010101010101010101") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101010101010101") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101010101010101") == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111100000111110000011111000001111100000111110000011") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111100000111110000011111000001111100000111110000011") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111111111") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111111111") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "100010001000100010001000100010001000100010001000") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100010001000100010001000100010001000100010001000") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001001001001001001001001001001001001001001001001001") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001001001001001001001001001001001001001001001001001") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001001001001001") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001001001001001") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001100110011001100110011001100110011001100110011001100110011001") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001100110011001100110011001100110011001100110011001100110011001") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101010101010101") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101010101010101") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000111111000000111111000000111111000000111111000000") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000111111000000111111000000111111000000111111000000") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101010101010101") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101010101010101") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110000111100001111000011110000111100001111000011110") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110000111100001111000011110000111100001111000011110") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "11010101010101010101") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11010101010101010101") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000001111000001111") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000001111000001111") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100110011001100110011001100110011001100") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100110011001100110011001100110011001100") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101010") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101010") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "011001100110011001100110011001100110011001100110") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011001100110011001100110011001100110011001100110") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000001000000000001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000001000000000001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000000000000001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000000000000001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "011011011011011011011011011011011011011011011011011011011011011011011011") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011011011011011011011011011011011011011011011011011011011011011011011011") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001111111000000111111111000000111111111100000011111") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001111111000000111111111000000111111111100000011111") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "100100100100") == 7
    assert candidate(s = "110110110110110110110110110110110110110110110110") == 47
    assert candidate(s = "1100101") == 5
    assert candidate(s = "1001001001") == 6
    assert candidate(s = "11111") == 5
    assert candidate(s = "111111") == 6
    assert candidate(s = "0101010101") == 9
    assert candidate(s = "0") == 0
    assert candidate(s = "000000") == 0
    assert candidate(s = "0010") == 2
    assert candidate(s = "111000111") == 6
    assert candidate(s = "00000") == 0
    assert candidate(s = "000111000") == 6
    assert candidate(s = "1010101010") == 9
    assert candidate(s = "101101101101101") == 14
    assert candidate(s = "111100001111") == 8
    assert candidate(s = "1") == 1
    assert candidate(s = "101010101010101") == 14
    assert candidate(s = "1101001010111001010111001010111001010111001010111001") == 50
    assert candidate(s = "101010101010101010101010101010101010101010101010101010101010101") == 62
    assert candidate(s = "111000111000111000") == 15
    assert candidate(s = "11010101010101010101010101010101010101") == 37
    assert candidate(s = "0000000000000000000000000000000000000000000000") == 0
    assert candidate(s = "010101010101010101010101010101010101") == 35
    assert candidate(s = "111111111111111111111111111111111111111111111111") == 48
    assert candidate(s = "10101010101010101010101010101010101010101010101010") == 49
    assert candidate(s = "1000100010001000100010001000100010001000100010001000") == 25
    assert candidate(s = "000000000000000000000000000000000000000001") == 1
    assert candidate(s = "111011101110111011101110111011101110111011101110") == 47
    assert candidate(s = "010101010101010101010101") == 23
    assert candidate(s = "00001111000011110000") == 16
    assert candidate(s = "111000111000111") == 12
    assert candidate(s = "100011110000111100001111") == 20
    assert candidate(s = "10101010101010101010101010101010101010101010101") == 46
    assert candidate(s = "101010101010101010101010101010101010101010101010101010") == 53
    assert candidate(s = "110101010101010101010101010101010101010101010101") == 47
    assert candidate(s = "111111111110111111111111") == 23
    assert candidate(s = "1100110011001100110011001100110011001100110011001100") == 50
    assert candidate(s = "1000000000000000000001") == 2
    assert candidate(s = "000001000001000001000001") == 7
    assert candidate(s = "000000000000000000000000000000000000000000000000000000") == 0
    assert candidate(s = "11110000000000001111") == 8
    assert candidate(s = "111111000000111111000000") == 18
    assert candidate(s = "111100001111000011110000") == 20
    assert candidate(s = "0010101010101010101010101010101010101010101010101010") == 50
    assert candidate(s = "0111111111111111111111111111111111111110") == 39
    assert candidate(s = "011011011011011011011011011011011011011011011011") == 47
    assert candidate(s = "1010101010101010101010101010101010101010101010101011") == 51
    assert candidate(s = "00001010101010101000") == 14
    assert candidate(s = "1110010100101001010010100101001010010100101001010010") == 41
    assert candidate(s = "11111111111111111111111111111111111111111111111") == 47
    assert candidate(s = "010101010101010101010101010101010101010101010101") == 47
    assert candidate(s = "010101010101010101010101010101010101010101010101010101010101010101010101") == 71
    assert candidate(s = "000000000000111111111111000000000000111111111111") == 36
    assert candidate(s = "111000111000111000111000111000111000111000111000111000111000") == 57
    assert candidate(s = "110011001100110011001100110011001100110011001100") == 46
    assert candidate(s = "101010101010101010101010101010101010101") == 38
    assert candidate(s = "00000000000000000000000000000000000000000000000") == 0
    assert candidate(s = "1110001110001110001110001110001110001110001110001110") == 49
    assert candidate(s = "000000000000000011111111111111110000000000000000") == 32
    assert candidate(s = "1010101010101010101010101010101010101010101010101010101010101010") == 63
    assert candidate(s = "000110001100011000110001100011000110001100011000110001100011") == 46
    assert candidate(s = "1111111111111111111111111111111111111111111111111111") == 52
    assert candidate(s = "00110011001100110011001100") == 24
    assert candidate(s = "1000000000000000000000000000000000000000000000000000") == 1
    assert candidate(s = "111100001111000011110000111100001111000011110000") == 44
    assert candidate(s = "01010101010101010101010101010101") == 31
    assert candidate(s = "11110000111100001111000011110000111100001111000011110000") == 52
    assert candidate(s = "00000000111111110000000011111111000000001111111100000000") == 48
    assert candidate(s = "0000011111000001111100000111110000011111000001111100") == 47
    assert candidate(s = "1101010101010101010101") == 21
    assert candidate(s = "010101010101010101010101010101010101010101010101010101") == 53
    assert candidate(s = "1111100000111110000011111000001111100000111110000011") == 47
    assert candidate(s = "000000000000000") == 0
    assert candidate(s = "00000000000000000000000000000000000000000000000000001") == 1
    assert candidate(s = "111111111111111111111111111111111111111111111111111111") == 54
    assert candidate(s = "100010001000100010001000100010001000100010001000") == 23
    assert candidate(s = "1111111111111111111111111111111111111111") == 40
    assert candidate(s = "0001001001001001001001001001001001001001001001001001") == 33
    assert candidate(s = "1001001001001001001001001001001001001001001001001001001001") == 38
    assert candidate(s = "1001100110011001100110011001100110011001100110011001100110011001") == 62
    assert candidate(s = "0101010101010101010101010101010101010101010101010101") == 51
    assert candidate(s = "00000000000000000000") == 0
    assert candidate(s = "111111000000111111000000111111000000111111000000111111000000") == 54
    assert candidate(s = "01010101010101010101010101010101010101010101010101010101") == 55
    assert candidate(s = "1110000111100001111000011110000111100001111000011110") == 48
    assert candidate(s = "11010101010101010101") == 19
    assert candidate(s = "1010101010101010101010101010101010101010101010") == 45
    assert candidate(s = "0000000000000000000000000000000000000000000000000000") == 0
    assert candidate(s = "1010101010101010101010") == 21
    assert candidate(s = "0000000000000000000000000000000000000000000000001") == 1
    assert candidate(s = "1111000001111000001111") == 16
    assert candidate(s = "1100110011001100110011001100110011001100110011001100110011001100") == 62
    assert candidate(s = "1010101010101010101010101010101010101010101010101010") == 51
    assert candidate(s = "011001100110011001100110011001100110011001100110") == 46
    assert candidate(s = "000000000001000000000001") == 3
    assert candidate(s = "10000000000000000001") == 2
    assert candidate(s = "011011011011011011011011011011011011011011011011011011011011011011011011") == 71
    assert candidate(s = "0001111111000000111111111000000111111111100000011111") == 46
    assert candidate(s = "10101010101010101010") == 19
    assert candidate(s = "0000000000000000000000") == 0


