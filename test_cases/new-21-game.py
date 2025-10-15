def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 10,k = 5,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50,maxPts = 20) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50,maxPts = 20) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 1,maxPts = 10) == 0.6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 1,maxPts = 10) == 0.6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,k = 0,maxPts = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,k = 0,maxPts = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1,maxPts = 10) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1,maxPts = 10) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 21,k = 17,maxPts = 10) == 0.7327777870686083
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21,k = 17,maxPts = 10) == 0.7327777870686083: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 15,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 15,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 0,k = 0,maxPts = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0,k = 0,maxPts = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 90,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 90,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3,maxPts = 2) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3,maxPts = 2) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 0,maxPts = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 0,maxPts = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 15,maxPts = 10) == 0.18009983358324094
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 15,maxPts = 10) == 0.18009983358324094: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,k = 50,maxPts = 20) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,k = 50,maxPts = 20) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 25,maxPts = 5) == 0.3333044673513253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 25,maxPts = 5) == 0.3333044673513253: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 100,maxPts = 1) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 100,maxPts = 1) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50,maxPts = 50) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50,maxPts = 50) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 25,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 25,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 150,maxPts = 50) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 150,maxPts = 50) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,k = 30,maxPts = 30) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,k = 30,maxPts = 30) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999,k = 0,maxPts = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999,k = 0,maxPts = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 45,maxPts = 10) == 0.18183615529245928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 45,maxPts = 10) == 0.18183615529245928: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 30,maxPts = 20) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 30,maxPts = 20) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 80,maxPts = 20) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 80,maxPts = 20) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 400,maxPts = 50) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 400,maxPts = 50) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 40,maxPts = 10) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 40,maxPts = 10) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,k = 55,maxPts = 10) == 0.818177813346613
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,k = 55,maxPts = 10) == 0.818177813346613: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,k = 30,maxPts = 10) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,k = 30,maxPts = 10) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 0,maxPts = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 0,maxPts = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 150,maxPts = 30) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 150,maxPts = 30) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 10,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 10,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 50,maxPts = 25) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 50,maxPts = 25) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 25,maxPts = 20) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 25,maxPts = 20) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,k = 40,maxPts = 15) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,k = 40,maxPts = 15) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,k = 70,maxPts = 10) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,k = 70,maxPts = 10) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,k = 85,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,k = 85,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,k = 300,maxPts = 50) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,k = 300,maxPts = 50) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 25,maxPts = 10) == 0.8193954028011721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 25,maxPts = 10) == 0.8193954028011721: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 250,maxPts = 100) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 250,maxPts = 100) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 7,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 7,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,k = 20,maxPts = 3) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,k = 20,maxPts = 3) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 15,maxPts = 1) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 15,maxPts = 1) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,k = 60,maxPts = 10) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,k = 60,maxPts = 10) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 25,maxPts = 1) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 25,maxPts = 1) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 0,maxPts = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 0,maxPts = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,k = 1,maxPts = 100) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,k = 1,maxPts = 100) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 20,maxPts = 10) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 20,maxPts = 10) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 20,maxPts = 15) == 0.6217079716932831
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 20,maxPts = 15) == 0.6217079716932831: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 20,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 20,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,k = 90,maxPts = 20) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,k = 90,maxPts = 20) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 70,k = 60,maxPts = 3) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70,k = 60,maxPts = 3) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 10,maxPts = 3) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 10,maxPts = 3) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,k = 75,maxPts = 12) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,k = 75,maxPts = 12) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 25,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 25,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,k = 50,maxPts = 25) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,k = 50,maxPts = 25) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 0,maxPts = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 0,maxPts = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 150,maxPts = 10) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 150,maxPts = 10) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 70,k = 10,maxPts = 30) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70,k = 10,maxPts = 30) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,k = 100,maxPts = 15) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,k = 100,maxPts = 15) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 15,maxPts = 10) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 15,maxPts = 10) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 90,maxPts = 10) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 90,maxPts = 10) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 15,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 15,maxPts = 5) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,k = 80,maxPts = 5) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,k = 80,maxPts = 5) == 1.0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 10,k = 5,maxPts = 5) == 1.0
    assert candidate(n = 100,k = 50,maxPts = 20) == 1.0
    assert candidate(n = 100,k = 50,maxPts = 5) == 1.0
    assert candidate(n = 6,k = 1,maxPts = 10) == 0.6
    assert candidate(n = 10000,k = 0,maxPts = 10000) == 1
    assert candidate(n = 10,k = 1,maxPts = 10) == 1.0
    assert candidate(n = 21,k = 17,maxPts = 10) == 0.7327777870686083
    assert candidate(n = 20,k = 15,maxPts = 5) == 1.0
    assert candidate(n = 0,k = 0,maxPts = 1) == 1
    assert candidate(n = 100,k = 90,maxPts = 5) == 1.0
    assert candidate(n = 5,k = 3,maxPts = 2) == 1.0
    assert candidate(n = 20,k = 0,maxPts = 10) == 1
    assert candidate(n = 15,k = 15,maxPts = 10) == 0.18009983358324094
    assert candidate(n = 75,k = 50,maxPts = 20) == 1.0
    assert candidate(n = 25,k = 25,maxPts = 5) == 0.3333044673513253
    assert candidate(n = 100,k = 100,maxPts = 1) == 1.0
    assert candidate(n = 100,k = 50,maxPts = 50) == 1.0
    assert candidate(n = 30,k = 25,maxPts = 5) == 1.0
    assert candidate(n = 200,k = 150,maxPts = 50) == 1.0
    assert candidate(n = 75,k = 30,maxPts = 30) == 1.0
    assert candidate(n = 9999,k = 0,maxPts = 100) == 1
    assert candidate(n = 45,k = 45,maxPts = 10) == 0.18183615529245928
    assert candidate(n = 50,k = 30,maxPts = 20) == 1.0
    assert candidate(n = 100,k = 80,maxPts = 20) == 1.0
    assert candidate(n = 500,k = 400,maxPts = 50) == 1.0
    assert candidate(n = 50,k = 40,maxPts = 10) == 1.0
    assert candidate(n = 60,k = 55,maxPts = 10) == 0.818177813346613
    assert candidate(n = 60,k = 30,maxPts = 10) == 1.0
    assert candidate(n = 100,k = 0,maxPts = 1) == 1
    assert candidate(n = 200,k = 150,maxPts = 30) == 1.0
    assert candidate(n = 15,k = 10,maxPts = 5) == 1.0
    assert candidate(n = 100,k = 50,maxPts = 25) == 1.0
    assert candidate(n = 50,k = 25,maxPts = 20) == 1.0
    assert candidate(n = 80,k = 40,maxPts = 15) == 1.0
    assert candidate(n = 80,k = 70,maxPts = 10) == 1.0
    assert candidate(n = 90,k = 85,maxPts = 5) == 1.0
    assert candidate(n = 750,k = 300,maxPts = 50) == 1.0
    assert candidate(n = 30,k = 25,maxPts = 10) == 0.8193954028011721
    assert candidate(n = 500,k = 250,maxPts = 100) == 1.0
    assert candidate(n = 15,k = 7,maxPts = 5) == 1.0
    assert candidate(n = 80,k = 20,maxPts = 3) == 1.0
    assert candidate(n = 15,k = 15,maxPts = 1) == 1.0
    assert candidate(n = 80,k = 60,maxPts = 10) == 1.0
    assert candidate(n = 25,k = 25,maxPts = 1) == 1.0
    assert candidate(n = 25,k = 0,maxPts = 25) == 1
    assert candidate(n = 300,k = 1,maxPts = 100) == 1.0
    assert candidate(n = 30,k = 20,maxPts = 10) == 1.0
    assert candidate(n = 25,k = 20,maxPts = 15) == 0.6217079716932831
    assert candidate(n = 25,k = 20,maxPts = 5) == 1.0
    assert candidate(n = 120,k = 90,maxPts = 20) == 1.0
    assert candidate(n = 70,k = 60,maxPts = 3) == 1.0
    assert candidate(n = 15,k = 10,maxPts = 3) == 1.0
    assert candidate(n = 90,k = 75,maxPts = 12) == 1.0
    assert candidate(n = 50,k = 25,maxPts = 5) == 1.0
    assert candidate(n = 75,k = 50,maxPts = 25) == 1.0
    assert candidate(n = 40,k = 0,maxPts = 5) == 1
    assert candidate(n = 200,k = 150,maxPts = 10) == 1.0
    assert candidate(n = 70,k = 10,maxPts = 30) == 1.0
    assert candidate(n = 150,k = 100,maxPts = 15) == 1.0
    assert candidate(n = 30,k = 15,maxPts = 10) == 1.0
    assert candidate(n = 100,k = 90,maxPts = 10) == 1.0
    assert candidate(n = 30,k = 15,maxPts = 5) == 1.0
    assert candidate(n = 90,k = 80,maxPts = 5) == 1.0


