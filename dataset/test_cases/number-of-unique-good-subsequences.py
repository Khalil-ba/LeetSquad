def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(binary = "101") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "101") == 5: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1111") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1111") == 4: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(binary = "010101") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "010101") == 13: {e}')
    
    total += 1
    try:
        result = candidate(binary = "111000111") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "111000111") == 43: {e}')
    
    total += 1
    try:
        result = candidate(binary = "10000100001") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "10000100001") == 64: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1001001") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1001001") == 26: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1010101010") == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1010101010") == 144: {e}')
    
    total += 1
    try:
        result = candidate(binary = "00000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "00000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(binary = "000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(binary = "000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(binary = "001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11") == 2: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0101010101") == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0101010101") == 89: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1100110011") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1100110011") == 99: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0101010") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0101010") == 21: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0") == 1: {e}')
    
    total += 1
    try:
        result = candidate(binary = "111111") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "111111") == 6: {e}')
    
    total += 1
    try:
        result = candidate(binary = "100101010") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "100101010") == 76: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1000000000000000000000000000000000000000000000000000000000000001") == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1000000000000000000000000000000000000000000000000000000000000001") == 127: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1101") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1101") == 8: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1001010") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1001010") == 29: {e}')
    
    total += 1
    try:
        result = candidate(binary = "01010101") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "01010101") == 34: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11010") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11010") == 13: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11111") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11111") == 5: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1111111111") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1111111111") == 10: {e}')
    
    total += 1
    try:
        result = candidate(binary = "00000000000000000000000000000000000000000001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "00000000000000000000000000000000000000000001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11011011011011011011") == 7953
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11011011011011011011") == 7953: {e}')
    
    total += 1
    try:
        result = candidate(binary = "10000000000000000001") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "10000000000000000001") == 39: {e}')
    
    total += 1
    try:
        result = candidate(binary = "010101010101010101010101") == 75025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "010101010101010101010101") == 75025: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11111111111111111111111111111111111111111110") == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11111111111111111111111111111111111111111110") == 87: {e}')
    
    total += 1
    try:
        result = candidate(binary = "100000000000000000000000") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "100000000000000000000000") == 25: {e}')
    
    total += 1
    try:
        result = candidate(binary = "101010101010101010101010101010101010101010101010101") == 316290802
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "101010101010101010101010101010101010101010101010101") == 316290802: {e}')
    
    total += 1
    try:
        result = candidate(binary = "10101010101010101010") == 17711
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "10101010101010101010") == 17711: {e}')
    
    total += 1
    try:
        result = candidate(binary = "010101010101010101010101010101010101010101010101010") == 951279875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "010101010101010101010101010101010101010101010101010") == 951279875: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0000000011111111") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0000000011111111") == 9: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11110000111100001111000011110000") == 121393
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11110000111100001111000011110000") == 121393: {e}')
    
    total += 1
    try:
        result = candidate(binary = "110110110110") == 265
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "110110110110") == 265: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11111000001111100000") == 836
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11111000001111100000") == 836: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1010101010101") == 610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1010101010101") == 610: {e}')
    
    total += 1
    try:
        result = candidate(binary = "111000111000") == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "111000111000") == 142: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1001001001001001001001001001001001") == 3650401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1001001001001001001001001001001001") == 3650401: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0101010101010101010101010101") == 514229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0101010101010101010101010101") == 514229: {e}')
    
    total += 1
    try:
        result = candidate(binary = "010101010101") == 233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "010101010101") == 233: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1010101010101010101010101010101010101010") == 267914296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1010101010101010101010101010101010101010") == 267914296: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0101010101010101") == 1597
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0101010101010101") == 1597: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1111111111111111111111111111111111111111") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1111111111111111111111111111111111111111") == 40: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11001100110011001100") == 8119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11001100110011001100") == 8119: {e}')
    
    total += 1
    try:
        result = candidate(binary = "000000000001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "000000000001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110") == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110") == 199: {e}')
    
    total += 1
    try:
        result = candidate(binary = "01010101010101010101010101010101010101010101010") == 807526948
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "01010101010101010101010101010101010101010101010") == 807526948: {e}')
    
    total += 1
    try:
        result = candidate(binary = "10101010101010101010101") == 75025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "10101010101010101010101") == 75025: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1001001001") == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1001001001") == 97: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11001010010111") == 545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11001010010111") == 545: {e}')
    
    total += 1
    try:
        result = candidate(binary = "000111111111111111111111111111111111111111111111111") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "000111111111111111111111111111111111111111111111111") == 49: {e}')
    
    total += 1
    try:
        result = candidate(binary = "111111111111111111111111") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "111111111111111111111111") == 24: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11111111111111111111111111111111111111111111") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11111111111111111111111111111111111111111111") == 44: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1001001001001001001001001001001001001001001001001001001001") == 379190178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1001001001001001001001001001001001001001001001001001001001") == 379190178: {e}')
    
    total += 1
    try:
        result = candidate(binary = "000000000000000000000000000000000000000000000000001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "000000000000000000000000000000000000000000000000001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0101010101010101010101010101010101010101") == 165580141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0101010101010101010101010101010101010101") == 165580141: {e}')
    
    total += 1
    try:
        result = candidate(binary = "110110110110110110") == 3691
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "110110110110110110") == 3691: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1111000011110000") == 377
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1111000011110000") == 377: {e}')
    
    total += 1
    try:
        result = candidate(binary = "000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1111100000011111") == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1111100000011111") == 191: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1111111111111111111111111111") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1111111111111111111111111111") == 28: {e}')
    
    total += 1
    try:
        result = candidate(binary = "111000111000111000111000111000111000111000111000111000111") == 619446900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "111000111000111000111000111000111000111000111000111000111") == 619446900: {e}')
    
    total += 1
    try:
        result = candidate(binary = "110101010101") == 377
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "110101010101") == 377: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001") == 2: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1001001001001001") == 1351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1001001001001001") == 1351: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1100110011001100") == 1393
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1100110011001100") == 1393: {e}')
    
    total += 1
    try:
        result = candidate(binary = "00000000000000000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "00000000000000000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(binary = "01010101010101010101010101010101010101010101") == 134903163
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "01010101010101010101010101010101010101010101") == 134903163: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1010101010101010101010101010101010101010101010101011") == 681301736
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1010101010101010101010101010101010101010101010101011") == 681301736: {e}')
    
    total += 1
    try:
        result = candidate(binary = "10111001001010011001") == 8492
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "10111001001010011001") == 8492: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11111111111111111110") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11111111111111111110") == 39: {e}')
    
    total += 1
    try:
        result = candidate(binary = "111000111000111000111000111000111000111000111000") == 239244622
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "111000111000111000111000111000111000111000111000") == 239244622: {e}')
    
    total += 1
    try:
        result = candidate(binary = "101010101010") == 377
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "101010101010") == 377: {e}')
    
    total += 1
    try:
        result = candidate(binary = "000000000011111111110000000000") == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "000000000011111111110000000000") == 111: {e}')
    
    total += 1
    try:
        result = candidate(binary = "00000000000000000000") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "00000000000000000000") == 1: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1111100000111110000011111") == 4341
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1111100000111110000011111") == 4341: {e}')
    
    total += 1
    try:
        result = candidate(binary = "100100100100100100100100100100100100100100100100100") == 694626305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "100100100100100100100100100100100100100100100100100") == 694626305: {e}')
    
    total += 1
    try:
        result = candidate(binary = "000111000111000") == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "000111000111000") == 142: {e}')
    
    total += 1
    try:
        result = candidate(binary = "001100110011") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "001100110011") == 99: {e}')
    
    total += 1
    try:
        result = candidate(binary = "11000110001100011000") == 4401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "11000110001100011000") == 4401: {e}')
    
    total += 1
    try:
        result = candidate(binary = "1000000000000000001") == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "1000000000000000001") == 37: {e}')
    
    total += 1
    try:
        result = candidate(binary = "111100001111000011110000111100001111000011110000111") == 133957148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "111100001111000011110000111100001111000011110000111") == 133957148: {e}')
    
    total += 1
    try:
        result = candidate(binary = "10010101010101010101") == 15127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "10010101010101010101") == 15127: {e}')
    
    total += 1
    try:
        result = candidate(binary = "01010101010101010101") == 10946
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "01010101010101010101") == 10946: {e}')
    
    total += 1
    try:
        result = candidate(binary = "0001111111000") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(binary = "0001111111000") == 29: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(binary = "101") == 5
    assert candidate(binary = "1111") == 4
    assert candidate(binary = "1") == 1
    assert candidate(binary = "010101") == 13
    assert candidate(binary = "111000111") == 43
    assert candidate(binary = "10000100001") == 64
    assert candidate(binary = "1001001") == 26
    assert candidate(binary = "1010101010") == 144
    assert candidate(binary = "00000") == 1
    assert candidate(binary = "000000") == 1
    assert candidate(binary = "0000000000") == 1
    assert candidate(binary = "000") == 1
    assert candidate(binary = "001") == 2
    assert candidate(binary = "11") == 2
    assert candidate(binary = "0101010101") == 89
    assert candidate(binary = "1100110011") == 99
    assert candidate(binary = "0101010") == 21
    assert candidate(binary = "0") == 1
    assert candidate(binary = "111111") == 6
    assert candidate(binary = "100101010") == 76
    assert candidate(binary = "1000000000000000000000000000000000000000000000000000000000000001") == 127
    assert candidate(binary = "1101") == 8
    assert candidate(binary = "1001010") == 29
    assert candidate(binary = "01010101") == 34
    assert candidate(binary = "11010") == 13
    assert candidate(binary = "11111") == 5
    assert candidate(binary = "1111111111") == 10
    assert candidate(binary = "00000000000000000000000000000000000000000001") == 2
    assert candidate(binary = "11011011011011011011") == 7953
    assert candidate(binary = "10000000000000000001") == 39
    assert candidate(binary = "010101010101010101010101") == 75025
    assert candidate(binary = "11111111111111111111111111111111111111111110") == 87
    assert candidate(binary = "100000000000000000000000") == 25
    assert candidate(binary = "101010101010101010101010101010101010101010101010101") == 316290802
    assert candidate(binary = "10101010101010101010") == 17711
    assert candidate(binary = "010101010101010101010101010101010101010101010101010") == 951279875
    assert candidate(binary = "0000000011111111") == 9
    assert candidate(binary = "11110000111100001111000011110000") == 121393
    assert candidate(binary = "110110110110") == 265
    assert candidate(binary = "11111000001111100000") == 836
    assert candidate(binary = "1010101010101") == 610
    assert candidate(binary = "111000111000") == 142
    assert candidate(binary = "1001001001001001001001001001001001") == 3650401
    assert candidate(binary = "0101010101010101010101010101") == 514229
    assert candidate(binary = "010101010101") == 233
    assert candidate(binary = "1010101010101010101010101010101010101010") == 267914296
    assert candidate(binary = "0101010101010101") == 1597
    assert candidate(binary = "1111111111111111111111111111111111111111") == 40
    assert candidate(binary = "11001100110011001100") == 8119
    assert candidate(binary = "000000000001") == 2
    assert candidate(binary = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110") == 199
    assert candidate(binary = "01010101010101010101010101010101010101010101010") == 807526948
    assert candidate(binary = "10101010101010101010101") == 75025
    assert candidate(binary = "1001001001") == 97
    assert candidate(binary = "11001010010111") == 545
    assert candidate(binary = "000111111111111111111111111111111111111111111111111") == 49
    assert candidate(binary = "111111111111111111111111") == 24
    assert candidate(binary = "11111111111111111111111111111111111111111111") == 44
    assert candidate(binary = "1001001001001001001001001001001001001001001001001001001001") == 379190178
    assert candidate(binary = "000000000000000000000000000000000000000000000000001") == 2
    assert candidate(binary = "0101010101010101010101010101010101010101") == 165580141
    assert candidate(binary = "110110110110110110") == 3691
    assert candidate(binary = "1111000011110000") == 377
    assert candidate(binary = "000000000000") == 1
    assert candidate(binary = "1111100000011111") == 191
    assert candidate(binary = "1111111111111111111111111111") == 28
    assert candidate(binary = "111000111000111000111000111000111000111000111000111000111") == 619446900
    assert candidate(binary = "110101010101") == 377
    assert candidate(binary = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001") == 2
    assert candidate(binary = "1001001001001001") == 1351
    assert candidate(binary = "1100110011001100") == 1393
    assert candidate(binary = "00000000000000000000000000000000") == 1
    assert candidate(binary = "01010101010101010101010101010101010101010101") == 134903163
    assert candidate(binary = "1010101010101010101010101010101010101010101010101011") == 681301736
    assert candidate(binary = "10111001001010011001") == 8492
    assert candidate(binary = "11111111111111111110") == 39
    assert candidate(binary = "111000111000111000111000111000111000111000111000") == 239244622
    assert candidate(binary = "101010101010") == 377
    assert candidate(binary = "000000000011111111110000000000") == 111
    assert candidate(binary = "00000000000000000000") == 1
    assert candidate(binary = "1111100000111110000011111") == 4341
    assert candidate(binary = "100100100100100100100100100100100100100100100100100") == 694626305
    assert candidate(binary = "000111000111000") == 142
    assert candidate(binary = "001100110011") == 99
    assert candidate(binary = "11000110001100011000") == 4401
    assert candidate(binary = "1000000000000000001") == 37
    assert candidate(binary = "111100001111000011110000111100001111000011110000111") == 133957148
    assert candidate(binary = "10010101010101010101") == 15127
    assert candidate(binary = "01010101010101010101") == 10946
    assert candidate(binary = "0001111111000") == 29


