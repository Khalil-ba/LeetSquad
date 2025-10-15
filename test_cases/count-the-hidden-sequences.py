def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0],lower = 1,upper = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0],lower = 1,upper = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -5, 5, -5],lower = -10,upper = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -5, 5, -5],lower = -10,upper = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(differences = [3, -4, 5, 1, -2],lower = -4,upper = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [3, -4, 5, 1, -2],lower = -4,upper = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -3, 4],lower = 1,upper = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -3, 4],lower = 1,upper = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -1, -1],lower = -3,upper = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -1, -1],lower = -3,upper = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1],lower = -2,upper = -1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1],lower = -2,upper = -1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -2, -3, -4, -5],lower = -100,upper = 1) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -2, -3, -4, -5],lower = -100,upper = 1) == 87: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100000, -100000, 100000, -100000],lower = -100000,upper = 100000) == 100001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100000, -100000, 100000, -100000],lower = -100000,upper = 100000) == 100001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, -5, 15, -10],lower = -10,upper = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, -5, 15, -10],lower = -10,upper = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0],lower = 1,upper = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0],lower = 1,upper = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 1, 1],lower = -5,upper = -1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 1, 1],lower = -5,upper = -1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100000, -100000],lower = -100000,upper = 100000) == 100001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100000, -100000],lower = -100000,upper = 100000) == 100001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 2, 3],lower = 0,upper = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 2, 3],lower = 0,upper = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -2, -3],lower = -10,upper = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -2, -3],lower = -10,upper = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, -10, 10, -10],lower = -5,upper = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, -10, 10, -10],lower = -5,upper = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100000, -100000, 100000],lower = -100000,upper = 100000) == 100001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100000, -100000, 100000],lower = -100000,upper = 100000) == 100001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0],lower = 0,upper = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0],lower = 0,upper = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1],lower = 1,upper = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1],lower = 1,upper = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -2, -3],lower = -5,upper = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -2, -3],lower = -5,upper = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -1, -1],lower = 1,upper = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -1, -1],lower = 1,upper = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 2, 3, 4, 5],lower = 1,upper = 100) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 2, 3, 4, 5],lower = 1,upper = 100) == 85: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0],lower = 0,upper = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0],lower = 0,upper = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(differences = [4, -7, 2],lower = 3,upper = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [4, -7, 2],lower = 3,upper = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],lower = -15,upper = 15) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],lower = -15,upper = 15) == 21: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],lower = -10,upper = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],lower = -10,upper = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(differences = [2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 100) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 100) == 47: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10],lower = 0,upper = 500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10],lower = 0,upper = 500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, 10, 15, 20, 25, 30],lower = 0,upper = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, 10, 15, 20, 25, 30],lower = 0,upper = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1000, -500, 200, -100, 50, -25, 10],lower = -1000,upper = 1000) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1000, -500, 200, -100, 50, -25, 10],lower = -1000,upper = 1000) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100000, 0, -100000, 0, 100000, 0, -100000],lower = -200000,upper = 200000) == 300001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100000, 0, -100000, 0, 100000, 0, -100000],lower = -200000,upper = 200000) == 300001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-5, -10, -15, -20, -25, -30],lower = -100,upper = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-5, -10, -15, -20, -25, -30],lower = -100,upper = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = 0,upper = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = 0,upper = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],lower = 10,upper = 60) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],lower = 10,upper = 60) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -2, 8, -3, 7],lower = -5,upper = 20) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -2, 8, -3, 7],lower = -5,upper = 20) == 11: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10000, -20000, 30000, -40000, 50000],lower = -100000,upper = 100000) == 150001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10000, -20000, 30000, -40000, 50000],lower = -100000,upper = 100000) == 150001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, 2, -1, 2, -1],lower = -10,upper = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, 2, -1, 2, -1],lower = -10,upper = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, 0, 1, 0, -1],lower = -5,upper = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, 0, 1, 0, -1],lower = -5,upper = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -20,upper = -10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -20,upper = -10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],lower = 1,upper = 50) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],lower = 1,upper = 50) == 20: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = 0,upper = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = 0,upper = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 0,upper = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 0,upper = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [50000, -50000, 50000, -50000, 50000, -50000, 50000, -50000],lower = -100000,upper = 100000) == 150001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [50000, -50000, 50000, -50000, 50000, -50000, 50000, -50000],lower = -100000,upper = 100000) == 150001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100000, 100000, 100000, -300000, 100000, 100000, 100000],lower = -100000,upper = 100000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100000, 100000, 100000, -300000, 100000, 100000, 100000],lower = -100000,upper = 100000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, 1, -1, 1, -1],lower = 0,upper = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, 1, -1, 1, -1],lower = 0,upper = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10000, -10000, 20000, -20000],lower = -50000,upper = 50000) == 80001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10000, -10000, 20000, -20000],lower = -50000,upper = 50000) == 80001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],lower = -10,upper = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],lower = -10,upper = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-5, 10, -15, 20, -25],lower = -30,upper = 30) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-5, 10, -15, 20, -25],lower = -30,upper = 30) == 36: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 5,upper = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 5,upper = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0, 0, 0],lower = -1,upper = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0, 0, 0],lower = -1,upper = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, 2, -3, 4, -5, 6, -7, 8],lower = -10,upper = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, 2, -3, 4, -5, 6, -7, 8],lower = -10,upper = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, 2, -3, 4, -5, 6, -7],lower = -20,upper = 20) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, 2, -3, 4, -5, 6, -7],lower = -20,upper = 20) == 34: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = 0,upper = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = 0,upper = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 1,upper = 1000) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 1,upper = 1000) == 450: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -2, 3, 7, -4],lower = 1,upper = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -2, 3, 7, -4],lower = 1,upper = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],lower = -100,upper = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],lower = -100,upper = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -5, 5, -5, 5, -5],lower = -10,upper = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -5, 5, -5, 5, -5],lower = -10,upper = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0, 0, 0],lower = 1,upper = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0, 0, 0],lower = 1,upper = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, 2, -2, 1, -1],lower = -5,upper = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, 2, -2, 1, -1],lower = -5,upper = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, 20, 30, 40, 50],lower = 0,upper = 200) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, 20, 30, 40, 50],lower = 0,upper = 200) == 51: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 1,upper = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 1,upper = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [50, -25, 75, -37, 100, -50, 125, -62, 150, -75, 175, -87, 200, -93, 225, -100, 250, -112, 275, -125],lower = 0,upper = 300) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [50, -25, 75, -37, 100, -50, 125, -62, 150, -75, 175, -87, 200, -93, 225, -100, 250, -112, 275, -125],lower = 0,upper = 300) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100000, -100000, 100000, -100000, 100000],lower = -50000,upper = 50000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100000, -100000, 100000, -100000, 100000],lower = -50000,upper = 50000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],lower = -100,upper = 100) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],lower = -100,upper = 100) == 151: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -1, 1, -1, 1],lower = 1,upper = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -1, 1, -1, 1],lower = 1,upper = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -55,upper = -45) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -55,upper = -45) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -10,upper = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -10,upper = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 2, -3, 4, -5, 6],lower = 1,upper = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 2, -3, 4, -5, 6],lower = 1,upper = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100, -50, 200, -100, 50, -200, 100],lower = -1000,upper = 1000) == 1751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100, -50, 200, -100, 50, -200, 100],lower = -1000,upper = 1000) == 1751: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1],lower = -1,upper = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1],lower = -1,upper = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -2, -3, -4, -5, -6],lower = -15,upper = -5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -2, -3, -4, -5, -6],lower = -15,upper = -5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -1000,upper = 1) == 452
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -1000,upper = 1) == 452: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-15, 14, -13, 12, -11, 10, -9, 8, -7, 6, -5, 4, -3, 2, -1],lower = -20,upper = 20) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-15, 14, -13, 12, -11, 10, -9, 8, -7, 6, -5, 4, -3, 2, -1],lower = -20,upper = 20) == 26: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],lower = -10,upper = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],lower = -10,upper = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, 10, -15, 20, -25],lower = -100,upper = 100) == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, 10, -15, 20, -25],lower = -100,upper = 100) == 176: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100000, -50000, 50000, -100000, 50000],lower = -100000,upper = 100000) == 100001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100000, -50000, 50000, -100000, 50000],lower = -100000,upper = 100000) == 100001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100, -50, 25, -10, 5],lower = 0,upper = 200) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100, -50, 25, -10, 5],lower = 0,upper = 200) == 101: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],lower = -50,upper = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],lower = -50,upper = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 10,upper = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 10,upper = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 100,upper = 1000) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 100,upper = 1000) == 351: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -2, 3, -4, 1],lower = 1,upper = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -2, 3, -4, 1],lower = 1,upper = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(differences = [2, -1, 3, -2, 4, -3, 5, -4],lower = -5,upper = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [2, -1, 3, -2, 4, -3, 5, -4],lower = -5,upper = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0, 0, 0],lower = 0,upper = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0, 0, 0],lower = 0,upper = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -10,upper = -1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -10,upper = -1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -2, 3, -1, 4],lower = -5,upper = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -2, 3, -1, 4],lower = -5,upper = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100000, -50000, 25000, -12500, 6250, -3125, 1562, -781, 390, -195],lower = 0,upper = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100000, -50000, 25000, -12500, 6250, -3125, 1562, -781, 390, -195],lower = 0,upper = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-10, 20, -30, 40, -50, 60],lower = -20,upper = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-10, 20, -30, 40, -50, 60],lower = -20,upper = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-10, -20, -30, -40, -50],lower = -200,upper = 0) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-10, -20, -30, -40, -50],lower = -200,upper = 0) == 51: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, 10, -5, -10, 15, -15, 20, -20],lower = -100,upper = 100) == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, 10, -5, -10, 15, -15, 20, -20],lower = -100,upper = 100) == 181: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -10,upper = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -10,upper = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],lower = 0,upper = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],lower = 0,upper = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],lower = -50,upper = 50) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],lower = -50,upper = 50) == 91: {e}')
    
    total += 1
    try:
        result = candidate(differences = [20, -10, 30, -15, 5, -1],lower = -100,upper = 100) == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [20, -10, 30, -15, 5, -1],lower = -100,upper = 100) == 161: {e}')
    
    total += 1
    try:
        result = candidate(differences = [2, 3, -2, 1, -3, 2],lower = -5,upper = 15) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [2, 3, -2, 1, -3, 2],lower = -5,upper = 15) == 16: {e}')
    
    total += 1
    try:
        result = candidate(differences = [2, 3, -5, 2, 3, -5],lower = -3,upper = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [2, 3, -5, 2, 3, -5],lower = -3,upper = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100, -50, 25, -10, 5],lower = -20,upper = 200) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100, -50, 25, -10, 5],lower = -20,upper = 200) == 121: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100000, 0, -100000, 0, 100000],lower = 50000,upper = 150000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100000, 0, -100000, 0, 100000],lower = 50000,upper = 150000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-100000, 50000, -50000, 100000, -50000],lower = -100000,upper = 100000) == 100001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-100000, 50000, -50000, 100000, -50000],lower = -100000,upper = 100000) == 100001: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = -1,upper = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = -1,upper = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -1, 1, -1, 1, -1],lower = 1,upper = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -1, 1, -1, 1, -1],lower = 1,upper = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 2, 3, -1, -2, -3, 1, 2, 3, -1, -2, -3],lower = -5,upper = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 2, 3, -1, -2, -3, 1, 2, 3, -1, -2, -3],lower = -5,upper = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, -10, 10, -10, 10, -10, 10, -10],lower = 0,upper = 20) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, -10, 10, -10, 10, -10, 10, -10],lower = 0,upper = 20) == 11: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, -20, 30, -40, 50],lower = 5,upper = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, -20, 30, -40, 50],lower = 5,upper = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [2, 4, -6, 8, -10, 12, -14],lower = -15,upper = 15) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [2, 4, -6, 8, -10, 12, -14],lower = -15,upper = 15) == 17: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 0,upper = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 0,upper = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [10, 20, 30, 40, 50],lower = 100,upper = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [10, 20, 30, 40, 50],lower = 100,upper = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -5, 10, -10, 15, -15],lower = -50,upper = 50) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -5, 10, -10, 15, -15],lower = -50,upper = 50) == 86: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -50,upper = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -50,upper = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = -1,upper = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = -1,upper = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -2, 8, -6, 3],lower = 2,upper = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -2, 8, -6, 3],lower = 2,upper = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [100, -50, 25, -12, 6, -3, 1],lower = 0,upper = 500) == 401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [100, -50, 25, -12, 6, -3, 1],lower = 0,upper = 500) == 401: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 2, 3, 4, 5, 6],lower = 5,upper = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 2, 3, 4, 5, 6],lower = 5,upper = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],lower = -10,upper = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],lower = -10,upper = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0, 0, 0],lower = 0,upper = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0, 0, 0],lower = 0,upper = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -2, 3, -4, 7, -1],lower = -5,upper = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -2, 3, -4, 7, -1],lower = -5,upper = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(differences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 0,upper = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 0,upper = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3],lower = -50,upper = -1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3],lower = -50,upper = -1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16],lower = -100,upper = 100) == 185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16],lower = -100,upper = 100) == 185: {e}')
    
    total += 1
    try:
        result = candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],lower = -50,upper = 50) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],lower = -50,upper = 50) == 86: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -1000,upper = -100) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -1000,upper = -100) == 351: {e}')
    
    total += 1
    try:
        result = candidate(differences = [5, -2, 3, 7, -5, 8, -6],lower = -10,upper = 20) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [5, -2, 3, 7, -5, 8, -6],lower = -10,upper = 20) == 15: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],lower = -5,upper = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],lower = -5,upper = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(differences = [-1, -2, -3, -4, -5],lower = -15,upper = -5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(differences = [-1, -2, -3, -4, -5],lower = -15,upper = -5) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(differences = [0, 0, 0],lower = 1,upper = 1) == 1
    assert candidate(differences = [5, -5, 5, -5],lower = -10,upper = 10) == 16
    assert candidate(differences = [3, -4, 5, 1, -2],lower = -4,upper = 5) == 4
    assert candidate(differences = [1, -3, 4],lower = 1,upper = 6) == 2
    assert candidate(differences = [-1, -1, -1],lower = -3,upper = 3) == 4
    assert candidate(differences = [-1],lower = -2,upper = -1) == 1
    assert candidate(differences = [-1, -2, -3, -4, -5],lower = -100,upper = 1) == 87
    assert candidate(differences = [100000, -100000, 100000, -100000],lower = -100000,upper = 100000) == 100001
    assert candidate(differences = [10, -5, 15, -10],lower = -10,upper = 10) == 1
    assert candidate(differences = [0, 0, 0],lower = 1,upper = 5) == 5
    assert candidate(differences = [1, 1, 1],lower = -5,upper = -1) == 2
    assert candidate(differences = [100000, -100000],lower = -100000,upper = 100000) == 100001
    assert candidate(differences = [1, 2, 3],lower = 0,upper = 10) == 5
    assert candidate(differences = [-1, -2, -3],lower = -10,upper = 0) == 5
    assert candidate(differences = [10, -10, 10, -10],lower = -5,upper = 5) == 1
    assert candidate(differences = [100000, -100000, 100000],lower = -100000,upper = 100000) == 100001
    assert candidate(differences = [0, 0, 0],lower = 0,upper = 0) == 1
    assert candidate(differences = [1],lower = 1,upper = 2) == 1
    assert candidate(differences = [-1, -2, -3],lower = -5,upper = 5) == 5
    assert candidate(differences = [-1, -1, -1],lower = 1,upper = 5) == 2
    assert candidate(differences = [1, 2, 3, 4, 5],lower = 1,upper = 100) == 85
    assert candidate(differences = [0, 0, 0],lower = 0,upper = 10) == 11
    assert candidate(differences = [4, -7, 2],lower = 3,upper = 6) == 0
    assert candidate(differences = [2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],lower = -15,upper = 15) == 21
    assert candidate(differences = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],lower = -10,upper = 10) == 11
    assert candidate(differences = [2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 100) == 47
    assert candidate(differences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10],lower = 0,upper = 500) == 0
    assert candidate(differences = [5, 10, 15, 20, 25, 30],lower = 0,upper = 100) == 0
    assert candidate(differences = [1000, -500, 200, -100, 50, -25, 10],lower = -1000,upper = 1000) == 1001
    assert candidate(differences = [100000, 0, -100000, 0, 100000, 0, -100000],lower = -200000,upper = 200000) == 300001
    assert candidate(differences = [-5, -10, -15, -20, -25, -30],lower = -100,upper = 0) == 0
    assert candidate(differences = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = 0,upper = 2) == 2
    assert candidate(differences = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],lower = 10,upper = 60) == 1
    assert candidate(differences = [5, -2, 8, -3, 7],lower = -5,upper = 20) == 11
    assert candidate(differences = [10000, -20000, 30000, -40000, 50000],lower = -100000,upper = 100000) == 150001
    assert candidate(differences = [-1, 2, -1, 2, -1],lower = -10,upper = 10) == 18
    assert candidate(differences = [-1, 0, 1, 0, -1],lower = -5,upper = 5) == 10
    assert candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -20,upper = -10) == 0
    assert candidate(differences = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],lower = 1,upper = 50) == 20
    assert candidate(differences = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = 0,upper = 1) == 1
    assert candidate(differences = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 0,upper = 10) == 1
    assert candidate(differences = [50000, -50000, 50000, -50000, 50000, -50000, 50000, -50000],lower = -100000,upper = 100000) == 150001
    assert candidate(differences = [100000, 100000, 100000, -300000, 100000, 100000, 100000],lower = -100000,upper = 100000) == 0
    assert candidate(differences = [-1, 1, -1, 1, -1],lower = 0,upper = 5) == 5
    assert candidate(differences = [10000, -10000, 20000, -20000],lower = -50000,upper = 50000) == 80001
    assert candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],lower = -10,upper = 10) == 11
    assert candidate(differences = [-5, 10, -15, 20, -25],lower = -30,upper = 30) == 36
    assert candidate(differences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 5,upper = 5) == 1
    assert candidate(differences = [0, 0, 0, 0, 0],lower = -1,upper = 1) == 3
    assert candidate(differences = [-1, 2, -3, 4, -5, 6, -7, 8],lower = -10,upper = 10) == 13
    assert candidate(differences = [-1, 2, -3, 4, -5, 6, -7],lower = -20,upper = 20) == 34
    assert candidate(differences = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = 0,upper = 100) == 0
    assert candidate(differences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 1,upper = 1000) == 450
    assert candidate(differences = [5, -2, 3, 7, -4],lower = 1,upper = 20) == 7
    assert candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],lower = -100,upper = 0) == 0
    assert candidate(differences = [5, -5, 5, -5, 5, -5],lower = -10,upper = 10) == 16
    assert candidate(differences = [0, 0, 0, 0, 0],lower = 1,upper = 1) == 1
    assert candidate(differences = [-1, 2, -2, 1, -1],lower = -5,upper = 5) == 9
    assert candidate(differences = [10, 20, 30, 40, 50],lower = 0,upper = 200) == 51
    assert candidate(differences = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 1,upper = 10) == 0
    assert candidate(differences = [50, -25, 75, -37, 100, -50, 125, -62, 150, -75, 175, -87, 200, -93, 225, -100, 250, -112, 275, -125],lower = 0,upper = 300) == 0
    assert candidate(differences = [100000, -100000, 100000, -100000, 100000],lower = -50000,upper = 50000) == 1
    assert candidate(differences = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],lower = -100,upper = 100) == 151
    assert candidate(differences = [1, -1, 1, -1, 1],lower = 1,upper = 5) == 4
    assert candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -55,upper = -45) == 0
    assert candidate(differences = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -10,upper = 0) == 0
    assert candidate(differences = [1, 2, -3, 4, -5, 6],lower = 1,upper = 10) == 4
    assert candidate(differences = [100, -50, 200, -100, 50, -200, 100],lower = -1000,upper = 1000) == 1751
    assert candidate(differences = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1],lower = -1,upper = 1) == 2
    assert candidate(differences = [-1, -2, -3, -4, -5, -6],lower = -15,upper = -5) == 0
    assert candidate(differences = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -1000,upper = 1) == 452
    assert candidate(differences = [-15, 14, -13, 12, -11, 10, -9, 8, -7, 6, -5, 4, -3, 2, -1],lower = -20,upper = 20) == 26
    assert candidate(differences = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],lower = -10,upper = 10) == 16
    assert candidate(differences = [5, 10, -15, 20, -25],lower = -100,upper = 100) == 176
    assert candidate(differences = [100000, -50000, 50000, -100000, 50000],lower = -100000,upper = 100000) == 100001
    assert candidate(differences = [100, -50, 25, -10, 5],lower = 0,upper = 200) == 101
    assert candidate(differences = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5],lower = -50,upper = 0) == 1
    assert candidate(differences = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 10,upper = 20) == 0
    assert candidate(differences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 100,upper = 1000) == 351
    assert candidate(differences = [5, -2, 3, -4, 1],lower = 1,upper = 10) == 4
    assert candidate(differences = [2, -1, 3, -2, 4, -3, 5, -4],lower = -5,upper = 10) == 8
    assert candidate(differences = [0, 0, 0, 0, 0],lower = 0,upper = 10) == 11
    assert candidate(differences = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -10,upper = -1) == 0
    assert candidate(differences = [5, -2, 3, -1, 4],lower = -5,upper = 5) == 2
    assert candidate(differences = [100000, -50000, 25000, -12500, 6250, -3125, 1562, -781, 390, -195],lower = 0,upper = 100000) == 1
    assert candidate(differences = [-10, 20, -30, 40, -50, 60],lower = -20,upper = 20) == 0
    assert candidate(differences = [-10, -20, -30, -40, -50],lower = -200,upper = 0) == 51
    assert candidate(differences = [5, 10, -5, -10, 15, -15, 20, -20],lower = -100,upper = 100) == 181
    assert candidate(differences = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],lower = -10,upper = 0) == 1
    assert candidate(differences = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],lower = 0,upper = 50) == 1
    assert candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],lower = -50,upper = 50) == 91
    assert candidate(differences = [20, -10, 30, -15, 5, -1],lower = -100,upper = 100) == 161
    assert candidate(differences = [2, 3, -2, 1, -3, 2],lower = -5,upper = 15) == 16
    assert candidate(differences = [2, 3, -5, 2, 3, -5],lower = -3,upper = 3) == 2
    assert candidate(differences = [100, -50, 25, -10, 5],lower = -20,upper = 200) == 121
    assert candidate(differences = [100000, 0, -100000, 0, 100000],lower = 50000,upper = 150000) == 1
    assert candidate(differences = [-100000, 50000, -50000, 100000, -50000],lower = -100000,upper = 100000) == 100001
    assert candidate(differences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = -1,upper = 1) == 3
    assert candidate(differences = [1, -1, 1, -1, 1, -1],lower = 1,upper = 5) == 4
    assert candidate(differences = [1, 2, 3, -1, -2, -3, 1, 2, 3, -1, -2, -3],lower = -5,upper = 5) == 5
    assert candidate(differences = [10, -10, 10, -10, 10, -10, 10, -10],lower = 0,upper = 20) == 11
    assert candidate(differences = [10, -20, 30, -40, 50],lower = 5,upper = 15) == 0
    assert candidate(differences = [2, 4, -6, 8, -10, 12, -14],lower = -15,upper = 15) == 17
    assert candidate(differences = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],lower = 0,upper = 10) == 0
    assert candidate(differences = [10, 20, 30, 40, 50],lower = 100,upper = 200) == 0
    assert candidate(differences = [5, -5, 10, -10, 15, -15],lower = -50,upper = 50) == 86
    assert candidate(differences = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],lower = -50,upper = 0) == 0
    assert candidate(differences = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],lower = -1,upper = 1) == 2
    assert candidate(differences = [5, -2, 8, -6, 3],lower = 2,upper = 12) == 0
    assert candidate(differences = [100, -50, 25, -12, 6, -3, 1],lower = 0,upper = 500) == 401
    assert candidate(differences = [1, 2, 3, 4, 5, 6],lower = 5,upper = 15) == 0
    assert candidate(differences = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 50) == 0
    assert candidate(differences = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],lower = -10,upper = 10) == 16
    assert candidate(differences = [0, 0, 0, 0, 0],lower = 0,upper = 0) == 1
    assert candidate(differences = [5, -2, 3, -4, 7, -1],lower = -5,upper = 15) == 12
    assert candidate(differences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],lower = 0,upper = 0) == 1
    assert candidate(differences = [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3],lower = -50,upper = -1) == 20
    assert candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16],lower = -100,upper = 100) == 185
    assert candidate(differences = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],lower = -50,upper = 50) == 86
    assert candidate(differences = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],lower = -1000,upper = -100) == 351
    assert candidate(differences = [5, -2, 3, 7, -5, 8, -6],lower = -10,upper = 20) == 15
    assert candidate(differences = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],lower = -5,upper = 5) == 1
    assert candidate(differences = [-1, -2, -3, -4, -5],lower = -15,upper = -5) == 0


