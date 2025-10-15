def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "1111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "00111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "100100") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100100") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "001001") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "100001") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100001") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "001100") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001100") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "011101") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011101") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111000") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111000") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000001") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000001") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000001") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000001") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000111111000000111111") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000111111000000111111") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000100010001") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000100010001") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111110000000001111111111100000000") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111110000000001111111111100000000") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110110110110110110110110110") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110110110110110110110110110") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000011111111111111") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000011111111111111") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011110000111100001111000011110000111100001111") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011110000111100001111000011110000111100001111") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111110") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111110") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "111110000011111000001111100000") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111110000011111000001111100000") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000001111111111000000001111111111") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000001111111111000000001111111111") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110110110") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110110110") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000001111111111111111") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000001111111111111111") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111110") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111110") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "10011111000111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10011111000111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "010010010010010") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010010010010010") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111000011110000111100001111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111000011110000111100001111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000111111000000") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000111111000000") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111000011110000") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111000011110000") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000001") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000001") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "011101110111011101") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011101110111011101") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100000000") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100000000") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010010101001010100101010010101") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010010101001010100101010010101") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111000001111100000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111000001111100000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011110000111100001111000011110000") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011110000111100001111000011110000") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111110000000001") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111110000000001") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111100000001111111100000000111111") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111100000001111111100000000111111") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100110011001100110011001100110011001100110011001100") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100110011001100110011001100110011001100110011001100") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000011111110000000011111111000000") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000011111110000000011111111000000") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110110110110110") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110110110110110") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000001") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000001") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111110000000000000000") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111110000000000000000") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "010100101001010010100101001") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010100101001010010100101001") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "000001111111111111") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000001111111111111") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001111000") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001111000") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000011111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000011111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110110110110110110110110110110110110110110110") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110110110110110110110110110110110110110110110") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "110001010101101010010101011110000101010101") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110001010101101010010101011110000101010101") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "111001010101010") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111001010101010") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "01000110011001100110") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01000110011001100110") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000001111111111") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000001111111111") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111111110000") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111111110000") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000001111111111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000001111111111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "100100100100100100100100100100100100") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100100100100100100100100100100100100") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000001111111111111111") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000001111111111111111") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111110000000000") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111110000000000") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "11100011100011100011") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11100011100011100011") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000001111111110000000001111111110000000000111111111") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000001111111110000000001111111110000000000111111111") == 37: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "10010010010010010010") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10010010010010010010") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000") == 43: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000011111100") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000011111100") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011111111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011111111") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100101010101010") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100101010101010") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111101") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111101") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "00010001000100010001") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00010001000100010001") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011110000111100001111") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011110000111100001111") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111000111000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111000111000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111110") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111110") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "00110011001100110011") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00110011001100110011") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "0111111111000000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0111111111000000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111100000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111100000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000000001111000000001111000000001111000000001111") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000000001111000000001111000000001111000000001111") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000001") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000001") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101101") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101101") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "111110000011111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111110000011111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "00011100011100011100") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00011100011100011100") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "11101110111011101110") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11101110111011101110") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "000100010001000100") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000100010001000100") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101010101010101010101010101010101") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101010101010101010101010101010101") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "000001111100000111110000011111") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000001111100000111110000011111") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "0010100101001010010100101001010010") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0010100101001010010100101001010010") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "00011110001111") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00011110001111") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "01101101101101101101") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01101101101101101101") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111110000000000000000") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111110000000000000000") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001100110") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001100110") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000011111111111") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000011111111111") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111110000000000") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111110000000000") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "001100110011001100110011001100") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001100110011001100110011001100") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "001100110011") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001100110011") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "0111000001") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0111000001") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100001111") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100001111") == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "1111") == 3
    assert candidate(s = "00111") == 5
    assert candidate(s = "100100") == 3
    assert candidate(s = "110011") == 4
    assert candidate(s = "001001") == 5
    assert candidate(s = "11110000") == 3
    assert candidate(s = "0000") == 3
    assert candidate(s = "111000") == 2
    assert candidate(s = "1001001") == 5
    assert candidate(s = "1100") == 1
    assert candidate(s = "100001") == 5
    assert candidate(s = "00001111") == 8
    assert candidate(s = "000111") == 6
    assert candidate(s = "1001001001") == 7
    assert candidate(s = "001100") == 4
    assert candidate(s = "01010101") == 5
    assert candidate(s = "010101") == 4
    assert candidate(s = "101010") == 3
    assert candidate(s = "11001100") == 4
    assert candidate(s = "011101") == 5
    assert candidate(s = "000111000111000111000") == 12
    assert candidate(s = "101010101010101010") == 9
    assert candidate(s = "00000000000000000000000001") == 26
    assert candidate(s = "1000000000000000001") == 18
    assert candidate(s = "000000111111000000111111") == 18
    assert candidate(s = "01010101010101010101010101010101010101010") == 21
    assert candidate(s = "1000100010001") == 10
    assert candidate(s = "11111111110000000001111111111100000000") == 20
    assert candidate(s = "0110110110110110110110110110") == 19
    assert candidate(s = "0000000011111111111111") == 22
    assert candidate(s = "000011110000111100001111000011110000111100001111") == 28
    assert candidate(s = "1111111110") == 8
    assert candidate(s = "111110000011111000001111100000") == 15
    assert candidate(s = "10000000001111111111000000001111111111") == 29
    assert candidate(s = "010101010101010101010101") == 13
    assert candidate(s = "0110110110") == 7
    assert candidate(s = "10101010101010101010101010") == 13
    assert candidate(s = "00000000000000001111111111111111") == 32
    assert candidate(s = "111000111000111") == 9
    assert candidate(s = "111111111111111110") == 16
    assert candidate(s = "10011111000111") == 10
    assert candidate(s = "000111000111000111") == 12
    assert candidate(s = "101010101010101010101010") == 12
    assert candidate(s = "1010101010") == 5
    assert candidate(s = "010010010010010") == 10
    assert candidate(s = "0000000000") == 9
    assert candidate(s = "0000000000000000") == 15
    assert candidate(s = "1010101010101010") == 8
    assert candidate(s = "111100001111000011110000111100001111") == 20
    assert candidate(s = "111111000000111111000000") == 12
    assert candidate(s = "111100001111000011110000") == 12
    assert candidate(s = "000000000000001") == 15
    assert candidate(s = "011101110111011101") == 14
    assert candidate(s = "111100000000") == 7
    assert candidate(s = "101010010101001010100101010010101") == 19
    assert candidate(s = "11111000001111100000") == 10
    assert candidate(s = "000011110000111100001111000011110000") == 20
    assert candidate(s = "1111110000000001") == 10
    assert candidate(s = "111111100000001111111100000000111111") == 21
    assert candidate(s = "110011001100110011001100110011001100110011001100110011001100110011001100") == 36
    assert candidate(s = "010101010101010101010101010") == 14
    assert candidate(s = "000000011111110000000011111111000000") == 23
    assert candidate(s = "0110110110110110") == 11
    assert candidate(s = "0000000001") == 10
    assert candidate(s = "11111111111111111110000000000000000") == 18
    assert candidate(s = "010100101001010010100101001") == 17
    assert candidate(s = "000001111111111111") == 18
    assert candidate(s = "101010101010") == 6
    assert candidate(s = "0001111000") == 7
    assert candidate(s = "1001001001001001001001001001001001001001001001") == 31
    assert candidate(s = "0000011111") == 10
    assert candidate(s = "11111111111111111111") == 19
    assert candidate(s = "1000000000") == 8
    assert candidate(s = "1111111111111111") == 15
    assert candidate(s = "000111000111000") == 9
    assert candidate(s = "0110110110110110110110110110110110110110110110") == 31
    assert candidate(s = "110001010101101010010101011110000101010101") == 22
    assert candidate(s = "111001010101010") == 7
    assert candidate(s = "01000110011001100110") == 12
    assert candidate(s = "101010101010101010101010101010101010101") == 20
    assert candidate(s = "0000001111111111") == 16
    assert candidate(s = "000111111110000") == 11
    assert candidate(s = "00000000001111111111") == 20
    assert candidate(s = "100100100100100100100100100100100100") == 23
    assert candidate(s = "00000000000000000001111111111111111") == 35
    assert candidate(s = "111111111111111111111111111111111111111111111") == 44
    assert candidate(s = "111000111000111000111") == 12
    assert candidate(s = "11001100110011001100") == 10
    assert candidate(s = "11111111110000000000") == 9
    assert candidate(s = "11100011100011100011") == 11
    assert candidate(s = "01010101010101010101010101010101") == 17
    assert candidate(s = "0000000001111111110000000001111111110000000000111111111") == 37
    assert candidate(s = "0101010101010101010101010101010101010101") == 21
    assert candidate(s = "10010010010010010010") == 13
    assert candidate(s = "1010101010101010101010101010") == 14
    assert candidate(s = "00000000000000000000000000000000000000000000") == 43
    assert candidate(s = "111000111000") == 6
    assert candidate(s = "111000011111100") == 10
    assert candidate(s = "1000000000000000") == 14
    assert candidate(s = "000011111111") == 12
    assert candidate(s = "1100110011001100110011001100") == 14
    assert candidate(s = "0100101010101010") == 9
    assert candidate(s = "0101010101010101") == 9
    assert candidate(s = "1111111111111101") == 14
    assert candidate(s = "0101010101010101010") == 10
    assert candidate(s = "00010001000100010001") == 16
    assert candidate(s = "000011110000111100001111") == 16
    assert candidate(s = "0000111000111000") == 10
    assert candidate(s = "0101010101") == 6
    assert candidate(s = "11111111111111111111111110") == 24
    assert candidate(s = "00110011001100110011") == 12
    assert candidate(s = "0111111111000000") == 10
    assert candidate(s = "00000000000000000000") == 19
    assert candidate(s = "1111000011110000") == 8
    assert candidate(s = "10101010101010101010101010101010") == 16
    assert candidate(s = "1111100000") == 4
    assert candidate(s = "1111000000001111000000001111000000001111000000001111") == 36
    assert candidate(s = "0000000000000001") == 16
    assert candidate(s = "01010101010101") == 8
    assert candidate(s = "1101101101") == 6
    assert candidate(s = "1010101010101010101010101010101010101010") == 20
    assert candidate(s = "1111111111") == 9
    assert candidate(s = "111110000011111") == 10
    assert candidate(s = "00011100011100011100") == 12
    assert candidate(s = "11101110111011101110") == 14
    assert candidate(s = "000100010001000100") == 13
    assert candidate(s = "01010101010101010101") == 11
    assert candidate(s = "0101010101010101010101010101010101010101010101010101010101010101010101") == 36
    assert candidate(s = "1001001001001001001001001001") == 19
    assert candidate(s = "000001111100000111110000011111") == 20
    assert candidate(s = "0010100101001010010100101001010010") == 21
    assert candidate(s = "010101010101010") == 8
    assert candidate(s = "00011110001111") == 11
    assert candidate(s = "01101101101101101101") == 14
    assert candidate(s = "10101010101010101010") == 10
    assert candidate(s = "11111111111111110000000000000000") == 15
    assert candidate(s = "0001100110") == 7
    assert candidate(s = "0000000000011111111111") == 22
    assert candidate(s = "11111111111111110000000000") == 15
    assert candidate(s = "001100110011001100110011001100") == 16
    assert candidate(s = "001100110011") == 8
    assert candidate(s = "0111000001") == 7
    assert candidate(s = "0000111100001111") == 12


