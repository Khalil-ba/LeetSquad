def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "00111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "101100110") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101100110") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "100001110") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100001110") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "110001101") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110001101") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001101") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001101") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100011") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100011") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "101000101") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101000101") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101001") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101001") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "110000011") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110000011") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "100010001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100010001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "11010000011100000111") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11010000011100000111") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001011001011001011") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001011001011001011") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "110010010101001") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110010010101001") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "100001000010000100001") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100001000010000100001") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110011001100110011001100110011001100110011001100110011001") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110011001100110011001100110011001100110011001100110011001") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "10010010010010010010010010010010010010010010010010") == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10010010010010010010010010010010010010010010010010") == 153: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111000011110000") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111000011110000") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101") == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101") == 276: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000000000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000000000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101") == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101") == 300: {e}')
    
    total += 1
    try:
        result = candidate(s = "110000000000000000000000000000000000000000000000000000000000000000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110000000000000000000000000000000000000000000000000000000000000000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101") == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101") == 253: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111000011110000") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111000011110000") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "00011110001111000111100011110001111000111100011110") == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00011110001111000111100011110001111000111100011110") == 112: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001100110011") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001100110011") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "01001001001001001001001001001001001001001001001001") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01001001001001001001001001001001001001001001001001") == 136: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011110000111100001111000011110000") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011110000111100001111000011110000") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100001111000011110000") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100001111000011110000") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101010101") == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101010101") == 300: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000000000000000000000000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000000000000000000000000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000000000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000000000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000001000000010000000100000001") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000001000000010000000100000001") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000") == 84: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000001111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000001111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000100000001000000010000000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000100000001000000010000000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000111110000011111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000111110000011111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000000000000000000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000000000000000000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111110000000000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111110000000000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101") == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101") == 190: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010") == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010") == 105: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000000000000000000000000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000000000000000000000000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111100000000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111100000000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000111000111000111000111") == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000111000111000111000111") == 165: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100001111000011110000") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100001111000011110000") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000000") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000000") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101101101101101101101101101101101101") == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101101101101101101101101101101101101") == 182: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101010101010") == 435
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101010101010") == 435: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000000000000000000000000000000000000001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000000000000000000000000000000000000001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111000001111100000111110000011111000001111100000") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111000001111100000111110000011111000001111100000") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001") == 91: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111110000000") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111110000000") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000010000001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000010000001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111000011110000111100001111") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111000011110000111100001111") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000011100001110000111") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000011100001110000111") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010") == 136: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000011111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000011111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001100110011001100110011001100110011001100110011001100110") == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001100110011001100110011001100110011001100110011001100110") == 225: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100010010011010") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100010010011010") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100101001010010100101001010010100101001") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100101001010010100101001010010100101001") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100000011110000001111000000") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100000011110000001111000000") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010") == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010") == 210: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100001111000011110000111100001111") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100001111000011110000111100001111") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101010101010101010101010101") == 528
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101010101010101010101010101") == 528: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "00011110000111100001111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00011110000111100001111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111111111111111") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111111111111111") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100001111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100001111") == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "00111") == 0
    assert candidate(s = "101100110") == 9
    assert candidate(s = "000111000") == 3
    assert candidate(s = "11110000") == 4
    assert candidate(s = "010101010") == 10
    assert candidate(s = "1001001001001") == 10
    assert candidate(s = "100001110") == 5
    assert candidate(s = "1111111111") == 0
    assert candidate(s = "1010101") == 6
    assert candidate(s = "1000000000") == 1
    assert candidate(s = "00001111") == 0
    assert candidate(s = "10001") == 1
    assert candidate(s = "00000000") == 0
    assert candidate(s = "11111") == 0
    assert candidate(s = "1001001001") == 6
    assert candidate(s = "11111111") == 0
    assert candidate(s = "110001101") == 6
    assert candidate(s = "1001101") == 4
    assert candidate(s = "1010101010") == 15
    assert candidate(s = "1100011") == 2
    assert candidate(s = "1100110011") == 6
    assert candidate(s = "101000101") == 6
    assert candidate(s = "1101001") == 5
    assert candidate(s = "101010") == 6
    assert candidate(s = "0101010101") == 10
    assert candidate(s = "110000011") == 2
    assert candidate(s = "00000") == 0
    assert candidate(s = "100010001") == 3
    assert candidate(s = "11010000011100000111") == 11
    assert candidate(s = "111111111111111111111111111111111111111111111111") == 0
    assert candidate(s = "11001011001011001011") == 33
    assert candidate(s = "00000000000000000000000000000000") == 0
    assert candidate(s = "110010010101001") == 20
    assert candidate(s = "100001000010000100001") == 10
    assert candidate(s = "1010101010101010101") == 45
    assert candidate(s = "0110011001100110011001100110011001100110011001100110011001") == 210
    assert candidate(s = "10010010010010010010010010010010010010010010010010") == 153
    assert candidate(s = "00001111000011110000") == 12
    assert candidate(s = "111000111000111") == 9
    assert candidate(s = "000111000111000111") == 9
    assert candidate(s = "10101010101010101010101010101010101010101010101") == 276
    assert candidate(s = "0000000000000000000000000000000000000000000000000001") == 0
    assert candidate(s = "1111111111111111111111111111111111111") == 0
    assert candidate(s = "1010101010101010101010101010101010101010101010101") == 300
    assert candidate(s = "110000000000000000000000000000000000000000000000000000000000000000") == 2
    assert candidate(s = "110011001100") == 12
    assert candidate(s = "101010101010101010101010101010101010101010101") == 253
    assert candidate(s = "111100001111000011110000") == 24
    assert candidate(s = "00011110001111000111100011110001111000111100011110") == 112
    assert candidate(s = "0011001100110011") == 12
    assert candidate(s = "000000111111") == 0
    assert candidate(s = "01001001001001001001001001001001001001001001001001") == 136
    assert candidate(s = "10101010101010101010101") == 66
    assert candidate(s = "000011110000111100001111000011110000") == 40
    assert candidate(s = "0000111100001111000011110000") == 24
    assert candidate(s = "0000000000000000000000000000000000000000") == 0
    assert candidate(s = "1001001001001001001001001001001") == 55
    assert candidate(s = "100000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000") == 3
    assert candidate(s = "01010101010101010101010101010101010101010101010101") == 300
    assert candidate(s = "100000000000000000000000000000000000000000000000000000000000000001") == 1
    assert candidate(s = "10000000000000000000000000000000000000000000000000001") == 1
    assert candidate(s = "1000000001000000010000000100000001") == 10
    assert candidate(s = "111000111000111000111000111000111000111000") == 84
    assert candidate(s = "00000000001111111111") == 0
    assert candidate(s = "10000000100000001000000010000000") == 10
    assert candidate(s = "00000111110000011111") == 5
    assert candidate(s = "111000111000111000111") == 18
    assert candidate(s = "1000000000000000000000000000000000000000000000000000") == 1
    assert candidate(s = "11111111110000000000") == 10
    assert candidate(s = "01010101010101010101010101010101") == 120
    assert candidate(s = "0101010101010101010101010101010101010101") == 190
    assert candidate(s = "1010101010101010101010101010") == 105
    assert candidate(s = "100000000000000000000000000000000000000000000000") == 1
    assert candidate(s = "00000000000000000000000000000000000000000000000000000000000") == 0
    assert candidate(s = "1111111100000000") == 8
    assert candidate(s = "111000111000111000111000111000111000111000111000111000111000111") == 165
    assert candidate(s = "11110000111100001111000011110000") == 40
    assert candidate(s = "1111111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000000") == 52
    assert candidate(s = "1101101101101101101101101101101101101101") == 182
    assert candidate(s = "0101010101010101") == 28
    assert candidate(s = "11111111111111111111111111111111") == 0
    assert candidate(s = "1010101010101010101010101010101010101010101010101010101010") == 435
    assert candidate(s = "000000000000000000000000000000000000000000000000000000000000000001") == 0
    assert candidate(s = "11111000001111100000111110000011111000001111100000") == 75
    assert candidate(s = "1001001001001001001") == 21
    assert candidate(s = "1001001001001001001001001001001001001001") == 91
    assert candidate(s = "11111110000000") == 7
    assert candidate(s = "100000010000001") == 3
    assert candidate(s = "00001111000011110000111100001111") == 24
    assert candidate(s = "1111111111111111111111111111111111111111") == 0
    assert candidate(s = "111000011100001110000111") == 18
    assert candidate(s = "1111000011110000") == 12
    assert candidate(s = "10101010101010101010101010101010") == 136
    assert candidate(s = "0000000011111111") == 0
    assert candidate(s = "1001100110011001100110011001100110011001100110011001100110") == 225
    assert candidate(s = "1100010010011010") == 22
    assert candidate(s = "0100101001010010100101001010010100101001") == 120
    assert candidate(s = "1100000011110000001111000000") == 18
    assert candidate(s = "1010101010101010101010101010101010101010") == 210
    assert candidate(s = "0000111100001111000011110000111100001111") == 40
    assert candidate(s = "01010101010101010101") == 45
    assert candidate(s = "010101010101010101010101010101010101010101010101010101010101010101") == 528
    assert candidate(s = "0000000000000000000000000000000000000") == 0
    assert candidate(s = "10101010101010101010") == 55
    assert candidate(s = "00011110000111100001111") == 12
    assert candidate(s = "1111111111111111111111111111111111111111111111111111111111") == 0
    assert candidate(s = "0000111100001111") == 4


