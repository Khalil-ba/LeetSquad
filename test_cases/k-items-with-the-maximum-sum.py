def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 3,numZeros = 2,numNegOnes = 0,k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 3,numZeros = 2,numNegOnes = 0,k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 20,numNegOnes = 10,k = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 20,numNegOnes = 10,k = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 10,numNegOnes = 10,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 10,numNegOnes = 10,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 25,numZeros = 0,numNegOnes = 25,k = 30) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 25,numZeros = 0,numNegOnes = 25,k = 30) == 20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 50,numZeros = 50,numNegOnes = 50,k = 100) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 50,numZeros = 50,numNegOnes = 50,k = 100) == 50: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 50) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 50) == -25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 1,numZeros = 3,numNegOnes = 2,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 1,numZeros = 3,numNegOnes = 2,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 5,numZeros = 5,numNegOnes = 5,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 5,numZeros = 5,numNegOnes = 5,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 50,numZeros = 30,numNegOnes = 20,k = 100) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 50,numZeros = 30,numNegOnes = 20,k = 100) == 30: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 10) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 10) == -10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 40) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 40) == -15: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 25) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 25) == -25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 10,numNegOnes = 10,k = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 10,numNegOnes = 10,k = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 50) == -50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 50) == -50: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 0,numNegOnes = 0,k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 0,numNegOnes = 0,k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 40) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 40) == -10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 1,numZeros = 1,numNegOnes = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 1,numZeros = 1,numNegOnes = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 0,numNegOnes = 5,k = 3) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 0,numNegOnes = 5,k = 3) == -3: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 30) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 30) == 25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 25,numZeros = 0,numNegOnes = 25,k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 25,numZeros = 0,numNegOnes = 25,k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 20) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 20) == -20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 3,numZeros = 2,numNegOnes = 0,k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 3,numZeros = 2,numNegOnes = 0,k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 45,numZeros = 0,numNegOnes = 5,k = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 45,numZeros = 0,numNegOnes = 5,k = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 10,numNegOnes = 10,k = 50) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 10,numNegOnes = 10,k = 50) == 20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 10,numNegOnes = 20,k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 10,numNegOnes = 20,k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 20,numNegOnes = 5,k = 40) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 20,numNegOnes = 5,k = 40) == 30: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 45,numZeros = 20,numNegOnes = 35,k = 50) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 45,numZeros = 20,numNegOnes = 35,k = 50) == 45: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 20,numNegOnes = 10,k = 30) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 20,numNegOnes = 10,k = 30) == 20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 15,numZeros = 10,numNegOnes = 25,k = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 15,numZeros = 10,numNegOnes = 25,k = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 40,numZeros = 5,numNegOnes = 5,k = 48) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 40,numZeros = 5,numNegOnes = 5,k = 48) == 37: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 0,numNegOnes = 30,k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 0,numNegOnes = 30,k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 10,numNegOnes = 10,k = 45) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 10,numNegOnes = 10,k = 45) == 25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 15,numNegOnes = 10,k = 45) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 15,numNegOnes = 10,k = 45) == 30: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 35) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 35) == -5: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 40,numZeros = 5,numNegOnes = 5,k = 45) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 40,numZeros = 5,numNegOnes = 5,k = 45) == 40: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 5,numZeros = 0,numNegOnes = 45,k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 5,numZeros = 0,numNegOnes = 45,k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 0,numNegOnes = 20,k = 40) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 0,numNegOnes = 20,k = 40) == 20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 15,numNegOnes = 15,k = 30) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 15,numNegOnes = 15,k = 30) == 20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 49) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 49) == 49: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 40,numZeros = 5,numNegOnes = 5,k = 50) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 40,numZeros = 5,numNegOnes = 5,k = 50) == 35: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 30,numNegOnes = 10,k = 50) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 30,numNegOnes = 10,k = 50) == 20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 45,numZeros = 3,numNegOnes = 2,k = 50) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 45,numZeros = 3,numNegOnes = 2,k = 50) == 43: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 24) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 24) == 24: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 45,numZeros = 0,numNegOnes = 5,k = 48) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 45,numZeros = 0,numNegOnes = 5,k = 48) == 42: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 25,numZeros = 15,numNegOnes = 10,k = 50) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 25,numZeros = 15,numNegOnes = 10,k = 50) == 15: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 0,numNegOnes = 40,k = 50) == -30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 0,numNegOnes = 40,k = 50) == -30: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 15,numZeros = 0,numNegOnes = 35,k = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 15,numZeros = 0,numNegOnes = 35,k = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 10,numNegOnes = 20,k = 30) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 10,numNegOnes = 20,k = 30) == 20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 45,numZeros = 2,numNegOnes = 3,k = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 45,numZeros = 2,numNegOnes = 3,k = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 20,numNegOnes = 30,k = 60) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 20,numNegOnes = 30,k = 60) == -20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 15,numNegOnes = 15,k = 40) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 15,numNegOnes = 15,k = 40) == 15: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 30,numNegOnes = 10,k = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 30,numNegOnes = 10,k = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 20,numNegOnes = 20,k = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 20,numNegOnes = 20,k = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 15,numZeros = 15,numNegOnes = 20,k = 40) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 15,numZeros = 15,numNegOnes = 20,k = 40) == 5: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 45) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 45) == -20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 20,numNegOnes = 30,k = 40) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 20,numNegOnes = 30,k = 40) == -20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 40,numZeros = 0,numNegOnes = 10,k = 45) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 40,numZeros = 0,numNegOnes = 10,k = 45) == 35: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 40) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 40) == 25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 15,numZeros = 15,numNegOnes = 20,k = 20) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 15,numZeros = 15,numNegOnes = 20,k = 20) == 15: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 15,numNegOnes = 5,k = 40) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 15,numNegOnes = 5,k = 40) == 30: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 35,numZeros = 10,numNegOnes = 5,k = 45) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 35,numZeros = 10,numNegOnes = 5,k = 45) == 35: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 30,numNegOnes = 20,k = 40) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 30,numNegOnes = 20,k = 40) == -10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 15,numZeros = 20,numNegOnes = 15,k = 25) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 15,numZeros = 20,numNegOnes = 15,k = 25) == 15: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 20,numNegOnes = 20,k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 20,numNegOnes = 20,k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 40,numNegOnes = 10,k = 60) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 40,numNegOnes = 10,k = 60) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 10,numNegOnes = 10,k = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 10,numNegOnes = 10,k = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 0,numNegOnes = 30,k = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 0,numNegOnes = 30,k = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 1,numZeros = 48,numNegOnes = 1,k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 1,numZeros = 48,numNegOnes = 1,k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 1,numZeros = 1,numNegOnes = 1,k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 1,numZeros = 1,numNegOnes = 1,k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 15,numNegOnes = 15,k = 40) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 15,numNegOnes = 15,k = 40) == 30: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 40,numZeros = 40,numNegOnes = 10,k = 60) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 40,numZeros = 40,numNegOnes = 10,k = 60) == 40: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 30,numNegOnes = 50,k = 60) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 30,numNegOnes = 50,k = 60) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 30,numNegOnes = 10,k = 40) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 30,numNegOnes = 10,k = 40) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 2,numZeros = 2,numNegOnes = 2,k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 2,numZeros = 2,numNegOnes = 2,k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 15,numZeros = 25,numNegOnes = 10,k = 20) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 15,numZeros = 25,numNegOnes = 10,k = 20) == 15: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 10,numNegOnes = 10,k = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 10,numNegOnes = 10,k = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 20,numNegOnes = 50,k = 70) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 20,numNegOnes = 50,k = 70) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 5,numNegOnes = 15,k = 40) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 5,numNegOnes = 15,k = 40) == 25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 15,numNegOnes = 15,k = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 15,numNegOnes = 15,k = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 30,numZeros = 20,numNegOnes = 10,k = 40) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 30,numZeros = 20,numNegOnes = 10,k = 40) == 30: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 30) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 30) == -5: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 0,numNegOnes = 100,k = 50) == -50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 0,numNegOnes = 100,k = 50) == -50: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 45,numZeros = 30,numNegOnes = 25,k = 50) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 45,numZeros = 30,numNegOnes = 25,k = 50) == 45: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 0,numZeros = 10,numNegOnes = 40,k = 20) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 0,numZeros = 10,numNegOnes = 40,k = 20) == -10: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 49) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 49) == 25: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 45,numZeros = 0,numNegOnes = 5,k = 35) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 45,numZeros = 0,numNegOnes = 5,k = 35) == 35: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 50,numZeros = 0,numNegOnes = 50,k = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 50,numZeros = 0,numNegOnes = 50,k = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 20,numZeros = 15,numNegOnes = 10,k = 30) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 20,numZeros = 15,numNegOnes = 10,k = 30) == 20: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 5,numZeros = 5,numNegOnes = 40,k = 20) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 5,numZeros = 5,numNegOnes = 40,k = 20) == -5: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 45,numZeros = 5,numNegOnes = 0,k = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 45,numZeros = 5,numNegOnes = 0,k = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(numOnes = 5,numZeros = 10,numNegOnes = 35,k = 50) == -30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numOnes = 5,numZeros = 10,numNegOnes = 35,k = 50) == -30: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 50) == 25
    assert candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 10) == 0
    assert candidate(numOnes = 3,numZeros = 2,numNegOnes = 0,k = 2) == 2
    assert candidate(numOnes = 20,numZeros = 20,numNegOnes = 10,k = 50) == 10
    assert candidate(numOnes = 10,numZeros = 10,numNegOnes = 10,k = 5) == 5
    assert candidate(numOnes = 25,numZeros = 0,numNegOnes = 25,k = 30) == 20
    assert candidate(numOnes = 50,numZeros = 50,numNegOnes = 50,k = 100) == 50
    assert candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 50) == -25
    assert candidate(numOnes = 1,numZeros = 3,numNegOnes = 2,k = 5) == 0
    assert candidate(numOnes = 5,numZeros = 5,numNegOnes = 5,k = 5) == 5
    assert candidate(numOnes = 50,numZeros = 30,numNegOnes = 20,k = 100) == 30
    assert candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 10) == -10
    assert candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 40) == -15
    assert candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 50) == 0
    assert candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 25) == -25
    assert candidate(numOnes = 10,numZeros = 10,numNegOnes = 10,k = 15) == 10
    assert candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 50) == 50
    assert candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 50) == -50
    assert candidate(numOnes = 0,numZeros = 0,numNegOnes = 0,k = 0) == 0
    assert candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 40) == -10
    assert candidate(numOnes = 1,numZeros = 1,numNegOnes = 1,k = 1) == 1
    assert candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 10) == 10
    assert candidate(numOnes = 0,numZeros = 0,numNegOnes = 5,k = 3) == -3
    assert candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 30) == 0
    assert candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 30) == 25
    assert candidate(numOnes = 25,numZeros = 0,numNegOnes = 25,k = 50) == 0
    assert candidate(numOnes = 0,numZeros = 0,numNegOnes = 50,k = 20) == -20
    assert candidate(numOnes = 3,numZeros = 2,numNegOnes = 0,k = 4) == 3
    assert candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 20) == 0
    assert candidate(numOnes = 45,numZeros = 0,numNegOnes = 5,k = 45) == 45
    assert candidate(numOnes = 30,numZeros = 10,numNegOnes = 10,k = 50) == 20
    assert candidate(numOnes = 20,numZeros = 10,numNegOnes = 20,k = 50) == 0
    assert candidate(numOnes = 30,numZeros = 20,numNegOnes = 5,k = 40) == 30
    assert candidate(numOnes = 45,numZeros = 20,numNegOnes = 35,k = 50) == 45
    assert candidate(numOnes = 20,numZeros = 20,numNegOnes = 10,k = 30) == 20
    assert candidate(numOnes = 15,numZeros = 10,numNegOnes = 25,k = 30) == 10
    assert candidate(numOnes = 40,numZeros = 5,numNegOnes = 5,k = 48) == 37
    assert candidate(numOnes = 20,numZeros = 0,numNegOnes = 30,k = 20) == 20
    assert candidate(numOnes = 30,numZeros = 10,numNegOnes = 10,k = 45) == 25
    assert candidate(numOnes = 30,numZeros = 15,numNegOnes = 10,k = 45) == 30
    assert candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 35) == -5
    assert candidate(numOnes = 40,numZeros = 5,numNegOnes = 5,k = 45) == 40
    assert candidate(numOnes = 5,numZeros = 0,numNegOnes = 45,k = 10) == 0
    assert candidate(numOnes = 30,numZeros = 0,numNegOnes = 20,k = 40) == 20
    assert candidate(numOnes = 20,numZeros = 15,numNegOnes = 15,k = 30) == 20
    assert candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 49) == 49
    assert candidate(numOnes = 40,numZeros = 5,numNegOnes = 5,k = 50) == 35
    assert candidate(numOnes = 20,numZeros = 30,numNegOnes = 10,k = 50) == 20
    assert candidate(numOnes = 45,numZeros = 3,numNegOnes = 2,k = 50) == 43
    assert candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 24) == 24
    assert candidate(numOnes = 0,numZeros = 50,numNegOnes = 0,k = 25) == 0
    assert candidate(numOnes = 45,numZeros = 0,numNegOnes = 5,k = 48) == 42
    assert candidate(numOnes = 25,numZeros = 15,numNegOnes = 10,k = 50) == 15
    assert candidate(numOnes = 10,numZeros = 0,numNegOnes = 40,k = 50) == -30
    assert candidate(numOnes = 15,numZeros = 0,numNegOnes = 35,k = 20) == 10
    assert candidate(numOnes = 20,numZeros = 10,numNegOnes = 20,k = 30) == 20
    assert candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 20) == 10
    assert candidate(numOnes = 45,numZeros = 2,numNegOnes = 3,k = 45) == 45
    assert candidate(numOnes = 10,numZeros = 20,numNegOnes = 30,k = 60) == -20
    assert candidate(numOnes = 20,numZeros = 15,numNegOnes = 15,k = 40) == 15
    assert candidate(numOnes = 10,numZeros = 30,numNegOnes = 10,k = 30) == 10
    assert candidate(numOnes = 10,numZeros = 20,numNegOnes = 20,k = 30) == 10
    assert candidate(numOnes = 15,numZeros = 15,numNegOnes = 20,k = 40) == 5
    assert candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 45) == -20
    assert candidate(numOnes = 0,numZeros = 20,numNegOnes = 30,k = 40) == -20
    assert candidate(numOnes = 40,numZeros = 0,numNegOnes = 10,k = 45) == 35
    assert candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 40) == 25
    assert candidate(numOnes = 15,numZeros = 15,numNegOnes = 20,k = 20) == 15
    assert candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 30) == 30
    assert candidate(numOnes = 30,numZeros = 15,numNegOnes = 5,k = 40) == 30
    assert candidate(numOnes = 35,numZeros = 10,numNegOnes = 5,k = 45) == 35
    assert candidate(numOnes = 0,numZeros = 30,numNegOnes = 20,k = 40) == -10
    assert candidate(numOnes = 15,numZeros = 20,numNegOnes = 15,k = 25) == 15
    assert candidate(numOnes = 10,numZeros = 20,numNegOnes = 20,k = 10) == 10
    assert candidate(numOnes = 10,numZeros = 40,numNegOnes = 10,k = 60) == 0
    assert candidate(numOnes = 30,numZeros = 10,numNegOnes = 10,k = 25) == 25
    assert candidate(numOnes = 20,numZeros = 0,numNegOnes = 30,k = 30) == 10
    assert candidate(numOnes = 1,numZeros = 48,numNegOnes = 1,k = 50) == 0
    assert candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 25) == 0
    assert candidate(numOnes = 1,numZeros = 1,numNegOnes = 1,k = 3) == 0
    assert candidate(numOnes = 30,numZeros = 15,numNegOnes = 15,k = 40) == 30
    assert candidate(numOnes = 40,numZeros = 40,numNegOnes = 10,k = 60) == 40
    assert candidate(numOnes = 20,numZeros = 30,numNegOnes = 50,k = 60) == 10
    assert candidate(numOnes = 10,numZeros = 30,numNegOnes = 10,k = 40) == 10
    assert candidate(numOnes = 2,numZeros = 2,numNegOnes = 2,k = 6) == 0
    assert candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 25) == 25
    assert candidate(numOnes = 15,numZeros = 25,numNegOnes = 10,k = 20) == 15
    assert candidate(numOnes = 50,numZeros = 0,numNegOnes = 0,k = 25) == 25
    assert candidate(numOnes = 10,numZeros = 10,numNegOnes = 10,k = 25) == 5
    assert candidate(numOnes = 30,numZeros = 20,numNegOnes = 50,k = 70) == 10
    assert candidate(numOnes = 30,numZeros = 5,numNegOnes = 15,k = 40) == 25
    assert candidate(numOnes = 20,numZeros = 15,numNegOnes = 15,k = 50) == 5
    assert candidate(numOnes = 30,numZeros = 20,numNegOnes = 10,k = 40) == 30
    assert candidate(numOnes = 0,numZeros = 25,numNegOnes = 25,k = 30) == -5
    assert candidate(numOnes = 0,numZeros = 0,numNegOnes = 100,k = 50) == -50
    assert candidate(numOnes = 45,numZeros = 30,numNegOnes = 25,k = 50) == 45
    assert candidate(numOnes = 0,numZeros = 10,numNegOnes = 40,k = 20) == -10
    assert candidate(numOnes = 25,numZeros = 25,numNegOnes = 0,k = 49) == 25
    assert candidate(numOnes = 45,numZeros = 0,numNegOnes = 5,k = 35) == 35
    assert candidate(numOnes = 50,numZeros = 0,numNegOnes = 50,k = 45) == 45
    assert candidate(numOnes = 20,numZeros = 15,numNegOnes = 10,k = 30) == 20
    assert candidate(numOnes = 5,numZeros = 5,numNegOnes = 40,k = 20) == -5
    assert candidate(numOnes = 45,numZeros = 5,numNegOnes = 0,k = 45) == 45
    assert candidate(numOnes = 10,numZeros = 10,numNegOnes = 30,k = 25) == 5
    assert candidate(numOnes = 5,numZeros = 10,numNegOnes = 35,k = 50) == -30


