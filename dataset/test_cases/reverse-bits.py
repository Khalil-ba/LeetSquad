def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111111111111111111111111111111) == 3817748707
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111111111111111111111111111111) == 3817748707: {e}')
    
    total += 1
    try:
        result = candidate(n = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000000000000000000000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000000000000000000000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483648) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483648) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 43261596) == 964176192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43261596) == 964176192: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967293) == 3221225471
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967293) == 3221225471: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 2147483648: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111111111111111111111111111101) == 3180214499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111111111111111111111111111101) == 3180214499: {e}')
    
    total += 1
    try:
        result = candidate(n = 10100101001010010100101001010010) == 1524246408
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10100101001010010100101001010010) == 1524246408: {e}')
    
    total += 1
    try:
        result = candidate(n = 11110000111100001111000011110000) == 242192076
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11110000111100001111000011110000) == 242192076: {e}')
    
    total += 1
    try:
        result = candidate(n = 11110000000011111111000000001111) == 3928946530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11110000000011111111000000001111) == 3928946530: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111111111111110000000000000000) == 57352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111111111111110000000000000000) == 57352: {e}')
    
    total += 1
    try:
        result = candidate(n = 11011011011011011011011011011011) == 3280443572
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11011011011011011011011011011011) == 3280443572: {e}')
    
    total += 1
    try:
        result = candidate(n = 10011100100001011011100110000110) == 2012287233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10011100100001011011100110000110) == 2012287233: {e}')
    
    total += 1
    try:
        result = candidate(n = 11100000111000001110000011100000) == 117259735
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11100000111000001110000011100000) == 117259735: {e}')
    
    total += 1
    try:
        result = candidate(n = 11100001111000011110000111100001) == 2248527424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11100001111000011110000111100001) == 2248527424: {e}')
    
    total += 1
    try:
        result = candidate(n = 10010010010010010010010010010010) == 1501692052
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10010010010010010010010010010010) == 1501692052: {e}')
    
    total += 1
    try:
        result = candidate(n = 10101010101010100101010101010101) == 2910733234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10101010101010100101010101010101) == 2910733234: {e}')
    
    total += 1
    try:
        result = candidate(n = 10101010101010101010101010101010) == 1221553761
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10101010101010101010101010101010) == 1221553761: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111111000000001111111100000000) == 15193787
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111111000000001111111100000000) == 15193787: {e}')
    
    total += 1
    try:
        result = candidate(n = 11110000000000000000000000000000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11110000000000000000000000000000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 10001000100010001000100010001000) == 373324907
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10001000100010001000100010001000) == 373324907: {e}')
    
    total += 1
    try:
        result = candidate(n = 11001100110011001100110011001100) == 815197725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11001100110011001100110011001100) == 815197725: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 11111111111111111111111111111111) == 3817748707
    assert candidate(n = 0) == 0
    assert candidate(n = 10000000000000000000000000000000) == 1
    assert candidate(n = 2147483648) == 1
    assert candidate(n = 43261596) == 964176192
    assert candidate(n = 4294967293) == 3221225471
    assert candidate(n = 1) == 2147483648
    assert candidate(n = 11111111111111111111111111111101) == 3180214499
    assert candidate(n = 10100101001010010100101001010010) == 1524246408
    assert candidate(n = 11110000111100001111000011110000) == 242192076
    assert candidate(n = 11110000000011111111000000001111) == 3928946530
    assert candidate(n = 11111111111111110000000000000000) == 57352
    assert candidate(n = 11011011011011011011011011011011) == 3280443572
    assert candidate(n = 10011100100001011011100110000110) == 2012287233
    assert candidate(n = 11100000111000001110000011100000) == 117259735
    assert candidate(n = 11100001111000011110000111100001) == 2248527424
    assert candidate(n = 10010010010010010010010010010010) == 1501692052
    assert candidate(n = 10101010101010100101010101010101) == 2910733234
    assert candidate(n = 10101010101010101010101010101010) == 1221553761
    assert candidate(n = 11111111000000001111111100000000) == 15193787
    assert candidate(n = 11110000000000000000000000000000) == 14
    assert candidate(n = 10001000100010001000100010001000) == 373324907
    assert candidate(n = 11001100110011001100110011001100) == 815197725


