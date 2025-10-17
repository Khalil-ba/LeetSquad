def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = "00000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "00110") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00110") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "1100110011") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1100110011") == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = "000111000111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000111000111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "001100") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "001100") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "10001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "10001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "010101010101010101") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "010101010101010101") == 17: {e}')
    
    total += 1
    try:
        result = candidate(target = "001001001") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "001001001") == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = "1111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "0000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "01010") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01010") == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = "101") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "101") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "11001100") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11001100") == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = "10010") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "10010") == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = "11001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "10111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "10111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "001100110011") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "001100110011") == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = "111100001111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "111100001111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "1001010") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1001010") == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = "010101") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "010101") == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = "1001001") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1001001") == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = "0101010101") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0101010101") == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = "110011") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "110011") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "111000111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "111000111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "10101010101010101010") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "10101010101010101010") == 20: {e}')
    
    total += 1
    try:
        result = candidate(target = "000011110000111100001111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000011110000111100001111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = "011010101010101010101010") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "011010101010101010101010") == 22: {e}')
    
    total += 1
    try:
        result = candidate(target = "10101010101010101010101010101010") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "10101010101010101010101010101010") == 32: {e}')
    
    total += 1
    try:
        result = candidate(target = "110011001100110") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "110011001100110") == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = "000000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "10001000100010001000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "10001000100010001000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = "101010101010101010101010101010101010101010101010") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "101010101010101010101010101010101010101010101010") == 48: {e}')
    
    total += 1
    try:
        result = candidate(target = "000111000111000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000111000111000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = "1001001001") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1001001001") == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = "1111111111111111111111111111111111111111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1111111111111111111111111111111111111111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "01010101010101010101") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01010101010101010101") == 19: {e}')
    
    total += 1
    try:
        result = candidate(target = "1001001001001001001001001001001001001001") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1001001001001001001001001001001001001001") == 27: {e}')
    
    total += 1
    try:
        result = candidate(target = "1010101010101010101010101010") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1010101010101010101010101010") == 28: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000111110000011111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000111110000011111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "0000000000111111111100000000001111111111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0000000000111111111100000000001111111111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "1010101010101010101010101010101010101010101010101010") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1010101010101010101010101010101010101010101010101010") == 52: {e}')
    
    total += 1
    try:
        result = candidate(target = "000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "1100110011001100110011001100") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1100110011001100110011001100") == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000000000000000000000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000000000000000000000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "00110011001100110011") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00110011001100110011") == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = "1111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111111111111111110") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111111111111111110") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "11000000000000000001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11000000000000000001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = "111111111111111111111111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "111111111111111111111111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "101010101010101010101010101010101010") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "101010101010101010101010101010101010") == 36: {e}')
    
    total += 1
    try:
        result = candidate(target = "0101010101010101010101010101") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0101010101010101010101010101") == 27: {e}')
    
    total += 1
    try:
        result = candidate(target = "110110110110110110110110110110") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "110110110110110110110110110110") == 20: {e}')
    
    total += 1
    try:
        result = candidate(target = "111100001111000011110000") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "111100001111000011110000") == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = "000111000111000111000111") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000111000111000111000111") == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = "100110011001100110011001") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "100110011001100110011001") == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = "01010101010101010101010101010101010101") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01010101010101010101010101010101010101") == 37: {e}')
    
    total += 1
    try:
        result = candidate(target = "000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "10010010010010010010010010010010010010010010010010") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "10010010010010010010010010010010010010010010010010") == 34: {e}')
    
    total += 1
    try:
        result = candidate(target = "1001001001001001001001001001001001001001001001001") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1001001001001001001001001001001001001001001001001") == 33: {e}')
    
    total += 1
    try:
        result = candidate(target = "01100110011001100110") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01100110011001100110") == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = "11110000111100001111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11110000111100001111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = "111000111000111000111000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "111000111000111000111000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111000001111100000111110000011111000001111100000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111000001111100000111110000011111000001111100000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "10101010101010101010101010") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "10101010101010101010101010") == 26: {e}')
    
    total += 1
    try:
        result = candidate(target = "11001100110011001100110011") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11001100110011001100110011") == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = "00110011001100110011001100110011001100110011001100") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00110011001100110011001100110011001100110011001100") == 24: {e}')
    
    total += 1
    try:
        result = candidate(target = "0111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "01010101010101010101010101") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01010101010101010101010101") == 25: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111000000000000000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111000000000000000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "1000000000000000000000000000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1000000000000000000000000000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111111111111111111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111111111111111111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000111110000011111000001111100000111110000011111") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000111110000011111000001111100000111110000011111") == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = "01001001001001001001001001001001") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01001001001001001001001001001001") == 21: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111000001111100000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111000001111100000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "11011011011011011011") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11011011011011011011") == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = "001001001001001001001001") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "001001001001001001001001") == 15: {e}')
    
    total += 1
    try:
        result = candidate(target = "11001100110011001100110011001100110011001100110011") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11001100110011001100110011001100110011001100110011") == 25: {e}')
    
    total += 1
    try:
        result = candidate(target = "001100110011001100110011001100110011001100110011") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "001100110011001100110011001100110011001100110011") == 23: {e}')
    
    total += 1
    try:
        result = candidate(target = "11001100110011001100110011001100") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11001100110011001100110011001100") == 16: {e}')
    
    total += 1
    try:
        result = candidate(target = "1001001001001001001001001001") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "1001001001001001001001001001") == 19: {e}')
    
    total += 1
    try:
        result = candidate(target = "00001111000011110000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00001111000011110000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = "111000111000111000111000111000111000111000111000111000111000111000") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "111000111000111000111000111000111000111000111000111000111000111000") == 22: {e}')
    
    total += 1
    try:
        result = candidate(target = "111111111111111111111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "111111111111111111111111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "0101010101010101010101010101010101010101010101010101") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0101010101010101010101010101010101010101010101010101") == 51: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "01110111011101110111") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01110111011101110111") == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = "0110110110") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0110110110") == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000111111111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "000111000111000111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000111000111000111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = "000011110000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000011110000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111111111111111111111111111111111111111111111110") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111111111111111111111111111111111111111111111110") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "01001001001001001001") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01001001001001001001") == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = "111111111111111111111110") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "111111111111111111111110") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "101010101010101010") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "101010101010101010") == 18: {e}')
    
    total += 1
    try:
        result = candidate(target = "100101010101010101010101") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "100101010101010101010101") == 23: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000000001111111111000000000011111111110000000000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000000001111111111000000000011111111110000000000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = "010101010101010101010101010101") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "010101010101010101010101010101") == 29: {e}')
    
    total += 1
    try:
        result = candidate(target = "0101010101010101010101010101010101") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0101010101010101010101010101010101") == 33: {e}')
    
    total += 1
    try:
        result = candidate(target = "000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "01010101010101010101010101010101010101010101010101") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01010101010101010101010101010101010101010101010101") == 49: {e}')
    
    total += 1
    try:
        result = candidate(target = "0011001100110011001100110011") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0011001100110011001100110011") == 13: {e}')
    
    total += 1
    try:
        result = candidate(target = "11001100110011001100") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11001100110011001100") == 10: {e}')
    
    total += 1
    try:
        result = candidate(target = "00001111111111110000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00001111111111110000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "01001001001001001001001001001001001001001001001001") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01001001001001001001001001001001001001001001001001") == 33: {e}')
    
    total += 1
    try:
        result = candidate(target = "00000000001111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "00000000001111111111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = "01001001001001001001001001001001001001001001") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01001001001001001001001001001001001001001001") == 29: {e}')
    
    total += 1
    try:
        result = candidate(target = "01010101010101010101010101010101") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "01010101010101010101010101010101") == 31: {e}')
    
    total += 1
    try:
        result = candidate(target = "0000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "0000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111111110000000000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111111110000000000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = "110011001100110011") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "110011001100110011") == 9: {e}')
    
    total += 1
    try:
        result = candidate(target = "10010010010010010010") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "10010010010010010010") == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = "11111111111111111111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "11111111111111111111") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = "00000") == 0
    assert candidate(target = "00110") == 2
    assert candidate(target = "1100110011") == 5
    assert candidate(target = "000111000111") == 3
    assert candidate(target = "001100") == 2
    assert candidate(target = "10001") == 3
    assert candidate(target = "010101010101010101") == 17
    assert candidate(target = "001001001") == 5
    assert candidate(target = "1111111111") == 1
    assert candidate(target = "0000000000") == 0
    assert candidate(target = "01010") == 4
    assert candidate(target = "101") == 3
    assert candidate(target = "11001100") == 4
    assert candidate(target = "10010") == 4
    assert candidate(target = "11001") == 3
    assert candidate(target = "10111") == 3
    assert candidate(target = "001100110011") == 5
    assert candidate(target = "111100001111") == 3
    assert candidate(target = "11111") == 1
    assert candidate(target = "1001010") == 6
    assert candidate(target = "010101") == 5
    assert candidate(target = "1001001") == 5
    assert candidate(target = "0101010101") == 9
    assert candidate(target = "110011") == 3
    assert candidate(target = "111000111") == 3
    assert candidate(target = "10101010101010101010") == 20
    assert candidate(target = "000011110000111100001111") == 5
    assert candidate(target = "011010101010101010101010") == 22
    assert candidate(target = "10101010101010101010101010101010") == 32
    assert candidate(target = "110011001100110") == 8
    assert candidate(target = "000000000000000000000000000000000000000000000000") == 0
    assert candidate(target = "10001000100010001000") == 10
    assert candidate(target = "101010101010101010101010101010101010101010101010") == 48
    assert candidate(target = "000111000111000") == 4
    assert candidate(target = "1001001001") == 7
    assert candidate(target = "1111111111111111111111111111111111111111111111111111111111111111") == 1
    assert candidate(target = "01010101010101010101") == 19
    assert candidate(target = "1001001001001001001001001001001001001001") == 27
    assert candidate(target = "1010101010101010101010101010") == 28
    assert candidate(target = "00000111110000011111") == 3
    assert candidate(target = "0000000000111111111100000000001111111111") == 3
    assert candidate(target = "11111111111111111111111111") == 1
    assert candidate(target = "1010101010101010101010101010101010101010101010101010") == 52
    assert candidate(target = "000000000000000000000001") == 1
    assert candidate(target = "1100110011001100110011001100") == 14
    assert candidate(target = "00000000000000000000000000000000000000000000000000000000000000000") == 0
    assert candidate(target = "00000000000000000000000000") == 0
    assert candidate(target = "00110011001100110011") == 9
    assert candidate(target = "1111111111111111111111111111") == 1
    assert candidate(target = "11111111111111111110") == 2
    assert candidate(target = "11000000000000000001") == 3
    assert candidate(target = "111111111111111111111111111111111111111111111111") == 1
    assert candidate(target = "101010101010101010101010101010101010") == 36
    assert candidate(target = "0101010101010101010101010101") == 27
    assert candidate(target = "110110110110110110110110110110") == 20
    assert candidate(target = "111100001111000011110000") == 6
    assert candidate(target = "000111000111000111000111") == 7
    assert candidate(target = "100110011001100110011001") == 13
    assert candidate(target = "01010101010101010101010101010101010101") == 37
    assert candidate(target = "000000000000000000000000000000000000") == 0
    assert candidate(target = "10010010010010010010010010010010010010010010010010") == 34
    assert candidate(target = "1001001001001001001001001001001001001001001001001") == 33
    assert candidate(target = "01100110011001100110") == 10
    assert candidate(target = "11110000111100001111") == 5
    assert candidate(target = "111000111000111000111000") == 8
    assert candidate(target = "11111000001111100000111110000011111000001111100000") == 10
    assert candidate(target = "00000000000000000000000000000000000000000000000000") == 0
    assert candidate(target = "10101010101010101010101010") == 26
    assert candidate(target = "11001100110011001100110011") == 13
    assert candidate(target = "00110011001100110011001100110011001100110011001100") == 24
    assert candidate(target = "0111111111111111111111111111") == 1
    assert candidate(target = "01010101010101010101010101") == 25
    assert candidate(target = "11111000000000000000") == 2
    assert candidate(target = "1000000000000000000000000000") == 2
    assert candidate(target = "11111111111111111111111111111111111111111111") == 1
    assert candidate(target = "00000111110000011111000001111100000111110000011111") == 9
    assert candidate(target = "01001001001001001001001001001001") == 21
    assert candidate(target = "11111000001111100000") == 4
    assert candidate(target = "00000000000000000001") == 1
    assert candidate(target = "11011011011011011011") == 13
    assert candidate(target = "001001001001001001001001") == 15
    assert candidate(target = "11001100110011001100110011001100110011001100110011") == 25
    assert candidate(target = "001100110011001100110011001100110011001100110011") == 23
    assert candidate(target = "11001100110011001100110011001100") == 16
    assert candidate(target = "1001001001001001001001001001") == 19
    assert candidate(target = "00001111000011110000") == 4
    assert candidate(target = "111000111000111000111000111000111000111000111000111000111000111000") == 22
    assert candidate(target = "111111111111111111111111111111111111") == 1
    assert candidate(target = "0101010101010101010101010101010101010101010101010101") == 51
    assert candidate(target = "00000000000000000000000000000000000000000000") == 0
    assert candidate(target = "01110111011101110111") == 9
    assert candidate(target = "0110110110") == 6
    assert candidate(target = "00000111111111111111") == 1
    assert candidate(target = "000111000111000111") == 5
    assert candidate(target = "000011110000") == 2
    assert candidate(target = "11111111111111111111111111111111111111111111111110") == 2
    assert candidate(target = "01001001001001001001") == 13
    assert candidate(target = "111111111111111111111110") == 2
    assert candidate(target = "101010101010101010") == 18
    assert candidate(target = "100101010101010101010101") == 23
    assert candidate(target = "00000000001111111111000000000011111111110000000000") == 4
    assert candidate(target = "010101010101010101010101010101") == 29
    assert candidate(target = "0101010101010101010101010101010101") == 33
    assert candidate(target = "000000000000000000000000000000") == 0
    assert candidate(target = "01010101010101010101010101010101010101010101010101") == 49
    assert candidate(target = "0011001100110011001100110011") == 13
    assert candidate(target = "11001100110011001100") == 10
    assert candidate(target = "00001111111111110000") == 2
    assert candidate(target = "01001001001001001001001001001001001001001001001001") == 33
    assert candidate(target = "00000000001111111111") == 1
    assert candidate(target = "01001001001001001001001001001001001001001001") == 29
    assert candidate(target = "01010101010101010101010101010101") == 31
    assert candidate(target = "0000000000000000000000000000") == 0
    assert candidate(target = "11111111110000000000") == 2
    assert candidate(target = "110011001100110011") == 9
    assert candidate(target = "10010010010010010010") == 14
    assert candidate(target = "11111111111111111111") == 1


