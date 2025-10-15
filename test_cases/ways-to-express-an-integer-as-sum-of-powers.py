def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 100,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,x = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,x = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,x = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,x = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 160,x = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 160,x = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,x = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,x = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,x = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,x = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,x = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,x = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 144,x = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 144,x = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 225,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 180,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 125,x = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125,x = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 190,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 190,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 199,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 243,x = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 243,x = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 210,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 210,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 290,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 290,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,x = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,x = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 260,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 260,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,x = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 128,x = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128,x = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 160,x = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 160,x = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 180,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,x = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,x = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 299,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 299,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 175,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 175,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 180,x = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180,x = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 210,x = 2) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 210,x = 2) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 220,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 220,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 280,x = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 280,x = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 275,x = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 275,x = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 275,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 275,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,x = 1) == 872471266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,x = 1) == 872471266: {e}')
    
    total += 1
    try:
        result = candidate(n = 190,x = 2) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 190,x = 2) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 140,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 140,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 170,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 170,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 299,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 299,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 195,x = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 195,x = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 275,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 275,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 280,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 280,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 140,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 140,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 260,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 260,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 196,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 196,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 289,x = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 289,x = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,x = 1) == 487067746
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,x = 1) == 487067746: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,x = 1) == 444793
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 1) == 444793: {e}')
    
    total += 1
    try:
        result = candidate(n = 175,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 175,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 260,x = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 260,x = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 180,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 170,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 170,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 290,x = 2) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 290,x = 2) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 299,x = 2) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 299,x = 2) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 256,x = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256,x = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 270,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 270,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,x = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,x = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,x = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,x = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 125,x = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125,x = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,x = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,x = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,x = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,x = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 81,x = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81,x = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,x = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,x = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,x = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,x = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,x = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,x = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,x = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,x = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,x = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,x = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 64,x = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,x = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,x = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,x = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 31,x = 1) == 340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31,x = 1) == 340: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,x = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,x = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 256,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 64,x = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,x = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,x = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,x = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,x = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,x = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,x = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,x = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,x = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,x = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 81,x = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81,x = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 70,x = 1) == 29927
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70,x = 1) == 29927: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,x = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,x = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,x = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,x = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,x = 1) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,x = 1) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,x = 2) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,x = 2) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,x = 1) == 296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,x = 1) == 296: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 100,x = 4) == 0
    assert candidate(n = 50,x = 2) == 3
    assert candidate(n = 200,x = 2) == 9
    assert candidate(n = 300,x = 5) == 0
    assert candidate(n = 160,x = 3) == 1
    assert candidate(n = 4,x = 1) == 2
    assert candidate(n = 10,x = 2) == 1
    assert candidate(n = 20,x = 2) == 1
    assert candidate(n = 200,x = 5) == 0
    assert candidate(n = 144,x = 2) == 2
    assert candidate(n = 225,x = 4) == 0
    assert candidate(n = 180,x = 5) == 0
    assert candidate(n = 125,x = 2) == 5
    assert candidate(n = 80,x = 3) == 0
    assert candidate(n = 190,x = 5) == 0
    assert candidate(n = 300,x = 3) == 0
    assert candidate(n = 199,x = 4) == 0
    assert candidate(n = 243,x = 5) == 1
    assert candidate(n = 210,x = 5) == 0
    assert candidate(n = 290,x = 5) == 0
    assert candidate(n = 200,x = 4) == 0
    assert candidate(n = 120,x = 2) == 4
    assert candidate(n = 260,x = 4) == 0
    assert candidate(n = 100,x = 2) == 3
    assert candidate(n = 128,x = 2) == 0
    assert candidate(n = 160,x = 2) == 4
    assert candidate(n = 150,x = 4) == 0
    assert candidate(n = 180,x = 4) == 0
    assert candidate(n = 150,x = 2) == 9
    assert candidate(n = 299,x = 5) == 0
    assert candidate(n = 175,x = 3) == 0
    assert candidate(n = 180,x = 2) == 6
    assert candidate(n = 210,x = 2) == 18
    assert candidate(n = 220,x = 3) == 0
    assert candidate(n = 280,x = 3) == 1
    assert candidate(n = 275,x = 5) == 1
    assert candidate(n = 275,x = 4) == 0
    assert candidate(n = 300,x = 1) == 872471266
    assert candidate(n = 190,x = 2) == 14
    assert candidate(n = 140,x = 5) == 0
    assert candidate(n = 170,x = 3) == 0
    assert candidate(n = 299,x = 3) == 0
    assert candidate(n = 195,x = 2) == 16
    assert candidate(n = 275,x = 3) == 0
    assert candidate(n = 280,x = 4) == 0
    assert candidate(n = 140,x = 4) == 0
    assert candidate(n = 260,x = 5) == 0
    assert candidate(n = 196,x = 4) == 0
    assert candidate(n = 250,x = 3) == 0
    assert candidate(n = 289,x = 3) == 1
    assert candidate(n = 150,x = 3) == 0
    assert candidate(n = 200,x = 1) == 487067746
    assert candidate(n = 120,x = 3) == 0
    assert candidate(n = 100,x = 1) == 444793
    assert candidate(n = 175,x = 4) == 0
    assert candidate(n = 260,x = 2) == 19
    assert candidate(n = 180,x = 3) == 0
    assert candidate(n = 170,x = 5) == 0
    assert candidate(n = 290,x = 2) == 31
    assert candidate(n = 299,x = 2) == 33
    assert candidate(n = 256,x = 4) == 1
    assert candidate(n = 270,x = 3) == 0
    assert candidate(n = 90,x = 3) == 0
    assert candidate(n = 250,x = 4) == 0
    assert candidate(n = 17,x = 2) == 1
    assert candidate(n = 1,x = 5) == 1
    assert candidate(n = 3,x = 1) == 2
    assert candidate(n = 125,x = 3) == 1
    assert candidate(n = 2,x = 2) == 0
    assert candidate(n = 50,x = 3) == 0
    assert candidate(n = 81,x = 4) == 1
    assert candidate(n = 20,x = 4) == 0
    assert candidate(n = 17,x = 4) == 1
    assert candidate(n = 5,x = 1) == 3
    assert candidate(n = 15,x = 2) == 0
    assert candidate(n = 120,x = 4) == 0
    assert candidate(n = 100,x = 3) == 1
    assert candidate(n = 27,x = 3) == 1
    assert candidate(n = 64,x = 2) == 1
    assert candidate(n = 8,x = 3) == 1
    assert candidate(n = 31,x = 1) == 340
    assert candidate(n = 1,x = 1) == 1
    assert candidate(n = 256,x = 5) == 0
    assert candidate(n = 64,x = 3) == 1
    assert candidate(n = 25,x = 2) == 2
    assert candidate(n = 28,x = 2) == 0
    assert candidate(n = 9,x = 2) == 1
    assert candidate(n = 12,x = 2) == 0
    assert candidate(n = 250,x = 5) == 0
    assert candidate(n = 81,x = 2) == 3
    assert candidate(n = 70,x = 1) == 29927
    assert candidate(n = 50,x = 5) == 0
    assert candidate(n = 9,x = 4) == 0
    assert candidate(n = 15,x = 1) == 27
    assert candidate(n = 250,x = 2) == 21
    assert candidate(n = 30,x = 1) == 296


