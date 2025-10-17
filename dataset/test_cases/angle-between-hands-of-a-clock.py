def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(hour = 3,minutes = 30) == 75.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 3,minutes = 30) == 75.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 11,minutes = 59) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 11,minutes = 59) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 3,minutes = 15) == 7.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 3,minutes = 15) == 7.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 7,minutes = 30) == 45.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 7,minutes = 30) == 45.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 11,minutes = 0) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 11,minutes = 0) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 2,minutes = 10) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 2,minutes = 10) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 12,minutes = 30) == 165.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 12,minutes = 30) == 165.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 1,minutes = 0) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 1,minutes = 0) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 1,minutes = 55) == 87.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 1,minutes = 55) == 87.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 9,minutes = 45) == 22.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 9,minutes = 45) == 22.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 1,minutes = 5) == 2.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 1,minutes = 5) == 2.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 12,minutes = 0) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 12,minutes = 0) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 6,minutes = 0) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 6,minutes = 0) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 7,minutes = 10) == 155.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 7,minutes = 10) == 155.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 7,minutes = 35) == 17.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 7,minutes = 35) == 17.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 2,minutes = 5) == 32.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 2,minutes = 5) == 32.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 6,minutes = 15) == 97.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 6,minutes = 15) == 97.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 5,minutes = 0) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 5,minutes = 0) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 2,minutes = 47) == 161.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 2,minutes = 47) == 161.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 4,minutes = 0) == 120.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 4,minutes = 0) == 120.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 10,minutes = 25) == 162.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 10,minutes = 25) == 162.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 8,minutes = 23) == 113.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 8,minutes = 23) == 113.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 11,minutes = 15) == 112.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 11,minutes = 15) == 112.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 4,minutes = 50) == 155.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 4,minutes = 50) == 155.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 8,minutes = 18) == 141.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 8,minutes = 18) == 141.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 8,minutes = 20) == 130.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 8,minutes = 20) == 130.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 10,minutes = 31) == 129.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 10,minutes = 31) == 129.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 5,minutes = 10) == 95.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 5,minutes = 10) == 95.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 12,minutes = 15) == 82.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 12,minutes = 15) == 82.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 5,minutes = 14) == 73.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 5,minutes = 14) == 73.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 5,minutes = 45) == 97.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 5,minutes = 45) == 97.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 12,minutes = 59) == 35.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 12,minutes = 59) == 35.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 12,minutes = 1) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 12,minutes = 1) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 10,minutes = 10) == 115.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 10,minutes = 10) == 115.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 7,minutes = 22) == 89.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 7,minutes = 22) == 89.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 12,minutes = 47) == 101.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 12,minutes = 47) == 101.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 2,minutes = 40) == 160.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 2,minutes = 40) == 160.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 5,minutes = 55) == 152.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 5,minutes = 55) == 152.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 7,minutes = 0) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 7,minutes = 0) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 4,minutes = 48) == 144.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 4,minutes = 48) == 144.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 6,minutes = 37) == 23.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 6,minutes = 37) == 23.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 2,minutes = 24) == 72.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 2,minutes = 24) == 72.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 8,minutes = 40) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 8,minutes = 40) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 5,minutes = 15) == 67.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 5,minutes = 15) == 67.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 4,minutes = 10) == 65.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 4,minutes = 10) == 65.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 8,minutes = 50) == 35.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 8,minutes = 50) == 35.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 4,minutes = 40) == 100.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 4,minutes = 40) == 100.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 4,minutes = 25) == 17.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 4,minutes = 25) == 17.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 1,minutes = 37) == 173.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 1,minutes = 37) == 173.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 3,minutes = 47) == 168.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 3,minutes = 47) == 168.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 10,minutes = 48) == 36.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 10,minutes = 48) == 36.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 8,minutes = 32) == 64.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 8,minutes = 32) == 64.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 1,minutes = 10) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 1,minutes = 10) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 7,minutes = 5) == 177.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 7,minutes = 5) == 177.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 6,minutes = 30) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 6,minutes = 30) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 7,minutes = 59) == 114.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 7,minutes = 59) == 114.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 8,minutes = 28) == 86.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 8,minutes = 28) == 86.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 9,minutes = 27) == 121.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 9,minutes = 27) == 121.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 4,minutes = 55) == 177.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 4,minutes = 55) == 177.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 10,minutes = 35) == 107.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 10,minutes = 35) == 107.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 7,minutes = 32) == 34.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 7,minutes = 32) == 34.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 6,minutes = 33) == 1.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 6,minutes = 33) == 1.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 10,minutes = 20) == 170.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 10,minutes = 20) == 170.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 1,minutes = 50) == 115.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 1,minutes = 50) == 115.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 5,minutes = 37) == 53.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 5,minutes = 37) == 53.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 5,minutes = 47) == 108.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 5,minutes = 47) == 108.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 11,minutes = 5) == 57.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 11,minutes = 5) == 57.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 2,minutes = 30) == 105.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 2,minutes = 30) == 105.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 2,minutes = 20) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 2,minutes = 20) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 12,minutes = 45) == 112.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 12,minutes = 45) == 112.5: {e}')
    
    total += 1
    try:
        result = candidate(hour = 8,minutes = 0) == 120.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 8,minutes = 0) == 120.0: {e}')
    
    total += 1
    try:
        result = candidate(hour = 7,minutes = 47) == 48.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hour = 7,minutes = 47) == 48.5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(hour = 3,minutes = 30) == 75.0
    assert candidate(hour = 11,minutes = 59) == 5.5
    assert candidate(hour = 3,minutes = 15) == 7.5
    assert candidate(hour = 7,minutes = 30) == 45.0
    assert candidate(hour = 11,minutes = 0) == 30.0
    assert candidate(hour = 2,minutes = 10) == 5.0
    assert candidate(hour = 12,minutes = 30) == 165.0
    assert candidate(hour = 1,minutes = 0) == 30.0
    assert candidate(hour = 1,minutes = 55) == 87.5
    assert candidate(hour = 9,minutes = 45) == 22.5
    assert candidate(hour = 1,minutes = 5) == 2.5
    assert candidate(hour = 12,minutes = 0) == 0.0
    assert candidate(hour = 6,minutes = 0) == 180.0
    assert candidate(hour = 7,minutes = 10) == 155.0
    assert candidate(hour = 7,minutes = 35) == 17.5
    assert candidate(hour = 2,minutes = 5) == 32.5
    assert candidate(hour = 6,minutes = 15) == 97.5
    assert candidate(hour = 5,minutes = 0) == 150.0
    assert candidate(hour = 2,minutes = 47) == 161.5
    assert candidate(hour = 4,minutes = 0) == 120.0
    assert candidate(hour = 10,minutes = 25) == 162.5
    assert candidate(hour = 8,minutes = 23) == 113.5
    assert candidate(hour = 11,minutes = 15) == 112.5
    assert candidate(hour = 4,minutes = 50) == 155.0
    assert candidate(hour = 8,minutes = 18) == 141.0
    assert candidate(hour = 8,minutes = 20) == 130.0
    assert candidate(hour = 10,minutes = 31) == 129.5
    assert candidate(hour = 5,minutes = 10) == 95.0
    assert candidate(hour = 12,minutes = 15) == 82.5
    assert candidate(hour = 5,minutes = 14) == 73.0
    assert candidate(hour = 5,minutes = 45) == 97.5
    assert candidate(hour = 12,minutes = 59) == 35.5
    assert candidate(hour = 12,minutes = 1) == 5.5
    assert candidate(hour = 10,minutes = 10) == 115.0
    assert candidate(hour = 7,minutes = 22) == 89.0
    assert candidate(hour = 12,minutes = 47) == 101.5
    assert candidate(hour = 2,minutes = 40) == 160.0
    assert candidate(hour = 5,minutes = 55) == 152.5
    assert candidate(hour = 7,minutes = 0) == 150.0
    assert candidate(hour = 4,minutes = 48) == 144.0
    assert candidate(hour = 6,minutes = 37) == 23.5
    assert candidate(hour = 2,minutes = 24) == 72.0
    assert candidate(hour = 8,minutes = 40) == 20.0
    assert candidate(hour = 5,minutes = 15) == 67.5
    assert candidate(hour = 4,minutes = 10) == 65.0
    assert candidate(hour = 8,minutes = 50) == 35.0
    assert candidate(hour = 4,minutes = 40) == 100.0
    assert candidate(hour = 4,minutes = 25) == 17.5
    assert candidate(hour = 1,minutes = 37) == 173.5
    assert candidate(hour = 3,minutes = 47) == 168.5
    assert candidate(hour = 10,minutes = 48) == 36.0
    assert candidate(hour = 8,minutes = 32) == 64.0
    assert candidate(hour = 1,minutes = 10) == 25.0
    assert candidate(hour = 7,minutes = 5) == 177.5
    assert candidate(hour = 6,minutes = 30) == 15.0
    assert candidate(hour = 7,minutes = 59) == 114.5
    assert candidate(hour = 8,minutes = 28) == 86.0
    assert candidate(hour = 9,minutes = 27) == 121.5
    assert candidate(hour = 4,minutes = 55) == 177.5
    assert candidate(hour = 10,minutes = 35) == 107.5
    assert candidate(hour = 7,minutes = 32) == 34.0
    assert candidate(hour = 6,minutes = 33) == 1.5
    assert candidate(hour = 10,minutes = 20) == 170.0
    assert candidate(hour = 1,minutes = 50) == 115.0
    assert candidate(hour = 5,minutes = 37) == 53.5
    assert candidate(hour = 5,minutes = 47) == 108.5
    assert candidate(hour = 11,minutes = 5) == 57.5
    assert candidate(hour = 2,minutes = 30) == 105.0
    assert candidate(hour = 2,minutes = 20) == 50.0
    assert candidate(hour = 12,minutes = 45) == 112.5
    assert candidate(hour = 8,minutes = 0) == 120.0
    assert candidate(hour = 7,minutes = 47) == 48.5


