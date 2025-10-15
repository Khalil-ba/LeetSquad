def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 255) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255) == [4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == [1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == [1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == [1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == [1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == [2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == [2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 315) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 315) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 678) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 678) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 170) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 170) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 511) == [5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 511) == [5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 341) == [5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 341) == [5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2047) == [6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2047) == [6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(n = 496) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 496) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 841) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 841) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 384) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 384) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == [1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == [1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 345) == [4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 345) == [4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == [1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == [1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 192) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 192) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 254) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 254) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1365) == [6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1365) == [6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 977) == [4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 977) == [4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 819) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 819) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4095) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4095) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3141) == [4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3141) == [4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 789) == [4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789) == [4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 43690) == [0, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43690) == [0, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 234) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 234) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 131) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == [4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == [3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == [3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 240) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 240) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023) == [5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023) == [5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(n = 564) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 564) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 768) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 768) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535) == [8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535) == [8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 665) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 665) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 641) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 641) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 456) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 456) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == [4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == [4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 867) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 867) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 399) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 399) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 224) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 224) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 577) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 577) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 199) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 987) == [4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987) == [4, 4]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == [0, 1]
    assert candidate(n = 3) == [1, 1]
    assert candidate(n = 1000) == [2, 4]
    assert candidate(n = 63) == [3, 3]
    assert candidate(n = 255) == [4, 4]
    assert candidate(n = 15) == [2, 2]
    assert candidate(n = 64) == [1, 0]
    assert candidate(n = 31) == [3, 2]
    assert candidate(n = 2) == [0, 1]
    assert candidate(n = 1) == [1, 0]
    assert candidate(n = 50) == [1, 2]
    assert candidate(n = 7) == [2, 1]
    assert candidate(n = 5) == [2, 0]
    assert candidate(n = 123) == [3, 3]
    assert candidate(n = 97) == [2, 1]
    assert candidate(n = 315) == [3, 3]
    assert candidate(n = 678) == [1, 4]
    assert candidate(n = 170) == [0, 4]
    assert candidate(n = 511) == [5, 4]
    assert candidate(n = 341) == [5, 0]
    assert candidate(n = 100) == [2, 1]
    assert candidate(n = 2047) == [6, 5]
    assert candidate(n = 496) == [3, 2]
    assert candidate(n = 841) == [3, 2]
    assert candidate(n = 384) == [1, 1]
    assert candidate(n = 4) == [1, 0]
    assert candidate(n = 345) == [4, 1]
    assert candidate(n = 16) == [1, 0]
    assert candidate(n = 192) == [1, 1]
    assert candidate(n = 254) == [3, 4]
    assert candidate(n = 1365) == [6, 0]
    assert candidate(n = 1001) == [3, 4]
    assert candidate(n = 977) == [4, 2]
    assert candidate(n = 819) == [3, 3]
    assert candidate(n = 128) == [0, 1]
    assert candidate(n = 4095) == [6, 6]
    assert candidate(n = 3141) == [4, 1]
    assert candidate(n = 250) == [2, 4]
    assert candidate(n = 789) == [4, 1]
    assert candidate(n = 43690) == [0, 8]
    assert candidate(n = 234) == [1, 4]
    assert candidate(n = 131) == [1, 2]
    assert candidate(n = 999) == [4, 4]
    assert candidate(n = 89) == [3, 1]
    assert candidate(n = 32) == [0, 1]
    assert candidate(n = 240) == [2, 2]
    assert candidate(n = 1023) == [5, 5]
    assert candidate(n = 564) == [2, 2]
    assert candidate(n = 768) == [1, 1]
    assert candidate(n = 65535) == [8, 8]
    assert candidate(n = 665) == [2, 3]
    assert candidate(n = 641) == [1, 2]
    assert candidate(n = 456) == [2, 2]
    assert candidate(n = 85) == [4, 0]
    assert candidate(n = 867) == [3, 3]
    assert candidate(n = 399) == [3, 3]
    assert candidate(n = 1234) == [3, 2]
    assert candidate(n = 512) == [0, 1]
    assert candidate(n = 224) == [1, 2]
    assert candidate(n = 577) == [2, 1]
    assert candidate(n = 199) == [3, 2]
    assert candidate(n = 987) == [4, 4]


