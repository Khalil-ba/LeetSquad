def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "0100100010001000",minJump = 2,maxJump = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100100010001000",minJump = 2,maxJump = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001000",minJump = 2,maxJump = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001000",minJump = 2,maxJump = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0010010010010010010010010010010010010010",minJump = 2,maxJump = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0010010010010010010010010010010010010010",minJump = 2,maxJump = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "011010",minJump = 2,maxJump = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011010",minJump = 2,maxJump = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100000",minJump = 1,maxJump = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100000",minJump = 1,maxJump = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "00001000",minJump = 3,maxJump = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00001000",minJump = 3,maxJump = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101",minJump = 2,maxJump = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101",minJump = 2,maxJump = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101010101010101",minJump = 5,maxJump = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101010101010101",minJump = 5,maxJump = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0111111111111111111111111111111111111111",minJump = 3,maxJump = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0111111111111111111111111111111111111111",minJump = 3,maxJump = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000",minJump = 1,maxJump = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000",minJump = 1,maxJump = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "001000",minJump = 2,maxJump = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001000",minJump = 2,maxJump = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "010101",minJump = 1,maxJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010101",minJump = 1,maxJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000",minJump = 1,maxJump = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000",minJump = 1,maxJump = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "00100",minJump = 3,maxJump = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00100",minJump = 3,maxJump = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "01101110",minJump = 2,maxJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01101110",minJump = 2,maxJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "010000",minJump = 1,maxJump = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010000",minJump = 1,maxJump = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000001000000000",minJump = 4,maxJump = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000001000000000",minJump = 4,maxJump = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000011111000000000000000000",minJump = 1,maxJump = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000011111000000000000000000",minJump = 1,maxJump = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000000000000000000000000000000000",minJump = 5,maxJump = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000000000000000000000000000000000",minJump = 5,maxJump = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000",minJump = 2,maxJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000",minJump = 2,maxJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0111111111111111111111111110",minJump = 10,maxJump = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0111111111111111111111111110",minJump = 10,maxJump = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100000000000000000000000000",minJump = 2,maxJump = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100000000000000000000000000",minJump = 2,maxJump = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000000000000000000000000000000000000000",minJump = 10,maxJump = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000000000000000000000000000000000000000",minJump = 10,maxJump = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "01010101010101010101010101010101010101010101010101",minJump = 5,maxJump = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01010101010101010101010101010101010101010101010101",minJump = 5,maxJump = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",minJump = 3,maxJump = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",minJump = 3,maxJump = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000001",minJump = 5000,maxJump = 10000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000001",minJump = 5000,maxJump = 10000) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000001",minJump = 1,maxJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000001",minJump = 1,maxJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "000001000001000001000001000001000001000001000001",minJump = 6,maxJump = 12) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000001000001000001000001000001000001000001000001",minJump = 6,maxJump = 12) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000111000111000111000111000111000111000111",minJump = 3,maxJump = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000111000111000111000111000111000111000111",minJump = 3,maxJump = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "01001001001001001001001000",minJump = 5,maxJump = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01001001001001001001001000",minJump = 5,maxJump = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "001001001000",minJump = 2,maxJump = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "001001001000",minJump = 2,maxJump = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100000000000000000000000000",minJump = 50000,maxJump = 50000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100000000000000000000000000",minJump = 50000,maxJump = 50000) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000100100010001000100010001000100010001000100010000",minJump = 5,maxJump = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000100100010001000100010001000100010001000100010000",minJump = 5,maxJump = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000000000000000000000000001000000000000000000000000",minJump = 10,maxJump = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000000000000000000000000001000000000000000000000000",minJump = 10,maxJump = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "01001001001001001001001001001001001001001001001001",minJump = 4,maxJump = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "01001001001001001001001001001001001001001001001001",minJump = 4,maxJump = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000",minJump = 5,maxJump = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000",minJump = 5,maxJump = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "010001000100010001000100010001000100010000",minJump = 4,maxJump = 12) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "010001000100010001000100010001000100010000",minJump = 4,maxJump = 12) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000",minJump = 1,maxJump = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000",minJump = 1,maxJump = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0101010101010101010101010101",minJump = 3,maxJump = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0101010101010101010101010101",minJump = 3,maxJump = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100000000000000000000000000",minJump = 10,maxJump = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100000000000000000000000000",minJump = 10,maxJump = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001010101010101010101010101010100",minJump = 3,maxJump = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001010101010101010101010101010100",minJump = 3,maxJump = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000",minJump = 50,maxJump = 100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000",minJump = 50,maxJump = 100) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000",minJump = 4,maxJump = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000",minJump = 4,maxJump = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000",minJump = 1,maxJump = 99999) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000",minJump = 1,maxJump = 99999) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0100000000000000000000000000",minJump = 10000,maxJump = 50000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0100000000000000000000000000",minJump = 10000,maxJump = 50000) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000",minJump = 10000,maxJump = 10000) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000",minJump = 10000,maxJump = 10000) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000",minJump = 100,maxJump = 100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000",minJump = 100,maxJump = 100) == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000000000000000000",minJump = 1,maxJump = 50000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000000000000000000",minJump = 1,maxJump = 50000) == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "0001000100010001000100010000",minJump = 3,maxJump = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0001000100010001000100010000",minJump = 3,maxJump = 5) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "0100100010001000",minJump = 2,maxJump = 5) == True
    assert candidate(s = "00001000",minJump = 2,maxJump = 4) == True
    assert candidate(s = "0010010010010010010010010010010010010010",minJump = 2,maxJump = 4) == True
    assert candidate(s = "011010",minJump = 2,maxJump = 3) == True
    assert candidate(s = "0100000",minJump = 1,maxJump = 2) == True
    assert candidate(s = "00001000",minJump = 3,maxJump = 5) == True
    assert candidate(s = "01010101",minJump = 2,maxJump = 4) == False
    assert candidate(s = "0101010101010101010101010101010101010101",minJump = 5,maxJump = 10) == False
    assert candidate(s = "0111111111111111111111111111111111111111",minJump = 3,maxJump = 5) == False
    assert candidate(s = "000000",minJump = 1,maxJump = 2) == True
    assert candidate(s = "001000",minJump = 2,maxJump = 3) == True
    assert candidate(s = "010101",minJump = 1,maxJump = 2) == False
    assert candidate(s = "00000000",minJump = 1,maxJump = 2) == True
    assert candidate(s = "00100",minJump = 3,maxJump = 4) == True
    assert candidate(s = "01101110",minJump = 2,maxJump = 3) == False
    assert candidate(s = "010000",minJump = 1,maxJump = 3) == True
    assert candidate(s = "00000000001000000000",minJump = 4,maxJump = 7) == True
    assert candidate(s = "0000011111000000000000000000",minJump = 1,maxJump = 5) == False
    assert candidate(s = "00000000000000000000000000000000000000000000000000000000000000000000000000000000",minJump = 5,maxJump = 10) == True
    assert candidate(s = "0000000000000000000000000000",minJump = 2,maxJump = 2) == False
    assert candidate(s = "0111111111111111111111111110",minJump = 10,maxJump = 20) == False
    assert candidate(s = "0100000000000000000000000000",minJump = 2,maxJump = 3) == True
    assert candidate(s = "00000000000000000000000000000000000000000000000000",minJump = 10,maxJump = 20) == True
    assert candidate(s = "01010101010101010101010101010101010101010101010101",minJump = 5,maxJump = 15) == False
    assert candidate(s = "0010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101",minJump = 3,maxJump = 7) == False
    assert candidate(s = "0000000000000000000000000001",minJump = 5000,maxJump = 10000) == False
    assert candidate(s = "0000000000000000000000000001",minJump = 1,maxJump = 1) == False
    assert candidate(s = "000001000001000001000001000001000001000001000001",minJump = 6,maxJump = 12) == False
    assert candidate(s = "000111000111000111000111000111000111000111000111",minJump = 3,maxJump = 6) == False
    assert candidate(s = "01001001001001001001001000",minJump = 5,maxJump = 10) == True
    assert candidate(s = "001001001000",minJump = 2,maxJump = 4) == True
    assert candidate(s = "0100000000000000000000000000",minJump = 50000,maxJump = 50000) == False
    assert candidate(s = "0000100100010001000100010001000100010001000100010000",minJump = 5,maxJump = 15) == True
    assert candidate(s = "0000000000000000000000000000000000000000000000000001000000000000000000000000",minJump = 10,maxJump = 20) == True
    assert candidate(s = "01001001001001001001001001001001001001001001001001",minJump = 4,maxJump = 8) == False
    assert candidate(s = "0000000000000000000000000000",minJump = 5,maxJump = 5) == False
    assert candidate(s = "010001000100010001000100010001000100010000",minJump = 4,maxJump = 12) == True
    assert candidate(s = "0000000000000000000000000000",minJump = 1,maxJump = 10) == True
    assert candidate(s = "0101010101010101010101010101",minJump = 3,maxJump = 5) == False
    assert candidate(s = "0100000000000000000000000000",minJump = 10,maxJump = 10) == False
    assert candidate(s = "0001010101010101010101010101010100",minJump = 3,maxJump = 8) == True
    assert candidate(s = "0000000000000000000000000000",minJump = 50,maxJump = 100) == False
    assert candidate(s = "0000000000",minJump = 4,maxJump = 6) == True
    assert candidate(s = "0000000000000000000000000000",minJump = 1,maxJump = 99999) == True
    assert candidate(s = "0100000000000000000000000000",minJump = 10000,maxJump = 50000) == False
    assert candidate(s = "0000000000000000000000000000",minJump = 10000,maxJump = 10000) == False
    assert candidate(s = "0000000000000000000000000000",minJump = 100,maxJump = 100) == False
    assert candidate(s = "0000000000000000000000000000",minJump = 1,maxJump = 50000) == True
    assert candidate(s = "0001000100010001000100010000",minJump = 3,maxJump = 5) == True


