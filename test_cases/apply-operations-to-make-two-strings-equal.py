def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "101010",s2 = "010101",x = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010",s2 = "010101",x = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1111",s2 = "1111",x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1111",s2 = "1111",x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "101010",s2 = "010101",x = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010",s2 = "010101",x = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1111",s2 = "1111",x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1111",s2 = "1111",x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1111",s2 = "1111",x = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1111",s2 = "1111",x = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "001100",s2 = "110011",x = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "001100",s2 = "110011",x = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "101010",s2 = "010101",x = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010",s2 = "010101",x = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1100011000",s2 = "0101001010",x = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1100011000",s2 = "0101001010",x = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0000",s2 = "1111",x = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0000",s2 = "1111",x = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0000",s2 = "1111",x = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0000",s2 = "1111",x = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "10110",s2 = "00011",x = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "10110",s2 = "00011",x = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110100001111001011010101010101010101010101",s2 = "001011110001010100101010101010101010101010",x = 8) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110100001111001011010101010101010101010101",s2 = "001011110001010100101010101010101010101010",x = 8) == 22: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "01010101010101",s2 = "10101010101010",x = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "01010101010101",s2 = "10101010101010",x = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "00000000000000",s2 = "11111111111111",x = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "00000000000000",s2 = "11111111111111",x = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1010101010101010101010",s2 = "1101101101101101101101",x = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1010101010101010101010",s2 = "1101101101101101101101",x = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "000000000000",s2 = "111111111111",x = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "000000000000",s2 = "111111111111",x = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "000000000000000000000000000000000000",s2 = "111111111111111111111111111111111111",x = 20) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "000000000000000000000000000000000000",s2 = "111111111111111111111111111111111111",x = 20) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110011001100",s2 = "001100110011",x = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110011001100",s2 = "001100110011",x = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000111000111",s2 = "000111000111000",x = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000111000111",s2 = "000111000111000",x = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "101010101010",s2 = "010101010101",x = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010101010",s2 = "010101010101",x = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "11001100110011",s2 = "00110011001100",x = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "11001100110011",s2 = "00110011001100",x = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0000000000000000000000",s2 = "1111111111111111111111",x = 20) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0000000000000000000000",s2 = "1111111111111111111111",x = 20) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110011001100",s2 = "001100110011",x = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110011001100",s2 = "001100110011",x = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1111000011",s2 = "0000111100",x = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1111000011",s2 = "0000111100",x = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1001001001001001",s2 = "0110110110110110",x = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1001001001001001",s2 = "0110110110110110",x = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000111000",s2 = "000111000111",x = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000111000",s2 = "000111000111",x = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "000000000000",s2 = "111111111111",x = 100) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "000000000000",s2 = "111111111111",x = 100) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1111000011110000",s2 = "0000111100001111",x = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1111000011110000",s2 = "0000111100001111",x = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "01010101010",s2 = "10101010101",x = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "01010101010",s2 = "10101010101",x = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000000111",s2 = "000111111000",x = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000000111",s2 = "000111111000",x = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "101010101010",s2 = "010101010101",x = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010101010",s2 = "010101010101",x = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "100110011001",s2 = "011001100110",x = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "100110011001",s2 = "011001100110",x = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111100001111",s2 = "000011110000",x = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111100001111",s2 = "000011110000",x = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "10101010101010101010101010101010",s2 = "01010101010101010101010101010101",x = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "10101010101010101010101010101010",s2 = "01010101010101010101010101010101",x = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1100101010101010",s2 = "0110010101010101",x = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1100101010101010",s2 = "0110010101010101",x = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "10010010010010010010010010010010",s2 = "01101101101101101101101101101101",x = 3) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "10010010010010010010010010010010",s2 = "01101101101101101101101101101101",x = 3) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "100010001000",s2 = "011101110111",x = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "100010001000",s2 = "011101110111",x = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000111000",s2 = "000111000111",x = 8) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000111000",s2 = "000111000111",x = 8) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0011001100",s2 = "1100110011",x = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0011001100",s2 = "1100110011",x = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "010101010101010101010101",s2 = "101010101010101010101010",x = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "010101010101010101010101",s2 = "101010101010101010101010",x = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1010101010101010101010",s2 = "0101010101010101010101",x = 4) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1010101010101010101010",s2 = "0101010101010101010101",x = 4) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0110011001",s2 = "1001100110",x = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0110011001",s2 = "1001100110",x = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "101010101010",s2 = "101010101010",x = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010101010",s2 = "101010101010",x = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "10101010101010",s2 = "01010101010101",x = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "10101010101010",s2 = "01010101010101",x = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0000000000",s2 = "1111111111",x = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0000000000",s2 = "1111111111",x = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "101010101010",s2 = "101010101010",x = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010101010",s2 = "101010101010",x = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111111111111",s2 = "000000000000",x = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111111111111",s2 = "000000000000",x = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "101010101010",s2 = "010101010101",x = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010101010",s2 = "010101010101",x = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110101010101",s2 = "001010101010",x = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110101010101",s2 = "001010101010",x = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "101010101010",s2 = "110011001100",x = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010101010",s2 = "110011001100",x = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000001110",s2 = "111111111111",x = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000001110",s2 = "111111111111",x = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "11110000111100001111",s2 = "00001111000011110000",x = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "11110000111100001111",s2 = "00001111000011110000",x = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1001100110",s2 = "1100110011",x = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1001100110",s2 = "1100110011",x = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "010101010101",s2 = "101010101010",x = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "010101010101",s2 = "101010101010",x = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "10101010101010",s2 = "01010101010101",x = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "10101010101010",s2 = "01010101010101",x = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0000000000000000000000",s2 = "0000000000000000000000",x = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0000000000000000000000",s2 = "0000000000000000000000",x = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "11110000",s2 = "00001111",x = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "11110000",s2 = "00001111",x = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "101010101010",s2 = "101010101010",x = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "101010101010",s2 = "101010101010",x = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0000000000",s2 = "1111111111",x = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0000000000",s2 = "1111111111",x = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1100110011",s2 = "0011001100",x = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1100110011",s2 = "0011001100",x = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1111000011110000",s2 = "0000111100001111",x = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1111000011110000",s2 = "0000111100001111",x = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111011101110",s2 = "000100010001",x = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111011101110",s2 = "000100010001",x = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "11111111111111",s2 = "11111111111111",x = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "11111111111111",s2 = "11111111111111",x = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "000000000000000000000000000000",s2 = "111111111111111111111111111111",x = 50) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "000000000000000000000000000000",s2 = "111111111111111111111111111111",x = 50) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110110110110",s2 = "111001100111",x = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110110110110",s2 = "111001100111",x = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000111",s2 = "111111111",x = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000111",s2 = "111111111",x = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0101010101",s2 = "1100110011",x = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0101010101",s2 = "1100110011",x = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0101010101010101010101010101010101010101",s2 = "1010101010101010101010101010101010101010",x = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0101010101010101010101010101010101010101",s2 = "1010101010101010101010101010101010101010",x = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "01010101010101010101",s2 = "10101010101010101010",x = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "01010101010101010101",s2 = "10101010101010101010",x = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1001100110",s2 = "0110011001",x = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1001100110",s2 = "0110011001",x = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1111111111",s2 = "0000000000",x = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1111111111",s2 = "0000000000",x = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1100110011",s2 = "0011001100",x = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1100110011",s2 = "0011001100",x = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110110110110110110",s2 = "001001001001001001",x = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110110110110110110",s2 = "001001001001001001",x = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1111111111111111111111",s2 = "1111111111111111111111",x = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1111111111111111111111",s2 = "1111111111111111111111",x = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000111000",s2 = "000111000111",x = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000111000",s2 = "000111000111",x = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "01010101010101",s2 = "10101010101010",x = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "01010101010101",s2 = "10101010101010",x = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1001001001",s2 = "0110110110",x = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1001001001",s2 = "0110110110",x = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "0101010101",s2 = "1010101010",x = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "0101010101",s2 = "1010101010",x = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1101101101",s2 = "1010101010",x = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1101101101",s2 = "1010101010",x = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "010101010101",s2 = "101010101010",x = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "010101010101",s2 = "101010101010",x = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000111000",s2 = "000111000111",x = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000111000",s2 = "000111000111",x = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1100110011001100",s2 = "0011001100110011",x = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1100110011001100",s2 = "0011001100110011",x = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1101010101",s2 = "0110101010",x = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1101010101",s2 = "0110101010",x = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110000110000",s2 = "001111001111",x = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110000110000",s2 = "001111001111",x = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1100110011",s2 = "0011001100",x = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1100110011",s2 = "0011001100",x = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111111111111",s2 = "000000000000",x = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111111111111",s2 = "000000000000",x = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "100010001000",s2 = "011101110111",x = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "100010001000",s2 = "011101110111",x = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "10101010101010",s2 = "01010101010101",x = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "10101010101010",s2 = "01010101010101",x = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "10101010101010",s2 = "11001100110011",x = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "10101010101010",s2 = "11001100110011",x = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "11010101010101010101",s2 = "00101010101010101010",x = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "11010101010101010101",s2 = "00101010101010101010",x = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110011001100110011001100",s2 = "001100110011001100110011",x = 9) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110011001100110011001100",s2 = "001100110011001100110011",x = 9) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000111000",s2 = "000111000111",x = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000111000",s2 = "000111000111",x = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "10101010101010",s2 = "01010101010101",x = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "10101010101010",s2 = "01010101010101",x = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1001001001",s2 = "1110111011",x = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1001001001",s2 = "1110111011",x = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111111000000",s2 = "000000111111",x = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111111000000",s2 = "000000111111",x = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110011001100110011001100110011001100",s2 = "110011001100110011001100110011001100",x = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110011001100110011001100110011001100",s2 = "110011001100110011001100110011001100",x = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110001100011",s2 = "001110011100",x = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110001100011",s2 = "001110011100",x = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "100100100100",s2 = "011001100110",x = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "100100100100",s2 = "011001100110",x = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110011001100",s2 = "001100110011",x = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110011001100",s2 = "001100110011",x = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1001010010",s2 = "0110101101",x = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1001010010",s2 = "0110101101",x = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111111111111",s2 = "000000000000",x = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111111111111",s2 = "000000000000",x = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000111000111",s2 = "000111000111000",x = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000111000111",s2 = "000111000111000",x = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110111011101",s2 = "001000100010",x = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110111011101",s2 = "001000100010",x = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "11110000",s2 = "00001111",x = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "11110000",s2 = "00001111",x = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "011001100110",s2 = "100110011001",x = 9) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "011001100110",s2 = "100110011001",x = 9) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "11111111111111111111111111111111",s2 = "11111111111111111111111111111111",x = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "11111111111111111111111111111111",s2 = "11111111111111111111111111111111",x = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "10101010101010101010101010101010",s2 = "01010101010101010101010101010101",x = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "10101010101010101010101010101010",s2 = "01010101010101010101010101010101",x = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1100101100",s2 = "0011010011",x = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1100101100",s2 = "0011010011",x = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "000000000000",s2 = "111111111111",x = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "000000000000",s2 = "111111111111",x = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "100100100100",s2 = "100100100100",x = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "100100100100",s2 = "100100100100",x = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "111000111",s2 = "111111111",x = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "111000111",s2 = "111111111",x = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "1001010101",s2 = "0110101010",x = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "1001010101",s2 = "0110101010",x = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "110110110110",s2 = "001001001001",x = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "110110110110",s2 = "001001001001",x = 2) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "101010",s2 = "010101",x = 1) == 3
    assert candidate(s1 = "1111",s2 = "1111",x = 3) == 0
    assert candidate(s1 = "101010",s2 = "010101",x = 5) == 3
    assert candidate(s1 = "1111",s2 = "1111",x = 5) == 0
    assert candidate(s1 = "1111",s2 = "1111",x = 10) == 0
    assert candidate(s1 = "001100",s2 = "110011",x = 3) == 3
    assert candidate(s1 = "101010",s2 = "010101",x = 3) == 3
    assert candidate(s1 = "1100011000",s2 = "0101001010",x = 2) == 4
    assert candidate(s1 = "0000",s2 = "1111",x = 1) == 2
    assert candidate(s1 = "0000",s2 = "1111",x = 5) == 2
    assert candidate(s1 = "10110",s2 = "00011",x = 4) == -1
    assert candidate(s1 = "110100001111001011010101010101010101010101",s2 = "001011110001010100101010101010101010101010",x = 8) == 22
    assert candidate(s1 = "01010101010101",s2 = "10101010101010",x = 1) == 7
    assert candidate(s1 = "00000000000000",s2 = "11111111111111",x = 1) == 7
    assert candidate(s1 = "1010101010101010101010",s2 = "1101101101101101101101",x = 7) == 12
    assert candidate(s1 = "000000000000",s2 = "111111111111",x = 10) == 6
    assert candidate(s1 = "000000000000000000000000000000000000",s2 = "111111111111111111111111111111111111",x = 20) == 18
    assert candidate(s1 = "110011001100",s2 = "001100110011",x = 7) == 6
    assert candidate(s1 = "111000111000111",s2 = "000111000111000",x = 15) == -1
    assert candidate(s1 = "101010101010",s2 = "010101010101",x = 7) == 6
    assert candidate(s1 = "11001100110011",s2 = "00110011001100",x = 10) == 7
    assert candidate(s1 = "0000000000000000000000",s2 = "1111111111111111111111",x = 20) == 11
    assert candidate(s1 = "110011001100",s2 = "001100110011",x = 6) == 6
    assert candidate(s1 = "1111000011",s2 = "0000111100",x = 4) == 5
    assert candidate(s1 = "1001001001001001",s2 = "0110110110110110",x = 15) == 8
    assert candidate(s1 = "111000111000",s2 = "000111000111",x = 6) == 6
    assert candidate(s1 = "000000000000",s2 = "111111111111",x = 100) == 6
    assert candidate(s1 = "1111000011110000",s2 = "0000111100001111",x = 3) == 8
    assert candidate(s1 = "01010101010",s2 = "10101010101",x = 10) == -1
    assert candidate(s1 = "111000000111",s2 = "000111111000",x = 3) == 6
    assert candidate(s1 = "101010101010",s2 = "010101010101",x = 4) == 6
    assert candidate(s1 = "100110011001",s2 = "011001100110",x = 7) == 6
    assert candidate(s1 = "111100001111",s2 = "000011110000",x = 3) == 6
    assert candidate(s1 = "10101010101010101010101010101010",s2 = "01010101010101010101010101010101",x = 5) == 16
    assert candidate(s1 = "1100101010101010",s2 = "0110010101010101",x = 5) == 8
    assert candidate(s1 = "10010010010010010010010010010010",s2 = "01101101101101101101101101101101",x = 3) == 16
    assert candidate(s1 = "100010001000",s2 = "011101110111",x = 20) == 6
    assert candidate(s1 = "111000111000",s2 = "000111000111",x = 8) == 6
    assert candidate(s1 = "0011001100",s2 = "1100110011",x = 2) == 5
    assert candidate(s1 = "010101010101010101010101",s2 = "101010101010101010101010",x = 1) == 12
    assert candidate(s1 = "1010101010101010101010",s2 = "0101010101010101010101",x = 4) == 11
    assert candidate(s1 = "0110011001",s2 = "1001100110",x = 7) == 5
    assert candidate(s1 = "101010101010",s2 = "101010101010",x = 7) == 0
    assert candidate(s1 = "10101010101010",s2 = "01010101010101",x = 5) == 7
    assert candidate(s1 = "0000000000",s2 = "1111111111",x = 10) == 5
    assert candidate(s1 = "101010101010",s2 = "101010101010",x = 10) == 0
    assert candidate(s1 = "111111111111",s2 = "000000000000",x = 1) == 6
    assert candidate(s1 = "101010101010",s2 = "010101010101",x = 1) == 6
    assert candidate(s1 = "110101010101",s2 = "001010101010",x = 10) == 6
    assert candidate(s1 = "101010101010",s2 = "110011001100",x = 8) == 3
    assert candidate(s1 = "111000001110",s2 = "111111111111",x = 6) == 6
    assert candidate(s1 = "11110000111100001111",s2 = "00001111000011110000",x = 10) == 10
    assert candidate(s1 = "1001100110",s2 = "1100110011",x = 2) == -1
    assert candidate(s1 = "010101010101",s2 = "101010101010",x = 10) == 6
    assert candidate(s1 = "10101010101010",s2 = "01010101010101",x = 4) == 7
    assert candidate(s1 = "0000000000000000000000",s2 = "0000000000000000000000",x = 8) == 0
    assert candidate(s1 = "11110000",s2 = "00001111",x = 3) == 4
    assert candidate(s1 = "101010101010",s2 = "101010101010",x = 1) == 0
    assert candidate(s1 = "0000000000",s2 = "1111111111",x = 15) == 5
    assert candidate(s1 = "1100110011",s2 = "0011001100",x = 10) == 5
    assert candidate(s1 = "1111000011110000",s2 = "0000111100001111",x = 8) == 8
    assert candidate(s1 = "111011101110",s2 = "000100010001",x = 4) == 6
    assert candidate(s1 = "11111111111111",s2 = "11111111111111",x = 100) == 0
    assert candidate(s1 = "000000000000000000000000000000",s2 = "111111111111111111111111111111",x = 50) == 15
    assert candidate(s1 = "110110110110",s2 = "111001100111",x = 2) == 4
    assert candidate(s1 = "111000111",s2 = "111111111",x = 1) == -1
    assert candidate(s1 = "0101010101",s2 = "1100110011",x = 2) == -1
    assert candidate(s1 = "0101010101010101010101010101010101010101",s2 = "1010101010101010101010101010101010101010",x = 4) == 20
    assert candidate(s1 = "01010101010101010101",s2 = "10101010101010101010",x = 3) == 10
    assert candidate(s1 = "1001100110",s2 = "0110011001",x = 3) == 5
    assert candidate(s1 = "1111111111",s2 = "0000000000",x = 3) == 5
    assert candidate(s1 = "1100110011",s2 = "0011001100",x = 5) == 5
    assert candidate(s1 = "110110110110110110",s2 = "001001001001001001",x = 6) == 9
    assert candidate(s1 = "1111111111111111111111",s2 = "1111111111111111111111",x = 2) == 0
    assert candidate(s1 = "111000111000",s2 = "000111000111",x = 3) == 6
    assert candidate(s1 = "01010101010101",s2 = "10101010101010",x = 8) == 7
    assert candidate(s1 = "1001001001",s2 = "0110110110",x = 6) == 5
    assert candidate(s1 = "0101010101",s2 = "1010101010",x = 10) == 5
    assert candidate(s1 = "1101101101",s2 = "1010101010",x = 5) == 6
    assert candidate(s1 = "010101010101",s2 = "101010101010",x = 2) == 6
    assert candidate(s1 = "111000111000",s2 = "000111000111",x = 7) == 6
    assert candidate(s1 = "1100110011001100",s2 = "0011001100110011",x = 9) == 8
    assert candidate(s1 = "1101010101",s2 = "0110101010",x = 5) == -1
    assert candidate(s1 = "110000110000",s2 = "001111001111",x = 4) == 6
    assert candidate(s1 = "1100110011",s2 = "0011001100",x = 8) == 5
    assert candidate(s1 = "111111111111",s2 = "000000000000",x = 2) == 6
    assert candidate(s1 = "100010001000",s2 = "011101110111",x = 4) == 6
    assert candidate(s1 = "10101010101010",s2 = "01010101010101",x = 8) == 7
    assert candidate(s1 = "10101010101010",s2 = "11001100110011",x = 6) == -1
    assert candidate(s1 = "11010101010101010101",s2 = "00101010101010101010",x = 2) == 10
    assert candidate(s1 = "110011001100110011001100",s2 = "001100110011001100110011",x = 9) == 12
    assert candidate(s1 = "111000111000",s2 = "000111000111",x = 10) == 6
    assert candidate(s1 = "10101010101010",s2 = "01010101010101",x = 15) == 7
    assert candidate(s1 = "1001001001",s2 = "1110111011",x = 5) == 5
    assert candidate(s1 = "111111000000",s2 = "000000111111",x = 2) == 6
    assert candidate(s1 = "110011001100110011001100110011001100",s2 = "110011001100110011001100110011001100",x = 15) == 0
    assert candidate(s1 = "110001100011",s2 = "001110011100",x = 2) == 6
    assert candidate(s1 = "100100100100",s2 = "011001100110",x = 1) == 3
    assert candidate(s1 = "110011001100",s2 = "001100110011",x = 5) == 6
    assert candidate(s1 = "1001010010",s2 = "0110101101",x = 5) == 5
    assert candidate(s1 = "111111111111",s2 = "000000000000",x = 3) == 6
    assert candidate(s1 = "111000111000111",s2 = "000111000111000",x = 1) == -1
    assert candidate(s1 = "110111011101",s2 = "001000100010",x = 6) == 6
    assert candidate(s1 = "11110000",s2 = "00001111",x = 1) == 4
    assert candidate(s1 = "011001100110",s2 = "100110011001",x = 9) == 6
    assert candidate(s1 = "11111111111111111111111111111111",s2 = "11111111111111111111111111111111",x = 7) == 0
    assert candidate(s1 = "10101010101010101010101010101010",s2 = "01010101010101010101010101010101",x = 10) == 16
    assert candidate(s1 = "1100101100",s2 = "0011010011",x = 5) == 5
    assert candidate(s1 = "000000000000",s2 = "111111111111",x = 1) == 6
    assert candidate(s1 = "100100100100",s2 = "100100100100",x = 7) == 0
    assert candidate(s1 = "111000111",s2 = "111111111",x = 5) == -1
    assert candidate(s1 = "1001010101",s2 = "0110101010",x = 5) == 5
    assert candidate(s1 = "110110110110",s2 = "001001001001",x = 2) == 6


