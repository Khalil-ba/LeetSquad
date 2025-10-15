def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "1111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00110011") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00110011") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "110") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110010011100100111001") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110010011100100111001") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101101010101010101010101") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101101010101010101010101") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "110010110010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110010110010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "000110110001101100011011") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000110110001101100011011") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "00111111001111110011111100111111001111110011111100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00111111001111110011111100111111001111110011111100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101110") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101110") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000111111000000111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000111111000000111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000111111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000111111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000111111111111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000111111111111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100001111000011110000111100001111000011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100001111000011110000111100001111000011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101010101011") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101010101011") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101001010101010") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101001010101010") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010110101010101") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010110101010101") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000001111111111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000001111111111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11010101010101010101010101010101") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11010101010101010101010101010101") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000111111111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000111111111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111110101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111110101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001100110011") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001100110011") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000111111111000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000111111111000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101001010101010101010") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101001010101010101010") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111000011110000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111000011110000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1011010010110100") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011010010110100") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010010101001010100101010") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010010101001010100101010") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111010101010") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111010101010") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000111111000000111111000000111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000111111000000111111000000111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "11000011000011000011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11000011000011000011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101001011") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101001011") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "111001100110011001100110011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111001100110011001100110011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111000000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111000000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111000011110000111100001111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111000011110000111100001111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000111111100000000111111110000000011111111") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000111111100000000111111110000000011111111") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000111111000000") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000111111000000") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "011111000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011111000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111000011110000") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111000011110000") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101110101000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101110101000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "11100101101000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11100101101000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001100110011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001100110011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "001100110011001100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001100110011001100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000111111") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000111111") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111000001111100000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111000001111100000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "110010101001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110010101001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100000011") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100000011") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101011") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101011") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111100001111000011110000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111100001111000011110000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110001000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110001000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10100101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10100101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000011111111111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000011111111111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100001111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100001111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "01101101101101") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01101101101101") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111000000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111000000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111000000111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111000000111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111100000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111100000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111110000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111110000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001100110") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001100110") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "01101010100") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01101010100") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111111000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111111000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010010101010") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010010101010") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011110000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011110000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111100000000011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111100000000011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "001001110010011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001110010011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111111100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111111100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111000000001111111100000000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111000000001111111100000000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "001100110011") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001100110011") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111000000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111000000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "10010010010010") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10010010010010") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111000000001111111100000000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111000000001111111100000000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000001111111111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000001111111111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111000000000011111111110000000000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111000000000011111111110000000000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101010100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101010100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111110000000000") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111110000000000") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111000000011111111100000001111111110000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111000000011111111100000001111111110000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111010101001") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111010101001") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110000011100000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110000011100000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111101111111011111110") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111101111111011111110") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000111111110000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000111111110000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111100000000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111100000000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010110100") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010110100") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "101110010110") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101110010110") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101101010101001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101101010101001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000011111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000011111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000111111111111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000111111111111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "110110001101100") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110110001101100") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100001111000011110000") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100001111000011110000") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "110110110110110110110110") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110110110110110110110110") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00110011001100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00110011001100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000100011") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000100011") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111100000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111100000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "10100101001010010100101001010010100101001010") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10100101001010010100101001010010100101001010") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000010101010") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000010101010") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111100000000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111100000000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11100111001110011100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11100111001110011100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101110001010") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101110001010") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "11000000110000001100000011000000110000001100000011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11000000110000001100000011000000110000001100000011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000100000001000000010") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000100000001000000010") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "111100001111000011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111100001111000011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000001") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000001") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000001111111111111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000001111111111111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111000111000111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111000111000111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111110000000") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111110000000") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000001111111111111111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000001111111111111111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "010100011101010") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010100011101010") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010001010101010101010") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010001010101010101010") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000111111000000111111000000111111000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000111111000000111111000000111111000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "110101010101010101") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110101010101010101") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "100010001000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100010001000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111000011110000111100001111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111000011110000111100001111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111110000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111110000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010010") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010010") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "10010010010") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10010010010") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00110011001100110011") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00110011001100110011") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "010110001110") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010110001110") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "011011010101010101010101010") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011011010101010101010101010") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000011111111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000011111111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000000001111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000000001111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111100000") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111100000") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100110011001100110011001100110011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100110011001100110011001100110011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00100100100100100100100100100100100100100100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00100100100100100100100100100100100100100100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111000111000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111000111000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111000010101") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000010101") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101011100010101") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101011100010101") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100101101001011") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100101101001011") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110110110110110110110110") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110110110110110110110110") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111000000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111000000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00111100111100111100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00111100111100111100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "100110011001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100110011001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "111001001001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111001001001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "11101110111011101110") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11101110111011101110") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00011100011100011100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00011100011100011100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001100110011001") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001100110011001") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "100100100100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100100100100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0011001100110011001100110011") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0011001100110011001100110011") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100110011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100110011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010100") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010100") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101011010100010") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101011010100010") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "0110011001100110011001100110011") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110011001100110011001100110011") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010010101010101010101010") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010010101010101010101010") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111110000000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111110000000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "000100100100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000100100100") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111110000000000111111111110000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111110000000000111111111110000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111000000011111110000000") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111000000011111110000000") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "11000011110000111100") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11000011110000111100") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000111111111111111") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000111111111111111") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "100110011001100110011001") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100110011001100110011001") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100110011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100110011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000111111000000111111000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000111111000000111111000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "011011011011") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011011011011") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111111110") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111111110") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001111000011110000111100001111000011110000111100") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001111000011110000111100001111000011110000111100") == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "1111") == -1
    assert candidate(s = "1100110") == 2
    assert candidate(s = "110011") == -1
    assert candidate(s = "00110011") == 2
    assert candidate(s = "0101010") == 0
    assert candidate(s = "111") == -1
    assert candidate(s = "11110000") == 2
    assert candidate(s = "1110") == -1
    assert candidate(s = "0000") == -1
    assert candidate(s = "01010") == 0
    assert candidate(s = "111000") == 1
    assert candidate(s = "10101") == 0
    assert candidate(s = "1100") == 1
    assert candidate(s = "010") == 0
    assert candidate(s = "1010101") == 0
    assert candidate(s = "1010") == 0
    assert candidate(s = "0101") == 0
    assert candidate(s = "000111") == 1
    assert candidate(s = "000") == -1
    assert candidate(s = "01010101") == 0
    assert candidate(s = "10101010") == 0
    assert candidate(s = "110") == 1
    assert candidate(s = "1010101010") == 0
    assert candidate(s = "010101") == 0
    assert candidate(s = "101010") == 0
    assert candidate(s = "1101001") == 2
    assert candidate(s = "11001100") == 2
    assert candidate(s = "0011") == 1
    assert candidate(s = "0101010101") == 0
    assert candidate(s = "0011001") == 2
    assert candidate(s = "1001") == 1
    assert candidate(s = "101010101010101010") == 0
    assert candidate(s = "1110010011100100111001") == -1
    assert candidate(s = "010101101010101010101010101") == 3
    assert candidate(s = "110010110010") == 2
    assert candidate(s = "000110110001101100011011") == 6
    assert candidate(s = "00111111001111110011111100111111001111110011111100") == -1
    assert candidate(s = "101010101110") == -1
    assert candidate(s = "000000111111000000111111") == 6
    assert candidate(s = "0000000111111") == 3
    assert candidate(s = "000000000000000000111111111111111") == -1
    assert candidate(s = "11110000111100001111000011110000111100001111000011") == -1
    assert candidate(s = "010101010101010101010101010101010101010101010101011") == 25
    assert candidate(s = "101010101010101001010101010") == 8
    assert candidate(s = "1010101010101010101") == 0
    assert candidate(s = "010101010101010110101010101") == 8
    assert candidate(s = "0000000000000001111111111111") == -1
    assert candidate(s = "11010101010101010101010101010101") == -1
    assert candidate(s = "010101010101010101010101") == 0
    assert candidate(s = "10101010101010101010101010") == 0
    assert candidate(s = "000000000000111111111111") == 6
    assert candidate(s = "0000111110101010") == 2
    assert candidate(s = "1001100110011") == 3
    assert candidate(s = "0000000000111111111000") == -1
    assert candidate(s = "101010101001010101010101010") == 5
    assert candidate(s = "00001111000011110000") == -1
    assert candidate(s = "111000111000111") == -1
    assert candidate(s = "1011010010110100") == 4
    assert candidate(s = "000111000111000111") == 3
    assert candidate(s = "101010101010101010101010") == 0
    assert candidate(s = "1010010101001010100101010") == -1
    assert candidate(s = "111010101010") == -1
    assert candidate(s = "101010101010101010101") == 0
    assert candidate(s = "111111000000111111000000111111000000111111") == -1
    assert candidate(s = "010101010101010101") == 0
    assert candidate(s = "101010101010101010101010101") == 0
    assert candidate(s = "1010101010101010101010101010101010101010101010101") == 0
    assert candidate(s = "1100110011") == -1
    assert candidate(s = "111000111000111000111000111000") == 5
    assert candidate(s = "11000011000011000011") == -1
    assert candidate(s = "0101010101001011") == 2
    assert candidate(s = "111001100110011001100110011") == -1
    assert candidate(s = "1111111111111111111000000000000000") == -1
    assert candidate(s = "1010101010101010") == 0
    assert candidate(s = "111100001111000011110000111100001111") == -1
    assert candidate(s = "0000000111111100000000111111110000000011111111") == 11
    assert candidate(s = "111111000000111111000000") == 6
    assert candidate(s = "011111000000") == -1
    assert candidate(s = "111100001111000011110000") == 6
    assert candidate(s = "10101110101000") == 1
    assert candidate(s = "110011001100") == 3
    assert candidate(s = "11100101101000") == 3
    assert candidate(s = "0011001100110011") == 4
    assert candidate(s = "001100110011001100") == -1
    assert candidate(s = "000000111111") == 3
    assert candidate(s = "11111000001111100000") == 4
    assert candidate(s = "110010101001") == 2
    assert candidate(s = "111100000011") == 3
    assert candidate(s = "01010101011") == 5
    assert candidate(s = "0101010101010101010101010101010101") == 0
    assert candidate(s = "0000111100001111000011110000") == -1
    assert candidate(s = "1110001000") == -1
    assert candidate(s = "010101010101010101010101010") == 0
    assert candidate(s = "10100101010") == 2
    assert candidate(s = "000000000000000011111111111111") == -1
    assert candidate(s = "01010101010101010101010") == 0
    assert candidate(s = "11110000111100001111") == -1
    assert candidate(s = "01010101010101010101010101") == 0
    assert candidate(s = "01101101101101") == -1
    assert candidate(s = "111111111111111111000000000000000") == -1
    assert candidate(s = "101010101010") == 0
    assert candidate(s = "111111000000111111") == -1
    assert candidate(s = "111111111111111100000000000000") == -1
    assert candidate(s = "1111111111110000000000") == -1
    assert candidate(s = "0011001100110") == 3
    assert candidate(s = "01101010100") == 4
    assert candidate(s = "000111111000") == 3
    assert candidate(s = "0101010010101010") == -1
    assert candidate(s = "11111111111111111111") == -1
    assert candidate(s = "000011110000") == -1
    assert candidate(s = "1111111111100000000011") == -1
    assert candidate(s = "001001110010011") == 4
    assert candidate(s = "00001111111100") == -1
    assert candidate(s = "000111000111000") == -1
    assert candidate(s = "11111111000000001111111100000000") == 8
    assert candidate(s = "001100110011") == 3
    assert candidate(s = "1111111000000") == 3
    assert candidate(s = "10010010010010") == -1
    assert candidate(s = "111111111000000001111111100000000") == 8
    assert candidate(s = "00000000001111111111") == 5
    assert candidate(s = "101010101010101010101010101010101") == 0
    assert candidate(s = "1111111111000000000011111111110000000000") == 10
    assert candidate(s = "01010101010101010101010101010101010101010101010100") == -1
    assert candidate(s = "11001100110011001100") == 5
    assert candidate(s = "11111111110000000000") == 5
    assert candidate(s = "1111111000000011111111100000001111111110000000") == -1
    assert candidate(s = "01010101010101010101010101010101") == 0
    assert candidate(s = "0101010101010101010101010101010101010101") == 0
    assert candidate(s = "1010101010101010101010101010") == 0
    assert candidate(s = "11110000111100") == -1
    assert candidate(s = "00000000000000000000000000000000000000000000000000") == -1
    assert candidate(s = "111010101001") == -1
    assert candidate(s = "111000111000111000111000111") == -1
    assert candidate(s = "1110000011100000") == -1
    assert candidate(s = "111111101111111011111110") == -1
    assert candidate(s = "0000111111110000") == 4
    assert candidate(s = "111000111000") == 2
    assert candidate(s = "1111111100000000") == 4
    assert candidate(s = "1010101010110100") == 2
    assert candidate(s = "101110010110") == -1
    assert candidate(s = "0101101010101001") == 3
    assert candidate(s = "111100001111") == -1
    assert candidate(s = "000011111111") == -1
    assert candidate(s = "00000000000000000111111111111111") == -1
    assert candidate(s = "110110001101100") == 4
    assert candidate(s = "1100110011001100110011001100") == 7
    assert candidate(s = "11110000111100001111000011110000") == 8
    assert candidate(s = "110110110110110110110110") == -1
    assert candidate(s = "00110011001100") == -1
    assert candidate(s = "010101010101") == 0
    assert candidate(s = "111000100011") == 2
    assert candidate(s = "1111111111111111111111111111") == -1
    assert candidate(s = "0101010101010101") == 0
    assert candidate(s = "00001111") == 2
    assert candidate(s = "11111100000000") == -1
    assert candidate(s = "10100101001010010100101001010010100101001010") == -1
    assert candidate(s = "1111000010101010") == 2
    assert candidate(s = "11111111111111100000000000000000") == -1
    assert candidate(s = "11100111001110011100") == -1
    assert candidate(s = "1010101110001010") == 1
    assert candidate(s = "0101010101010101010101010101") == 0
    assert candidate(s = "11000000110000001100000011000000110000001100000011") == -1
    assert candidate(s = "0000000100000001000000010") == -1
    assert candidate(s = "111100001111000011") == -1
    assert candidate(s = "00000000000000000000000000000000000000000000000001") == -1
    assert candidate(s = "0101010101010101010") == 0
    assert candidate(s = "0000000000001111111111111111") == -1
    assert candidate(s = "000111000111000111000111000111") == 5
    assert candidate(s = "11111110000000") == 3
    assert candidate(s = "0000000000000001111111111111111") == 8
    assert candidate(s = "010100011101010") == 1
    assert candidate(s = "010101010001010101010101010") == -1
    assert candidate(s = "11111111111111111111111111111111111111111111111111") == -1
    assert candidate(s = "000000111111000000111111000000111111000000") == -1
    assert candidate(s = "110101010101010101") == -1
    assert candidate(s = "100010001000") == -1
    assert candidate(s = "00001111000011110000111100001111") == 8
    assert candidate(s = "1111111111111110000000000000") == -1
    assert candidate(s = "101010101000") == -1
    assert candidate(s = "10101010010") == 4
    assert candidate(s = "10010010010") == -1
    assert candidate(s = "00110011001100110011") == 5
    assert candidate(s = "010110001110") == 3
    assert candidate(s = "011011010101010101010101010") == 12
    assert candidate(s = "010101010101010101010101010101010101010") == 0
    assert candidate(s = "0101010101010101010101010101010101010101010101010101") == 0
    assert candidate(s = "10101010101010101010101010101010101010101010101010101") == 0
    assert candidate(s = "00000000000000000000") == -1
    assert candidate(s = "1010101010101") == 0
    assert candidate(s = "1111000011110000") == 4
    assert candidate(s = "0000000011111111") == 4
    assert candidate(s = "010101010101010101010101010101010101010101010101010") == 0
    assert candidate(s = "1111000000001111") == 4
    assert candidate(s = "1111100000") == 2
    assert candidate(s = "11001100110011001100110011001100110011001100110011") == -1
    assert candidate(s = "00100100100100100100100100100100100100100100") == -1
    assert candidate(s = "000111000111000111000111000") == -1
    assert candidate(s = "01010101010101") == 0
    assert candidate(s = "111000010101") == 2
    assert candidate(s = "1001001001001") == -1
    assert candidate(s = "101011100010101") == 1
    assert candidate(s = "0100101101001011") == 4
    assert candidate(s = "0110110110110110110110110") == -1
    assert candidate(s = "11111111111111111000000000000000") == -1
    assert candidate(s = "1010101010101010101010") == 0
    assert candidate(s = "1010101010101010101010101010101010101010") == 0
    assert candidate(s = "00111100111100111100") == -1
    assert candidate(s = "100110011001") == 3
    assert candidate(s = "111001001001") == 3
    assert candidate(s = "11101110111011101110") == -1
    assert candidate(s = "00011100011100011100") == -1
    assert candidate(s = "1001100110011001") == 4
    assert candidate(s = "01010101010101010101010101010101010101010101") == 0
    assert candidate(s = "100100100100") == -1
    assert candidate(s = "1010101010101010101010101010101010101010101010101010") == 0
    assert candidate(s = "0011001100110011001100110011") == 7
    assert candidate(s = "01010101010101010101") == 0
    assert candidate(s = "110011001100110011001100110011") == -1
    assert candidate(s = "1100110011001") == 3
    assert candidate(s = "11001100110011") == -1
    assert candidate(s = "101010101010101010101010101010101010101010101010100") == 25
    assert candidate(s = "1001001001001001001001001001") == -1
    assert candidate(s = "01010101010101010101010101010101010101010101010101010") == 0
    assert candidate(s = "1101011010100010") == 3
    assert candidate(s = "0110011001100110011001100110011") == 8
    assert candidate(s = "101010010101010101010101010") == 3
    assert candidate(s = "1111111111110000000000000000") == -1
    assert candidate(s = "101010101010101010101010101010101010") == 0
    assert candidate(s = "000100100100") == -1
    assert candidate(s = "1111000000") == -1
    assert candidate(s = "0101010101010") == 0
    assert candidate(s = "111111111110000000000111111111110000000000") == -1
    assert candidate(s = "1111111000000011111110000000") == 6
    assert candidate(s = "11000011110000111100") == 5
    assert candidate(s = "10101010101010101010") == 0
    assert candidate(s = "0000000000000000000111111111111111") == -1
    assert candidate(s = "100110011001100110011001") == 6
    assert candidate(s = "11001100110011001100110011") == -1
    assert candidate(s = "000000111111000000111111000000") == -1
    assert candidate(s = "011011011011") == -1
    assert candidate(s = "0000000000000000000000000000") == -1
    assert candidate(s = "11111111111111111111111111111111111111111111111110") == -1
    assert candidate(s = "00001111000011110000111100001111000011110000111100") == -1


