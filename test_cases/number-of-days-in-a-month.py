def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(year = 2023,month = 11) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2023,month = 11) == 30: {e}')
    
    total += 1
    try:
        result = candidate(year = 1583,month = 8) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1583,month = 8) == 31: {e}')
    
    total += 1
    try:
        result = candidate(year = 1583,month = 1) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1583,month = 1) == 31: {e}')
    
    total += 1
    try:
        result = candidate(year = 1583,month = 12) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1583,month = 12) == 31: {e}')
    
    total += 1
    try:
        result = candidate(year = 2020,month = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2020,month = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(year = 1992,month = 7) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1992,month = 7) == 31: {e}')
    
    total += 1
    try:
        result = candidate(year = 1600,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1600,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 2100,month = 6) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2100,month = 6) == 30: {e}')
    
    total += 1
    try:
        result = candidate(year = 2024,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2024,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 2023,month = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2023,month = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(year = 2020,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2020,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 2100,month = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2100,month = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(year = 2100,month = 12) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2100,month = 12) == 31: {e}')
    
    total += 1
    try:
        result = candidate(year = 1900,month = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1900,month = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(year = 2019,month = 12) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2019,month = 12) == 31: {e}')
    
    total += 1
    try:
        result = candidate(year = 2000,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2000,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 2024,month = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2024,month = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(year = 2040,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2040,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 2021,month = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2021,month = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(year = 2004,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2004,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 1900,month = 12) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1900,month = 12) == 31: {e}')
    
    total += 1
    try:
        result = candidate(year = 1920,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1920,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 2060,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2060,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 2012,month = 9) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2012,month = 9) == 30: {e}')
    
    total += 1
    try:
        result = candidate(year = 1800,month = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1800,month = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(year = 1996,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1996,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 1848,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1848,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 2032,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2032,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 1583,month = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1583,month = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(year = 1924,month = 4) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1924,month = 4) == 30: {e}')
    
    total += 1
    try:
        result = candidate(year = 1980,month = 2) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1980,month = 2) == 29: {e}')
    
    total += 1
    try:
        result = candidate(year = 1700,month = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 1700,month = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(year = 2025,month = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(year = 2025,month = 2) == 28: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(year = 2023,month = 11) == 30
    assert candidate(year = 1583,month = 8) == 31
    assert candidate(year = 1583,month = 1) == 31
    assert candidate(year = 1583,month = 12) == 31
    assert candidate(year = 2020,month = 4) == 30
    assert candidate(year = 1992,month = 7) == 31
    assert candidate(year = 1600,month = 2) == 29
    assert candidate(year = 2100,month = 6) == 30
    assert candidate(year = 2024,month = 2) == 29
    assert candidate(year = 2023,month = 4) == 30
    assert candidate(year = 2020,month = 2) == 29
    assert candidate(year = 2100,month = 4) == 30
    assert candidate(year = 2100,month = 12) == 31
    assert candidate(year = 1900,month = 2) == 28
    assert candidate(year = 2019,month = 12) == 31
    assert candidate(year = 2000,month = 2) == 29
    assert candidate(year = 2024,month = 4) == 30
    assert candidate(year = 2040,month = 2) == 29
    assert candidate(year = 2021,month = 2) == 28
    assert candidate(year = 2004,month = 2) == 29
    assert candidate(year = 1900,month = 12) == 31
    assert candidate(year = 1920,month = 2) == 29
    assert candidate(year = 2060,month = 2) == 29
    assert candidate(year = 2012,month = 9) == 30
    assert candidate(year = 1800,month = 2) == 28
    assert candidate(year = 1996,month = 2) == 29
    assert candidate(year = 1848,month = 2) == 29
    assert candidate(year = 2032,month = 2) == 29
    assert candidate(year = 1583,month = 2) == 28
    assert candidate(year = 1924,month = 4) == 30
    assert candidate(year = 1980,month = 2) == 29
    assert candidate(year = 1700,month = 2) == 28
    assert candidate(year = 2025,month = 2) == 28


