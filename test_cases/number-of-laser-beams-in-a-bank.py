def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(bank = ['00000', '00000', '00000', '00000']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000', '00000', '00000', '00000']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['001', '000', '101', '000', '110']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['001', '000', '101', '000', '110']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111', '000', '111']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111', '000', '111']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0000', '0000', '0000', '0000']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0000', '0000', '0000', '0000']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['11111', '11111', '11111']) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['11111', '11111', '11111']) == 50: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000', '000', '000']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000', '000', '000']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['101', '010', '101', '010']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['101', '010', '101', '010']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000', '111', '000']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000', '111', '000']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['001', '000', '110', '000', '101']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['001', '000', '110', '000', '101']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1', '0', '1', '0', '1']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1', '0', '1', '0', '1']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111', '000', '111', '000', '111']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111', '000', '111', '000', '111']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['10101', '01010', '10101', '01010']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['10101', '01010', '10101', '01010']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['001', '010', '100']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['001', '010', '100']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111', '111', '111', '111']) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111', '111', '111', '111']) == 27: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['101', '000', '101', '111']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['101', '000', '101', '111']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1010', '0101', '1010', '0101']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1010', '0101', '1010', '0101']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1111', '0000', '1111', '0000']) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1111', '0000', '1111', '0000']) == 16: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000', '000', '000', '111']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000', '000', '000', '111']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000', '000', '000', '000']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000', '000', '000', '000']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['11111', '00000', '00000', '00000', '11111']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['11111', '00000', '00000', '00000', '11111']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['11111', '00000', '11111', '00000']) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['11111', '00000', '11111', '00000']) == 25: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00000', '00001', '00010', '00100', '01000', '10000']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000', '00001', '00010', '00100', '01000', '10000']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['011001', '000000', '010100', '001000']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['011001', '000000', '010100', '001000']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1', '1', '1', '1']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1', '1', '1', '1']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1100', '0011', '0000', '1100']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1100', '0011', '0000', '1100']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00100', '01010', '10001']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00100', '01010', '10001']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['01010', '01010', '01010', '01010']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['01010', '01010', '01010', '01010']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1111', '0000', '1111', '0000', '1111']) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1111', '0000', '1111', '0000', '1111']) == 32: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000', '110111', '000000', '111011', '000000', '101010', '000000']) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000', '110111', '000000', '111011', '000000', '101010', '000000']) == 40: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1010101010', '0101010101', '0000000000', '1111111111', '0000000000', '1010101010']) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1010101010', '0101010101', '0000000000', '1111111111', '0000000000', '1010101010']) == 125: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['11111111111111111111', '00000000000000000000', '11111111111111111111', '00000000000000000000', '11111111111111111111']) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['11111111111111111111', '00000000000000000000', '11111111111111111111', '00000000000000000000', '11111111111111111111']) == 800: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['100100', '001100', '010101', '101010', '000000', '111111']) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['100100', '001100', '010101', '101010', '000000', '111111']) == 37: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['10101', '01010', '10101', '01010', '10101']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['10101', '01010', '10101', '01010', '10101']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00100', '01010', '10001', '01010', '10001', '01010']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00100', '01010', '10001', '01010', '10001', '01010']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['100000', '010000', '001000', '000100', '000010', '000001']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['100000', '010000', '001000', '000100', '000010', '000001']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1111111111', '0000000000', '1010101010', '0101010101', '0000000000', '1111111111']) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1111111111', '0000000000', '1010101010', '0101010101', '0000000000', '1111111111']) == 125: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['101010', '101010', '101010', '101010', '101010', '101010']) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['101010', '101010', '101010', '101010', '101010', '101010']) == 45: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['10001', '01010', '00100', '00000', '10001', '01010', '00100']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['10001', '01010', '00100', '00000', '10001', '01010', '00100']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['10000001', '00100100', '00011000', '00000000', '11111111', '00000000', '10101010']) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['10000001', '00100100', '00011000', '00000000', '11111111', '00000000', '10101010']) == 56: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000', '111', '101', '010', '111', '000', '111']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000', '111', '101', '010', '111', '000', '111']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['01010101', '00000000', '10101010', '00000000', '10101010', '00000000', '10101010']) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['01010101', '00000000', '10101010', '00000000', '10101010', '00000000', '10101010']) == 48: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['110011', '000000', '010100', '001000', '000000', '101010']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['110011', '000000', '010100', '001000', '000000', '101010']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000000', '000000000', '000000000', '000000000', '111111111', '000000000', '111111111', '000000000', '000000000', '000000000']) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000000', '000000000', '000000000', '000000000', '111111111', '000000000', '111111111', '000000000', '000000000', '000000000']) == 81: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['11111', '00000', '10001', '00100', '00000', '10001']) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['11111', '00000', '10001', '00100', '00000', '10001']) == 14: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['11111', '10001', '01110', '10001', '11111']) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['11111', '10001', '01110', '10001', '11111']) == 32: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000000', '000101000', '000000000', '000010000', '000000000', '100000001']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000000', '000101000', '000000000', '000010000', '000000000', '100000001']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000', '000000', '000000', '000000', '000000', '000000']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000', '000000', '000000', '000000', '000000', '000000']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0101010101', '1010101010', '0101010101', '1010101010', '0101010101', '1010101010', '0101010101', '1010101010', '0101010101', '1010101010']) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0101010101', '1010101010', '0101010101', '1010101010', '0101010101', '1010101010', '0101010101', '1010101010', '0101010101', '1010101010']) == 225: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['10000001', '00000000', '00010000', '00000000', '00001000', '00000000', '00000100', '00000000']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['10000001', '00000000', '00010000', '00000000', '00001000', '00000000', '00000100', '00000000']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00000', '00000', '00000', '00000', '11111', '11111', '00000', '11111']) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000', '00000', '00000', '00000', '11111', '11111', '00000', '11111']) == 50: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111', '111', '111', '111', '111', '111', '111']) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111', '111', '111', '111', '111', '111', '111']) == 54: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00000', '00000', '00000', '00000', '00000', '11111', '00000', '11111', '00000', '11111']) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000', '00000', '00000', '00000', '00000', '11111', '00000', '11111', '00000', '11111']) == 50: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1110011', '0000000', '0111011', '0010100', '1111111', '0000000', '1000010']) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1110011', '0000000', '0111011', '0010100', '1111111', '0000000', '1000010']) == 63: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00000', '00100', '01110', '00100', '00000', '11111']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000', '00100', '01110', '00100', '00000', '11111']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['101010', '010101', '101010', '000000', '010101']) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['101010', '010101', '101010', '000000', '010101']) == 27: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000', '101010', '010101', '000000', '101010']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000', '101010', '010101', '000000', '101010']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0000000000', '0000000000', '0000000000', '1111111111', '0000000000', '1010101010', '0101010101', '0000000000']) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0000000000', '0000000000', '0000000000', '1111111111', '0000000000', '1010101010', '0101010101', '0000000000']) == 75: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0010100', '1011011', '0000000', '0000000', '1100110', '0000000', '1001001', '0101010', '0000000', '0000000', '0000000', '1111111']) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0010100', '1011011', '0000000', '0000000', '1100110', '0000000', '1001001', '0101010', '0000000', '0000000', '0000000', '1111111']) == 72: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111', '000', '000', '000', '111', '111', '000', '000', '111', '111']) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111', '000', '000', '000', '111', '111', '000', '000', '111', '111']) == 36: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1111111111', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '1111111111', '0000000000']) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1111111111', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '1111111111', '0000000000']) == 100: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['110000', '001100', '000011', '001100', '110000', '000000', '110000', '001100', '000011', '001100']) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['110000', '001100', '000011', '001100', '110000', '000000', '110000', '001100', '000011', '001100']) == 32: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111111', '000000', '000000', '000000', '111111', '000000', '111111']) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111111', '000000', '000000', '000000', '111111', '000000', '111111']) == 72: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['101010', '010101', '101010', '000000', '111111']) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['101010', '010101', '101010', '000000', '111111']) == 36: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1', '0', '1', '0', '1', '0', '1']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1', '0', '1', '0', '1', '0', '1']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000000000000000', '111111111111111111', '000000000000000000', '000000000000000000', '111111111111111111', '000000000000000000', '111111111111111111']) == 648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000000000000000', '111111111111111111', '000000000000000000', '000000000000000000', '111111111111111111', '000000000000000000', '111111111111111111']) == 648: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1010101010', '0101010101', '0000000000', '1111111111', '0000000000', '1010101010', '0101010101']) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1010101010', '0101010101', '0000000000', '1111111111', '0000000000', '1010101010', '0101010101']) == 150: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1010101010', '0000000000', '0000000000', '1010101010', '0000000000', '0000000000', '1010101010']) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1010101010', '0000000000', '0000000000', '1010101010', '0000000000', '0000000000', '1010101010']) == 50: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00000', '11111', '10101', '01010', '11111', '00000']) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000', '11111', '10101', '01010', '11111', '00000']) == 31: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00000000', '00000000', '00000000', '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000', '00000000', '00000000', '00000000']) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000000', '00000000', '00000000', '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000', '00000000', '00000000', '00000000']) == 7: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1', '0', '1', '0', '1', '0', '1', '0', '1']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1', '0', '1', '0', '1', '0', '1', '0', '1']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00000', '10001', '01010', '00100', '10001', '01010', '00100', '10001', '01010', '00100']) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000', '10001', '01010', '00100', '10001', '01010', '00100', '10001', '01010', '00100']) == 22: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000', '100101', '001000', '000100', '111111', '000000', '110111']) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000', '100101', '001000', '000100', '111111', '000000', '110111']) == 40: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['010101010101010101', '101010101010101010', '000000000000000000', '000000000000000000', '111111111111111111', '000000000000000000', '101010101010101010']) == 405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['010101010101010101', '101010101010101010', '000000000000000000', '000000000000000000', '111111111111111111', '000000000000000000', '101010101010101010']) == 405: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111000', '000111', '111000', '000111', '111000', '000111']) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111000', '000111', '111000', '000111', '111000', '000111']) == 45: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0000000', '0000000', '0000000', '0000000', '0000000', '0000000', '1111111', '1111111']) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0000000', '0000000', '0000000', '0000000', '0000000', '0000000', '1111111', '1111111']) == 49: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111111', '010101', '111111', '000000', '111111']) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111111', '010101', '111111', '000000', '111111']) == 72: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0101010101', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000', '0101010101', '1010101010', '0000000000', '1111111111']) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0101010101', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000', '0101010101', '1010101010', '0000000000', '1111111111']) == 275: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0000000', '0000000', '0101010', '0000000', '1010101', '0000000', '0101010']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0000000', '0000000', '0101010', '0000000', '1010101', '0000000', '0101010']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000', '000000', '101010', '010101', '101010', '000000']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000', '000000', '101010', '010101', '101010', '000000']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['110101', '000000', '011001', '000000', '100100']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['110101', '000000', '011001', '000000', '100100']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1001', '0110', '0000', '1101', '0010', '1010', '0101', '0000', '1111']) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1001', '0110', '0000', '1101', '0010', '1010', '0101', '0000', '1111']) == 27: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111111', '000000', '000000', '000000', '111111', '000000', '111111', '000000', '111111']) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111111', '000000', '000000', '000000', '111111', '000000', '111111', '000000', '111111']) == 108: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0000000000000000000000', '1111111111111111111111', '0000000000000000000000', '0000000000000000000000', '0000000000000000000000', '0000000000000000000000', '1111111111111111111111']) == 484
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0000000000000000000000', '1111111111111111111111', '0000000000000000000000', '0000000000000000000000', '0000000000000000000000', '0000000000000000000000', '1111111111111111111111']) == 484: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111', '111', '000', '111', '111', '000', '111', '111', '000', '111']) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111', '111', '000', '111', '111', '000', '111', '111', '000', '111']) == 54: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['01010101', '10101010', '00000000', '11111111', '01010101']) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['01010101', '10101010', '00000000', '11111111', '01010101']) == 80: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111000', '000111', '111000', '000111', '111000']) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111000', '000111', '111000', '000111', '111000']) == 36: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00000', '11100', '00111', '01010', '10101', '11111', '00000', '11100', '00111', '01010', '10101']) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000', '11100', '00111', '01010', '10101', '11111', '00000', '11100', '00111', '01010', '10101']) == 72: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111111', '000000', '000000', '000000', '000000', '111111']) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111111', '000000', '000000', '000000', '000000', '111111']) == 36: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0000000001', '0000000010', '0000000100', '0000001000', '0000010000', '0000100000', '0001000000', '0010000000', '0100000000', '1000000000']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0000000001', '0000000010', '0000000100', '0000001000', '0000010000', '0000100000', '0001000000', '0010000000', '0100000000', '1000000000']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000', '000100', '100010', '001000', '010000', '100001', '111111']) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000', '000100', '100010', '001000', '010000', '100001', '111111']) == 19: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00000', '00000', '00000', '11111', '00000', '11111', '00000', '11111']) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00000', '00000', '00000', '11111', '00000', '11111', '00000', '11111']) == 50: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['10001', '01100', '00000', '00000', '00000', '01100', '10001', '10001', '01100', '00000', '00000', '10001']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['10001', '01100', '00000', '00000', '00000', '01100', '10001', '10001', '01100', '00000', '00000', '10001']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['01110', '00000', '11001', '00000', '01110', '00000', '10010']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['01110', '00000', '11001', '00000', '01110', '00000', '10010']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111111', '111111', '111111', '111111', '111111', '111111']) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111111', '111111', '111111', '111111', '111111', '111111']) == 180: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111000', '000111', '111000', '000111', '111000', '000111', '111000', '000111']) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111000', '000111', '111000', '000111', '111000', '000111', '111000', '000111']) == 63: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['00100', '01010', '00000', '10001', '01010']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['00100', '01010', '00000', '10001', '01010']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1010101010', '0101010101', '1010101010', '0000000000', '0000000000', '1010101010', '0101010101', '1010101010']) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1010101010', '0101010101', '1010101010', '0000000000', '0000000000', '1010101010', '0101010101', '1010101010']) == 125: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0000000', '0011000', '0000000', '1100110', '0000000', '0101010', '0000000', '1000100']) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0000000', '0011000', '0000000', '1100110', '0000000', '0101010', '0000000', '1000100']) == 26: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['110101', '000000', '101010', '000000', '110101']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['110101', '000000', '101010', '000000', '110101']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['100100', '011011', '000000', '000000', '100100', '011011']) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['100100', '011011', '000000', '000000', '100100', '011011']) == 24: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['001000', '001000', '001000', '001000', '001000', '001000']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['001000', '001000', '001000', '001000', '001000', '001000']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1100011', '0000000', '0110101', '0011001', '1010101', '1111111', '0000000', '1111111']) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1100011', '0000000', '0110101', '0011001', '1010101', '1111111', '0000000', '1111111']) == 117: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['010101', '101010', '010101', '101010', '010101', '101010', '010101']) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['010101', '101010', '010101', '101010', '010101', '101010', '010101']) == 54: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['11111', '00000', '00000', '00000', '11111', '00000', '00000', '11111']) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['11111', '00000', '00000', '00000', '11111', '00000', '00000', '11111']) == 50: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['111111', '000000', '110011', '001100', '111111', '000000', '111111']) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['111111', '000000', '110011', '001100', '111111', '000000', '111111']) == 80: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['110000', '001100', '000011', '000000', '110000', '001100', '000011']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['110000', '001100', '000011', '000000', '110000', '001100', '000011']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['0000000', '0010000', '0000100', '0000010', '0000001', '0000000', '0000000']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['0000000', '0010000', '0000100', '0000010', '0000001', '0000000', '0000000']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000', '000000', '000000', '000000', '110111', '000000', '101010']) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000', '000000', '000000', '000000', '110111', '000000', '101010']) == 15: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1111111', '0000000', '0101010', '0000000', '1010101', '0000000', '1111111']) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1111111', '0000000', '0101010', '0000000', '1010101', '0000000', '1111111']) == 61: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['001000', '010100', '000010', '100001', '000000', '100100', '010010', '001001']) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['001000', '010100', '000010', '100001', '000000', '100100', '010010', '001001']) == 18: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000', '010101', '101010', '000000', '111111', '000000']) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000', '010101', '101010', '000000', '111111', '000000']) == 27: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['000000', '000100', '001010', '010001', '100010', '010100', '100001', '001000']) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['000000', '000100', '001010', '010001', '100010', '010100', '100001', '001000']) == 20: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1010101', '0101010', '1010101', '0101010', '1010101']) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1010101', '0101010', '1010101', '0101010', '1010101']) == 48: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1111111111', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000']) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1111111111', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000']) == 400: {e}')
    
    total += 1
    try:
        result = candidate(bank = ['1111111111', '0000000000', '0000000000', '0000000000', '0000000000', '1111111111']) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bank = ['1111111111', '0000000000', '0000000000', '0000000000', '0000000000', '1111111111']) == 100: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(bank = ['00000', '00000', '00000', '00000']) == 0
    assert candidate(bank = ['001', '000', '101', '000', '110']) == 6
    assert candidate(bank = ['111', '000', '111']) == 9
    assert candidate(bank = ['0000', '0000', '0000', '0000']) == 0
    assert candidate(bank = ['11111', '11111', '11111']) == 50
    assert candidate(bank = ['000', '000', '000']) == 0
    assert candidate(bank = ['101', '010', '101', '010']) == 6
    assert candidate(bank = ['000', '111', '000']) == 0
    assert candidate(bank = ['001', '000', '110', '000', '101']) == 6
    assert candidate(bank = ['1', '0', '1', '0', '1']) == 2
    assert candidate(bank = ['111', '000', '111', '000', '111']) == 18
    assert candidate(bank = ['10101', '01010', '10101', '01010']) == 18
    assert candidate(bank = ['001', '010', '100']) == 2
    assert candidate(bank = ['111', '111', '111', '111']) == 27
    assert candidate(bank = ['101', '000', '101', '111']) == 10
    assert candidate(bank = ['1010', '0101', '1010', '0101']) == 12
    assert candidate(bank = ['1111', '0000', '1111', '0000']) == 16
    assert candidate(bank = ['000', '000', '000', '111']) == 0
    assert candidate(bank = ['000', '000', '000', '000']) == 0
    assert candidate(bank = ['11111', '00000', '00000', '00000', '11111']) == 25
    assert candidate(bank = ['11111', '00000', '11111', '00000']) == 25
    assert candidate(bank = ['00000', '00001', '00010', '00100', '01000', '10000']) == 4
    assert candidate(bank = ['011001', '000000', '010100', '001000']) == 8
    assert candidate(bank = ['1', '1', '1', '1']) == 3
    assert candidate(bank = ['1100', '0011', '0000', '1100']) == 8
    assert candidate(bank = ['00100', '01010', '10001']) == 6
    assert candidate(bank = ['01010', '01010', '01010', '01010']) == 12
    assert candidate(bank = ['1111', '0000', '1111', '0000', '1111']) == 32
    assert candidate(bank = ['000000', '110111', '000000', '111011', '000000', '101010', '000000']) == 40
    assert candidate(bank = ['1010101010', '0101010101', '0000000000', '1111111111', '0000000000', '1010101010']) == 125
    assert candidate(bank = ['11111111111111111111', '00000000000000000000', '11111111111111111111', '00000000000000000000', '11111111111111111111']) == 800
    assert candidate(bank = ['100100', '001100', '010101', '101010', '000000', '111111']) == 37
    assert candidate(bank = ['10101', '01010', '10101', '01010', '10101']) == 24
    assert candidate(bank = ['00100', '01010', '10001', '01010', '10001', '01010']) == 18
    assert candidate(bank = ['100000', '010000', '001000', '000100', '000010', '000001']) == 5
    assert candidate(bank = ['1111111111', '0000000000', '1010101010', '0101010101', '0000000000', '1111111111']) == 125
    assert candidate(bank = ['101010', '101010', '101010', '101010', '101010', '101010']) == 45
    assert candidate(bank = ['10001', '01010', '00100', '00000', '10001', '01010', '00100']) == 14
    assert candidate(bank = ['10000001', '00100100', '00011000', '00000000', '11111111', '00000000', '10101010']) == 56
    assert candidate(bank = ['000', '111', '101', '010', '111', '000', '111']) == 20
    assert candidate(bank = ['01010101', '00000000', '10101010', '00000000', '10101010', '00000000', '10101010']) == 48
    assert candidate(bank = ['110011', '000000', '010100', '001000', '000000', '101010']) == 13
    assert candidate(bank = ['000000000', '000000000', '000000000', '000000000', '111111111', '000000000', '111111111', '000000000', '000000000', '000000000']) == 81
    assert candidate(bank = ['11111', '00000', '10001', '00100', '00000', '10001']) == 14
    assert candidate(bank = ['11111', '10001', '01110', '10001', '11111']) == 32
    assert candidate(bank = ['000000000', '000101000', '000000000', '000010000', '000000000', '100000001']) == 4
    assert candidate(bank = ['000000', '000000', '000000', '000000', '000000', '000000']) == 0
    assert candidate(bank = ['0101010101', '1010101010', '0101010101', '1010101010', '0101010101', '1010101010', '0101010101', '1010101010', '0101010101', '1010101010']) == 225
    assert candidate(bank = ['10000001', '00000000', '00010000', '00000000', '00001000', '00000000', '00000100', '00000000']) == 4
    assert candidate(bank = ['00000', '00000', '00000', '00000', '11111', '11111', '00000', '11111']) == 50
    assert candidate(bank = ['111', '111', '111', '111', '111', '111', '111']) == 54
    assert candidate(bank = ['00000', '00000', '00000', '00000', '00000', '11111', '00000', '11111', '00000', '11111']) == 50
    assert candidate(bank = ['1110011', '0000000', '0111011', '0010100', '1111111', '0000000', '1000010']) == 63
    assert candidate(bank = ['00000', '00100', '01110', '00100', '00000', '11111']) == 11
    assert candidate(bank = ['101010', '010101', '101010', '000000', '010101']) == 27
    assert candidate(bank = ['000000', '101010', '010101', '000000', '101010']) == 18
    assert candidate(bank = ['0000000000', '0000000000', '0000000000', '1111111111', '0000000000', '1010101010', '0101010101', '0000000000']) == 75
    assert candidate(bank = ['0010100', '1011011', '0000000', '0000000', '1100110', '0000000', '1001001', '0101010', '0000000', '0000000', '0000000', '1111111']) == 72
    assert candidate(bank = ['111', '000', '000', '000', '111', '111', '000', '000', '111', '111']) == 36
    assert candidate(bank = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1']) == 7
    assert candidate(bank = ['1111111111', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '0000000000', '1111111111', '0000000000']) == 100
    assert candidate(bank = ['110000', '001100', '000011', '001100', '110000', '000000', '110000', '001100', '000011', '001100']) == 32
    assert candidate(bank = ['111111', '000000', '000000', '000000', '111111', '000000', '111111']) == 72
    assert candidate(bank = ['101010', '010101', '101010', '000000', '111111']) == 36
    assert candidate(bank = ['1', '0', '1', '0', '1', '0', '1']) == 3
    assert candidate(bank = ['000000000000000000', '111111111111111111', '000000000000000000', '000000000000000000', '111111111111111111', '000000000000000000', '111111111111111111']) == 648
    assert candidate(bank = ['1010101010', '0101010101', '0000000000', '1111111111', '0000000000', '1010101010', '0101010101']) == 150
    assert candidate(bank = ['1010101010', '0000000000', '0000000000', '1010101010', '0000000000', '0000000000', '1010101010']) == 50
    assert candidate(bank = ['00000', '11111', '10101', '01010', '11111', '00000']) == 31
    assert candidate(bank = ['00000000', '00000000', '00000000', '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000', '00000000', '00000000', '00000000']) == 7
    assert candidate(bank = ['1', '0', '1', '0', '1', '0', '1', '0', '1']) == 4
    assert candidate(bank = ['00000', '10001', '01010', '00100', '10001', '01010', '00100', '10001', '01010', '00100']) == 22
    assert candidate(bank = ['000000', '100101', '001000', '000100', '111111', '000000', '110111']) == 40
    assert candidate(bank = ['010101010101010101', '101010101010101010', '000000000000000000', '000000000000000000', '111111111111111111', '000000000000000000', '101010101010101010']) == 405
    assert candidate(bank = ['111000', '000111', '111000', '000111', '111000', '000111']) == 45
    assert candidate(bank = ['0000000', '0000000', '0000000', '0000000', '0000000', '0000000', '1111111', '1111111']) == 49
    assert candidate(bank = ['111111', '010101', '111111', '000000', '111111']) == 72
    assert candidate(bank = ['0101010101', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000', '0101010101', '1010101010', '0000000000', '1111111111']) == 275
    assert candidate(bank = ['0000000', '0000000', '0101010', '0000000', '1010101', '0000000', '0101010']) == 24
    assert candidate(bank = ['000000', '000000', '101010', '010101', '101010', '000000']) == 18
    assert candidate(bank = ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0']) == 9
    assert candidate(bank = ['110101', '000000', '011001', '000000', '100100']) == 18
    assert candidate(bank = ['1001', '0110', '0000', '1101', '0010', '1010', '0101', '0000', '1111']) == 27
    assert candidate(bank = ['111111', '000000', '000000', '000000', '111111', '000000', '111111', '000000', '111111']) == 108
    assert candidate(bank = ['0000000000000000000000', '1111111111111111111111', '0000000000000000000000', '0000000000000000000000', '0000000000000000000000', '0000000000000000000000', '1111111111111111111111']) == 484
    assert candidate(bank = ['111', '111', '000', '111', '111', '000', '111', '111', '000', '111']) == 54
    assert candidate(bank = ['01010101', '10101010', '00000000', '11111111', '01010101']) == 80
    assert candidate(bank = ['111000', '000111', '111000', '000111', '111000']) == 36
    assert candidate(bank = ['00000', '11100', '00111', '01010', '10101', '11111', '00000', '11100', '00111', '01010', '10101']) == 72
    assert candidate(bank = ['111111', '000000', '000000', '000000', '000000', '111111']) == 36
    assert candidate(bank = ['0000000001', '0000000010', '0000000100', '0000001000', '0000010000', '0000100000', '0001000000', '0010000000', '0100000000', '1000000000']) == 9
    assert candidate(bank = ['000000', '000100', '100010', '001000', '010000', '100001', '111111']) == 19
    assert candidate(bank = ['00000', '00000', '00000', '11111', '00000', '11111', '00000', '11111']) == 50
    assert candidate(bank = ['10001', '01100', '00000', '00000', '00000', '01100', '10001', '10001', '01100', '00000', '00000', '10001']) == 24
    assert candidate(bank = ['01110', '00000', '11001', '00000', '01110', '00000', '10010']) == 24
    assert candidate(bank = ['111111', '111111', '111111', '111111', '111111', '111111']) == 180
    assert candidate(bank = ['111000', '000111', '111000', '000111', '111000', '000111', '111000', '000111']) == 63
    assert candidate(bank = ['00100', '01010', '00000', '10001', '01010']) == 10
    assert candidate(bank = ['1010101010', '0101010101', '1010101010', '0000000000', '0000000000', '1010101010', '0101010101', '1010101010']) == 125
    assert candidate(bank = ['0000000', '0011000', '0000000', '1100110', '0000000', '0101010', '0000000', '1000100']) == 26
    assert candidate(bank = ['110101', '000000', '101010', '000000', '110101']) == 24
    assert candidate(bank = ['100100', '011011', '000000', '000000', '100100', '011011']) == 24
    assert candidate(bank = ['001000', '001000', '001000', '001000', '001000', '001000']) == 5
    assert candidate(bank = ['1100011', '0000000', '0110101', '0011001', '1010101', '1111111', '0000000', '1111111']) == 117
    assert candidate(bank = ['010101', '101010', '010101', '101010', '010101', '101010', '010101']) == 54
    assert candidate(bank = ['11111', '00000', '00000', '00000', '11111', '00000', '00000', '11111']) == 50
    assert candidate(bank = ['111111', '000000', '110011', '001100', '111111', '000000', '111111']) == 80
    assert candidate(bank = ['110000', '001100', '000011', '000000', '110000', '001100', '000011']) == 20
    assert candidate(bank = ['0000000', '0010000', '0000100', '0000010', '0000001', '0000000', '0000000']) == 3
    assert candidate(bank = ['000000', '000000', '000000', '000000', '110111', '000000', '101010']) == 15
    assert candidate(bank = ['1111111', '0000000', '0101010', '0000000', '1010101', '0000000', '1111111']) == 61
    assert candidate(bank = ['001000', '010100', '000010', '100001', '000000', '100100', '010010', '001001']) == 18
    assert candidate(bank = ['000000', '010101', '101010', '000000', '111111', '000000']) == 27
    assert candidate(bank = ['000000', '000100', '001010', '010001', '100010', '010100', '100001', '001000']) == 20
    assert candidate(bank = ['1010101', '0101010', '1010101', '0101010', '1010101']) == 48
    assert candidate(bank = ['1111111111', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000', '1111111111', '0000000000']) == 400
    assert candidate(bank = ['1111111111', '0000000000', '0000000000', '0000000000', '0000000000', '1111111111']) == 100


