def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(strs = ['0', '0', '1', '1'],m = 2,n = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['0', '0', '1', '1'],m = 2,n = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111', '000', '101010'],m = 3,n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111', '000', '101010'],m = 3,n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['10', '0', '1'],m = 1,n = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['10', '0', '1'],m = 1,n = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111', '000', '1010', '0101'],m = 3,n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111', '000', '1010', '0101'],m = 3,n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110', '100', '001'],m = 2,n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110', '100', '001'],m = 2,n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110', '100', '010'],m = 2,n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110', '100', '010'],m = 2,n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1', '10', '100', '1000'],m = 4,n = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1', '10', '100', '1000'],m = 4,n = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111111', '000000'],m = 3,n = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111111', '000000'],m = 3,n = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['0', '0', '0', '0'],m = 0,n = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['0', '0', '0', '0'],m = 0,n = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111', '1010', '0101', '0000'],m = 2,n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111', '1010', '0101', '0000'],m = 2,n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111111', '000000', '101010', '010101'],m = 3,n = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111111', '000000', '101010', '010101'],m = 3,n = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11111010110010001111', '01001100001100111100', '00000110011101011010', '11010011000101000011', '10011001110100010100', '00110001011100100010', '01000101110110011101'],m = 34,n = 21) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11111010110010001111', '01001100001100111100', '00000110011101011010', '11010011000101000011', '10011001110100010100', '00110001011100100010', '01000101110110011101'],m = 34,n = 21) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['0', '0', '0', '0'],m = 0,n = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['0', '0', '0', '0'],m = 0,n = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1100', '100001111000', '000000000000001010', '11111111111111111111', '100001111000', '100001111000'],m = 31,n = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1100', '100001111000', '000000000000001010', '11111111111111111111', '100001111000', '100001111000'],m = 31,n = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['00', '00'],m = 1,n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['00', '00'],m = 1,n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1101', '1101', '0010', '0000'],m = 4,n = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1101', '1101', '0010', '0000'],m = 4,n = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['10', '0001', '111001', '1', '0'],m = 5,n = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['10', '0001', '111001', '1', '0'],m = 5,n = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['101010', '010101', '110011', '001100', '111000', '000111', '1111000000', '0000111111'],m = 10,n = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['101010', '010101', '110011', '001100', '111000', '000111', '1111000000', '0000111111'],m = 10,n = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11111', '11100', '11010', '10110', '01110', '10011', '01011', '00111', '11110', '11001', '10101', '01101'],m = 9,n = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11111', '11100', '11010', '10110', '01110', '10011', '01011', '00111', '11110', '11001', '10101', '01101'],m = 9,n = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111000', '000111', '111100', '000011', '111111', '000000', '101010'],m = 5,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111000', '000111', '111100', '000011', '111111', '000000', '101010'],m = 5,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['10101010', '01010101', '11110000', '00001111', '11001100', '00110011'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['10101010', '01010101', '11110000', '00001111', '11001100', '00110011'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111110', '1010101', '0101010', '0000000', '1111111', '1000001', '0011110'],m = 6,n = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111110', '1010101', '0101010', '0000000', '1111111', '1000001', '0011110'],m = 6,n = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1010101010', '0101010101', '1111111111', '0000000000'],m = 5,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1010101010', '0101010101', '1111111111', '0000000000'],m = 5,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],m = 10,n = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],m = 10,n = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['101', '0011', '1000', '1100', '0100', '0000'],m = 5,n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['101', '0011', '1000', '1100', '0100', '0000'],m = 5,n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1010101010', '0101010101', '1111100000', '0000011111', '1100110011'],m = 10,n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1010101010', '0101010101', '1111100000', '0000011111', '1100110011'],m = 10,n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1010101010', '0101010101', '1110000000', '0001111111', '1100110011', '0011001100', '1011000101', '0100111010', '1111000011', '0000111100'],m = 12,n = 12) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1010101010', '0101010101', '1110000000', '0001111111', '1100110011', '0011001100', '1011000101', '0100111010', '1111000011', '0000111100'],m = 12,n = 12) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110000', '001100', '101010', '010101', '111100', '000011', '101001'],m = 6,n = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110000', '001100', '101010', '010101', '111100', '000011', '101001'],m = 6,n = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],m = 10,n = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],m = 10,n = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111111111', '000000000', '101010101', '010101010', '111000011', '000111100'],m = 7,n = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111111111', '000000000', '101010101', '010101010', '111000011', '000111100'],m = 7,n = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110', '100', '001', '100', '001', '001', '010', '101', '100', '001', '001', '100', '001', '101', '010', '101', '101', '010', '100', '001'],m = 6,n = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110', '100', '001', '100', '001', '001', '010', '101', '100', '001', '001', '100', '001', '101', '010', '101', '101', '010', '100', '001'],m = 6,n = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1110000', '0001111', '1100110', '0011001', '1011000', '0100111', '1000000', '0111111', '1101010', '0010101'],m = 10,n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1110000', '0001111', '1100110', '0011001', '1011000', '0100111', '1000000', '0111111', '1101010', '0010101'],m = 10,n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111'],m = 5,n = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111'],m = 5,n = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111110', '110101', '010110', '110001', '101000', '000011', '011101'],m = 6,n = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111110', '110101', '010110', '110001', '101000', '000011', '011101'],m = 6,n = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1100', '1010', '0011', '0101', '1111', '0000', '1000', '0111', '1101', '1011'],m = 6,n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1100', '1010', '0011', '0101', '1111', '0000', '1000', '0111', '1101', '1011'],m = 6,n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1010101', '0101010', '1110000', '0001111', '1100110', '0011001', '1011000', '0100111'],m = 6,n = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1010101', '0101010', '1110000', '0001111', '1100110', '0011001', '1011000', '0100111'],m = 6,n = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1001', '0110', '1010', '0011', '1111', '0000', '1100', '0010', '1000', '0100'],m = 5,n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1001', '0110', '1010', '0011', '1111', '0000', '1100', '0010', '1000', '0100'],m = 5,n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11111111', '10101010', '01010101', '00000000', '11000011', '00110011', '10001100'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11111111', '10101010', '01010101', '00000000', '11000011', '00110011', '10001100'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111', '110', '101', '011', '100', '010', '001', '000', '1111', '0000', '1010', '0101'],m = 7,n = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111', '110', '101', '011', '100', '010', '001', '000', '1111', '0000', '1010', '0101'],m = 7,n = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1101010', '1010101', '0011001', '0100110', '1110000', '0001111'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1101010', '1010101', '0011001', '0100110', '1110000', '0001111'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111110', '000011', '101010', '010101', '111000', '000111'],m = 6,n = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111110', '000011', '101010', '010101', '111000', '000111'],m = 6,n = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1'],m = 12,n = 12) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1'],m = 12,n = 12) == 24: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111111111', '1111111111', '1111111111', '1111111111', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000'],m = 5,n = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111111111', '1111111111', '1111111111', '1111111111', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000'],m = 5,n = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11000', '10011', '00100', '01101', '11111'],m = 5,n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11000', '10011', '00100', '01101', '11111'],m = 5,n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111111111', '0000000000', '1010101010', '0101010101', '1110000111', '0001111000'],m = 8,n = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111111111', '0000000000', '1010101010', '0101010101', '1110000111', '0001111000'],m = 8,n = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1100101', '0000000', '1010101', '1110111', '0001000'],m = 5,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1100101', '0000000', '1010101', '1110111', '0001000'],m = 5,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1010101010', '0101010101', '1111000000', '0000111111', '1100110011', '0011001100'],m = 5,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1010101010', '0101010101', '1111000000', '0000111111', '1100110011', '0011001100'],m = 5,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['101010101010101010', '010101010101010101', '111100000000000000', '000011111111111111', '110011001100110011', '001100110011001100'],m = 10,n = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['101010101010101010', '010101010101010101', '111100000000000000', '000011111111111111', '110011001100110011', '001100110011001100'],m = 10,n = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11011', '10010', '01001', '10000', '00111', '01010', '10001'],m = 4,n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11011', '10010', '01001', '10000', '00111', '01010', '10001'],m = 4,n = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['001', '010', '100', '111', '000', '110', '011'],m = 3,n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['001', '010', '100', '111', '000', '110', '011'],m = 3,n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1010101010101010101010101010', '0101010101010101010101010101', '1111111111111111111111111111', '0000000000000000000000000000'],m = 10,n = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1010101010101010101010101010', '0101010101010101010101010101', '1111111111111111111111111111', '0000000000000000000000000000'],m = 10,n = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111100', '111000', '100000', '000111', '001010', '110101'],m = 6,n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111100', '111000', '100000', '000111', '001010', '110101'],m = 6,n = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11001100', '00110011', '11110000', '00001111', '10101010', '01010101'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11001100', '00110011', '11110000', '00001111', '10101010', '01010101'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11001010', '00010101', '10101010', '00110011', '10111011', '01000100'],m = 6,n = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11001010', '00010101', '10101010', '00110011', '10111011', '01000100'],m = 6,n = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1101', '0110', '1010', '0010', '1111'],m = 4,n = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1101', '0110', '1010', '0010', '1111'],m = 4,n = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111000000', '0000111100', '1100110000', '0011001100', '1010101000', '0101010100', '1110001100', '0001110011'],m = 10,n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111000000', '0000111100', '1100110000', '0011001100', '1010101000', '0101010100', '1110001100', '0001110011'],m = 10,n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1101010', '0101110', '1010101', '0011010', '1110000', '0001111', '1111100', '0000011'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1101010', '0101110', '1010101', '0011010', '1110000', '0001111', '1111100', '0000011'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111000111', '000111000', '110011001', '001100110', '101010101'],m = 6,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111000111', '000111000', '110011001', '001100110', '101010101'],m = 6,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11000', '01110', '00010', '10011', '00001'],m = 5,n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11000', '01110', '00010', '10011', '00001'],m = 5,n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1110101', '0001100', '1100011', '0101010', '0010101', '1011010'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1110101', '0001100', '1100011', '0101010', '0010101', '1011010'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['10101', '01010', '11001', '00110', '11111', '00000'],m = 5,n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['10101', '01010', '11001', '00110', '11111', '00000'],m = 5,n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11111111', '00000000', '11000000', '00111111', '10101010', '01010101'],m = 10,n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11111111', '00000000', '11000000', '00111111', '10101010', '01010101'],m = 10,n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],m = 10,n = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],m = 10,n = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11111', '00000', '11000', '00111', '10101', '01010'],m = 4,n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11111', '00000', '11000', '00111', '10101', '01010'],m = 4,n = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111111111', '0000000000', '1111000000', '0000111111', '1110110011', '0001001100', '1011000101', '0100111010', '1111000011', '0000111100', '1010101010', '0101010101', '1101010010', '0010101101'],m = 10,n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111111111', '0000000000', '1111000000', '0000111111', '1110110011', '0001001100', '1011000101', '0100111010', '1111000011', '0000111100', '1010101010', '0101010101', '1101010010', '0010101101'],m = 10,n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11111111', '00000000', '10101010', '01010101', '11001100', '00110011', '10010010', '01101101'],m = 10,n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11111111', '00000000', '10101010', '01010101', '11001100', '00110011', '10010010', '01101101'],m = 10,n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111111111', '0000000000', '1100110011', '0011001100', '1010101010', '0101010101'],m = 8,n = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111111111', '0000000000', '1100110011', '0011001100', '1010101010', '0101010101'],m = 8,n = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110000', '000011', '110000', '000011', '110000', '000011', '110000', '000011'],m = 6,n = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110000', '000011', '110000', '000011', '110000', '000011', '110000', '000011'],m = 6,n = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['011101', '111111', '010101', '000001', '101011'],m = 5,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['011101', '111111', '010101', '000001', '101011'],m = 5,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11110000', '00001111', '10101010', '01010101', '11001100', '00110011', '10011001', '01100110'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11110000', '00001111', '10101010', '01010101', '11001100', '00110011', '10011001', '01100110'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1001001', '0110110', '1111000', '0000111', '1010101', '0101010'],m = 6,n = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1001001', '0110110', '1111000', '0000111', '1010101', '0101010'],m = 6,n = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1110101', '1000110', '0111000', '0000111', '1010100', '0010011', '1001100'],m = 7,n = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1110101', '1000110', '0111000', '0000111', '1010100', '0010011', '1001100'],m = 7,n = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11000', '10011', '01110', '00101', '10110', '11101'],m = 7,n = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11000', '10011', '01110', '00101', '10110', '11101'],m = 7,n = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111111', '000000', '111000', '000111', '101010', '010101', '110101'],m = 4,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111111', '000000', '111000', '000111', '101010', '010101', '110101'],m = 4,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1', '0', '11', '00', '10', '01', '1010', '0101'],m = 5,n = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1', '0', '11', '00', '10', '01', '1010', '0101'],m = 5,n = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['101010101', '010101010', '111000000', '000111111', '110011001', '001100110', '100100100', '011011011'],m = 8,n = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['101010101', '010101010', '111000000', '000111111', '110011001', '001100110', '100100100', '011011011'],m = 8,n = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111000', '000111', '110011', '010101', '101010'],m = 4,n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111000', '000111', '110011', '010101', '101010'],m = 4,n = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1010101', '0101010', '1100110', '0011001', '1111000', '0000111'],m = 7,n = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1010101', '0101010', '1100110', '0011001', '1111000', '0000111'],m = 7,n = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111111', '000000', '110011', '010101', '101010', '001100', '110001', '000111'],m = 4,n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111111', '000000', '110011', '010101', '101010', '001100', '110001', '000111'],m = 4,n = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1010101010', '0101010101', '1110000000', '0001111111', '1100110011', '0011001100', '1011000101', '0100111010', '1111000011', '0000111100', '1010101010', '0101010101'],m = 15,n = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1010101010', '0101010101', '1110000000', '0001111111', '1100110011', '0011001100', '1011000101', '0100111010', '1111000011', '0000111100', '1010101010', '0101010101'],m = 15,n = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11001100', '00110011', '10101010', '01010101', '11110000', '00001111', '10001000', '01110111'],m = 10,n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11001100', '00110011', '10101010', '01010101', '11110000', '00001111', '10001000', '01110111'],m = 10,n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['101010101010', '010101010101', '111100000000', '000011111111', '110011001100', '001100110011'],m = 6,n = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['101010101010', '010101010101', '111100000000', '000011111111', '110011001100', '001100110011'],m = 6,n = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['10101010101010101010', '01010101010101010101', '11100000000000000000', '00011111111111111111', '11001100110011001100', '00110011001100110011', '10110001010101010101', '01001110101010101010', '11110000110000110000', '00001111001111001111'],m = 20,n = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['10101010101010101010', '01010101010101010101', '11100000000000000000', '00011111111111111111', '11001100110011001100', '00110011001100110011', '10110001010101010101', '01001110101010101010', '11110000110000110000', '00001111001111001111'],m = 20,n = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['010101010101', '101010101010', '111111000000', '000000111111', '110011001100'],m = 12,n = 12) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['010101010101', '101010101010', '111111000000', '000000111111', '110011001100'],m = 12,n = 12) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1010101010', '0101010101', '1111000000', '0000111111', '1010101010', '0101010101', '1111000000', '0000111111'],m = 8,n = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1010101010', '0101010101', '1111000000', '0000111111', '1010101010', '0101010101', '1111000000', '0000111111'],m = 8,n = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110010', '010101', '100100', '111001', '001101', '110011'],m = 7,n = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110010', '010101', '100100', '111001', '001101', '110011'],m = 7,n = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110101', '101001', '001100', '111000', '000110'],m = 5,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110101', '101001', '001100', '111000', '000110'],m = 5,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110010', '1001', '110', '00010', '1'],m = 5,n = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110010', '1001', '110', '00010', '1'],m = 5,n = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1101101', '1010101', '0000001', '1111111', '0000000', '1010101'],m = 7,n = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1101101', '1010101', '0000001', '1111111', '0000000', '1010101'],m = 7,n = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110101', '100110', '101010', '111100', '000111', '010001'],m = 6,n = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110101', '100110', '101010', '111100', '000111', '010001'],m = 6,n = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['00000', '11111', '10101', '01010', '11000', '00111'],m = 6,n = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['00000', '11111', '10101', '01010', '11000', '00111'],m = 6,n = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['010101010101', '101010101010', '111111111111', '000000000000', '110011001100', '001100110011'],m = 10,n = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['010101010101', '101010101010', '111111111111', '000000000000', '110011001100', '001100110011'],m = 10,n = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1101010101', '1010101010', '0011001100', '1111111111', '0000000000', '1010101010', '0101010101', '1111000000'],m = 12,n = 12) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1101010101', '1010101010', '0011001100', '1111111111', '0000000000', '1010101010', '0101010101', '1111000000'],m = 12,n = 12) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1', '0', '11', '00', '101', '010', '110', '001', '111', '000'],m = 6,n = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1', '0', '11', '00', '101', '010', '110', '001', '111', '000'],m = 6,n = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111001101', '100110100', '011010101', '000111000', '111100001', '101010101', '010101010', '001001001', '110110110'],m = 9,n = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111001101', '100110100', '011010101', '000111000', '111100001', '101010101', '010101010', '001001001', '110110110'],m = 9,n = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111000', '000111', '101010', '010101', '110011', '001100', '110100', '001011', '100110', '011001'],m = 10,n = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111000', '000111', '101010', '010101', '110011', '001100', '110100', '001011', '100110', '011001'],m = 10,n = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111111111', '0000000000', '1010101010', '0101010101', '1100110011', '0011001100'],m = 8,n = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111111111', '0000000000', '1010101010', '0101010101', '1100110011', '0011001100'],m = 8,n = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111000', '000111', '101010', '010101', '110010', '001101', '100100'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111000', '000111', '101010', '010101', '110010', '001101', '100100'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['101010', '000000', '111111', '100100', '011011'],m = 5,n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['101010', '000000', '111111', '100100', '011011'],m = 5,n = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11110000', '00001111', '11101100', '00010011', '11010100', '00101011', '10111000', '01000111'],m = 8,n = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11110000', '00001111', '11101100', '00010011', '11010100', '00101011', '10111000', '01000111'],m = 8,n = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111111', '110000', '001111', '000011', '101010', '010101', '111000', '000111', '101010', '010101', '110011', '001100'],m = 12,n = 12) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111111', '110000', '001111', '000011', '101010', '010101', '111000', '000111', '101010', '010101', '110011', '001100'],m = 12,n = 12) == 4: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111111', '101010', '010101', '000000', '110011'],m = 3,n = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111111', '101010', '010101', '000000', '110011'],m = 3,n = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1111111', '0000000', '1110000', '0001111', '1010101', '0101010'],m = 5,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1111111', '0000000', '1110000', '0001111', '1010101', '0101010'],m = 5,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['111100000', '000011111', '110011000', '001100111', '101010101', '010101010', '111000111', '000111000', '100100110', '011011001'],m = 10,n = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['111100000', '000011111', '110011000', '001100111', '101010101', '010101010', '111000111', '000111000', '100100110', '011011001'],m = 10,n = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['110', '100', '001', '000', '111', '011', '110', '101', '010', '100', '000', '001', '111', '101', '011', '110', '101', '010'],m = 10,n = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['110', '100', '001', '000', '111', '011', '110', '101', '010', '100', '000', '001', '111', '101', '011', '110', '101', '010'],m = 10,n = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['10000111', '01111000', '11100011', '00011100', '10101010', '01010101', '11010101', '00101010'],m = 12,n = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['10000111', '01111000', '11100011', '00011100', '10101010', '01010101', '11010101', '00101010'],m = 12,n = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['1100000000', '0011111111', '1010101010', '0101010101', '1110001110', '0001110001', '1101011011'],m = 7,n = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['1100000000', '0011111111', '1010101010', '0101010101', '1110001110', '0001110001', '1101011011'],m = 7,n = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['11001010', '1001111', '00010', '1010', '111', '0000000'],m = 6,n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['11001010', '1001111', '00010', '1010', '111', '0000000'],m = 6,n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(strs = ['101010', '010101', '111111', '000000', '110000', '001100'],m = 4,n = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(strs = ['101010', '010101', '111111', '000000', '110000', '001100'],m = 4,n = 4) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(strs = ['0', '0', '1', '1'],m = 2,n = 2) == 4
    assert candidate(strs = ['111', '000', '101010'],m = 3,n = 3) == 2
    assert candidate(strs = ['10', '0', '1'],m = 1,n = 1) == 2
    assert candidate(strs = ['111', '000', '1010', '0101'],m = 3,n = 3) == 2
    assert candidate(strs = ['110', '100', '001'],m = 2,n = 2) == 1
    assert candidate(strs = ['110', '100', '010'],m = 2,n = 2) == 1
    assert candidate(strs = ['1', '10', '100', '1000'],m = 4,n = 4) == 3
    assert candidate(strs = ['111111', '000000'],m = 3,n = 3) == 0
    assert candidate(strs = ['0', '0', '0', '0'],m = 0,n = 4) == 0
    assert candidate(strs = ['1111', '1010', '0101', '0000'],m = 2,n = 2) == 1
    assert candidate(strs = ['111111', '000000', '101010', '010101'],m = 3,n = 3) == 1
    assert candidate(strs = ['11111010110010001111', '01001100001100111100', '00000110011101011010', '11010011000101000011', '10011001110100010100', '00110001011100100010', '01000101110110011101'],m = 34,n = 21) == 2
    assert candidate(strs = ['0', '0', '0', '0'],m = 0,n = 0) == 0
    assert candidate(strs = ['1100', '100001111000', '000000000000001010', '11111111111111111111', '100001111000', '100001111000'],m = 31,n = 12) == 3
    assert candidate(strs = ['00', '00'],m = 1,n = 1) == 0
    assert candidate(strs = ['1101', '1101', '0010', '0000'],m = 4,n = 4) == 2
    assert candidate(strs = ['10', '0001', '111001', '1', '0'],m = 5,n = 3) == 4
    assert candidate(strs = ['101010', '010101', '110011', '001100', '111000', '000111', '1111000000', '0000111111'],m = 10,n = 10) == 3
    assert candidate(strs = ['11111', '11100', '11010', '10110', '01110', '10011', '01011', '00111', '11110', '11001', '10101', '01101'],m = 9,n = 9) == 3
    assert candidate(strs = ['111000', '000111', '111100', '000011', '111111', '000000', '101010'],m = 5,n = 5) == 1
    assert candidate(strs = ['10101010', '01010101', '11110000', '00001111', '11001100', '00110011'],m = 8,n = 8) == 2
    assert candidate(strs = ['1111110', '1010101', '0101010', '0000000', '1111111', '1000001', '0011110'],m = 6,n = 6) == 1
    assert candidate(strs = ['1010101010', '0101010101', '1111111111', '0000000000'],m = 5,n = 5) == 1
    assert candidate(strs = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],m = 10,n = 10) == 10
    assert candidate(strs = ['101', '0011', '1000', '1100', '0100', '0000'],m = 5,n = 5) == 2
    assert candidate(strs = ['1010101010', '0101010101', '1111100000', '0000011111', '1100110011'],m = 10,n = 10) == 2
    assert candidate(strs = ['1010101010', '0101010101', '1110000000', '0001111111', '1100110011', '0011001100', '1011000101', '0100111010', '1111000011', '0000111100'],m = 12,n = 12) == 2
    assert candidate(strs = ['110000', '001100', '101010', '010101', '111100', '000011', '101001'],m = 6,n = 6) == 2
    assert candidate(strs = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],m = 10,n = 10) == 20
    assert candidate(strs = ['111111111', '000000000', '101010101', '010101010', '111000011', '000111100'],m = 7,n = 7) == 1
    assert candidate(strs = ['110', '100', '001', '100', '001', '001', '010', '101', '100', '001', '001', '100', '001', '101', '010', '101', '101', '010', '100', '001'],m = 6,n = 6) == 4
    assert candidate(strs = ['1110000', '0001111', '1100110', '0011001', '1011000', '0100111', '1000000', '0111111', '1101010', '0010101'],m = 10,n = 10) == 2
    assert candidate(strs = ['1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111', '1111111111'],m = 5,n = 5) == 0
    assert candidate(strs = ['111110', '110101', '010110', '110001', '101000', '000011', '011101'],m = 6,n = 6) == 2
    assert candidate(strs = ['1100', '1010', '0011', '0101', '1111', '0000', '1000', '0111', '1101', '1011'],m = 6,n = 6) == 3
    assert candidate(strs = ['000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111', '000000', '111111'],m = 8,n = 8) == 2
    assert candidate(strs = ['1010101', '0101010', '1110000', '0001111', '1100110', '0011001', '1011000', '0100111'],m = 6,n = 6) == 1
    assert candidate(strs = ['1001', '0110', '1010', '0011', '1111', '0000', '1100', '0010', '1000', '0100'],m = 5,n = 5) == 2
    assert candidate(strs = ['11111111', '10101010', '01010101', '00000000', '11000011', '00110011', '10001100'],m = 8,n = 8) == 2
    assert candidate(strs = ['111', '110', '101', '011', '100', '010', '001', '000', '1111', '0000', '1010', '0101'],m = 7,n = 7) == 4
    assert candidate(strs = ['1101010', '1010101', '0011001', '0100110', '1110000', '0001111'],m = 8,n = 8) == 2
    assert candidate(strs = ['111110', '000011', '101010', '010101', '111000', '000111'],m = 6,n = 6) == 2
    assert candidate(strs = ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1'],m = 12,n = 12) == 24
    assert candidate(strs = ['1111111111', '1111111111', '1111111111', '1111111111', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000'],m = 5,n = 5) == 0
    assert candidate(strs = ['11000', '10011', '00100', '01101', '11111'],m = 5,n = 5) == 2
    assert candidate(strs = ['1111111111', '0000000000', '1010101010', '0101010101', '1110000111', '0001111000'],m = 8,n = 8) == 1
    assert candidate(strs = ['1100101', '0000000', '1010101', '1110111', '0001000'],m = 5,n = 5) == 1
    assert candidate(strs = ['1010101010', '0101010101', '1111000000', '0000111111', '1100110011', '0011001100'],m = 5,n = 5) == 1
    assert candidate(strs = ['101010101010101010', '010101010101010101', '111100000000000000', '000011111111111111', '110011001100110011', '001100110011001100'],m = 10,n = 10) == 1
    assert candidate(strs = ['11011', '10010', '01001', '10000', '00111', '01010', '10001'],m = 4,n = 4) == 1
    assert candidate(strs = ['001', '010', '100', '111', '000', '110', '011'],m = 3,n = 3) == 2
    assert candidate(strs = ['1010101010101010101010101010', '0101010101010101010101010101', '1111111111111111111111111111', '0000000000000000000000000000'],m = 10,n = 10) == 0
    assert candidate(strs = ['111100', '111000', '100000', '000111', '001010', '110101'],m = 6,n = 4) == 1
    assert candidate(strs = ['11001100', '00110011', '11110000', '00001111', '10101010', '01010101'],m = 8,n = 8) == 2
    assert candidate(strs = ['11001010', '00010101', '10101010', '00110011', '10111011', '01000100'],m = 6,n = 6) == 1
    assert candidate(strs = ['1101', '0110', '1010', '0010', '1111'],m = 4,n = 3) == 1
    assert candidate(strs = ['1111000000', '0000111100', '1100110000', '0011001100', '1010101000', '0101010100', '1110001100', '0001110011'],m = 10,n = 10) == 2
    assert candidate(strs = ['1101010', '0101110', '1010101', '0011010', '1110000', '0001111', '1111100', '0000011'],m = 8,n = 8) == 2
    assert candidate(strs = ['111000111', '000111000', '110011001', '001100110', '101010101'],m = 6,n = 5) == 1
    assert candidate(strs = ['11000', '01110', '00010', '10011', '00001'],m = 5,n = 5) == 2
    assert candidate(strs = ['1110101', '0001100', '1100011', '0101010', '0010101', '1011010'],m = 8,n = 8) == 2
    assert candidate(strs = ['10101', '01010', '11001', '00110', '11111', '00000'],m = 5,n = 5) == 2
    assert candidate(strs = ['11111111', '00000000', '11000000', '00111111', '10101010', '01010101'],m = 10,n = 10) == 2
    assert candidate(strs = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],m = 10,n = 10) == 10
    assert candidate(strs = ['11111', '00000', '11000', '00111', '10101', '01010'],m = 4,n = 4) == 1
    assert candidate(strs = ['1111111111', '0000000000', '1111000000', '0000111111', '1110110011', '0001001100', '1011000101', '0100111010', '1111000011', '0000111100', '1010101010', '0101010101', '1101010010', '0010101101'],m = 10,n = 10) == 2
    assert candidate(strs = ['11111111', '00000000', '10101010', '01010101', '11001100', '00110011', '10010010', '01101101'],m = 10,n = 10) == 2
    assert candidate(strs = ['1111111111', '0000000000', '1100110011', '0011001100', '1010101010', '0101010101'],m = 8,n = 8) == 1
    assert candidate(strs = ['110000', '000011', '110000', '000011', '110000', '000011', '110000', '000011'],m = 6,n = 6) == 1
    assert candidate(strs = ['011101', '111111', '010101', '000001', '101011'],m = 5,n = 5) == 1
    assert candidate(strs = ['11110000', '00001111', '10101010', '01010101', '11001100', '00110011', '10011001', '01100110'],m = 8,n = 8) == 2
    assert candidate(strs = ['1001001', '0110110', '1111000', '0000111', '1010101', '0101010'],m = 6,n = 6) == 1
    assert candidate(strs = ['1110101', '1000110', '0111000', '0000111', '1010100', '0010011', '1001100'],m = 7,n = 7) == 1
    assert candidate(strs = ['11000', '10011', '01110', '00101', '10110', '11101'],m = 7,n = 7) == 2
    assert candidate(strs = ['111111', '000000', '111000', '000111', '101010', '010101', '110101'],m = 4,n = 5) == 1
    assert candidate(strs = ['1', '0', '11', '00', '10', '01', '1010', '0101'],m = 5,n = 5) == 6
    assert candidate(strs = ['101010101', '010101010', '111000000', '000111111', '110011001', '001100110', '100100100', '011011011'],m = 8,n = 8) == 1
    assert candidate(strs = ['111000', '000111', '110011', '010101', '101010'],m = 4,n = 4) == 1
    assert candidate(strs = ['1010101', '0101010', '1100110', '0011001', '1111000', '0000111'],m = 7,n = 7) == 2
    assert candidate(strs = ['111111', '000000', '110011', '010101', '101010', '001100', '110001', '000111'],m = 4,n = 4) == 1
    assert candidate(strs = ['1010101010', '0101010101', '1110000000', '0001111111', '1100110011', '0011001100', '1011000101', '0100111010', '1111000011', '0000111100', '1010101010', '0101010101'],m = 15,n = 15) == 3
    assert candidate(strs = ['11001100', '00110011', '10101010', '01010101', '11110000', '00001111', '10001000', '01110111'],m = 10,n = 10) == 2
    assert candidate(strs = ['101010101010', '010101010101', '111100000000', '000011111111', '110011001100', '001100110011'],m = 6,n = 6) == 1
    assert candidate(strs = ['10101010101010101010', '01010101010101010101', '11100000000000000000', '00011111111111111111', '11001100110011001100', '00110011001100110011', '10110001010101010101', '01001110101010101010', '11110000110000110000', '00001111001111001111'],m = 20,n = 20) == 2
    assert candidate(strs = ['010101010101', '101010101010', '111111000000', '000000111111', '110011001100'],m = 12,n = 12) == 2
    assert candidate(strs = ['1010101010', '0101010101', '1111000000', '0000111111', '1010101010', '0101010101', '1111000000', '0000111111'],m = 8,n = 8) == 1
    assert candidate(strs = ['110010', '010101', '100100', '111001', '001101', '110011'],m = 7,n = 6) == 2
    assert candidate(strs = ['110101', '101001', '001100', '111000', '000110'],m = 5,n = 5) == 1
    assert candidate(strs = ['110010', '1001', '110', '00010', '1'],m = 5,n = 4) == 3
    assert candidate(strs = ['1101101', '1010101', '0000001', '1111111', '0000000', '1010101'],m = 7,n = 7) == 2
    assert candidate(strs = ['110101', '100110', '101010', '111100', '000111', '010001'],m = 6,n = 6) == 2
    assert candidate(strs = ['00000', '11111', '10101', '01010', '11000', '00111'],m = 6,n = 6) == 2
    assert candidate(strs = ['010101010101', '101010101010', '111111111111', '000000000000', '110011001100', '001100110011'],m = 10,n = 10) == 1
    assert candidate(strs = ['1101010101', '1010101010', '0011001100', '1111111111', '0000000000', '1010101010', '0101010101', '1111000000'],m = 12,n = 12) == 2
    assert candidate(strs = ['1', '0', '11', '00', '101', '010', '110', '001', '111', '000'],m = 6,n = 6) == 6
    assert candidate(strs = ['111001101', '100110100', '011010101', '000111000', '111100001', '101010101', '010101010', '001001001', '110110110'],m = 9,n = 9) == 2
    assert candidate(strs = ['111000', '000111', '101010', '010101', '110011', '001100', '110100', '001011', '100110', '011001'],m = 10,n = 10) == 3
    assert candidate(strs = ['1111111111', '0000000000', '1010101010', '0101010101', '1100110011', '0011001100'],m = 8,n = 8) == 1
    assert candidate(strs = ['111000', '000111', '101010', '010101', '110010', '001101', '100100'],m = 8,n = 8) == 2
    assert candidate(strs = ['101010', '000000', '111111', '100100', '011011'],m = 5,n = 4) == 1
    assert candidate(strs = ['11110000', '00001111', '11101100', '00010011', '11010100', '00101011', '10111000', '01000111'],m = 8,n = 8) == 2
    assert candidate(strs = ['111111', '110000', '001111', '000011', '101010', '010101', '111000', '000111', '101010', '010101', '110011', '001100'],m = 12,n = 12) == 4
    assert candidate(strs = ['111111', '101010', '010101', '000000', '110011'],m = 3,n = 3) == 1
    assert candidate(strs = ['1111111', '0000000', '1110000', '0001111', '1010101', '0101010'],m = 5,n = 5) == 1
    assert candidate(strs = ['111100000', '000011111', '110011000', '001100111', '101010101', '010101010', '111000111', '000111000', '100100110', '011011001'],m = 10,n = 10) == 2
    assert candidate(strs = ['110', '100', '001', '000', '111', '011', '110', '101', '010', '100', '000', '001', '111', '101', '011', '110', '101', '010'],m = 10,n = 10) == 6
    assert candidate(strs = ['10000111', '01111000', '11100011', '00011100', '10101010', '01010101', '11010101', '00101010'],m = 12,n = 12) == 3
    assert candidate(strs = ['1100000000', '0011111111', '1010101010', '0101010101', '1110001110', '0001110001', '1101011011'],m = 7,n = 7) == 1
    assert candidate(strs = ['11001010', '1001111', '00010', '1010', '111', '0000000'],m = 6,n = 6) == 3
    assert candidate(strs = ['101010', '010101', '111111', '000000', '110000', '001100'],m = 4,n = 4) == 1


