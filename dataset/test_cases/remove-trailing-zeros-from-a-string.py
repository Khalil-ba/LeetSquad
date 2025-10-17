def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = "10") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10") == "1": {e}')
    
    total += 1
    try:
        result = candidate(num = "100100") == "1001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100100") == "1001": {e}')
    
    total += 1
    try:
        result = candidate(num = "1111111111") == "1111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111111111") == "1111111111": {e}')
    
    total += 1
    try:
        result = candidate(num = "1000") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000") == "1": {e}')
    
    total += 1
    try:
        result = candidate(num = "1") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1") == "1": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210") == "987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210") == "987654321": {e}')
    
    total += 1
    try:
        result = candidate(num = "10500") == "105"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10500") == "105": {e}')
    
    total += 1
    try:
        result = candidate(num = "0") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "51230100") == "512301"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "51230100") == "512301": {e}')
    
    total += 1
    try:
        result = candidate(num = "10101000") == "10101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10101000") == "10101": {e}')
    
    total += 1
    try:
        result = candidate(num = "987654321000") == "987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "987654321000") == "987654321": {e}')
    
    total += 1
    try:
        result = candidate(num = "000000000000000000000") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000000000000000000000") == "": {e}')
    
    total += 1
    try:
        result = candidate(num = "123") == "123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123") == "123": {e}')
    
    total += 1
    try:
        result = candidate(num = "999999999999999999999") == "999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999999999999999999999") == "999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000000000000000001") == "1000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000000000000000001") == "1000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = "1010101010") == "101010101"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1010101010") == "101010101": {e}')
    
    total += 1
    try:
        result = candidate(num = "999999999900") == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999999999900") == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(num = "10000") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10000") == "1": {e}')
    
    total += 1
    try:
        result = candidate(num = "1001001000") == "1001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1001001000") == "1001001": {e}')
    
    total += 1
    try:
        result = candidate(num = "1000000000") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1000000000") == "1": {e}')
    
    total += 1
    try:
        result = candidate(num = "100100100") == "1001001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100100100") == "1001001": {e}')
    
    total += 1
    try:
        result = candidate(num = "9999999999") == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9999999999") == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(num = "00001") == "00001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "00001") == "00001": {e}')
    
    total += 1
    try:
        result = candidate(num = "100000") == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100000") == "1": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = "10") == "1"
    assert candidate(num = "100100") == "1001"
    assert candidate(num = "1111111111") == "1111111111"
    assert candidate(num = "1000") == "1"
    assert candidate(num = "1") == "1"
    assert candidate(num = "9876543210") == "987654321"
    assert candidate(num = "10500") == "105"
    assert candidate(num = "0") == ""
    assert candidate(num = "51230100") == "512301"
    assert candidate(num = "10101000") == "10101"
    assert candidate(num = "987654321000") == "987654321"
    assert candidate(num = "000000000000000000000") == ""
    assert candidate(num = "123") == "123"
    assert candidate(num = "999999999999999999999") == "999999999999999999999"
    assert candidate(num = "1000000000000000000001") == "1000000000000000000001"
    assert candidate(num = "1010101010") == "101010101"
    assert candidate(num = "999999999900") == "9999999999"
    assert candidate(num = "10000") == "1"
    assert candidate(num = "1001001000") == "1001001"
    assert candidate(num = "1000000000") == "1"
    assert candidate(num = "100100100") == "1001001"
    assert candidate(num = "9999999999") == "9999999999"
    assert candidate(num = "00001") == "00001"
    assert candidate(num = "100000") == "1"


