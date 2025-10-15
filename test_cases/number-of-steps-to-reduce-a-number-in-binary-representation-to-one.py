def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "11101110111") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11101110111") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010101010101") == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010101010101") == 95: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "10010") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10010") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000000000000000000000000000000000000000000000000000000000000") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000000000000000000000000000000000000000000000000000000000000") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111111111111111111111111111111111111111111111111111111111111") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111111111111111111111111111111111111111111111111111111111111") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "11011011") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11011011") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "10") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000000") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000000") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101001") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101001") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110011") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110011") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100100") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100100") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100110011001100110011001100110011001100110") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100110011001100110011001100110011001100110") == 94: {e}')
    
    total += 1
    try:
        result = candidate(s = "11010") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11010") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "100000000000000000000000000000000") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100000000000000000000000000000000") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100100100100100100100100100100100") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100100100100100100100100100100100") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001001001001001001001001001001001001") == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001001001001001001001001001001001001") == 132: {e}')
    
    total += 1
    try:
        result = candidate(s = "1011011011011011011011011011011011011011011") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011011011011011011011011011011011011011011") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000100010001") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000100010001") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "1011011011011011011011011011011011") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011011011011011011011011011011011") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111011111110111111101111111") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111011111110111111101111111") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000000000000000000") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000000000000000000") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000111100001111000") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000111100001111000") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001001001001001001001") == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001001001001001001001") == 107: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101101101101101101101101101101101101101") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101101101101101101101101101101101101101") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110101010101010101010101010101") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110101010101010101010101010101") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000000000000000000000000000000000000000000000000001") == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000000000000000000000000000000000000000000000000001") == 127: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110101010101010101010101010101010101010101010101010101010101010") == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110101010101010101010101010101010101010101010101010101010101010") == 96: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101011010110101101011010110") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101011010110101101011010110") == 43: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010101010101010101010101010101010101010101010101") == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010101010101010101010101010101010101010101010101") == 74: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101") == 68: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110111011101110111011101110111011101110111011101110111011101110") == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110111011101110111011101110111011101110111011101110111011101110") == 80: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101101101101101101101101101101101101101101101101101101101101") == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101101101101101101101101101101101101101101101101101101101101") == 86: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000000000000000000000000000000000000000000000000000000000001") == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000000000000000000000000000000000000000000000000000000000001") == 129: {e}')
    
    total += 1
    try:
        result = candidate(s = "110011001100110011001100110011001100110011001100110011001100110011001100") == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110011001100110011001100110011001100110011001100110011001100110011001100") == 107: {e}')
    
    total += 1
    try:
        result = candidate(s = "110111011101110111011101110111011101110111011101110111011101110111011101") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110111011101110111011101110111011101110111011101110111011101110111011101") == 91: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100001111000011110000111100001111") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100001111000011110000111100001111") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010101") == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010101") == 107: {e}')
    
    total += 1
    try:
        result = candidate(s = "1011101010101010101010101010101") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011101010101010101010101010101") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "11101110111011101110111011101110111011101110111011101110111011101110111") == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11101110111011101110111011101110111011101110111011101110111011101110111") == 89: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111000011110000111100001111000011110000111100001111000011110000") == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111000011110000111100001111000011110000111100001111000011110000") == 93: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111111111111111111111111111111111111") == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111111111111111111111111111111111111") == 80: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010101010101010101") == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010101010101010101") == 98: {e}')
    
    total += 1
    try:
        result = candidate(s = "1011010110101101011010110101101011010110101101011") == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011010110101101011010110101101011010110101101011") == 69: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111111111111111111111") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111111111111111111111") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101") == 59: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010101") == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010101") == 86: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101010101010101010101010101010") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101010101010101010101010101010") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010") == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010") == 108: {e}')
    
    total += 1
    try:
        result = candidate(s = "11101010101010101010101010101") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11101010101010101010101010101") == 43: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000011111111111111111111111111") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000011111111111111111111111111") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111111111111111111111111111") == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111111111111111111111111111") == 69: {e}')
    
    total += 1
    try:
        result = candidate(s = "1010000000000000000000000000000000001") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1010000000000000000000000000000000001") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000000000000000000000000000000000000000000000000111") == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000000000000000000000000000000000000000000000000111") == 125: {e}')
    
    total += 1
    try:
        result = candidate(s = "1011011011011011011011011011011011011011011011011011011011011011011") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011011011011011011011011011011011011011011011011011011011011011011") == 90: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110111011101110111011101110111") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110111011101110111011101110111") == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111111111111111111111111111111111") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111111111111111111111111111111111") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001001001001001001001001001001") == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001001001001001001001001001001") == 122: {e}')
    
    total += 1
    try:
        result = candidate(s = "11110000111100001111000011110000") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11110000111100001111000011110000") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101101101101101101101101101101101101101") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101101101101101101101101101101101101101") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100110011001100110011001") == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100110011001100110011001") == 74: {e}')
    
    total += 1
    try:
        result = candidate(s = "110101010101010101010101010101010101010101010101010101010101010101") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "110101010101010101010101010101010101010101010101010101010101010101") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101010101010101010101010000") == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101010101010101010101010000") == 96: {e}')
    
    total += 1
    try:
        result = candidate(s = "11111111111111111111111111111111") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11111111111111111111111111111111") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "1101111111000000") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1101111111000000") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001") == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001") == 67: {e}')
    
    total += 1
    try:
        result = candidate(s = "10101010101010101010101010101010101010101") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10101010101010101010101010101010101010101") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "10000000000000000000000000000000000000000") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10000000000000000000000000000000000000000") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001100110011001100110011001100110011001100") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001100110011001100110011001100110011001100") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111111111111111111111111111111111111111111111111111111111111010") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111111111111111111111111111111111111111111111111111111111111010") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111101010101010101010101010101") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111101010101010101010101010101") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "11010101010101010101") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11010101010101010101") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "1011101001101001101001101001101") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011101001101001101001101001101") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100110011001100110011001100110") == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100110011001100110011001100110") == 46: {e}')
    
    total += 1
    try:
        result = candidate(s = "1100011000110001100011000110001") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1100011000110001100011000110001") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "1111101111101111101111101111101111101111101111101") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1111101111101111101111101111101111101111101111101") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "1001001001001001001001001001001001001001001001001") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1001001001001001001001001001001001001001001001001") == 82: {e}')
    
    total += 1
    try:
        result = candidate(s = "11001101100110110") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11001101100110110") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "1110111011101110111011101110111011101110111") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1110111011101110111011101110111011101110111") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "111001000111001000111001000111001000") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111001000111001000111001000111001000") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000000000000000000000000000000000000000000000000") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000000000000000000000000000000000000000000000000") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "1011011011011011011011011011011011011011011011011011011011011011011011") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011011011011011011011011011011011011011011011011011011011011011011011") == 94: {e}')
    
    total += 1
    try:
        result = candidate(s = "1011101110111011101110111011101110111011101110111011101110111011") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1011101110111011101110111011101110111011101110111011101110111011") == 81: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "11101110111") == 14
    assert candidate(s = "1111") == 5
    assert candidate(s = "101010101010101010101010101010101010101010101010101010101010101") == 95
    assert candidate(s = "1100110") == 10
    assert candidate(s = "111") == 4
    assert candidate(s = "10010") == 8
    assert candidate(s = "100000") == 5
    assert candidate(s = "100000000000000000000000000000000000000000000000000000000000000") == 62
    assert candidate(s = "1001001") == 12
    assert candidate(s = "1111111111") == 11
    assert candidate(s = "111111111111111111111111111111111111111111111111111111111111111") == 64
    assert candidate(s = "1111111") == 8
    assert candidate(s = "1101") == 6
    assert candidate(s = "11011011") == 11
    assert candidate(s = "10") == 1
    assert candidate(s = "10101010") == 12
    assert candidate(s = "10000000000") == 10
    assert candidate(s = "1010101010") == 15
    assert candidate(s = "1") == 0
    assert candidate(s = "1101001") == 11
    assert candidate(s = "101010") == 9
    assert candidate(s = "1110011") == 10
    assert candidate(s = "1100100") == 10
    assert candidate(s = "110011001100110011001100110011001100110011001100110011001100110") == 94
    assert candidate(s = "11010") == 7
    assert candidate(s = "100000000000000000000000000000000") == 32
    assert candidate(s = "1100100100100100100100100100100100") == 55
    assert candidate(s = "1001001001001001001001001001001001001001001001001001001001001001001001001001001") == 132
    assert candidate(s = "1011011011011011011011011011011011011011011") == 58
    assert candidate(s = "1000100010001") == 23
    assert candidate(s = "1011011011011011011011011011011011") == 46
    assert candidate(s = "1111111011111110111111101111111") == 35
    assert candidate(s = "11111111111111111111111111111111111111111") == 42
    assert candidate(s = "1000000000000000000000000000000") == 30
    assert candidate(s = "1010101010101010101") == 29
    assert candidate(s = "1111000011110000111100001111000") == 44
    assert candidate(s = "1010101010101010101010101010101") == 47
    assert candidate(s = "1001001001001001001001001001001001001001001001001001001001001001") == 107
    assert candidate(s = "1101101101101101101101101101101101101101101") == 58
    assert candidate(s = "1110101010101010101010101010101") == 46
    assert candidate(s = "1000000000000000000000000000000000000000000000000000000000000001") == 127
    assert candidate(s = "11110101010101010101010101010101010101010101010101010101010101010") == 96
    assert candidate(s = "1101101011010110101101011010110") == 43
    assert candidate(s = "1010101010101010101010101010101010101010101010101") == 74
    assert candidate(s = "1001001001001001001001001001001001001") == 62
    assert candidate(s = "101010101010101010101010101010101010101010101") == 68
    assert candidate(s = "1110111011101110111011101110111011101110111011101110111011101110") == 80
    assert candidate(s = "1101101101101101101101101101101101101101101101101101101101101101") == 86
    assert candidate(s = "10101010101010101010101") == 35
    assert candidate(s = "10000000000000000000000000000000000000000000000000000000000000001") == 129
    assert candidate(s = "110011001100110011001100110011001100110011001100110011001100110011001100") == 107
    assert candidate(s = "110111011101110111011101110111011101110111011101110111011101110111011101") == 91
    assert candidate(s = "11110000111100001111000011110000111100001111") == 65
    assert candidate(s = "1001001001001001001001001001001") == 52
    assert candidate(s = "10101010101010101010101010101010101010101010101010101010101010101010101") == 107
    assert candidate(s = "1011101010101010101010101010101") == 46
    assert candidate(s = "11101110111011101110111011101110111011101110111011101110111011101110111") == 89
    assert candidate(s = "1111111111111111111111111111111") == 32
    assert candidate(s = "1111000011110000111100001111000011110000111100001111000011110000") == 93
    assert candidate(s = "1111111111111111111111111111111111111111111111111111111111111111111111111111111") == 80
    assert candidate(s = "10101010101010101010101010101010101010101010101010101010101010101") == 98
    assert candidate(s = "1011010110101101011010110101101011010110101101011") == 69
    assert candidate(s = "1111111111111111111111111111111111111111111111111111111111111111") == 65
    assert candidate(s = "101010101010101010101010101010101010101") == 59
    assert candidate(s = "101010101010101010101010101010101010101010101010101010101") == 86
    assert candidate(s = "1101010101010101010101010101010") == 46
    assert candidate(s = "101010101010101010101010101010101010101010101010101010101010101010101010") == 108
    assert candidate(s = "11101010101010101010101010101") == 43
    assert candidate(s = "1000011111111111111111111111111") == 36
    assert candidate(s = "11111111111111111111111111111111111111111111111111111111111111111111") == 69
    assert candidate(s = "1010000000000000000000000000000000001") == 72
    assert candidate(s = "1000000000000000000000000000000000000000000000000000000000000111") == 125
    assert candidate(s = "1011011011011011011011011011011011011011011011011011011011011011011") == 90
    assert candidate(s = "1110111011101110111011101110111") == 39
    assert candidate(s = "11111111111111111111111111111111111111111111111111111111111111") == 63
    assert candidate(s = "1001001001001001001001001001001001001001001001001001001001001001001001001") == 122
    assert candidate(s = "11110000111100001111000011110000") == 45
    assert candidate(s = "1101101101101101101101101101101101101101") == 54
    assert candidate(s = "1100110011001100110011001100110011001100110011001") == 74
    assert candidate(s = "110101010101010101010101010101010101010101010101010101010101010101") == 99
    assert candidate(s = "10101010101010101010101010101010101010101010101010101010101010000") == 96
    assert candidate(s = "11111111111111111111111111111111") == 33
    assert candidate(s = "1101111111000000") == 18
    assert candidate(s = "1001001001001001001001001001001001001001") == 67
    assert candidate(s = "10101010101010101010101010101010101010101") == 62
    assert candidate(s = "10000000000000000000000000000000000000000") == 40
    assert candidate(s = "11001100110011001100110011001100110011001100") == 65
    assert candidate(s = "1111111111111111111111111111111111111111111111111111111111111010") == 66
    assert candidate(s = "1111101010101010101010101010101") == 45
    assert candidate(s = "11010101010101010101") == 30
    assert candidate(s = "1011101001101001101001101001101") == 46
    assert candidate(s = "1100110011001100110011001100110") == 46
    assert candidate(s = "1100011000110001100011000110001") == 50
    assert candidate(s = "1111101111101111101111101111101111101111101111101") == 58
    assert candidate(s = "1001001001001001001001001001001001001001001001001") == 82
    assert candidate(s = "11001101100110110") == 24
    assert candidate(s = "1110111011101110111011101110111011101110111") == 54
    assert candidate(s = "111001000111001000111001000111001000") == 54
    assert candidate(s = "1000000000000000000000000000000000000000000000000") == 48
    assert candidate(s = "1011011011011011011011011011011011011011011011011011011011011011011011") == 94
    assert candidate(s = "1011101110111011101110111011101110111011101110111011101110111011") == 81


