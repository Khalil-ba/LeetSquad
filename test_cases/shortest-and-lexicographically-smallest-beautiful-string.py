def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100",k = 6) == "1100110011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100",k = 6) == "1100110011": {e}')
    
    total += 1
    try:
        result = candidate(s = "100011001",k = 3) == "11001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100011001",k = 3) == "11001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010",k = 5) == "101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010",k = 5) == "101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111",k = 5) == "11111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111",k = 5) == "11111": {e}')
    
    total += 1
    try:
        result = candidate(s = "100100100",k = 3) == "1001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100100100",k = 3) == "1001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "111010101",k = 2) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111010101",k = 2) == "11": {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "111000",k = 2) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000",k = 2) == "11": {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001",k = 4) == "1001001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001",k = 4) == "1001001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1111",k = 2) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111",k = 2) == "11": {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101",k = 5) == "101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101",k = 5) == "101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100",k = 5) == "100110011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100",k = 5) == "100110011": {e}')
    
    total += 1
    try:
        result = candidate(s = "010101",k = 3) == "10101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101",k = 3) == "10101": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101",k = 4) == "1010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101",k = 4) == "1010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "1011",k = 2) == "11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011",k = 2) == "11": {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010",k = 10) == "1010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010",k = 10) == "1010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101010",k = 12) == "10101010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101010",k = 12) == "10101010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010",k = 10) == "1010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010",k = 10) == "1010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "110110110110110110110110110110",k = 5) == "1011011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110110110110110110110110110110",k = 5) == "1011011": {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000",k = 5) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000",k = 5) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001",k = 5) == "1001001001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001",k = 5) == "1001001001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010",k = 10) == "1010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010",k = 10) == "1010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000111100001111000011110000111100001111000011110000",k = 8) == "111100001111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000111100001111000011110000111100001111000011110000",k = 8) == "111100001111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111111111111111111111111111111111",k = 15) == "111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111111111111111111111111111111111",k = 15) == "111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(s = "01001001001001001001001001001001001001001001001001001001001001001001",k = 8) == "1001001001001001001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01001001001001001001001001001001001001001001001001001001001001001001",k = 8) == "1001001001001001001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101010101010101010101010101",k = 12) == "10101010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101010101010101010101010101",k = 12) == "10101010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000",k = 3) == "111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000",k = 3) == "111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1100011000110001100011000110001100011000",k = 6) == "110001100011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100011000110001100011000110001100011000",k = 6) == "110001100011": {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010",k = 9) == "10101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010",k = 9) == "10101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111111111",k = 50) == "11111111111111111111111111111111111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111111111",k = 50) == "11111111111111111111111111111111111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101010101",k = 5) == "101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101010101",k = 5) == "101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010",k = 10) == "1010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010",k = 10) == "1010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111",k = 10) == "1111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111",k = 10) == "1111111111": {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000111000",k = 9) == "111000111000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000111000",k = 9) == "111000111000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101010101",k = 8) == "101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101010101",k = 8) == "101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101",k = 10) == "1010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101",k = 10) == "1010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "1001100110011001100110011001100110011001100110011001100110011001100110011001",k = 6) == "1100110011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001100110011001100110011001100110011001100110011001100110011001100110011001",k = 6) == "1100110011": {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101",k = 3) == "10101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101",k = 3) == "10101": {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111",k = 6) == "111000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111",k = 6) == "111000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101010101",k = 10) == "1010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101010101",k = 10) == "1010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000",k = 11) == "11000111000111000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000",k = 11) == "11000111000111000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1101001101001101001101001101",k = 4) == "1001101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101001101001101001101001101",k = 4) == "1001101": {e}')
    
    total += 1
    try:
        result = candidate(s = "111011101110111011101110",k = 7) == "101110111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111011101110111011101110",k = 7) == "101110111": {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001",k = 3) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001",k = 3) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000000000000000000000000000000000000000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000000000000000000000000000000000000000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100110011001100110011001100110011001100",k = 15) == "10011001100110011001100110011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100110011001100110011001100110011001100",k = 15) == "10011001100110011001100110011": {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000000000000000000001",k = 1) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000000000000000000001",k = 1) == "1": {e}')
    
    total += 1
    try:
        result = candidate(s = "0001000100010001000100010001000100010001000100010001",k = 3) == "100010001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001000100010001000100010001000100010001000100010001",k = 3) == "100010001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101010",k = 7) == "1010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101010",k = 7) == "1010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000000000000000000000",k = 3) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000000000000000000000",k = 3) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "1110011100011100111000011100000111000000",k = 6) == "11100111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110011100011100111000011100000111000000",k = 6) == "11100111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1110000001110000011100000111000001110000011100000111",k = 6) == "11100000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110000001110000011100000111000001110000011100000111",k = 6) == "11100000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100110011001100110011001100110011001100",k = 11) == "100110011001100110011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100110011001100110011001100110011001100",k = 11) == "100110011001100110011": {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100110011001100",k = 6) == "1100110011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100110011001100",k = 6) == "1100110011": {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010",k = 13) == "1010101010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010",k = 13) == "1010101010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000",k = 6) == "111000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000",k = 6) == "111000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010",k = 15) == "10101010101010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010",k = 15) == "10101010101010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101",k = 15) == "10101010101010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101",k = 15) == "10101010101010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "10001000100010001000100010001000100010001000",k = 5) == "10001000100010001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10001000100010001000100010001000100010001000",k = 5) == "10001000100010001": {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010101010101010101",k = 15) == "10101010101010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010101010101010101",k = 15) == "10101010101010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "110001100011000110001100011000110001100011000",k = 5) == "10001100011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110001100011000110001100011000110001100011000",k = 5) == "10001100011": {e}')
    
    total += 1
    try:
        result = candidate(s = "11000110001100011000110001100011000",k = 6) == "110001100011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11000110001100011000110001100011000",k = 6) == "110001100011": {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101010101",k = 10) == "1010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101010101",k = 10) == "1010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101",k = 5) == "101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101",k = 5) == "101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010",k = 10) == "1010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010",k = 10) == "1010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101",k = 5) == "101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101",k = 5) == "101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111",k = 6) == "111000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111",k = 6) == "111000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "111110000000000000000000000000000000000000000000",k = 5) == "11111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111110000000000000000000000000000000000000000000",k = 5) == "11111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101101101101101101101101101101101101",k = 7) == "1011011011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101101101101101101101101101101101101",k = 7) == "1011011011": {e}')
    
    total += 1
    try:
        result = candidate(s = "11100111001110011100111001110011100111001110011100",k = 8) == "110011100111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11100111001110011100111001110011100111001110011100",k = 8) == "110011100111": {e}')
    
    total += 1
    try:
        result = candidate(s = "10000001000000100000010000001",k = 3) == "100000010000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000001000000100000010000001",k = 3) == "100000010000001": {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100001111000011110000",k = 4) == "1111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100001111000011110000",k = 4) == "1111": {e}')
    
    total += 1
    try:
        result = candidate(s = "0010010010010010010010010010010010010010",k = 2) == "1001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0010010010010010010010010010010010010010",k = 2) == "1001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010",k = 20) == "101010101010101010101010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010",k = 20) == "101010101010101010101010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010",k = 8) == "101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010",k = 8) == "101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "111110000011111000001111100000111110000011111",k = 8) == "1110000011111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111110000011111000001111100000111110000011111",k = 8) == "1110000011111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010",k = 15) == "10101010101010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010",k = 15) == "10101010101010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000",k = 9) == "111000111000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000",k = 9) == "111000111000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1000001000001000001000001000001000001000001000001000001000001",k = 2) == "1000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000001000001000001000001000001000001000001000001000001000001",k = 2) == "1000001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000000000000000000000000001",k = 1) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000000000000000000000000001",k = 1) == "1": {e}')
    
    total += 1
    try:
        result = candidate(s = "1110000111000011100001110000",k = 4) == "10000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110000111000011100001110000",k = 4) == "10000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010",k = 7) == "1010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010",k = 7) == "1010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "000100010001000100010001",k = 2) == "10001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000100010001000100010001",k = 2) == "10001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1000100010001000100010001",k = 3) == "100010001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000100010001000100010001",k = 3) == "100010001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001",k = 5) == "1001001001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001",k = 5) == "1001001001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000000000000001",k = 1) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000000000000001",k = 1) == "1": {e}')
    
    total += 1
    try:
        result = candidate(s = "11111000001111100000111110000011111",k = 5) == "11111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111000001111100000111110000011111",k = 5) == "11111": {e}')
    
    total += 1
    try:
        result = candidate(s = "0110110110110110110110110110110110110110110110",k = 4) == "11011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0110110110110110110110110110110110110110110110",k = 4) == "11011": {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000000000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000000000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "11000001110000011100000111000001110000011100000111",k = 7) == "10000011100000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11000001110000011100000111000001110000011100000111",k = 7) == "10000011100000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "001001001001001001001001001001001001001",k = 3) == "1001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001001001001001001001001001001001001",k = 3) == "1001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111",k = 15) == "111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111",k = 15) == "111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010",k = 8) == "101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010",k = 8) == "101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000000000000000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000000000000000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111",k = 9) == "111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111",k = 9) == "111111111": {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101010101",k = 10) == "1010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101010101",k = 10) == "1010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100110011001100110011001100110011001100",k = 10) == "110011001100110011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100110011001100110011001100110011001100",k = 10) == "110011001100110011": {e}')
    
    total += 1
    try:
        result = candidate(s = "100000100000100000100000100000100000100000100000",k = 3) == "1000001000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000100000100000100000100000100000100000100000",k = 3) == "1000001000001": {e}')
    
    total += 1
    try:
        result = candidate(s = "100110011001100110011001100110011001100110011001100110011001100110011001",k = 9) == "10011001100110011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100110011001100110011001100110011001100110011001100110011001100110011001",k = 9) == "10011001100110011": {e}')
    
    total += 1
    try:
        result = candidate(s = "111000111000111000111000111000111000111000111000111000111000111000111000111000111000",k = 7) == "1000111000111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111000111000111000111000111000111000111000111000111000111000111000111000111000111000",k = 7) == "1000111000111": {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010",k = 7) == "1010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010",k = 7) == "1010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000111100001111",k = 8) == "111100001111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000111100001111",k = 8) == "111100001111": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010",k = 12) == "10101010101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010",k = 12) == "10101010101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101",k = 3) == "10101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101",k = 3) == "10101": {e}')
    
    total += 1
    try:
        result = candidate(s = "001001001001001001001001001001001001001001001001",k = 5) == "1001001001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001001001001001001001001001001001001001001001",k = 5) == "1001001001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001001001001001",k = 12) == "1001001001001001001001001001001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001001001001001",k = 12) == "1001001001001001001001001001001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000011111111111111111111111111111111111111111111111111111111111111",k = 20) == "11111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000011111111111111111111111111111111111111111111111111111111111111",k = 20) == "11111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(s = "110110110110110110110110110110110110110",k = 7) == "1011011011"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110110110110110110110110110110110110110",k = 7) == "1011011011": {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010",k = 6) == "10101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010",k = 6) == "10101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "01001001001001001001001001001001001001001001001001001001001001001001001001001001",k = 4) == "1001001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01001001001001001001001001001001001001001001001001001001001001001001001001001001",k = 4) == "1001001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001",k = 12) == "1001001001001001001001001001001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001",k = 12) == "1001001001001001001001001001001001": {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000",k = 1) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000",k = 1) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 9) == "10101010101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 9) == "10101010101010101": {e}')
    
    total += 1
    try:
        result = candidate(s = "010101010101010101010101010101",k = 5) == "101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101010101010101010101010101",k = 5) == "101010101": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "1100110011001100110011001100",k = 6) == "1100110011"
    assert candidate(s = "100011001",k = 3) == "11001"
    assert candidate(s = "1010101010",k = 5) == "101010101"
    assert candidate(s = "1111111111",k = 5) == "11111"
    assert candidate(s = "100100100",k = 3) == "1001001"
    assert candidate(s = "000",k = 1) == ""
    assert candidate(s = "111010101",k = 2) == "11"
    assert candidate(s = "0000000000",k = 1) == ""
    assert candidate(s = "111000",k = 2) == "11"
    assert candidate(s = "1001001001",k = 4) == "1001001001"
    assert candidate(s = "1111",k = 2) == "11"
    assert candidate(s = "0101010101010101010101010101",k = 5) == "101010101"
    assert candidate(s = "11001100110011001100",k = 5) == "100110011"
    assert candidate(s = "010101",k = 3) == "10101"
    assert candidate(s = "1010101",k = 4) == "1010101"
    assert candidate(s = "1011",k = 2) == "11"
    assert candidate(s = "10101010101010101010",k = 10) == "1010101010101010101"
    assert candidate(s = "1010101010101010101010101010101010101010101010101010",k = 12) == "10101010101010101010101"
    assert candidate(s = "101010101010101010101010101010101010101010101010",k = 10) == "1010101010101010101"
    assert candidate(s = "000000000000000000000000000000",k = 1) == ""
    assert candidate(s = "110110110110110110110110110110",k = 5) == "1011011"
    assert candidate(s = "00000000000000000000000000000000",k = 5) == ""
    assert candidate(s = "1001001001001001001001001001001",k = 5) == "1001001001001"
    assert candidate(s = "1010101010101010101010101010101010101010",k = 10) == "1010101010101010101"
    assert candidate(s = "00000000000000000000000000000000",k = 1) == ""
    assert candidate(s = "1111000011110000111100001111000011110000111100001111000011110000",k = 8) == "111100001111"
    assert candidate(s = "1111111111111111111111111111111111111111111111111111111111111111111111111111",k = 15) == "111111111111111"
    assert candidate(s = "01001001001001001001001001001001001001001001001001001001001001001001",k = 8) == "1001001001001001001001"
    assert candidate(s = "0101010101010101010101010101010101010101010101010101010101010101",k = 12) == "10101010101010101010101"
    assert candidate(s = "111000111000111000",k = 3) == "111"
    assert candidate(s = "1100011000110001100011000110001100011000",k = 6) == "110001100011"
    assert candidate(s = "101010101010101010101010101010101010101010101010",k = 9) == "10101010101010101"
    assert candidate(s = "1111111111111111111111111111111111111111111111111111",k = 50) == "11111111111111111111111111111111111111111111111111"
    assert candidate(s = "010101010101010101010101010101010101010101010101",k = 5) == "101010101"
    assert candidate(s = "10101010101010101010101010101010",k = 10) == "1010101010101010101"
    assert candidate(s = "111111111111111111111111111111",k = 10) == "1111111111"
    assert candidate(s = "111000111000111000111000111000111000111000111000",k = 9) == "111000111000111"
    assert candidate(s = "010101010101010101010101010101010101010101010101",k = 8) == "101010101010101"
    assert candidate(s = "01010101010101010101010101010101010101010101",k = 10) == "1010101010101010101"
    assert candidate(s = "1001100110011001100110011001100110011001100110011001100110011001100110011001",k = 6) == "1100110011"
    assert candidate(s = "0101010101010101010101010101",k = 3) == "10101"
    assert candidate(s = "111000111000111000111000111000111000111",k = 6) == "111000111"
    assert candidate(s = "01010101010101010101010101010101010101010101010101",k = 10) == "1010101010101010101"
    assert candidate(s = "111000111000111000111000111000111000111000",k = 11) == "11000111000111000111"
    assert candidate(s = "1101001101001101001101001101",k = 4) == "1001101"
    assert candidate(s = "111011101110111011101110",k = 7) == "101110111"
    assert candidate(s = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001",k = 3) == ""
    assert candidate(s = "0000000000000000000000000000000000000000000000000000000000000000000000000000",k = 1) == ""
    assert candidate(s = "1100110011001100110011001100110011001100110011001100110011001100",k = 15) == "10011001100110011001100110011"
    assert candidate(s = "00000000000000000000",k = 1) == ""
    assert candidate(s = "000000000000000000000000000000000000000000000001",k = 1) == "1"
    assert candidate(s = "0001000100010001000100010001000100010001000100010001",k = 3) == "100010001"
    assert candidate(s = "1010101010101010101010101010101010101010101010101010",k = 7) == "1010101010101"
    assert candidate(s = "000000000000000000000000000000000000000000000000",k = 3) == ""
    assert candidate(s = "1110011100011100111000011100000111000000",k = 6) == "11100111"
    assert candidate(s = "1110000001110000011100000111000001110000011100000111",k = 6) == "11100000111"
    assert candidate(s = "110011001100110011001100110011001100110011001100110011001100",k = 11) == "100110011001100110011"
    assert candidate(s = "0000000000000000000000000000000000000000",k = 1) == ""
    assert candidate(s = "110011001100110011001100110011001100",k = 6) == "1100110011"
    assert candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010",k = 13) == "1010101010101010101010101"
    assert candidate(s = "111000111000111000111000111000111000111000",k = 6) == "111000111"
    assert candidate(s = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010",k = 15) == "10101010101010101010101010101"
    assert candidate(s = "0101010101010101010101010101010101010101",k = 15) == "10101010101010101010101010101"
    assert candidate(s = "10001000100010001000100010001000100010001000",k = 5) == "10001000100010001"
    assert candidate(s = "10101010101010101010101010101010101010101010101010101010101010101",k = 15) == "10101010101010101010101010101"
    assert candidate(s = "110001100011000110001100011000110001100011000",k = 5) == "10001100011"
    assert candidate(s = "11000110001100011000110001100011000",k = 6) == "110001100011"
    assert candidate(s = "010101010101010101010101010101010101010101",k = 10) == "1010101010101010101"
    assert candidate(s = "01010101010101010101010101010101",k = 5) == "101010101"
    assert candidate(s = "101010101010101010101010101010101010",k = 10) == "1010101010101010101"
    assert candidate(s = "0101010101010101010101010101010101010101",k = 5) == "101010101"
    assert candidate(s = "111000111000111000111000111",k = 6) == "111000111"
    assert candidate(s = "111110000000000000000000000000000000000000000000",k = 5) == "11111"
    assert candidate(s = "1101101101101101101101101101101101101101",k = 7) == "1011011011"
    assert candidate(s = "11100111001110011100111001110011100111001110011100",k = 8) == "110011100111"
    assert candidate(s = "10000001000000100000010000001",k = 3) == "100000010000001"
    assert candidate(s = "11110000111100001111000011110000",k = 4) == "1111"
    assert candidate(s = "0010010010010010010010010010010010010010",k = 2) == "1001"
    assert candidate(s = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010",k = 20) == "101010101010101010101010101010101010101"
    assert candidate(s = "101010101010101010101010101010101010101010101010",k = 8) == "101010101010101"
    assert candidate(s = "111110000011111000001111100000111110000011111",k = 8) == "1110000011111"
    assert candidate(s = "1010101010101010101010101010101010101010",k = 15) == "10101010101010101010101010101"
    assert candidate(s = "111000111000111000111000",k = 9) == "111000111000111"
    assert candidate(s = "1000001000001000001000001000001000001000001000001000001000001",k = 2) == "1000001"
    assert candidate(s = "1000000000000000000000000000000000000001",k = 1) == "1"
    assert candidate(s = "1110000111000011100001110000",k = 4) == "10000111"
    assert candidate(s = "10101010101010101010101010101010101010101010",k = 7) == "1010101010101"
    assert candidate(s = "000100010001000100010001",k = 2) == "10001"
    assert candidate(s = "1000100010001000100010001",k = 3) == "100010001"
    assert candidate(s = "1001001001001001001001001001001001001001001001",k = 5) == "1001001001001"
    assert candidate(s = "0000000000000000000000000000000000000000000000000001",k = 1) == "1"
    assert candidate(s = "11111000001111100000111110000011111",k = 5) == "11111"
    assert candidate(s = "0110110110110110110110110110110110110110110110",k = 4) == "11011"
    assert candidate(s = "00000000000000000000000000000000000000000000000000000000",k = 1) == ""
    assert candidate(s = "11000001110000011100000111000001110000011100000111",k = 7) == "10000011100000111"
    assert candidate(s = "001001001001001001001001001001001001001",k = 3) == "1001001"
    assert candidate(s = "11111111111111111111111111111111",k = 15) == "111111111111111"
    assert candidate(s = "1010101010101010101010101010101010101010101010",k = 8) == "101010101010101"
    assert candidate(s = "0000000000000000000000000000000000000000000000000000",k = 1) == ""
    assert candidate(s = "111111111111111111111111111111111111111111111111",k = 9) == "111111111"
    assert candidate(s = "010101010101010101010101010101010101",k = 10) == "1010101010101010101"
    assert candidate(s = "1100110011001100110011001100110011001100110011001100110011001100",k = 10) == "110011001100110011"
    assert candidate(s = "100000100000100000100000100000100000100000100000",k = 3) == "1000001000001"
    assert candidate(s = "100110011001100110011001100110011001100110011001100110011001100110011001",k = 9) == "10011001100110011"
    assert candidate(s = "111000111000111000111000111000111000111000111000111000111000111000111000111000111000",k = 7) == "1000111000111"
    assert candidate(s = "10101010101010101010",k = 7) == "1010101010101"
    assert candidate(s = "1111000011110000111100001111",k = 8) == "111100001111"
    assert candidate(s = "1010101010101010101010101010101010101010",k = 12) == "10101010101010101010101"
    assert candidate(s = "01010101010101010101",k = 3) == "10101"
    assert candidate(s = "001001001001001001001001001001001001001001001001",k = 5) == "1001001001001"
    assert candidate(s = "1001001001001001001001001001001001001001001001001001001001",k = 12) == "1001001001001001001001001001001001"
    assert candidate(s = "000000000011111111111111111111111111111111111111111111111111111111111111",k = 20) == "11111111111111111111"
    assert candidate(s = "110110110110110110110110110110110110110",k = 7) == "1011011011"
    assert candidate(s = "10101010101010101010",k = 6) == "10101010101"
    assert candidate(s = "01001001001001001001001001001001001001001001001001001001001001001001001001001001",k = 4) == "1001001001"
    assert candidate(s = "1001001001001001001001001001001001001001",k = 12) == "1001001001001001001001001001001001"
    assert candidate(s = "00000000000000000000000000000000000000000000",k = 1) == ""
    assert candidate(s = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",k = 9) == "10101010101010101"
    assert candidate(s = "010101010101010101010101010101",k = 5) == "101010101"


